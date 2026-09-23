# V1 Zero Seed — Playbook v0.1 反馈

- Playbook 基线：`v0.1` @ `3ee871d618db84d55b3b2f86a198ac552864317e`
- 需求冻结：`82b448957ab08a5452df297a7a95d7b6def67bef`
- Run A/B final：`21af7b278d9be6c40ca7315fb0dd5298e3565506` / `a127b7978990d1d0c6027a72c689704dd5b09a04`
- 最终验收：R7 result checkpoint；完整 SHA 在 metadata/reporting commit 与最终报告中记录

## 1. 总体评价

- Required Rules：运行时全部 `Conformant`。冻结 Contract、Execute–Verify、Human Gate、异常严重度、阶段 checkpoint、五维结论与 Handoff 均有实际证据。
- Provisional R-VLD-003：A/B 均按规则执行并单独计量。Conformity 为 `Yes`；utility 为 `Low positive marginal value`；建议 `Change`。
- Playbook 的主要帮助：在首开前冻结范围和来源；将生成拆成可停止的原子步骤；让 Human 操作、MCP 回读和 Codex 文件操作可分离审计；避免用单一“成功”掩盖公共 Schema 缺口。
- 最大摩擦或冗余：核心往返已通过且有精确 manifest 与 MCP 回读后，再做一次完整 Desktop 往返在两组中都没有产生新发现；精确时间采集没有被前置到 Gate 流程，导致 utility 成本只能部分量化。

高 Conformity 不代表高 Utility。下表的符合性只说明 V1 按 v0.1 执行；utility 只依据本项目实际观察，不推导跨项目有效性。

## 2. Rule conformity 与 utility

| Rule ID | Conformity | Utility | V1 证据/问题 | 建议 |
| --- | --- | --- | --- | --- |
| R-FRM-001 | Yes | Helpful | 可证伪问题与范围外内容阻止 V1 扩展到完整 V0 业务模型 | Keep |
| R-CTR-001 | Yes | Helpful | `82b4489` 固定来源、路线、验收、停止和三级结论；未因结果回写 Contract | Keep |
| R-CTR-002 | Yes | Helpful | HG-00–HG-05 明确目标、禁止动作和继续授权；避免未经授权保存/关闭 | Keep |
| R-SAF-001 | Yes | Helpful, mostly preventive | 只读权限提升被记录；无凭据、发布、破坏操作或无关数据访问 | Keep |
| R-WRK-001 | Yes | Essential for this experiment | 0 文件/0 子目录与禁止来源边界是“零种子”结论的必要前提 | Keep |
| R-PFL-001 | Yes | Helpful | 两个 Run 都重新核实 Desktop/MCP/进程/权限；实际发现只读权限差异 | Keep |
| R-EXV-001 | Yes | Helpful | Run A R2b 的 Blocking GEN 在 Report 生成前被捕获；依赖链停止并原子重验 | Keep |
| R-EXV-002 | Yes | Helpful | Human 未明确确认时没有越 Gate；每次都核对项目身份与提示 | Keep |
| R-VLD-001 | Yes | Helpful | Schema/不变量、manifest、Desktop、Human 与 MCP 组合，避免生成器自证 | Keep |
| R-VLD-002 | Yes | Helpful | 精确磁盘 diff、产品观察和辅助回读被分级；`$schema` 缺口没有被隐藏 | Keep |
| R-VLD-003 | Yes | Low positive marginal value | 两次附加往返均 0 新发现；只增加第三次独立启动的重复性信心 | Change |
| R-STP-001 | Yes | Helpful | Blocking GEN 与 Non-blocking ENV/SPEC 分开；没有把工具假差异当产品失败 | Keep |
| R-GIT-001 | Yes | Helpful | freeze、pre-open、首存、核心往返和 Run final 均可回滚 | Keep |
| R-GIT-002 | Applied | Helpful | 阶段级提交足以定位状态，没有为每个文件动作制造提交噪声 | Keep |
| R-VDC-001 | Yes | Helpful | 最终五维判定允许“功能 Passed”与 Schema/计量限制并存 | Keep |
| R-HOF-001 | Yes | Helpful at handoff, not independently consumer-tested | 最终入口、复核方法、checkpoint 和不能声称内容集中；尚无下游复核结果 | Keep |
| R-GOV-001 | Yes | Helpful | v0.1 为真实祖先；`playbook/**` 在 freeze 后零差异；问题只进入反馈 | Keep |
| R-FBK-001 | Yes | Helpful | 强制把 conformity 与 utility 分开，避免把执行 R-VLD-003 当成规则有效证明 | Keep |

## 3. R-VLD-003 成本与价值

