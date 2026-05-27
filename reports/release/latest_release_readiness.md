# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T17:56:47.621504+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `83.049` |
| `import_runtime` | `true` | `0` | `110.229` |
| `rcc_nexus_check` | `true` | `0` | `93.44` |
| `readme_mini_repo_audit` | `true` | `0` | `143.752` |
| `architecture_contract_validation` | `true` | `0` | `79.002` |
| `unit_tests` | `true` | `0` | `273.936` |
| `benchmark_harness` | `true` | `0` | `561.906` |
| `baseline_claim` | `true` | `0` | `166.098` |
| `promotion_path_claim` | `true` | `0` | `160.043` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175647378675Z-f5dde1",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175647378675Z-f5dde1\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T175647378675Z-f5dde1"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175647535756Z-8be742",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175647535756Z-8be742\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T175647535756Z-8be742"
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
      "max_elapsed_ms": 40.9838,
      "mean_elapsed_ms": 36.265,
      "min_elapsed_ms": 33.8936,
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
      "max_elapsed_ms": 39.2707,
      "mean_elapsed_ms": 35.6648,
      "min_elapsed_ms": 34.204,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T17:56:46.809014+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 40.9838,
  "mean_elapsed_ms": 35.9649,
  "median_elapsed_ms": 35.0614,
  "min_elapsed_ms": 33.8936,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.9838,
      "evidence_path": "artifacts/runs/claim-20260527T175646809014Z-bd0dfc/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T175646809014Z-bd0dfc",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.9338,
      "evidence_path": "artifacts/runs/claim-20260527T175646850234Z-861f8e/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T175646850234Z-861f8e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.591,
      "evidence_path": "artifacts/runs/claim-20260527T175646885114Z-67d54d/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T175646885114Z-67d54d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.8936,
      "evidence_path": "artifacts/runs/claim-20260527T175646920874Z-dea2d4/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T175646920874Z-dea2d4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.999,
      "evidence_path": "artifacts/runs/claim-20260527T175646954744Z-e62a24/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T175646954744Z-e62a24",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.189,
      "evidence_path": "artifacts/runs/claim-20260527T175646992136Z-4d3333/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T175646992136Z-4d3333",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.461,
      "evidence_path": "artifacts/runs/claim-20260527T175647028180Z-142f2d/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T175647028180Z-142f2d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.5836,
      "evidence_path": "artifacts/runs/claim-20260527T175647062083Z-b3c9da/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T175647062083Z-b3c9da",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.5714,
      "evidence_path": "artifacts/runs/claim-20260527T175647099368Z-a0aed2/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T175647099368Z-a0aed2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.898,
      "evidence_path": "artifacts/runs/claim-20260527T175647134427Z-6daf9d/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T175647134427Z-6daf9d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.204,
      "evidence_path": "artifacts/runs/claim-20260527T175647169597Z-a69c78/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T175647169597Z-a69c78",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.2707,
      "evidence_path": "artifacts/runs/claim-20260527T175647203676Z-3a0759/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T175647203676Z-3a0759",
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
