# Playbook Changelog

## v1.0 candidate — 2026-09-28

输入基线：Playbook v0.2 `dff3a717d59935697e310a29caf6b29dff11ff11`；生命周期设计 `2319a6904cd1dba0b696e59b9376889a3179b068`；非 Power BI 实验 `data-quality-checker@416ec65453fd280a611065c09272aa5d293a9f33`。

- 将 v0.2 Evidence Gate Kernel 嵌入唯一的十阶段开发生命周期。
- 增加六种基础画像、八种风险修饰器和 `Required / Conditional / Not Applicable + 理由` 裁剪。
- 增加人机责任表达、需求原因对齐、条件式方案比较和多视角评审 Guidance。
- 增加项目根入口、Artifact Map、逻辑记录/物理文件分离和按画像目录示例。
- 增加可验证任务拆分和“风险优先 → 最小闭环 → 逐步扩展”的排序原则。
- `R-VLD-003` 从 Provisional 升为 Required；`R-VDC-002` 升为条件触发的 Required；`R-EXV-003` 保持 Provisional。
- 明确 Rolling Validation 与 Final Handoff 的单一权威边界。
- 增加 PROJECT、TECH_DESIGN、DELIVERY_PLAN、RELEASE_OPERATIONS 模板，并更新现有模板。
- Power BI adapter 区分文件、Desktop、Modeling MCP、Power BI Service 浏览器插件和 API/自动化路线；插件路线标记为未被 V0/V1 验证。
- 详细处置见 [v1.0 Rule and lifecycle disposition](reviews/v1.0-disposition.md)。

本节随候选版本存在，不代表 v1.0 已发布。人工验收和最终冻结提交完成后移除 candidate 标记并记录正式提交号。

## v0.2 — 2026-09-27

输入基线：Playbook v0.1 `3ee871d618db84d55b3b2f86a198ac552864317e`；V1 main `442b2c3223b2de3eb1c38ca015c4cd84fda66694`。

- 保留全部 18 条 v0.1 Rule ID；没有退役规则。
- 修改 `R-VLD-002`：允许以状态转换表压缩重复无变化证据，同时保留首末状态、首次转换和异常。
- 修改 `R-VLD-003`：从笼统往返要求改为风险触发、抽样或有理由省略，继续保持 Provisional。
- 修改 `R-GIT-001`：高风险宿主状态转换前必须有 rollback point。
- 新增 `R-EXV-003`：仅在声称效率时前置采集 Human active、wait 和 machine time；Provisional。
- 新增 `R-VDC-002`：最少步骤声明必须区分生产、诊断和验证专用操作；Provisional。
- Power BI adapter 增加 Desktop 生命周期、首存覆盖风险、PBIR/TMDL 路线、对象加载状态、项目级设置和 MCP 可选边界。
- 详细处置见 [v0.2 Rule disposition review](reviews/v0.2-rule-disposition.md)。

冻结规则：非 Power BI 项目 HANDOFF 返回前不升级 v1.0；新增 Provisional Rules 和状态转换证据压缩必须接受跨领域评价。

## v0.1 — 2026-09-22

基线来源：Power BI Builder V0，Git 提交 `78a20f0179b9deb5c3cdaa5e1fc64f502a78ec7b`。

- 首次定义 Frame、Contract、Prepare、Preflight、Execute–Verify、Decide、Handoff 闭环。
- 建立 Required、Provisional、Guidance 规则等级和稳定 Rule ID。
- 增加安全治理、Human Gate、独立验收、失败严重度、回滚和实验反馈规则。
- 将 Power BI 实现隔离到 adapter，将 V0 事实和规则依据隔离到 case study。
- `R-VLD-003` 为 v0.1 的显式 Provisional Rule，等待 V1 和后续跨领域项目评价。

冻结规则：V1 HANDOFF 返回前不升级 v0.2。非阻塞排版或链接问题只登记；阻塞性错误通过独立 erratum 处理。
