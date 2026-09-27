# Power BI Builder — V1 Zero Seed 需求与验收契约

- 状态：**已冻结；正式 Run 尚未开始**
- Playbook：`v0.1`，提交 `3ee871d618db84d55b3b2f86a198ac552864317e`
- 需求基线：包含本文的“v0.1 符合性检查及 V1 规划冻结”提交；SHA 由 Git 和执行报告记录
- 采用前草案：`22da780412f27decf17a097548d65d151c75b235`

## 1. 核心问题

要证明或否定：从经证明为空的目录开始，仅由 Codex 生成 PBIP 入口、PBIR 报表和 TMDL 语义模型工程结构后，Power BI Desktop 是否能够直接打开、显式保存、关闭并从同一磁盘项目稳定重开，而无需人工先创建空白 PBIP 种子。

本轮不证明：V0 完整业务模型、DAX 数值、六个视觉对象、Power BI Service、跨机器迁移、多页面、复杂视觉对象或产品化能力。

预期的负面结果构成完整实验：只要 Contract、证据和重复性要求均满足，“Desktop 首次补写”或“仍需人工种子”都是有效功能结论，不等于执行失败。

## 2. 输入、输出与范围

| 项目 | 冻结内容 |
| --- | --- |
| 输入及来源 | 本 Contract、固定 Playbook/adapter、运行时锁定的微软公开格式文档与 Schema；不需要业务数据。 |
| Trusted baseline | 每个 Run 中经递归清单证明为空的全新 `project/`，记录创建时间、路径、文件数和子目录数。 |
| 最小生成物 | 根 `*.pbip`、自洽的 `*.Report/` 与 `*.SemanticModel/`、相对 `byPath`、PBIR 根定义与唯一 `Overview` 页面、`definition.pbism` 和最小可解析 TMDL。 |
| 交付物 | 两个或更多正式 Run、项目文件、日志、证据、每 Run `VALIDATION.md`、总 `VALIDATION.md`、`RECORDS.md`、`HANDOFF.md`、`PLAYBOOK_FEEDBACK.md`。 |
| 允许修改 | 规划冻结前仅 `V1-zero-seed/**`；正式 Run 中仅对应 `V1-zero-seed/runs/<run-id>/**` 和 V1 汇总文档。 |
| 禁止修改 | `V0/**`、`playbook/**`、其他 Run 已冻结现场、仓库外文件。 |
| 主执行路线 | 空目录证明 → 分原子步骤生成/立即验证 → 预打开 checkpoint → 人工首开 → 首开 diff → 人工首存/关闭 → 首存 diff → 人工重开/只读回读 → 最终往返检查 → 跨 Run 分级。 |
| 禁止或需批准的替代路线 | 不得复制/改名既有项目、人工建壳、手工补造 Desktop 文件、静默换用离线模型路线或把失败现场覆盖为成功；路线改变需 Decision、Human Gate 和新 Run。 |

两个主试验保持不变：

| 试验 | 项目名 | 路径特征 | 独立性 |
| --- | --- | --- | --- |
| A | `ZeroSeedAlpha` | 仓库内短路径、ASCII、无空格 | 从空目录独立生成。 |
| B | `零种子 Beta` | 不同父目录、空格和 Unicode | 重新生成全部文件与标识符，不复制 A。 |

若 B 证明目标版本不支持该路径类别，记录为 PATH 限制，并增加另一组受支持但名称/路径不同的独立 Run；不得静默降低重复性要求。

## 3. 责任与 Human Gate

### 责任边界

- **AI / Experiment Owner**：创建 Run 结构、记录来源、生成项目、执行静态检查和清单/diff、维护 Validation/Records、请求 Gate、保存 checkpoint、归因并报告。
- **Human Approver**：明确授权正式 Run；在收到精确路径和预期后操作 Desktop；报告实际界面、提示与确认；完成主观可见性判断。
- **Shared**：确认目标项目身份、异常严重度和是否允许继续；Human 的观察不替代机器证据，AI 检查不替代 Human Gate。
- **Playbook Maintainer**：不属于本实验执行角色；仅在实验之后评审反馈。Experiment Owner 不修改 `playbook/**`。

### Human Gate

| ID | 责任人 | 动作/判断 | 继续条件 | 必需证据 |
| --- | --- | --- | --- | --- |
| HG-00 | Human | 确认规划冻结提交并授权正式 Run | 明确给出开始授权 | 请求、冻结 SHA、人工回复、时间 |
| HG-01 | Human | 首次打开 AI 指定的目标 `.pbip`，不保存、不另存为、不创建项目 | 确认实际路径/项目名及全部提示；项目可进入才继续 | 请求、绝对目标、预期、实际确认、截图或文字观察、继续授权 |
| HG-02 | Human | 在首开磁盘差异完成后显式保存并关闭 | Gate 判定允许；确认保存/关闭结果与二次提示 | 同上，另加进程退出检查 |
| HG-03 | Human | 从同一 `.pbip` 第一次重开 | 首存静态/语义 diff 已通过或带已接受限制 | 项目身份、提示、页面/模型观察、继续授权 |
| HG-04 | Human | 执行 R-VLD-003 的最终再次关闭/重开检查 | 第一次往返与只读回读已完成；明确授权额外往返 | 请求与理由、耗时、实际提示、继续授权 |
| HG-05 | Human | 完成最终可见状态确认 | 所有 Blocking 事件已关闭；项目无未解释修复提示 | 签字式确认、时间、目标身份 |

