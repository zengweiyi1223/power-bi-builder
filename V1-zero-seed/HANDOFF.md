# V1 Zero Seed — 交接

日期：`2026-09-22` · Runs：`20260922-012919-a`、`20260922-032410-b` · Playbook：`3ee871d618db84d55b3b2f86a198ac552864317e`

## 1. 结论

- 功能结果：`Passed — 完全零种子`
- Contract 符合度：`Conformant`
- 证据完整度：`Complete with known non-blocking evidence gaps`
- 运行/持久化状态：A/B 均完成首开、显式保存、关闭、第一次重开、额外最终重开与最终关闭；磁盘稳定
- 一句话结论：在 Power BI Desktop `2.157.1354.0` 的本机 Windows 环境中，Codex 从两个独立空目录生成的最小 PBIP/PBIR/TMDL 项目均可无修复地打开、保存和重开，人工空白 PBIP 种子对本 V1 场景不再必要。

Desktop 首次显式保存确实规范化 9 个文件并新增 6 个默认/平台/本机文件，但首开前后磁盘零变化，且没有已识别的 `STRUCTURAL_REQUIRED` 或 `SEMANTIC_CHANGE`；因此本项目不归类为“Desktop 首次补写”。

明确不能声称：所有版本、复杂模型、数据刷新、DAX、视觉对象、Service、跨机器、任意路径类别或 `.platform` 的反事实必要性已验证；也不能声称 Desktop canonical 根文件直接通过当前公开 Schema，或 V1 已修改 Playbook。

## 2. 交付物与入口

| 路径/入口 | 用途 | 完整性或哈希 |
| --- | --- | --- |
| `REQUIREMENTS.md` | 冻结 Contract 与三级结论口径 | freeze `82b4489` |
| `VALIDATION.md` | 跨 Run 最终证据与五维判定 | R7 final |
| `RECORDS.md` | DCS-001–005、DEV-001–002 | R7 final |
| `PLAYBOOK_FEEDBACK.md` | conformity / utility 分离评价 | R7 final |
| `r7/ACCEPTANCE_EVIDENCE.md` | R7 机器复核、tree hash、冻结边界 | R7 final |
| `runs/20260922-012919-a/` | Run A 项目、manifest、日志、截图、验证 | final `21af7b2`；project tree `01AE7F...E66C2` |
| `runs/20260922-032410-b/` | Run B 项目、manifest、日志、截图、验证 | final `a127b79`；project tree `B9460B...C737` |

所有正式项目、必要截图、manifest 和日志均在 Git 范围内；`.pbi` 本机缓存由 manifest 记录但按 adapter 规则不作为正式项目源文件提交。

## 3. 复核方法

1. 从 Playbook `3ee871d`、merge `8c28f5e` 与 freeze `82b4489` 核对祖先、Contract 和禁止来源边界。
2. 逐 Run 阅读 `RUN.md`、`VALIDATION.md`、`logs/HUMAN_ACTIONS.md`、`logs/MCP_ACTIONS.jsonl`、`logs/EVENTS.jsonl` 与 R2–R6 evidence。
3. 复算 `PRE_OPEN`、`POST_OPEN_NO_SAVE`、`POST_SAVE_CLOSED`、`POST_REOPEN_NO_SAVE`、`FINAL_REOPEN_NO_SAVE` 的路径、大小和 SHA-256；最终项目应与 final manifest 为 0/0/0。
4. 对照截图/Human 观察、Desktop 进程身份和 MCP 只读模型回读，确认产品运行证据不只依赖生成逻辑。
5. 最后检查 `r7/ACCEPTANCE_EVIDENCE.md` 与本文件的不能声称内容；不要用“Passed”覆盖公共 Schema 与计量限制。

## 4. 证据与回滚点

| 结论/阶段 | 证据 | Git checkpoint |
| --- | --- | --- |
| Playbook 真实继承 | merge 双亲与祖先关系 | `8c28f5e340ec41ef56e16d942fd2f9eb97767963` |
| V1 规划冻结 | Contract、符合性、路线、安全和 Gate | `82b448957ab08a5452df297a7a95d7b6def67bef` |
| Run A 起点 / pre-open / 首存 / final | Run A logs、manifest、evidence | `473ff1e` / `57b6e64` / `44c2fb7` / `21af7b2` |
| Run B 起点 / pre-open / 首存 / final | Run B logs、manifest、evidence | `a121769` / `6d0a594` / `5428294` / `a127b79` |
| 跨 Run 最终验收 | 本 Handoff、总 Validation、Records、Feedback、R7 evidence | R7 result checkpoint；完整 SHA 在 metadata/reporting commit 与最终报告中记录 |

## 5. 决策、偏差与限制

- Decision：`DCS-001` 固定/继承 Playbook；`DCS-002` 保留采用前实验设计；`DCS-003` 分离核心与附加往返；`DCS-004` 按冻结标准判定完全零种子；`DCS-005` 对 R-VLD-003 建议 Change。
- Deviation：`DEV-001` 未前置精确采集 Human active/wait 时间；`DEV-002` Desktop canonical 根文件移除公开 Schema required `$schema`。两项均为 Non-blocking，且明确限制相应结论。
- 环境依赖：Windows、Power BI Desktop `2.157.1354.0` x64、Modeling MCP `0.5.0-beta.13`、运行时获取的微软公开文档/Schema。
- 已知限制：两个最小空项目、单机单版本；没有业务数据、复杂模型或 Service。
- 残余风险：未来 Desktop/Schema 版本漂移；Unicode/空格之外的路径边界；Desktop 写入的 `.platform` 在其他场景中的必要性；R-VLD-003 成本计量精度。

## 6. Playbook 反馈入口

- [VALIDATION](VALIDATION.md)
- [RECORDS](RECORDS.md)
- [PLAYBOOK_FEEDBACK](PLAYBOOK_FEEDBACK.md)
- [R7 evidence](r7/ACCEPTANCE_EVIDENCE.md)
- Playbook 基线：`3ee871d618db84d55b3b2f86a198ac552864317e`
- 需求冻结：`82b448957ab08a5452df297a7a95d7b6def67bef`
- Run A/B final：`21af7b278d9be6c40ca7315fb0dd5298e3565506` / `a127b7978990d1d0c6027a72c689704dd5b09a04`
- 最终验收：R7 result checkpoint；SHA 由后续 metadata/reporting commit 记录

后续只能由 Playbook 对话读取这些产物并决定是否升级 v0.2。本 V1 不修改 `playbook/**`、不创建 v0.2、不做跨项目方法论总结，也不封装 Skill。
