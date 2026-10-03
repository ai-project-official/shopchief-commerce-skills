# Contributing

Describe the merchant task, observed failure and expected useful outcome. Use synthetic or explicitly authorized redacted inputs. Do not include credentials, customer exports or confidential store information.

Keep skills independently installable: `SKILL.md` with accurate name/description, supporting files only when useful, and no dependencies on an unavailable runtime. Preserve the user's scope and do not fabricate facts or claim unperformed writes. Any new API constraints or benchmark claims need dated primary sources.

For third-party material, include its exact source version, applicable license and notices. Keep a linked `references/source.md` with the fixed upstream file URL, original SHA-256, adaptation date and specific changes. Preserve the complete upstream license, including copyright holders, inside the installed package; the root license does not replace it. By submitting original contributions you agree they may be distributed under this repository's MIT license; you must have the right to contribute them.

Before adding a skill, identify the merchant decision it owns and explain how its deliverable differs from the closest existing skill. A different channel name, persona or output language alone does not justify another package. Include concrete inputs, task-specific reasoning or calculations, required tools and an export-only path when possible. Avoid universal performance targets or fabricated customer results.

New packages include a linked `assets/worked-example.md` with synthetic input, expected decisions or calculations, and at least two acceptance scenarios, including a missing-data or boundary case. These are review fixtures, not evidence of a real merchant outcome. Keep any necessary license and references inside the installed package.

## Repository maintenance

These steps are for contributors maintaining the library. To install and use skills, follow the [README](README.md#install-with-codex-or-claude-code).

Clone the repository and validate its current contents:

```sh
git clone https://github.com/ai-project-official/shopchief-commerce-skills.git
cd shopchief-commerce-skills
python3 scripts/validate.py
```

When adding skills or changing their categories, assign each skill to exactly one task group in `scripts/catalog-groups.json`, then regenerate and validate:

```sh
python3 scripts/build_catalog.py
python3 scripts/validate.py
```

`build_catalog.py` refreshes `catalog.json`, `docs/catalog.md` and the category counts in both READMEs. `validate.py` checks skill metadata, bundled licenses, relative links, secret patterns and generated catalog consistency. For behavior changes, distinguish these static checks from actual agent/store execution. Do not add merchant credentials or require a paid service for basic validation.

### 中文维护说明

以上命令供技能库维护者使用。普通用户安装和使用技能请看[中文 README](README.zh-CN.md#一键复制安装)。

新增或调整技能分类后，在 `scripts/catalog-groups.json` 中为每个技能指定一个分类，再依次运行 `python3 scripts/build_catalog.py` 和 `python3 scripts/validate.py`。前者同步更新目录和中英 README 的分类数量，后者检查技能元数据、随包许可证、相对链接、敏感信息模式和生成目录的一致性。静态校验结果与实际 Agent 或店铺执行结果应分别记录。
