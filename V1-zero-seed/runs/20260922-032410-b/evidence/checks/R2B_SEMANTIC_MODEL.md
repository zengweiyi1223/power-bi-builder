# R2b SemanticModel — Run 20260922-032410-b

验证时间：`2026-09-22T06:44:21.9571643-07:00`

## Execute

仅新增：

- `零种子 Beta.SemanticModel/definition.pbism`
- `零种子 Beta.SemanticModel/definition/database.tmdl`
- `零种子 Beta.SemanticModel/definition/model.tmdl`

未生成 Report，未启动 Desktop，未读取或复制 V0/Run A 工程文件。数据库标识符因含空格而按 TMDL 规则使用单引号。

## 公开依据

- SemanticModel folder：`https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset`
- TMDL：`https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview`
- PBISM Schema：`https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json`
- Schema SHA-256：`4BA062788EA423978642BFEEAD3F9FB6385A3598FE50331C99ED03EC3A80E0FC`

## 立即 Verify

- `definition.pbism`：JSON 与完整公开 Draft 7 Schema Passed
- `database.tmdl`：根 `database '零种子 Beta'`；`compatibilityLevel: 1600`
- `model.tmdl`：`model Model`、`culture: en-US`、`defaultPowerBIDataSourceVersion: powerBI_V3`
- TMDL：严格 UTF-8、无 BOM、LF-only；冻结最小子集解析 Passed
- Report 目录：不存在
- 项目递归文件数：`4`
- Desktop / 模型进程：`0`

## 哈希

- `definition.pbism`：`CC3D122D38A9D92D4389DC68ADEA2588A351698913860FC826A28B7EB9D2709A`
- `database.tmdl`：`64B5045974576510EC6575E32C469A73EF57E9CA4CAA08203C6927427FABB859`
- `model.tmdl`：`9943A73BBFAE86F12B75207AD34B064FB66E6169EE6933825E359F2958BF0821`

相同的最小模型固定属性可能产生与另一 Run 相同的内容哈希；Run B 的文件由公开规范和冻结规则独立生成，未从其他 Run 复制。

R2b Gate：`Passed`。
