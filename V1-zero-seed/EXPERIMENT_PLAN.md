# V1 Zero Seed — 实验计划

## 1. 设计原则

实验只测试工程壳来源，不把 Modeling MCP、业务数据或复杂报表混成首开前置条件。核心比较对象是同一试验的四个磁盘状态：

```text
空目录
  -> Codex 生成态
  -> Desktop 首开态（未保存）
  -> Desktop 首存态
  -> 稳定重开态
```

每个箭头均留下递归清单、SHA-256 和结构化差异。Desktop 能打开不等于完全零种子；必须证明首开没有补齐必需工程结构。

## 2. 试验单元

每个正式运行目录只容纳一个项目名、一个路径条件和一个 attempt：

```text
V1-zero-seed/runs/<run-id>/
├─ RUN.md
├─ VALIDATION.md
├─ project/                    # 创建后先证明为空；之后只放本次项目
├─ logs/
│  ├─ HUMAN_ACTIONS.md
│  ├─ MCP_ACTIONS.jsonl
│  ├─ CODEX_FILE_ACTIONS.jsonl
│  ├─ PREOPEN_MANIFEST.json
│  ├─ FIRST_OPEN_MANIFEST.json
│  ├─ FIRST_SAVE_MANIFEST.json
│  └─ REOPEN_MANIFEST.json
└─ evidence/
   ├─ PREOPEN_VALIDATION.md
   ├─ DIFF_FIRST_OPEN.md
   ├─ DIFF_FIRST_SAVE.md
   └─ REOPEN_VALIDATION.md
```

失败后不复用 `project/`。后续修正使用新的 `<run-id>` 或显式 `-attempt-N`，并在新记录中引用前一次失败。

## 3. 计划中的两组主试验

### A — ASCII 基线

- 项目名：`ZeroSeedAlpha`
- 预定位置：`V1-zero-seed/runs/<timestamp>-a/project/ZeroSeedAlpha/`
- 特征：短路径、ASCII、无空格。
- 用途：减少路径噪声，先验证公开格式推导出的最小工程壳。

### B — 名称与路径变化

- 项目名：`零种子 Beta`
- 预定位置：`V1-zero-seed/runs/<timestamp>-b/project path/零种子 Beta/`
- 特征：不同父目录、空格、Unicode。
- 用途：验证相对 `byPath`、文件系统编码和名称自洽性，排除 A 的偶然成功。

B 必须重新生成标识符和全部项目文件，不得复制或改名 A。A 的 Desktop 结果可以用于修正生成规则，但若修正规则发生变化，A 也要在新 attempt 中用同一规则重跑，保证两组可比较。

## 4. 阶段闸门

### P0 — 环境与治理预检

- 确认分支、Git 状态和基线提交。
- 记录 Desktop 完整版本、PBIP/PBIR 功能状态和 Modeling MCP 版本；不得沿用 V0 数值而不重新检查。
- 确认 Desktop 与本地模型进程均未运行。
- 固定允许使用的微软公开文档/Schema URL 与获取时间。
- 记录禁止来源确认，不扫描 `V0/seed/` 或 V0 项目目录内容。

通过条件：环境信息齐全、工作区可回滚、无目标进程、来源边界明确。

### P1 — 空目录证明

- 创建本次运行的 `project/`。
- 在任何项目文件写入前递归检查，文件数和子目录数都必须为 0。
- 把检查命令、时间和结果写到 `RUN.md`，而不是在 `project/` 内放占位文件。

通过条件：空目录证据可复核。

### P2 — Codex 生成与离线预检

- 依据公开规范生成最小 PBIP/PBIR/TMDL 项目。
- 所有创建和修改逐条写入 `CODEX_FILE_ACTIONS.jsonl`。
- 验证 JSON/TMDL 语法、根入口、Report/SemanticModel 目录关系、`byPath`、唯一页面和标识符唯一性。
- 生成 `PREOPEN_MANIFEST.json`，记录相对路径、字节数、SHA-256、文件角色和来源。
- 形成 Desktop 首开前 Git 快照。