AI 不得依据沉默、历史操作或“看起来已经打开”自行越过 Gate。每项 Gate 都记录请求、目标、预期、实际确认与继续授权。

## 4. 安全与权限

- 数据分类：仓库与正式运行证据按**内部**处理；公开微软规范为公开数据；本实验不需要业务数据、PII、密钥或凭据。
- 密钥、凭据、账号：不得读取、记录或请求。出现登录、凭据或组织账号提示时停止并记录 `Safety/Permission Blocker`。
- 本机信息：内部 Validation 可记录验证项目身份所必需的绝对路径、版本和本地端口；对外材料必须移除用户目录、端口、账号和无关进程信息。
- 外部访问：仅允许只读访问冻结时记录的微软公开文档/Schema；不发布到 Power BI Service，不上传项目，不扩大权限。
- 破坏性操作：不得强制重置、删除 V0/Playbook/其他 Run、覆盖失败现场或改写历史。删除/替换正式 Run、对外发布、发送和权限变更需新的明确授权。
- 证据脱敏：截图、日志和命令输出在纳入 Git 前检查账号、令牌、凭据、无关窗口和个人路径；原始证据若必须保留敏感信息则不得提交，改存经授权位置并记录哈希。
- Power BI 本机缓存和自动恢复文件是临时状态，不作为正式证据或交付物。

## 5. 阶段与验收

| 阶段 | 入口条件 | 原子产物 | 验收标准与验证方式 | Human Gate | Blocking 条件 |
| --- | --- | --- | --- | --- | --- |
| F0 规划冻结 | Playbook 已 no-ff 接入 | Contract、符合性、模板、反馈骨架、Git checkpoint | Required/Provisional/Guidance 映射完成；`playbook/**` 无 V1 修改；Git diff/check 通过 | 无 | 基线错误、工作树污染、Playbook 被修改 |
| R0 Run/Preflight | HG-00 通过 | 唯一 Run、环境/版本/权限/目标/回滚记录 | Git 干净；Desktop/MCP 版本重新核实；目标进程和权限明确 | HG-00 | 必要环境、能力、权限或回滚点缺失 |
| R1 空目录 | R0 Passed | 空 `project/` 证据 | 文件数=0、子目录数=0；证据在目录外 | 无 | 目录非空或来源不明 |
| R2a PBIP 入口 | R1 Passed | 根 `.pbip` | 立即做 JSON/Schema/目标 Report 路径检查并记录 Gate | 无 | 语法、Schema 或引用失败 |
| R2b SemanticModel | R2a Passed | `*.SemanticModel/`、PBISM、最小 TMDL | 立即做语法/结构/编码/标识符检查 | 无 | 无法独立解析或存在外部工程引用 |
| R2c Report/PBIR | R2b Passed | `*.Report/`、PBIR、唯一页面 | 立即做 JSON/Schema、页面索引、`byPath` 和目录边界检查 | 无 | 任一检查失败 |
| R2d 预打开冻结 | R2c Passed | 完整 manifest、预打开 Validation、Git checkpoint | 全量不变量、SHA-256、来源和 Desktop 未运行检查通过 | 无 | 证据缺口、污染、未解释文件 |
| R3 首开 | R2d Passed | Human 首开观察、首开 manifest/diff | 直接打开指定项目；无阻塞错误；所有补写分类 | HG-01 | 阻塞打开、目标错误、未授权保存 |
| R4 首存 | R3 Gate Passed | 保存/关闭观察、首存 manifest/diff、checkpoint | 结构/语义/字节差异分类；磁盘仍可解析 | HG-02 | 未解释结构/语义变化、进程未退出 |
| R5 第一次重开 | R4 Passed | 重开观察、可用时的 MCP 只读回读 | 同一路径可重开；页面/模型可识别；MCP 故障单独归因 | HG-03 | Desktop 不稳定或关键身份无法确认 |
| R6 最终往返 | R5 Passed | 第二次关闭/重开、最终 manifest、R-VLD-003 成本价值数据 | 状态稳定；比较第二次往返的新信息与成本 | HG-04、HG-05 | 新 Blocking 事件或最终状态不明 |
| R7 跨 Run 判定 | 至少两组有效 Run | 总 Validation、Handoff、Feedback | A/B 规则一致、异常已归因、五维最终判定完成 | 无 | 结果冲突未归因、证据不完整 |

