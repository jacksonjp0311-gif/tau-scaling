# docs\benchmarks\README.md

Local orientation surface for this Tau Scaling repository folder.


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
