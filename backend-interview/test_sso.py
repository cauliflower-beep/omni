"""Real HTTP flow checks. CookieJar is not a browser SameSite implementation."""
from concurrent.futures import ThreadPoolExecutor
from http.cookiejar import CookieJar
import re
import unittest
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlencode, urljoin, urlsplit
from urllib.request import HTTPCookieProcessor, HTTPRedirectHandler, ProxyHandler, Request, build_opener

from sso_demo import Demo


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args):
        return None


class Browser:
    def __init__(self):
        self.jar = CookieJar()
        self.opener = build_opener(ProxyHandler({}), HTTPCookieProcessor(self.jar), NoRedirect())

    def request(self, url, data=None):
        req = Request(url, data=None if data is None else urlencode(data).encode())
        try:
            response = self.opener.open(req, timeout=5)
        except HTTPError as error:
            response = error
        with response:
            return response.code, response.headers, response.read().decode()

    def follow(self, url):
        for _ in range(10):
            status, headers, body = self.request(url)
            if status not in (302, 303):
                return status, headers, body
            url = urljoin(url, headers['Location'])
        raise AssertionError('redirect loop')


class SSOTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Fixed ports are intentional: the registered callbacks must match exactly.
        cls.demo = Demo((19000, 19001, 19002)).start()

    @classmethod
    def tearDownClass(cls):
        cls.demo.stop()

    def setUp(self):
        with self.demo.lock:
            for table in self.demo.tables.values():
                table.clear()
            self.demo.password_logins = 0
        self.browser = Browser()
        self.urls = self.demo.urls

    def login_at_center(self, browser=None):
        browser = browser or self.browser
        status, _, form = browser.follow(self.urls['a'] + '/login')
        self.assertEqual(status, 200)
        csrf = re.search("name='csrf' value='([^']+)'", form)[1]
        result = browser.request(self.urls['idp'] + '/login',
                                 {'csrf': csrf, 'username': 'alice', 'password': 'demo-pass'})
        self.assertEqual(result[0], 303)
        return result[1]['Location']

    def grant(self, role='a'):
        # First log in A. Then start another transaction to capture an unused code.
        callback = self.login_at_center()
        self.assertEqual(self.browser.follow(callback)[0], 200)
        status, headers, _ = self.browser.request(self.urls[role] + '/login')
        self.assertEqual(status, 303)
        status, headers, _ = self.browser.request(headers['Location'])
        self.assertEqual(status, 303)
        callback = headers['Location']
        query = {k: v[0] for k, v in parse_qs(urlsplit(callback).query).items()}
        txn = self.demo.get('pending_' + role, query['state'])
        data = {'client_id': role, 'client_secret': self.demo.clients[role]['secret'],
                'code': query['code'], 'redirect_uri': self.demo.clients[role]['redirect_uri'],
                'code_verifier': txn['verifier']}
        return callback, data

    def test_one_password_login_for_two_apps_and_cookie_isolation(self):
        self.browser.follow(self.login_at_center())
        self.assertIn('未登录', self.browser.request(self.urls['b'])[2])
        result = self.browser.follow(self.urls['b'] + '/login')
        self.assertEqual(result[0], 200)
        self.assertIn('alice', result[2])
        self.assertEqual(self.demo.password_logins, 1)
        cookies = {c.name: c.domain for c in self.browser.jar}
        self.assertEqual(cookies['idp_sid'], '127.0.0.1')
        self.assertEqual(cookies['app_a_sid'], '127.0.0.2')
        self.assertEqual(cookies['app_b_sid'], '127.0.0.3')
        self.assertIn('未登录', Browser().request(self.urls['b'])[2])

    def test_state_tampering_and_browser_binding(self):
        callback = self.login_at_center()
        self.assertEqual(Browser().request(callback)[0], 400)
        self.assertEqual(self.browser.request(callback.replace('state=', 'state=bad'))[0], 400)
        self.assertEqual(self.browser.follow(callback)[0], 200)
        self.assertEqual(self.browser.request(callback)[0], 400)

    def test_redirect_allowlist(self):
        _, headers, _ = self.browser.request(self.urls['a'] + '/login')
        bad = headers['Location'].replace(urlencode({'redirect_uri': self.demo.clients['a']['redirect_uri']}),
                                          urlencode({'redirect_uri': 'http://attacker.invalid/callback'}))
        status, headers, _ = self.browser.request(bad)
        self.assertEqual(status, 400)
        self.assertIsNone(headers.get('Location'))

    def test_pkce_client_and_callback_binding(self):
        _, data = self.grant()
        for changes, expected in [({'code_verifier': 'wrong'}, 400),
                                  ({'client_secret': 'wrong'}, 401),
                                  ({'redirect_uri': self.urls['b'] + '/callback'}, 400),
                                  ({'client_id': 'b', 'client_secret': self.demo.clients['b']['secret']}, 400)]:
            with self.subTest(changes=list(changes)):
                self.assertEqual(Browser().request(self.urls['idp'] + '/exchange', {**data, **changes})[0], expected)
        self.assertEqual(Browser().request(self.urls['idp'] + '/exchange', data)[0], 200)
        self.assertEqual(Browser().request(self.urls['idp'] + '/exchange', data)[0], 400)

    def test_code_expiry(self):
        _, data = self.grant()
        with self.demo.lock:
            expiry, value = self.demo.tables['codes'][data['code']]
            self.demo.tables['codes'][data['code']] = (0, value)
        self.assertEqual(Browser().request(self.urls['idp'] + '/exchange', data)[0], 400)

    def test_concurrent_code_redemption(self):
        _, data = self.grant()
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: Browser().request(self.urls['idp'] + '/exchange', data)[0], range(2)))
        self.assertEqual(sorted(results), [200, 400])

    def test_local_logout_does_not_end_central_or_other_app_session(self):
        self.browser.follow(self.login_at_center())
        self.browser.follow(self.urls['b'] + '/login')
        _, _, page = self.browser.request(self.urls['a'])
        csrf = re.search("name='csrf' value='([^']+)'", page)[1]
        self.assertEqual(self.browser.request(self.urls['a'] + '/logout', {'csrf': 'bad'})[0], 400)
        self.assertEqual(self.browser.request(self.urls['a'] + '/logout', {'csrf': csrf})[0], 303)
        self.assertIn('未登录', self.browser.request(self.urls['a'])[2])
        self.assertIn('alice', self.browser.request(self.urls['b'])[2])
        self.assertIn('alice', self.browser.follow(self.urls['a'] + '/login')[2])
        self.assertEqual(self.demo.password_logins, 1)

    def test_login_csrf_and_wrong_password(self):
        _, _, form = self.browser.follow(self.urls['a'] + '/login')
        csrf = re.search("name='csrf' value='([^']+)'", form)[1]
        data = {'csrf': csrf, 'username': 'alice', 'password': 'demo-pass'}
        self.assertEqual(Browser().request(self.urls['idp'] + '/login', data)[0], 400)
        self.assertEqual(self.browser.request(self.urls['idp'] + '/login', {**data, 'password': 'wrong'})[0], 401)
        self.assertEqual(self.demo.password_logins, 0)

    def test_expired_local_session(self):
        self.browser.follow(self.login_at_center())
        with self.demo.lock:
            for key, (_, value) in self.demo.tables['local_a'].items():
                self.demo.tables['local_a'][key] = (0, value)
        self.assertIn('未登录', self.browser.request(self.urls['a'])[2])


if __name__ == '__main__':
    unittest.main(verbosity=2)
