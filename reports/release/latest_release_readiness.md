# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T14:56:34.896939+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `79.749` |
| `import_runtime` | `true` | `0` | `126.8` |
| `rcc_nexus_check` | `true` | `0` | `93.843` |
| `readme_mini_repo_audit` | `true` | `0` | `94.322` |
| `architecture_contract_validation` | `true` | `0` | `68.584` |
| `unit_tests` | `true` | `0` | `213.176` |
| `benchmark_harness` | `true` | `0` | `533.835` |
| `baseline_claim` | `true` | `0` | `164.679` |
| `promotion_path_claim` | `true` | `0` | `157.081` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T145634655371Z-35b2b4",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T145634655371Z-35b2b4\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T145634655371Z-35b2b4"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T145634813308Z-ce2f9f",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T145634813308Z-ce2f9f\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T145634813308Z-ce2f9f"
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
      "max_elapsed_ms": 38.5081,
      "mean_elapsed_ms": 35.2524,
      "min_elapsed_ms": 33.5044,
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
      "max_elapsed_ms": 36.1063,
      "mean_elapsed_ms": 34.4426,
      "min_elapsed_ms": 32.0329,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T14:56:34.101529+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 38.5081,
  "mean_elapsed_ms": 34.8475,
  "median_elapsed_ms": 34.994,
  "min_elapsed_ms": 32.0329,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.5081,
      "evidence_path": "artifacts/runs/claim-20260526T145634102529Z-8bdd2d/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T145634102529Z-8bdd2d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.3315,
      "evidence_path": "artifacts/runs/claim-20260526T145634140493Z-8597a6/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T145634140493Z-8597a6",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1091,
      "evidence_path": "artifacts/runs/claim-20260526T145634176178Z-af6343/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T145634176178Z-af6343",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.5044,
      "evidence_path": "artifacts/runs/claim-20260526T145634211169Z-7b45b1/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T145634211169Z-7b45b1",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.9466,
      "evidence_path": "artifacts/runs/claim-20260526T145634245073Z-919b5c/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T145634245073Z-919b5c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1146,
      "evidence_path": "artifacts/runs/claim-20260526T145634279763Z-5d020f/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T145634279763Z-5d020f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.0329,
      "evidence_path": "artifacts/runs/claim-20260526T145634314977Z-2e7e2e/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T145634314977Z-2e7e2e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.2061,
      "evidence_path": "artifacts/runs/claim-20260526T145634346961Z-ebe42c/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T145634346961Z-ebe42c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.058,
      "evidence_path": "artifacts/runs/claim-20260526T145634380703Z-91d1a0/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T145634380703Z-91d1a0",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.8789,
      "evidence_path": "artifacts/runs/claim-20260526T145634416910Z-e42a0f/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T145634416910Z-e42a0f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.3732,
      "evidence_path": "artifacts/runs/claim-20260526T145634452086Z-b1757f/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T145634452086Z-b1757f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.1063,
      "evidence_path": "artifacts/runs/claim-20260526T145634486693Z-69bb3b/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T145634486693Z-69bb3b",
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
