# V1 Zero Seed — 总体验证记录

- 状态：`Passed`
- 日期/时区：`2026-09-22`，`America/Los_Angeles`
- Playbook 基线：`3ee871d618db84d55b3b2f86a198ac552864317e`
- V1 采用前草案：`22da780412f27decf17a097548d65d151c75b235`
- no-ff merge：`8c28f5e340ec41ef56e16d942fd2f9eb97767963`
- 需求冻结：`82b448957ab08a5452df297a7a95d7b6def67bef`
- Run A final：`21af7b278d9be6c40ca7315fb0dd5298e3565506`
- Run B final：`a127b7978990d1d0c6027a72c689704dd5b09a04`
- 最终验收提交：`c9003aaf29056edac67be88e9f9cf6745816a9cd`

本文件只汇总已核实的跨 Run 事实。逐阶段 Execute–Verify、Human Gate、异常、manifest、MCP 和 Codex 文件操作分别保存在各 Run 目录。

## 1. 基线与治理

| 条款 | 结果 | 独立依据 |
| --- | --- | --- |
| Playbook 真实继承 | Passed | `3ee871d` 是当前分支祖先；merge `8c28f5e` 双亲为 `22da780` 与 `3ee871d` |
| V1 规划冻结 | Passed | `82b4489`；Required/Provisional/Guidance 映射与 HG-00 前停止点已冻结 |
| V0 与 Playbook 不变 | Passed | `git diff 82b4489..Run-B-final -- V0 playbook` 为空 |
| 禁止来源 | Passed | 两个 Run 的来源声明、空目录证据、文件操作日志；未读取/复制 `V0/seed/**` 或 V0/其他 Run 工程作为起点 |
| 独立分支与 rollback | Passed | `codex/v1-zero-seed`；阶段级 checkpoint 可识别 |
| 最终环境 | Passed | Run B 关闭后 `PBIDesktop=0`、`msmdsrv=0`，工作树在 Run B final checkpoint 上干净 |

## 2. 正式 Run 与 checkpoint

| 试验 | Run ID / 项目 | 路径条件 | 结果 | 关键 checkpoint |
| --- | --- | --- | --- | --- |
| A | `20260922-012919-a` / `ZeroSeedAlpha` | ASCII 短路径 | Passed | Run/R1 `473ff1e`；pre-open `57b6e64`；首开 `3707c47`；首存 `44c2fb7`；核心往返 `9c34b5f`；final `21af7b2` |
| B | `20260922-032410-b` / `零种子 Beta` | 不同父目录、空格、Unicode | Passed | Run/R1 `a121769`；pre-open `6d0a594`；首开 `af23869`；首存 `5428294`；核心往返 `45a0dda`；final `a127b79` |

两组均由独立的 0 文件、0 子目录 Trusted baseline 生成。B 重新生成全部工程文件与页面标识符；A 页面 ID 为 `78c91ddf6ab57cf694f0`，B 为 `ee10ab53292bad27c265`。

## 3. Execute–Verify 与持久化矩阵

| 验收条款 | Run A | Run B | 结论 |
| --- | --- | --- | --- |
| 首开前项目 | 9 文件 / 1498 bytes | 9 文件 / 1503 bytes | Codex 在 Desktop 启动前生成完整最小 PBIP/PBIR/TMDL |
| Desktop 首开 | 标题/`Overview` 正确，无提示；磁盘 0/0/0 | 标题/`Overview` 正确，无提示；磁盘 0/0/0 | 首开不依赖 Desktop 写盘或修复 |
| 首次显式保存 | 6 added / 9 modified / 0 deleted；3643 bytes | 6 added / 9 modified / 0 deleted；3647 bytes | 保存时发生相同类别的规范化、默认元数据、版本升级和本机缓存写入 |
| `STRUCTURAL_REQUIRED` / `SEMANTIC_CHANGE` | 0 / 0 | 0 / 0 | 未识别到使 Codex 首开前项目不成立的结构补写或语义改变 |
| 第一次重开 + MCP | UI 正确；磁盘 0/0/0；模型 1606、PowerBI_V3、0 表 | 同左，Unicode/空格身份保留 | 核心往返 Passed；MCP 全部只读，mutation=true 为 0 |
| Playbook-only 额外重开 | 第三个 Desktop/模型进程；磁盘 0/0/0 | 第三个 Desktop/模型进程；磁盘 0/0/0 | R6 Passed；没有新增结构或语义发现 |
| 最终关闭 | 无提示，进程退出 | 无提示，进程退出 | 最终现场稳定 |

R7 逐文件复算结果：A 为 15 文件 / 3643 bytes，tree SHA-256 `01AE7F03157DF35DF430A73EC62166393E81195E8B7652F7283F37224A0E66C2`；B 为 15 文件 / 3647 bytes，tree SHA-256 `B9460B8B2642080D92050A861791FC971CF01A32EC46BB383A4E3DBC8F08C737`。两者均与各自 `FINAL_REOPEN_NO_SAVE.json` 为 0/0/0。

