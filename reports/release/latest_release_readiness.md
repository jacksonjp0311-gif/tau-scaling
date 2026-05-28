# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T07:52:51.529265+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `90.805` |
| `import_runtime` | `true` | `0` | `129.228` |
| `rcc_nexus_check` | `true` | `0` | `100.353` |
| `readme_mini_repo_audit` | `true` | `0` | `90.927` |
| `architecture_contract_validation` | `true` | `0` | `67.274` |
| `unit_tests` | `true` | `0` | `234.254` |
| `benchmark_harness` | `true` | `0` | `622.851` |
| `baseline_claim` | `true` | `0` | `180.71` |
| `promotion_path_claim` | `true` | `0` | `188.273` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T075251251257Z-3385cc",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T075251251257Z-3385cc\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T075251251257Z-3385cc"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T075251430358Z-85ae80",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T075251430358Z-85ae80\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T075251430358Z-85ae80"
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
      "max_elapsed_ms": 48.624,
      "mean_elapsed_ms": 43.409,
      "min_elapsed_ms": 40.0937,
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
      "max_elapsed_ms": 40.6185,
      "mean_elapsed_ms": 38.8891,
      "min_elapsed_ms": 37.2583,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T07:52:50.612078+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 48.624,
  "mean_elapsed_ms": 41.1491,
  "median_elapsed_ms": 40.5414,
  "min_elapsed_ms": 37.2583,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.3882,
      "evidence_path": "artifacts/runs/claim-20260528T075250613119Z-11a3a2/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T075250613119Z-11a3a2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.4098,
      "evidence_path": "artifacts/runs/claim-20260528T075250657806Z-713b88/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T075250657806Z-713b88",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.0499,
      "evidence_path": "artifacts/runs/claim-20260528T075250699382Z-fa9a27/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T075250699382Z-fa9a27",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.8883,
      "evidence_path": "artifacts/runs/claim-20260528T075250741972Z-3d06d1/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T075250741972Z-3d06d1",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.0937,
      "evidence_path": "artifacts/runs/claim-20260528T075250784863Z-291e32/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T075250784863Z-291e32",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 48.624,
      "evidence_path": "artifacts/runs/claim-20260528T075250825713Z-9ee4b5/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T075250825713Z-9ee4b5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.4644,
      "evidence_path": "artifacts/runs/claim-20260528T075250873844Z-0a895d/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T075250873844Z-0a895d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.5058,
      "evidence_path": "artifacts/runs/claim-20260528T075250915683Z-9ad343/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T075250915683Z-9ad343",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.6185,
      "evidence_path": "artifacts/runs/claim-20260528T075250953336Z-b36cea/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T075250953336Z-b36cea",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.8511,
      "evidence_path": "artifacts/runs/claim-20260528T075250994092Z-360a2f/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T075250994092Z-360a2f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.2583,
      "evidence_path": "artifacts/runs/claim-20260528T075251032829Z-69a55b/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T075251032829Z-69a55b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.6367,
      "evidence_path": "artifacts/runs/claim-20260528T075251069624Z-034069/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T075251069624Z-034069",
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
