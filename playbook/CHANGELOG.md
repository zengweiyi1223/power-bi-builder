# Playbook Changelog

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
