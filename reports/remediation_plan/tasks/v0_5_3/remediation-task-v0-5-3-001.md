# remediation-task-v0-5-3-001

- Source card: `over-penalty-cause-v0-5-2-001`
- Gate pair: `B_baseline+B_tau`
- Remediation class: `support_aware_negative_control`
- Status: `planned_not_applied`
- Mutation allowed: `False`
- Policy enforced: `False`

## Action

Design a support-aware negative control before reconsidering downgrade pressure.

## Required Validation

- build disabled negative-control case
- compare downgrade pressure against high-support retention baseline
- rerun cause decomposition
- keep mutation_allowed false

## Boundary

Remediation tasks are local classifier-governance planning artifacts only.
