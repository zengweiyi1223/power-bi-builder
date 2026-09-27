# V1 Zero Seed — Playbook v0.1 符合性检查

- 固定 Playbook：`v0.1` @ `3ee871d618db84d55b3b2f86a198ac552864317e`
- 采用前 V1 草案：`22da780412f27decf17a097548d65d151c75b235`
- no-ff merge：`8c28f5e340ec41ef56e16d942fd2f9eb97767963`
- 检查日期：2026-09-22，America/Los_Angeles
- 检查范围：规划与 Contract 符合性；运行时符合性尚未验证

## 1. 判定口径

- `Planned Conformant`：冻结 Contract 已覆盖规则；仍需 Run 证据证明实际执行符合。
- `Not Yet Evaluated`：必须通过正式 Run 评价。
- `N/A`：有明确理由和替代证据。

采用 v0.1 导致的修改按四类记录。`Playbook-only Alignment` 仅证明文档或流程对齐，不证明规则有用。

## 2. Required Rules

| Rule ID | 采用前检查 | 调整分类 | 冻结后规划状态 | V1 证据位置 |
| --- | --- | --- | --- | --- |
| R-FRM-001 | 已有可证伪问题、范围外和三级结论 | No Change | Planned Conformant | `REQUIREMENTS.md` §1、§7 |
| R-CTR-001 | 已有路线、验收和停止思想，但输入/输出/允许修改/checkpoint 分散 | Operational Clarification | Planned Conformant | `REQUIREMENTS.md` §2、§5、§6、§8 |
| R-CTR-002 | 有角色日志，缺少带编号的 Human Gate、继续条件和授权证据 | Risk Correction | Planned Conformant | `REQUIREMENTS.md` §3 |
| R-SAF-001 | 缺少完整数据分类、密钥/PII、外部权限、不可逆操作和脱敏契约 | Risk Correction | Planned Conformant | `REQUIREMENTS.md` §4 |
| R-WRK-001 | 已区分空目录、Run、证据和缓存 | No Change | Planned Conformant | `BASELINE.md` §5；`REQUIREMENTS.md` §8 |
| R-PFL-001 | 已有版本/进程预检，目标身份、权限和回滚条件不够集中 | Operational Clarification | Planned Conformant | `REQUIREMENTS.md` R0；`RUN_RECORD_TEMPLATE.md` §2 |
| R-EXV-001 | 原计划按阶段验证，但 PBIP/模型/报告生成仍可被理解为批量动作 | Operational Clarification | Planned Conformant | `EXPERIMENT_PLAN.md` §4 的 R2a–R2d |
| R-EXV-002 | 人工动作已分离记录，但未冻结请求/目标/预期/确认/继续授权 | Risk Correction | Planned Conformant | `REQUIREMENTS.md` §3；`EXPERIMENT_PLAN.md` §5 |
| R-VLD-001 | 已组合静态检查、Desktop 和 MCP，但未明确生成逻辑与验证逻辑的独立边界 | Operational Clarification | Planned Conformant | `REQUIREMENTS.md` §5；`EXPERIMENT_PLAN.md` §6 |
| R-VLD-002 | 已有 manifests/diff，缺少精确证明、辅助证明、人工观察的显式区分 | Operational Clarification | Planned Conformant | `REQUIREMENTS.md` §5；`VALIDATION.template.md` |
| R-STP-001 | 已有 V1 主因，缺 Playbook 事件类型和 Blocking/Non-blocking 严重度 | Risk Correction | Planned Conformant | `REQUIREMENTS.md` §6；`RUN_RECORD_TEMPLATE.md` §5 |
| R-GIT-001 | 有预打开快照，关键阶段的 rollback map 不完整 | Operational Clarification | Planned Conformant | `REQUIREMENTS.md` §8；`VALIDATION.template.md` |
| R-VDC-001 | 原结论偏重功能分级 | Playbook-only Alignment | Planned Conformant | `VALIDATION.md`、`HANDOFF.md` 的五维结论 |
| R-HOF-001 | 原草案没有项目级 Handoff 文件 | Playbook-only Alignment | Planned Conformant | `HANDOFF.md` |
| R-GOV-001 | 已要求独立 V1，不修改 V0；v0.1 接入方式尚未存在 | No Change | Planned Conformant | Git 祖先关系；`BASELINE.md` §1 |
| R-FBK-001 | 原草案没有 Rule conformity/utility 分离反馈 | Playbook-only Alignment | Planned Conformant | `PLAYBOOK_FEEDBACK.md` |

## 3. Provisional 与 Guidance

| Rule ID | 等级 | 采用前检查 | 调整分类 | 冻结后处理 |
| --- | --- | --- | --- | --- |
| R-VLD-003 | Provisional | 首次保存/关闭/重开已是实验核心；没有单独的最终再次检查或成本/价值指标 | 核心首次往返：No Change；最终再次往返与计量：Playbook-only Alignment | 应用。分别记录 Core roundtrip 与 Playbook-only final roundtrip 的时间、启动次数、证据量、唯一发现、反事实风险和建议。Utility 为 Not Yet Evaluated。 |
| R-GIT-002 | Guidance | 已计划 Git 快照但粒度未明确 | Operational Clarification | 采用阶段级 checkpoint，不为每个小动作提交。 |

## 4. 采用前规划变更摘要

| 原规划内容 | v0.1 后变化 | 分类 | 理由 |
| --- | --- | --- | --- |
| 核心问题、空目录、A/B、三级结论、污染边界 | 保持 | No Change | 已直接服务实验可证伪性和重复性。 |
| PBIP/模型/报告生成阶段 | 拆成 R2a/R2b/R2c，每步立即验证 | Operational Clarification | 消除“全部生成后统一验证”的歧义。 |
| 人工操作独立日志 | 增加 HG-00–HG-05、请求和继续授权 | Risk Correction | 防止打开错误项目、未经确认保存或越 Gate。 |
| 安全说明 | 增加数据分类、秘密/PII、权限、发布、破坏操作和脱敏 | Risk Correction | 原草案无法回答权限或敏感提示出现时如何停止。 |
| 失败主因 | 增加 Playbook 事件类型与严重度双轴 | Risk Correction | 让 Blocking 与预期负面结果可区分。 |
| Handoff/Feedback/五维结论模板 | 新增 | Playbook-only Alignment | 满足固定输出结构；是否有用待 Run 后评价。 |
| 最终第二次往返 | 新增并单独计量 | Playbook-only Alignment | 专门评价 R-VLD-003，不把执行本身当作有效性证据。 |

## 5. 冻结 Gate 结论

规划层面覆盖全部 Required Rules，R-VLD-003 已有可计量评价设计，R-GIT-002 采用方式明确。该结论只允许形成规划冻结 checkpoint；它不证明运行时 conformity、规则 utility 或零种子业务结果。

正式 Run 前仍需 `HG-00` 明确授权。
