# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T14:52:25.615003+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `75.546` |
| `import_runtime` | `true` | `0` | `106.703` |
| `rcc_nexus_check` | `true` | `0` | `90.867` |
| `readme_mini_repo_audit` | `true` | `0` | `101.139` |
| `architecture_contract_validation` | `true` | `0` | `72.805` |
| `unit_tests` | `true` | `0` | `224.902` |
| `benchmark_harness` | `true` | `0` | `596.926` |
| `baseline_claim` | `true` | `0` | `165.272` |
| `promotion_path_claim` | `true` | `0` | `173.519` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T145225360883Z-f67872",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T145225360883Z-f67872\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T145225360883Z-f67872"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T145225530982Z-a75d66",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T145225530982Z-a75d66\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T145225530982Z-a75d66"
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
      "max_elapsed_ms": 42.7929,
      "mean_elapsed_ms": 39.7736,
      "min_elapsed_ms": 37.3936,
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
      "max_elapsed_ms": 38.35,
      "mean_elapsed_ms": 36.3638,
      "min_elapsed_ms": 34.3155,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T14:52:24.770151+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 42.7929,
  "mean_elapsed_ms": 38.0687,
  "median_elapsed_ms": 37.7884,
  "min_elapsed_ms": 34.3155,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.4238,
      "evidence_path": "artifacts/runs/claim-20260526T145224770151Z-d11ceb/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T145224770151Z-d11ceb",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.1831,
      "evidence_path": "artifacts/runs/claim-20260526T145224812287Z-8f126e/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T145224812287Z-8f126e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.2591,
      "evidence_path": "artifacts/runs/claim-20260526T145224850157Z-2c108a/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T145224850157Z-2c108a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.5893,
      "evidence_path": "artifacts/runs/claim-20260526T145224888568Z-16caec/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T145224888568Z-16caec",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.3936,
      "evidence_path": "artifacts/runs/claim-20260526T145224928866Z-0281d8/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T145224928866Z-0281d8",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.7929,
      "evidence_path": "artifacts/runs/claim-20260526T145224967395Z-fc5823/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T145224967395Z-fc5823",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.35,
      "evidence_path": "artifacts/runs/claim-20260526T145225010346Z-8758fc/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T145225010346Z-8758fc",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.3524,
      "evidence_path": "artifacts/runs/claim-20260526T145225048616Z-d4bd8b/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T145225048616Z-d4bd8b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.696,
      "evidence_path": "artifacts/runs/claim-20260526T145225085951Z-4bb670/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T145225085951Z-4bb670",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.4849,
      "evidence_path": "artifacts/runs/claim-20260526T145225122886Z-f28975/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T145225122886Z-f28975",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.3155,
      "evidence_path": "artifacts/runs/claim-20260526T145225158671Z-f8238c/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T145225158671Z-f8238c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.9838,
      "evidence_path": "artifacts/runs/claim-20260526T145225192921Z-1568ff/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T145225192921Z-1568ff",
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
