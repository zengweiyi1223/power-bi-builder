# V1 Zero Seed — Run 20260922-032410-b 验证记录

- 状态：`In Progress — R4 Passed with known evidence gap；等待 HG-03`
- Playbook 基线：`3ee871d618db84d55b3b2f86a198ac552864317e`
- 需求冻结提交：`82b448957ab08a5452df297a7a95d7b6def67bef`
- Run 起点：`21af7b278d9be6c40ca7315fb0dd5298e3565506`
- 项目：`零种子 Beta` @ `E:\AIWorkspace\01_Projects\power-bi-builder\V1-zero-seed\runs\20260922-032410-b\project path\零种子 Beta`

## 1. 环境与安全边界

- Desktop：`2.157.1354.0` x64，独立重新查询成功。
- Modeling MCP：固定安装标识 `0.5.0-beta.13`；`Help` 与 `ListConnections` 成功；活动连接 0。
- `PBIDesktop` / `msmdsrv`：0。
- Git：目标分支、Run A final checkpoint 和 clean worktree 均已核对。
- 冻结边界：V0 与 `playbook/**` 相对规划冻结 tree 无变化。
- 禁止来源：V0 seed/run project 与 Run A project 均不读取、不复制。

## 2. Execute–Verify 阶段

| 阶段 | 状态 | 原子 Execute | 立即 Verify | Gate 判定 | 证据 | Checkpoint |
| --- | --- | --- | --- | --- | --- | --- |
| R0 Run/Preflight | Passed | 创建唯一 Run 身份并重新探测 Git、Desktop、MCP、进程和权限 | 分支/HEAD/clean；Desktop 版本；MCP 两次只读调用；进程 0；冻结树无变化 | Passed | `evidence/checks/R0_PREFLIGHT.md`；分离日志 | 待 R1 合并形成 Run/R1 checkpoint |
| R1 空目录 | Passed | 创建精确 Unicode+空格目标目录 | 递归文件数=0、子目录数=0；证据位于目录外；进程 0 | Passed | `evidence/checks/R1_EMPTY_BASELINE.md` | 与 R0 合并形成 Run/R1 checkpoint |
| R2a PBIP 入口 | Passed | 生成唯一根 `零种子 Beta.pbip` | JSON、完整公开 Schema、版本、唯一 report path、Unicode/空格与目录边界 | Passed | `evidence/checks/R2A_PBIP.md` | 预打开 checkpoint 待 R2d |
| R2b SemanticModel | Passed | 仅生成 PBISM 与最小 TMDL 根文件 | PBISM 完整 Schema；TMDL 最小子集、UTF-8/LF、Unicode 引号标识符、身份和目录边界 | Passed | `evidence/checks/R2B_SEMANTIC_MODEL.md` | 预打开 checkpoint 待 R2d |
| R2c Report/PBIR | Passed | 仅生成 PBIR 根、Report 根、版本、页面索引和唯一空页面 | 五个完整 Schema；Unicode `byPath`、页面索引、新 ID、文件数与目录边界 | Passed | `evidence/checks/R2C_REPORT_PBIR.md` | 预打开 checkpoint 待 R2d |
| R2d 预打开冻结 | Passed | 生成 9 文件完整 manifest 并冻结首开入口 | 独立复算 SHA/大小；7 Schema、TMDL、引用、页面 ID、污染、进程、日志、Git 和冻结树检查 | Passed | `manifests/PRE_OPEN.json`；`evidence/checks/R2D_PRE_OPEN_FREEZE.md` | 包含本记录的预打开 checkpoint |
| R3 首开 | Passed | Human 仅打开冻结入口，禁止保存/另存为/修复 | UI/标题/页面正确；无提示；9 文件/1503 bytes；相对 pre-open 0/0/0 | Passed | `evidence/checks/R3_FIRST_OPEN.md`；截图；`POST_OPEN_NO_SAVE.json` | pre-open `6d0a594` |
| R4 首存 | Passed with known evidence gap | Human 显式保存并正常关闭 | 进程 0；15 文件；6 新增/9 改写/0 删除；JSON/Schema/TMDL/身份/引用和差异分类 | Passed | `evidence/checks/R4_POST_SAVE.md`；`POST_SAVE_CLOSED.json` | 包含本记录的首存 checkpoint |
| R5 第一次重开 | Waiting HG-03 | Human 从同一路径重开；禁止保存/修改 | 等待 UI、磁盘稳定性与只读 MCP | Pending | `logs/HUMAN_ACTIONS.md` |  |
| R6 | Not Started |  |  |  |  |  |

