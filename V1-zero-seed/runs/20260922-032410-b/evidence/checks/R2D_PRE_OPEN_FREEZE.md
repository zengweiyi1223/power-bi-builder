# R2d Pre-open Freeze — Run 20260922-032410-b

验证时间：`2026-09-22T06:53:50.3167355-07:00`

## 冻结对象

- 项目：`零种子 Beta`
- 绝对路径：`E:\AIWorkspace\01_Projects\power-bi-builder\V1-zero-seed\runs\20260922-032410-b\project path\零种子 Beta`
- Manifest：`manifests/PRE_OPEN.json`
- Manifest SHA-256：`71CD48D6D56062EFB0C586F6E68BA8BA3583392683E32631E703259DA740D8A4`
- 项目文件数：`9`
- 项目总字节数：`1503`

## 独立全量复验

- Manifest 与磁盘逐文件路径、字节数、SHA-256：added `0`、modified `0`、deleted `0`
- 7 个 JSON/入口文件：解析与声明的完整公开 Schema 全部 Passed
- TMDL：冻结最小子集、Unicode 引号标识符、必需属性、UTF-8/no-BOM/LF 全部 Passed
- PBIP → Report 与 PBIR → SemanticModel：解析后精确指向本 Run，未越出项目根
- 页面：独立派生 ID `ee10ab53292bad27c265`；唯一 `Overview`；索引与活动页一致
- 污染扫描：无 `ZeroSeedAlpha`、Run A ID、`.pbi`、visuals 或资源目录
- Desktop / 模型进程：`0`
- `git diff --check`：Passed
- V0 与 `playbook/**`：相对规划冻结 tree 无变化
- Run A：相对 final checkpoint 无变化

## 来源与边界

- 未读取或复制 `V0/seed/**`、V0 run project 或 Run A project。
- 项目文件全部在 Run B 的 R2a/R2b/R2c 原子步骤中由公开规范与冻结 Contract 独立生成。
- 未启动 Power BI Desktop，未建立模型连接，未执行 MCP mutation。

R2d Gate：`Passed`。只有包含本证据、manifest 和完整项目的 Git checkpoint 形成后，才可请求 HG-01。
