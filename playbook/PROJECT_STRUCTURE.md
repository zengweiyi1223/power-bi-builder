# 项目结构与记录指南

本指南落实 `R-DOC-001` 和 `R-WRK-001`。目标是让人或 AI 第一次进入仓库时，能快速找到当前状态、权威文档、实现、验证和恢复入口；它不规定所有项目使用同一目录树。

## 1. README 与 AI 指令入口

- `README.md` 是人类优先入口，也供 AI 理解项目目的、使用方式、状态和 Artifact Map；
- `AGENTS.md` 或工具等价文件是支持该机制的 AI 自动入口，只保存反复适用的仓库指令、阅读顺序、权限边界和已验证命令；
- Contract、当前 Validation 和代码/测试仍是事实来源，`AGENTS.md` 不复制整份 Playbook、需求或滚动状态。

一次性低风险任务可以只用清楚的 README。仓库需要 AI 跨会话持续执行、存在特殊命令/权限/禁区或容易误判的项目状态时，应提供简短的 AI 指令入口，并固定实际使用的 Playbook/Contract 基线。可从 [AGENTS 模板](templates/AGENTS.template.md)裁剪。

## 2. 根入口必须回答什么

根目录的 `README.md` 或等价入口至少说明：

- 项目解决什么问题，当前处于什么状态；
- 主要使用、构建或阅读入口；
- 当前 Playbook、Contract、release 或实验基线；
- Artifact Map：逻辑记录分别保存在哪里；
- 当前滚动状态指向哪个 `VALIDATION`；
- 当前阶段、允许操作、Blocker、下一 Gate 和 checkpoint 在 `VALIDATION` 的哪个控制区；
- 最终交付或上一次稳定状态指向哪个 `HANDOFF`；
- AI 指令入口是否存在、适用于哪些目录；
- 哪些目录是源码、测试、正式证据、运行副本和可重建临时产物。

README 提供导航，不复制所有需求、状态和证据。

## 3. 六类信息分区

| 信息区 | 内容 | 管理原则 |
| --- | --- | --- |
| 入口与治理 | README、PROJECT、REQUIREMENTS、Decision/Deviation | 稳定、可定位、变更有版本点 |
| 产品与实现 | 文档正文、源码、配置、数据模型、设计资产 | 与生成物和运行副本分开 |
| 测试与 Oracle | tests、fixtures、expected results、量表 | 不由被测实现自行生成关键预期 |
| 验证与证据 | VALIDATION、日志摘要、截图索引、hash、外部回读 | 滚动状态只有一个权威来源；必要时脱敏 |
| 发布与运行 | RELEASE、RUNBOOK、部署/迁移/恢复记录 | 只有触发相应阶段时启用 |
| 临时与可重建内容 | cache、dist、临时日志、工具工作目录 | 不作为唯一证据；明确忽略或清理策略 |

目录名可以变化，但六类信息不能混得无法判断生命周期。大型二进制、外部系统记录或不能进入 Git 的证据，应在 Artifact Map 中记录位置、身份、访问边界和完整性方法。

### 3.1 文档职责

| 类型 | 回答的问题 | 更新原则 |
| --- | --- | --- |
| Normative / 规范 | 以后应该怎样做？ | 低频修订，经适当 Review/Approve 后生效 |
| Baseline / 基线 | 当前已经批准什么？ | 冻结后通过 Decision 和新版本点变更 |
| Record / 记录 | 实际发生了什么？ | 及时追加，纠错保留原结论和更正原因 |

同一信息只设一个主要权威来源，其他文档用链接或稳定编号引用。分类可以写在 Artifact Map 或文档头，不要求增加文件数量。

## 4. 逻辑记录与物理文件

### 最小逻辑记录

| 逻辑记录 | 权威内容 | 更新方式 |
| --- | --- | --- |
| PROJECT | 画像、风险修饰器、角色、阶段裁剪、Artifact Map | 项目边界变化时更新 |
| REQUIREMENTS | Why、目标、范围、验收、安全和 Human Gate | 冻结；变化通过 Decision 和新版本点 |
| VALIDATION | 当前阶段状态、证据、异常、Gate 和 checkpoint | 执行过程中滚动更新 |
| HANDOFF | 最终入口、结论、限制、恢复与后续边界 | 里程碑或项目结束时形成 |

