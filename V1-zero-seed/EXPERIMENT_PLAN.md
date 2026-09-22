# V1 Zero Seed — 实验路线

本路线受 `REQUIREMENTS.md` 冻结。Playbook 基线为 `3ee871d618db84d55b3b2f86a198ac552864317e`；路线变化必须先记录 Decision，不得在运行中静默调整。

## 1. 设计原则

实验只测试工程壳来源，不把业务数据、完整建模或复杂报表混成首开前置条件。每个 Run 比较五个磁盘状态：

```text
空目录
  → Codex 原子生成态
  → Desktop 首开态（未保存）
  → Desktop 首存态
  → 第一次稳定重开态
  → 最终再次重开态（R-VLD-003 评价）
```

每个箭头均留下清单、SHA-256、结构/语义差异和 Gate。Desktop 能打开不等于完全零种子；必须确定首开是否补齐了必需工程结构。

## 2. Run 单元与目录

每个正式 Run 只容纳一个项目名、一个路径条件和一个 attempt：

```text
V1-zero-seed/runs/<run-id>/
├─ RUN.md
├─ VALIDATION.md
├─ project/                    # 先证明为空；不放占位文件
├─ logs/
│  ├─ HUMAN_ACTIONS.md
│  ├─ MCP_ACTIONS.jsonl
│  ├─ CODEX_FILE_ACTIONS.jsonl
│  ├─ EVENTS.jsonl
│  └─ R-VLD-003-METRICS.json
└─ evidence/
   ├─ manifests/
   │  ├─ PREOPEN_MANIFEST.json
   │  ├─ FIRST_OPEN_MANIFEST.json
   │  ├─ FIRST_SAVE_MANIFEST.json
   │  ├─ FIRST_REOPEN_MANIFEST.json
   │  └─ FINAL_REOPEN_MANIFEST.json
   └─ checks/
      ├─ PREOPEN_VALIDATION.md
      ├─ DIFF_FIRST_OPEN.md
      ├─ DIFF_FIRST_SAVE.md
      └─ REOPEN_VALIDATION.md
```

失败后不复用 `project/`。仅当 Contract 已允许、状态可信且失败证据不会被覆盖时，才在同一 Run 的同一原子步骤重试；其他情况回滚或新建 `<run-id>-attempt-N`。

## 3. 重复矩阵

### A — ASCII 基线

- 项目名：`ZeroSeedAlpha`
- 预定位置：`V1-zero-seed/runs/<timestamp>-a/project/ZeroSeedAlpha/`
- 特征：短路径、ASCII、无空格。

### B — 名称与路径变化

- 项目名：`零种子 Beta`
- 预定位置：`V1-zero-seed/runs/<timestamp>-b/project path/零种子 Beta/`
- 特征：不同父目录、空格、Unicode。

B 必须重新生成标识符和全部工程文件，不得复制或改名 A。若生成规则在 A 后发生实质变化，A 与 B 都要在新 attempt 中使用同一冻结规则重跑。

## 4. Execute–Verify 原子循环

| 原子阶段 | Execute | 立即 Verify | Gate / checkpoint |
| --- | --- | --- | --- |
| R0 | 创建 Run 记录，执行环境与权限预检 | 核实分支、版本、工具、目标身份、进程和回滚条件 | Blocking 为 0；记录 Run 起点 |
| R1 | 创建目标 `project/` | 立即递归证明文件数和子目录数均为 0 | 空目录作为 Trusted baseline |
| R2a | 只生成根 `.pbip` | JSON/Schema、Report 目标和名称检查 | 通过才生成模型 |
| R2b | 只生成 SemanticModel 最小结构 | PBISM/TMDL 语法、编码、标识符和目录边界 | 通过才生成 Report |
| R2c | 只生成 Report/PBIR/唯一页面 | JSON/Schema、页面索引、`byPath`、引用边界 | 通过才做全量冻结 |
| R2d | 生成全量 manifest 和来源记录 | 独立不变量检查、SHA-256、污染扫描、Desktop 未运行 | 预打开 Git checkpoint |
| R3 | 请求 HG-01 并由 Human 首开，禁止保存 | 记录目标、提示、首开 manifest；分类缓存/补写/修复 | Gate 判定后才可保存 |
| R4 | 请求 HG-02 并由 Human 首存/关闭 | 进程退出、首存 manifest、原始/结构/语义 diff、离线复验 | 首存 Git checkpoint |
| R5 | 请求 HG-03 并由 Human 第一次重开 | Desktop 观察；可用时 MCP 只读回读；首次往返判定 | Run 核心功能候选结论 |
| R6 | 请求 HG-04/HG-05，执行最终再次关闭/重开 | 最终 manifest、稳定性、R-VLD-003 新发现与成本 | Run 最终 checkpoint |
| R7 | 两组有效 Run 完成后汇总 | 交叉比较规则、结果、证据、限制和 Playbook utility | 最终验收 checkpoint |

