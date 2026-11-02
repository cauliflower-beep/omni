# AI 大模型应用开发学习路线

大模型应用开发将模型、业务数据和工具接入软件系统，通过评估、权限控制与运行治理，交付可用的产品功能。核心能力包括模型接口、上下文工程、RAG、工具调用、任务状态管理和效果评估。

## 内容导航

| 内容 | 重点 |
| --- | --- |
| [行业与能力](industry-and-skills.md) | 岗位分工、概念边界、技术栈 |
| [分阶段路线](roadmap.md) | 24 周任务、交付物与验收条件 |
| [开源项目](open-source-samples.md) | WeKnora、Coze Studio、Dify、RAGFlow、Eino |
| [实践项目](projects.md) | 文档知识助手、运维助手、文档工单流程 |
| [评估与交付](evaluation.md) | 数据集、质量指标、成本、故障与安全验证 |
| [资料来源](sources.md) | 官方文档、论文、源码和岗位样本 |
| [样本版本](data/samples.json) | 提交 SHA、发布标签、依赖与许可证 |
| [实验记录](templates/experiment.md) | 假设、基线、复现步骤与实测结果 |

## 实践顺序

1. 模型接口：文本生成、流式响应、结构化输出、超时与取消。
2. 评估：建立工单抽取数据集，对照 Prompt、模型、质量和成本。
3. RAG：导入技术文档，对比关键词、向量和混合检索，实现引用与版本管理。
4. Agent：接入只读工具，再加入审批、幂等、任务恢复和调用预算。
5. 交付：部署、观测、故障注入、回归评估与业务试用。

Python 可使用模型 SDK、LangGraph 和 Dify；Go 可使用模型 SDK、Eino、WeKnora 和 Coze Studio。具体实现顺序见[技术栈](industry-and-skills.md)。
