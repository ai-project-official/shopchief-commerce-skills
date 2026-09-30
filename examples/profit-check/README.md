# Synthetic contribution example

This is invented demonstration data, not a customer result. Revenue is already net of discounts/refunds and excludes collected tax. Landed cost and outbound fulfillment are distinct. Return costs exclude refund amounts already removed from revenue.

Run `python3 scripts/profit_report.py examples/profit-check/orders.csv` from the repository root.

- DEMO-POUCH: revenue 1,000; non-ad variable costs 600; pre-ad contribution 400; ad spend 250; post-ad contribution 150. Per order: 40 before ads and 15 after ads. The first-order break-even CPA is 40 only if the 10 orders are the relevant acquired-order cohort.
- DEMO-BOTTLE: revenue including retained shipping 840; non-ad costs 600; pre-ad contribution 240; ad spend 160; post-ad contribution 80.

Blank inputs fail rather than become zero. Fixed overhead, cash-flow timing and customer lifetime value are not modeled. Use the profit-margin-analyzer skill to reconcile real account exports and explain missing cost coverage.
