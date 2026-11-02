"""Local teaching model: code exchange + PKCE, NOT an OIDC implementation."""
import base64
import hashlib
import html
import json
import re
import secrets
import threading
import time
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import ProxyHandler, Request, build_opener


def token():
    return secrets.token_urlsafe(32)


def challenge(verifier):
    return base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()


class Demo:
    def __init__(self, ports=(9000, 9001, 9002)):
        hosts = ("127.0.0.1", "127.0.0.2", "127.0.0.3")
        self.urls = dict(zip(("idp", "a", "b"), (f"http://{h}:{p}" for h, p in zip(hosts, ports))))
        self.clients = {c: {"redirect_uri": self.urls[c] + "/callback", "secret": token()} for c in ("a", "b")}
        self.lock = threading.RLock()
        self.tables = {k: {} for k in ("central", "local_a", "local_b", "pending_a", "pending_b", "forms", "codes")}
        self.password_logins = 0
        self.servers = []

    def put(self, table, value, ttl):
        key = token()
        with self.lock:
            # Lazy cleanup is enough for this finite local experiment.
            now = time.time()
            self.tables[table] = {k: v for k, v in self.tables[table].items() if v[0] > now}
            self.tables[table][key] = (now + ttl, value)
        return key

    def get(self, table, key, consume=False):
        with self.lock:
            entry = self.tables[table].pop(key, None) if consume else self.tables[table].get(key)
            return entry[1] if entry and entry[0] > time.time() else None

    def start(self):
        try:
            for role, url in self.urls.items():
                parts = urlsplit(url)
                server = ThreadingHTTPServer((parts.hostname, parts.port), self.handler(role))
                self.servers.append(server)
                threading.Thread(target=server.serve_forever, daemon=True).start()
        except OSError:
            self.stop()
            raise
        return self

    def stop(self):
        for server in self.servers:
            server.shutdown()
            server.server_close()
        self.servers.clear()

    def handler(self, role):
        demo = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *_):
                pass  # Do not log callback codes, state, or credentials.

            def cookie(self, name):
                jar = SimpleCookie()
                try:
                    jar.load(self.headers.get("Cookie", ""))
                    return jar[name].value if name in jar else ""
                except Exception:
                    return ""

            def reply(self, status, body="", location=None, cookies=(), kind="text/html; charset=utf-8"):
                raw = body.encode()
                self.send_response(status)
                self.send_header("Content-Type", kind)
                self.send_header("Content-Length", str(len(raw)))
                self.send_header("Cache-Control", "no-store")
                self.send_header("Referrer-Policy", "no-referrer")
                if location:
                    self.send_header("Location", location)
                for name, value, ttl in cookies:
                    # HTTP is exclusively for this loopback lab; production requires Secure + TLS.
                    self.send_header("Set-Cookie", f"{name}={value}; Path=/; HttpOnly; SameSite=Lax; Max-Age={ttl}")
                self.end_headers()
                self.wfile.write(raw)

            def do_GET(self):
                self.route("GET")

            def do_POST(self):
                self.route("POST")

            def route(self, method):
                parts = urlsplit(self.path)
                if method == "POST":
                    size = int(self.headers.get("Content-Length", "0"))
                    if size > 8192:
                        return self.reply(413, "body too large")
                    raw = self.rfile.read(size).decode()
                else:
                    raw = parts.query
                params = parse_qs(raw, keep_blank_values=True)
                if any(len(v) != 1 for v in params.values()):
                    return self.reply(400, "duplicate parameter")
                q = {k: v[0] for k, v in params.items()}
                if role == "idp":
                    return self.idp(method, parts.path, q)
                return self.client(method, parts.path, q)

            def issue(self, q, user, cookies=()):
                code = demo.put("codes", {**q, "sub": user}, 30)
                return self.reply(303, location=q["redirect_uri"] + "?" + urlencode({"code": code, "state": q["state"]}), cookies=cookies)

            def idp(self, method, path, q):
                if method == "GET" and path == "/authorize":
                    client = demo.clients.get(q.get("client_id"))
                    if (not client or q.get("redirect_uri") != client["redirect_uri"]
                            or q.get("response_type") != "code" or not q.get("state")
                            or q.get("code_challenge_method") != "S256"
                            or not re.fullmatch(r"[A-Za-z0-9_-]{43}", q.get("code_challenge", ""))):
                        return self.reply(400, "invalid authorization request")
                    user = demo.get("central", self.cookie("idp_sid"))
                    if user:
                        return self.issue(q, user)
                    csrf = demo.put("forms", q, 300)
                    form = ("<!doctype html><meta charset='utf-8'><h1>认证中心</h1>"
                            "<p>演示账号 alice / demo-pass</p><form method='post' action='/login'>"
                            f"<input type='hidden' name='csrf' value='{csrf}'>"
                            "<label>用户名<input name='username' autocomplete='username'></label>"
                            "<label>密码<input name='password' type='password' autocomplete='current-password'></label>"
                            "<button>登录</button></form>")
                    return self.reply(200, form, cookies=[("login_csrf", csrf, 300)])
                if method == "POST" and path == "/login":
                    csrf = q.get("csrf", "")
                    if not csrf or not secrets.compare_digest(csrf, self.cookie("login_csrf")):
                        return self.reply(400, "invalid login csrf")
                    auth = demo.get("forms", csrf)
                    if not auth:
                        return self.reply(400, "expired login form")
                    if q.get("username") != "alice" or q.get("password") != "demo-pass":
                        return self.reply(401, "invalid credentials; go back and retry")
                    # Consume once, even if concurrent login submissions arrive.
                    auth = demo.get("forms", csrf, consume=True)
                    if not auth:
                        return self.reply(400, "used login form")
                    with demo.lock:
                        demo.password_logins += 1
                    sid = demo.put("central", "alice", 3600)
                    return self.issue(auth, "alice", [("idp_sid", sid, 3600), ("login_csrf", "", 0)])
                if method == "POST" and path == "/exchange":
                    client = demo.clients.get(q.get("client_id"))
                    if not client or not secrets.compare_digest(q.get("client_secret", ""), client["secret"]):
                        return self.reply(401, "invalid client")
                    # Validate and consume under one lock: only one redemption can succeed.
                    with demo.lock:
                        auth = demo.get("codes", q.get("code", ""))
                        if (not auth or auth["client_id"] != q.get("client_id")
                                or auth["redirect_uri"] != q.get("redirect_uri")
                                or challenge(q.get("code_verifier", "")) != auth["code_challenge"]):
                            return self.reply(400, "invalid grant")
                        demo.get("codes", q["code"], consume=True)
                    return self.reply(200, json.dumps({"sub": auth["sub"], "issuer": demo.urls["idp"]}), kind="application/json")
                return self.reply(404, "not found")

            def client(self, method, path, q):
                sid_name, txn_name = f"app_{role}_sid", f"txn_{role}"
                if method == "GET" and path == "/login":
                    verifier = token()
                    state = demo.put("pending_" + role, {"verifier": verifier}, 300)
                    auth = {"response_type": "code", "client_id": role,
                            "redirect_uri": demo.clients[role]["redirect_uri"], "state": state,
                            "code_challenge": challenge(verifier), "code_challenge_method": "S256"}
                    return self.reply(303, location=demo.urls["idp"] + "/authorize?" + urlencode(auth), cookies=[(txn_name, state, 300)])
                if method == "GET" and path == "/callback":
                    state = q.get("state", "")
                    if not state or not secrets.compare_digest(state, self.cookie(txn_name)):
                        return self.reply(400, "invalid state")
                    txn = demo.get("pending_" + role, state, consume=True)
                    if not txn:
                        return self.reply(400, "expired or used state")
                    data = {"client_id": role, "client_secret": demo.clients[role]["secret"],
                            "redirect_uri": demo.clients[role]["redirect_uri"], "code": q.get("code", ""),
                            "code_verifier": txn["verifier"]}
                    try:
                        req = Request(demo.urls["idp"] + "/exchange", data=urlencode(data).encode())
                        with build_opener(ProxyHandler({})).open(req, timeout=3) as response:
                            identity = json.load(response)
                        if identity.get("issuer") != demo.urls["idp"] or not identity.get("sub"):
                            raise ValueError("invalid identity")
                    except (HTTPError, URLError, TimeoutError, ValueError):
                        return self.reply(502, "identity exchange failed")
                    # Rotate the local session on successful authentication.
                    demo.get("local_" + role, self.cookie(sid_name), consume=True)
                    sid = demo.put("local_" + role, identity["sub"], 600)
                    return self.reply(303, location="/", cookies=[(sid_name, sid, 600), (txn_name, "", 0)])
                user = demo.get("local_" + role, self.cookie(sid_name))
                if method == "POST" and path == "/logout":
                    if not user or not secrets.compare_digest(q.get("csrf", ""), self.cookie(sid_name)):
                        return self.reply(400, "invalid logout csrf")
                    demo.get("local_" + role, self.cookie(sid_name), consume=True)
                    return self.reply(303, location="/", cookies=[(sid_name, "", 0)])
                if method == "GET" and path == "/":
                    other = "b" if role == "a" else "a"
                    body = f"<!doctype html><meta charset='utf-8'><h1>应用 {role.upper()}</h1>"
                    body += f"<p>当前用户：{html.escape(user or '未登录')}</p>"
                    body += f"<p><a href='{demo.urls[other]}'>访问应用 {other.upper()}</a></p>"
                    if user:
                        body += ("<form method='post' action='/logout'>"
                                 f"<input type='hidden' name='csrf' value='{html.escape(self.cookie(sid_name))}'>"
                                 "<button>仅退出本应用</button></form>")
                    else:
                        body += "<a href='/login'>统一登录</a>"
                    return self.reply(200, body)
                return self.reply(404, "not found")

        return Handler


if __name__ == "__main__":
    instance = Demo().start()
    for name, url in instance.urls.items():
        print(f"{name}: {url}", flush=True)
    print("Demo only. alice / demo-pass. Ctrl+C to stop.", flush=True)
    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        pass
    finally:
        instance.stop()
