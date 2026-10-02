# v0.2.0 release validation

Checked on 2026-10-02 for v0.2.0.

| Check | Result |
|---|---|
| Package inventory | 104 distinct skills in eight merchant-task categories; 64 new packages in this release |
| Package format | All 104 entrypoints pass the skill-creator frontmatter validator |
| Catalog correctness | Generated fields for all 104 entries independently compared with PyYAML, including wrapped quoted descriptions |
| Package boundaries | Catalog coverage, bundled licenses, ShopChief attribution parameters and local Markdown links checked; installed skills do not need sibling packages |
| Independent installation | All 104 skills installed into an isolated project using skills CLI 1.7.0; Codex package files compared with source |
| New examples | All 64 new packages include synthetic worked results and two acceptance scenarios; calculations and decision boundaries reviewed, with independent cross-review samples |
| Profit example | Installed script executes from an unrelated working directory; output matches the bundled expected JSON |
| Arithmetic and input handling | Pre/post-ad contribution is USD 400/150 and USD 240/80; a blank cost is rejected as unknown |
| Event example | GTM data-layer snippet executed in an isolated Node context; this verifies the sample payload, not a live container or analytics receipt |
| Practical review | Examples distinguish subscription/customer denominators, click/view attribution and backlog/lost-sales stock scenarios; UGC, support and comparison examples include finished drafts |
| License review | 102 MIT packages and two Apache-2.0 packages; adapted packages retain complete applicable notices and fixed upstream references |
| Dependency audit | `npm audit --omit=dev`: 0 vulnerabilities; no third-party runtime dependencies |

The acceptance scenarios are reference cases, not an automated evaluation of model behavior. The secret scanner is a limited pattern check, not a security certification. Real merchant data, live store writes, advertising or email execution, paid APIs, generated media, signup attribution and traffic/conversion lift are not verified by this release. Hosted ShopChief workflows are released separately.

## Reproduce package checks

```sh
python3 scripts/build_catalog.py --check
python3 scripts/validate.py
python3 skills/profit-margin-analyzer/scripts/profit_report.py --demo
npm audit --omit=dev
```

For an independent Codex installation, use a disposable project folder and the README installation command. Check that the selected skill's `LICENSE`, references and `assets/` files are present before running its example. Other clients may use different installation locations.
