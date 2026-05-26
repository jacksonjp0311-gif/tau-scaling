# Tau Scaling Process Alignment Protocol

Generated: 2026-05-26T11:25:45Z

## Purpose

This protocol prevents repository drift after each Tau Scaling evolution step.

## Required Promotion Sequence

1. Patch the intended runtime/documentation/report surface.
2. Update the root README checkpoint, metrics, release lineage, and next target.
3. Update affected mini READMEs and route maps when directory meaning changes.
4. Run `python scripts/release/validate_release.py`.
5. Inspect warnings even when `passed: true`.
6. Run `python scripts/rcc/audit_readme_surface.py`.
7. Run `python -m unittest discover -s tests`.
8. Commit only after validator, README audit, and tests pass.
9. Push only after the README public state matches the actual repo state.

## Hard Rules

- A release is not aligned if README still points to the previous next version.
- A release is not aligned if the Full Directory Box contains duplicate durable entries.
- A release is not aligned if validator warnings are ignored.
- A release is not aligned if public claims imply silicon/product validation.
- Large repair scripts must be run as files, not pasted line by line.

## Non-Claim Lock

Process alignment improves repository hygiene and experiment discipline. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
