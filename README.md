# ShopChief Commerce Skills

**300+ open-source AI skills for independent ecommerce and DTC sellers.** Research products, improve your storefront, plan campaigns, retain customers and manage inventory with evidence and clear deliverables.

[中文说明](README.zh-CN.md) · [Browse by task](docs/catalog.md) · [Workflow recipes](docs/playbooks.md) · [Worked examples](examples/README.md) · [ShopChief](https://shopchief.ai/?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=readme)

## Start with a merchant task

| I want to… | Skill | See the result |
|---|---|---|
| Know where my order margin went | [Profit margin analyzer](skills/profit-margin-analyzer/SKILL.md) | [CSV → contribution waterfall → next action](skills/profit-margin-analyzer/assets/worked-example.md) |
| Make a product page clearer | [Shopify PDP CRO](skills/shopify-product-page-cro/SKILL.md) | [Source page → findings → finished replacement copy](skills/shopify-product-page-cro/assets/worked-review.md) |
| Validate a product opportunity | [Product opportunity research](skills/product-opportunity-research/SKILL.md) | Supported candidates, risks and a test/defer/reject decision |
| Understand store search problems | [Site SEO audit](skills/site-seo-audit/SKILL.md) | Evidence and prioritized repairs |
| Plan a collection launch | [DTC launch marketing](skills/dtc-launch-marketing/SKILL.md) | Readiness, assets, channels and measurement |
| Turn product facts into social content | [DTC social content](skills/dtc-social-content/SKILL.md) | Finished scripts and factual asset requirements |
| Stop discounts from destroying margin | [Discount profitability](skills/discount-profitability/SKILL.md) | Contribution per order and the volume needed to recover it |
| Restock without tying up too much cash | [Inventory replenishment](skills/inventory-replenishment-planning/SKILL.md) | Stock position, lead-time demand and an order proposal |
| Build a useful welcome sequence | [Email welcome series](skills/email-welcome-series/SKILL.md) | Trigger, exclusions, finished messages and a QA plan |
| Diagnose missing purchase events | [GA4 ecommerce measurement](skills/ga4-ecommerce-measurement/SKILL.md) | Event contract, duplicate checks and a verification plan |
| Understand why customers return products | [Returns analysis](skills/returns-reason-analysis/SKILL.md) | Comparable reason rates and actions tied to source evidence |
| Prepare a safe catalog import | [Catalog import preflight](skills/catalog-import-change-preflight/SKILL.md) | [Change rows, conflict checks and preserved fields](skills/catalog-import-change-preflight/assets/worked-example.md) |
| Explain a payout difference | [Payment reconciliation](skills/payment-payout-reconciliation/SKILL.md) | [Signed transactions, deposit and unresolved order links](skills/payment-payout-reconciliation/assets/worked-example.md) |
| Check whether creator content can run as an ad | [Creator paid amplification](skills/creator-paid-amplification/SKILL.md) | [Rights, dates, offer consistency and activation decision](skills/creator-paid-amplification/assets/worked-example.md) |

The [task catalog](docs/catalog.md) groups skills into research, storefront conversion, search and feeds, content, advertising, retention, measurement, and operations. Choose a focused workflow; you do not need to install the whole library.

## Install a skill

With Node.js and an Agent Skills-compatible client:

```sh
npx skills add ai-project-official/shopchief-commerce-skills --list
npx skills add ai-project-official/shopchief-commerce-skills --skill profit-margin-analyzer
```

Choose your client in the installer. Each folder includes its references and license. Entry instructions are in English; some packages also include Chinese companion instructions. Ask for deliverables in your preferred language. Using these skills does not require a ShopChief account.

## Get your first result

The profit and product-page examples are included in their individual skill packages. After installing the profit skill, ask your agent:

> Use profit-margin-analyzer. Locate its installed folder, run scripts/profit_report.py --demo from that folder, and explain the contribution waterfall and missing costs. Compare with assets/worked-example.md. Do not change prices or budgets.

For a **Codex project installation**, this complete terminal example works from your project directory with Python 3.10+:

```sh
npx skills add ai-project-official/shopchief-commerce-skills --skill profit-margin-analyzer --agent codex -y --copy
python3 .agents/skills/profit-margin-analyzer/scripts/profit_report.py --demo
```

Expected post-ad contribution: USD 150 for DEMO-POUCH and USD 80 for DEMO-BOTTLE. These are synthetic inputs, not customer performance. The script resolves its bundled CSV automatically. Other clients may use a different installation path; ask the agent to locate the skill folder.

For the page review, install `shopify-product-page-cro` and ask:

> Read assets/source-page.md and assets/product-facts.md in this skill's installed folder. Produce findings and finished replacement copy, then compare with assets/worked-review.md. Do not modify a store.

## Continue with ShopChief

Local skills suit merchants and operators who already use an AI client and want to supply their own exports and tools. [ShopChief](https://shopchief.ai/?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=hosted_workflows) suits teams that want built-in commerce workflows, store context and supported connected actions in one workspace. The open-source library and the hosted skill catalog are separate releases; check the app for available workflows and integrations.

Use the [profit calculator](https://shopchief.ai/tools/profit-margin-calculator?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=profit_example) to explore your cost assumptions, or the [product-copy workflow](https://shopchief.ai/solutions/shopify-product-descriptions?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=product_page_example) to prepare verified Shopify copy. Installed skills and local examples work independently.

## Tools and permissions

Merchant files and public evidence support basic analysis. Live Shopify operations need an authorized connector or CLI; paid research and image generation need their respective tools. If unavailable, deliver local files or a complete review and identify missing evidence. Skills do not grant permission to publish, send messages, spend money or change a store. See [runtime requirements](docs/runtime.md) and [validation](VALIDATION.md).

## Contribute

Share a reproducible failure, clearer merchant input or an improvement to a specific workflow. Use synthetic or authorized redacted examples. Read [CONTRIBUTING.md](CONTRIBUTING.md).

To work on the full repository:

```sh
git clone https://github.com/ai-project-official/shopchief-commerce-skills.git
cd shopchief-commerce-skills
python3 scripts/validate.py
```

For catalog changes, update `scripts/catalog-groups.json`, run `python3 scripts/build_catalog.py`, then validate. A new skill needs a distinct merchant decision, concrete inputs and outputs, a worked example, failure cases, and appropriate permissions. See [the contribution guide](CONTRIBUTING.md).

## License

ShopChief's original contributions use [MIT](LICENSE). Adapted packages retain their applicable licenses and notices. See [NOTICE.md](NOTICE.md) and each installed package's `LICENSE` for exact terms and attribution.
