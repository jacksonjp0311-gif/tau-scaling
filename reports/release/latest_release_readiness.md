# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T11:31:10.849214+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `72.773` |
| `import_runtime` | `true` | `0` | `113.609` |
| `rcc_nexus_check` | `true` | `0` | `83.631` |
| `readme_mini_repo_audit` | `true` | `0` | `89.914` |
| `architecture_contract_validation` | `true` | `0` | `68.606` |
| `unit_tests` | `true` | `0` | `221.046` |
| `benchmark_harness` | `true` | `0` | `609.65` |
| `baseline_claim` | `true` | `0` | `176.614` |
| `promotion_path_claim` | `true` | `0` | `193.011` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T113110561461Z-9f51ac",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T113110561461Z-9f51ac\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T113110561461Z-9f51ac"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T113110766810Z-543926",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T113110766810Z-543926\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T113110766810Z-543926"
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
      "max_elapsed_ms": 41.2614,
      "mean_elapsed_ms": 38.1593,
      "min_elapsed_ms": 35.9637,
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
      "max_elapsed_ms": 50.5763,
      "mean_elapsed_ms": 41.1536,
      "min_elapsed_ms": 34.1887,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T11:31:09.953331+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 50.5763,
  "mean_elapsed_ms": 39.6564,
  "median_elapsed_ms": 38.7851,
  "min_elapsed_ms": 34.1887,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.2614,
      "evidence_path": "artifacts/runs/claim-20260526T113109953331Z-9dc7ec/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T113109953331Z-9dc7ec",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.2485,
      "evidence_path": "artifacts/runs/claim-20260526T113109994580Z-7e3640/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T113109994580Z-7e3640",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.3068,
      "evidence_path": "artifacts/runs/claim-20260526T113110034767Z-f0bc37/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T113110034767Z-f0bc37",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.6324,
      "evidence_path": "artifacts/runs/claim-20260526T113110072434Z-edf382/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T113110072434Z-edf382",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.5428,
      "evidence_path": "artifacts/runs/claim-20260526T113110110542Z-8a7d52/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T113110110542Z-8a7d52",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.9637,
      "evidence_path": "artifacts/runs/claim-20260526T113110147692Z-c92925/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T113110147692Z-c92925",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.2313,
      "evidence_path": "artifacts/runs/claim-20260526T113110184039Z-86cd87/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T113110184039Z-86cd87",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.9378,
      "evidence_path": "artifacts/runs/claim-20260526T113110220833Z-d8dec8/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T113110220833Z-d8dec8",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 50.5763,
      "evidence_path": "artifacts/runs/claim-20260526T113110260056Z-29133c/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T113110260056Z-29133c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 46.5572,
      "evidence_path": "artifacts/runs/claim-20260526T113110311468Z-92290c/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T113110311468Z-92290c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.4303,
      "evidence_path": "artifacts/runs/claim-20260526T113110358148Z-f35933/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T113110358148Z-f35933",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.1887,
      "evidence_path": "artifacts/runs/claim-20260526T113110398277Z-ec8424/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T113110398277Z-ec8424",
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
