# R2a PBIP Entry — Run 20260922-032410-b

- 生成/复验时间：`2026-09-22T06:41:14.8825960-07:00`
- 文件：`project path/零种子 Beta/零种子 Beta.pbip`
- 文件 SHA-256：`4769DE97405C40B1B618A0252A37F78110DE4D2400CC1C02C640400703890E7C`
- 声明 Schema：`https://developer.microsoft.com/json-schemas/fabric/pbip/pbipProperties/1.0.0/schema.json`
- Schema SHA-256：`AF66CD9850F8F99373C4EBC991E3C1612E74AEBDCDC67A9F564D6122C313250D`
- 验证器：Python `jsonschema`，Draft 7

## Execute

仅从 R1 空目录生成唯一根 `.pbip`。未生成 SemanticModel/Report，未启动 Desktop，未读取或复制 Run A/V0 工程文件。

## 立即 Verify

- 严格 UTF-8 JSON 解析：Passed
- 完整公开 Schema：Passed
- `version`：`1.0`
- artifacts：唯一 report 引用
- report path：`零种子 Beta.Report`
- 路径使用正斜杠语义的相对引用，解析后仍在本 Run 项目根内
- 项目递归文件数：`1`
- Desktop / 模型进程：`0`

首次联机 Schema 获取被受限网络阻止；未进入 R2b。使用只读网络权限重跑同一验证后通过，记录为 `EVT-B002`。

R2a Gate：`Passed`。
