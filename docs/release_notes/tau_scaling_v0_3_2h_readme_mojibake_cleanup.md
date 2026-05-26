# TAU-SCALING-SA v0.3.2h — README Mojibake Cleanup + Audit Surface Consolidation

Generated: 2026-05-26T10:18:36Z

## Purpose

This patch repairs mojibake/encoding drift in the public README after repeated Unicode and PowerShell patch passes.

## Repairs

- Rewrites the root README as clean UTF-8 markdown.
- Replaces corrupted arrows with ASCII `->`.
- Restores clean `rcc/` and `reports/` paths.
- Restores proper fenced code blocks.
- Preserves the exact Unicode audit anchor required by `scripts/rcc/audit_readme_surface.py`.
- Adds encoding drift as an explicit AI failure-learning class.
- Keeps public non-claim locks and machine-readable lock IDs visible.

## Lesson Encoded

The audit layer passed, but visual inspection showed public README mojibake. Therefore, repository health requires both machine audit and human-readable public surface quality.

## Non-Claim Lock

README cleanup improves public readability and context integrity. It is not runtime correctness proof, silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling proof.
