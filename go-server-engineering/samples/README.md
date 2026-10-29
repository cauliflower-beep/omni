# 学习样本

样本用于理解真实业务下的设计选择；热度不代表架构质量。第一批为前一轮讨论的全部 12 个项目，初始状态均为已登记、待核验。

## 样本清单

- [Apache Answer](answer/overview.md)：问答社区。
- [PocketBase](pocketbase/overview.md)：可嵌入的通用后端底座。
- [Memos](memos/overview.md)：自托管笔记。
- [Navidrome](navidrome/overview.md)：音乐管理与流媒体。
- [Gotify](gotify/overview.md)：消息推送。
- [Gitea](gitea/overview.md)：Git 托管与研发协作。
- [Beszel](beszel/overview.md)：服务器监控。
- [1Panel](1panel/overview.md)：服务器管理面板。
- [PhotoPrism](photoprism/overview.md)：照片与视频管理。
- [Mattermost](mattermost/overview.md)：团队通信与协作。
- [Casdoor](casdoor/overview.md)：身份与访问管理。
- [Gatus](gatus/overview.md)：健康检查与状态页。

## 数据与文档职责

registry.json 保存唯一 id、规范仓库、登记日期、当前选定基线与核验状态；overview.md 保存产品与架构轮廓；module-map.md 链接固定版本源码与模块实现分析。

source_revision 必须是核实的完整 commit SHA；source_ref 是辅助分支或标签；verified_at 是实际核验日期。null 代表尚未核验，不填写猜测值。当前不保存易失效的 star 数。

后续可通过网站展示层筛选、导航；当前以此文档和 [模块矩阵说明](../modules/matrix.md) 为入口。
