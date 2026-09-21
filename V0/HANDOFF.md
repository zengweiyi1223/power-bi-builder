# Power BI Builder — V0 交付与交接

交接日期：2026-09-21 · 运行编号：`20260917-003433`

## 1. 结论

V0 的端到端功能链路已跑通：固定 CSV → Codex → 微软官方 Power BI Modeling MCP → Power Query/语义模型/DAX → Codex 生成 PBIR → PBIP → Power BI Desktop。报告可打开、展示、筛选、保存并重开；重开后 MCP 再次回读模型并执行 DAX，结果与独立基准一致。

**验收口径：功能实验成功，最终版精确 Schema 校验有一项待补证。** Desktop 保存后把切片器 `visual.json` 的 `$schema` 从 `visualContainer/2.9.0` 升至 `2.12.0`，而该版本的公开 Schema 地址在验收时返回 404。因此不能声称最终文件已按自身声明的 2.12.0 Schema 严格校验；这不是已观察到的报表使用故障，也不应把旧版兼容性校验冒充为精确校验。微软[公开版本记录](https://github.com/microsoft/json-schemas/blob/main/fabric/item/report/definition/visualContainer/CHANGELOG.md)可供后续跟踪；完整实验记录见 [VALIDATION.md](runs/20260917-003433/VALIDATION.md)。

## 2. 实验范围与结果

| 环节 | V0 结果 |
| --- | --- |
| 输入与基准 | 固定 15 行销售 CSV；独立 Python 脚本生成总计、月份、品类和零分母预期值。 |
| 语义模型 | MCP 创建/回读 `FactSales`、`DimProduct`、`DimDate`，3 个 Ready 的 Import/M 分区、2 条活动单向关系、5 个度量值及关键日期属性。 |
| DAX | 总计销售额 `9356.75`、毛利额 `3011.95`、毛利率 `32.1901%`；Technology 销售额 `7690`、毛利额 `2314`；零销售额毛利率为 BLANK，均符合独立基准。 |
| 报表 | 唯一 `Overview` 页面：3 张 KPI 卡片、月度趋势图、品类柱状图、品类下拉切片器，共 6 个视觉对象。 |
| Desktop 验收 | 首次打开和保存后重开均无错误或自动修复提示；Technology 筛选和清除后的卡片、图表变化正确，页面清晰可读。 |
| 持久化 | PBIR 保存前后业务语义未漂移；最终 MCP 回读 3 表、2 关系、5 度量值及代表性 DAX 成功。 |

功能验收基线提交为 `2db7009`。后续提交仅整理项目报告、教程和交接材料，不改写 V0 的成功口径或正式运行产物。

## 3. 关键文件地图

项目入口与说明：

- [`../README.md`](../README.md)：项目入口、当前状态和目录说明。
- [`REQUIREMENTS.md`](REQUIREMENTS.md)：已冻结的 V0 需求、执行步骤和验收基线。
- [`HANDOFF.md`](HANDOFF.md)：本文件；汇总结论、交付物、复用规则和后续方向。
- [`../tutorial/xhs/cards.html`](../tutorial/xhs/cards.html)：五张图文教程的唯一内容源；同目录提供 JPG 发布版本、导出脚本和版面检查脚本。
- [`../.gitignore`](../.gitignore)：忽略本机 Power BI 缓存、Python 缓存及 `V0/.work/`；不忽略正式运行产物。
- [`../.gitattributes`](../.gitattributes)：普通文本规范换行；PBIP/PBIR/TMDL 与项目内的 Power BI JSON 保留 Desktop 原生字节。

V0 数据、种子、脚本和运行产物：

| 路径 | 用途 |
| --- | --- |
| [`data/sales.csv`](data/sales.csv) | 各次运行共用的固定销售输入，不动态随机生成。 |
| [`seed/`](seed/) | 人工创建的空白 PBIP/PBIR 种子；保留原件，不在其上实施 Demo。 |
| [`scripts/calc_expected.py`](scripts/calc_expected.py) | 从 CSV 独立计算 DAX 对照基准。 |
| [`scripts/validate_pbir.py`](scripts/validate_pbir.py)、[`requirements.txt`](scripts/requirements.txt) | PBIP/PBIR 离线校验及其依赖版本。 |
| [`runs/20260917-003433/project/PowerBIBuilderV0Seed.pbip`](runs/20260917-003433/project/PowerBIBuilderV0Seed.pbip) | **可直接用 Desktop 打开的最终 Demo 入口。** 同目录的 `.Report/` 是 PBIR 页面与 6 个视觉对象，`.SemanticModel/` 是 TMDL 模型、M 表达式、关系和度量值；这些目录必须与 `.pbip` 一起保留。 |
| [`runs/20260917-003433/expected-results.json`](runs/20260917-003433/expected-results.json) | 本次运行的独立预期值。 |
| [`runs/20260917-003433/VALIDATION.md`](runs/20260917-003433/VALIDATION.md) | 逐阶段验收、环境、Git 快照、PBIR diff 和已知限制。 |
| [`runs/20260917-003433/logs/final-mcp-readback.json`](runs/20260917-003433/logs/final-mcp-readback.json) | 保存重开后的 MCP 对象和 DAX 回读摘要。 |
| [`runs/20260917-003433/evidence/`](runs/20260917-003433/evidence/) | 未筛选与 Technology 筛选的两张关键截图。 |
| `.work/` | 被 Git 忽略的可重建临时依赖/中间文件，不作为验收证据。 |

Desktop 在 `project/` 下生成的 `.pbi` 本机设置与缓存可能仍存在于磁盘，但被 Git 忽略，不属于正式交付。

## 4. 复核入口与已知边界

- 打开上述运行目录中的 `.pbip`，不要打开或修改 `seed/`。
- 对照 [未筛选截图](runs/20260917-003433/evidence/overview-unfiltered.png)和 [Technology 筛选截图](runs/20260917-003433/evidence/overview-technology.png)；精确数值以 `expected-results.json` 和最终 MCP 日志为准。
- Git 提交 `535a0c7`（Desktop 保存前）与 `c7a4579`（保存后）保留 PBIR 原始差异；验收提交为 `2db7009`。
- 后续若微软发布 `visualContainer/2.12.0` 的公开 Schema，可对最终切片器文件补做精确校验并更新验收记录；无需为此改写已能正常使用的 Demo。
- 跨机器数据源重绑定、Power BI Service 发布和产品化能力不属于本次 V0 验证范围。

## 5. 复用规则

- 创建新的正式运行时，先复制完整的不可变种子目录，再在独立运行目录操作；不要修改种子原件。
- 将运行副本及其项目文件改为实际业务报表名称，不要让最终交付物继续沿用 `Seed`。重命名时必须保持 `.pbip` 文件及其 Report、SemanticModel 目录的名称和相对引用一致。
- 每次运行使用独立 `<run-id>`，把项目、日志、证据、独立基准和验收记录放在同一运行目录中。
- 教程卡片用于操作说明和对外分享，不代替 `VALIDATION.md`、机器日志或正式验收证据。

## 6. 后续方向

本节记录从 V0 交接出去的规划，不授权启动实验，也不向已冻结的 V0 追加目标。每个方向执行前应另定范围、验收口径、目录和回滚点。

| 顺序 | 方向 | 核心问题 | 建议位置 | 阶段产物 |
| --- | --- | --- | --- | --- |
| 1 | 零种子实验 | 人工创建 PBIP/PBIR 种子是否必要？ | `V1-zero-seed/` | 可重复实验、三级结论、技术限制记录。 |
| 2 | 项目闭环 Playbook | 这套人机协作方法能否复制到其他项目？ | `playbook/` | 通用流程、文档模板、Power BI 适配说明、跨项目试用结果。 |
| 3 | Power BI 能力扩展 | 在已证明的本地链路上，哪些新能力值得逐项加入？ | 后续独立 `V2-*` 实验 | 按优先级分别立项、验收和交付。 |

### 6.1 `V1-zero-seed/`：验证从空目录直出

从全新空目录开始，不读取或复制 `V0/seed/`，也不把 Desktop 生成的空壳暗藏为模板。最小实验只回答“种子是否必要”，不同时引入 Service、多页面或新数据源。

1. 固定输入、Desktop/MCP 版本及允许使用的公开规范，留存空目录起点。
2. AI 生成项目入口、Report 和 SemanticModel 工程结构，记录首次打开前的完整文件清单。
3. Desktop 首次打开、必要的模型/页面创建、保存重开；区分 AI 生成内容和 Desktop 自动补写内容。
4. 至少用不同项目名和路径重复一次，避免一次性碰巧可用。

结论分级为：**完全成立**、**近似成立**或**种子仍必要**。“零种子”不等于“零人工”，凭据、系统确认和 Desktop 操作仍应单独记录。

### 6.2 `playbook/`：提炼可复用的项目闭环

先复盘 V0 与零种子实验，再把 Power BI 特有操作从通用方法中剥离：目标与范围 → 需求/验收契约 → AI/人工职责 → 安全工作区和 Git 回滚 → 分阶段制品 → 人工交接 → 结论与文件地图。

建议产物包括通用流程、需求模板、执行记录模板、交接模板、决策记录模板和 Power BI 适配说明。应用到一个非 Power BI 小项目并完成跨项目验证后，再考虑封装为 Codex Skill。

### 6.3 Power BI 能力扩展：独立立项

候选能力包括 Power BI Service 发布、更多页面、更多数据源和复杂视觉对象。每次只选择一个清晰增量，单独建立需求与成功标准；它们以 V0 为参照，但不属于“继续扩展 V0”，也不与零种子实验混跑。

下一次行动入口：先为 `V1-zero-seed/` 编写独立需求文档和实验设计；获得明确执行指令后再创建目录或运行 Power BI。
