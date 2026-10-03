# 人机协作开发闭环 Playbook

版本：`v1.0.1`（2026-10-03 人工验收通过并冻结）

本 Playbook 用于人类与 AI 共同完成可验证、可停止、可恢复、可交付的软件、数据、文档和实验项目。它由一条可裁剪开发生命周期、责任模型、阶段记录和 Evidence Gate Kernel 组成；领域操作放在 adapter，单项目事实留在项目记录和 case study。

## 1. 一条生命周期

```text
Profile & Tailor
→ Discover & Frame
→ Contract
→ Design
→ Plan & Prepare
→ [Implement → Verify → Human Gate → Decide → Checkpoint] × N
→ Integrated Acceptance
→ Release / Delivery
→ Operate / Observe
→ Handoff / Close / Learn
```

这是唯一的顶层流程。中间方括号是 Evidence Gate Kernel：每个可验证增量完成后立即验证、判定和建立回滚点，不是全部开发结束后才统一测试。

阶段可以合并，不能静默删除。每个阶段标记为：

- `Required`：项目必须完成；
- `Conditional`：触发条件成立时必须完成；
- `Not Applicable`：不适用，必须写明理由。

## 2. 项目画像与裁剪

先选择最接近的基础画像，再叠加风险修饰器。画像不是行业分类，只决定默认流程起点。

| ID | 基础画像 | 典型交付 |
| --- | --- | --- |
| PF-EXP | 实验/研究 | 结论、原型、证据 |
| PF-DOC | 文档/内容 | 文档、教程、知识资产 |
| PF-DAT | 数据/分析 | 数据集、分析、模型、报告 |
| PF-CMP | 组件/自动化 | 库、CLI、脚本、工作流 |
| PF-APP | 交互应用/内部工具 | Web、桌面或交互工具 |
| PF-SVC | 生产服务 | 持续运行的服务或平台 |

风险修饰器：`MD-UI` 界面与交互、`MD-DATA` 持久化数据、`MD-EXT` 外部系统、`MD-DEPLOY` 部署、`MD-OPS` 长期运行、`MD-SEC` 安全与敏感信息、`MD-MULTI` 多角色协作、`MD-HIGH` 高代价或不可逆风险。

默认阶段裁剪如下，修饰器可以把 `Conditional` 或 `Not Applicable` 提升为 `Required`，不能用“轻量项目”降低真实风险。

| Stage | PF-EXP | PF-DOC | PF-DAT | PF-CMP | PF-APP | PF-SVC |
| --- | --- | --- | --- | --- | --- | --- |
| Profile & Tailor | R | R | R | R | R | R |
| Discover & Frame | R | R | R | R | R | R |
| Contract | R | R | R | R | R | R |
| Design | C | C | R | R | R | R |
| Plan & Prepare | R | C | R | R | R | R |
| Implement & Verify | R | R | R | R | R | R |
| Integrated Acceptance | R | R | R | R | R | R |
| Release / Delivery | R | R | R | R | R | R |
| Operate / Observe | N/A | N/A | C | C | C | R |
| Handoff / Close / Learn | R | R | R | R | R | R |

`Release / Delivery` 对所有项目表示受控交付，不等于所有项目都要上线。人工 UAT、实际部署和持续运维只在对应风险存在时启用。

画像和裁剪不是只做一次。Contract 新增交付形态、界面、数据、外部系统、部署、运维、安全或多人协作范围时，必须重新检查画像、修饰器、阶段适用性和记录映射；不需要为了保持最初分类而忽略后来出现的真实风险。

## 3. 阶段最低要求

