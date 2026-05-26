# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T13:13:44.712606+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `79.844` |
| `import_runtime` | `true` | `0` | `109.456` |
| `rcc_nexus_check` | `true` | `0` | `82.356` |
| `readme_mini_repo_audit` | `true` | `0` | `89.049` |
| `architecture_contract_validation` | `true` | `0` | `66.699` |
| `unit_tests` | `true` | `0` | `231.138` |
| `benchmark_harness` | `true` | `0` | `596.247` |
| `baseline_claim` | `true` | `0` | `185.125` |
| `promotion_path_claim` | `true` | `0` | `191.663` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T131344435686Z-768966",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T131344435686Z-768966\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T131344435686Z-768966"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T131344632330Z-d7db9d",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T131344632330Z-d7db9d\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T131344632330Z-d7db9d"
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
      "max_elapsed_ms": 44.0232,
      "mean_elapsed_ms": 41.7332,
      "min_elapsed_ms": 39.2114,
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
      "max_elapsed_ms": 40.9105,
      "mean_elapsed_ms": 37.1339,
      "min_elapsed_ms": 35.5134,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T13:13:43.810794+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 44.0232,
  "mean_elapsed_ms": 39.4335,
  "median_elapsed_ms": 40.0609,
  "min_elapsed_ms": 35.5134,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.2042,
      "evidence_path": "artifacts/runs/claim-20260526T131343810794Z-35ea4a/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T131343810794Z-35ea4a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.2417,
      "evidence_path": "artifacts/runs/claim-20260526T131343852752Z-1930c1/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T131343852752Z-1930c1",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.492,
      "evidence_path": "artifacts/runs/claim-20260526T131343895168Z-fd3500/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T131343895168Z-fd3500",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.0232,
      "evidence_path": "artifacts/runs/claim-20260526T131343937474Z-704810/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T131343937474Z-704810",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.2266,
      "evidence_path": "artifacts/runs/claim-20260526T131343981425Z-be1248/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T131343981425Z-be1248",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.2114,
      "evidence_path": "artifacts/runs/claim-20260526T131344022550Z-8bfd5d/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T131344022550Z-8bfd5d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.2512,
      "evidence_path": "artifacts/runs/claim-20260526T131344062700Z-fdb9be/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T131344062700Z-fdb9be",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.9105,
      "evidence_path": "artifacts/runs/claim-20260526T131344099046Z-330c97/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T131344099046Z-330c97",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.9119,
      "evidence_path": "artifacts/runs/claim-20260526T131344139974Z-7dcde2/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T131344139974Z-7dcde2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.5134,
      "evidence_path": "artifacts/runs/claim-20260526T131344176789Z-16626d/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T131344176789Z-16626d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.4769,
      "evidence_path": "artifacts/runs/claim-20260526T131344213259Z-21ad3d/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T131344213259Z-21ad3d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.7393,
      "evidence_path": "artifacts/runs/claim-20260526T131344248597Z-79f196/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T131344248597Z-79f196",
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
