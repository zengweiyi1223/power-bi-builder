# V1 Zero Seed — 基线与历史对照

## 1. Git 与 Playbook 基线

- 仓库基线：`78a20f0179b9deb5c3cdaa5e1fc64f502a78ec7b`（`docs: consolidate V0 handoff and tutorial`）。
- V1 分支：`codex/v1-zero-seed`。
- V1 非规范预备草案：`22da780412f27decf17a097548d65d151c75b235`。
- Playbook v0.1 固定提交：`3ee871d618db84d55b3b2f86a198ac552864317e`。
- no-ff merge 提交：`8c28f5e340ec41ef56e16d942fd2f9eb97767963`。
- V1 规划冻结：包含本轮符合性检查的提交；其 SHA 由 Git 和本轮报告记录，文档不回写自身哈希。

合并后 `3ee871d` 是 V1 HEAD 的真实祖先。实验期间 `playbook/**` 只读；任何建议进入 `PLAYBOOK_FEEDBACK.md`，由 Maintainer 决定是否用于 v0.2。

## 2. 状态检查

接入前已确认：

- 当前分支为 `codex/v1-zero-seed`；
- HEAD 精确为 `22da780`；
- 工作树干净；
- `codex/playbook-v0.1` 的独立 worktree 精确指向 `3ee871d`；
- 未覆盖或重写任何既有 V1 提交。

规划冻结阶段未启动 Desktop、未连接 Modeling MCP、未创建正式 Run。

## 3. 已阅读资料

- `README.md`
- `V0/HANDOFF.md`
- `V0/REQUIREMENTS.md`
- `V0/runs/20260917-003433/VALIDATION.md`
- `playbook/README.md`
- `playbook/PLAYBOOK.md`
- `playbook/templates/*`
- `playbook/adapters/power-bi.md`
- 与 V0 执行链路和以上文件相关的 Git 历史

未读取或复制 `V0/seed/` 的文件内容，也未读取 V0 正式运行目录中的 PBIP/PBIR/TMDL 项目内容。

## 4. V0 历史提供的对照

| 提交 | V0 证据 | 对 V1 的用途 |
| --- | --- | --- |
| `f2aa331` | 冻结 V0 执行与验收基线 | 保留职责分离、阶段闸门和失败即停止纪律。 |
| `c5f43c1` | 人工空白种子进入版本库 | 仅证明 V0 使用过种子；不读取其内容，不作为 V1 起点。 |
| `b01d551` | Desktop 将 MCP 模型持久化到 TMDL | 要求区分首次打开前文件与 Desktop 保存后文件。 |
| `c0cbb92` | Codex 生成并离线校验 PBIR | 证明报表文件可生成，但未回答完整工程壳能否零种子生成。 |
| `c7a4579` | Desktop 保存后重排 PBIR 并升级部分 Schema | 要求做字节、结构和语义三层 diff。 |
| `2db7009` | Desktop 保存重开与 MCP 最终回读通过 | 提供持久化闸门的最低证据形态。 |
| `fc79816` | 首次提出零种子实验与三级结论 | 形成 V1 原始范围。 |

## 5. Trusted baseline 与污染控制

每个 Run 的 Trusted baseline 是一项被记录和验证的空目录状态，不是 V0 种子、V0 项目或 Desktop 生成的空壳。

允许来源：冻结的 V1 Contract、固定 Playbook 与 Power BI adapter、微软公开 PBIP/PBIR/TMDL 文档和 Schema、V0 文档中已记录的事实、允许的验证脚本。实际使用项必须进入 Run 来源清单。

禁止来源：

- `V0/seed/**`
- `V0/runs/**/project/**`
- 任何从上述路径导出、改名或缓存的工程壳
- A/B 试验之间复制或改名得到的工程文件

如误读或复制禁止来源，该 Run 记录为 `Governance Failure` + `PROVENANCE` + `Blocking`，不得用于业务结论；必须保留现场并新建 Run。
