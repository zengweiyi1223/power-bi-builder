# V1 Zero Seed — Decision 与 Deviation 记录

## DCS-001 — 固定并真实继承 Playbook v0.1

- 时间：2026-09-22，America/Los_Angeles
- 关联 Rule ID / 阶段：R-GOV-001；F0
- 背景与问题：V1 草案早于 Playbook v0.1，需要固定协议且保留其真实祖先关系。
- 可选方案：no-ff merge；cherry-pick；手工复制；仅文本引用。
- 决定及理由：按用户要求 no-ff merge `3ee871d618db84d55b3b2f86a198ac552864317e`，不 cherry-pick、不复制。这样可审计 v0.1 原始提交和 V1 采用前草案。
- 影响：实验期间 `playbook/**` 只读；所有问题进入反馈，不在 V1 修订基线。
- 证据：merge `8c28f5e340ec41ef56e16d942fd2f9eb97767963`。
- 是否更新 Contract：是，已在本轮规划冻结中纳入。

## DCS-002 — 保留采用前实验设计，仅补治理缺口

- 时间：2026-09-22，America/Los_Angeles
- 关联 Rule ID / 阶段：R-FRM-001、R-CTR-001、R-FBK-001；F0
- 背景与问题：`22da780` 已定义空目录、A/B 重复、三级结论和来源边界；需要判断哪些内容应改变。
- 可选方案：按模板重做实验；原样执行；保留实验设计并逐项分类调整。
- 决定及理由：保留核心设计；只做 Risk Correction、Operational Clarification 和明确的 Playbook-only Alignment。避免为了证明 Playbook 正确而改造业务问题。
- 影响：三级结论、A/B 名称与路径、禁止 V0 工程来源均不变；新增安全、Human Gate、严重度、模板和反馈结构。
- 证据：`PLAYBOOK_CONFORMITY.md`、`PLAYBOOK_FEEDBACK.md` 的采用前对比。
- 是否更新 Contract：是，治理条款补入冻结版本。

## DCS-003 — 分离 R-VLD-003 的核心往返与附加往返

- 时间：2026-09-22，America/Los_Angeles
- 关联 Rule ID / 阶段：R-VLD-003；R5–R6
- 背景与问题：保存/关闭/重开本来就是零种子核心问题，无法用其总成本单独评价 Provisional Rule 的附加成本。
- 可选方案：只评价核心往返；把所有往返都归因于 Playbook；额外执行一次最终往返并单独计量。
- 决定及理由：首次往返标记 `Core roundtrip`；最终再次往返标记 `Playbook-only final roundtrip`，分别记录时间、证据和唯一发现。
- 影响：增加 HG-04 和一次额外 Desktop 往返；该动作只产生 utility 数据，不自动证明规则有效。
- 证据：`EXPERIMENT_PLAN.md` §9、`VALIDATION.template.md` §7。
- 是否更新 Contract：是，已冻结。

## Deviation

规划冻结时无 Deviation。正式执行中的偏离从 `DEV-001` 起编号；不得为适配结果回写或删除既有记录。
