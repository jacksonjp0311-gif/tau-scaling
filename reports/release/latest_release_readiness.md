# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T07:49:48.279423+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `71.544` |
| `import_runtime` | `true` | `0` | `129.89` |
| `rcc_nexus_check` | `true` | `0` | `108.527` |
| `readme_mini_repo_audit` | `true` | `0` | `91.775` |
| `architecture_contract_validation` | `true` | `0` | `65.865` |
| `unit_tests` | `true` | `0` | `221.979` |
| `benchmark_harness` | `true` | `0` | `581.488` |
| `baseline_claim` | `true` | `0` | `161.562` |
| `promotion_path_claim` | `true` | `0` | `180.745` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074948004443Z-8ca4ed",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074948004443Z-8ca4ed\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T074948004443Z-8ca4ed"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074948192719Z-9d3310",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074948192719Z-9d3310\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T074948192719Z-9d3310"
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
      "max_elapsed_ms": 66.6227,
      "mean_elapsed_ms": 42.9227,
      "min_elapsed_ms": 34.337,
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
      "max_elapsed_ms": 35.9873,
      "mean_elapsed_ms": 33.8113,
      "min_elapsed_ms": 32.5572,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T07:49:47.424711+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 66.6227,
  "mean_elapsed_ms": 38.367,
  "median_elapsed_ms": 35.1621,
  "min_elapsed_ms": 32.5572,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.9623,
      "evidence_path": "artifacts/runs/claim-20260528T074947424711Z-d7aaea/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T074947424711Z-d7aaea",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.781,
      "evidence_path": "artifacts/runs/claim-20260528T074947466861Z-aa9724/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T074947466861Z-aa9724",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.4776,
      "evidence_path": "artifacts/runs/claim-20260528T074947505188Z-ae33d3/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T074947505188Z-ae33d3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.337,
      "evidence_path": "artifacts/runs/claim-20260528T074947543847Z-944ed2/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T074947543847Z-944ed2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 66.6227,
      "evidence_path": "artifacts/runs/claim-20260528T074947578962Z-a794c2/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T074947578962Z-a794c2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.3555,
      "evidence_path": "artifacts/runs/claim-20260528T074947645116Z-db67e2/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T074947645116Z-db67e2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.9873,
      "evidence_path": "artifacts/runs/claim-20260528T074947684019Z-0cb74c/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T074947684019Z-0cb74c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.9614,
      "evidence_path": "artifacts/runs/claim-20260528T074947719950Z-cdfc14/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T074947719950Z-cdfc14",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.7877,
      "evidence_path": "artifacts/runs/claim-20260528T074947754601Z-b7a315/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T074947754601Z-b7a315",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.5572,
      "evidence_path": "artifacts/runs/claim-20260528T074947787846Z-7a4db9/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T074947787846Z-7a4db9",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.6899,
      "evidence_path": "artifacts/runs/claim-20260528T074947820549Z-fc5f77/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T074947820549Z-fc5f77",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.8846,
      "evidence_path": "artifacts/runs/claim-20260528T074947855149Z-f79aae/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T074947855149Z-f79aae",
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
