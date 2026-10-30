# 启动到退出：六项目横向比较

状态：六份固定版本的静态分析，均未运行验证。下表的证据、范围和例外以各项目正文为准，不能据一个入口推断全项目的所有任务都已纳管。

基线：[Answer v2.0.3](implementations/answer.md)、[Memos v0.31.0](implementations/memos.md)、[Navidrome v0.64.2](implementations/navidrome.md)、[Gotify v3.1.1](implementations/gotify.md)、[Gitea v28.2.0](implementations/gitea.md)、[PocketBase v0.40.6](implementations/pocketbase.md)。PocketBase 使用迁移前 GitHub 历史版本，不代表新托管仓库当前实现。

## 1. 启动成功，到底确认了什么？

| 样本 | 入口与装配 | 迁移位置 | 启动确认及运行错误 |
| --- | --- | --- | --- |
| Answer | Cobra → Wire 生成依赖 → Pacman 管理登记的 Server | 容器脚本调用独立 upgrade，不能混为 run 内步骤 | goroutine 中 ListenAndServe；返回错误进入协调 channel |
| Memos | RunE → runServer 显式构造 Driver/Store/Server | runServer 在监听前 Migrate | Start 同步 net.Listen；后续 Serve 错误只记日志，主流程等待信号 |
| Navidrome | 生成依赖构造；多个运行函数共享取消并集中等待 | db.Init 在运行组启动前迁移 | Run 同步监听并观察 50ms 错误；不是全部业务就绪屏障；组成员错误可传播，局部吞错除外 |
| Gotify | serve 拥有 DB；Router 创建 Stream；Runner 管理监听 | database.New 内 AutoMigrate 与历史字段处理 | 同步绑定 listener；异步 Serve 尝试通知退出，非阻塞发送存在早到事件丢失窗口 |
| Gitea | web → InitWebInstalled → graceful.Server | DB 初始化重试、Ping、迁移与表同步，位于正常实例监听前 | listener 包装后登记服务；监听错误返回后主链还等 Manager.Done，不能推定立刻自动退出 |
| PocketBase | Start → Execute → Bootstrap → serve 命令 / OnServe | Bootstrap 执行系统迁移；Serve 再调用 RunAllMigrations | 默认 OnServe 末端同步建立 listener；命令错误回到 Execute，扩展钩子可能截断默认流程 |

“开始提供 HTTP”与“所有业务功能准备完毕”需要分别定义。Navidrome 初始扫描并行开展，不能把监听成功当成扫描完成；Gitea 的 READY 通知基于预定 listener 槽位已处理，登记条件包括失败尝试和未使用槽位，也不能直接当成全部端口成功的证明。

## 2. 退出从哪里开始，在哪里等完？

| 样本 | 停止触发与主要等待 | HTTP / 长连接策略 | 最后的资源边界 |
| --- | --- | --- | --- |
| Answer | Pacman 接收信号、context 或登记 Server 的错误，调用 Stop | 锁定包默认一分钟 Shutdown；失败记录后继续；长期会话未完整审计 | DB 与缓存清理不共享 HTTP 期限 |
| Memos | runServer 接收信号后调用 Shutdown | 先关 SSE Hub，再用十秒 context Shutdown；失败再 Close | 再关上传管理器与 Store；根 cancel 在返回时 defer 执行，十秒不是总预算 |
| Navidrome | NotifyContext 或组成员错误触发取消；等待登记运行函数返回 | 三秒 Shutdown；超时分支未继续 Close；全部流媒体会话未完整审计 | 登记函数结束后关 DB，但有子工作未统一等待，没有全局期限 |
| Gotify | 信号 / Serve 返回尝试送达 channel，然后 Shutdown | 五秒 HTTP 等待后，入口 defer 单独关 WebSocket；未等待读写循环完成 | 再关 DB；token 定时维护未纳入停止等待；原始触发错误只记录，返回的是 Shutdown 错误 |
| Gitea | Shutdown → 运行任务等待 / Hammer → Terminate → 终止回调等待 → Manager.Done | 先关闭 listener / keep-alive，Hammer 才取消请求基础 context；连接计数清零解除等待，未逐一 Close socket | 60 秒默认值是 Hammer 升级时间；非合作任务仍可阻塞；DB 全局关闭链未获完整证明 |
| PocketBase | 信号或命令结束 → OnTerminate → 默认末端 ClearBootstrap | 先取消请求基础 context（SSE 可响应），再等待主 HTTP 一秒；忽略 Shutdown 错误，未追加 Close | 日志、Cron、DB 的默认清理依赖事件链继续；一秒和局部 WaitGroup 不覆盖所有任务 |