| Stage | 主要问题 | 最低退出条件 | 主要记录 |
| --- | --- | --- | --- |
| Profile & Tailor | 这是什么项目，哪些风险改变默认流程？ | 画像、修饰器、阶段 R/C/N/A、角色和记录映射明确 | PROJECT |
| Discover & Frame | 为什么做、为谁做、期望改变什么？ | 人与 AI 对 Why、对象、结果、约束、假设和非目标达成一致 | PROJECT / REQUIREMENTS |
| Contract | 做什么、怎么验收、何时停止？ | 范围、验收、安全、责任、Human Gate 和结论口径冻结 | REQUIREMENTS |
| Design | 采用什么方案，为什么？ | 重要候选、取舍、接口、风险和验证设计经适当 Review/Approve | TECH_DESIGN / UX_SPEC / Decision |
| Plan & Prepare | 如何拆分、以什么顺序安全推进？ | 可验证增量、依赖、环境、证据、Gate 和 checkpoint 就绪 | DELIVERY_PLAN / TECH_DESIGN / VALIDATION |
| Implement & Verify | 当前最小增量是否真实通过？ | Evidence Gate 通过；失败不进入依赖任务 | VALIDATION / Evidence |
| Integrated Acceptance | 各部分合起来是否满足 Contract？ | 自动验证、外部回读及适用的人工验收完成 | VALIDATION / UAT |
| Release / Delivery | 如何把正确版本交给正确对象？ | 身份、版本、目标、权限、交付结果和回滚可核验 | RELEASE / HANDOFF |
| Operate / Observe | 如何知道它仍然可用并在失败时恢复？ | 适用的监控、升级、恢复和责任边界明确 | RUNBOOK / Operations evidence |
| Handoff / Close / Learn | 如何复核、恢复、继续或关闭？ | 最终入口、结论、限制、遗留项和恢复方法可定位 | HANDOFF / Retrospective |

启用阶段至少回答：Purpose、Applicability、Ownership、Entry、Inputs、Actions、AI Boundary、Validation、Record、Exit Gate、Recovery。小项目可以把这些字段合并到少量文件。

## 4. 人机协作责任

责任表达分为执行者与控制方式：

- 执行者：`AI`、`Human`、`Shared`、`Automation`；
- AI 动作：`AI Draft`、`AI Execute`、`AI Recommend`；
- 人工控制：`Human Review`、`Human Approve`、`Human Execute`。

AI 可以在已冻结边界内起草、分析、实现和验证，但不能自行批准影响范围、风险、外部系统、共享发布或主观验收的 Human Gate。每个 Gate 必须有可识别的 Approver；多人项目可以增加 Accountable、Contributor、Reviewer 和 Consulted，小项目只需记录 Owner、Executor 和必要 Approver。

传统岗位可以映射到同一流程，但岗位名称不是强制结构：

| 生命周期环节 | 常见人类角色 | AI 常见协作方式 |
| --- | --- | --- |
| Discover / Contract | 产品经理、业务负责人、领域专家、项目负责人 | 整理背景、澄清问题、起草需求和验收候选 |
| Design | UI/UX、架构师、技术负责人、数据/安全专家 | 生成备选方案、原型、接口草案和反方检查 |
| Plan / Implement | 项目经理、技术负责人、开发、内容或数据执行者 | 拆分任务、实现、局部验证和证据整理 |
| Integrated Acceptance | QA、产品、最终用户、业务验收人 | 自动检查、差异分析和验收记录；不代替主观签字 |
| Release / Operate | 发布工程师、DevOps、SRE、系统管理员 | 发布前检查、可观测性分析和恢复建议；高风险动作需授权 |
| Handoff / Close | 项目 Owner、维护者、接收团队 | 汇总入口、限制、恢复方法和后续边界 |

同一个人可以承担多个角色；关键是责任和批准权可识别，而不是为小项目制造完整组织架构。

### 4.1 执行控制协议

项目不能依赖聊天记忆或“AI 应该记得”。每次开始新执行会话、从中断恢复或切换执行者时，先完成以下恢复握手：

```text
读取固定 Playbook 基线与根入口
→ 读取冻结 Contract 和唯一滚动 VALIDATION
→ 复述当前阶段、当前任务、允许/禁止范围、Blocker、下一 Gate 和 checkpoint
→ 核对入口条件
→ 执行一个增量并立即验证
→ 先更新证据与控制状态，再进入下一任务
```

若权威记录缺失、互相冲突、过期或无法确认当前 Gate，必须停止首次修改，把问题记录为 `Evidence Gap` 或 `Governance Failure`，不能凭对话印象继续。

适合机器检查的约束应尽量交给脚本、CI、Schema、测试或静态检查，例如：固定基线存在、必需记录可定位、`Passed` 关联证据、发布关联 Human Gate、Git/checkpoint 可识别。机器检查不能代替产品取舍、风险接受和主观验收。

