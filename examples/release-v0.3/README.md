# Fresh-input review cases

Independent reviewers exercised nine skill cases offline with new synthetic merchant requests on 2026-10-02. Each reviewer received the requested skill entrypoint and input, while the package’s worked example was withheld. A second reviewer checked the completed output for calculations, supported conclusions, missing-data handling and action boundaries.

These are observed outputs from a small selected set, not an automated benchmark or a guarantee for all tasks, models or clients. No store, payment, advertising or email account was connected.

- [Requests and synthetic inputs](inputs.json)
- [Captured outputs and actions performed](observed-results.json)

| Case | Skill | Decision exercised |
|---|---|---|
| Conflicting catalog edit | [Catalog import preflight](../../skills/catalog-import-change-preflight/SKILL.md) | Preserve omitted fields; separate a stale price conflict from a valid proposal |
| Settlement membership | [Payout reconciliation](../../skills/payment-payout-reconciliation/SKILL.md) | Reconcile signed transactions and bank deposit while leaving order linkage unknown |
| Identity and opt-out | [Customer identity and consent](../../skills/customer-identity-and-consent-audit/SKILL.md) | Separate identity evidence from contact permission; preserve suppression |
| Creator asset eligibility | [Paid amplification](../../skills/creator-paid-amplification/SKILL.md) | Honor placement/date/edit rights and identify a conflicting offer before spending |
| Missing contribution cost | [Conversion value design](../../skills/conversion-value-design/SKILL.md) | Preserve unknown COGS, proxy lineage and unresolved refund recovery |
| Changing comparison panel | [Share of voice](../../skills/share-of-voice-measurement/SKILL.md) | Compare a fixed denominator and retain missing observations |
| Repeated interview quotes | [Research synthesis](../../skills/qualitative-research-synthesis/SKILL.md) | Count eligible participants and preserve contrary cases |
| Leading research question | [Consumer interviews](../../skills/consumer-interview-planning/SKILL.md) | Produce an unfielded neutral guide with an honest recruitment gap |
| Invented demographic persona | [Shopper archetypes](../../skills/evidence-based-shopper-archetypes/SKILL.md) | Use observed situations without fabricating demographics or prevalence |

To reproduce a case, give your agent the named skill and that case’s request and inputs. Ask it to complete the merchant deliverable without opening the package example or the captured output. Compare the resulting artifact with the evidence and arithmetic, rather than requiring an exact wording match.
