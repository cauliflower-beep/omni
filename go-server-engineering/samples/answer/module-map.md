# Answer 模块入口映射

基线：v2.0.3，6744295fa888e0621fc9f9a8ace04f1a4daf8554；核验日期：2026-10-29。入口定位不等于完成该模块独立分析。

| 模块 | 固定版本入口 | 状态 |
| --- | --- | --- |
| 生命周期 | [runApp](https://github.com/apache/answer/blob/6744295fa888e0621fc9f9a8ace04f1a4daf8554/cmd/main.go#L75-L104) | [第一轮静态分析](../../modules/application/lifecycle/implementations/answer.md)，analyzed |
| 启动装配 | [Wire](https://github.com/apache/answer/blob/6744295fa888e0621fc9f9a8ace04f1a4daf8554/cmd/wire_gen.go#L131-L320) | located |
| 配置 | [ReadConfig](https://github.com/apache/answer/blob/6744295fa888e0621fc9f9a8ace04f1a4daf8554/internal/base/conf/conf.go#L98-L114) | located |
| HTTP 服务 | [newApplication](https://github.com/apache/answer/blob/6744295fa888e0621fc9f9a8ace04f1a4daf8554/cmd/main.go#L97-L104) | located |
| 路由 | [NewHTTPServer](https://github.com/apache/answer/blob/6744295fa888e0621fc9f9a8ace04f1a4daf8554/internal/base/server/http.go#L36-L128) | located |
| 数据库 | [NewDB](https://github.com/apache/answer/blob/6744295fa888e0621fc9f9a8ace04f1a4daf8554/internal/base/data/data.go#L56-L95) | located |
| 定时调度 | [ScheduledTaskManager.Run](https://github.com/apache/answer/blob/6744295fa888e0621fc9f9a8ace04f1a4daf8554/internal/base/cron/cron.go#L62-L119) | located |
| 后台队列 | [通用队列](https://github.com/apache/answer/blob/6744295fa888e0621fc9f9a8ace04f1a4daf8554/internal/base/queue/queue.go#L52-L128) | located |
| 健康检查 | [healthz](https://github.com/apache/answer/blob/6744295fa888e0621fc9f9a8ace04f1a4daf8554/internal/base/server/http.go#L63-L66) | located |

[覆盖记录](../../modules/coverage.json) 是进度入口；[证据清单](../../modules/application/lifecycle/implementations/answer.sources.json) 保存版本、范围与行号。所有运行验证待开展。
