# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T15:16:20.065206+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `76.333` |
| `import_runtime` | `true` | `0` | `122.408` |
| `rcc_nexus_check` | `true` | `0` | `73.283` |
| `readme_mini_repo_audit` | `true` | `0` | `91.792` |
| `architecture_contract_validation` | `true` | `0` | `71.421` |
| `unit_tests` | `true` | `0` | `231.733` |
| `benchmark_harness` | `true` | `0` | `560.792` |
| `baseline_claim` | `true` | `0` | `168.997` |
| `promotion_path_claim` | `true` | `0` | `171.409` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T151619806143Z-565665",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T151619806143Z-565665\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T151619806143Z-565665"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T151619976779Z-e8d524",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T151619976779Z-e8d524\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T151619976779Z-e8d524"
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
      "max_elapsed_ms": 40.1103,
      "mean_elapsed_ms": 37.4862,
      "min_elapsed_ms": 35.5447,
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
      "max_elapsed_ms": 37.0281,
      "mean_elapsed_ms": 35.8185,
      "min_elapsed_ms": 34.8902,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T15:16:19.229228+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 40.1103,
  "mean_elapsed_ms": 36.6523,
  "median_elapsed_ms": 36.0408,
  "min_elapsed_ms": 34.8902,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.1103,
      "evidence_path": "artifacts/runs/claim-20260526T151619230230Z-19082e/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T151619230230Z-19082e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.9442,
      "evidence_path": "artifacts/runs/claim-20260526T151619270221Z-cca2dd/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T151619270221Z-cca2dd",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.5447,
      "evidence_path": "artifacts/runs/claim-20260526T151619307729Z-612fc4/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T151619307729Z-612fc4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.7351,
      "evidence_path": "artifacts/runs/claim-20260526T151619342690Z-b7c621/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T151619342690Z-b7c621",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.9,
      "evidence_path": "artifacts/runs/claim-20260526T151619382836Z-b5ceb2/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T151619382836Z-b5ceb2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.6831,
      "evidence_path": "artifacts/runs/claim-20260526T151619419326Z-8b6cf8/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T151619419326Z-8b6cf8",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.8902,
      "evidence_path": "artifacts/runs/claim-20260526T151619455906Z-4c352c/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T151619455906Z-4c352c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.6975,
      "evidence_path": "artifacts/runs/claim-20260526T151619490868Z-0734b1/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T151619490868Z-0734b1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.8876,
      "evidence_path": "artifacts/runs/claim-20260526T151619526651Z-c75402/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T151619526651Z-c75402",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.1817,
      "evidence_path": "artifacts/runs/claim-20260526T151619562651Z-585750/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T151619562651Z-585750",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.0281,
      "evidence_path": "artifacts/runs/claim-20260526T151619599583Z-bd1fe6/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T151619599583Z-bd1fe6",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.2257,
      "evidence_path": "artifacts/runs/claim-20260526T151619636436Z-94c2a6/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T151619636436Z-94c2a6",
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
