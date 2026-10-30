# Gotify 样本档案

状态：生命周期第一轮静态分析完成，未运行验证。

- 产品方向：消息推送。
- 分析仓库：[gotify/server](https://github.com/gotify/server)。
- 本轮标签：v3.1.1；完整 SHA：e6361caa512547052b1013dbf4544e6d7ff32604。
- 核验日期：2026-10-30。
- go.mod 声明 Go 1.25.0；实际发行制品工具链未核验。
- 固定版本的部分源码快照位于 .cache/repos/gotify-evidence/，不提交。

## 架构认识

入口显式装配数据库与 Gin；Runner 管理 HTTP/TLS；Stream 单独管理 WebSocket。返回的清理函数只关闭 Stream，不覆盖全部后台活动。

## 证据与边界

- [生命周期带读](../../modules/application/lifecycle/implementations/gotify.md)
- [证据清单](../../modules/application/lifecycle/implementations/gotify.sources.json)
- [模块映射](module-map.md)

常规 serve：配置与数据库初始化、Gin 装配、HTTP/TLS 监听、WebSocket 与数据库清理；不完整审计插件、OIDC 与部署信号链。

未执行构建、测试、服务或退出实验；独立配置、数据、路由和业务模块仍待研究。
