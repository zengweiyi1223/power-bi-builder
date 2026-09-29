# 项目画像与生命周期裁剪模型

- 状态：`Historical validation design; experiment complete`
- 依据：[通用开发生命周期来源审查](lifecycle-source-reconciliation.md)
- 固定 Playbook：`v0.2@dff3a717d59935697e310a29caf6b29dff11ff11`

本文定义非 Power BI 验证项目曾测试的项目画像、阶段模块、责任表达和记录策略。它是冻结的实验设计，不是 v0.2 规则，也不直接构成 v1.0；实验结果与正式处置见 [跨领域案例](../case-studies/data-quality-checker.md)和 [v1.0 审查矩阵](v1.0-disposition.md)。

## 1. 裁剪原则

1. 先选择一个最接近的基础画像，再叠加风险修饰器；不穷举行业组合。
2. 每个阶段只能标记为 `Required`、`Conditional` 或 `Not Applicable`。
3. `Conditional` 必须写明触发条件；`Not Applicable` 必须写明理由，不能静默删除。
4. 可以合并阶段和文件，但不能丢失责任、Gate、证据或恢复信息。
5. 项目风险高于画像默认值时只能增强，不能用“轻量项目”名义降低安全和验收要求。
6. v0.2 的 Evidence Gate Kernel 嵌入实施阶段，不与生命周期并列成第二套流程。

## 2. 基础项目画像

| Profile ID | 基础画像 | 典型交付 | 主要风险 |
| --- | --- | --- | --- |
| PF-EXP | 实验/研究 | 结论、原型、证据 | 假设不可证伪、结果自证、环境污染 |
| PF-DOC | 文档/内容 | 文档、教程、知识资产 | 事实错误、目标受众不匹配、版本失真 |
| PF-DAT | 数据/分析 | 数据集、分析、模型、报告 | 数据质量、隐私、口径和可复现性 |
| PF-CMP | 组件/自动化 | 库、CLI、脚本、工作流 | 接口兼容、依赖、错误处理和发布 |
| PF-APP | 交互应用/内部工具 | UI 应用、桌面或 Web 工具 | 可用性、状态、集成和用户验收 |
| PF-SVC | 生产服务 | 持续运行的服务或平台 | 可用性、安全、部署、监控和恢复 |

画像只决定默认起点。一个数据产品可以选择 `PF-DAT`，再叠加外部用户、生产运行和敏感数据修饰器。

## 3. 风险修饰器

| Modifier ID | 触发条件 | 必须增强的模块 |
| --- | --- | --- |
| MD-UI | 存在用户界面、关键交互或无障碍要求 | 用户场景、UX 设计、可用性 Review、UAT |
| MD-DATA | 存在持久化数据、迁移或不可重建输入 | 数据契约、备份、迁移验证、恢复方案 |
| MD-EXT | 依赖外部系统、账号、API 或第三方服务 | 权限、失败模式、费用、替代路线和外部回读 |
| MD-DEPLOY | 交付物进入共享、测试或生产环境 | Release、部署验证、回滚和环境记录 |
| MD-OPS | 需要长期运行、值守、监控或故障响应 | Runbook、监控、告警、升级和恢复演练 |
| MD-SEC | 涉及敏感数据、凭据、安全或合规要求 | 威胁/隐私检查、审批、脱敏和审计证据 |
| MD-MULTI | 多角色、多团队或存在正式交接 | 责任矩阵、接口约定、阶段 Review 和状态交接 |
| MD-HIGH | 错误代价高、操作不可逆或影响外部用户 | 更强独立验收、双重确认、保护性 checkpoint |

## 4. 候选生命周期

```text
STG-00 Profile & Tailor
→ STG-01 Discover & Frame
→ STG-02 Contract
→ STG-03 Design
→ STG-04 Plan & Prepare
→ STG-05 [Implement → Verify → Human Gate → Decide → Checkpoint] × N
→ STG-06 Integrated Acceptance
→ STG-07 Release / Delivery
→ STG-08 Operate / Observe
→ STG-09 Handoff / Close / Learn
```

`STG-05` 直接使用 v0.2 的 Evidence Gate Kernel。其他阶段也可以调用 Gate，但不得建立另一套相互冲突的状态或失败分类。

## 5. 默认阶段裁剪矩阵

`R` = Required，`C` = Conditional，`N/A` = 通常不适用。项目最终结果仍须根据修饰器调整。

| Stage | PF-EXP | PF-DOC | PF-DAT | PF-CMP | PF-APP | PF-SVC |
| --- | --- | --- | --- | --- | --- | --- |
| STG-00 Profile & Tailor | R | R | R | R | R | R |
| STG-01 Discover & Frame | R | C | R | C | R | R |
| STG-02 Contract | R | R | R | R | R | R |
| STG-03 Design | C | C | R | R | R | R |
| STG-04 Plan & Prepare | R | C | R | R | R | R |
| STG-05 Implement & Verify | R | R | R | R | R | R |
| STG-06 Integrated Acceptance | R | R | R | R | R | R |
| STG-07 Release / Delivery | R | R | R | R | R | R |
| STG-08 Operate / Observe | N/A | N/A | C | C | C | R |
| STG-09 Handoff / Close / Learn | R | R | R | R | R | R |

说明：

