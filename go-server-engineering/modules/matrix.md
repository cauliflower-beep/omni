# 样本 × 模块：覆盖矩阵约定

第一批共 12 个样本；其中 Answer、Memos、Navidrome、Gotify、Gitea、PocketBase 的生命周期已有第一轮静态分析，相关模块入口已按范围登记。尚无运行验证记录。具体状态以 coverage.json 为准；无记录默认显示“待检索”，不意味着“不存在”。

## 数据来源

- 样本轴：[samples/registry.json](../samples/registry.json)。
- 模块轴：[catalog.json](catalog.json)。
- 单元格：[coverage.json](coverage.json)，每个 sample_id + module_id 只有一条当前记录。

## 记录格式

```json
{
  "sample_id": "从样本登记表选择",
  "module_id": "从模块目录表选择",
  "status": "located",
  "source_revision": "实际核验的完整 commit SHA",
  "verified_at": "实际核验日期 YYYY-MM-DD",
  "analysis_path": "相对 go-server-engineering 根目录的分析文档路径，未创建时为 null",
  "evidence_urls": [],
  "lab_paths": [],
  "scope": "本次检索或验证的范围",
  "note": "状态说明、限制或不适用理由"
}
```

以上为格式说明，不是真实研究结果；所有文档和实验路径相对本子项目根目录。source_revision 与 verified_at 在取得证据前为 null；located 起应有对应版本和源码入口。状态可取 located、analyzed、validated、not_found、not_applicable。

analyzed 要链接真实分析文档；validated 还要链接已执行实验及结果，且注明验证范围。not_found 需记录检索范围；not_applicable 需记录理由。网站未来据此呈现可筛选矩阵，并对比分析记录和样本基线，提示可能需要重审的条目。
