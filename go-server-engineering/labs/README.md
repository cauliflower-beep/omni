# 可复现实验

每个实验隔离一个问题，记录环境、依赖版本、完整命令、预期、实际结果和边界。当前只占位，没有可执行代码或测量结果。

## 服务器行为实验

- [优雅退出](graceful-shutdown/README.md)：请求、后台工作和资源关闭的协作。
- [事务边界](transaction-boundaries/README.md)：成功、失败和中断下的数据行为。

## 独立专题实验（按需）

- [errgroup](errgroup-cancellation/README.md)
- [有界并发](bounded-concurrency/README.md)

这些是可选实验占位，不要求每个服务器主题都使用或验证这些工具。

code/ 放实验代码，results/ 放脱敏的实际结果；需要 Go 代码时在各实验 code/ 内独立初始化 module。实验依赖不会自动加入未来业务项目或脚手架。

使用 [实验模板](../templates/lab.md)。概念演示放在 website/src/demos/，实验结果从此处链接，不用动画代替验证。
