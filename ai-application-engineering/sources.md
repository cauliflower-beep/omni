# 资料与来源

核查日期：2026 年 10 月 30 日。动态接口与依赖以对应版本为准。

## 模型接口与评估

| 编号 | 资料与出处 | 用于什么 | 时间与边界 |
| --- | --- | --- | --- |
| S01 | [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)，OpenAI | Schema、结构化响应、拒绝与不完整输出 | 动态官方文档；结构不等于内容正确 |
| S02 | [Function Calling](https://developers.openai.com/api/docs/guides/function-calling)，OpenAI | 应用执行工具并回传结果的过程 | 按选定 API 与模型核对能力 |
| S03 | [Evaluation Best Practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)，OpenAI | 任务评估、数据集、人工校准与持续回归 | 方法可用，文中托管产品依赖需结合退役说明 |
| S04 | [Deprecations](https://developers.openai.com/api/docs/deprecations)，OpenAI | 核对平台/API 退役安排 | Evals：2026-10-31 只读，2026-11-30 计划关闭 |
| S05 | [OpenAI Go SDK README](https://github.com/openai/openai-go/blob/main/README.md)，官方仓库 | Go 原生接入、Responses 用法和工具链要求 | 核查时为 v3 导入路径；实际运行要锁 SDK/Go 版本 |
| S06 | [Your First API Call](https://api-docs.deepseek.com/)，DeepSeek | 国内模型接口对照、兼容 API 的具体格式 | 兼容声明不代表所有厂商功能完全相同 |
| S07 | [Demystifying Evals for AI Agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)，Anthropic | task/trial、最终状态、重复试验和判分 | 2026-01-09；区分单次输出与任务完成 |
| S08 | [Promptfoo Intro](https://www.promptfoo.dev/docs/intro/)，项目官方文档 | 本地评估、断言和 CI 入口 | 动态文档；本地工具仍可能调用外部模型 |
| S09 | [Ragas](https://docs.ragas.io/en/stable/)，项目官方文档 | RAG/Agent 指标的可选实现 | 指标定义与本地评分规则需要逐项对应 |

## Agent 与上下文工程

| 编号 | 资料与出处 | 用于什么 | 时间与边界 |
| --- | --- | --- | --- |
| S10 | [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)，Anthropic | Workflow 与 Agent、简单模式、何时增加复杂度 | 2024-12-19；页面已提醒旧工具环境有变化，不作最新 API 手册 |
| S11 | [Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)，Anthropic | 上下文筛选、工具设计、记忆与压缩 | 2025 年工程文章，按方法读 |
| S12 | [Harness Design for Long Running Apps](https://www.anthropic.com/research/harness-design-long-running-apps)，Anthropic | 长任务的运行环境与交付机制 | 官方工程索引标为 2026-03-24；进阶阅读 |
| S13 | [Scaling Managed Agents with Stable Interfaces](https://www.anthropic.com/research/managed-agents)，Anthropic | 模型决策与运行环境的接口分离 | 2026 年工程实践；产品专属能力不是本路线的依赖 |
| S14 | [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)，LangChain | 状态、持久执行、流式与人工介入 | 当前文档，Python 编排路径入口 |
| S15 | [Eino Overview](https://www.cloudwego.io/docs/eino/overview/)，CloudWeGo | Go 组件、Graph/Workflow、ADK 与观测 | 当前官方文档，主要 Go 框架入口 |

## 数据 检索 协议与运行

| 编号 | 资料与出处 | 用于什么 | 时间与边界 |
| --- | --- | --- | --- |
| S16 | [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28)，协议官方 | Host/Client/Server、工具、资源与安全原则 | 当前 latest 重定向至 2026-07-28；必须核对实际客户端支持 |
| S17 | [MCP Go SDK](https://github.com/modelcontextprotocol/go-sdk/blob/main/README.md)，官方仓库 | Go 工具服务和协议版本兼容表 | 核查时兼容表列出 v1.7.0+ 支持 2026-07-28；执行时锁版本 |
| S18 | [MCP 2026-07-28 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)，官方维护者 | 理解 2025 与 2026 规范变化的背景 | 文章发布日期为 2026-05-21，标题日期是目标规范版本；最终要求以 S16 为准 |
| S19 | [pgvector README](https://github.com/pgvector/pgvector/blob/master/README.md)，项目官方 | Postgres 向量索引、距离与检索行为 | 动态主分支；生产选择另锁版本 |
| S20 | [Langfuse Docs](https://docs.langfuse.com/)，项目官方 | Trace、Prompt 管理、评估和成本观测 | Go 可研究 OpenTelemetry 兼容接入；部署时核对接收端要求 |
| S21 | [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/)，OWASP | 注入、输出处理、越权和无界消耗等风险 | 本轮官方入口仍展示 2025 列表；不采用未核实的 2026 转载排名 |
| S22 | [vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)，项目官方 | 可选的自托管推理实验 | 不是 API 应用入门前提；平台与硬件要单独确认 |

## 课程与原始论文

| 编号 | 资料与出处 | 建议读法 | 时间与边界 |
| --- | --- | --- | --- |
| S23 | [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)，Microsoft | 先选概念、Prompt、安全、生命周期和 RAG；边做边查 | 教学仓库持续更新，具体产品路径可能迁移 |
| S24 | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)，Hugging Face | 第一轮选模型与 Tokenizer 概念；训练章节后置 | 官方课程本身要求较好的 Python 基础，不应强制从头学完才动手 |
| S25 | [Retrieval Augmented Generation for Knowledge Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)，Lewis 等 | 读摘要、架构与方法定位，理解参数与外部知识结合 | 初稿 2020 年；原论文方法不等同于所有现代 RAG 流水线 |
| S26 | [ReAct](https://arxiv.org/abs/2210.03629)，Yao 等 | 看推理、行动、环境反馈如何交替 | 初稿 2022 年、ICLR 2023；现代工具调用不要求暴露模型内部思维链 |
| S27 | [Lost in the Middle](https://arxiv.org/abs/2307.03172)，Liu 等 | 理解位置与长度应进入上下文测试 | 2023 年；不能将当时模型的结果直接套到 2026 每个模型 |

## 完整产品与框架样本

| 编号 | 仓库 | 核查内容与用途 |
| --- | --- | --- |
| S28 | [Tencent WeKnora](https://github.com/Tencent/WeKnora) | README、LICENSE、go.mod、cmd/internal 目录、提交与发布；Go RAG 主样本 |
| S29 | [Coze Studio](https://github.com/coze-dev/coze-studio) | README、LICENSE-APACHE、backend/go.mod、业务目录、提交与发布；Go 工作流样本 |
| S30 | [Dify](https://github.com/langgenius/dify) | README、LICENSE、api/pyproject.toml、api/core、提交与发布；Python 完整产品样本 |
| S31 | [RAGFlow](https://github.com/infiniflow/ragflow) | README、LICENSE、go.mod、internal、提交与发布；复杂文档与新架构 |
| S32 | [Eino Examples](https://github.com/cloudwego/eino-examples) | README、LICENSE-APACHE、示例目录与 assistant README、提交；机制与小型应用 |

固定 SHA、发布标签和许可证见[样本档案](open-source-samples.md)与 [JSON 数据](data/samples.json)。

## 公开岗位样本

| 编号 | 来源 | 已读正文支持的结论 |
| --- | --- | --- |
| S33 | [慧辰 大模型应用开发工程师](https://career.nankai.edu.cn/correcruit/content/id/119530.html)，南开就业平台，2026-10-08 | 应用接口、评估、成本取舍、运行监控和业务集成；Python 与其他语言要求 |
| S34 | [Speediance 大模型应用开发工程师](https://sil.speediance.com/zh/career/llm-application-engineer)，雇主官网 | Agent 应用与后端工程结合；Java/Python、框架与中间件 |
| S35 | [Anthropic Applied AI Research Engineer](https://job-boards.greenhouse.io/anthropic/jobs/5390811008)，官方招聘系统 | 资深应用研发、评估、原型和客户沟通能力；仅作能力上限参考 |
