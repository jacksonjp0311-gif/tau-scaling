# v0.4.5b Nexus Feedback Health Schema Alignment

## Purpose

This folder stores the schema-alignment repair for Nexus feedback health scoring.

## Repair

- Treat `findings: []` as zero findings.
- Treat `step_failures: []` as zero step failures.
- Derive sensitivity point count from `results` when `total_points` is absent.
- Emit health details explaining normalized inputs.

## README Update Rule

Update this mini README whenever feedback health scoring, schema normalization, or input report interpretation changes.

Boundary: feedback health schema alignment is repository self-observation only.
