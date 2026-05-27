# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T14:40:05.704783+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `85.901` |
| `import_runtime` | `true` | `0` | `127.976` |
| `rcc_nexus_check` | `true` | `0` | `105.828` |
| `readme_mini_repo_audit` | `true` | `0` | `101.709` |
| `architecture_contract_validation` | `true` | `0` | `73.912` |
| `unit_tests` | `true` | `0` | `240.291` |
| `benchmark_harness` | `true` | `0` | `600.357` |
| `baseline_claim` | `true` | `0` | `176.236` |
| `promotion_path_claim` | `true` | `0` | `175.398` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T144005443413Z-b518c8",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T144005443413Z-b518c8\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T144005443413Z-b518c8"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T144005618614Z-19dfd3",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T144005618614Z-19dfd3\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T144005618614Z-19dfd3"
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
      "max_elapsed_ms": 47.538,
      "mean_elapsed_ms": 39.7752,
      "min_elapsed_ms": 35.939,
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
      "max_elapsed_ms": 39.933,
      "mean_elapsed_ms": 36.9875,
      "min_elapsed_ms": 35.3673,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T14:40:04.839797+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 47.538,
  "mean_elapsed_ms": 38.3813,
  "median_elapsed_ms": 37.2211,
  "min_elapsed_ms": 35.3673,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.538,
      "evidence_path": "artifacts/runs/claim-20260527T144004839797Z-d99557/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T144004839797Z-d99557",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.4724,
      "evidence_path": "artifacts/runs/claim-20260527T144004887648Z-d20128/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T144004887648Z-d20128",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.2597,
      "evidence_path": "artifacts/runs/claim-20260527T144004929429Z-576641/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T144004929429Z-576641",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.8481,
      "evidence_path": "artifacts/runs/claim-20260527T144004968797Z-767398/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T144004968797Z-767398",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.939,
      "evidence_path": "artifacts/runs/claim-20260527T144005005860Z-76dffc/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T144005005860Z-76dffc",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.5941,
      "evidence_path": "artifacts/runs/claim-20260527T144005041064Z-b5ff3f/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T144005041064Z-b5ff3f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.8503,
      "evidence_path": "artifacts/runs/claim-20260527T144005079802Z-883c80/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T144005079802Z-883c80",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.6975,
      "evidence_path": "artifacts/runs/claim-20260527T144005115055Z-7e335b/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T144005115055Z-7e335b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.4307,
      "evidence_path": "artifacts/runs/claim-20260527T144005152778Z-ee801b/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T144005152778Z-ee801b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.6461,
      "evidence_path": "artifacts/runs/claim-20260527T144005189412Z-6c84b1/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T144005189412Z-6c84b1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.933,
      "evidence_path": "artifacts/runs/claim-20260527T144005227334Z-6a3af5/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T144005227334Z-6a3af5",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.3673,
      "evidence_path": "artifacts/runs/claim-20260527T144005266981Z-c51ae3/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T144005266981Z-c51ae3",
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
