# v0.4.5d Nexus Feedback Chart-Path Health Repair

## Purpose

This folder stores the chart-path normalization repair for Nexus feedback health scoring.

## Cause

v0.4.5c repaired list-valued findings and step failures, but sensitivity health still failed because the persisted sensitivity JSON stores chart evidence under `chart_paths`, while the feedback scorer checked only top-level `chart_count`.

## Repair

- Derive sensitivity chart count from `chart_count` if present.
- Fall back to `len(chart_paths)` when `chart_count` is absent.
- Assert feedback health becomes `1.0`.

## README Update Rule

Update this mini README whenever sensitivity report schema or feedback health scoring changes.

Boundary: feedback health repair is repository self-observation only.
