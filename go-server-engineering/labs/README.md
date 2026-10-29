# 可复现实验

每个实验隔离一个问题，记录环境、依赖版本、完整命令、预期、实际结果和边界。当前只占位，没有可执行代码或测量结果。

- [优雅退出](graceful-shutdown/README.md)：观察停止接收请求、在途请求处理、后台任务取消与资源关闭的顺序。
- [errgroup 取消传播](errgroup-cancellation/README.md)：观察一个任务失败后，取消、其他任务响应和错误返回之间的关系。
- [有界并发](bounded-concurrency/README.md)：比较任务数量、并发上限、等待与取消的行为，不预设必须使用协程池。
- [事务边界](transaction-boundaries/README.md)：观察成功、业务失败和超时情况下的提交、回滚与资源释放。

code/ 放实验代码，results/ 放脱敏的实际结果；需要 Go 代码时在各实验 code/ 内独立初始化 module。实验依赖不会自动加入未来业务项目或脚手架。

使用 [实验模板](../templates/lab.md)。概念演示放在 website/src/demos/，实验结果从此处链接，不用动画代替验证。
