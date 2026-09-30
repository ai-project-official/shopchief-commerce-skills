# Release validation

Checked on 2026-09-30 for v0.1.1.

| Check | Result |
|---|---|
| Package format | All 40 entrypoints pass the Agent Skills frontmatter validator |
| Package boundaries | Catalog, bundled licenses and relative links checked; a skill may not link to a missing file or escape its individually installed folder |
| Independent installation | All 40 skills installed into an isolated Codex project using skills CLI 1.7.0 |
| Profit example | Installed script runs with `--demo` from an unrelated working directory; output matches the bundled expected JSON |
| Arithmetic and input handling | Pre/post-ad contribution is USD 400/150 and USD 240/80; a blank cost is rejected as unknown |
| Page-review example | Input page, product facts and completed review are included in the installed skill; replacement copy checked against the supplied facts |
| Portability review | Shared research/delivery instructions allow actual client tools and local files; Shopify integrations are conditional |
| Product update instructions | Category/SKU references preserve merchant taxonomy and existing identifiers; unknown fields do not request clearing |
| Referral destinations | Profit calculator and product-copy workflow opened successfully in a browser with substantive task content |
| Attribution parameters | Every entrypoint's ShopChief links retain skill source, medium, campaign and placement |
| Dependency audit | `npm audit --omit=dev`: 0 vulnerabilities; no third-party runtime dependencies |

The scanner is a limited pattern check, not a security certification. The page review is an editorial reference answer. No claim is made that all models produce identical answers. Live store writes, paid APIs, generated images, signup attribution and traffic/conversion lift are not verified by this release.
