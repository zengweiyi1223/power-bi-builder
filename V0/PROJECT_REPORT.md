# Power BI Builder — V0 项目报告

报告日期：2026-09-17 · 运行编号：`20260917-003433`

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

## 3. 当前文件地图

项目根目录只放仓库入口与 Git 规则：

- [`README.md`](../README.md)：项目入口和当前状态。
- [`.gitignore`](../.gitignore)：忽略本机 Power BI 缓存、Python 缓存及 `V0/.work/`；不忽略正式运行产物。
- [`.gitattributes`](../.gitattributes)：普通文本规范换行；PBIP/PBIR/TMDL 与项目内的 Power BI JSON 保留 Desktop 原生字节。

V0 目录按用途分开：

| 路径 | 用途 |
| --- | --- |
| [`REQUIREMENTS.md`](REQUIREMENTS.md) | 已冻结的 V0 需求、执行步骤和验收基线。 |
| [`data/sales.csv`](data/sales.csv) | 各次运行共用的固定销售输入，不动态随机生成。 |
| [`seed/`](seed/) | 人工创建的空白 PBIP/PBIR 种子；保留原件，不在其上实施 Demo。 |
| [`scripts/calc_expected.py`](scripts/calc_expected.py) | 从 CSV 独立计算 DAX 对照基准。 |
| [`scripts/validate_pbir.py`](scripts/validate_pbir.py)、[`requirements.txt`](scripts/requirements.txt) | PBIP/PBIR 离线校验及其依赖版本。 |
| [`runs/20260917-003433/project/PowerBIBuilderV0Seed.pbip`](runs/20260917-003433/project/PowerBIBuilderV0Seed.pbip) | **可直接用 Desktop 打开的最终 Demo 入口。** 同目录的 `PowerBIBuilderV0Seed.Report/` 是 PBIR 页面与 6 个视觉对象，`PowerBIBuilderV0Seed.SemanticModel/` 是 TMDL 模型、M 表达式、关系和度量值；这些目录必须与 `.pbip` 一起保留。 |
| [`runs/20260917-003433/expected-results.json`](runs/20260917-003433/expected-results.json) | 本次运行的独立预期值。 |
| [`runs/20260917-003433/VALIDATION.md`](runs/20260917-003433/VALIDATION.md) | 逐阶段验收、环境、Git 快照、PBIR diff 和已知限制。 |
| [`runs/20260917-003433/logs/final-mcp-readback.json`](runs/20260917-003433/logs/final-mcp-readback.json) | 保存重开后的 MCP 对象和 DAX 回读摘要。 |
| [`runs/20260917-003433/evidence/`](runs/20260917-003433/evidence/) | 未筛选与 Technology 筛选的两张关键截图。 |
| `.work/` | 被 Git 忽略的可重建临时依赖/中间文件，不作为验收证据。 |

运行目录中有 32 个 Git 跟踪文件；其中 `.gitkeep` 仅维持空目录结构。Desktop 在 `project/` 下生成的 `.pbi` 本机设置与缓存可能仍存在于磁盘，但被 Git 忽略，不属于正式交付。

## 4. 复核入口与后续边界

- 打开上述运行目录中的 `.pbip`，不要打开或修改 `seed/`。
- 对照 [未筛选截图](runs/20260917-003433/evidence/overview-unfiltered.png)和 [Technology 筛选截图](runs/20260917-003433/evidence/overview-technology.png)；精确数值以 `expected-results.json` 和最终 MCP 日志为准。
- Git 提交 `535a0c7`（Desktop 保存前）与 `c7a4579`（保存后）保留 PBIR 原始差异；验收提交为 `2db7009`。
- 后续若微软发布 `visualContainer/2.12.0` 的公开 Schema，可对最终切片器文件补做精确校验并更新验收记录；无需为此改写已能正常使用的 Demo。
- 跨机器数据源重绑定、Power BI Service 发布和产品化能力不属于本次 V0 验证范围。
