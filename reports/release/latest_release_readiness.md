# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T11:10:07.366214+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `1`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `89.087` |
| `import_runtime` | `true` | `0` | `128.017` |
| `rcc_nexus_check` | `true` | `0` | `102.932` |
| `readme_mini_repo_audit` | `true` | `0` | `99.181` |
| `architecture_contract_validation` | `true` | `0` | `69.008` |
| `unit_tests` | `true` | `0` | `226.119` |
| `benchmark_harness` | `true` | `0` | `585.624` |
| `baseline_claim` | `true` | `0` | `199.35` |
| `promotion_path_claim` | `true` | `0` | `157.127` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T111007129024Z-eea5d5",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T111007129024Z-eea5d5\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T111007129024Z-eea5d5"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T111007288218Z-c1d630",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T111007288218Z-c1d630\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T111007288218Z-c1d630"
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
      "max_elapsed_ms": 54.5185,
      "mean_elapsed_ms": 41.9411,
      "min_elapsed_ms": 34.9769,
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
      "max_elapsed_ms": 36.364,
      "mean_elapsed_ms": 34.4594,
      "min_elapsed_ms": 33.4125,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T11:10:06.504252+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 54.5185,
  "mean_elapsed_ms": 38.2002,
  "median_elapsed_ms": 35.4574,
  "min_elapsed_ms": 33.4125,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.3165,
      "evidence_path": "artifacts/runs/claim-20260526T111006504252Z-dad5a7/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T111006504252Z-dad5a7",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.0978,
      "evidence_path": "artifacts/runs/claim-20260526T111006551468Z-421cf4/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T111006551468Z-421cf4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.9379,
      "evidence_path": "artifacts/runs/claim-20260526T111006592926Z-023d36/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T111006592926Z-023d36",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.9769,
      "evidence_path": "artifacts/runs/claim-20260526T111006628844Z-2b1df9/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T111006628844Z-2b1df9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.7988,
      "evidence_path": "artifacts/runs/claim-20260526T111006664304Z-e6b8d7/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T111006664304Z-e6b8d7",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 54.5185,
      "evidence_path": "artifacts/runs/claim-20260526T111006702352Z-d373b0/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T111006702352Z-d373b0",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.364,
      "evidence_path": "artifacts/runs/claim-20260526T111006757556Z-38e632/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T111006757556Z-38e632",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.6076,
      "evidence_path": "artifacts/runs/claim-20260526T111006793716Z-36bfd3/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T111006793716Z-36bfd3",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.4125,
      "evidence_path": "artifacts/runs/claim-20260526T111006828338Z-d7bdea/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T111006828338Z-d7bdea",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.6481,
      "evidence_path": "artifacts/runs/claim-20260526T111006862173Z-ac1402/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T111006862173Z-ac1402",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.9673,
      "evidence_path": "artifacts/runs/claim-20260526T111006895773Z-238da2/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T111006895773Z-238da2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.757,
      "evidence_path": "artifacts/runs/claim-20260526T111006930349Z-0e8226/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T111006930349Z-0e8226",
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
