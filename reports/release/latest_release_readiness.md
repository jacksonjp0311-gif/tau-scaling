# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T13:00:20.542502+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `83.436` |
| `import_runtime` | `true` | `0` | `168.017` |
| `rcc_nexus_check` | `true` | `0` | `363.809` |
| `readme_mini_repo_audit` | `true` | `0` | `248.153` |
| `architecture_contract_validation` | `true` | `0` | `83.277` |
| `unit_tests` | `true` | `0` | `334.736` |
| `benchmark_harness` | `true` | `0` | `572.98` |
| `baseline_claim` | `true` | `0` | `165.85` |
| `promotion_path_claim` | `true` | `0` | `180.834` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T130020277269Z-9b5906",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T130020277269Z-9b5906\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T130020277269Z-9b5906"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T130020453834Z-f9ca37",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T130020453834Z-f9ca37\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T130020453834Z-f9ca37"
}
```

## Benchmark Summary

```json
{
  "boundary": "Benchmark timing and class stability are local-runtime diagnostics only. They are not silicon validation, product validation, or universal Tau Scaling proof.",
  "by_seed": {
    "configs/seeds/logicfolding_claim_card.json": {
      "A_TSEK_values": [
        0.0
      ],
      "classes": {
        "TSEK-C": 6
      },
      "findings_values": [
        1
      ],
      "max_elapsed_ms": 42.4596,
      "mean_elapsed_ms": 37.5956,
      "min_elapsed_ms": 34.3441,
      "runs": 6
    },
    "configs/seeds/logicfolding_promotion_path_claim_card.json": {
      "A_TSEK_values": [
        1.0
      ],
      "classes": {
        "TSEK-B": 6
      },
      "findings_values": [
        0
      ],
      "max_elapsed_ms": 35.1919,
      "mean_elapsed_ms": 34.3433,
      "min_elapsed_ms": 33.0958,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T13:00:19.706316+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 42.4596,
  "mean_elapsed_ms": 35.9694,
  "median_elapsed_ms": 35.0967,
  "min_elapsed_ms": 33.0958,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.4596,
      "evidence_path": "artifacts/runs/claim-20260526T130019706316Z-b662fa/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T130019706316Z-b662fa",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.7357,
      "evidence_path": "artifacts/runs/claim-20260526T130019749410Z-144af0/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T130019749410Z-144af0",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.0326,
      "evidence_path": "artifacts/runs/claim-20260526T130019785252Z-cd428b/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T130019785252Z-cd428b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.9482,
      "evidence_path": "artifacts/runs/claim-20260526T130019823401Z-1f2152/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T130019823401Z-1f2152",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.3441,
      "evidence_path": "artifacts/runs/claim-20260526T130019858790Z-ab63c4/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T130019858790Z-ab63c4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.0531,
      "evidence_path": "artifacts/runs/claim-20260526T130019893849Z-ed8f92/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T130019893849Z-ed8f92",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0015,
      "evidence_path": "artifacts/runs/claim-20260526T130019940519Z-cb9b9f/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T130019940519Z-cb9b9f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.0369,
      "evidence_path": "artifacts/runs/claim-20260526T130019975323Z-8f5dff/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T130019975323Z-8f5dff",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.8257,
      "evidence_path": "artifacts/runs/claim-20260526T130020009412Z-fa1bc6/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T130020009412Z-fa1bc6",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.1919,
      "evidence_path": "artifacts/runs/claim-20260526T130020045203Z-7c5f80/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T130020045203Z-7c5f80",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.9082,
      "evidence_path": "artifacts/runs/claim-20260526T130020079907Z-84d2b9/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T130020079907Z-84d2b9",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.0958,
      "evidence_path": "artifacts/runs/claim-20260526T130020114548Z-38105a/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T130020114548Z-38105a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    }
  ],
  "schema": "tau-scaling-benchmark-summary-v0.3.2",
  "total_runs": 12,
  "unique_run_ids": 12
}
```

## Findings

No findings.

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
