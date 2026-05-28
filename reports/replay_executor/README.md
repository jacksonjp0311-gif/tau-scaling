# Replay Executor Reports

Current layer: **TAU-SCALING-SA v0.6.7 - Approval-Gated Replay Executor**

## Purpose

This folder stores approval-gated replay executor reports. The executor refuses to run when live approval handoff is invalid.

## Primary command

```powershell
python scripts/benchmarks/run_approval_gated_replay_executor.py
```

## README Update Rule

Update this mini README whenever replay executor schemas, execution rules, or approval gates change.

Boundary: replay executor reports are local classifier-governance execution-boundary artifacts only.
