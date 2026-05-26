# reports/benchmarks

RCC Nexus Echo Location:
- Shell: outer
- Meridians: validation, evidence, release
- Sector: validation
- TTL: 180 days

Purpose:
- Stores benchmark summaries emitted by `scripts/benchmarks/run_tau_scaling_benchmarks.py`.

Current primary files:
- `latest_benchmark_summary.json`
- `latest_benchmark_summary.md`
- `tau_scaling_v0_3_2_benchmark_summary.json`
- `tau_scaling_v0_3_2_benchmark_summary.md`

Boundary:
- Benchmark reports are local-runtime diagnostics only.
- They are not silicon validation, product validation, manufacturing validation, or universal-law proof.


## AI Failure Learning Note

If a patch touching this folder fails validation, record the reusable lesson in the root README `AI Failure Learning Ledger` and update this mini README when the local rule changes.

Minimum repair discipline:

```powershell
python -m py_compile src/tau_scaling/core/runtime.py
python -c "from tau_scaling.core.runtime import TauScalingRuntime; print('TauScalingRuntime import OK')"
python -m unittest discover -s tests
python scripts/benchmarks/run_tau_scaling_benchmarks.py
```

Boundary: passing local runtime checks improves repository confidence but does not validate silicon, product performance, manufacturing capability, process-node equivalence, or a universal Tau Scaling law.

## README / Mini Repo Audit Rule

This folder participates in the repository-wide README + mini repo audit.

When this folder changes, an AI or human maintainer must check:

- root `README.md`
- this folder `README.md`
- nearest parent folder `README.md`
- `docs/context/repository_context_index.json` if route meaning changes
- `docs/context/rcc_nexus_index.json` if Nexus position changes
- `rcc/nexus/route_map.json` if task routing changes

Audit command:

```powershell
python scripts/rcc/audit_readme_surface.py
```

Non-claim lock: README audit alignment is not runtime correctness or silicon validation.
