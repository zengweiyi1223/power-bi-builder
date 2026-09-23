# Power BI Builder — V1 Zero Seed

状态：**实验完成；A/B 两组正式 Run 均通过，最终结论为“完全零种子”。**

## 项目定位

V1-zero-seed 是冻结的 Playbook v0.1 的第一个实际验证项目。它只执行固定协议并返回 V1 证据与反馈，不修改 Playbook、不提炼跨项目方法论，也不封装 Skill。

核心问题是：Codex 能否从经证明为空的目录直接生成可被 Power BI Desktop 打开、保存、关闭并重新打开的 PBIP/PBIR/TMDL 项目，从而判断人工创建空白 PBIP 种子是否仍然必要。

## 结论

- Run A：`ZeroSeedAlpha`，ASCII 短路径，Passed。
- Run B：`零种子 Beta`，不同父目录、空格与 Unicode，Passed。
- 两组项目均从 0 文件、0 子目录开始，Desktop 首开时无磁盘变化、无修复或警告；首次显式保存后均新增 6、修改 9、删除 0，随后两次重开稳定且磁盘零差异。
- 业务分级：`完全零种子`。Desktop 首次显式保存发生规范化、默认元数据和本机缓存写入，但没有已识别的 `STRUCTURAL_REQUIRED` 或 `SEMANTIC_CHANGE`，因此不归入“Desktop 首次补写”。
- 当前证据不支持“仍需人工种子”。

## 固定基线与范围

- Playbook：`v0.1` @ `3ee871d618db84d55b3b2f86a198ac552864317e`。
- V1 非规范预备草案：`22da780412f27decf17a097548d65d151c75b235`。
- no-ff merge：`8c28f5e340ec41ef56e16d942fd2f9eb97767963`。
- 需求与规划冻结：`82b448957ab08a5452df297a7a95d7b6def67bef`。
- Run A final：`21af7b278d9be6c40ca7315fb0dd5298e3565506`。
- Run B final：`a127b7978990d1d0c6027a72c689704dd5b09a04`。
- 跨 Run 最终验收提交：`c9003aaf29056edac67be88e9f9cf6745816a9cd`。

V0 与 `playbook/**` 在实验期间保持冻结。V1 未读取或复制 `V0/seed/**` 作为工程起点，也未在 A/B 之间复制工程文件。

## 文档地图

- [BASELINE.md](BASELINE.md)：Git、Playbook、V0 对照和污染边界。
- [PLAYBOOK_CONFORMITY.md](PLAYBOOK_CONFORMITY.md)：v0.1 采用前符合性与调整分类。
- [REQUIREMENTS.md](REQUIREMENTS.md)：冻结的 V1 Contract。
- [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md)：冻结的 Execute–Verify 路线。
- [VALIDATION.md](VALIDATION.md)：跨 Run 最终验证与五维判定。
- [RECORDS.md](RECORDS.md)：Decision 与 Deviation。
- [HANDOFF.md](HANDOFF.md)：最终交接、证据入口与回滚点。
- [PLAYBOOK_FEEDBACK.md](PLAYBOOK_FEEDBACK.md)：Rule conformity 与 utility 的分离评价。
- [r7/ACCEPTANCE_EVIDENCE.md](r7/ACCEPTANCE_EVIDENCE.md)：R7 机器复核与最终证据索引。
- [runs/](runs/)：两组完整运行项目、日志、manifest、截图和逐阶段证据。

## 不能声称

本实验只有一个 Desktop 版本、一个 Windows 环境和两个最小空项目样本。它不证明所有 Power BI 版本、复杂模型、跨机器迁移、Power BI Service、任意路径类别或 `.platform` 文件的反事实必要性，也不直接修改 Playbook v0.1。
