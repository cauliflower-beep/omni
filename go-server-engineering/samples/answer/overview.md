# Apache Answer 样本档案

状态：基线已核验，生命周期完成第一轮静态分析；未构建、运行或执行退出实验。

## 产品与基线

- 产品方向：Go 后端与 Web 前端组成的问答社区。
- 规范仓库：[apache/answer](https://github.com/apache/answer)。
- 标签：v2.0.3；完整 SHA：6744295fa888e0621fc9f9a8ace04f1a4daf8554。
- 核验日期：2026-10-29。
- [固定版本源码](https://github.com/apache/answer/tree/6744295fa888e0621fc9f9a8ace04f1a4daf8554)。
- 缓存：.cache/repos/answer/，不提交。
- go.mod 声明 go 1.25.0，不代表实际发行制品的工具链已经核验。

## 架构轮廓

Cobra 选择命令，Wire 生成装配，Gin 承载路由，锁定的 Pacman 管理登记的 HTTP Server。Cron、业务队列和数据清理需单独核对接线。依据统一保存在 [生命周期分析](../../modules/application/lifecycle/implementations/answer.md)。

## 运行与边界

常规服务命令为 answer run -C <数据目录>；仓库容器脚本另依次执行 init、upgrade、run。本轮没有准备依赖、构建前后端或启动程序，这些命令不是本项目已经验证的复现步骤。业务流程、完整部署和其他模块待研究。

## 导航与记录

- [模块入口](module-map.md)
- [样本登记表](../registry.json)
- [源码证据清单](../../modules/application/lifecycle/implementations/answer.sources.json)

2026-10-29：首次固定 v2.0.3，完成生命周期第一轮静态分析；没有更早的本项目分析基线。
