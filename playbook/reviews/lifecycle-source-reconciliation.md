# 通用开发生命周期来源审查

- 状态：`Historical design input; cross-domain validation complete`
- 工作分支：`codex/lifecycle-validation-design`

本文是 Playbook v1.0 的历史研究输入，不是 v0.2 的增补规范。它整理 Playbook v0.2、历史 AI-System 和常见开发生命周期之间的重合、缺口与候选抽象。跨领域实验已经完成，正式处置见 [v1.0 审查矩阵](v1.0-disposition.md)；本文件保留设计时口径，不作为当前规则。

## 1. 固定基线

| 来源 | 固定版本 | 本次用途 |
| --- | --- | --- |
| Playbook v0.2 | `dff3a717d59935697e310a29caf6b29dff11ff11` | 已验证的证据闸门内核 |
| Power BI Builder V0/V1 | `78a20f0`、`442b2c3` 及 v0.2 review 引用提交 | 已发生实验的事实与边界 |
| 历史 AI-System | `main@5dc740a` | 生命周期、文档治理、Git、恢复和关闭候选来源 |
| 常见开发生命周期 | 产品、设计、开发、QA、发布、运维的职责模型 | 检查角色和阶段缺口，不作为未经证据的规范来源 |

本审查不得修改 v0.2 的规则、等级或模板，也不得把历史文档中的 `active` 状态解释为已经完成跨项目验证。

## 2. 目标结构

```text
通用开发生命周期
├─ 人机协作责任模型
├─ 可裁剪阶段模块
├─ 每阶段记录模板
└─ 证据闸门内核
```

为避免把所有内容塞进一个主文档，候选内容按以下层级归类：

| 层级 | 职责 |
| --- | --- |
| Lifecycle Core | 稳定的阶段顺序、裁剪原则和进入/退出条件 |
| Responsibility Model | 人、AI、共同责任、Review 和 Approve 边界 |
| Stage Module | 只在相应项目画像下启用的产品、UX、架构、发布、运维等阶段 |
| Evidence Gate Kernel | v0.2 的 Contract、Execute–Verify、Evidence、Gate、停止、回滚与 Handoff |
| Record Template | 保存阶段决策和证据的逻辑记录；不强制每项一个文件 |
| Specialized Standard | Git、备份、文档恢复、信息安全等跨项目专项规则 |
| Domain Adapter | Power BI、特定框架或宿主生命周期的领域映射 |
| Project-specific | 单项目命令、路径、偏好、版本行为和一次性例外 |

## 3. 候选内容准入检查

候选内容进入 v1.0 前必须回答：

1. 是否在两个以上不同领域具有相同问题，而非仅更换了术语？
2. 是否能定义清楚的输入、输出、负责人和退出 Gate？
3. 是否减少遗漏、返工、风险或恢复成本，并有实际证据？
4. 是否已经由现有 Core、专项标准或项目惯例覆盖？
5. 对小项目的记录负担是否与风险相称？
6. 能否用 `Required / Conditional / Not Applicable` 裁剪？
7. 人与 AI 的权限边界是否明确且可执行？

证据状态统一使用：

- `V0/V1 observed`：在 Power BI 实验中真实发生过；仍不自动代表跨领域有效。
- `Historical practice`：历史 AI-System 已定义，但尚缺本轮跨领域实测。
- `Cross-domain candidate`：根据生命周期缺口提出，必须在下一项目验证。
- `Domain-only`：保留在 adapter 或项目文档，不进入 Core。

## 4. 生命周期候选矩阵

| ID | 候选阶段/能力 | 主要来源 | v0.2 覆盖 | 建议归属 | 适用项目 | 当前证据 | 下一项目验证重点 | 逻辑记录 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LFC-01 | 项目画像与流程裁剪 | AWSS、Workflow、当前讨论 | 无显式画像 | Lifecycle Core | 全部正式项目 | Cross-domain candidate | 能否在启动时决定阶段而不遗漏风险 | `PROJECT_PROFILE` |
| LFC-02 | 产品发现与问题定义 | Workflow Phase 0–1 | `Frame` 只覆盖可证伪问题 | Stage Module | 产品、服务、内部工具 | Historical practice | 用户、价值和场景记录是否改善需求质量 | `PROJECT_BRIEF` 或并入 `PROJECT` |
| LFC-03 | 需求、范围与验收契约 | 两套体系 | 强覆盖 | Evidence Gate Kernel | 全部正式项目 | V0/V1 observed | 普通开发中是否需要放宽实验式措辞 | `REQUIREMENTS` |
| LFC-04 | UI/UX 与交互设计 | 常见生命周期 | 未覆盖 | Stage Module | 有界面或复杂交互的项目 | Cross-domain candidate | 设计稿、状态和可用性验收如何成为实现输入 | `UX_SPEC` 或设计链接 |
| LFC-05 | 技术、数据与安全设计 | Workflow、Decision 模板、常见生命周期 | 部分覆盖路线和安全边界 | Stage Module | 存在架构、数据或安全取舍时 | Historical practice | 何种复杂度才需要独立设计记录 | `TECH_DESIGN`、`ADR/DECISION` |
| LFC-06 | 实施与交付计划 | Workflow、HANDOFF | 仅有 Contract 阶段表 | Stage Module | 多阶段、多人或高依赖项目 | Historical practice | 计划是否帮助拆出可验证增量而不重复需求 | `DELIVERY_PLAN` 或并入 Contract |
| LFC-07 | 工作区、输入与环境准备 | AWSS、v0.2 | 强覆盖 baseline、Run 和 Preflight | Core + Specialized Standard | 全部正式项目 | V0/V1 observed | 非实验项目是否需要 `Run` 概念 | 项目结构、Preflight 记录 |
| LFC-08 | 分阶段实现与验证 | v0.2 | 强覆盖 | Evidence Gate Kernel | 全部实施型项目 | V0/V1 observed | 在代码、UI 和部署变更中保持原子粒度的成本 | `VALIDATION` |
| LFC-09 | 集成验收与 UAT | Workflow Review、Review 模板 | Human Gate 和最终判定部分覆盖 | Stage Module | 有最终用户或跨组件行为时 | Historical practice | 自动验证、人工 UAT 和业务批准如何分层 | `REVIEW/UAT` |
| LFC-10 | 发布、部署与迁移 | Runbook、Git Standard | 仅覆盖权限、证据和 checkpoint | Stage Module | 有可发布环境的项目 | Historical practice | 发布前后 Gate、数据迁移和回滚是否充分 | `RELEASE_PLAN`、部署记录 |
| LFC-11 | 运行、监控与维护 | Runbook | 未覆盖 | Stage Module | 长期运行的软件或服务 | Historical practice | 最小监控、故障升级和恢复要求 | `RUNBOOK`、运行记录 |
| LFC-12 | 正式交付与上下文恢复 | ADRG、两套 HANDOFF | 强覆盖最终 Handoff；持续恢复部分不足 | Core + Record Template | 全部长期项目 | V0/V1 observed + Historical practice | 区分当前状态记录与最终交接 | `STATUS/HANDOFF` |
| LFC-13 | 项目关闭、归档与复盘 | ADRG、Closeout、Retrospective | 仅有 Playbook Feedback | Stage Module | 里程碑或长期项目 | Historical practice | 关闭检查是否降低遗留和重开成本 | `CLOSEOUT`、`RETROSPECTIVE` |

