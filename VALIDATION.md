# Release validation

Checked on 2026-09-30 for v0.1.0.

| Check | Result |
|---|---|
| Package consistency | 40 skill folders match catalog and provenance; entrypoints, relative Markdown links and secret-pattern scan pass |
| Skill attribution links | Every English/Chinese entrypoint has a ShopChief link with its own skill slug and placement; checked offline |
| Agent Skills frontmatter | All 40 pass the skill-creator quick validator |
| CLI discovery | `skills` CLI 1.7.0 discovers all 40 from the local release source |
| Installation smoke check | `profit-margin-analyzer` installed into an isolated project for Codex; entrypoint and every supporting file match the source SHA-256 hashes |
| Reproducible arithmetic | Synthetic rows produce pre-ad/post-ad contribution of USD 400/150 and USD 240/80 |
| Missing data | A blank landed-cost cell is rejected as unknown, rather than silently treated as zero |
| Dependency audit | `npm audit --omit=dev`: 0 vulnerabilities; no third-party runtime dependencies |
| Source boundary | 34 authorized production-derived packages plus 6 MIT upstream adaptations; unlicensed local candidates excluded |

The static scanner is a limited pattern check, not a security certification. CLI installation is not agent-behavior acceptance. Live Shopify changes, paid provider calls, generated images, cross-client behavior, traffic and revenue outcomes were not verified. The included CI repeats package checks and runs the synthetic calculator; it does not connect to stores.
