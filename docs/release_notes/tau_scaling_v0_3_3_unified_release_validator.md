# TAU-SCALING-SA v0.3.3 — Unified Release Validator

Generated: 2026-05-26T11:02:49Z

## Purpose

This patch adds a single authoritative release-readiness validator for Tau Scaling.

## Additions

- scripts/release/validate_release.py
- eports/release/latest_release_readiness.json
- eports/release/latest_release_readiness.md
- eports/release/README.md
- scripts/release/README.md

## Validation Scope

The validator runs:

1. Runtime compile check.
2. Runtime import check.
3. RCC-N checker.
4. README / mini repo audit.
5. Architecture contract validator.
6. Unit tests.
7. Benchmark harness.
8. Baseline claim.
9. Promotion-path claim.
10. Expected artifact checks.
11. README mojibake/path-break scan.

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.