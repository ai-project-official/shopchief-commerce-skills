# Worked merchant examples

## Included with single-skill installation

| Task | Input | Completed result |
|---|---|---|
| Profit analysis | [Synthetic CSV](../skills/profit-margin-analyzer/assets/orders.csv) | [Waterfall and merchant action](../skills/profit-margin-analyzer/assets/worked-example.md), [calculator JSON](../skills/profit-margin-analyzer/assets/expected-report.json) |
| Product-page review | [Original page](../skills/shopify-product-page-cro/assets/source-page.md), [verified facts](../skills/shopify-product-page-cro/assets/product-facts.md) | [Findings and finished copy](../skills/shopify-product-page-cro/assets/worked-review.md) |

Install the corresponding skill and ask the agent to locate its folder. Profit: run `scripts/profit_report.py --demo` inside that folder. Page review: read the two input files under `assets/`, complete the review, then compare with `assets/worked-review.md`.

These are synthetic worked examples. The profit output is reproducible arithmetic; the page review is an editorial reference answer. Neither is a claim of live-store performance or uniform agent behavior.

## Campaigns, retention and store operations

Every package added in v0.2.0 or v0.3.0 contains `assets/worked-example.md`: synthetic input, an expected result and two acceptance scenarios, including missing or conflicting evidence. The [task catalog](../docs/catalog.md) links each available example.

| Task | Completed example |
|---|---|
| Discount without losing contribution | [Price, costs, contribution and required sales volume](../skills/discount-profitability/assets/worked-example.md) |
| Allocate inventory cash | [Weekly cash projection and funding gap](../skills/cash-flow-inventory-planning/assets/worked-example.md) |
| Replenish a SKU | [Stock position, receipt timing and pack rounding](../skills/inventory-replenishment-planning/assets/worked-example.md) |
| Plan an ad budget | [Remaining cap and reconciled daily pacing](../skills/ad-budget-pacing/assets/worked-example.md) |
| Brief a UGC creator | [Shot sequence, finished lines and usage-rights boundaries](../skills/ugc-creator-brief/assets/worked-example.md) |
| Welcome an email subscriber | [Trigger, exclusions and finished messages](../skills/email-welcome-series/assets/worked-example.md) |
| Measure influencer orders | [Order deduplication and net campaign contribution](../skills/influencer-campaign-measurement/assets/worked-example.md) |
| Measure customer value | [Mature cohort contribution and acquisition payback](../skills/customer-lifetime-value/assets/worked-example.md) |
| Diagnose purchase tracking | [Item value, tax, shipping and duplicate transaction handling](../skills/ga4-ecommerce-measurement/assets/worked-example.md) |
| Repair a product feed | [Variant identity and factual field corrections](../skills/product-feed-optimization/assets/worked-example.md) |
| Triage support tickets | [Priority, ownership and a customer reply](../skills/customer-support-triage/assets/worked-example.md) |
| Write a help article | [Approved care instructions and a completed article](../skills/support-knowledge-base/assets/worked-example.md) |

Try a case before supplying your own data: ask the agent to read the skill and the example's inputs, produce its answer, then compare it with the worked result. A good answer preserves denominators and source facts, identifies unknowns and proposes the next merchant decision. Matching a synthetic result does not establish live tool compatibility or a sales lift.

## Independent fresh-input cases

[Nine v0.3.0 review cases](release-v0.3/README.md) include new inputs and captured agent outputs for catalog changes, payouts, consent, creator rights, contribution values, comparison panels and shopper research. The reviewers used the skills without seeing their worked examples. These selected offline cases complement the package checks; they do not establish live-store compatibility.

## Additional prompts

The following exercises use the [merchant brief](merchant-brief.md), which is a repository resource rather than an asset bundled in these other skills. Open the link and supply its text to your agent, or obtain the full repository with `git clone https://github.com/ai-project-official/shopchief-commerce-skills.git` and work inside its directory.

- **dtc-content-strategy:** Plan four buyer guides from the brief. Show each question, facts needed, destination and measurement. Do not invent keyword volume.
- **dtc-launch-marketing:** Produce a launch calendar, readiness gates and launch-page copy outline. Identify inventory and policy gaps. Do not spend or publish.
- **dtc-social-content:** Produce two short-video scripts using only the brief's dimensions and material. Identify shots needing real photos; do not claim waterproofing or customer outcomes.
