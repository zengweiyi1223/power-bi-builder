# V1 Zero Seed — Playbook v0.1 反馈

- Playbook 基线：`v0.1` @ `3ee871d618db84d55b3b2f86a198ac552864317e`
- 采用前 V1 草案：`22da780412f27decf17a097548d65d151c75b235`
- 需求冻结提交：本轮规划冻结提交，SHA 由 Git/报告记录
- 最终验收提交：`Not Started`

## 1. 当前总体评价

- Required Rules：规划层面均已映射；运行时 conformity 尚未评价。
- Provisional Rule R-VLD-003：已冻结可量化方案；utility 为 `Not Yet Evaluated`。
- Playbook 对风险、验证和交接的总体帮助：`Not Yet Evaluated`；只能记录采用时观察，不能在 Run 前判定有效。
- 最大摩擦或冗余：待 Run 后依据计时、证据量和唯一发现填写。

## 2. Rule conformity 与 utility

| Rule ID | 规划 Conformity | 运行 Conformity | Utility | 当前证据/问题 | 最终建议 |
| --- | --- | --- | --- | --- | --- |
| R-FRM-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 原草案已覆盖核心问题与非目标 | 待定 |
| R-CTR-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | Contract 已集中冻结 | 待定 |
| R-CTR-002 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 新增 HG-00–HG-05 | 待定 |
| R-SAF-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 新增安全/权限/脱敏边界 | 待定 |
| R-WRK-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 空目录 Trusted baseline 与 Run 分离 | 待定 |
| R-PFL-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | Run 时重新核实版本、权限、身份、回滚 | 待定 |
| R-EXV-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 生成拆成 R2a–R2d | 待定 |
| R-EXV-002 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | Gate 请求字段已冻结 | 待定 |
| R-VLD-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 组合 Schema/不变量/Desktop/MCP/Human | 待定 |
| R-VLD-002 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | Validation 映射证明等级 | 待定 |
| R-VLD-003 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 核心与附加往返分开计量 | 待定 |
| R-STP-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 事件类型+严重度+V1 主因 | 待定 |
| R-GIT-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 冻结/预开/首存/Run 最终/总验收 checkpoint | 待定 |
| R-GIT-002 | Applied (Guidance) | Not Yet Evaluated | Not Yet Evaluated | 使用阶段级 checkpoint | 待定 |
| R-VDC-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 五维最终结论 | 待定 |
| R-HOF-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | Handoff 骨架已建立 | 待定 |
| R-GOV-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | no-ff merge；playbook 只读 | 待定 |
| R-FBK-001 | Planned Conformant | Not Yet Evaluated | Not Yet Evaluated | 本文件分开记录 conformity/utility | 待定 |

高 Conformity 不代表高 Utility。仅为满足模板或规则而新增的文件、字段或第二次往返，必须依靠实际发现与成本评价。

## 3. 采用前规划对比

| 原规划内容 | 采用 v0.1 后的变化 | 分类 | 理由与待观察效果 |
| --- | --- | --- | --- |
| 可证伪问题、范围外、A/B、三级结论 | 不变 | No Change | 已满足实验目的；避免因采用 Playbook 改写问题。 |
| 来源污染和空目录证据 | 不变 | No Change | 原设计已直接控制种子污染风险。 |
| PBIP/模型/Report 一次生成阶段 | 拆分为 R2a/R2b/R2c/R2d | Operational Clarification | 观察是否更快定位错误，或只是增加记录负担。 |
| 人工动作日志 | 增加编号 Gate、明确请求与继续授权 | Risk Correction | 观察是否防止错项目/错时机操作。 |
| 安全边界 | 增加数据分类、凭据、权限、不可逆操作和脱敏 | Risk Correction | 观察是否真正触发有用停止或仅为预防性文本。 |
| V1 失败主因 | 增加事件类型和 Blocking/Non-blocking | Risk Correction | 观察是否改善停止/恢复判断。 |
| 五维结论、Handoff、Feedback 文件 | 新增 | Playbook-only Alignment | 只证明输出结构一致；复核价值待评价。 |
| 第一次保存/关闭/重开 | 保持核心验收 | No Change | 不归因于 Playbook utility。 |
| 最终第二次往返 | 新增、独立计时 | Playbook-only Alignment | 直接评价 R-VLD-003 的附加成本和唯一发现。 |

## 4. R-VLD-003 评价框架

最终至少回答：

1. Core roundtrip 与 Playbook-only final roundtrip 各耗费多少 Human/等待/机器时间？
2. 最终再次往返发现了哪些此前证据没有发现的问题？
3. 若无新发现，它提高了什么置信度，能否由更低成本的 manifest/diff/回读替代？
4. 对本项目和其他持久化宿主项目，建议 Keep、Change、Retire 还是 Move？

## 5. 问题分类

正式 Run 尚未开始，当前没有基于执行事实的问题分类。后续每项建议标为 `Core`、`Template`、`Adapter`、`Project-specific` 或 `Evidence gap`；分类仅是 V1 建议，Maintainer 决定是否修改 Playbook。

## 6. 反馈附件

- [HANDOFF](HANDOFF.md)
- [VALIDATION](VALIDATION.md)
- [Decision/Deviation](RECORDS.md)
- [符合性检查](PLAYBOOK_CONFORMITY.md)
- 证据及机器日志索引：待正式 Run
- 相关 Git 提交：`3ee871d`、`22da780`、`8c28f5e`、规划冻结提交待报告
