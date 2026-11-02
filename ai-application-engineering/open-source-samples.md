# 开源完整项目与源码学习样本

## 怎么选

Python 路径：原生模型接口 → LangGraph → Dify。Go 路径：原生模型接口 → Eino → WeKnora 或 Coze Studio。复杂文档解析选 RAGFlow。

完整产品：WeKnora、Coze Studio、Dify、RAGFlow。框架与机制示例：Eino、Eino Examples。

核查范围：仓库文档、模块、目录和元数据；运行验证待开展。部署成本按依赖数量与配置复杂度估计。

| 样本 | 主要学习价值 | 当前核查的技术情况 | 学习部署成本 | 建议角色 |
| --- | --- | --- | --- | --- |
| [WeKnora](https://github.com/Tencent/WeKnora) | 文档接入、检索、引用、Agent 与多工作区 | Go 服务，`go.mod` 为 1.26.0，有前端和 Compose | 中 | Go 知识应用样本 |
| [Coze Studio](https://github.com/coze-dev/coze-studio) | 工作流、插件、知识、发布与运行 | Go 后端与 React/TypeScript，模块要求 Go 1.24.0 | 中高 | Go 工作流样本 |
| [Dify](https://github.com/langgenius/dify) | 平台产品、模型插件、RAG 与应用运行 | Python API 与 Web，当前 `pyproject.toml` 要求约束为 `~=3.13.0` | 中高 | Python 完整产品样本 |
| [RAGFlow](https://github.com/infiniflow/ragflow) | 复杂文档、解析、检索与引用 | 当前主分支已有 Go 服务，Go 1.27 与原生库依赖 | 高 | 文档解析专项 |
| [Eino Examples](https://github.com/cloudwego/eino-examples) | 组件、编排、工具循环、流式和中断 | Go 示例；含有服务和 Web UI 的 `eino_assistant` | 低至中 | 机制实验入口 |

## 固定版本和发布信息

源码入口固定到主分支 SHA，发布标签单独登记；两者的功能与依赖可能不同。完整元数据见 [samples.json](data/samples.json)。

| 仓库 | 研究 SHA | 提交日期 UTC | GitHub latest 返回的发布标签 | 发布日期 UTC |
| --- | --- | --- | --- | --- |
| Tencent/WeKnora | `40192ace214ca046a86b590d69c1fe7286f3423e` | 2026-10-29 | [v0.9.0](https://github.com/Tencent/WeKnora/releases/tag/v0.9.0) | 2026-10-29 |
| coze-dev/coze-studio | `fefb05ff27be1da939612fbf9faf5db62583b8ae` | 2026-07-29 | [v0.5.1](https://github.com/coze-dev/coze-studio/releases/tag/v0.5.1) | 2026-02-05 |
| langgenius/dify | `adcc9a40bdfa5b7c5afb2b54f3efe333855d4541` | 2026-10-30 | [1.18.0](https://github.com/langgenius/dify/releases/tag/1.18.0) | 2026-10-23 |
| infiniflow/ragflow | `aaa8e05354f1a24256cdc1780bfb938e60c9411e` | 2026-10-30 | [v1.0.0-rc2](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0-rc2) | 2026-10-16 |
| cloudwego/eino-examples | `00ad7425513ff231b7467e88f5eeecde3c440bed` | 2026-10-27 | 本轮未查询发布版 | — |

RAGFlow 标签带 `rc2`，应按候选版本对待；虽然 GitHub latest 元数据的 `prerelease` 是 false，也不据此把它称为稳定版。Coze 的发布与主分支更新日期明显早于本次调研，应在选定部署日重新检查维护与安全状态。

## WeKnora Go 知识应用样本

选择理由：具备文档接入、检索、引用和应用服务的完整链路，适合研究 Go 知识应用的工程实现。当前 README 介绍了知识问答、Agent 与 Wiki 三条产品路径；第一轮只研究文档问答，避免功能面过大。[固定 README](https://github.com/Tencent/WeKnora/blob/40192ace214ca046a86b590d69c1fe7286f3423e/README.md)

已核验目录入口：

- [cmd/server](https://github.com/Tencent/WeKnora/tree/40192ace214ca046a86b590d69c1fe7286f3423e/cmd/server)：从服务入口追依赖。
- [internal/router](https://github.com/Tencent/WeKnora/tree/40192ace214ca046a86b590d69c1fe7286f3423e/internal/router)、[internal/handler](https://github.com/Tencent/WeKnora/tree/40192ace214ca046a86b590d69c1fe7286f3423e/internal/handler)：定位文档上传与问答接口。
- [internal/application](https://github.com/Tencent/WeKnora/tree/40192ace214ca046a86b590d69c1fe7286f3423e/internal/application)、[internal/reranking](https://github.com/Tencent/WeKnora/tree/40192ace214ca046a86b590d69c1fe7286f3423e/internal/reranking)：追索引、检索和重排的协作。
- [internal/agent](https://github.com/Tencent/WeKnora/tree/40192ace214ca046a86b590d69c1fe7286f3423e/internal/agent)、[internal/mcpserver](https://github.com/Tencent/WeKnora/tree/40192ace214ca046a86b590d69c1fe7286f3423e/internal/mcpserver)：第二轮再看工具与对外集成。

源码问题：文件如何成为检索片段？版本与文档 ID 怎么关联？权限在哪层过滤？检索证据如何进入模型与 UI 引用？更新失败如何恢复？

部署练习：导入 20 份来源清楚的技术文档，提 10 个有答案的问题、5 个资料外问题；更新一份文档、删除一份文档，再测试两个账号或工作区的数据边界。改造选题首选文档版本过滤或检索评估导出。

许可证文件声明主体采用 MIT，并列出第三方组件的独立条款；不要只看仓库徽章或 GitHub 的自动识别结果。[固定许可证](https://github.com/Tencent/WeKnora/blob/40192ace214ca046a86b590d69c1fe7286f3423e/LICENSE)

## Coze Studio 工作流与工具样本

适合观察“可视化画布上的节点如何变成实际执行过程”，以及模型、插件、知识、会话如何组合。其 README 确认 Go 后端使用 Eino 等组件；云端 Coze 的文档和商业功能不能直接等同于开源版本。[固定 README](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md)

已核验入口：[backend/api](https://github.com/coze-dev/coze-studio/tree/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/api)、[backend/application](https://github.com/coze-dev/coze-studio/tree/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/application)、[backend/domain/workflow](https://github.com/coze-dev/coze-studio/tree/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/domain/workflow)、[backend/domain/plugin](https://github.com/coze-dev/coze-studio/tree/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/domain/plugin)、[backend/domain/knowledge](https://github.com/coze-dev/coze-studio/tree/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/domain/knowledge)。

部署练习：做“文档输入 → 信息抽取 → 规则判断 → 人工确认 → 模拟工单”流程；观察节点输入输出、超时、失败和运行历史。改造选题为自己的只读 HTTP 插件或节点错误可观察性。

README 给出的起步最低配置为 2 核、4 GB，不含本地大模型的额外消耗。Windows 入口是复制 `docker/.env.example` 后使用 `docker/docker-compose.yml`；默认 UI 为 8888 端口。[Apache 2.0 文件](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/LICENSE-APACHE)

## Dify Python 产品与平台对照

适合从产品层理解模型管理、知识流水线、工作流、应用 API 和运行观测，也可作为 Python 服务代码的深读样本。完成同一需求后，与练习实现比较交付速度、调试透明度和定制成本。[固定 README](https://github.com/langgenius/dify/blob/adcc9a40bdfa5b7c5afb2b54f3efe333855d4541/README.md)

已核验入口：[api/core/app](https://github.com/langgenius/dify/tree/adcc9a40bdfa5b7c5afb2b54f3efe333855d4541/api/core/app)、[api/core/workflow](https://github.com/langgenius/dify/tree/adcc9a40bdfa5b7c5afb2b54f3efe333855d4541/api/core/workflow)、[api/core/rag](https://github.com/langgenius/dify/tree/adcc9a40bdfa5b7c5afb2b54f3efe333855d4541/api/core/rag)、[api/core/plugin](https://github.com/langgenius/dify/tree/adcc9a40bdfa5b7c5afb2b54f3efe333855d4541/api/core/plugin)。

部署练习：用相同 20 份文档和同一模型搭建知识应用，以 API 接到 Python 或 Go 业务服务；比较 10 个固定问题，追踪一次失败。改造方向为数据连接或评估接入，不先重写整个平台。

README 给出最低 2 核、4 GiB 和 Docker Compose 入口；当前源代码的 Python 要求应以[模块声明](https://github.com/langgenius/dify/blob/adcc9a40bdfa5b7c5afb2b54f3efe333855d4541/api/pyproject.toml)为准，避免照搬旧 Python 版本教程。许可证是 Dify 自定义条款、基于 Apache 2.0 并有附加条件，涉及多租户和前端标识；按选定版本阅读原文，不能标成纯 Apache 2.0。[固定 LICENSE](https://github.com/langgenius/dify/blob/adcc9a40bdfa5b7c5afb2b54f3efe333855d4541/LICENSE)

## RAGFlow 复杂文档专项

适合第二轮深入 PDF、表格、版面结构和解析质量。若输入主要是 Markdown，第一轮无需承担整套依赖。[固定 README](https://github.com/infiniflow/ragflow/blob/aaa8e05354f1a24256cdc1780bfb938e60c9411e/README.md)

已核验入口：[internal/parser](https://github.com/infiniflow/ragflow/tree/aaa8e05354f1a24256cdc1780bfb938e60c9411e/internal/parser)、[internal/ingestion](https://github.com/infiniflow/ragflow/tree/aaa8e05354f1a24256cdc1780bfb938e60c9411e/internal/ingestion)、[internal/rag](https://github.com/infiniflow/ragflow/tree/aaa8e05354f1a24256cdc1780bfb938e60c9411e/internal/rag)、[internal/agentic_rag](https://github.com/infiniflow/ragflow/tree/aaa8e05354f1a24256cdc1780bfb938e60c9411e/internal/agentic_rag)。

部署练习：同一份带表格 PDF，比较普通文本抽取和版面感知解析，人工标注 30 个关键字段或证据位置；检查解析、切分、检索三层各自丢失了什么。

当前 README 建议起步 4 核、16 GB 内存、50 GB 磁盘，实际随数据和并发变化；源码构建需 Go 1.27、CGO 相关原生库等，优先使用其候选发布版的容器说明。Windows 容器宿主、WSL2 内核参数和镜像平台需要在真正部署时验证。[go.mod](https://github.com/infiniflow/ragflow/blob/aaa8e05354f1a24256cdc1780bfb938e60c9411e/go.mod)、[Apache 2.0 文件](https://github.com/infiniflow/ragflow/blob/aaa8e05354f1a24256cdc1780bfb938e60c9411e/LICENSE)

## Eino Examples 机制学习入口

先从 `quickstart/chatwitheino` 按组件、状态、工具、观测和中断逐项练习，再阅读 `quickstart/eino_assistant` 的服务与知识索引入口。后者当前示例依赖 Redis 与模型服务，其旧模型推荐仅用来理解配置，实际模型可用性另查供应商当前文档。[固定示例目录](https://github.com/cloudwego/eino-examples/tree/00ad7425513ff231b7467e88f5eeecde3c440bed/quickstart/eino_assistant)、[README](https://github.com/cloudwego/eino-examples/blob/00ad7425513ff231b7467e88f5eeecde3c440bed/README.md)

练习不是复制后即结束：替换文档源、增加一个工具超时、观察流式取消，再写出引入框架前后的差异。框架的编排与中断能力不自动证明业务写操作幂等。[Apache 2.0 文件](https://github.com/cloudwego/eino-examples/blob/00ad7425513ff231b7467e88f5eeecde3c440bed/LICENSE-APACHE)

## 第一次落地的操作配方

WeKnora 部署步骤，待运行验证。准备 Docker daemon、空闲端口、模型 Key 与存储空间，使用本地或学习内网环境。

在独立样本工作目录执行 PowerShell 命令，避免与自己的实现混在一起：

```powershell
git clone https://github.com/Tencent/WeKnora.git
Set-Location WeKnora
git checkout --detach 40192ace214ca046a86b590d69c1fe7286f3423e
Copy-Item -LiteralPath .env.example -Destination .env
```

编辑 `.env`，按该快照配置模型和基础服务；若使用发布镜像，将 `WEKNORA_VERSION` 固定为 `0.9.0` 并核对与源码/迁移的兼容性，不保留 `latest`。源码 SHA 与镜像标签分别记录；若需要严格比较该 SHA 的源码行为，应从此 SHA 构建镜像，而非把发布镜像当成相同源码。

```powershell
docker compose config --quiet
docker compose pull
docker compose up -d
docker compose ps
```

README 的默认 Web 入口是 `http://localhost`。注册与配置完成后导入文档、完成问答和引用检查，保存脱敏截图、镜像摘要、配置版本和验收记录。容器显示 running 后，还要通过实际 HTTP 与完整问答确认可用。

结束练习可运行 `docker compose down` 停止该套服务；保留数据卷供复查。其他三个平台按各自快照 README 进入相应 Compose 目录，模型配置和端口各不相同，不能把这组命令原样套用。

## 源码带读统一要求

每次只追一条用户路径：输入 → 鉴权 → 业务服务 → 数据/模型/工具 → 流式事件 → 用户看到的结果。画出调用关系并链接到固定 SHA；记录取消、错误、恢复和权限边界。完成一个最小改动并跑回归，再决定是否读下一条链路。

“读懂”应能用自己的话解释一次正常执行和一次失败，而不只是展示目录树。当前文档提供的是入口地图，后续逐函数分析和运行实验单独记录。
