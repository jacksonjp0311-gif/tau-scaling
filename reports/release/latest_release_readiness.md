# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T07:46:03.218363+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `76.01` |
| `import_runtime` | `true` | `0` | `112.324` |
| `rcc_nexus_check` | `true` | `0` | `92.701` |
| `readme_mini_repo_audit` | `true` | `0` | `86.793` |
| `architecture_contract_validation` | `true` | `0` | `67.587` |
| `unit_tests` | `true` | `0` | `216.037` |
| `benchmark_harness` | `true` | `0` | `602.259` |
| `baseline_claim` | `true` | `0` | `195.781` |
| `promotion_path_claim` | `true` | `0` | `200.631` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074602924144Z-250e2a",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074602924144Z-250e2a\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T074602924144Z-250e2a"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074603135721Z-da4fa6",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074603135721Z-da4fa6\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T074603135721Z-da4fa6"
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
      "max_elapsed_ms": 48.681,
      "mean_elapsed_ms": 39.9213,
      "min_elapsed_ms": 35.2979,
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
      "max_elapsed_ms": 38.4535,
      "mean_elapsed_ms": 37.0712,
      "min_elapsed_ms": 35.5569,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T07:46:02.305169+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 48.681,
  "mean_elapsed_ms": 38.4962,
  "median_elapsed_ms": 37.2947,
  "min_elapsed_ms": 35.2979,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.1368,
      "evidence_path": "artifacts/runs/claim-20260528T074602306444Z-f9c98f/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T074602306444Z-f9c98f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.8618,
      "evidence_path": "artifacts/runs/claim-20260528T074602349738Z-1bf6fb/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T074602349738Z-1bf6fb",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.2979,
      "evidence_path": "artifacts/runs/claim-20260528T074602385868Z-760124/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T074602385868Z-760124",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 48.681,
      "evidence_path": "artifacts/runs/claim-20260528T074602421796Z-3f3870/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T074602421796Z-3f3870",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.0173,
      "evidence_path": "artifacts/runs/claim-20260528T074602469770Z-3b2b74/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T074602469770Z-3b2b74",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.533,
      "evidence_path": "artifacts/runs/claim-20260528T074602508761Z-35ee95/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T074602508761Z-35ee95",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.0564,
      "evidence_path": "artifacts/runs/claim-20260528T074602546826Z-a78368/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T074602546826Z-a78368",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.4535,
      "evidence_path": "artifacts/runs/claim-20260528T074602583601Z-797532/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T074602583601Z-797532",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.9381,
      "evidence_path": "artifacts/runs/claim-20260528T074602621955Z-5b050d/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T074602621955Z-5b050d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.8562,
      "evidence_path": "artifacts/runs/claim-20260528T074602659976Z-6fe9a2/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T074602659976Z-6fe9a2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.5659,
      "evidence_path": "artifacts/runs/claim-20260528T074602697512Z-8b63db/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T074602697512Z-8b63db",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.5569,
      "evidence_path": "artifacts/runs/claim-20260528T074602734485Z-245605/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T074602734485Z-245605",
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
