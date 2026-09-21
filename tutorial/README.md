# Codex × Power BI 图文教程

本目录用于发布可复用的实战教程，不改变已经冻结的 `V0/` 实验产物。

## 输出

- `index.html`：可离线打开的完整作品集页面。
- `CONTENT.md`：教程事实、步骤和人工边界的内容基线。
- `assets/screenshots/`：教程引用的原始操作截图副本。
- `xhs/cards.html`：小红书竖版卡片源文件。
- `xhs/jpg/`：从卡片源文件导出的 JPG。
- `xhs/export-cards.mjs`：使用 Playwright 重复导出卡片的脚本。

## 内容原则

- 一次性配置与每个报表的重复操作分开说明。
- 明确标注 Power BI Desktop 应保持打开还是关闭。
- MCP、PBIP 项目和数据路径分别解释，不把它们混为一谈。
- V0 的验证细节不进入主教程，只保留实际生产必需的安全检查和交接动作。
- 截图公开前必须去除账号、凭据、令牌和不必要的本机信息。

## 本地查看

直接用浏览器打开 `index.html`。卡片源文件可打开 `xhs/cards.html` 查看。
