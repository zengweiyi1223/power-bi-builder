# 证据闸门式 AI 项目闭环

版本：`v0.1`

本 Playbook 将 Power BI Builder V0 已形成但未显式命名的工作方式规范化。它适用于需要 AI 生成或修改制品，并要求结果可验证、可停止、可回滚和可交接的项目。

## 1. 核心流程

```text
Frame → Contract → Prepare → Preflight
                         ↓
       [ Execute → Verify → Gate → Checkpoint ] × N
                         ↓
                    Decide → Handoff & Feedback
```

`Execute–Verify` 是原子循环：每次只实施一个可验证增量，立即验证并保存证据；Gate 通过后才进入下一依赖阶段。

## 2. 术语

| 术语 | 定义 |
| --- | --- |
| Contract | 冻结的目标、范围、路线、验收、安全和责任约定。 |
| Run | 基于同一 Contract、在一个隔离工作副本内完成的一次正式尝试。 |
| Trusted baseline | 可追溯的启动状态，可以是种子、模板、脚手架或已记录的空目录。 |
| Evidence | 支撑某项判断的机器结果、差异、日志、截图或人工确认。 |
| Gate | 决定是否允许进入下一依赖阶段的检查点。 |
| Human Gate | 未经指定人工明确确认不得继续的 Gate。 |
| Decision | 对范围、路线、安全或重要实现策略的显式取舍。 |
| Deviation | 实际执行相对 Contract 或 Playbook 的偏离。 |
| Blocker | 使当前 Gate 无法通过、需要外部状态变化或处置的条件。 |
| Rollback point | 能恢复到已知状态并识别其来源的版本或快照。 |
| Handoff | 面向复核和后续工作的最终结论、入口、证据与限制说明。 |
| Maintainer | 唯一有权修改和发布 Playbook 基线的角色。 |

## 3. 规则等级与状态

- `Required`：必须遵守；未经批准的偏离会使项目不符合本 Playbook。
- `Provisional`：必须评估并反馈；明确的不适用或受控偏离不自动构成违规。
- `Guidance`：建议做法，可按项目情况选择。

阶段状态统一使用：`Not Started`、`In Progress`、`Passed`、`Passed with Limitations`、`Blocked`、`Failed`、`Not Applicable`。只有限制不影响当前 Gate 的核心结论时，才可使用 `Passed with Limitations`。

## 4. 核心规则

### Frame 与 Contract

- **R-FRM-001 · Required**：正式项目必须定义一个可证伪的核心问题，并列出不在本轮证明的内容。
- **R-CTR-001 · Required**：正式 Run 前必须冻结输入、输出、主路线、允许修改范围、验收标准、停止条件和结论分级。Contract 变更使用 Decision 记录并形成独立版本点。
- **R-CTR-002 · Required**：Contract 必须划分 AI、人工和共同责任，列出 Human Gate、继续条件及所需证据。
- **R-SAF-001 · Required**：Contract 必须声明数据分类、密钥/PII/本机信息处理、外部权限、破坏性操作、对外发布和证据脱敏边界。

### Prepare 与 Preflight

- **R-WRK-001 · Required**：固定输入、Trusted baseline、Run 工作副本、正式证据和可重建临时文件必须可区分；不得在已验证基线原件上直接实验。
- **R-PFL-001 · Required**：执行前必须核实必要环境、版本、权限、工具能力、目标身份和回滚条件。必要能力缺失时不得静默切换路线。

### Execute–Verify Loop

- **R-EXV-001 · Required**：每个原子变更后必须立即执行约定验证、保存证据并完成 Gate 判定；失败的 Gate 不得继续其依赖步骤。
- **R-EXV-002 · Required**：Human Gate 必须记录请求、目标、预期、实际确认和继续授权；AI 不得依据推测自行越过。
- **R-VLD-001 · Required**：关键结论必须使用独立验收依据。验证逻辑不得完全依赖生成路径自身的成功声明；不适用时必须说明原因和替代证据。
- **R-VLD-002 · Required**：证据必须与验收条款对应、可定位、经过必要脱敏，并区分精确证明、辅助证明和人工观察。
- **R-VLD-003 · Provisional**：存在持久化状态或外部宿主重写时，应在下游工作前执行保存/关闭/重开/回读或等价往返验证，并在最终验收前再次检查。Playbook 验证项目必须评价该规则的成本和价值。

### 停止、回滚与恢复

- **R-STP-001 · Required**：异常必须同时记录类型和严重度。`Blocking` 会停止后续依赖步骤；`Non-blocking` 只有在不影响核心结论时才可继续。
- **R-GIT-001 · Required**：关键已验证阶段必须具有可识别的 Rollback point，并在 Validation 中记录。若无法安全回滚，应作为治理阻塞而不是技术失败。
- **R-GIT-002 · Guidance**：默认使用阶段级 Git checkpoint；高风险变更前可以增加保护性快照，不要求每个小动作提交。

Blocking 后按以下顺序判断：

1. Contract 已允许、状态仍可信且不覆盖失败证据时，可在原 Run 内重试。
2. 有明确回滚点时，可回滚、重新验证后继续。
3. 状态不可信、路线改变或需要复杂替代方案时，新建 Run。

事件类型至少区分：`Validation Failure`、`Environment Failure`、`Safety/Permission Blocker`、`Governance Failure`、`Evidence Gap`、`Expected Negative Result` 和 `Warning`。预期的负面实验结果可以是完整结论，不等于执行失败。

### Decide、Handoff 与治理

- **R-VDC-001 · Required**：最终结论必须分别报告功能结果、Contract 符合度、证据完整度、运行/持久化状态和已知边界，不得用单一“成功”掩盖缺口。
- **R-HOF-001 · Required**：Handoff 必须包含结论与非结论、交付入口、证据和 checkpoint 地图、复核方法、限制、Decision/Deviation 摘要及后续边界。
- **R-GOV-001 · Required**：只有 Maintainer 可以修改或发布 Playbook。实验项目固定所用提交，不得在执行期间修改 `playbook/**`。
- **R-FBK-001 · Required（Playbook 验证项目）**：实验必须分别评价 Rule conformity 与 utility，并把问题初步分类为 Core、Template、Adapter、Project-specific 或 Evidence gap。

## 5. 独立验收的选择

优先使用与项目相称的最强依据：

1. 独立 Oracle 或参考结果。
2. 不变量、属性测试、静态或 Schema 检查。
3. 外部系统回读或真实运行结果。
4. 使用预先冻结量表的人工验收。

同一标准可以组合多种证据。无法获得独立依据时可以报告观察结果，但不能声明该结论“证据完整”。

## 6. Decision 与 Deviation

- 使用 `DCS-001`、`DEV-001` 格式编号，在项目内保持稳定。
- 可以每项一个文件，也可以在 `DECISIONS.md`、`DEVIATIONS.md` 中累计。
- 小型、可逆且不影响 Contract 的操作选择无需记录。
- Validation 只引用编号，不重复全文；记录可以引用 Rule ID、证据路径和 Git 提交。

## 7. 冻结与反馈

实验采用固定 Playbook 提交。明显排版或链接错误若不阻塞执行，先登记而不修改基线；阻塞性错误只能由 Maintainer 形成独立 erratum，并重新声明实验使用的提交号。

实验不得用高 conformity 证明 Playbook 有效。采用前规划必须保留；为符合 Playbook 作出的修改需区分：`Risk Correction`、`Operational Clarification`、`Playbook-only Alignment`、`No Change`。其中 `Playbook-only Alignment` 只证明遵守，不证明规则有用。
