# TAU-SCALING-SA v0.3.2a — Runtime Import Repair

This patch repairs a malformed import introduced during the v0.3.2 collision-proof run identity and benchmark injection.

## Repair

src/tau_scaling/core/runtime.py now imports runtime dependencies on separate lines:

`python
from tau_scaling.evidence.package import emit_evidence_package
from tau_scaling.utils.run_identity import ensure_unique_run_dir, generate_run_id
`

## Validation

The repair script reruns:

`powershell
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python -m unittest discover -s tests
python scripts/benchmarks/run_tau_scaling_benchmarks.py
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_promotion_path_claim_card.json
`

## Non-claim lock

This is an implementation hygiene repair. It does not independently validate silicon, product metrics, manufacturing capability, benchmark superiority, process-node equivalence, or universal Tau Scaling law.