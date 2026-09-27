# V1 — 最少人工步骤与人机协作工作流验证

状态：**四项实验均已完成。**

V1 验证 Codex 能否从空目录直接生成完整 Power BI Project，并确定长期协作中模型设置、模型修改和视觉修改所需的最少人工操作。零种子不是 V1 的全部，而是四个连续实验中的第一阶段。

## 最短阅读路径

1. 先看本页，了解四项实验如何共同形成 V1 结论。
2. 看 [04-minimal-human-workflow/results/FINAL_RESULT.md](04-minimal-human-workflow/results/FINAL_RESULT.md)，了解已验证的最少人工流程。
3. 总结 Playbook v0.2 时，再读取各实验的 `results/`；只有复核具体结论时才进入 `project/`、`evidence/`、`logs/` 和 `manifests/`。

## 四项实验

| 阶段 | 实验 | 核心问题 | 结果 | 主要结论入口 |
| --- | --- | --- | --- | --- |
| 1 | [01-zero-seed](01-zero-seed/) | 是否仍需人工创建空白 PBIP 种子？ | Passed | [VALIDATION](01-zero-seed/results/VALIDATION.md) · [HANDOFF](01-zero-seed/results/HANDOFF.md) |
| 2 | [02-auto-date-setting](02-auto-date-setting/) | 当前文件的自动日期/时间能否由模型显式关闭？ | Passed | [VALIDATION](02-auto-date-setting/results/VALIDATION.md) · [FINAL_RESULT](02-auto-date-setting/results/FINAL_RESULT.md) |
| 3 | [03-live-pbir-reload](03-live-pbir-reload/) | Desktop 保持打开时，已加载 PBIR 视觉能否应用外部修改？ | Passed（限定已加载视觉） | [FINAL_RESULT](03-live-pbir-reload/results/FINAL_RESULT.md) · [HANDOFF](03-live-pbir-reload/results/HANDOFF.md) |
| 4 | [04-minimal-human-workflow](04-minimal-human-workflow/) | 真实模型与数据绑定视觉的最少人工流程是什么？ | Passed（PBIR Apply；TMDL 重开） | [FINAL_RESULT](04-minimal-human-workflow/results/FINAL_RESULT.md) · [HANDOFF](04-minimal-human-workflow/results/HANDOFF.md) |

## V1 综合结论

- Codex 可以从空目录直接生成完整 PBIP、PBIR 和 TMDL 项目；当前证据不支持人工空白种子仍为必要条件。
- `__PBI_TimeIntelligenceEnabled = 0` 可以显式关闭当前文件的自动日期/时间，并在保存、关闭和重开后保持。
- 首次生成的项目无需先保存即可打开；长期协作建议首次打开后保存并关闭，让 Desktop 写入规范化、平台和身份元数据。
- Desktop 关闭时由 Codex 修改 TMDL，随后重开验收，是当前验证过的可靠模型文件路径；纯磁盘外部修改无需再次保存。
- Desktop 保持打开时，Codex 可以修改已经被当前会话加载的 PBIR 视觉，人工选择 **Apply external changes** 后查看结果；成功应用后无需额外保存。
- MCP 不是生成 Power BI 项目的必要条件。它适合复杂、多轮模型工程的实时修改与验收；人工或 MCP 在 Desktop 内产生的修改必须保存。

## 统一目录规则

每个实验只在根目录保留 `README.md` 和实际产物目录：

- `planning/`：基线、需求、实验计划、Human Gate 和安全边界。
- `results/`：Validation、Final Result、Handoff、Decision/Deviation 和 Playbook Feedback。
- `project/`：实际 PBIP/PBIR/TMDL 项目。
- `evidence/`：截图和阶段性检查。
- `logs/`：Human、Codex 与 MCP 操作记录。
- `manifests/`：文件清单、哈希和差异。
- `templates/`、`runs/`、`r7/`：零种子多 Run 实验专用的模板、正式运行和最终机器复核。

`project/` 以下文件是项目本体；其余大部分文件用于实验审计，不是日常交付时都需要阅读的文件。

## 历史与冻结边界

- `01-zero-seed` 原位于 `V1-zero-seed/`；另外三项实验原位于 `followups/`。本次归档只重组路径和导航，不改写实验事实。
- 四项实验的分支、固定提交、运行日志、截图、manifest 和实际项目均保留在 Git 历史中。
- 运行时的旧绝对路径是历史证据，仍按执行当时的值保留。
- `V0/**` 与冻结的 `playbook/**` 未因本次归档而修改。
- `.work/` 和 `.pbi/` 是可重建或机器本地缓存，不属于正式交付和实验结论。

## 不能声称

V1 的结论来自同一 Windows/Power BI Desktop 环境和有限项目样本。它不证明所有 Desktop 版本、数据源、凭据、Power BI Service、跨机器迁移以及任意 PBIR/TMDL 对象都具有完全相同的行为。