### 4.2 跨会话协调模式

跨对话流转以仓库证据为权威，不以复制完整聊天记录为默认方式。项目按成本和时效选择：

- `Human Relay`：默认的低 Token 模式。执行会话更新正式记录并返回紧凑摘要，由人类审核后把下一项任务交给后续会话；
- `Automatic Orchestration`：主控会话自动派发、等待和回读。仅在无人值守或时效收益足以覆盖 Token、协调和误读成本时采用。

两种模式使用同一个最小转移包：仓库与路径、固定基线、分支与 HEAD、当前 Gate、权威文档入口、验证结果、Decision/Deviation/Blocker、下一项唯一动作。长日志和完整对话不进入转移包；需要复核时回读仓库证据。模式可以在阶段间切换，但必须在当前 Validation 记录。

### 4.3 会话、计算资源与权限适配提醒

这是轻量 Guidance，提醒收益仍待项目验证，不新增固定 Gate 或每次调用的记录要求。AI 在开工/恢复、阶段边界、目标或职责明显变化，以及约定反复混淆、重复失败或证据矛盾时，评估当前会话、计算资源与权限是否适配；无明显问题就继续，只在需要人类决定时提出简短建议。

- **会话**：同一目标、责任与可信基线且上下文清晰时继续。独立实验、不同仓库、需要隔离职责或上下文持续混淆时，建议先交接再新开；优先选择阶段验收、checkpoint 等自然边界，不因对话长或职责改变就机械切换。长期 Maintainer 对话可以继续承担后续职责。新会话使用 §4.2 转移包恢复，不重新讨论或擅自改变冻结 Contract。
- **计算资源**：以任务歧义、复杂度、风险、工具能力、质量底线和成本/时效选择模型与推理强度。明确小修改可考虑较轻配置；复杂方案、归因或高风险审查可考虑更强配置，但不是硬性任务—模型映射。重复失败先检查输入、方法、环境和权限，再判断是否升级；更高强度不保证正确，不能替代独立验证。具体模型、价格和可用设置不写死在 Core；必要时核对工具当前官方说明。
- **权限**：先核对具体文件、网络、工具与外部写入需要。被阻塞时区分必要权限缺失与环境/工具故障；优先请求具体操作的单次授权，重复需要时才建议项目范围的最小权限配置。说明用途、扩大范围、风险和恢复原配置的方法；不因审批频繁或反复报错就推荐完全访问，不绕过拒绝。批准工具权限不等于批准新需求或外部发布。

提醒格式：`触发原因 → 建议继续/交接/调整哪一项 → 影响与边界 → 由人决定`。模型能力、推理强度和工具权限是独立维度；AI 不擅自新建或向其他对话派发任务、切换模型或修改权限。无法确认当前配置、额度或计量结果时明确未知，不猜测。仅影响安全、路线、成本约束或结果解释的重大选择/切换记录到现有 Decision/Validation；其余不增加流水账。

## 5. 术语与状态

| 术语 | 定义 |
| --- | --- |
| Contract | 冻结的目标、范围、路线、验收、安全和责任约定 |
| Run / Change Set | 基于同一 Contract、在受控工作状态内完成的一次正式尝试或变更批次 |
| Trusted baseline | 可追溯的启动状态，可以是种子、模板、脚手架或已记录的空目录 |
| Evidence | 支撑判断的机器结果、差异、日志、截图、外部回读或人工确认 |
| Gate | 决定是否允许进入下一依赖步骤的检查点 |
| Human Gate | 未经指定人工明确确认不得继续的 Gate |
| Decision | 对范围、路线、安全或重要实现策略的显式取舍 |
| Deviation | 实际执行相对 Contract 或 Playbook 的偏离 |
| Blocker | 使当前 Gate 无法通过、需要处置或外部状态变化的条件 |
| Rollback point | 能恢复到已知状态并识别其来源的版本或快照 |
| Handoff | 面向复核和后续工作的最终结论、入口、证据与限制说明 |
| Maintainer | 有权修改和发布 Playbook 基线的角色 |

规则等级：`Required` 必须遵守；`Provisional` 必须评估反馈但允许证明其不合理；`Guidance` 是可裁剪建议。

