# R0 Preflight — Run 20260922-012919-a

检查时间：`2026-09-22T01:29:19-07:00`

## Git 与治理

- 分支：`codex/v1-zero-seed`
- HEAD / Run 起点：`82b448957ab08a5452df297a7a95d7b6def67bef`
- 工作树：检查时干净
- Playbook 固定基线：`3ee871d618db84d55b3b2f86a198ac552864317e`，tree 与 V1 HEAD 中的 `playbook/**` 一致
- V0：tree 与冻结仓库基线 `78a20f0` 一致
- HG-00：用户明确确认并授权

## 环境

- Power BI Desktop Appx：`Microsoft.MicrosoftPowerBIDesktop` `2.157.1354.0` x64
- 安装类型：Microsoft Store Appx
- Modeling MCP 安装版本：`0.5.0-beta.13`
- MCP 可执行文件产品版本：`0.5.0-beta.13`
- MCP 可执行文件版本：`0.5.0.0`
- MCP SHA-256：`8B5434688C0A5CBBE94928F0099F24C91886393A888AC35DCCED349B2F5A30F7`
- `PBIDesktop` / `msmdsrv` 进程：0

## 权限事件

首次受限 shell 无法枚举 Store 包/本机 MCP 安装目录。按 R-PFL-001 停止依赖步骤后，使用只读提升权限重新探测并成功。该事件为 `EVT-001`，未启动任何程序、未修改本机安装、未切换路线。

R0 Gate：`Passed`。
