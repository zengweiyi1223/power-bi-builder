# R5 First Reopen and Read-only MCP — Run 20260922-032410-b

验证完成时间：`2026-09-22T08:02:38.5522526-07:00`

## Human 观察

- 从同一绝对路径成功进入报表。
- 仍显示空白 `Overview`。
- 标题仍为 `零种子 Beta`。
- 无任何提示、错误或修复信息。
- 未保存、未修改、未接受修复。

## 独立重启身份

- `PBIDesktop` PID `6096`，启动时间 `2026-09-22T07:58:08-07:00`
- `msmdsrv` PID `21644`，启动时间 `2026-09-22T07:58:10-07:00`
- 与首开 PID `26420` / `1968` 不同，证明发生了新 Desktop 与模型进程实例。

## 磁盘稳定性

- Manifest：`manifests/POST_REOPEN_NO_SAVE.json`
- 文件数：`15`
- 总字节数：`3647`
- 相对 `POST_SAVE_CLOSED.json`：Added `0`、Modified `0`、Deleted `0`
- MCP 只读回读后再次比较仍为 `0/0/0`。

## Modeling MCP 只读回读

- 本地实例：父窗口标题 `零种子 Beta`；模型 PID `21644`；端口 `61967`
- 连接：`PBIDesktop-零种子 Beta-61967`
- 连接状态：local、non-offline、无 transaction、无 trace
- 数据库：1 个 Tabular；compatibility level `1606`；language `1033`；state `Unprocessed`
- 模型：`Model`；`en-US`；Import；`PowerBI_V3`；`PBI_ProTooling=["DevMode"]`；`IsEmpty=true`
- 表：`0`
- 断开后活动连接：`0`
- 全部操作均为发现、连接、Get/List 与断开；mutation：`false`

## 判定

- 核心首开—保存—关闭—第一次重开链：`Passed`。
- Run B 当前功能候选：`完全零种子（Desktop 首次显式保存时正常规范化/补写）`。
- Unicode+空格路径未产生 PATH 失败。
- `.platform` 反事实必要性仍未测试；首开已证明它不是首次打开的必要前置文件。

R5 Gate：`Passed`。等待 R-VLD-003 的 HG-04 额外关闭—重开。
