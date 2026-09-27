# V1 后续实验索引

本目录保存 V1-zero-seed 完成后的三个独立 Power BI follow-up。它们从不同角度收窄实际使用边界，并为 Playbook v0.2 提供观察与建议；这些实验不直接修改冻结的 `V0/`、`V1-zero-seed/` 或 `playbook/`。

## 实验顺序与结论

| 顺序 | 实验 | 最终提交 | 结论 |
| --- | --- | --- | --- |
| 1 | [auto-date-setting](auto-date-setting/) | `77a188f20f85a614a7a2774ecb64fa6426411fa6` | 模型级 `__PBI_TimeIntelligenceEnabled = 0` 可在首开时显式关闭当前文件自动日期/时间，并在保存、关闭、重开后保持。 |
| 2 | [live-pbir-reload](live-pbir-reload/) | `8732141fa58d6314c0b17e31116f2b0db5296d71` | 已被 Desktop 加载的 PBIR 视觉可通过 **Apply external changes** 热重载；会话中新增但从未加载的视觉未被发现。 |
| 3 | [minimal-human-workflow](minimal-human-workflow/) | `8a005159aa2b739ecc4a399405b2caecb3a752f6` | 零种子完整项目可直接生成；已有 PBIR 视觉可 Apply，测试过的 TMDL 修改需要关闭—重开。 |

三个实验及其真实 Git 历史最终整合于 `codex/v1-followups-integrated`，整合提交为 `036fe6434b9632524cba55c042c6fa85a3193406`。

## 综合使用结论

- Codex 可以直接写出完整 PBIP/PBIR/TMDL 项目，不依赖人工空白种子。
- 自动日期/时间等当前文件设置可以通过 TMDL 显式表达，不必依赖人工点选。
- MCP 不是文件生成的必需条件；它的主要优势是复杂、多轮模型工程的实时修改和验收。
- 外部修改已有 PBIR 视觉时，Desktop 可保持打开并由人工应用外部更改；应用成功后无需额外保存。
- 修改 TMDL 时，当前验证过的可靠路径是关闭 Desktop、由 Codex 修改、再重开验收。
- 人工或 MCP 在 Desktop 内修改后必须保存；Codex 每批外部修改前应保留 Git checkpoint。

## 证据布局

每个实验目录保留其适用的：

- `README.md`、`REQUIREMENTS.md`、`EXPERIMENT_PLAN.md`；
- `VALIDATION.md`、`FINAL_RESULT.md`、`HANDOFF.md`；
- `project/`、`manifests/`、`logs/` 和 `evidence/`；
- `PLAYBOOK_FEEDBACK.md` 与 Decision/Deviation 记录。

具体结论以各实验的最终验证和 Handoff 为准；本索引只负责导航，不扩大原实验可以声称的范围。