原子验证失败立即记录事件类型、严重度和 V1 主因；`Blocking` 不得越过当前 Gate。

## 5. Human Gate 请求格式

每次请求必须给出：

1. Gate ID 与目的；
2. 目标 `.pbip` 的精确绝对路径、项目名和 Run ID；
3. 允许执行的唯一动作与明确禁止动作；
4. 预期看到的状态和需要报告的全部提示；
5. 当前自动验证与 checkpoint；
6. 用户回复中必须包含的实际确认和是否授权继续。

Human 未明确回复时保持 `Blocked` 或等待状态，不推断授权。

## 6. 离线检查与独立依据

- 按文件声明的公开 Schema 验证 JSON；Schema 不可得时标记 `Evidence Gap`，不以旧版代替精确证明。
- 根 `.pbip` 指向本 Run 的 Report，`definition.pbir` 的 `byPath` 解析后仍在本 Run 内并指向目标 SemanticModel。
- PBISM/TMDL 根文件存在，语法、编码和换行被记录。
- PBIR 只有一个 `Overview` 页面，页面索引与目录一致。
- 项目级标识符在本 Run 中唯一，A/B 不共用固定标识符。
- 清单和文本中不得出现 V0 种子名、V0 工程路径或外部绝对工程引用。
- manifest 生成与不变量验证使用分离的命令/逻辑；再由 Git diff、Desktop 真实运行和 MCP 只读回读组合佐证。

## 7. Desktop 差异分类

- `CACHE_LOCAL`：`.pbi/` 等本机缓存，排除出正式项目。
- `SERIALIZATION_EQUIVALENT`：等价序列化、顺序、缩进或换行变化。
- `DEFAULT_ENRICHMENT`：非必需默认属性或元数据。
- `VERSION_UPGRADE`：Schema/版本声明升级但结构等价。
- `STRUCTURAL_REQUIRED`：新增或修复项目成立所必需的文件、引用或对象。
- `SEMANTIC_CHANGE`：模型、页面或绑定语义改变。
- `UNKNOWN`：不能解释；最终分级前必须关闭或保留为证据限制。

## 8. 异常双轴归因

每个异常必须同时选择一个 Playbook 事件类型、一个严重度和一个 V1 主因：

| V1 主因 | 典型问题 | 常见 Playbook 类型 |
| --- | --- | --- |
| `GEN` | JSON/TMDL/引用生成错误 | Validation Failure |
| `SPEC` | 公开规范缺口或版本漂移 | Evidence Gap / Validation Failure |
| `DESKTOP` | 阻塞打开、自动修复、宿主补写 | Expected Negative Result / Validation Failure |
| `PATH` | Unicode、空格、长度或编码 | Expected Negative Result / Environment Failure |
| `MCP` | 连接或只读回读失败 | Environment Failure / Warning |
| `ENV` | 版本、权限、进程或工具状态 | Environment Failure |
| `HUMAN` | 打错项目、未按 Gate 执行 | Governance Failure |
| `PROVENANCE` | 读取/复制禁止来源 | Governance Failure |

表中只是常见映射，实际以证据为准。预期负面结果可形成完整业务结论，但未完成证据链仍是执行问题。

## 9. R-VLD-003 成本与价值评价

第一次保存/关闭/重开属于零种子核心验收，记为 `Core roundtrip`；第二次最终关闭/重开是为评价 Provisional Rule 加入的 `Playbook-only final roundtrip`。两者分开计量：

- Desktop 启动、保存、关闭、重开次数；
- Human 主动操作分钟、等待分钟、AI/机器检查分钟；
- 新增日志/清单/截图数量与字节；
- 只在该轮往返发现的问题、其严重度和避免的错误结论；
- 未发现新问题时，对置信度的实际增加及是否可由更低成本证据替代；
- 对后续项目的建议：Keep / Change / Retire / Move。

第二次往返是 `Playbook-only Alignment`，只能证明遵守并提供 utility 数据，不能因执行了它就证明规则有效。

## 10. 当前停止点

规划冻结提交形成并报告后，状态停在 `HG-00`。在 Human 明确确认冻结提交并授权正式 Run 前：

- 不启动 Power BI Desktop；
- 不连接 Modeling MCP；
- 不创建 A/B 正式 Run；
- 不生成任何 PBIP/PBIR/TMDL 项目；
- 不修改 V0 或 `playbook/**`。
