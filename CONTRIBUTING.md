# Contributing

Describe the merchant task, observed failure and expected useful outcome. Use synthetic or explicitly authorized redacted inputs. Do not include credentials, customer exports or confidential store information.

Keep skills independently installable: `SKILL.md` with accurate name/description, supporting files only when useful, and no dependencies on an unavailable runtime. Preserve the user's scope and do not fabricate facts or claim unperformed writes. Any new API constraints or benchmark claims need dated primary sources.

For third-party material, include its exact source version, applicable license and notices. By submitting original contributions you agree they may be distributed under this repository's MIT license; you must have the right to contribute them.

Before adding a skill, identify the merchant decision it owns and explain how its deliverable differs from the closest existing skill. A different channel name, persona or output language alone does not justify another package. Include concrete inputs, task-specific reasoning or calculations, required tools and an export-only path when possible. Avoid universal performance targets or fabricated customer results.

New packages include a linked `assets/worked-example.md` with synthetic input, expected decisions or calculations, and at least two acceptance scenarios, including a missing-data or boundary case. These are review fixtures, not evidence of a real merchant outcome. Keep any necessary license and references inside the installed package.

Add the skill to one task group in `scripts/catalog-groups.json`, then run `python3 scripts/build_catalog.py` and `python3 scripts/validate.py`. For behavior changes, distinguish static checks from actual agent/store execution. Do not add merchant credentials or require a paid service for basic validation.
