# TAU-SCALING-SA v0.3.2d — README + Mini Repo Audit Map

Generated: 2026-05-26T10:08:12Z

## Purpose

This patch adds an AI-facing audit map to the root README so agents know exactly where to scan for repository gaps before editing or declaring a patch complete.

## Additions

- Root README section: README + Mini Repo Audit Map
- Executable audit: scripts/rcc/audit_readme_surface.py
- Protocol: docs/protocols/readme_mini_repo_audit_protocol.md
- Audit outputs:
  - eports/readme/latest_readme_mini_repo_audit.json
  - eports/readme/latest_readme_mini_repo_audit.md
- Mini README audit rules in key folders.

## Lesson Encoded

The v0.3.2 syntax failures showed that RCC-N and architecture validation are necessary but not sufficient. The repo now separates context health, architecture health, syntax/import health, unit-test health, benchmark health, evidence identity health, and claim-boundary health.

## Non-Claim Lock

README and mini repo audits are context-alignment checks. They are not runtime correctness proof, silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling proof.