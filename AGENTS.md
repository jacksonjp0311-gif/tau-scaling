# AGENTS.md — Tau Scaling Agent Operating Contract

## Read order

1. README.md
2. README_90_SECONDS.md
3. docs/context/repository_context_index.json
4. docs/context/rcc_nexus_index.json
5. rcc/nexus/route_map.json
6. target folder README.md
7. relevant source/tests/evidence only

## Patch rule

Patch the smallest necessary surface. Do not make broad rewrites unless the task is a versioned architecture update.

## Validation rule

After README/RCC/RCC-N changes run:

    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py
    python -m unittest discover -s tests

After runtime changes also run:

    python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json

## Non-claim locks

- navigation_is_not_validation
- documentation_is_not_correctness
- simulation_is_not_silicon_validation
- density_equivalence_is_not_node_equivalence
- local_path_win_is_not_full_chip_win
- validation_remains_required