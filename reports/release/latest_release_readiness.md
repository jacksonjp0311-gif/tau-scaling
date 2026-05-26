# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T15:02:35.376539+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `75.28` |
| `import_runtime` | `true` | `0` | `116.218` |
| `rcc_nexus_check` | `true` | `0` | `97.882` |
| `readme_mini_repo_audit` | `true` | `0` | `88.437` |
| `architecture_contract_validation` | `true` | `0` | `71.093` |
| `unit_tests` | `true` | `0` | `221.903` |
| `benchmark_harness` | `true` | `0` | `573.536` |
| `baseline_claim` | `true` | `0` | `176.411` |
| `promotion_path_claim` | `true` | `0` | `177.764` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T150235108591Z-ab5ada",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T150235108591Z-ab5ada\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T150235108591Z-ab5ada"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T150235289358Z-a4fd81",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T150235289358Z-a4fd81\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T150235289358Z-a4fd81"
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
      "max_elapsed_ms": 42.6216,
      "mean_elapsed_ms": 38.6392,
      "min_elapsed_ms": 36.9639,
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
      "max_elapsed_ms": 38.4022,
      "mean_elapsed_ms": 35.9915,
      "min_elapsed_ms": 34.7637,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T15:02:34.521194+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 42.6216,
  "mean_elapsed_ms": 37.3154,
  "median_elapsed_ms": 37.24,
  "min_elapsed_ms": 34.7637,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.6216,
      "evidence_path": "artifacts/runs/claim-20260526T150234521194Z-e8e1f7/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T150234521194Z-e8e1f7",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.8997,
      "evidence_path": "artifacts/runs/claim-20260526T150234563763Z-9c779d/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T150234563763Z-9c779d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.516,
      "evidence_path": "artifacts/runs/claim-20260526T150234601648Z-96c80e/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T150234601648Z-96c80e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.1593,
      "evidence_path": "artifacts/runs/claim-20260526T150234640055Z-414053/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T150234640055Z-414053",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.6749,
      "evidence_path": "artifacts/runs/claim-20260526T150234677897Z-72b41c/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T150234677897Z-72b41c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.9639,
      "evidence_path": "artifacts/runs/claim-20260526T150234717094Z-2b7ceb/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T150234717094Z-2b7ceb",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.3648,
      "evidence_path": "artifacts/runs/claim-20260526T150234754379Z-2812d0/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T150234754379Z-2812d0",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.2697,
      "evidence_path": "artifacts/runs/claim-20260526T150234791165Z-d191c1/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T150234791165Z-d191c1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.4022,
      "evidence_path": "artifacts/runs/claim-20260526T150234826658Z-bc3b28/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T150234826658Z-bc3b28",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.7637,
      "evidence_path": "artifacts/runs/claim-20260526T150234864884Z-b86dba/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T150234864884Z-b86dba",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.0128,
      "evidence_path": "artifacts/runs/claim-20260526T150234900113Z-996197/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T150234900113Z-996197",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.136,
      "evidence_path": "artifacts/runs/claim-20260526T150234936014Z-a549dd/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T150234936014Z-a549dd",
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
