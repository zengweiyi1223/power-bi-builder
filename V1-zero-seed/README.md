# Power BI Builder — V1 Zero Seed

状态：**Playbook v0.1 符合性检查与 V1 规划冻结；正式 Run 尚未开始。**

## 项目定位

V1-zero-seed 是冻结的 Playbook v0.1 的第一个实际验证项目。它严格执行固定协议并返回项目证据与反馈，不负责修改 Playbook、提炼跨项目方法论或封装 Skill。

核心问题是：Codex 能否从一个经证明为空的目录，直接生成可被 Power BI Desktop 打开、保存、关闭并重新打开的 PBIP/PBIR/TMDL 项目，从而判断人工创建空白 PBIP 种子是否仍然必要。

本实验只改变“项目壳的来源”。V0 的需求、种子、正式运行产物和验收记录保持冻结，不作为 V1 项目模板。

## 固定基线

- Playbook：`v0.1`，提交 `3ee871d618db84d55b3b2f86a198ac552864317e`。
- V1 非规范预备草案：`22da780412f27decf17a097548d65d151c75b235`。
- 接入方式：no-ff merge；Playbook 原始提交是 V1 的真实祖先。
- 需求冻结：以包含本轮符合性检查和规划冻结的 Git 提交为准；提交号由 Git 与交付报告记录，避免文档自引用。

实验期间不得修改 `playbook/**`。发现规则问题时只写入 `PLAYBOOK_FEEDBACK.md` 或 `RECORDS.md`。

## 三种业务结论

| 结论 | 定义 |
| --- | --- |
| 完全零种子 | Codex 在 Desktop 首次启动前生成完整项目；至少两组不同名称和路径的项目均可无修复地打开、保存和重开，且不依赖 Desktop 补齐必需工程结构。 |
| Desktop 首次补写 | 无需人工创建或另存为空白项目，Codex 生成物可以进入 Desktop，但 Desktop 首开或首次保存必须补齐、升级或修复必需结构后才能稳定重开。 |
| 仍需人工种子 | 在排除环境、操作和单一路径问题后，合规的重复试验仍无法直接打开或稳定重开，继续成功必须依赖人工创建的有效项目壳。 |

另设“无法判定”，用于来源污染、环境不稳定、冲突结果或关键证据缺失。预期的负面业务结论不等于执行失败。

## 文档地图

- [BASELINE.md](BASELINE.md)：Git、Playbook、V0 对照和污染边界。
- [PLAYBOOK_CONFORMITY.md](PLAYBOOK_CONFORMITY.md)：Required、Provisional、Guidance 符合性与采用前差异分类。
- [REQUIREMENTS.md](REQUIREMENTS.md)：冻结的 V1 Contract、安全、Human Gate、验收和停止规则。
- [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md)：Execute–Verify 原子阶段、双路径矩阵与 R-VLD-003 评价设计。
- [RUN_RECORD_TEMPLATE.md](RUN_RECORD_TEMPLATE.md)：每个正式 Run 的身份、来源和操作日志模板。
- [VALIDATION.template.md](VALIDATION.template.md)：每个 Run 的验证模板。
- [VALIDATION.md](VALIDATION.md)：V1 跨 Run 汇总验证，当前保持 `Not Started`。
- [RECORDS.md](RECORDS.md)：Decision 与 Deviation。
- [HANDOFF.md](HANDOFF.md)：最终交接骨架，运行完成前不预填成功结论。
- [PLAYBOOK_FEEDBACK.md](PLAYBOOK_FEEDBACK.md)：Rule conformity 与 utility 的分离评价。
- [runs/README.md](runs/README.md)：正式运行目录规则。

## 正式 Run 闸门

规划冻结提交形成并报告后，必须由 Human Approver 明确确认 `HG-00`，才可创建正式 Run。任何 Run 的 `project/` 必须从空目录开始，在首次 Desktop 打开前完成来源确认、离线验证、文件/SHA-256 清单和 Git checkpoint。

本轮规划冻结不启动 Power BI Desktop、不连接 Modeling MCP，也不创建 A/B 正式运行目录。
