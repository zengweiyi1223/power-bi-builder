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

## DCS-004 — 按冻结标准判定“完全零种子”

- 时间：2026-09-22，America/Los_Angeles
- 关联 Rule ID / 阶段：R-FRM-001、R-VLD-001、R-VDC-001；R7
- 背景与需要决定的问题：A/B 首次显式保存都新增 6 个文件并修改 9 个文件，需要区分“完全零种子”和业务分类“Desktop 首次补写”。
- 可选方案：因任何 Desktop 写盘而判为首次补写；只看能否首开；按冻结的 `STRUCTURAL_REQUIRED` / `SEMANTIC_CHANGE` 和三级结论标准综合判定。
- 决定及理由：判为“完全零种子”。两组首开均无磁盘变化、无修复或警告；首存变化均被分类为缓存、等价序列化、默认元数据和版本升级，没有已识别的结构必需补写或语义改变；两次重开均稳定。
- 对范围、验收、安全和后续阶段的影响：满足 V1 的两组重复性标准；不把正常显式保存的 canonicalization 误称为首开修复。保留 `.platform` 反事实必要性未测试的限制。
- 证据或 Git 提交：两组 `R3_FIRST_OPEN.md`、`R4_POST_SAVE.md`、R5/R6 evidence；Run A `21af7b2`；Run B `a127b79`；总 `VALIDATION.md`。
- 是否需要更新 Contract：否；使用冻结口径，不回写需求。

## DCS-005 — 对 R-VLD-003 建议 Change，不在 V1 修改规则

- 时间：2026-09-22，America/Los_Angeles
- 关联 Rule ID / 阶段：R-VLD-003、R-FBK-001、R-GOV-001；R7
- 背景与需要决定的问题：Playbook-only 最终再次往返在两组中都通过，但是否提供了与成本相称的新信息。
- 可选方案：Keep 无条件重复；Change 为风险触发/抽样；Retire；Move 到 Power BI adapter。
- 决定及理由：反馈建议 `Change`。A/B 的额外往返均为 0 新发现、0 捕获问题、0 避免错误结论，只增加第三个独立进程启动的重复性信心；对低风险最小项目边际价值较低，但高风险持久化宿主仍可能需要。
- 对范围、验收、安全和后续阶段的影响：只写入 `PLAYBOOK_FEEDBACK.md`；不修改 `playbook/**`、不创建 v0.2、不把建议当成已采纳规则。
- 证据或 Git 提交：两组 `R-VLD-003-METRICS.json`；A/B R6 evidence；R7 总 Validation。
- 是否需要更新 Contract：否。

## Deviation

规划冻结时无 Deviation。以下偏差在正式执行后按观察事实追加；冻结 Contract 未被回写。

## DEV-001 — R-VLD-003 精确时间未前置采集

- 时间：2026-09-22，America/Los_Angeles
- 关联 Rule ID / Contract 条款：R-VLD-003；`REQUIREMENTS.md` §9；R6
- 预期行为：分别记录 core 与 Playbook-only 往返的 Human active、等待和机器检查时间。
- 实际行为：核心阶段 Human/机器时间未前置计时；额外往返 Human 仅定性报告“约几秒”。A/B 机器检查分别记录 2.34 和 0.04 分钟，但口径并不完全相同。
- 类型与严重度：`Evidence Gap` / `Non-blocking`；V1 主因 `HUMAN`（计量流程设计未在 Gate 时落地）。
- 原因和影响：冻结计划定义了指标，但未把开始/结束时间采集嵌入每个 Human Gate。功能与 conformity 结论不受影响；R-VLD-003 的精确成本比较受限。
- 临时处理或恢复方式：保留 null 和定性值，不伪造分钟；逐 Run metrics 明确口径和限制。
- 证据或 Git 提交：两组 `logs/R-VLD-003-METRICS.json`。
- 对最终结论的限制：只能评价为低度正向边际价值，不能声称获得完整的人时成本模型。
- 给 Maintainer 的建议：`Template`；在 Gate/metrics 模板中前置开始、结束、active/wait 与机器计时字段。

## DEV-002 — Desktop canonical 根文件与公开 Schema 的 `$schema` 要求不一致

- 时间：2026-09-22，America/Los_Angeles
- 关联 Rule ID / Contract 条款：R-VLD-001、R-VLD-002；R4–R7
- 预期行为：Desktop 保存后的根 `.pbip`、`definition.pbir`、`definition.pbism` 可直接按各自公开 Schema 复验。
- 实际行为：A/B 的 Desktop 首存均移除三个根文件中的 `$schema`；该属性在所用公开 Schema 中标为 required。恢复同一 Schema URL 到内存副本后，其余结构通过。
- 类型与严重度：`Evidence Gap` / `Non-blocking`；V1 主因 `SPEC`。
- 原因和影响：目标 Desktop 的 canonical 输出与当前公开 Schema 元数据要求不一致。不能声称原样文件直接通过这些 Schema；Desktop 实际稳定重开、磁盘 diff 和 MCP 只读回读仍支持功能结论。
- 临时处理或恢复方式：不修改 Desktop 现场；保留直接失败、内存恢复验证与产品回读三类证据。
- 证据或 Git 提交：两组 `R4_POST_SAVE.md`、事件日志、R5 evidence；Run A `21af7b2`；Run B `a127b79`。
- 对最终结论的限制：V1 为 `Complete with known non-blocking evidence gaps`，不是无条件公共 Schema conformance 声明。
- 给 Maintainer 的建议：`Evidence gap`；可在 Power BI adapter 中说明产品 canonical 输出与公开 Schema 冲突时的证据组合。

其余已记录的 PowerShell 分词、CRLF 和路径分隔符假失败遵守了停止—修正—从头重跑规则，没有改变 Contract、路线或成功口径，因此保留为 Run event，不另列 Deviation。
