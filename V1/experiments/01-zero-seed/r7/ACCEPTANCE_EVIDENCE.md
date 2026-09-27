# R7 Cross-Run Acceptance Evidence

检查时间：`2026-09-22T09:01:42.4373799-07:00` · 时区：`America/Los_Angeles`

## 1. Git、冻结边界与进程

- 分支：`codex/v1-zero-seed`
- R7 起点：`a127b7978990d1d0c6027a72c689704dd5b09a04`
- 起点工作树：clean
- Playbook `3ee871d618db84d55b3b2f86a198ac552864317e` 是 R7 起点的祖先：`true`
- `git diff 82b4489..a127b79 -- V0 playbook`：空
- Run B 最终关闭后：`PBIDesktop=0`、`msmdsrv=0`
- R7 不启动 Desktop、不连接 MCP、不修改项目文件。

## 2. 最终项目逐文件复算

| Run | 最终文件/bytes | 相对 `FINAL_REOPEN_NO_SAVE.json` | Project tree SHA-256 |
| --- | --- | --- | --- |
| A `20260922-012919-a` | 15 / 3643 | 0 added / 0 modified / 0 deleted | `01AE7F03157DF35DF430A73EC62166393E81195E8B7652F7283F37224A0E66C2` |
| B `20260922-032410-b` | 15 / 3647 | 0 added / 0 modified / 0 deleted | `B9460B8B2642080D92050A861791FC971CF01A32EC46BB383A4E3DBC8F08C737` |

Tree hash 输入为按路径排序的 UTF-8 文本行 `relative-path|bytes|file-sha256`，路径分隔符统一为 `/`。它用于 R7 快速复核，不替代各 Run 的逐文件 manifest。

## 3. 状态转换复核

| 转换 | Run A | Run B | 判定 |
| --- | --- | --- | --- |
| 空目录 → pre-open | 0/0 → 9 文件/1498 bytes | 0/0 → 9 文件/1503 bytes | 独立零种子生成 |
| pre-open → first open/no save | 0/0/0 | 0/0/0 | Desktop 首开未补写项目目录 |
| first open → first save/closed | +6 / ~9 / -0 | +6 / ~9 / -0 | Desktop 显式保存 canonicalization |
| first save → first reopen | 0/0/0 | 0/0/0 | 核心往返稳定 |
| first reopen → final reopen | 0/0/0 | 0/0/0 | Playbook-only 额外往返稳定 |
| final reopen → final close | 0/0/0；进程 0 | 0/0/0；进程 0 | 最终现场稳定 |

`~9` 表示 9 个已存在文件的字节变化；逐文件分类见各 Run `R4_POST_SAVE.md`。A/B 均没有被归类为 `STRUCTURAL_REQUIRED` 或 `SEMANTIC_CHANGE` 的变化。

## 4. 独立身份与来源

- A：`ZeroSeedAlpha`，页面 ID `78c91ddf6ab57cf694f0`。
- B：`零种子 Beta`，父目录与项目名含空格/Unicode，页面 ID `ee10ab53292bad27c265`。
- 两个页面 ID 不同；Run B 来源声明和文件操作日志显示重新生成，未复制 Run A。
- 两个 Run 均有目录外的 R1 空目录证据，首开前均有 Git checkpoint、manifest 和全量离线验证。
- 未使用 `V0/seed/**`、V0 正式项目或另一 Run 项目作为工程来源。

## 5. 日志、异常与体积

| 项目 | Run A | Run B |
| --- | --- | --- |
| Event 数 | 5：1 Blocking / 3 Non-blocking / 1 Informational | 9：0 Blocking / 8 Non-blocking / 1 Informational |
| MCP log 操作 | 8；mutation=true 为 0 | 10；mutation=true 为 0 |
| Run 文件/总 bytes | 38 / 446249 | 38 / 444058 |
| 最大文件 | 349730 bytes | 350891 bytes |

所有单文件均低于 10 MB，单 Run 均低于 50 MB。Human、MCP 与 Codex 文件操作分别记录；R7 的文件修改另写入 `CODEX_FILE_ACTIONS.jsonl`。

## 6. R-VLD-003 复核

- A/B 都执行核心往返和一次 Playbook-only 额外往返，Conformity 为 `Yes`。
- 额外往返共 2 次 Desktop 启动、4 个主要证据文件、10411 bytes。
- 新发现、捕获问题和避免错误结论均为 0。
- Human 只报告“约几秒”；机器检查约 2.38 分钟，但两个 Run 的测量口径有限且不完全相同。
- Utility：`Low positive marginal value`；V1 建议 `Change` 为风险触发/抽样，不在本项目修改 Playbook。

## 7. R7 Gate

- 至少两组有效、独立 Run：Passed。
- A/B 生成规则与验收口径一致：Passed。
- 冲突结果：无。
- Blocking 事件：已在依赖步骤前关闭并全量重验；无未关闭 Blocking。
- 关键证据缺失：无；存在两个明确的 Non-blocking evidence limitations（公共 Schema `$schema`、时间计量精度）。
- 五维最终判定、Handoff、Decision/Deviation、Feedback：已形成。

R7 结论：`Passed — 完全零种子`。
