# 企业战略、组织与人力研究 Skill

`analyze-business-organization-context` 是一个面向企业管理者、CHRO、战略 HRBP 和组织发展专业人士的 AI Skill。

它围绕目标企业研究行业环境、竞争挑战、战略与业务定位、关键业务运作方式和代表性企业组织模式，并进一步形成对目标企业组织、人才、机制和文化建设的要求。

这个 Skill 服务于后续组织诊断、组织设计、人才管理、绩效、薪酬、领导力和文化建设，而不是生成一份与组织工作割裂的宏观行业报告。

## 核心推理

> 外部竞争与行业挑战 → 战略与业务定位 → 关键业务运作方式 → 组织运作模式 → 核心组织能力 → 组织与人力资源要求

报告以前台的“行业—企业—组织—启示”结构表达，后台使用上述因果链检查结论，避免从行业趋势直接跳到通用 HR 建议。

## 工作流程

Skill 会先确认研究目标、范围、后续管理任务和内部资料，再主动检索年报、监管披露、ESG 报告、公司官网、政府与行业资料以及可公开访问的专业研究。

默认交付包括：

1. 行业赛道整体洞察；
2. 代表性企业战略与经营比较；
3. 代表性企业组织模式比较；
4. 对目标企业的组织与人力启示；
5. 证据底稿与组织情境输入卡。

研究过程明确区分事实、计算、推断和待验证假设，不用企业公开口号直接证明组织能力已经形成，也不把不同经营模式下的人效指标直接用于裁员或组织优劣排名。

## 使用示例

> 使用 `$analyze-business-organization-context` 研究安踏所在行业，比较 4—6 家代表性企业的战略、经营和组织模式，并形成对安踏组织与人力建设的启示。开始前先询问我是否有内部材料。

安踏正向测试：

- [比较研究报告](examples/analyze-business-organization-context/anta-comparative-forward-test.md)
- [研究证据底稿](examples/analyze-business-organization-context/anta-comparative-evidence-ledger.csv)

## 安装

```bash
git clone https://github.com/2rs72swr8m-gif/analyze-business-organization-context.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R analyze-business-organization-context/skills/analyze-business-organization-context \
  "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后可显式调用 `$analyze-business-organization-context`，也可在相关研究请求中由 Codex 自动匹配。

## 仓库结构

```text
analyze-business-organization-context/
├── README.md
├── skills/analyze-business-organization-context/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   └── scripts/
└── examples/analyze-business-organization-context/
```

## 适用边界

- 当前公开示例主要依据公开信息；真实权责、流程、协同和人才机制仍需目标企业内部资料验证。
- Skill 不直接替代完整组织诊断或组织方案设计。
- 内部材料不得未经授权写入公开版本。

本仓库暂未附加开源许可证；公开可见不等于允许复制、修改或再分发。
