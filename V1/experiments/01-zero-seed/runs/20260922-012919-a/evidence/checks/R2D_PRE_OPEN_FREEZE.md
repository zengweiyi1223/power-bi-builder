# R2d Pre-open Freeze — Run 20260922-012919-a

验证完成时间：`2026-09-22T02:01:53.8318043-07:00`

## 冻结对象

- Run：`20260922-012919-a`
- 项目：`ZeroSeedAlpha`
- 精确入口：`E:\AIWorkspace\01_Projects\power-bi-builder\V1-zero-seed\runs\20260922-012919-a\project\ZeroSeedAlpha\ZeroSeedAlpha.pbip`
- Run 起点 checkpoint：`473ff1e1e83cbb21458186468ad853d244ded562`
- 需求冻结：`82b448957ab08a5452df297a7a95d7b6def67bef`
- 预打开 checkpoint：包含本证据、`PRE_OPEN.json` 和完整项目的 Git 提交；SHA 由 Git 与 HG-01 报告记录。

## Manifest

- 文件：`manifests/PRE_OPEN.json`
- Manifest SHA-256：`7595073CD6685E681403063DB64E22018FC0E6E5E26377DF54D9E20857A06C46`
- 项目文件数：`9`
- 项目总字节数：`1498`
- 单文件上限：全部小于 `10 MB`
- 独立复算：逐文件路径、大小和 SHA-256 与磁盘完全一致；无缺失、额外文件或目录逃逸。

## 全量不变量复验

- 7 个 JSON：全部再次通过各自下载的微软公开 Draft 7 Schema。
- 2 个 TMDL：再次通过分离的最小 TMDL 解析器；严格 UTF-8 无 BOM；数据库、模型、兼容级别、文化和 `powerBI_V3` 身份一致。
- PBIP：唯一入口指向本 Run Report。
- PBIR：`byPath` 精确指向本 Run SemanticModel，未越出项目根。
- 页面：唯一 `Overview`，ID、目录、`pageOrder` 和 `activePageName` 一致。
- 来源：项目无 `.platform`、主题资源、缓存或其他模板性文件；只包含公开规范允许的最小生成物。
- 治理：`playbook/**` 相对固定提交无变化；`V0/**` 相对冻结 tree 无变化；当前正式变化仅为 Run A 与 V1 汇总状态。
- 日志：Human、Codex 文件、事件日志分离；两份 JSONL 均逐行可解析；MCP 尚未连接。
- Desktop：`PBIDesktop` 与 `msmdsrv` 进程均为 `0`。
- `git diff --check`：通过。

## Gate

R2d Gate：`Passed`。项目首次进入可以请求 `HG-01` 的状态；在 Human 明确报告首开结果前，禁止保存、另存为、创建项目或连接 MCP。
