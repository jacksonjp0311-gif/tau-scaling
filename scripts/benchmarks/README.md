# scripts/benchmarks

RCC Nexus Echo Location:
- Shell: middle
- Meridians: validation, evidence, runtime, benchmark
- Sector: validation
- TTL: 180 days

Purpose:
- Stores local benchmark harnesses for Tau Scaling runtime behavior.
- Current harness: `run_tau_scaling_benchmarks.py`.

Validation:
```powershell
python scripts/benchmarks/run_tau_scaling_benchmarks.py
```

Boundary:
- Benchmarks here measure local runtime stability, class consistency, and run identity behavior.
- They do not validate silicon, product performance, manufacturing claims, process-node equivalence, or universal Tau Scaling law.

AI update rule:
- If benchmark scripts change, update this README, the root README directory box if routes change, `docs/benchmarks/current_public_metrics.md`, and the latest benchmark report.