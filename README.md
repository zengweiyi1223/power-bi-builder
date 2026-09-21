# Power BI Builder

Power BI Builder 用于验证 Codex 能否结合 Microsoft Power BI Modeling MCP 与 PBIP/PBIR，自动生成可由 Power BI Desktop 打开、展示和交互的报表。

## 当前状态

- V0 最小可行实验已完成：报表可在 Power BI Desktop 打开、交互、保存重开，最终模型回读与 DAX 基准一致。
- [`V0/REQUIREMENTS.md`](V0/REQUIREMENTS.md) 是执行与验收基线；[项目报告](V0/PROJECT_REPORT.md)概述结果、文件和已知限制。
- [后续项目规划](ROADMAP.md)分开安排零种子实验、通用 Playbook 和独立的 Power BI 能力扩展；V0 保持冻结。
- [Codex × Power BI 五张图文教程](tutorial/xhs/cards.html)以卡片形式整理一次性配置、可复制提示词、三个人工等待点和完整 PBIP 交付方式；同目录提供 JPG 发布版本。
- 正式运行及证据位于 [`V0/runs/20260917-003433/`](V0/runs/20260917-003433/)；最终保存后的切片器 2.12.0 Schema 精确校验仍待公开文件补证，不影响已验证的 Desktop 使用。

## 目录

```text
V0/
├─ REQUIREMENTS.md   # V0 需求与验收基线
├─ data/             # 固定输入数据
├─ seed/             # 不可直接修改的空白 PBIP 种子
├─ scripts/          # 基准计算和验证脚本
├─ presentation/     # 面向演示的 HTML 流程图
├─ runs/             # 每次正式实验的独立运行目录
└─ .work/            # 可删除的中间文件，不提交 Git
```

正式运行统一使用 `V0/runs/<run-id>/`，其中包含 `project/`、`logs/`、`evidence/`、`expected-results.json` 和 `VALIDATION.md`。运行时从 `seed/` 复制种子，不直接修改种子文件。

正式运行证据默认纳入 Git；可重建中间文件只放入 `.work/`，由脚本按需创建且不得作为验收证据。制品范围、体积限制和 Power BI 文件换行策略以 `V0/REQUIREMENTS.md` 为准。
