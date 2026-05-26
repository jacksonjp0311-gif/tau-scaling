# Reflection Documentation

Current layer: **TAU-SCALING-SA v0.4.0f - Coherence Reflection and Agent Contract Re-Sync**

## Purpose

This folder stores system reflection reports, lessons learned, improvement queues, and next-experiment framing.

## README Update Rule

This mini README must be updated whenever reflection reports, improvement queues, or experiment-planning surfaces change.

Required synchronized surfaces:

```text
README.md
AGENTS.md
rcc/nexus/task_routing_matrix.md
docs/reflection/
reports/reflection/
```

Required validation:

```powershell
python scripts/rcc/audit_readme_surface.py
python scripts/release/validate_release.py
```

Non-claim lock: reflection improves repository coherence only. It is not code correctness, silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
