# 用 Codex 生成可直接打开的 Power BI 项目

副标题：Power BI Modeling MCP + PBIP/PBIR 完整实战。

## 1. 教程结论

Codex 可以把自然语言报表需求转成 Power Query/M、语义模型、关系、DAX 和 PBIR 页面，并交付可由 Power BI Desktop 打开的 PBIP 项目。当前稳定流程仍需要人工完成少量 Desktop 操作：首次创建标准种子，以及每次项目中的打开、保存、关闭、重开和业务确认。

## 2. 三个容易混淆的路径

1. MCP 安装目录：存放 `powerbi-modeling-mcp.exe` 的稳定工具目录。
2. PBIP 项目目录：每个报表的 `.pbip`、`.Report/` 和 `.SemanticModel/`。
3. 数据源路径：CSV、Excel 或其他数据文件的位置，由 Power Query/M 引用。

三者互相独立。MCP 不需要放在 PBIP 项目中。Codex 通过配置中记录的可执行文件路径启动 MCP；MCP 再连接当前打开的 Desktop 模型。

本次实测安装位置：

```text
%LOCALAPPDATA%\Programs\PowerBIModelingMCP\0.5.0-beta.13\
└─ dist\powerbi-modeling-mcp.exe
```

只要该目录不移动、Codex 的 MCP 注册仍存在，后续项目不需要重新下载。移动或删除 MCP 后必须更新配置。新增或修改 MCP 配置后，应重启 Codex。

## 3. 一次性配置

### 3.1 Power BI Desktop

1. 安装或更新 Power BI Desktop。
2. 在“文件 → 选项和设置 → 选项 → 预览功能”中勾选 Power BI Project `.pbip` 保存功能。
3. 勾选“使用增强的元数据格式存储报表（PBIR）”。
4. 重启 Power BI Desktop，使预览功能生效。
5. 在“全局 → 数据加载 → 时间智能”中取消“新文件的自动日期/时间”。这是防止以后新文件再次自动生成隐藏日期表的推荐设置。
6. 在标准种子的“当前文件 → 数据加载 → 时间智能”中取消当前文件的 Auto date/time。这是种子的必要设置。

### 3.2 安装固定版本 Modeling MCP

本教程的实测版本为微软官方 Windows x64 包 `@microsoft/powerbi-modeling-mcp-win32-x64@0.5.0-beta.13`。为了可重复，使用版本化工具目录，不把 MCP 二进制提交进项目 Git。

可复现的手动方法：

