# Try a merchant task

All fixtures here are synthetic. Prompts can be used with an installed skill; they are examples of requested deliverables, not recorded live-agent success results.

## 1. Contribution margin

Install `profit-margin-analyzer`, then ask:

> Read examples/profit-check/orders.csv. Reconcile the input definitions and produce pre-ad and post-ad contribution, the conditional first-order CPA ceiling, missing costs and a merchant action. Do not change prices.

The dependency-free script and expected arithmetic are in [profit-check](profit-check/README.md).

## 2. Product-page review

Install `shopify-product-page-cro`, supply your actual page URL or screenshot and ask:

> Review this page for product clarity, variant selection, delivery questions and genuine proof. Separate observed issues from hypotheses. Deliver specific replacement copy using only verified product facts. Do not modify my store.

Requires public-page access or supplied evidence. Without analytics, this is a heuristic page review, not a measured conversion diagnosis.

## 3. Search content

Install `dtc-content-strategy` and use [the merchant brief](merchant-brief.md):

> Plan four buyer guides for this product. Show the unique question, facts required, destination, distribution and measurement. We have no keyword provider account; do not invent volume.

## 4. Collection launch

Install `dtc-launch-marketing` and use the same brief:

> Prepare a launch plan for the inventory shown, list missing readiness facts, draft a launch-page outline and show the budget decision we need to make. Do not send or publish anything.

## 5. Social creative

Install `dtc-social-content`:

> Create two short-video scripts from the brief. Keep dimensions/material accurate, identify shots requiring real photos and do not claim waterproofing or customer results.