停止条件：任何引用离开本次项目、存在未解释的既有文件、或离线验证失败。

### P3 — Desktop 首次打开（禁止保存）

- 人工仅双击或从 Desktop 打开本次根 `.pbip`。
- 不创建新报表，不执行另存为，不手工添加页面或模型对象。
- 记录所有对话框、修复、升级、隐私和预览确认。
- 在未保存时采集 `FIRST_OPEN_MANIFEST.json`。
- 将预打开与首开态差异分类；`.pbi/` 单独排除。

通过条件：Desktop 可进入项目且不存在阻塞错误。出现修复或结构性补写时可继续收证，但已失去“完全零种子”的资格。

### P4 — 首次保存与关闭

- 人工显式保存，然后关闭。
- 记录是否出现二次保存提示和实际选择。
- 确认 Desktop 与本地模型进程均退出。
- 采集 `FIRST_SAVE_MANIFEST.json` 和原始 diff。
- 分别评估字节变化、结构变化和语义变化。

通过条件：磁盘项目仍可离线解析，所有差异已分类或标记为待归因。

### P5 — 重开与只读回读

- 从同一根 `.pbip` 重开。
- 确认无阻塞错误，唯一 `Overview` 页面存在，SemanticModel 可识别。
- 如 Modeling MCP 可连接，创建新连接并只读回读模型；所有 MCP 调用写入独立日志。
- 采集 `REOPEN_MANIFEST.json`，关闭 Desktop 后再次确认磁盘稳定。

通过条件：项目可稳定重开；MCP 故障单独归因，不覆盖 Desktop 结果。

### P6 — 重复性与最终分级

- A 与 B 均完成 P0–P5 后才给出三级结论。
- 比较两组的首次补写类型、Schema 升级、目录命名和相对引用差异。
- 若规则在 A 后修正，使用相同最终规则重新执行新的 A 与 B attempt。
- 在总报告中列出主结论、适用版本、路径限制、置信度和所有例外。

## 5. 预定离线检查

规划阶段不实现检查器。执行阶段应优先扩展独立验证脚本，而不是靠目视判断：

- JSON 语法和文件声明的公开 Schema；公开文件不可得时必须显式记为未校验。
- 根 `.pbip` 引用目标 Report 目录存在。
- `definition.pbir` 的相对 `byPath` 解析后仍在本试验目录内并指向目标 SemanticModel。
- `definition.pbism` 与 TMDL 根文件存在且编码/换行被记录。
- PBIR 只有一个 `Overview` 页面，页面索引与目录一致。
- 所有项目级标识符在本次生成中唯一，A/B 不共用固定标识符。
- 清单中无 V0 项目路径、种子名称或外部绝对工程引用。

## 6. 决策表

| 观察 | 分类 | 候选结论 |
| --- | --- | --- |
| 首开无提示；只产生缓存；保存仅等价重排或默认元数据；重开成功 | 无结构性补写 | 完全零种子 |
| 首开可进入，但 Desktop 自动新增必需根文件/引用或报告修复；保存后稳定 | Desktop 首次补写 | Desktop 首次补写 |
| 首开阻塞，修正规范后新的独立 attempt 仍重复失败；人工空白壳才能继续 | 项目壳不可由当前方法可靠生成 | 仍需人工种子 |
| 只有 Unicode/空格路径失败，ASCII 的两组独立路径成功 | 路径兼容限制 | 完全零种子或首次补写，并附限制 |
| MCP 回读失败但 Desktop 打开、保存、重开均成功 | MCP 独立故障 | 不改变项目壳结论 |
| 首开前发现读取或复制既有项目文件 | 来源污染 | 无法判定，重做 |
| Desktop 版本、权限或进程状态不稳定 | 环境阻塞 | 无法判定，修复后重做 |

## 7. 本轮明确不执行

- 不启动 Power BI Desktop。
- 不连接 Modeling MCP。
- 不创建 A/B 的 `project/` 或任何 PBIP/PBIR/TMDL 文件。
- 不读取 `V0/seed/` 或 V0 正式运行中的项目文件。
- 不宣称零种子已经通过。
