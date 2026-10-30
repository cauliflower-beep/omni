# Gitea 模块映射

基线：v28.2.0 / 829b49c1ae96015e345f9d2a0eb1ea7acd5f31e1，核验日期 2026-10-30。

| 模块 | 固定版本源码 | 关键符号 / 入口 |
| --- | --- | --- |
| 生命周期 | [modules/graceful/manager.go](https://github.com/go-gitea/gitea/blob/829b49c1ae96015e345f9d2a0eb1ea7acd5f31e1/modules/graceful/manager.go) | doShutdown / doTerminate |
| 启动装配 | [routers/init.go](https://github.com/go-gitea/gitea/blob/829b49c1ae96015e345f9d2a0eb1ea7acd5f31e1/routers/init.go) | InitWebInstalled |
| HTTP | [modules/graceful/server_http.go](https://github.com/go-gitea/gitea/blob/829b49c1ae96015e345f9d2a0eb1ea7acd5f31e1/modules/graceful/server_http.go) | newHTTPServer |
| 路由 | [routers/init.go](https://github.com/go-gitea/gitea/blob/829b49c1ae96015e345f9d2a0eb1ea7acd5f31e1/routers/init.go) | NormalRoutes |
| 数据库 | [models/db/engine_init.go](https://github.com/go-gitea/gitea/blob/829b49c1ae96015e345f9d2a0eb1ea7acd5f31e1/models/db/engine_init.go) | InitEngine / UnsetDefaultEngine |
| 迁移 | [routers/common/db.go](https://github.com/go-gitea/gitea/blob/829b49c1ae96015e345f9d2a0eb1ea7acd5f31e1/routers/common/db.go) | InitDBEngine / migrateWithSetting |
| 定时调度 | [services/cron/cron.go](https://github.com/go-gitea/gitea/blob/829b49c1ae96015e345f9d2a0eb1ea7acd5f31e1/services/cron/cron.go) | Init |
| 任务执行 | [services/cron/tasks.go](https://github.com/go-gitea/gitea/blob/829b49c1ae96015e345f9d2a0eb1ea7acd5f31e1/services/cron/tasks.go) | RunWithUser |
| 平台服务控制 | [modules/graceful/manager_unix.go](https://github.com/go-gitea/gitea/blob/829b49c1ae96015e345f9d2a0eb1ea7acd5f31e1/modules/graceful/manager_unix.go) | start / handleSignals |

[生命周期](../../modules/application/lifecycle/implementations/gitea.md) 为 analyzed；其余仅为 located。状态见[覆盖记录](../../modules/coverage.json)，不表示整个模块已分析或验证。
