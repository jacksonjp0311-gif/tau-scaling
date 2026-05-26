# TAU-SCALING-SA v0.3.2b — Runtime Newline Repair

This patch repairs literal PowerShell newline residue introduced during v0.3.2 runtime patching.

## Repair

The invalid sequence:

`python
runs_base = self.repo_root / "artifacts" / "runs"
        run_id, run_dir = ensure_unique_run_dir(...)
`

is converted into valid Python lines.

## Validation

The repair verifies:

`powershell
python -m py_compile src/tau_scaling/core/runtime.py
python -c "from tau_scaling.core.runtime import TauScalingRuntime"
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python -m unittest discover -s tests
python scripts/benchmarks/run_tau_scaling_benchmarks.py
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_promotion_path_claim_card.json
`

## Non-claim lock

This repair is local runtime syntax hygiene and benchmark observability. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling proof.