这里有一处关键分歧：**何时取消在途请求的 context？** Gitea 留到 Hammer 阶段，PocketBase 在 HTTP 等待前就取消，Memos 则专门通知 SSE Hub。选择取决于请求能否自然完成、长期连接如何结束，以及业务对中断的承诺；不能从名称“优雅退出”判断实际行为。

## 3. 后台工作与健康检查补上了哪些证据？

| 样本 | 后台工作接线 | 健康 / 就绪的范围 |
| --- | --- | --- |
| Answer | Cron、队列的主停止调用未找到；缓存保存循环没有停止等待 | healthz 固定响应；仓库 Helm 探针指向 /，部署行为未实测 |
| Memos | 上传清扫与三个缓存循环接入停止/等待；不代表全部异步活动已审计 | healthz 固定响应；先完成迁移与构造，但没有持续依赖检查 |
| Navidrome | Scheduler 调 Stop 未等 jobs；Watcher 子工作未统一 join；Artwork 内部有等待计数 | ping 心跳配置与 ready 日志；初始扫描并行 |
| Gotify | Stream 关闭当前连接；五分钟 token 维护循环没有停止分支 | /health 会 Ping DB，失败 500；没有排空状态，也不覆盖全部业务能力 |
| Gitea | Cron 调度器登记停止；实际 Task 接入 RunWithShutdownContext 的运行计数 | Unix 有 systemd 通知与启动超时配置；READY 条件须按 listener 槽位语义解释 |
| PocketBase | Cron.Stop 停 ticker，已启动 job 未统一等待；日志有本次阻塞刷新与异步分支 | 本轮确认监听与 banner 顺序；未据此证明全部扩展和后台工作已就绪 |

容器或服务管理器是另一层：Answer 的脚本末尾没有显式 exec，Memos 使用 exec；Navidrome 有 service 回调等待与 systemd 模板限制；Gitea 的 Unix 与 Windows 退出接口不同。这里只保留已读证据，真实进程树、信号传递与外层预算都还需要环境实验。

## 4. 能提出哪些设计判断？

这些是从六份源码提出的研究判断，尚未形成已验证脚手架准则。

**把启动划成可观察的状态。** 构造对象、绑定监听、完成迁移、业务准备完毕，各自有不同的证据。健康接口和进程管理器通知，应能解释自己代表哪个状态。

**给每个长期资源配上所有者和完成条件。** 不仅问谁创建、谁 Close，还要问谁仍在使用它、停止通知怎样送达、在哪里等返回。Memos 的 Store 责任转移与 Gitea 的运行登记是两种可对照的组织方式；Gotify 和 PocketBase 的未统一等待活动则提醒我们检查覆盖范围。

**按业务决定排空顺序。** 普通请求、SSE、WebSocket、定时任务具有不同的结束条件。数据库写入成功也不自动证明在线消息已送达客户端。

**让失败和清理都能回到入口。** 同步启动错误、运行中错误、超时与清理错误应分别追踪。Gotify 的原错误只记录、Memos 的 Serve 后续错误只记录、PocketBase 的 Shutdown 错误被忽略，都会影响外层能观察到什么。

**为整体退出预算建立单独约束。** 子阶段 timeout、Hammer 计时、连接计数归零和回调执行完毕，代表不同的事情。需要同时考虑业务最大工作时长和容器/服务管理器的外层期限。

接下来可沿四条路径检验这些判断：正常启动、启动部分失败、正常退出、退出超时或运行故障。具体入口是[优雅退出实验](../../../labs/graceful-shutdown/README.md)，实验结果产生前不将静态结论升级为 validated。
