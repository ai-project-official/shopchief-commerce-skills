# Runtime requirements and verification

The public interface is the Agent Skills `SKILL.md` format. Each folder is independently installable with its local references. Format/discovery checks do not demonstrate behavioral compatibility with every client or successful merchant operations.

| Capability | Required input/tool | If unavailable |
|---|---|---|
| Profit/context/content planning | Merchant facts, CSVs or briefs | Deliver partial analysis with explicit missing fields |
| Public page review | Browsing or provided HTML/screenshots | Limit conclusions to supplied evidence |
| Search metrics | Merchant exports or an authorized provider client | Use qualitative public evidence; do not invent metrics |
| Shopify mutations | Authorized store connector/CLI and current schema | Produce drafts/import sheets/local theme files |
| Image generation/editing | An installed image provider tool and source assets | Produce prompts/asset briefs, not fabricated images |
| Theme preview | Local preview or authorized unpublished Shopify theme | Report local-only files and unverified rendering |
| Paid media and lifecycle messaging | Platform exports, or a connector with appropriate account scope | Produce analyses and campaign/flow drafts; no automatic budget changes or sends |
| Inventory, pricing and fulfillment | Dated SKU, stock, lead-time, cost and policy exports | Produce order proposals and policy-aware worksheets; do not assume missing values are zero |
| Analytics and cohorts | Event definitions, observation windows and appropriately minimized exports | Produce a measurement plan or partial analysis; do not invent causal attribution or lifetime outcomes |

No API keys, runtime accounts, analytics tracker, automatic network calls or scheduled tasks are bundled. Paid providers can charge for agent-initiated operations; those require the user's scope and budget. Never paste secrets into an issue or generated report.

The release is statically checked for names, entrypoints, references, bundled licenses and accidental secret patterns. A synthetic profit example checks arithmetic. Client discovery/install verification is recorded in [VALIDATION.md](../VALIDATION.md). Live Shopify, paid research, image generation and end-to-end commercial performance have not been accepted as part of this release.
