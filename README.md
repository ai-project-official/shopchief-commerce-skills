# ShopChief Commerce Skills

**40 open-source agent skills for independent ecommerce and DTC sellers.** Research products, improve Shopify pages, plan search content, understand contribution margin, and prepare campaigns with evidence you can inspect.

[中文说明](README.zh-CN.md) · [Browse all 40 skills](docs/catalog.md) · [Try an example](examples/README.md) · [ShopChief](https://shopchief.ai/?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=readme)

## Start with a merchant task

| I want to… | Start here | You get |
|---|---|---|
| Know whether orders are profitable | [Profit margin analyzer](skills/profit-margin-analyzer/SKILL.md) | A revenue/cost waterfall, break-even CPA and evidence gaps |
| Improve a product page | [Shopify PDP CRO](skills/shopify-product-page-cro/SKILL.md) | Findings tied to the actual page, replacement copy and a review plan |
| Find a product opportunity | [Product opportunity research](skills/product-opportunity-research/SKILL.md) | Supported candidates, risks and a test/defer/reject decision |
| Understand store search problems | [Site SEO audit](skills/site-seo-audit/SKILL.md) | Scoped findings, source evidence and prioritized actions |
| Plan a collection launch | [DTC launch marketing](skills/dtc-launch-marketing/SKILL.md) | A contribution-aware launch plan, assets and measurement |
| Turn product facts into social content | [DTC social content](skills/dtc-social-content/SKILL.md) | Finished scripts/carousels and factual asset requirements |

## Install

With an Agent Skills-compatible client and Node.js available:

```sh
# Discover the available skills
npx skills add ai-project-official/shopchief-commerce-skills --list

# Select a single task
npx skills add ai-project-official/shopchief-commerce-skills --skill profit-margin-analyzer

# Open the interactive skill/client selector
npx skills add ai-project-official/shopchief-commerce-skills
```

Choose the client you actually use, such as Codex or Claude Code. These are standard `SKILL.md` packages; the repository does not install accounts, APIs, background jobs or paid subscriptions. See [runtime and compatibility](docs/runtime.md) for the verification boundary.

Example prompt after installation:

> Analyze the sample order table and calculate pre-ad contribution, post-ad contribution and break-even CPA. Identify missing costs. Do not change any prices or advertising budgets.

## What is included

- 40 independently installable skills for DTC and independent ecommerce sellers.
- 40 English entrypoints and 33 Chinese companion instructions.
- Supporting references, input examples and a reproducible sample profit report.

The workflows cover product selection, suppliers, merchant context, copy, product imagery, Shopify drafts and themes, CRO, SEO/GEO, unit economics and campaign planning.

## Try it without a store connection

```sh
python3 scripts/profit_report.py examples/profit-check/orders.csv
python3 scripts/validate.py
```

The sample is synthetic, not a customer result. Other [example prompts](examples/README.md) show page review, content planning and launch preparation. No skill execution is measured as a revenue benchmark.

## Data and tools

Start with merchant-provided files and public sources. Live Shopify operations need an authorized connector or CLI; paid research needs the user's provider account and budget; image generation needs an available image tool. None are bundled. Missing data remains unknown.

Theme Studio supports local theme work and authorized draft uploads. It does not reproduce ShopChief's hosted project-state service. A prepared file, uploaded draft and published change are different outcomes.

Skills never grant permission to send messages, spend money, publish a page, change a price or alter checkout. Follow the user's actual scope and the host's authorization rules. Keep credentials and customer data out of Git.

## About ShopChief

Built and maintained by [ShopChief](https://shopchief.ai/?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=about), an AI workspace for ecommerce operations. These open-source packages can be used independently. The website is an optional way to explore the product; using these files does not require a ShopChief account.

## Contribute

Useful contributions include a reproducible failure, clearer merchant inputs, better source attribution, or an improvement to a specific task. Read [CONTRIBUTING.md](CONTRIBUTING.md). Please use synthetic/redacted examples and describe what was actually verified.

## License

[MIT](LICENSE). Third-party adaptations retain Corey Haines' copyright and MIT notice. See [NOTICE.md](NOTICE.md). Product names and logos identify their respective owners and do not imply endorsement.
