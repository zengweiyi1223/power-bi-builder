# R2b SemanticModel — Run 20260922-012919-a

首次验证时间：`2026-09-22T01:49:32.2038658-07:00`  
修正后复验时间：`2026-09-22T01:55:00-07:00`

## Execute

仅在本 Run 的空目录项目内新增：

- `ZeroSeedAlpha.SemanticModel/definition.pbism`
- `ZeroSeedAlpha.SemanticModel/definition/database.tmdl`
- `ZeroSeedAlpha.SemanticModel/definition/model.tmdl`

未生成 Report，未启动 Power BI Desktop，未连接 Modeling MCP，未读取或复制任何既有工程文件。

## 公开依据

- SemanticModel folder：Microsoft Learn `https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset`
- TMDL 根文件与语法：Microsoft Learn `https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview`
- Tabular compatibility level：Microsoft Learn `https://learn.microsoft.com/en-us/analysis-services/tabular-models/compatibility-level-for-tabular-models-in-analysis-services`
- Power BI 增强模型元数据：Microsoft Learn `https://learn.microsoft.com/en-us/fabric/cicd/troubleshoot-cicd`；模型须使用 `defaultPowerBIDataSourceVersion: powerBI_V3`。
- `definition.pbism` Schema：`https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json`
  - 获取时间：`2026-09-22T01:48:20.3725500-07:00`
  - Schema SHA-256：`4BA062788EA423978642BFEEAD3F9FB6385A3598FE50331C99ED03EC3A80E0FC`

## 立即 Verify

- `definition.pbism`：JSON 可解析，并通过下载后离线执行的完整 Draft 7 Schema 验证。
- TMDL：由与生成动作分离的确定性解析器读取两个文档，确认根声明、缩进、属性 token、无重复属性、必需属性和值。
- 编码：两个 TMDL 文件均为严格 UTF-8、无 BOM；内容只使用 LF 换行。
- 身份：`database ZeroSeedAlpha`、`model Model`、`compatibilityLevel: 1600`、`culture: en-US`、`defaultPowerBIDataSourceVersion: powerBI_V3`。
- 结构：`definition/` 仅含 `database.tmdl` 与 `model.tmdl`；此阶段整个项目恰有 4 个文件，全部解析在精确 Run 项目根内。
- `git diff --check`：通过。

首次最小解析通过后，R2c 的公开资料复核发现缺少 Power BI 增强模型元数据版本。该发现记为 `EVT-002`（Blocking / `GEN`），立即停止 R2c；在未生成 Report 且状态可信的条件下原地补入该属性并复验通过。第一次文件哈希和修正链保留在 Codex 文件日志中。

解析证明等级：对本 Contract 冻结的最小 TMDL 子集为精确语法/结构检查；它不是完整 TOM 语义验证。后续 Desktop 首开将提供产品解析器证据，不能倒推替代本阶段检查。

## 哈希

- `definition.pbism`：`CC3D122D38A9D92D4389DC68ADEA2588A351698913860FC826A28B7EB9D2709A`
- `database.tmdl`：`51586A1B77AA7EA9DA099B1E4D5249BFF392CCBD94DC01A18420BA08B8A1AB9E`
- `model.tmdl` 首次：`4FB4784A2952F59DA62329BECF93EBDD903A2543843CCB37549A8560ED53B011`
- `model.tmdl` 修正后：`9943A73BBFAE86F12B75207AD34B064FB66E6169EE6933825E359F2958BF0821`

R2b Gate：`Passed after one in-stage retry`。
