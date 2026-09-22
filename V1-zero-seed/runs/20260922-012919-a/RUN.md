# V1 Zero Seed — Run 20260922-012919-a

## 1. Run 身份

- Run ID：`20260922-012919-a`
- Attempt：`1`
- 试验组：`A`
- 项目名：`ZeroSeedAlpha`
- 项目绝对路径：`E:\AIWorkspace\01_Projects\power-bi-builder\V1-zero-seed\runs\20260922-012919-a\project\ZeroSeedAlpha`
- Playbook 基线：`3ee871d618db84d55b3b2f86a198ac552864317e`
- 需求冻结提交：`82b448957ab08a5452df297a7a95d7b6def67bef`
- Run 起点：需求冻结 `82b448957ab08a5452df297a7a95d7b6def67bef`；Run/R1 checkpoint `473ff1e1e83cbb21458186468ad853d244ded562`
- 生成规则版本：冻结的 `REQUIREMENTS.md` 与 `EXPERIMENT_PLAN.md` @ `82b4489`
- 开始时间：`2026-09-22T01:29:19-07:00`
- Experiment Owner：Codex
- Human Approver：用户

## 2. 环境、权限与安全

- Power BI Desktop：Microsoft Store `Microsoft.MicrosoftPowerBIDesktop` `2.157.1354.0`，x64。
- Modeling MCP：`0.5.0-beta.13`；服务端文件版本 `0.5.0.0`；可执行文件 SHA-256 `8B5434688C0A5CBBE94928F0099F24C91886393A888AC35DCCED349B2F5A30F7`。
- 操作系统/路径：Windows；本试验为仓库内 ASCII 短路径。
- 进程预检：`PBIDesktop` 与 `msmdsrv` 均未运行。
- 外部访问：仅允许微软公开 PBIP/PBIR/TMDL 文档和 Schema 的只读访问。
- 权限：版本目录只读探测需提升权限；已通过只读授权完成，未启动程序。
- 敏感信息：不读取账号、令牌、凭据或 PII；内部记录保留目标绝对路径用于身份核对。
- 初始 Git：`codex/v1-zero-seed` @ `82b448957ab08a5452df297a7a95d7b6def67bef`，工作树干净。

## 3. 来源声明

- 已使用：V1 冻结 Contract、Playbook v0.1、Power BI adapter、V0 文档与 Git 历史中已记录的事实。
- 微软公开文档/Schema：已使用 PBIP overview、Report/SemanticModel folder、TMDL overview 与微软 `json-schemas`；每个实际 Schema 的 URL、获取时间和哈希写入对应 R2 证据。
- `V0/seed/**`：未读取、未复制。
- `V0/runs/**/project/**`：未作为实现参考。
- 其他 Run 工程文件：不存在，未复制。
- 来源例外：无。

## 4. Trusted baseline：空目录证明

- 精确目标：`project/ZeroSeedAlpha/`
- 创建/检查时间：`2026-09-22T01:30:54.6065818-07:00`
- 递归文件数：`0`
- 递归子目录数：`0`
- 证据：`evidence/checks/R1_EMPTY_BASELINE.md`
- Gate：`Passed`

## 5. 当前阶段

| 阶段 | 状态 | 证据 / checkpoint |
| --- | --- | --- |
| R0 Run/Preflight | Passed | `evidence/checks/R0_PREFLIGHT.md` |
| R1 空目录 | Passed | `evidence/checks/R1_EMPTY_BASELINE.md` |
| R2a PBIP 入口 | Passed | `evidence/checks/R2A_PBIP.md` |
| R2b SemanticModel | Passed | `evidence/checks/R2B_SEMANTIC_MODEL.md` |
| R2c Report/PBIR | Passed | `evidence/checks/R2C_REPORT_PBIR.md` |
| R2d 预打开冻结 | Passed | `manifests/PRE_OPEN.json`；`evidence/checks/R2D_PRE_OPEN_FREEZE.md`；checkpoint 为包含两者的提交 |
| R3 首开 | Passed | `manifests/POST_OPEN_NO_SAVE.json`；`evidence/checks/R3_FIRST_OPEN.md`；首开磁盘差异为 0 |
| R4 首存/关闭 | Passed with known evidence gap | `manifests/POST_SAVE_CLOSED.json`；`evidence/checks/R4_POST_SAVE.md` |
| R5 第一次重开/只读回读 | Passed | `manifests/POST_REOPEN_NO_SAVE.json`；`evidence/checks/R5_FIRST_REOPEN.md`；`logs/MCP_ACTIONS.jsonl` |
| R6 Playbook-only 最终往返 | Not Started | 等待 HG-04 |

## 6. 分离式日志

- Human：`logs/HUMAN_ACTIONS.md`
- MCP：尚未连接；首次实际调用时创建 `logs/MCP_ACTIONS.jsonl`
- Codex 文件操作：`logs/CODEX_FILE_ACTIONS.jsonl`
- 异常：`logs/EVENTS.jsonl`
- R-VLD-003：R5 前创建 `logs/R-VLD-003-METRICS.json`

## 7. 当前结论

- 功能结果：`Not Started`
- Contract 符合度：R0–R5 符合；后续未评价
- 证据完整度：R0–R5 证据齐全；保留 `EVT-003` 非阻塞 Schema/Product 缺口
- 持久化/重启状态：核心首开—保存—关闭—第一次重开通过
- 安全与权限：只读版本探测的权限事件已解决，无凭据或外部发布
- 不能声称：`.platform` 对后续重开的反事实必要性、Run B 重复性、R-VLD-003 utility 或 V1 最终结论
