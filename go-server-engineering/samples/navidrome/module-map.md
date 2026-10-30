# Navidrome 模块映射

基线：v0.64.2 / 101145742f4762164202cb4858c9126258bdc463，核验日期 2026-10-30。

| 模块 | 源码 |
| --- | --- |
| 生命周期 | [cmd/root.go](https://github.com/navidrome/navidrome/blob/101145742f4762164202cb4858c9126258bdc463/cmd/root.go) |
| HTTP | [server/server.go](https://github.com/navidrome/navidrome/blob/101145742f4762164202cb4858c9126258bdc463/server/server.go) |
| DB 初始化与迁移 | [db/db.go](https://github.com/navidrome/navidrome/blob/101145742f4762164202cb4858c9126258bdc463/db/db.go) |
| 调度 | [scheduler/scheduler.go](https://github.com/navidrome/navidrome/blob/101145742f4762164202cb4858c9126258bdc463/scheduler/scheduler.go) |
| Watcher | [scanner/watcher.go](https://github.com/navidrome/navidrome/blob/101145742f4762164202cb4858c9126258bdc463/scanner/watcher.go) |
| 扫描控制 | [scanner/controller.go](https://github.com/navidrome/navidrome/blob/101145742f4762164202cb4858c9126258bdc463/scanner/controller.go) |
| 封面 Worker | [core/artwork/worker.go](https://github.com/navidrome/navidrome/blob/101145742f4762164202cb4858c9126258bdc463/core/artwork/worker.go) |
| 服务管理 | [cmd/svc.go](https://github.com/navidrome/navidrome/blob/101145742f4762164202cb4858c9126258bdc463/cmd/svc.go) |

[生命周期](../../modules/application/lifecycle/implementations/navidrome.md) 为 analyzed；其余入口仅定位，不表示独立模块分析已完成。[覆盖记录](../../modules/coverage.json) 保存进度，运行验证均待开展。
