# 生命周期资料：来源、用途与边界

核验日期：2026-10-29。均为实际打开并读取的资料；网页采用核验当日在线版本，链接内容以后可能变化。正文使用自己的归纳，不转载原文、整篇论文或图表。

## 阅读顺序

先读 Twelve-Factor 的工程目标，再理解就绪与存活的区别，然后结合平台终止流程和协议语义，最后用 crash-only 的思想审查异常终止。

| 来源 | 类型与定位 | 支持的论点 | 不能替它声称什么 |
| --- | --- | --- | --- |
| [The Twelve-Factor App — IX. Disposability](https://12factor.net/disposability) | 原作者工程方法论；页面署名 Adam Wiggins，标注最后更新 2017 | 快速启动、优雅退出、Web 与任务工作器的区别 | 不是所有服务器的规范；Web 讨论有短请求等假设 |
| [Kubernetes — Probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/) | 平台官方文档；Types of probe | startup/liveness/readiness 职责与行为差别 | 探针存在不等于应用具备完整恢复能力；不适用于所有部署平台 |
| [Kubernetes — Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-flow) | 平台官方文档；Termination of Pods 与 Pod Termination Flow | 宽限期、preStop、信号、端点变化和强制终止 | 控制面与节点动作不是同步屏障；不保证零错误退出 |
| [systemd — sd_notify](https://www.freedesktop.org/software/systemd/man/latest/sd_notify.html) | 服务管理器官方接口文档；READY=1、STOPPING=1 | 应用向管理器报告启动完成、开始停止 | 特定服务类型的接口，不是通用协议，也不能假设 READY=0 对称存在 |
| [Linux man-pages — signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html) | Linux 手册原始维护站点；Signal dispositions 与 Standard signals | 信号默认动作，以及 SIGKILL 无法捕获、阻塞、忽略 | 本文不据此推导 Windows 服务通知语义 |
| [Docker — container stop](https://docs.docker.com/reference/cli/docker/container/stop/) | 平台官方命令文档；Description、signal、timeout | 停止信号和超时后的强制终止可配置 | 某个默认超时不是所有环境推荐值 |
| [RFC 9112 — HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112.html#section-9.6) | IETF Standards Track，2022；§9.3 Persistence、§9.6 Tear-down | 持久连接与 Connection: close 的连接关闭语义 | 连接关闭不是完整应用生命周期，不自动覆盖任务和其他协议 |
| [RFC 9113 — HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html#section-6.8) | IETF Standards Track，2022；§6.8 GOAWAY | 停止新流与完成已有流可以区分 | 不保证业务请求都成功，也不代表所有框架实现相同 |
| [Candea & Fox — Crash-Only Software](https://www.usenix.org/legacy/events/hotos03/tech/full_papers/candea/candea.pdf) | HotOS IX，2003，原始论文；§1、§3 | 崩溃安全、恢复、状态隔离与组件协作的研究视角 | 不是要求任意系统以强杀替代正常退出；历史产品实例不能视为当代实现事实 |

## 证据如何使用

- 平台行为由相应官方文档支持；协议语义由 RFC 支持；研究思想按论文的假设与范围理解。
- [正文](foundations.md) 的三方协作框架、四条路径、资源依赖示例与退出预算示例，属于综合归纳或假设，不宣称是某份文献的逐条原结论。
- 资料没有证明 Answer、Memos 等样本采用了某种实现。样本结论必须另附固定 SHA 的源码证据。
