# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T13:48:56.203603+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `71.036` |
| `import_runtime` | `true` | `0` | `117.081` |
| `rcc_nexus_check` | `true` | `0` | `86.212` |
| `readme_mini_repo_audit` | `true` | `0` | `92.46` |
| `architecture_contract_validation` | `true` | `0` | `65.859` |
| `unit_tests` | `true` | `0` | `242.195` |
| `benchmark_harness` | `true` | `0` | `576.383` |
| `baseline_claim` | `true` | `0` | `153.014` |
| `promotion_path_claim` | `true` | `0` | `155.302` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T134855970770Z-e02d26",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T134855970770Z-e02d26\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T134855970770Z-e02d26"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T134856125389Z-bcbec3",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T134856125389Z-bcbec3\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T134856125389Z-bcbec3"
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
      "max_elapsed_ms": 42.3735,
      "mean_elapsed_ms": 38.6864,
      "min_elapsed_ms": 36.9198,
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
      "max_elapsed_ms": 37.5594,
      "mean_elapsed_ms": 35.9414,
      "min_elapsed_ms": 34.0629,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T13:48:55.399567+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 42.3735,
  "mean_elapsed_ms": 37.3139,
  "median_elapsed_ms": 37.4057,
  "min_elapsed_ms": 34.0629,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.3735,
      "evidence_path": "artifacts/runs/claim-20260528T134855399567Z-a2e1b9/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T134855399567Z-a2e1b9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.2125,
      "evidence_path": "artifacts/runs/claim-20260528T134855441907Z-5211b8/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T134855441907Z-5211b8",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.109,
      "evidence_path": "artifacts/runs/claim-20260528T134855479931Z-f48e0d/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T134855479931Z-f48e0d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.2164,
      "evidence_path": "artifacts/runs/claim-20260528T134855519118Z-72768f/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T134855519118Z-72768f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.9198,
      "evidence_path": "artifacts/runs/claim-20260528T134855557319Z-35b01a/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T134855557319Z-35b01a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.2873,
      "evidence_path": "artifacts/runs/claim-20260528T134855594613Z-11d638/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T134855594613Z-11d638",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.5594,
      "evidence_path": "artifacts/runs/claim-20260528T134855632649Z-51c62b/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T134855632649Z-51c62b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.6947,
      "evidence_path": "artifacts/runs/claim-20260528T134855670416Z-ecc621/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T134855670416Z-ecc621",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.2521,
      "evidence_path": "artifacts/runs/claim-20260528T134855707100Z-9390dc/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T134855707100Z-9390dc",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.3553,
      "evidence_path": "artifacts/runs/claim-20260528T134855743837Z-30b6d2/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T134855743837Z-30b6d2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.7243,
      "evidence_path": "artifacts/runs/claim-20260528T134855781020Z-7b1f44/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T134855781020Z-7b1f44",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.0629,
      "evidence_path": "artifacts/runs/claim-20260528T134855815156Z-aec5a3/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T134855815156Z-aec5a3",
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
