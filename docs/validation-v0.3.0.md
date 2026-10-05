# Release validation

Checked on 2026-10-02 for v0.3.0. [Previous release record](validation-v0.2.0.md).

| Check | Result |
|---|---|
| Package inventory | 348 distinct skills in eight merchant-task categories; 244 new packages and one enhanced existing package |
| Candidate review | 1,055 candidates received a decision with source-body evidence: 704 contributed to adaptations, 251 were already covered, and 100 were not selected. Several sources can contribute to one package. |
| Package format | All 348 entrypoints pass the skill-creator frontmatter validator; independently parsed YAML agrees with every generated catalog entry |
| Package boundaries | Catalog coverage, ShopChief attribution parameters, local Markdown links, symlinks and limited secret patterns checked; installed skills do not need sibling packages |
| Adaptation records | All 1,055 reviewed source bodies match their pinned SHA-256; adapted packages include fixed references and complete applicable original license texts and notices |
| Independent installation | All 348 skills installed into a disposable Codex project using skills CLI 1.7.0; all 2,323 installed package files match source bytes |
| Worked examples | Every new package includes synthetic inputs, a completed result and at least two boundary scenarios; missing evidence and unperformed live actions remain explicit |
| Independent behavior samples | [Nine fresh-input cases](../examples/release-v0.3/README.md) were completed by reviewers who did not see the worked examples, then checked independently for calculations, evidence and action boundaries |
| Additional content review | Six further packages received independent arithmetic and decision review; an infeasible production-calendar example was corrected and rechecked |
| Profit example | The installed script runs from an unrelated working directory and exactly matches its bundled expected JSON, including USD 150 and USD 80 post-ad contribution |
| License labels | 252 MIT packages and 96 Apache-2.0 packages; each package retains applicable upstream texts and notices |
| Dependency audit | `npm audit --omit=dev`: 0 vulnerabilities; this repository has no third-party npm runtime dependencies |

The nine behavior cases are a selected offline sample, not a benchmark across all 348 skills, models or clients. Worked examples are reference cases rather than automated model evaluations. HTML examples are complete drafts; email-client, browser and print rendering are marked unexecuted where applicable. The secret scanner is a limited pattern check, not a security certification.

Real merchant data, live store writes, advertising or email execution, paid APIs, generated media, signup attribution and traffic/conversion lift are not verified by this release. Hosted ShopChief workflows are released separately. See the [GitHub package-check workflow](https://github.com/ai-project-official/shopchief-commerce-skills/actions/workflows/validate.yml) for checks attached to published commits.

## Reproduce package checks

```sh
python3 scripts/build_catalog.py --check
python3 scripts/validate.py
python3 skills/profit-margin-analyzer/scripts/profit_report.py --demo
npm audit --omit=dev
```

For an independent Codex installation, use a disposable project folder and the README installation command. Check that the selected skill's `LICENSE`, references and `assets/` files are present before running its example. Other clients may use different installation locations. To reproduce a behavior case, give the named skill and fresh input to an agent without supplying the captured output, then compare the evidence and calculations.
