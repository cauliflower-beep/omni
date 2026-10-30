# Navidrome 样本档案

状态：生命周期第一轮静态分析完成，未运行验证。

- 产品方向：音乐库管理与流媒体。
- 规范仓库：[navidrome/navidrome](https://github.com/navidrome/navidrome)。
- 本轮标签：v0.64.2；完整 SHA：101145742f4762164202cb4858c9126258bdc463。
- 核验日期：2026-10-30。
- go.mod 声明 Go 1.27；实际发行制品工具链未核验。
- 读取固定版本源码与目录树；部分快照 .cache/repos/navidrome-evidence/ 不提交。

## 架构认识

Cobra 进入 runNavidrome；数据库初始化/迁移后，以 errgroup 组织 HTTP、调度、扫描和封面等运行函数。Wire 生成依赖构造。g.Wait 之后登记的 DB 清理才执行，但组内函数是否等待所有子工作，仍需逐项分析。

## 证据与边界

- [生命周期带读](../../modules/application/lifecycle/implementations/navidrome.md)
- [证据清单](../../modules/application/lifecycle/implementations/navidrome.sources.json)
- [模块映射](module-map.md)

未执行构建、服务、扫描、测试、平台安装或信号实验。配置、业务模型、转码与插件等其他模块待研究。2026-10-30 为本项目首份分析基线。
