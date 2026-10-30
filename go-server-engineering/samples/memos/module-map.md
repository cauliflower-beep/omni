# Memos 模块映射

基线：v0.31.0 / 2b2192d4e153bd04f1d325b60fd880cf00d68b01，核验日期 2026-10-30。定位不等于完成独立模块分析。

| 模块 | 源码 | 进度 |
| --- | --- | --- |
| 生命周期 | [cmd/memos/main.go](https://github.com/usememos/memos/blob/2b2192d4e153bd04f1d325b60fd880cf00d68b01/cmd/memos/main.go) | [已分析](../../modules/application/lifecycle/implementations/memos.md) |
| 启动装配与配置 | [cmd/memos/main.go](https://github.com/usememos/memos/blob/2b2192d4e153bd04f1d325b60fd880cf00d68b01/cmd/memos/main.go) | 已定位，专题待研究 |
| HTTP 与健康检查 | [server/server.go](https://github.com/usememos/memos/blob/2b2192d4e153bd04f1d325b60fd880cf00d68b01/server/server.go) | 已定位 |
| API 路由 | [server/api/v1/v1.go](https://github.com/usememos/memos/blob/2b2192d4e153bd04f1d325b60fd880cf00d68b01/server/api/v1/v1.go) | 已定位 |
| SSE | [server/api/v1/sse_hub.go](https://github.com/usememos/memos/blob/2b2192d4e153bd04f1d325b60fd880cf00d68b01/server/api/v1/sse_hub.go) | 已定位 |
| 上传会话 | [server/api/v1/upload_session.go](https://github.com/usememos/memos/blob/2b2192d4e153bd04f1d325b60fd880cf00d68b01/server/api/v1/upload_session.go) | 已定位 |
| 数据库/Store | [store/store.go](https://github.com/usememos/memos/blob/2b2192d4e153bd04f1d325b60fd880cf00d68b01/store/store.go) | 已定位 |
| 迁移 | [store/migrator.go](https://github.com/usememos/memos/blob/2b2192d4e153bd04f1d325b60fd880cf00d68b01/store/migrator.go) | 已定位 |
| 缓存后台工作 | [store/cache/cache.go](https://github.com/usememos/memos/blob/2b2192d4e153bd04f1d325b60fd880cf00d68b01/store/cache/cache.go) | 已定位 |

[覆盖记录](../../modules/coverage.json)；[证据清单](../../modules/application/lifecycle/implementations/memos.sources.json)。所有运行验证待开展。
