# ShopChief Commerce Skills

**300+ open-source AI skills for independent ecommerce and DTC sellers.** Research products, improve your storefront, plan campaigns, retain customers and manage inventory with evidence and clear deliverables.

[中文说明](README.zh-CN.md) · [Copy installation prompt](#install-with-codex-or-claude-code) · [Browse by task](docs/catalog.md) · [Workflow recipes](docs/playbooks.md) · [Worked examples](examples/README.md) · [ShopChief](https://shopchief.ai/?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=readme)

## Install with Codex or Claude Code

Open your project in **Codex or Claude Code with local terminal access**. Copy the matching block using its copy button, paste it into the agent, and send it. The agent handles installation in this project. The current [skills CLI](https://github.com/vercel-labs/skills) requires **Node.js 22.20+**, npm/npx and Git.

**For Codex:**

```text
Install all ShopChief Commerce Skills for Codex in my current project.
Check Node.js 22.20+, npx and Git, then list this repository’s skills.
Preserve existing same-name folders or links in .agents/skills.
If any exist, install only missing names with an explicit --skill list.
If nothing is missing, skip installation and report that everything is present.
If there are no same-name conflicts, run:
npx --yes skills@latest add ai-project-official/shopchief-commerce-skills --agent codex --skill '*' --copy --yes
Verify SKILL.md files and bundled references; report installed/skipped counts, paths and failures.
Tell me if I need to reload the agent. Only install; do not run merchant tasks.
```

**For Claude Code:**

```text
Install all ShopChief Commerce Skills for Claude Code in my current project.
Check Node.js 22.20+, npx and Git, then list this repository’s skills.
Preserve existing same-name folders or links in .claude/skills.
If any exist, install only missing names with an explicit --skill list.
If nothing is missing, skip installation and report that everything is present.
If there are no same-name conflicts, run:
npx --yes skills@latest add ai-project-official/shopchief-commerce-skills --agent claude-code --skill '*' --copy --yes
Verify SKILL.md files and bundled references; report installed/skipped counts, paths and failures.
Tell me if I need to reload the agent. Only install; do not run merchant tasks.
```

These prompts install the whole library into `.agents/skills/` for Codex or `.claude/skills/` for Claude Code. To start smaller, change “all ShopChief Commerce Skills” to the skills you want and replace `--skill '*'` with their names, for example `--skill profit-margin-analyzer shopify-product-page-cro`. The [task catalog](docs/catalog.md) lists every installable name. Skills and bundled examples work without a ShopChief account.

<!-- skill-overview:start -->
## Skills by category

**348 skills across 8 categories.** Each skill package is counted once; translations and reference files are not additional skills.

| Category | Skills | Typical tasks |
|---|---:|---|
| [Research and positioning](docs/catalog.md#research-and-positioning) | 32 | Product opportunities, competitors, customer research and positioning |
| [Storefront and conversion](docs/catalog.md#storefront-and-conversion) | 36 | Shopify storefronts, product pages, checkout and catalog quality |
| [Search visibility and product feeds](docs/catalog.md#search-visibility-and-product-feeds) | 29 | SEO audits, AI search visibility, structured data and shopping feeds |
| [Content and creative](docs/catalog.md#content-and-creative) | 73 | Product copy, images, video, UGC briefs and localization |
| [Advertising and partnerships](docs/catalog.md#advertising-and-partnerships) | 26 | Ad planning, budget pacing, creators and affiliate programs |
| [Email and retention](docs/catalog.md#email-and-retention) | 25 | Welcome flows, cart recovery, SMS, loyalty and repeat purchases |
| [Measurement and unit economics](docs/catalog.md#measurement-and-unit-economics) | 58 | Profit, ROAS, attribution, pricing and financial reconciliation |
| [Inventory fulfillment and support](docs/catalog.md#inventory-fulfillment-and-support) | 69 | Replenishment, purchasing, shipping, returns and customer support |
| **Total** | **348** | |
<!-- skill-overview:end -->

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

For a focused installation from your terminal (Node.js 22.20+, npm/npx and Git):

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

## License

ShopChief's original contributions use [MIT](LICENSE). Adapted packages retain their applicable licenses and notices. See [NOTICE.md](NOTICE.md) and each installed package's `LICENSE` for exact terms and attribution.