执行状态统一使用：`Not Started`、`In Progress`、`Passed`、`Passed with Limitations`、`Blocked`、`Failed`、`Not Applicable`。只有限制不影响当前 Gate 核心结论时，才可使用 `Passed with Limitations`。

## 6. 核心规则

### 生命周期、发现与责任

- **R-LFC-001 · Required**：正式项目必须选择一个基础画像、适用的风险修饰器，并记录每个阶段的 `Required / Conditional / Not Applicable + 理由`；风险只能增强流程。Contract 新增交付形态或风险时必须重新裁剪。
- **R-LFC-002 · Required**：启用阶段必须有可定位的目的、责任、输入、验证、记录、退出 Gate 和恢复条件。阶段与文件可以合并，但不得建立冲突的第二套生命周期。
- **R-FRM-001 · Required**：实施前必须对齐问题背景、为什么做、目标对象、期望结果、约束、关键假设和非目标，并用可验证的语言表达；实验性主张还必须可证伪。
- **R-RSP-001 · Required**：项目必须指定结果 Owner、Executor、必要 Reviewer/Approver 和 AI 权限边界；AI 不得依据沉默或推测越过 Human Gate。

### 执行控制

- **R-CTL-001 · Required**：执行中的项目必须在唯一滚动 Validation 中维护当前阶段、当前任务、允许与禁止范围、Blocker、下一 Gate、最新证据和 Rollback point。每次新会话、恢复或执行者切换时，AI/执行者必须在首次修改前读取、核对并复述该状态；状态缺失或冲突时停止执行。
- **R-CTL-002 · Guidance**：对可机器判断且重复执行的约束，优先提供脚本、CI、Schema 或静态检查；项目必须区分“已自动强制”“仅记录提醒”和“需要人工判断”，不得把文档声明冒充自动执行。
- **R-CTL-003 · Guidance**：AI 应在 §4.3 的必要节点评估会话、计算资源和权限适配，并在需要人类决定时简短提醒；不频繁打扰、不擅自切换或扩大授权。建议效果待验证，既有安全与 Human Gate 的 Required 边界不因本 Guidance 降低。

### Contract、安全与工作区

- **R-CTR-001 · Required**：正式实施前必须冻结输入、输出、主路线、允许修改范围、验收标准、停止条件和结论分级。Contract 变更使用 Decision 记录并形成独立版本点。
- **R-CTR-002 · Required**：Contract 必须列出 Human Gate、继续条件、所需证据和各方责任。
- **R-SAF-001 · Required**：Contract 必须声明数据分类、密钥/PII/本机信息处理、外部权限、破坏性操作、对外发布和证据脱敏边界。
- **R-DOC-001 · Required**：项目根目录必须有 README 或等价入口，说明状态、使用入口、权威记录和 Artifact Map；需求、设计、实现、验证证据、交付运维和可重建临时产物必须可区分，但不要求统一目录名。
- **R-WRK-001 · Required**：固定输入、Trusted baseline、工作副本、正式证据和可重建临时文件必须可区分；不得在已验证基线原件上直接实验。
- **R-PFL-001 · Required**：执行前必须核实必要环境、版本、权限、工具能力、目标身份和回滚条件。必要能力缺失时不得静默切换路线。

### 设计与计划

- **R-DSN-001 · Required**：当存在重要产品、UX、架构、接口、数据、安全、依赖或部署取舍时，必须比较可行方案、代价与风险，记录选择理由，并在实现前由指定 Approver 冻结。
- **R-DSN-002 · Guidance**：高歧义、高风险或高投入决策可采用独立多视角评审，包括多个 AI、领域专家或反方提示；应记录分歧和依据，不能把共识当作事实证明。
- **R-PLN-001 · Required**：实施型项目必须把任务拆为可独立验证的增量，并记录依赖、责任、完成定义、验证、证据、风险和 checkpoint；未通过的增量不得解锁依赖任务。
- **R-PLN-002 · Guidance**：默认先消除阻塞并验证高代价不确定性，再建立最小端到端闭环，随后由低耦合增量扩展到复杂集成；不机械采用“由易到难”。

