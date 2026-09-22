# R3 First Open — Run 20260922-012919-a

验证完成时间：`2026-09-22T02:21:09.6358367-07:00`

## Human 观察

Human 按 HG-01 打开预先指定的 `ZeroSeedAlpha.pbip`，未保存、未另存为、未创建项目、未执行修复操作。

- 成功进入报表界面。
- 唯一页面 `Overview` 可见，页面为空白。
- 没有弹窗、警告或错误。
- 窗口标题显示 `ZeroSeedAlpha`；截图中完整可见标题为 `ZeroSeedAlpha • 上次保存于: 01:40 的今天 (Power BI 项目)`。
- 截图：`evidence/screenshots/HG01_FIRST_OPEN.png`
- 截图字节数：`349730`
- 截图 SHA-256：`CCE12ACA53C5E5F68938B283F565F304C5E85029B70CA6D712D534AFE3F6357B`

截图未显示账号、令牌、凭据或组织信息；右上角仅显示通用“登录”入口。

## 首开后无保存 manifest

- 文件：`manifests/POST_OPEN_NO_SAVE.json`
- SHA-256：`9374C22CD2FBEB3CB576491AFB9C0292D3CE202B94168A74E81729C20F701713`
- 采集时项目文件数：`9`
- 采集时项目总字节数：`1498`
- 枚举使用 `-Force -Recurse`，覆盖隐藏文件和目录。

独立比较 `PRE_OPEN.json` 与 `POST_OPEN_NO_SAVE.json`：

- Added：`0`
- Modified：`0`
- Deleted：`0`
- 隐藏或缓存文件：`0`

因此首开阶段没有观测到任何磁盘首次补写、结构修复或语义改写。该结论仅限项目目录磁盘状态；不声称 Desktop 未在进程内初始化运行时状态，也不覆盖后续显式保存可能产生的补写。

## 运行身份

- `PBIDesktop`：PID `29184`，启动时间 `2026-09-22T02:17:03.1125918-07:00`
- `msmdsrv`：PID `28476`，启动时间 `2026-09-22T02:17:04.6478755-07:00`
- Desktop 在采集时保持打开。
- Modeling MCP：未连接、未调用。

## 判定

- UI 产品解析：`Passed`
- 项目身份：`Passed`
- 首开磁盘差异：`None`
- Desktop 首次补写分类：当前为“首开无磁盘补写”；最终三级结论仍须经过显式保存、关闭和重开。

R3 Gate：`Passed`。可以请求 HG-02；在 Human 明确执行 HG-02 前仍禁止保存或关闭。
