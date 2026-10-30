# Gotify 模块映射

基线：v3.1.1 / e6361caa512547052b1013dbf4544e6d7ff32604，核验日期 2026-10-30。

| 模块 | 固定版本源码 | 关键符号 / 入口 |
| --- | --- | --- |
| 生命周期 | [app.go](https://github.com/gotify/server/blob/e6361caa512547052b1013dbf4544e6d7ff32604/app.go) | serve → runner.Run |
| 启动装配 | [app.go](https://github.com/gotify/server/blob/e6361caa512547052b1013dbf4544e6d7ff32604/app.go) | serve / router.Create |
| HTTP/TLS | [runner/runner.go](https://github.com/gotify/server/blob/e6361caa512547052b1013dbf4544e6d7ff32604/runner/runner.go) | Run / startListening |
| 路由 | [router/router.go](https://github.com/gotify/server/blob/e6361caa512547052b1013dbf4544e6d7ff32604/router/router.go) | Create |
| WebSocket | [api/stream/stream.go](https://github.com/gotify/server/blob/e6361caa512547052b1013dbf4544e6d7ff32604/api/stream/stream.go) | Handle / Close |
| 数据库 | [database/database.go](https://github.com/gotify/server/blob/e6361caa512547052b1013dbf4544e6d7ff32604/database/database.go) | New / Close |
| 迁移 | [database/database.go](https://github.com/gotify/server/blob/e6361caa512547052b1013dbf4544e6d7ff32604/database/database.go) | New 中的 AutoMigrate |
| 定时维护 | [router/router.go](https://github.com/gotify/server/blob/e6361caa512547052b1013dbf4544e6d7ff32604/router/router.go) | 五分钟 ticker |
| 健康检查 | [api/health.go](https://github.com/gotify/server/blob/e6361caa512547052b1013dbf4544e6d7ff32604/api/health.go) | Health |

[生命周期](../../modules/application/lifecycle/implementations/gotify.md) 为 analyzed；其余仅为 located。状态见[覆盖记录](../../modules/coverage.json)，不表示整个模块已分析或验证。
