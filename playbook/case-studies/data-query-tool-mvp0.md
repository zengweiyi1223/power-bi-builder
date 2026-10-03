# Data Query Tool MVP-0 — 跨会话执行案例

本案例记录 Playbook v1.0 在一个非 Power BI、本地数据应用最薄闭环中的实际使用。DQT 的产品和技术选择不自动成为通用规则。

## 1. 固定来源

- 项目：`data-query-tool`
- Playbook：`v1.0@3e5051b6159193bd430dbd85060fd04062dfd00e`
- 任务 A 最终：`1711c24a8fd88fe89a9a9d86d80f3e449556d17d`
- 任务 B 最终：`f21f9c9d1d2803b0904fadc0c62a2b7a2e9a7842`
- 归档 checkpoint：`056c9f10d5bdc3a769c006c7a290db9375f69cba`
- main 归档合并：`bbe253661a18abfde60d04337ff3dce17367208f`
- 正式证据：实验 `README.md`、`REQUIREMENTS.md`、`TECH_DESIGN.md`、`VALIDATION.md`、`RECORDS.md`、`PLAYBOOK_FEEDBACK.md`

## 2. 最薄闭环

任务 A 交付固定虚构库存、SQLite repository、一个只读关键词 HTTP API、独立 Oracle 和 21 项测试。任务 B 在新的独立会话中仅凭仓库恢复上下文，加入 Vue 3 + Vite + TypeScript 页面，并完成 30 项全量测试、21 项后端回归、真实 Vite 代理和浏览器状态验证。

CloudBase/MySQL、其他筛选、CSV、认证、写操作、真实数据和云部署始终保持范围外；本地 SQLite 只作为可替换适配器，不被描述为正式云路线完成。

## 3. 对 Playbook 的实际支持

- 新会话读取固定提交、根入口、Contract、唯一 Validation、实现、Oracle 和测试后，能够恢复任务 A 终点、禁区、下一 Gate 和 rollback point；没有依赖任务 A 对话记忆。
- Human 作为 A→B 的交接棒，只转移固定基线和任务提示；长过程由执行者从仓库回读，支持 `Human Relay`。
- 独立 Oracle、真实 HTTP、真实代理、真实浏览器和故障状态避免由生成链路自证。
- 环境、验证、权限和证据事件分别归因；失败证据不被静默忽略。
- 阶段级 checkpoint 足以恢复，不需要为每个动作提交。
- 最终归档保留实验目录、实验分支和 merge commit，区分“任务完成”与“合并 main”的独立 Human 授权。

## 4. 发现的摩擦

- 小型切片仍需要多份逻辑记录；通过 Artifact Map、稳定 ID 和只更新唯一 Validation 控制重复。
- 任务从后端实验扩展到 UI 后，正式反馈仍沿用最初 `PF-EXP + MD-DATA + MD-SEC`，说明 Contract 扩展时需要重新检查 `MD-UI` 和阶段裁剪。
- machine、AI wait、Human active time 无法可靠拆分，正确记录为 `unknown`；不能为了 ROI 或效率声明补估数字。
- 自动派发和回读能够减少人工操作，但相较 Human Relay 会消耗更多上下文和协调 Token。

## 5. 不进入 Core 的项目事实

SQLite、Node 24、pnpm、Vue、Vite、TypeScript 6、Edge DevTools、具体端口、字段数量和 CloudBase 路线均是 DQT 项目事实。它们只证明通用 Gate 可以承载该项目，不证明其他项目应采用相同技术。

## 6. v1.0.1 影响

- 澄清 Contract 扩展后的重新裁剪；
- 增加 Human Relay / Automatic Orchestration 协调模式；
- 增加紧凑阶段转移包；
- 增加 Git 工作状态和验证对象字段；
- 将 Reference Scan 作为条件式 Guidance；
- 保持 ROI 计量为 Provisional，不引入伪精确记录。