## 3. Human Gate

| ID | 请求与目标 | Human 实际确认 | 状态 |
| --- | --- | --- | --- |
| HG-00 | 授权正式 V1-zero-seed，并在 Run A 后继续不同名称/路径的重复验证 | 用户已授权；Run A 结束后按请求关闭 Desktop 且无提示 | Passed for formal V1 scope |
| HG-01 | 首次打开精确 Unicode+空格路径 `.pbip`；不保存、不另存为、不创建项目、不接受修复 | 成功进入；`Overview`/标题正确；无提示、错误或修复 | Passed |
| HG-02 | 显式保存当前项目并正常关闭；不另存为、不修改内容、不接受修复 | 保存成功；Desktop 已关闭；无提示或错误 | Passed |
| HG-03 | 从同一路径第一次重开；不保存、不修改、不接受修复 | 等待 Human | Pending |
| HG-04–HG-05 | 后续 Desktop 阶段 | 尚未请求 | Not Started |

## 4. 异常与恢复

| 事件 | 类型 | 严重度 | V1 主因 | 影响 | 处理 |
| --- | --- | --- | --- | --- | --- |
| EVT-B001 | Safety/Permission Blocker | Non-blocking | ENV | 受限 token 未返回 Store Appx 包 | 只读提升权限后重新查询成功；未启动或修改 Desktop |
| EVT-B002 | Environment Failure | Non-blocking | ENV | 受限网络阻止首次公开 Schema 获取 | R2b 未开始；只读网络权限下重跑同一验证并通过 |
| EVT-B003 | Validation Failure | Non-blocking | ENV | pre-commit 脚本分词错误及含空格路径引号导致两次工具侧失败/假阳性 | 每次均停止检查链；改用路径安全的范围枚举后从头重跑；项目未变化 |
| EVT-B004 | Validation Failure | Non-blocking | ENV | R3 checkpoint 脚本的 `-eq` 分词错误导致进程断言未执行 | 停止提交；修正后从头重跑全部 R3 检查并通过；项目与会话未变化 |
| EVT-B005 | Validation Failure | Non-blocking | ENV | R4 脚本未归一化 CRLF 且 `throw` 分词错误 | 停止检查；修正后从头全量重跑并通过；项目未变化 |
| EVT-B006 | Evidence Gap | Non-blocking | SPEC | Desktop 移除三个根文件 required `$schema` | 保留原样；内存恢复元数据后其余结构通过；R5 产品证据待补 |
| EVT-B007 | Expected Negative Result | Informational | DESKTOP | 首存新增 6、改写 9、删除 0 | 全量分类；Unicode 身份/引用保留；继续 R5 |

## 5. 当前判定

- 功能结果：`Not Started`
- Contract 符合度：R0–R4 符合
- 证据完整度：R0–R4 完整；`EVT-B006` 为已知非阻塞规范证据缺口
- 持久化状态：首次显式保存成功；等待第一次重开
- 首开入口：`E:\AIWorkspace\01_Projects\power-bi-builder\V1-zero-seed\runs\20260922-032410-b\project path\零种子 Beta\零种子 Beta.pbip`
- 当前 Blocking：0
- 不能声称：任何 Run B Desktop 或跨 Run 结论
