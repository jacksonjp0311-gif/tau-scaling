# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T08:12:47.938076+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `68.188` |
| `import_runtime` | `true` | `0` | `103.12` |
| `rcc_nexus_check` | `true` | `0` | `85.243` |
| `readme_mini_repo_audit` | `true` | `0` | `81.512` |
| `architecture_contract_validation` | `true` | `0` | `60.477` |
| `unit_tests` | `true` | `0` | `232.867` |
| `benchmark_harness` | `true` | `0` | `561.641` |
| `baseline_claim` | `true` | `0` | `166.946` |
| `promotion_path_claim` | `true` | `0` | `161.601` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T081247691582Z-bdb7ad",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T081247691582Z-bdb7ad\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T081247691582Z-bdb7ad"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T081247858817Z-bc2b18",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T081247858817Z-bc2b18\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T081247858817Z-bc2b18"
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
      "max_elapsed_ms": 41.3503,
      "mean_elapsed_ms": 36.6485,
      "min_elapsed_ms": 34.5444,
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
      "max_elapsed_ms": 38.0879,
      "mean_elapsed_ms": 36.5856,
      "min_elapsed_ms": 34.7096,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T08:12:47.117662+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 41.3503,
  "mean_elapsed_ms": 36.617,
  "median_elapsed_ms": 36.51,
  "min_elapsed_ms": 34.5444,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.3503,
      "evidence_path": "artifacts/runs/claim-20260528T081247118665Z-89ed57/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T081247118665Z-89ed57",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.9286,
      "evidence_path": "artifacts/runs/claim-20260528T081247159601Z-89da39/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T081247159601Z-89da39",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.6276,
      "evidence_path": "artifacts/runs/claim-20260528T081247197138Z-6d6d83/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T081247197138Z-6d6d83",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.4477,
      "evidence_path": "artifacts/runs/claim-20260528T081247233151Z-92e47d/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T081247233151Z-92e47d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.9923,
      "evidence_path": "artifacts/runs/claim-20260528T081247269503Z-317144/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T081247269503Z-317144",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.5444,
      "evidence_path": "artifacts/runs/claim-20260528T081247304645Z-f49495/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T081247304645Z-f49495",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.7096,
      "evidence_path": "artifacts/runs/claim-20260528T081247339085Z-d39789/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T081247339085Z-d39789",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.0879,
      "evidence_path": "artifacts/runs/claim-20260528T081247374160Z-35f3a3/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T081247374160Z-35f3a3",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.3925,
      "evidence_path": "artifacts/runs/claim-20260528T081247412867Z-7ba254/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T081247412867Z-7ba254",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.7149,
      "evidence_path": "artifacts/runs/claim-20260528T081247449262Z-cc5a2e/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T081247449262Z-cc5a2e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.1594,
      "evidence_path": "artifacts/runs/claim-20260528T081247487115Z-8ed7a5/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T081247487115Z-8ed7a5",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.4493,
      "evidence_path": "artifacts/runs/claim-20260528T081247523883Z-6eef41/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T081247523883Z-6eef41",
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