原始需求、已批准 Contract 与未来 Backlog 应能区分，但不要求创建三份文件；小项目可以在同一 Requirements 中分节保存。原始表达用于防止整理过程改变意图，只有经确认的 Contract 才解锁实施，未批准想法不得悄然进入当前范围。

`Reference Scan` 是设计阶段的条件式 Guidance，不是所有任务的固定 Gate。面对常见产品/组件、新技术路线、重要依赖或许可证和安全风险时，先冻结自己的问题，再在 GitHub、官方实现或可信生态中限时筛选少量候选，记录“借鉴什么、拒绝什么、许可证/维护/安全边界”，必要时先做最小验证。明确的小修复、项目特有逻辑、已有可靠基线或无相关候选时可以跳过并简述理由。不得因参考项目功能丰富而扩大当前 Contract，也不得直接运行未经审查的安装脚本。

### Evidence Gate Kernel

- **R-EXV-001 · Required**：每个原子变更后必须立即执行约定验证、保存证据并完成 Gate 判定；失败的 Gate 不得继续其依赖步骤。
- **R-EXV-002 · Required**：Human Gate 必须记录请求、目标、预期、实际确认和继续授权；AI 不得自行代签。
- **R-EXV-003 · Provisional**：项目若声称减少人力、等待或机器耗时，必须在被测阶段开始前定义 Human active、wait 和 machine time 的计量口径；不作效率声明的项目无需计时。
- **R-VLD-001 · Required**：关键结论必须使用独立验收依据。验证逻辑不得完全依赖生成路径自身的成功声明；不适用时必须说明原因和替代证据。
- **R-VLD-002 · Required**：证据必须对应验收条款、可定位、必要时脱敏，并区分精确证明、辅助证明和人工观察。重复无变化状态可以压缩，但首态、末态、Blocking、异常和首次状态转换必须保留。
- **R-VLD-003 · Required**：存在持久化状态、外部宿主或发布环境时，Contract 必须按风险选择往返验证强度。高风险转换必须完整验证；已有完整往返、独立 diff/回读且无未解释差异的低风险重复检查可以抽样或省略，但必须记录理由与残余风险。

独立验收依据按项目选择：独立 Oracle；不变量、属性测试或静态检查；外部系统回读或真实运行；使用冻结量表的人工验收。可以组合使用。无法获得独立依据时只能报告观察，不能声明“证据完整”。

### 停止、回滚与恢复

- **R-STP-001 · Required**：异常必须同时记录类型和严重度。`Blocking` 停止后续依赖步骤；`Non-blocking` 只有在不影响核心结论时才可继续。
- **R-STP-002 · Required**：对影响 Gate 或需要采取恢复动作的异常，记录受影响的验收项/阶段、可观察现象、可能原因及其证据、影响和下一动作；明确区分已确认、待验证和未知原因，不得把猜测写成根因。修复或恢复后重验受影响的 Gate。原因排查应与风险相称，不要求低影响警告进行穷尽分析。
- **R-GIT-001 · Required**：关键已验证阶段以及可能覆盖、规范化或接管现有状态的高风险转换之前，必须有可识别的 Rollback point，并在 Validation 中记录。无法安全回滚时应作为治理阻塞。
- **R-GIT-002 · Guidance**：默认使用阶段级 Git checkpoint；高风险变更前可以增加保护性快照，不要求每个小动作提交。

Blocking 后依次判断：状态可信且 Contract 允许时原地重试；有明确回滚点时恢复并重验；状态不可信、路线改变或需要复杂替代方案时建立新 Run/Change Set。

事件至少区分：`Validation Failure`、`Environment Failure`、`Safety/Permission Blocker`、`Governance Failure`、`Evidence Gap`、`Expected Negative Result` 和 `Warning`。预期负面结果可以是完整实验结论，不等于执行失败。

原因排查可按需检查需求/验收、方案/依赖、输入/数据、实现、环境/工具、权限/目标身份、验证依据和记录/交接等方向；这只是排查线索，不是封闭分类，也不要求逐项填写。证据不足时保留“待验证”或“未知”，并说明需要的下一项检查。

### 验收、交付与运行

