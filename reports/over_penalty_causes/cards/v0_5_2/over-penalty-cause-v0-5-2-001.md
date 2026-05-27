# over-penalty-cause-v0-5-2-001

- Gate pair: `B_baseline+B_tau`
- Primary cause: `high_diagnostic_support`
- Causes: `high_diagnostic_support, heuristic_over_sensitivity`
- Candidate status: `blocked_until_remediated`
- Mutation allowed: `False`
- Policy enforced: `False`

## Remediation

Add a secondary evidence-pressure test before downgrading high-support cases.

## Boundary

Cause cards are local classifier-governance diagnostics only.