## 5. 横切能力候选矩阵

| ID | 候选能力 | 主要来源 | 建议归属 | 当前证据 | 下一项目验证重点 | 逻辑记录 |
| --- | --- | --- | --- | --- | --- | --- |
| XFN-01 | 人机协作责任模型 | 两套体系 | Responsibility Model | V0/V1 observed + Historical practice | `AI Draft / AI Execute / Human Review / Human Approve` 是否足够表达真实责任 | 阶段责任矩阵 |
| XFN-02 | 阶段记录触发与唯一权威来源 | ADRG、v0.2 templates | Record Template + Specialized Standard | Historical practice | 减少重复文档，同时保证事实有归属 | Artifact map |
| XFN-03 | Git 检查、checkpoint 与恢复 | Git Standard、v0.2 | Specialized Standard + Gate 接口 | V0/V1 observed + Historical practice | 阶段 checkpoint 与日常提交怎样避免重复或过密 | Git/Validation 记录 |
| XFN-04 | 安全、隐私、权限和外部发布 | 两套体系 | Core boundary + Specialized Standard | V0/V1 observed | 小项目如何轻量记录，高风险项目如何增强 | Contract、安全记录 |
| XFN-05 | 备份、数据恢复和灾难恢复 | ADRG、Backup Register | Conditional Specialized Standard | Historical practice | Git 之外的数据是否需要独立恢复演练 | `BACKUP_REGISTER` |
| XFN-06 | Decision、Deviation、Blocker 与归因 | v0.2、Decision 模板 | Evidence Gate Kernel + Record Template | V0/V1 observed | 普通开发中记录阈值是否清楚 | `DECISIONS/DEVIATIONS` |
| XFN-07 | 文档格式与 Obsidian 兼容 | ONS | Optional writing standard | Historical practice | 不作为生命周期验证目标 | 项目自行选择 |

## 6. 已识别的重合与冲突

1. **双重顶层流程**：历史六阶段与 v0.2 八个英文阶段不能并行成为两套权威流程；v1.0 应只有一条生命周期，证据闸门作为阶段内循环。
2. **实验术语泛化**：`Run`、可证伪问题和 Expected Negative Result 适合实验，但普通开发可能只需要 Release、Iteration 或 Change Set；下一项目应验证术语边界。
3. **当前状态与最终交付混用**：历史 `HANDOFF-current` 面向恢复，v0.2 HANDOFF 面向最终复核；未来应区分用途，但允许小项目合并。
4. **文档数量风险**：历史模板职责完整，但全部独立建档会增加负担；逻辑记录必须存在，物理文件按项目规模合并。
5. **Git 规则重复**：主流程只定义何时需要 checkpoint，具体 Git 安全操作由专项标准负责。
6. **路径和工具绑定**：绝对路径、Obsidian 语法、个人目录和具体工具不进入跨环境 Core。
7. **领域观察泛化**：Power BI Desktop、PBIR、TMDL、MCP 和宿主保存行为继续留在 Power BI adapter。

## 7. 第 2 步输入

第 2 步应基于本矩阵形成：

1. 一组稳定的项目画像，而不是穷举所有行业。
2. 每个阶段的 `Required / Conditional / Not Applicable` 选择规则。
3. 统一的阶段骨架：目的、角色、入口、输入、AI 权限、动作、验证、记录和退出 Gate。
4. 最小文档集与条件式文档集。
5. 非 Power BI 项目需要验证的明确假设和反馈字段。

这些产物仍属于实验设计，不构成 v1.0，也不得改变已冻结的 v0.2 基线。