| 指标 | Run A | Run B | 合计/观察 |
| --- | --- | --- | --- |
| Playbook-only 额外 Desktop 启动 | 1 | 1 | 2 |
| Human 主动耗时 | “约几秒” | “约几秒” | 定性值；未精确计量 |
| 机器检查分钟 | 2.34 | 0.04 | 约 2.38；口径在各 metrics 文件中说明 |
| 主要新增证据 | 2 文件 / 5265 bytes | 2 文件 / 5146 bytes | 4 文件 / 10411 bytes |
| 新发现 | 0 | 0 | 0 |
| 捕获问题 / 避免错误结论 | 0 / 0 | 0 / 0 | 0 / 0 |
| 新增信心 | 第三个独立进程仍稳定 | Unicode+空格路径第三个进程仍稳定 | 重复性信心增加，无新结构/语义信息 |

建议 `Change`，不建议在 V1 中直接修改规则：

- 对已经完成一次完整保存/关闭/重开、精确磁盘 diff 和独立语义回读的低风险最小项目，将最终再次完整往返改为风险触发或抽样。
- 对宿主会重写持久化状态、缺少独立回读、存在未解释 diff、复杂模型/数据或高代价错误的项目，继续保留最终往返。
- 模板应在发出 Human Gate 时就开始记录 active/wait/machine 时间，而不是在 R6 后追溯。

## 4. 采用前规划对比

| 原规划内容 | 采用 v0.1 后的变化 | 分类 | 实际效果 |
| --- | --- | --- | --- |
| 可证伪问题、范围外、A/B、三级结论 | 不变 | No Change | 冻结口径足以给出完全零种子结论，未为证明 Playbook 改造问题 |
| 来源污染和空目录证据 | 不变 | No Change | 成为业务结论的关键证据 |
| PBIP/模型/Report 一次生成 | 拆为 R2a–R2d | Operational Clarification | Run A 的 TMDL GEN 错误在依赖 Report 生成前被捕获，实际有用 |
| 人工动作日志 | 增加编号 Gate、目标、预期与继续授权 | Risk Correction | 两组均保持“先机器验证、后人工动作”，没有越 Gate |
| 安全边界 | 增加权限、敏感信息、发布与不可逆操作边界 | Risk Correction | 支持只读权限事件的正确停止/恢复；其余主要是预防价值 |
| 异常记录 | 增加事件类型、严重度和 V1 主因 | Risk Correction | 使 Blocking GEN、Non-blocking 工具问题和产品 Evidence Gap 可区分 |
| 五维结论、Handoff、Feedback | 新增 | Playbook-only Alignment | 五维结论和反馈分离实际改善了限制表达；Handoff 尚未被下游独立检验 |
| 第一次保存/关闭/重开 | 保持核心验收 | No Change | 产生首存差异、稳定重开和 MCP 身份等主要发现，不归因于 Playbook-only utility |
| 第二次最终往返 | 新增并单独计量 | Playbook-only Alignment | 两组均无新发现，提供 Change 建议的直接证据 |

## 5. 问题分类

| 问题 | 初步分类 | 观察、影响与建议处理位置 |
| --- | --- | --- |
| 核心往返已强验证后仍无条件重复完整最终往返 | Core | 两组 0 新发现；建议 Maintainer 在 v0.2 评估风险触发/抽样条件 |
| Human active/wait 时间没有在 Gate 发出时前置采集 | Template | 影响成本精度；在 Gate/metrics 模板中加入开始、结束与口径字段 |
| Desktop canonical 根文件移除公开 Schema required `$schema` | Evidence gap | 不能声称原样直接 Schema 通过；建议 Power BI adapter 记录“产品 canonical 输出 vs 公开 Schema”处理方式 |
| 多次压缩 PowerShell 比较器/路径分隔符产生假失败 | Project-specific | 已停止并从头重跑；建议项目脚本保持可读、多行并使用平台路径 API，不上升为通用 Playbook 规则 |
| Handoff 的实际下游可复核价值尚未观察 | Template | 当前只证明产物符合；由 Playbook 对话读取 V1 后再评价消费端价值 |

分类只是 V1 的观察、影响和建议。是否修改 Playbook、模板或 adapter 由 Playbook Maintainer/后续对话决定。

## 6. 反馈附件

- [HANDOFF](HANDOFF.md)
- [VALIDATION](VALIDATION.md)
- [Decision/Deviation](RECORDS.md)
- [采用前符合性](PLAYBOOK_CONFORMITY.md)
- [R7 evidence](r7/ACCEPTANCE_EVIDENCE.md)
- 两组成本明细：`runs/*/logs/R-VLD-003-METRICS.json`
- 相关提交：`3ee871d`、`22da780`、`8c28f5e`、`82b4489`、`21af7b2`、`a127b79`、R7 result checkpoint
