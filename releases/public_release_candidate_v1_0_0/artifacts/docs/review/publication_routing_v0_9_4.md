# Publication Routing v0.9.4

## Route Table

| Route | Status | Reason | Required before publish |
|---|---|---|---|
| GitHub Release | READY | Repository artifacts, release checks, manifests, reports, and non-claim locks are present. | tag release; attach release notes; link manuscript package |
| Technical Note | READY_WITH_BOUNDARY | Evidence-governance result is bounded and reproducible; should avoid validation claims. | shorten abstract; include table and limitation summary; state non-claim lock early |
| Gist Summary | READY | Gist can present the publishable finding and link the repo package. | include repo link; include result statement; include limitations |
| Preprint Draft | HOLD_FOR_REVIEW | Preprint should wait for external review because primary and independent confirmations are zero. | external review checklist complete; reviewer comments addressed; preprint framing audited |
| Claim Promotion / Technical Validation | BLOCKED | No primary-source confirmation and no independent confirmation in current state. | first-party evidence; independent reproduction; workload/baseline/energy/thermal/yield gates |

## Recommendation

Publish first as a GitHub release and/or technical note. Hold preprint submission until external review confirms that the non-claim locks and evidence boundary are clear.