- `Release / Delivery` 对所有项目都表示受控交付；只有触发 `MD-DEPLOY` 时才要求实际部署流程。
- `Operate / Observe` 对一次性实验和文档通常不适用，但发布后的反馈观察可以作为项目自定义条件启用。
- `Discover` 或 `Plan` 标为 Conditional 不表示可以省略目标和验收；这些最低内容仍由 Contract 承载。

## 6. 统一阶段骨架

每个启用阶段只需回答以下问题，模板可按规模合并：

| 字段 | 要回答的问题 |
| --- | --- |
| Purpose | 本阶段解决什么问题？ |
| Applicability | 为什么是 Required/Conditional，或为什么 N/A？ |
| Ownership | 谁负责结果，谁执行，谁 Review，谁 Approve？ |
| Entry | 进入前必须满足什么？ |
| Inputs | 使用哪些固定输入、基线和上游决策？ |
| Actions | 本阶段执行哪些最小动作？ |
| AI Boundary | AI 可以起草、执行或建议什么；什么必须由人完成？ |
| Validation | 用什么独立依据判断结果？ |
| Record | 事实和证据保存在哪里？ |
| Exit Gate | 什么条件满足后才能进入下一阶段？ |
| Recovery | 失败后重试、回滚、新 Run 或升级确认的条件是什么？ |

## 7. 人机协作责任表达

候选责任模型分为执行者与控制方式两层：

- 执行者：`AI`、`Human`、`Shared`、`Automation`。
- AI 动作：`AI Draft`、`AI Execute`、`AI Recommend`。
- 人工控制：`Human Review`、`Human Approve`、`Human Execute`。

每个 Human Gate 必须指定一名可识别的 Approver；“用户”“业务”或“团队”只有在项目中能够映射到具体责任主体时才有效。

不要求所有活动都填写完整 RACI。小项目只需记录 Accountable Owner、Executor 和必须的 Approver；多人项目可以增加 Contributor、Reviewer 和 Consulted。

## 8. 记录策略

### 最小逻辑记录

所有正式项目至少保留：

1. `PROJECT`：画像、修饰器、角色、阶段裁剪和当前状态。
2. `REQUIREMENTS`：目标、范围、验收、安全与责任契约。
3. `VALIDATION`：阶段事实、证据、异常、Gate 和最终判定。
4. `HANDOFF`：交付入口、复核、限制、恢复和后续边界。

小项目可以把 `PROJECT` 和 `REQUIREMENTS` 合并，也可以把最终 Review 合并到 `VALIDATION`，但必须保持字段可定位。

### 条件式逻辑记录

| 触发条件 | 推荐记录 |
| --- | --- |
| 产品发现复杂 | `PROJECT_BRIEF` |
| 存在 UI/UX | `UX_SPEC` 或受控设计链接 |
| 存在架构、数据或安全取舍 | `TECH_DESIGN`、`ADR/DECISION` |
| 多阶段或多人协作 | `DELIVERY_PLAN`、当前状态记录 |
| 需要正式人工验收 | `REVIEW/UAT` |
| 需要发布或部署 | `CHANGELOG`、`RELEASE_PLAN`、部署证据 |
| 需要长期运行 | `RUNBOOK`、监控和事件记录 |
| Git 不能覆盖全部恢复对象 | `BACKUP_REGISTER` |
| 发生重大偏离 | `DECISIONS/DEVIATIONS` |
| 里程碑关闭或方法验证 | `CLOSEOUT/RETROSPECTIVE`、`PLAYBOOK_FEEDBACK` |

逻辑记录不等于独立文件。文件拆分由规模、协作人数、风险和更新频率决定。

## 9. 下一项目验证假设

| Hypothesis ID | 待验证假设 | 观察指标 |
| --- | --- | --- |
| HYP-01 | 基础画像加修饰器能覆盖真实项目，而无需穷举行业 | 是否出现无法表达的项目特征 |
| HYP-02 | `R/C/N/A + 理由` 能防止遗漏且不过度增加流程 | 被发现的遗漏、填写时间、无价值字段 |
| HYP-03 | 执行者与人工控制分层比简单“AI/人工负责”更清楚 | 越权、等待不明、重复确认次数 |
| HYP-04 | 逻辑记录与物理文件分离能减少模板负担 | 文件数量、重复内容、恢复成功率 |
| HYP-05 | 生命周期外壳与 v0.2 Evidence Gate Kernel 可以无重复结合 | 重复 Gate、冲突状态、额外维护成本 |
| HYP-06 | Release、Operate 和 Close 模块能覆盖非实验项目后半程 | 部署遗漏、回滚、监控和重开问题 |
| HYP-07 | 当前状态记录和最终 HANDOFF 应区分用途但允许合并 | 上下文恢复与最终复核是否都能完成 |

反馈必须分别记录 `Conformity` 与 `Utility`，并允许结论为 Keep、Change、Retire、Move 或 Defer。高遵守度不能单独证明候选模型有效。

## 10. 进入验证项目的最低条件

在选择项目并创建实验对话前，必须：

1. 选择基础画像和修饰器，并写明排除其他画像的理由。
2. 冻结阶段裁剪矩阵、角色与 Human Gate。
3. 声明最小逻辑记录将如何映射为实际文件。
4. 固定 Playbook v0.2 提交和本实验设计提交。
5. 定义对 HYP-01 至 HYP-07 的观察与反馈方式。
6. 保留项目采用本模型前的原始规划，避免为提高 conformity 改写实验事实。

实验项目不得修改 `playbook/**`。结果由 Maintainer 在 HANDOFF 返回后审查，届时才决定哪些内容进入 v1.0。
