# 服务从启动到退出

阅读主线：通用流程 → 项目实现 → 横向比较 → 实践。

六个计划样本的第一轮固定版本静态分析已完成，尚未运行实验。

## 正文

1. [通用模型与四条路径](foundations.md)：正常启动、启动失败、正常退出、异常终止。
2. [Answer v2.0.3](implementations/answer.md)：依赖装配、HTTP 协调与数据清理。
3. [Memos v0.31.0](implementations/memos.md)：Store 所有权、SSE 与分阶段退出。
4. [Navidrome v0.64.2](implementations/navidrome.md)：服务协作、扫描调度与后台任务收尾。
5. [Gotify v3.1.1](implementations/gotify.md)：HTTP 与 WebSocket 分开收尾、消息持久化与送达边界。
6. [Gitea v28.2.0](implementations/gitea.md)：分阶段退出、连接计数与后台任务登记。
7. [PocketBase v0.40.6](implementations/pocketbase.md)：事件链、主 HTTP/SSE 与底座清理；迁移前 GitHub 历史基线。
8. [六项目横向比较](comparison.md)：对照启动确认、错误传播、停止、等待与依赖释放。

## 配套资料

- [来源与适用边界](sources.md)
- [源码带读提纲](reading-guide.md)
- [实践准则](practice.md)：待实验后整理。
- [覆盖进度](../../matrix.md)

具体的配置、路由和健康检查分别在对应模块展开，本主题只解释它们参与生命周期的方式。