每个原子阶段均执行“变更 → 自动验证 → 必要人工验证 → Gate 判定 → checkpoint/证据引用”，不得全部生成或全部操作后统一验证。

关键结论的独立依据组合：微软公开 Schema 和格式不变量、与生成动作分离的清单/引用检查、Git 原始 diff、Desktop 真实打开/保存/重开、MCP 只读回读和预先冻结的人工观察。不存在单一完整 Oracle 时，必须分别说明精确证明、辅助证明和人工观察，不能声称证据完整。

## 6. 停止、恢复与事件分类

每个事件同时记录：

1. Playbook 类型：`Validation Failure`、`Environment Failure`、`Safety/Permission Blocker`、`Governance Failure`、`Evidence Gap`、`Expected Negative Result` 或 `Warning`；
2. 严重度：`Blocking`、`Non-blocking` 或 `Informational`；
3. V1 主因：`GEN`、`SPEC`、`DESKTOP`、`PATH`、`MCP`、`ENV`、`HUMAN` 或 `PROVENANCE`。

`Blocking` 立即停止依赖步骤。只有 Contract 已允许、状态仍可信且不覆盖失败证据时，才可在原 Run 原子步骤内重试；能回到明确 checkpoint 时可回滚并重新验证；状态不可信、路线改变、来源污染、人工建壳、跨 Run 复制或需要复杂替代方案时必须新建 Run。

功能结果分级：`完全零种子`、`Desktop 首次补写`、`仍需人工种子`、`无法判定`。最终报告另行给出 Contract 符合度、证据完整度、持久化状态和已知边界。

## 7. 三级结论标准

### 完全零种子

两组有效独立 Run 均满足：空目录与来源证据完整；Codex 首开前生成全部最小工程；Desktop 无阻塞错误、修复警告或人工建壳动作地直接打开；首开/首存无 `STRUCTURAL_REQUIRED` 或无法解释的 `SEMANTIC_CHANGE`；保存、关闭、两次重开和项目身份检查均通过。

### Desktop 首次补写

两组有效 Run 均无需人工创建或另存为项目壳且最终稳定，但至少一组依赖 Desktop 的结构性补写、非阻塞修复或初始化。必须列出补写的精确文件、语义和必要性。

### 仍需人工种子

排除 `ENV`、`HUMAN`、`MCP` 和单纯 `PATH` 后，至少两次独立、合规尝试仍无法直接打开或稳定重开，继续成功必须依赖人工创建/保存的工程壳。单个生成拼写错误或单次环境故障不足以下此结论。

### 无法判定

来源污染、环境不稳定、两组结果冲突未归因、公开规范缺口或关键证据缺失。

## 8. 文件、证据与 Git

```text
V1-zero-seed/
├─ REQUIREMENTS.md / EXPERIMENT_PLAN.md / RECORDS.md
├─ VALIDATION.md / HANDOFF.md / PLAYBOOK_FEEDBACK.md
├─ VALIDATION.template.md / RUN_RECORD_TEMPLATE.md
├─ .work/                              # 可重建临时文件，不提交
└─ runs/<run-id>/
   ├─ RUN.md / VALIDATION.md
   ├─ project/
   ├─ logs/
   └─ evidence/
```

正式证据包括 Contract、Run/Validation、Decision/Deviation、项目源文件、清单、差异、必要截图/日志和 Git checkpoint。缓存、依赖下载、Schema 临时副本进入 `.work/`；若公开 Schema 本身用于精确证明，记录 URL、获取时间、哈希和存储决定。

checkpoint 至少包括：规划冻结、每 Run 预打开、首存验证、Run 最终状态和跨 Run 最终验收。单文件不得超过 10 MB，单 Run 建议不超过 50 MB；超限先记录文件、用途、大小和 SHA-256，再决定存储方式，不静默删证据。

## 9. Playbook 规则处理

| Rule | 等级 | 处理方式 |
| --- | --- | --- |
| 全部 Required Rules | Required | 应用；具体映射见 `PLAYBOOK_CONFORMITY.md`。 |
| R-VLD-003 | Provisional | 应用并区分实验核心的首次往返与 Playbook-only 的最终再次往返；记录宿主启动次数、人工主动时间、等待时间、证据量、仅由往返发现的问题及若省略的风险。 |
| R-GIT-002 | Guidance | 采用阶段级 checkpoint，不为每个小文件动作提交。 |

## 10. 冻结与变更

冻结后影响范围、路线、验收、安全、Human Gate 或成功口径的变化必须记录 `DCS-nnn` 并形成独立提交。实际偏离使用 `DEV-nnn`，不得静默修改 Contract 以适配结果。

正式 Run 前需 HG-00 明确授权。实验期间不修改 Playbook；规则问题仅进入偏差或反馈。
