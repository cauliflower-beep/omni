# PocketBase 样本档案

状态：生命周期第一轮静态分析完成，未运行验证。

- 产品方向：可嵌入的实时后端与管理界面。
- 分析仓库：[pocketbase/pocketbase](https://github.com/pocketbase/pocketbase)。
- 本轮标签：v0.40.6；完整 SHA：9d281ccaba65f2686eb7b0b614ccda72d1116a1b。
- 核验日期：2026-10-30。
- go.mod 声明 Go 1.27；实际发行制品工具链未核验。
- 固定版本的部分源码快照位于 .cache/repos/pocketbase-evidence/，不提交。

该项目已迁往[新托管地址](https://ganigeorgiev.com/pocketbase/pocketbase)；本篇使用旧 GitHub 仓库中的历史版本，不代表新仓库当前实现。归档不代表停止开发。

## 架构认识

Start/Execute 管理命令与退出；Bootstrap 建立底座；Serve 和 ClearBootstrap 通过事件链组织 HTTP、日志、Cron 与 DB。扩展处理器必须遵守 Next 契约。

## 证据与边界

- [生命周期带读](../../modules/application/lifecycle/implementations/pocketbase.md)
- [证据清单](../../modules/application/lifecycle/implementations/pocketbase.sources.json)
- [模块映射](module-map.md)

迁移前 GitHub v0.40.6 历史基线：Go 扩展入口、Bootstrap/Execute、主 HTTP/SSE、事件链、Cron、日志和 DB 清理。不代表新托管仓库当前实现，不完整审计 JS 插件、备份和所有异步任务。

未执行构建、测试、服务或退出实验；独立配置、数据、路由和业务模块仍待研究。
