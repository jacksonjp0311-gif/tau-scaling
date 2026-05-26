# TAU-SCALING-SA v0.3.2f — README / Mini Repo Audit Visibility Repair

Generated: 2026-05-26T10:11:24Z

## Purpose

This patch force-repairs audit-visible README and mini README strings after v0.3.2d/v0.3.2e showed that placement-based insertion was too fragile.

## Repairs

- Appends exact root README anchor: AI Rule — Directory Box and Mini README Synchronization.
- Appends exact root README anchor: Public Non-Claim Locks.
- Appends exact visible validation commands.
- Restores all machine-readable lock IDs needed by RCC-N and README audit.
- Creates/patches mini READMEs that lacked audit guidance.

## Lesson Encoded

The audit scanner is behaving correctly. The repair strategy changed from fragile regex placement to explicit audit-visible appending.

## Non-Claim Lock

README / mini repo audit visibility repair improves context alignment. It is not runtime correctness proof, silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling proof.