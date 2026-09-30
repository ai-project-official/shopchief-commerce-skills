# Worked merchant examples

## Included with single-skill installation

| Task | Input | Completed result |
|---|---|---|
| Profit analysis | [Synthetic CSV](../skills/profit-margin-analyzer/assets/orders.csv) | [Waterfall and merchant action](../skills/profit-margin-analyzer/assets/worked-example.md), [calculator JSON](../skills/profit-margin-analyzer/assets/expected-report.json) |
| Product-page review | [Original page](../skills/shopify-product-page-cro/assets/source-page.md), [verified facts](../skills/shopify-product-page-cro/assets/product-facts.md) | [Findings and finished copy](../skills/shopify-product-page-cro/assets/worked-review.md) |

Install the corresponding skill and ask the agent to locate its folder. Profit: run `scripts/profit_report.py --demo` inside that folder. Page review: read the two input files under `assets/`, complete the review, then compare with `assets/worked-review.md`.

These are synthetic worked examples. The profit output is reproducible arithmetic; the page review is an editorial reference answer. Neither is a claim of live-store performance or uniform agent behavior.

## Additional prompts

The following exercises use the [merchant brief](merchant-brief.md), which is a repository resource rather than an asset bundled in these other skills. Open the link and supply its text to your agent, or obtain the full repository with `git clone https://github.com/ai-project-official/shopchief-commerce-skills.git` and work inside its directory.

- **dtc-content-strategy:** Plan four buyer guides from the brief. Show each question, facts needed, destination and measurement. Do not invent keyword volume.
- **dtc-launch-marketing:** Produce a launch calendar, readiness gates and launch-page copy outline. Identify inventory and policy gaps. Do not spend or publish.
- **dtc-social-content:** Produce two short-video scripts using only the brief's dimensions and material. Identify shots needing real photos; do not claim waterproofing or customer outcomes.