### 条件式逻辑记录

| 触发条件 | 推荐记录 |
| --- | --- |
| 重要技术、UX、数据、安全或依赖取舍 | TECH_DESIGN、UX_SPEC、ADR/Decision |
| 多阶段、多依赖或多人协作 | DELIVERY_PLAN |
| 正式用户验收 | UAT / REVIEW |
| 外部发布、部署或迁移 | RELEASE_PLAN、deployment evidence |
| 长期运行、监控或故障恢复 | RUNBOOK、incident records |
| Git 不能覆盖全部恢复对象 | BACKUP_REGISTER |
| Playbook 验证项目 | PLAYBOOK_FEEDBACK |

逻辑记录可以合并。例如小项目可以把 PROJECT 与 REQUIREMENTS 合并，把 DELIVERY_PLAN 放进 TECH_DESIGN；合并后仍须在 Artifact Map 中指出对应章节。不要让同一动态状态同时在 PROJECT、VALIDATION 和 HANDOFF 三处维护。

## 5. 推荐结构示例

### 5.1 小型组件、文档或单次实验

```text
project/
├─ README.md
├─ AGENTS.md                  # 条件式；AI 自动入口，不复制项目事实
├─ PROJECT.md                 # 可与 REQUIREMENTS 合并
├─ REQUIREMENTS.md
├─ VALIDATION.md              # 唯一滚动状态
├─ HANDOFF.md
├─ src/ or content/
├─ tests/ or review/
├─ fixtures/                  # 需要时
├─ evidence/                  # 正式、可定位的证据
└─ .work/ or dist/            # 可重建，不作为唯一证据
```

### 5.2 应用、组件或生产服务

```text
project/
├─ README.md
├─ AGENTS.md                  # 条件式
├─ docs/
│  ├─ PROJECT.md
│  ├─ REQUIREMENTS.md
│  ├─ TECH_DESIGN.md
│  ├─ DELIVERY_PLAN.md        # 可并入 TECH_DESIGN
│  ├─ VALIDATION.md
│  ├─ RELEASE_PLAN.md         # 条件式
│  ├─ RUNBOOK.md              # 条件式
│  ├─ RECORDS.md
│  └─ HANDOFF.md
├─ src/
├─ tests/
├─ fixtures/
├─ evidence/
└─ build/ or dist/            # 可重建
```

### 5.3 多实验或多方案集合

```text
project/
├─ README.md                  # 总入口与实验索引
├─ AGENTS.md                  # 条件式；固定范围和恢复顺序
├─ shared-inputs/             # 只读或来源固定
├─ experiments/
│  └─ <experiment-id>/
│     ├─ PROJECT.md
│     ├─ REQUIREMENTS.md
│     ├─ runs/
│     │  └─ <run-id>/
│     │     ├─ work/ or project/
│     │     ├─ evidence/
│     │     └─ VALIDATION.md
│     └─ HANDOFF.md
└─ HANDOFF.md                 # 集合级结论，不复制各实验明细
```

V0 式单一正式 Run 与 V1 式多实验归档不应被强迫成相同结构；两者都必须有明确总入口、固定输入、实验/运行身份和证据地图。

## 6. 可读性检查

项目进入正式实施、交付或恢复前，确认：

- 新参与者从根入口可以在几分钟内找到需求、当前状态、实现、证据和恢复点；
- 同一个状态、验收口径或限制只有一个权威来源；
- README 面向人解释项目，AI 指令入口只保存短小、稳定、可执行的仓库约束；
- 文件名或目录不能说明用途时，Artifact Map 已补充解释；
- 运行副本、生成物和缓存不会被误认为可信基线或正式交付物；
- 不适用的目录不会为了“看起来完整”而预建为空目录；
- 路径、账号、本机缓存和工具临时状态没有被误写成跨项目规范。
- 候选交付已完成单文件检查和受影响范围的跨文件一致性检查。
