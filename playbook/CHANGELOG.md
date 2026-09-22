# Playbook Changelog

## v0.1 — 2026-09-22

基线来源：Power BI Builder V0，Git 提交 `78a20f0179b9deb5c3cdaa5e1fc64f502a78ec7b`。

- 首次定义 Frame、Contract、Prepare、Preflight、Execute–Verify、Decide、Handoff 闭环。
- 建立 Required、Provisional、Guidance 规则等级和稳定 Rule ID。
- 增加安全治理、Human Gate、独立验收、失败严重度、回滚和实验反馈规则。
- 将 Power BI 实现隔离到 adapter，将 V0 事实和规则依据隔离到 case study。
- `R-VLD-003` 为 v0.1 的显式 Provisional Rule，等待 V1 和后续跨领域项目评价。

冻结规则：V1 HANDOFF 返回前不升级 v0.2。非阻塞排版或链接问题只登记；阻塞性错误通过独立 erratum 处理。
