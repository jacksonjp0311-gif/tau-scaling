# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T11:02:51.706200+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `1`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `78.256` |
| `import_runtime` | `true` | `0` | `110.798` |
| `rcc_nexus_check` | `true` | `0` | `73.73` |
| `readme_mini_repo_audit` | `true` | `0` | `88.719` |
| `architecture_contract_validation` | `true` | `0` | `65.776` |
| `unit_tests` | `true` | `0` | `223.877` |
| `benchmark_harness` | `true` | `0` | `594.36` |
| `baseline_claim` | `true` | `0` | `202.396` |
| `promotion_path_claim` | `true` | `0` | `159.84` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T110251450974Z-a78e3a",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T110251450974Z-a78e3a\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T110251450974Z-a78e3a"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T110251620810Z-261977",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T110251620810Z-261977\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T110251620810Z-261977"
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
      "max_elapsed_ms": 47.4835,
      "mean_elapsed_ms": 40.6697,
      "min_elapsed_ms": 35.9141,
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
      "max_elapsed_ms": 46.7367,
      "mean_elapsed_ms": 37.0335,
      "min_elapsed_ms": 34.0022,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T11:02:50.819149+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 47.4835,
  "mean_elapsed_ms": 38.8516,
  "median_elapsed_ms": 37.3618,
  "min_elapsed_ms": 34.0022,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.4835,
      "evidence_path": "artifacts/runs/claim-20260526T110250819149Z-a8fbc3/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T110250819149Z-a8fbc3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.883,
      "evidence_path": "artifacts/runs/claim-20260526T110250867136Z-1cd32e/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T110250867136Z-1cd32e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.1734,
      "evidence_path": "artifacts/runs/claim-20260526T110250906445Z-98e8a0/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T110250906445Z-98e8a0",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.0955,
      "evidence_path": "artifacts/runs/claim-20260526T110250944294Z-1400a9/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T110250944294Z-1400a9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.9141,
      "evidence_path": "artifacts/runs/claim-20260526T110250983919Z-c983ba/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T110250983919Z-c983ba",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.4689,
      "evidence_path": "artifacts/runs/claim-20260526T110251019899Z-e72fdc/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T110251019899Z-e72fdc",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 46.7367,
      "evidence_path": "artifacts/runs/claim-20260526T110251065222Z-e36d44/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T110251065222Z-e36d44",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.1994,
      "evidence_path": "artifacts/runs/claim-20260526T110251112106Z-6dd68c/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T110251112106Z-6dd68c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.8079,
      "evidence_path": "artifacts/runs/claim-20260526T110251147379Z-ee9190/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T110251147379Z-ee9190",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.0022,
      "evidence_path": "artifacts/runs/claim-20260526T110251182661Z-d81404/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T110251182661Z-d81404",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.9047,
      "evidence_path": "artifacts/runs/claim-20260526T110251216669Z-204d8b/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T110251216669Z-204d8b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.5502,
      "evidence_path": "artifacts/runs/claim-20260526T110251251725Z-3dc73e/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T110251251725Z-3dc73e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    }
  ],
  "schema": "tau-scaling-benchmark-summary-v0.3.2",
  "total_runs": 12,
  "unique_run_ids": 12
}
```

## Findings

| Severity | Code | Path | Detail |
|---|---|---|---|
| warning | `possible_mojibake_or_path_break` | `README.md` | Found token:   |

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
