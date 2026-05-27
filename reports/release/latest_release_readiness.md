# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T14:56:22.885781+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `125.191` |
| `import_runtime` | `true` | `0` | `148.763` |
| `rcc_nexus_check` | `true` | `0` | `397.249` |
| `readme_mini_repo_audit` | `true` | `0` | `243.835` |
| `architecture_contract_validation` | `true` | `0` | `106.65` |
| `unit_tests` | `true` | `0` | `335.175` |
| `benchmark_harness` | `true` | `0` | `863.616` |
| `baseline_claim` | `true` | `0` | `333.344` |
| `promotion_path_claim` | `true` | `0` | `713.936` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T145621972023Z-9d6dac",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T145621972023Z-9d6dac\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T145621972023Z-9d6dac"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T145622714527Z-bcb90a",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T145622714527Z-bcb90a\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T145622714527Z-bcb90a"
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
      "max_elapsed_ms": 61.5063,
      "mean_elapsed_ms": 48.6488,
      "min_elapsed_ms": 42.0495,
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
      "max_elapsed_ms": 149.0763,
      "mean_elapsed_ms": 66.3219,
      "min_elapsed_ms": 43.4394,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T14:56:21.069037+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 149.0763,
  "mean_elapsed_ms": 57.4854,
  "median_elapsed_ms": 50.1698,
  "min_elapsed_ms": 42.0495,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 50.3658,
      "evidence_path": "artifacts/runs/claim-20260527T145621070039Z-b8b3e4/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T145621070039Z-b8b3e4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 45.0316,
      "evidence_path": "artifacts/runs/claim-20260527T145621120703Z-7f3228/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T145621120703Z-7f3228",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 49.9738,
      "evidence_path": "artifacts/runs/claim-20260527T145621164665Z-1388a6/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T145621164665Z-1388a6",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 61.5063,
      "evidence_path": "artifacts/runs/claim-20260527T145621215185Z-65c53d/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T145621215185Z-65c53d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.9658,
      "evidence_path": "artifacts/runs/claim-20260527T145621277110Z-c96f74/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T145621277110Z-c96f74",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.0495,
      "evidence_path": "artifacts/runs/claim-20260527T145621320126Z-1b4a34/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T145621320126Z-1b4a34",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 44.0143,
      "evidence_path": "artifacts/runs/claim-20260527T145621362653Z-48e23f/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T145621362653Z-48e23f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 43.4394,
      "evidence_path": "artifacts/runs/claim-20260527T145621407663Z-2f09fa/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T145621407663Z-2f09fa",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 51.7165,
      "evidence_path": "artifacts/runs/claim-20260527T145621450873Z-0013c1/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T145621450873Z-0013c1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 56.4329,
      "evidence_path": "artifacts/runs/claim-20260527T145621502578Z-08db8a/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T145621502578Z-08db8a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 53.2522,
      "evidence_path": "artifacts/runs/claim-20260527T145621559783Z-85d9e6/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T145621559783Z-85d9e6",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 149.0763,
      "evidence_path": "artifacts/runs/claim-20260527T145621612486Z-02e963/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T145621612486Z-02e963",
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
