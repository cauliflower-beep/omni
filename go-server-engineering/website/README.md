# HTML 网站展示层

状态：结构预留；没有框架、依赖、构建配置、可运行页面或部署配置。

## 数据与内容来源

样本读取 ../samples/registry.json，模块读取 ../modules/catalog.json，覆盖进度读取 ../modules/coverage.json。文章读取相应 Markdown；以后根据交互需要引入可嵌入组件的文档格式，不复制文章正文。

手册以 HTML 供读者阅读，Markdown 是内容源。README 与贡献说明同时服务 GitHub 阅读。内容加载、链接映射和渲染策略在正式实现前确定。

## 目录职责

- src/pages/：页面和路由入口。
- src/layouts/：文章、样本、模块、比较页的统一布局。
- src/components/：导航、目录、代码块、筛选和对比组件。
- src/content/：内容读取与索引适配；不存重复文章。
- src/styles/：主题、排版、代码与响应式样式。
- src/demos/：解释生命周期、取消传播等过程的交互演示。
- public/assets/：可直接发布的静态资源，记录来源与许可。

## 后续实现顺序

先统一排版、双向导航、代码展示和搜索，再做样本筛选及对比矩阵，最后完成一个可控制的生命周期演示。按 [阅读与交互约定](design.md) 验收。

尚未选定构建工具与托管方式，当前不能运行 npm install、npm run dev 或发布网站；源码可先从根 README 阅读。