1. 安装 Node.js 18 或更高版本。
2. 从微软官方 npm 包获取固定版本。
3. 将包中的内容解压到稳定目录，例如 `%LOCALAPPDATA%\Programs\PowerBIModelingMCP\0.5.0-beta.13\`。
4. 确认可执行文件位于 `dist\powerbi-modeling-mcp.exe`。
5. 对不同版本先运行 `powerbi-modeling-mcp.exe --help`，不要照搬其他版本的参数。

### 3.3 注册到 Codex

推荐使用 Codex 设置界面：

1. 打开“设置 → MCP 服务器 → 添加服务器”。
2. 名称填 `powerbi-modeling-mcp`。
3. 类型选择 STDIO。
4. 命令填写 MCP exe 的绝对路径。
5. 本次锁定版本的参数为 `--start`、`--require-confirmation`。
6. 保存后重启 Codex。
7. 在新任务中确认 MCP 服务和 Power BI Modeling 工具可见。

对应的 `config.toml` 结构示例：

```toml
[mcp_servers.powerbi-modeling-mcp]
command = "C:\\Users\\<用户名>\\AppData\\Local\\Programs\\PowerBIModelingMCP\\0.5.0-beta.13\\dist\\powerbi-modeling-mcp.exe"
args = ["--start", "--require-confirmation"]
```

保留首次写操作和查询确认更适合教程与试验环境。不要在缺少备份和权限边界时启用自动跳过确认。

## 4. 一次性创建标准种子

1. 新建空白 Power BI Desktop 文件。
2. 确认 PBIR 与当前文件 Auto date/time 设置。
3. 将唯一空白页面命名为 `Overview`。
4. 不加载业务数据，不创建业务表、关系、度量值或视觉对象。
5. 使用“另存为”，类型选择 Power BI 项目文件 `.pbip`。
6. 保存后关闭 Desktop。
7. 将 `.pbip`、同级 `.Report/` 和 `.SemanticModel/` 一起纳入 Git。
8. 将种子视为只读模板；每次工作前复制，不直接修改原件。

当前版本需要人工建立种子。后续的零种子实验会单独验证 AI 能否从空目录直接生成完整工程壳，不把尚未验证的能力写成既成事实。

## 5. 每个报表的八步流程

### 01 人工提出需求与提供数据

- 业务问题、目标用户和指标口径。
- 数据文件或数据源访问方式。
- 页面、筛选和视觉偏好。
- 涉及敏感数据时明确权限和输出边界。

### 02 Codex 形成实施契约并复制种子

- 把自然语言转成表、列、粒度、关系、DAX 和页面规格。
- 建立新的运行目录。
- 从只读种子复制完整 PBIP 项目。
- 将数据路径和运行副本路径锁定到当前任务。

此阶段 Desktop 保持关闭。

### 03 人工打开运行副本

- 打开运行目录中的 `.pbip`，不要打开种子原件。
- 等待 Desktop 完全加载。
- 保持 Desktop 打开，使本地语义模型实例可被发现。
- 若 MCP 首次连接或写入要求确认，由人工确认。

### 04 Codex 通过 MCP 建立语义模型

- 连接当前打开的 Desktop 实例。
- 创建 Power Query/M 参数、命名表达式和 Import Partition。
- 创建事实表、维度表和日期表。
- 建立关系与筛选方向。
- 创建 DAX 度量值和格式字符串。
- 设置日期表、月份排序等模型属性。
- 刷新分区并运行代表性查询。

此阶段 Desktop 必须保持打开。人工不要同时在模型中做其他修改。

### 05 人工保存并关闭 Desktop

- 在 Desktop 中明确点击“保存”。
- 等待保存完成后关闭 Desktop。
- 若关闭时再次询问是否保存，选择保存。
- 这一步把运行中模型的 MCP 修改写入磁盘 TMDL。

MCP 能修改模型，但不会代替用户点击 Desktop 的保存按钮。

### 06 Codex 在 Desktop 关闭时生成 PBIR

- 修改运行副本的 PBIR `definition/`。
- 创建页面布局、卡片、图表和切片器。
- 将视觉对象绑定到模型字段和度量值。
- 设置切片器交互与位置尺寸。
- 保留 `.pbip` 入口和 `definition.pbir` 的相对引用。

Desktop 保持关闭，避免 Desktop 与外部编辑器同时重写 PBIR 文件。

### 07 人工重开、确认并保存

- 重新打开运行副本 `.pbip`。
- 处理凭据、隐私级别和系统提示。
- 确认没有阻塞错误或自动修复提示。
- 检查页面、指标、筛选和可读性。
- 点击保存，让 Desktop 写回其规范化格式。

### 08 Codex 整理交付包

- 保留 `.pbip` 项目入口。
- 保留同级 `.Report/` 和 `.SemanticModel/`。
- 附带需要的输入数据、使用说明和版本记录。
- 明确跨机器后可能需要重新绑定本地数据路径和凭据。

## 6. Desktop 打开/关闭时间线

| 阶段 | Desktop 状态 | 原因 |
| --- | --- | --- |
| 复制种子、准备运行目录 | 关闭 | 避免复制缓存或被占用文件 |
| MCP 连接、建模、刷新、DAX | 打开并保持 | MCP 连接运行中的本地模型 |
| 模型落盘 | 人工保存后关闭 | 把运行时模型持久化到 TMDL |
| PBIR 页面生成 | 关闭 | 避免并发重写报告定义 |
| 页面检查与业务确认 | 重新打开 | 让 Desktop 加载完整项目 |
| 最终规范化保存 | 打开时人工保存 | 形成 Desktop 认可的最终输出 |

## 7. AI 与人工边界

Codex 可以直接完成：需求规格、运行目录、M 数据加载、语义模型、关系、DAX、刷新、PBIR 页面、视觉绑定、交互配置和交付文件整理。

人工仍需完成：业务口径确认、数据授权、首次标准种子、Desktop 打开/保存/关闭/重开、MCP 安全确认、凭据或隐私弹窗、最终业务视觉确认，以及是否发布到 Power BI Service 的决策。

## 8. 最终交付不是一个文件

```text
YourReport/
├─ YourReport.pbip
├─ YourReport.Report/
│  ├─ definition.pbir
│  └─ definition/
└─ YourReport.SemanticModel/
   ├─ definition.pbism
   └─ definition/
```

`.pbip` 是项目入口，不包含全部模型与报告内容。移动或分享时必须保留同级 Report 与 SemanticModel 目录及其相对关系。

## 9. 常见问题

### MCP 一定要放在项目里吗？

不需要。放在项目里会让每个项目重复保存大体积工具文件，也容易误提交 Git。使用稳定的用户级工具目录更合适。

### 下一个 Power BI 项目能直接使用同一 MCP 吗？

可以。只要 exe 路径和 Codex 注册没有变化，打开新的 PBIP 后重新连接新的 Desktop 实例即可。

### 为什么 PBIR 生成时要关闭 Desktop？

因为 Desktop 和 Codex 都可能写入相同的 PBIR 文件。V0 采用先保存关闭、再离线生成、最后重开的路线，边界最清楚。

### 为什么不能只交付 `.pbip`？

因为 `.pbip` 主要是入口和目录引用，实际报告及模型分别存放在两个同级目录中。

### 是否已经实现完全无人操作？

没有。当前流程是高度自动化的人机协作链路。零种子、自动 Desktop 生命周期和 Service 发布需要独立实验。

## 10. 官方参考

- Microsoft Power BI Modeling MCP：<https://github.com/microsoft/powerbi-modeling-mcp>
- Power BI Desktop Projects：<https://learn.microsoft.com/power-bi/developer/projects/projects-overview>
- Power BI Project Report/PBIR：<https://learn.microsoft.com/power-bi/developer/projects/projects-report>
- External editing：<https://learn.microsoft.com/power-bi/developer/projects/projects-external-editing>
- Codex MCP：<https://developers.openai.com/codex/mcp>