- **R-REL-001 · Required**：发布、部署、迁移、共享或覆盖外部状态前，必须确认目标身份、版本、权限、影响、回滚点和 Human Gate；完成后从目标环境回读并区分“已构建、已发布、已可用”。
- **R-OPS-001 · Required**：当项目存在长期运行责任时，必须定义最小健康信号、监控/检查方式、责任人、故障升级、恢复方法和不在保障范围内的内容。
- **R-VDC-001 · Required**：最终结论必须分别报告功能结果、Contract 符合度、证据完整度、运行/持久化状态和已知边界，不得用单一“成功”掩盖缺口。
- **R-VDC-002 · Required**：项目若声明“最少步骤”或推荐生产工作流，必须区分固定生产必需、条件式生产、诊断和验证专用操作；实验中发生过的动作不得自动成为生产要求。
- **R-HOF-001 · Required**：Handoff 必须包含最终结论与非结论、交付入口、证据和 checkpoint 地图、复核方法、限制、Decision/Deviation 摘要、恢复及后续边界。滚动状态只以 Validation 为权威，Handoff 不复制其全部过程。

### 治理与反馈

- **R-GOV-001 · Required**：只有 Maintainer 可以修改或发布 Playbook。实验项目固定所用提交，不得在执行期间修改该基线。
- **R-FBK-001 · Required**：当项目用于验证 Playbook 时，必须分别评价 Rule conformity 与 utility，并把问题初步分类为 Core、Template、Adapter、Project-specific 或 Evidence gap。

## 7. 记录与文件

所有正式项目至少保留四类逻辑记录：`PROJECT`、`REQUIREMENTS`、`VALIDATION`、`HANDOFF`。重大决策或偏差使用 `DCS-001`、`DEV-001` 稳定编号。

`TECH_DESIGN`、`DELIVERY_PLAN`、`UX_SPEC`、`UAT`、`RELEASE_PLAN`、`RUNBOOK` 和 `PLAYBOOK_FEEDBACK` 按触发条件启用。逻辑记录可以合并到一个物理文件，但必须在根入口的 Artifact Map 中可定位。详细映射与示例见 [项目结构与记录指南](PROJECT_STRUCTURE.md)。

文档还可以按主要职责标记为：`Normative`（以后应怎样做）、`Baseline`（当前已经批准什么）和 `Record`（实际上发生了什么）。分类用于识别权威与更新方式，不要求为每类新建目录或重复文档。

## 8. Decision、Deviation 与变更

- 小型、可逆且不影响 Contract 的操作选择无需记录；
- 影响范围、验收、安全、技术路线或后续依赖的取舍记录为 Decision；
- 实际执行偏离 Contract 或 Playbook 时记录 Deviation；
- Validation 只引用编号，不重复整段记录；记录可以引用 Rule ID、证据和 Git 提交；
- 冻结后不得静默改写需求或成功口径以适配结果。

## 9. Playbook 验证与版本治理

实验采用固定 Playbook 提交。采用前规划必须保留；为符合 Playbook 作出的变化区分为 `Risk Correction`、`Operational Clarification`、`Playbook-only Alignment`、`No Change`。高 conformity 或 `Playbook-only Alignment` 不能单独证明规则有用。

明显排版或链接错误若不阻塞执行，先登记而不修改固定基线；阻塞性错误只能由 Maintainer 形成独立 erratum，并重新声明实验实际使用的提交号。

Maintainer 吸收旧流程或单项目经验前必须做轻量性审查：它是否解决真实或高影响问题、能否跨项目复用、执行成本是否合理、是否有更轻的模板/自动检查/Guidance、应放在 Core/Template/Adapter/Case Study 哪一层。只有重复出现或高损失的问题才优先进入 Required；每次增加规则同时检查能否合并、降级或移除旧内容。高 Conformity 不能证明规则值得保留。

v1.0.1 仍未充分验证：效率计量、完整生产服务运维、多团队协作、高风险/监管项目、多 AI 评审增益、Reference Scan 的实际收益和 Power BI Service 浏览器 Skill 路线。使用这些能力时必须增强 Contract 与证据，不能引用本版本声称它们已经普遍成立。

会话、计算资源与权限适配提醒的频率、质量和实际成本收益也待后续项目验证；不据此声明已有模型选择或提效实验结论。
