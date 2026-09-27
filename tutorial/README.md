# Codex × Power BI 图文教程

本目录保存两篇已经定稿的小红书图文笔记，共 9 张卡片；它们不改变冻结的 `V0/`、`V1/01-zero-seed/` 或 `playbook/` 实验产物。

## 两篇笔记

### 上篇：首次实践（5 张）

- 内容源：[xhs/cards.html](xhs/cards.html)
- 发布图片：[xhs/jpg/](xhs/jpg/)
- 视角：保留首次跑通 Codex、空白种子和 Modeling MCP 路线时的真实实践过程。
- 封面已标注“上篇”，并通过黄色贴纸提示后续已有零种子与更少人工步骤方案。

结构：

1. 封面与案例背景。
2. 当时采用的三项首次配置。
3. 可复制提示词与三个人工等待点。
4. 完整 PBIP 项目交付结构。
5. 最终报表成果与人机边界。

### 下篇：极简工作流（4 张）

- 内容源：[xhs-02-minimal-workflow/cards.html](xhs-02-minimal-workflow/cards.html)
- 发布图片：[xhs-02-minimal-workflow/jpg/](xhs-02-minimal-workflow/jpg/)
- 视角：基于 V1 和三个 follow-up 的实际验证结果，独立说明零种子、最少人工步骤与长期协作方式，不要求读者先阅读上篇。

结构：

1. 极简总结版封面。
2. 包含前置检查、数据和需求的完整任务提示词，以及首次打开、保存、关闭和完整目录交付。
3. PBIP、PBIR、TMDL 的职责，以及简单/复杂模型和视觉修改路径。
4. 四种常见场景的最少人工流程与长期协作建议。

## 内容边界

- 上篇是历史实践记录，不把后来验证出的路线倒写成当时已经知道的事实。
- 下篇采用当前已验证结论：空白种子不是必需条件；MCP 对直接生成不是必需条件，但适合复杂多轮建模。
- 外部 TMDL 修改通过关闭—重开加载；已加载 PBIR 视觉可以通过 **Apply external changes** 更新。
- 人工或 MCP 在 Desktop 内写入的内容需要保存；成功应用的纯外部 PBIR 修改无需额外保存。
- 公开图片不得包含账号、凭据、令牌或不必要的本机信息。

## 素材、导出与校验

- `assets/`：两篇共用的图标和报表截图素材。
- `xhs/export-cards.mjs`、`xhs/validate-cards.mjs`：上篇导出与校验。
- `xhs-02-minimal-workflow/export-cards.mjs`、`xhs-02-minimal-workflow/validate-cards.mjs`：下篇导出与校验。

两份 `cards.html` 都可以直接用浏览器打开。重新发布时，应在对应目录运行导出脚本，再运行校验脚本确认页码、图片资源和内容溢出均通过。
