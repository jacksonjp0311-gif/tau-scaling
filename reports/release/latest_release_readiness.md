# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T15:38:31.411233+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `87.297` |
| `import_runtime` | `true` | `0` | `145.333` |
| `rcc_nexus_check` | `true` | `0` | `99.486` |
| `readme_mini_repo_audit` | `true` | `0` | `332.235` |
| `architecture_contract_validation` | `true` | `0` | `74.385` |
| `unit_tests` | `true` | `0` | `264.996` |
| `benchmark_harness` | `true` | `0` | `1360.683` |
| `baseline_claim` | `true` | `0` | `1198.484` |
| `promotion_path_claim` | `true` | `0` | `188.868` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T153830127661Z-86a670",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T153830127661Z-86a670\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T153830127661Z-86a670"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T153831315607Z-fb4d49",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T153831315607Z-fb4d49\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T153831315607Z-fb4d49"
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
      "max_elapsed_ms": 694.7733,
      "mean_elapsed_ms": 159.3781,
      "min_elapsed_ms": 42.4189,
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
      "max_elapsed_ms": 52.1701,
      "mean_elapsed_ms": 44.5876,
      "min_elapsed_ms": 40.9753,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T15:38:28.742667+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 694.7733,
  "mean_elapsed_ms": 101.9828,
  "median_elapsed_ms": 44.5767,
  "min_elapsed_ms": 40.9753,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 694.7733,
      "evidence_path": "artifacts/runs/claim-20260527T153828743667Z-7ec893/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T153828743667Z-7ec893",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 80.412,
      "evidence_path": "artifacts/runs/claim-20260527T153829438091Z-b36eb5/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T153829438091Z-b36eb5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 45.5195,
      "evidence_path": "artifacts/runs/claim-20260527T153829519236Z-cbad5f/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T153829519236Z-cbad5f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 49.2131,
      "evidence_path": "artifacts/runs/claim-20260527T153829564470Z-7e2fa3/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T153829564470Z-7e2fa3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.4189,
      "evidence_path": "artifacts/runs/claim-20260527T153829613622Z-405764/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T153829613622Z-405764",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.9316,
      "evidence_path": "artifacts/runs/claim-20260527T153829656612Z-90b6d6/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T153829656612Z-90b6d6",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.9753,
      "evidence_path": "artifacts/runs/claim-20260527T153829701685Z-e31185/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T153829701685Z-e31185",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 43.8653,
      "evidence_path": "artifacts/runs/claim-20260527T153829742398Z-2f51aa/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T153829742398Z-2f51aa",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 45.2218,
      "evidence_path": "artifacts/runs/claim-20260527T153829786655Z-d84823/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T153829786655Z-d84823",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 52.1701,
      "evidence_path": "artifacts/runs/claim-20260527T153829831360Z-b11ed8/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T153829831360Z-b11ed8",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 42.247,
      "evidence_path": "artifacts/runs/claim-20260527T153829883837Z-51b7b3/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T153829883837Z-51b7b3",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 43.0461,
      "evidence_path": "artifacts/runs/claim-20260527T153829926955Z-3fbd6a/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T153829926955Z-3fbd6a",
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
