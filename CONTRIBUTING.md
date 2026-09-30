# Contributing

Describe the merchant task, observed failure and expected useful outcome. Use synthetic or explicitly authorized redacted inputs. Do not include credentials, customer exports or confidential store information.

Keep skills independently installable: `SKILL.md` with accurate name/description, supporting files only when useful, and no dependencies on an unavailable runtime. Preserve the user's scope and do not fabricate facts or claim unperformed writes. Any new API constraints or benchmark claims need dated primary sources.

For third-party material, include its exact source version, applicable license and notices. By submitting original contributions you agree they may be distributed under this repository's MIT license; you must have the right to contribute them.

Run `python3 scripts/validate.py`. For behavior changes, provide a concrete acceptance example and distinguish static checks from actual agent/store execution. Do not add merchant credentials or require a paid service for basic validation.
