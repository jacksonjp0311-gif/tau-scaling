# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T16:37:29.012620+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `91.05` |
| `import_runtime` | `true` | `0` | `143.61` |
| `rcc_nexus_check` | `true` | `0` | `97.827` |
| `readme_mini_repo_audit` | `true` | `0` | `124.375` |
| `architecture_contract_validation` | `true` | `0` | `81.577` |
| `unit_tests` | `true` | `0` | `258.755` |
| `benchmark_harness` | `true` | `0` | `691.568` |
| `baseline_claim` | `true` | `0` | `219.811` |
| `promotion_path_claim` | `true` | `0` | `176.07` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T163728738603Z-407287",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T163728738603Z-407287\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T163728738603Z-407287"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T163728922897Z-859c12",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T163728922897Z-859c12\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T163728922897Z-859c12"
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
      "max_elapsed_ms": 55.4493,
      "mean_elapsed_ms": 44.9911,
      "min_elapsed_ms": 38.2175,
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
      "max_elapsed_ms": 46.2931,
      "mean_elapsed_ms": 40.8469,
      "min_elapsed_ms": 38.1054,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T16:37:28.044932+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 55.4493,
  "mean_elapsed_ms": 42.919,
  "median_elapsed_ms": 40.9262,
  "min_elapsed_ms": 38.1054,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 51.2556,
      "evidence_path": "artifacts/runs/claim-20260528T163728044932Z-629f00/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T163728044932Z-629f00",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.8848,
      "evidence_path": "artifacts/runs/claim-20260528T163728097217Z-490a98/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T163728097217Z-490a98",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.2175,
      "evidence_path": "artifacts/runs/claim-20260528T163728136742Z-90ddcc/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T163728136742Z-90ddcc",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.9677,
      "evidence_path": "artifacts/runs/claim-20260528T163728175388Z-f21f1e/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T163728175388Z-f21f1e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 55.4493,
      "evidence_path": "artifacts/runs/claim-20260528T163728217233Z-25169f/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T163728217233Z-25169f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.1719,
      "evidence_path": "artifacts/runs/claim-20260528T163728272930Z-0a16a4/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T163728272930Z-0a16a4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 46.2931,
      "evidence_path": "artifacts/runs/claim-20260528T163728316545Z-4b545e/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T163728316545Z-4b545e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 44.0869,
      "evidence_path": "artifacts/runs/claim-20260528T163728363139Z-f24bf4/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T163728363139Z-f24bf4",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.2344,
      "evidence_path": "artifacts/runs/claim-20260528T163728407129Z-044033/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T163728407129Z-044033",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.0501,
      "evidence_path": "artifacts/runs/claim-20260528T163728447187Z-5211f6/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T163728447187Z-5211f6",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.1054,
      "evidence_path": "artifacts/runs/claim-20260528T163728486227Z-fdd3c7/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T163728486227Z-fdd3c7",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.3115,
      "evidence_path": "artifacts/runs/claim-20260528T163728524425Z-e90725/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T163728524425Z-e90725",
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
