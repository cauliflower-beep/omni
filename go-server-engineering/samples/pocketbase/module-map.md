# PocketBase 模块映射

基线：v0.40.6 / 9d281ccaba65f2686eb7b0b614ccda72d1116a1b，核验日期 2026-10-30。

仅对应迁移前 GitHub 历史版本；规范仓库地址见[样本档案](overview.md)。

| 模块 | 固定版本源码 | 关键符号 / 入口 |
| --- | --- | --- |
| 生命周期 | [pocketbase.go](https://github.com/pocketbase/pocketbase/blob/9d281ccaba65f2686eb7b0b614ccda72d1116a1b/pocketbase.go) | Execute |
| 启动装配 | [core/base.go](https://github.com/pocketbase/pocketbase/blob/9d281ccaba65f2686eb7b0b614ccda72d1116a1b/core/base.go) | Bootstrap / ClearBootstrap |
| HTTP | [apis/serve.go](https://github.com/pocketbase/pocketbase/blob/9d281ccaba65f2686eb7b0b614ccda72d1116a1b/apis/serve.go) | Serve |
| apis 路由装配 | [apis/serve.go](https://github.com/pocketbase/pocketbase/blob/9d281ccaba65f2686eb7b0b614ccda72d1116a1b/apis/serve.go) | NewRouter 调用 / OnServe 构建 mux |
| SSE | [apis/realtime.go](https://github.com/pocketbase/pocketbase/blob/9d281ccaba65f2686eb7b0b614ccda72d1116a1b/apis/realtime.go) | realtimeConnect |
| 数据库 | [core/base.go](https://github.com/pocketbase/pocketbase/blob/9d281ccaba65f2686eb7b0b614ccda72d1116a1b/core/base.go) | initDataDB / initAuxDB / ClearBootstrap |
| 迁移 | [apis/serve.go](https://github.com/pocketbase/pocketbase/blob/9d281ccaba65f2686eb7b0b614ccda72d1116a1b/apis/serve.go) | RunAllMigrations 调用 |
| 定时调度 | [tools/cron/cron.go](https://github.com/pocketbase/pocketbase/blob/9d281ccaba65f2686eb7b0b614ccda72d1116a1b/tools/cron/cron.go) | Start / Stop / runDue |

[生命周期](../../modules/application/lifecycle/implementations/pocketbase.md) 为 analyzed；其余仅为 located。状态见[覆盖记录](../../modules/coverage.json)，不表示整个模块已分析或验证。
