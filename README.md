# Org & HR Skills

面向企业管理者、CHRO、战略 HRBP 和组织发展专业人士的 AI Skills。

这个仓库把组织、人才、绩效、薪酬与文化领域的方法论，沉淀为可安装、可调用、可验证的工作流。Skill 不替代管理者判断，而是帮助使用者在真实业务情境中建立证据、识别因果关系、形成结构化建议。

### `analyze-business-organization-context`

围绕目标企业研究：

- 行业环境与内外部竞争挑战；
- 战略和业务定位；
- 关键业务运作方式；
- 代表性企业的组织模式及其优劣势；
- 对目标企业组织、人才、机制和文化建设的要求。

它服务于后续组织诊断、组织设计、人才管理、绩效、薪酬、领导力和文化建设，而不是生成一份与组织工作割裂的宏观行业报告。

核心推理链为：

> 外部竞争与行业挑战 → 战略与业务定位 → 关键业务运作方式 → 组织运作模式 → 核心组织能力 → 组织与人力资源要求

#### 研究工作流

Skill 会先确认研究目标、范围和内部资料，再主动检索年报、监管披露、ESG 报告、公司官网、政府与行业资料以及可公开访问的专业研究。

默认交付包括：

1. 行业赛道整体洞察；
2. 代表性企业战略与经营比较；
3. 代表性企业组织模式比较；
4. 对目标企业的组织与人力启示；
5. 证据底稿与组织情境输入卡。

研究过程明确区分事实、计算、推断和待验证假设，不用企业公开口号直接证明组织能力已经形成，也不把不同经营模式下的人效指标直接用于裁员或组织优劣排名。

#### 使用示例

> 使用 `$analyze-business-organization-context` 研究安踏所在行业，比较 4—6 家代表性企业的战略、经营和组织模式，并形成对安踏组织与人力建设的启示。开始前先询问我是否有内部材料。

安踏正向测试：

- [比较研究报告](examples/analyze-business-organization-context/anta-comparative-forward-test.md)
- [研究证据底稿](examples/analyze-business-organization-context/anta-comparative-evidence-ledger.csv)

### `diagnose-organization-problem`

在进入组织设计之前，判断当前的增长、效率、协同、客户、创新、质量或风险症状：

- 是否真正构成组织问题；
- 主要原因是结构、权责、流程、能力、激励、领导还是执行；
- 是否需要调整组织结构；
- 还是应优先采用更小的机制修复和验证。

Skill 将混合材料拆成无诊断标签的原始证据卡，再围绕每一个组织和候选问题形成诊断卡。它明确允许“未形成诊断”，并遵循“最小充分干预”原则。

#### 使用示例

> 使用 `$diagnose-organization-problem` 判断区域事业部决策缓慢是否真正构成组织问题，以及是否需要调整组织结构。先建立原始证据卡并比较替代解释，不要直接给出改组织图方案。

- [脱敏示例：区域事业部决策慢，是否需要调整组织](examples/diagnose-organization-problem/regional-business-unit-decision.md)

## 仓库结构

```text
org-hr-skills/
├── README.md
├── skills/
│   ├── analyze-business-organization-context/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       └── scripts/
│   └── diagnose-organization-problem/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
└── examples/
    ├── analyze-business-organization-context/
    └── diagnose-organization-problem/
```

## 安装

克隆仓库后，把 Skill 目录复制到 Codex 的 Skills 目录：

```bash
git clone https://github.com/2rs72swr8m-gif/org-hr-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R org-hr-skills/skills/* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后可显式调用 `$analyze-business-organization-context` 或 `$diagnose-organization-problem`，也可在相关请求中由 Codex 自动匹配。

## 当前状态

企业情境研究 Skill 已通过安踏案例正向测试；组织问题判断 Skill 已通过脱敏区域事业部案例验证。当前版本涉及真实权责、流程、协同和人才机制的结论仍需用目标企业内部资料验证。

本仓库暂未附加开源许可证；公开可见不等于允许复制、修改或再分发。后续将在明确知识产权策略后补充许可证。
