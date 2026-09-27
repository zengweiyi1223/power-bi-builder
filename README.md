# Power BI Builder

Power BI Builder 用于验证并沉淀 Codex 直接生成、验证和迭代 Power BI Project（PBIP/PBIR/TMDL）的可靠工作流。项目从 V0 的种子与 MCP 路线出发，已经完成零种子、模型级设置、PBIR 热重载和最少人工步骤等后续实验。

## 当前状态

- [V0](V0/)：最小可行实验已完成，证明报表可以在 Power BI Desktop 中打开、交互、保存重开，并通过模型回读与 DAX 基准验证。V0 需求、种子和正式运行产物保持冻结。
- [Playbook v0.1](playbook/)：基于 V0 提炼的固定执行协议，基线提交为 `3ee871d618db84d55b3b2f86a198ac552864317e`。V1 与后续实验没有直接修改该版本。
- [V1-zero-seed](V1-zero-seed/)：两组独立 Run 均通过，最终结论为“完全零种子”；在已测试环境中，人工无需先创建空白 PBIP 种子。
- [后续实验](followups/)：已完成显式关闭自动日期/时间、已加载 PBIR 视觉热重载和最少人工工作流验证。
- [图文教程](tutorial/)：已定稿上篇 5 张和下篇 4 张。上篇保留首次实践视角，下篇总结零种子、最少人工步骤和长期人机协作流程。

## 已验证的实际工作流

1. **初版生成**：用户提供前置检查要求、数据和业务需求；Codex 可从空目录直接生成完整 PBIP、PBIR 和 TMDL 项目。
2. **首次长期基线**：项目无需保存即可打开；长期协作建议首次打开后保存并关闭，让 Desktop 完成规范化和平台/身份元数据写入。
3. **模型文件修改**：Desktop 关闭时由 Codex 修改 TMDL，随后重开验收；纯磁盘外部修改无需再次保存。
4. **已有视觉修改**：Desktop 保持打开时由 Codex 修改已加载的 PBIR，人工选择 **Apply external changes**；成功应用后无需额外保存。
5. **复杂多轮建模**：MCP 不是生成项目的必需条件，但适合保持 Desktop 打开并实时调整、验收复杂模型；MCP 或人工在 Desktop 内完成修改后必须保存。

上述结论来自 Power BI Desktop `2.157.1354.0` 的本机 Windows 实验。不同版本、数据源、凭据、Service、跨机器迁移和未测试的 PBIR/TMDL 对象仍需按项目重新验证。

## 目录

```text
.
├─ README.md                       # 项目入口与当前结论
├─ V0/                             # 冻结的初始实验、种子、正式 Run 与证据
├─ playbook/                       # 冻结的 Playbook v0.1、模板和 Power BI adapter
├─ V1-zero-seed/                   # 零种子 A/B Run、证据、Handoff 与反馈
├─ followups/
│  ├─ auto-date-setting/           # 模型级自动日期/时间显式关闭
│  ├─ live-pbir-reload/            # 已加载 PBIR 视觉的外部热重载
│  └─ minimal-human-workflow/      # 最少人工步骤与模型/视觉边界
└─ tutorial/
   ├─ xhs/                         # 上篇：首次实践，5 张
   └─ xhs-02-minimal-workflow/     # 下篇：极简工作流，4 张
```

## 证据与冻结边界

- `V0/**` 和 `V1-zero-seed/**` 保存各自实验当时的需求、计划、项目、日志和验收记录；即使其中存在阶段性或历史措辞，也不回写改造成当前教程。
- `followups/**` 保存三个独立后续实验的完整项目、manifest、人工/Codex/MCP 操作日志和结论。
- `playbook/**` 当前仍是固定的 v0.1。实验观察只进入各自 `PLAYBOOK_FEEDBACK.md`；通用规则调整统一留给 Playbook v0.2。
- `.pbi/` 缓存、本机设置和自动恢复文件不属于正式项目交付物；完整交付应包含同级的 `.pbip`、Report 和 SemanticModel 目录。