## 4. Human、MCP 与 Codex 操作分离

- Human：HG-00–HG-05 的请求、精确目标、禁止动作、实际确认和继续授权写入各 Run 的 `logs/HUMAN_ACTIONS.md`。A/B 的首开、首存、重开、最终可见状态和最终关闭均由 Human 明确确认。
- MCP：只在 R0 能力检查与 R5 回读中使用；每次操作写入 `logs/MCP_ACTIONS.jsonl`。没有模型或报表 mutation。
- Codex：项目和证据文件的创建/修改、前后哈希、原因与验证写入 `logs/CODEX_FILE_ACTIONS.jsonl`；R7 汇总操作写入 `r7/CODEX_FILE_ACTIONS.jsonl`。

## 5. 异常、Decision 与 Deviation

- Run A：5 个事件，其中 1 个 Blocking GEN 在 R2b 停止依赖链、同一原子阶段修正并全量重验；3 个 Non-blocking；1 个 Informational。
- Run B：9 个事件，0 个 Blocking；8 个 Non-blocking 工具/环境或证据事件；1 个 Informational。每次验证脚本失败均先停止、修正并从头重跑，未改变项目现场。
- A/B 共同保留的非阻塞 Evidence Gap：Desktop 首存移除三个根文件中公开 Schema 标记为 required 的 `$schema`。原样文件不能声称直接通过该公开 Schema；Desktop 无提示重开、磁盘稳定与 MCP 回读支持功能结论，但不消除规范证据缺口。
- 主要 Decision：`DCS-001`–`DCS-005`。执行偏差：`DEV-001` 精确时间未前置采集；`DEV-002` Desktop canonical root 与公开 Schema 的 `$schema` 要求不一致。

## 6. Rule conformity 与 utility

- Required Rules：运行时全部 `Conformant`。该结论基于 Contract、阶段证据、Gate、checkpoint 和最终 Handoff；不等同于所有规则都具有相同 utility。
- R-GIT-002（Guidance）：采用阶段级 checkpoint，实际可用于 Run A/B 的预开、首存、核心往返和最终状态回滚；评价为 Helpful / Keep。
- R-VLD-003（Provisional）：A/B 均 Conformant。额外最终往返合计增加 2 次 Desktop 启动、4 个主要证据文件和 10411 bytes；Human 均报告“约几秒”，机器检查记录合计约 2.38 分钟，但 Human active/wait 未精确计量。两次额外往返的新发现、捕获问题和避免错误结论均为 0，只增加“第三个独立进程仍可稳定打开”的重复性信心。
- R-VLD-003 utility：`Low positive marginal value`。建议 `Change`：对已经完成核心保存/关闭/重开、精确 manifest diff 和独立回读的低风险最小项目，改为风险触发或抽样；高风险持久化宿主仍可保留强制最终往返。此处只提供 V1 反馈，不修改 Playbook v0.1。

## 7. 三级业务结论

最终分类：`完全零种子`。

理由：两组独立 Run 均满足冻结标准——来源和空目录证据完整；Codex 在首开前生成全部最小工程；Desktop 无阻塞错误、修复警告或人工建壳动作地直接打开；首开磁盘无变化；首存没有已识别的 `STRUCTURAL_REQUIRED` 或无法解释的 `SEMANTIC_CHANGE`；保存、关闭、两次重开、项目身份和只读模型回读均通过。

“Desktop 首次显式保存时写入/规范化”与业务分类“Desktop 首次补写”明确区分：前者在 A/B 都发生，但证据显示它不是首开所需的修复或结构性初始化。因此不能据此把结果降为“Desktop 首次补写”。同时，本实验没有做删除 `.platform` 后重开的反事实试验，不能声称这些文件在所有后续场景中绝对不必要。

## 8. 五维最终判定

- 功能结果：`Passed — 完全零种子`。在本次版本与两条计划路径中，不再需要人工先创建空白 PBIP 种子。
- Contract 符合度：`Conformant`。A/B 均遵守冻结路线、Human Gate、停止/恢复规则与来源边界。
- 证据完整度：`Complete with known non-blocking evidence gaps`。关键功能链证据完整；公共 Schema `$schema` 差异与时间计量限制明确保留。
- 运行/持久化状态：`Passed`。A/B 均可打开、保存、关闭、两次重开；最终磁盘与 manifest 一致，进程均退出。
- 安全与权限状态：`Passed`。只读提升仅用于环境探测；无凭据、PII、发布、破坏性操作或 MCP mutation；V0/Playbook 未修改。

明确不能声称：

- 所有 Power BI Desktop 版本、操作系统、路径长度、语言环境或复杂项目均兼容；
- 复杂模型、数据刷新、DAX、视觉对象、Power BI Service 或跨机器迁移已验证；
- Desktop 保存生成的 `.platform`/本机文件具有或不具有普遍的反事实必要性；
- Desktop canonical 文件直接符合当前公开根 Schema；
- R-VLD-003 的 conformity 本身证明其 utility，或本实验已修改 Playbook v0.1。
