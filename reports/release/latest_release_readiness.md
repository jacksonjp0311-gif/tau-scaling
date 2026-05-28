# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T07:43:06.655244+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `146.127` |
| `import_runtime` | `true` | `0` | `369.637` |
| `rcc_nexus_check` | `true` | `0` | `554.386` |
| `readme_mini_repo_audit` | `true` | `0` | `252.129` |
| `architecture_contract_validation` | `true` | `0` | `92.95` |
| `unit_tests` | `true` | `0` | `332.695` |
| `benchmark_harness` | `true` | `0` | `841.691` |
| `baseline_claim` | `true` | `0` | `331.36` |
| `promotion_path_claim` | `true` | `0` | `369.826` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074306120348Z-72a819",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074306120348Z-72a819\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T074306120348Z-72a819"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074306499004Z-70b8cf",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T074306499004Z-70b8cf\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T074306499004Z-70b8cf"
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
      "max_elapsed_ms": 46.5157,
      "mean_elapsed_ms": 43.031,
      "min_elapsed_ms": 36.324,
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
      "max_elapsed_ms": 170.841,
      "mean_elapsed_ms": 70.7992,
      "min_elapsed_ms": 40.1483,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T07:43:05.172851+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 170.841,
  "mean_elapsed_ms": 56.9151,
  "median_elapsed_ms": 45.1895,
  "min_elapsed_ms": 36.324,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.9016,
      "evidence_path": "artifacts/runs/claim-20260528T074305172851Z-41d99e/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T074305172851Z-41d99e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 46.1752,
      "evidence_path": "artifacts/runs/claim-20260528T074305217711Z-db443f/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T074305217711Z-db443f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.324,
      "evidence_path": "artifacts/runs/claim-20260528T074305264440Z-c3463a/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T074305264440Z-c3463a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.0264,
      "evidence_path": "artifacts/runs/claim-20260528T074305300444Z-8279f5/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T074305300444Z-8279f5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 46.5157,
      "evidence_path": "artifacts/runs/claim-20260528T074305341265Z-e10abb/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T074305341265Z-e10abb",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.2429,
      "evidence_path": "artifacts/runs/claim-20260528T074305387165Z-de98b0/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T074305387165Z-de98b0",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 43.9245,
      "evidence_path": "artifacts/runs/claim-20260528T074305441986Z-f07698/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T074305441986Z-f07698",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.1483,
      "evidence_path": "artifacts/runs/claim-20260528T074305485913Z-816e6c/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T074305485913Z-816e6c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 45.4774,
      "evidence_path": "artifacts/runs/claim-20260528T074305525840Z-c7bf1d/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T074305525840Z-c7bf1d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 47.4398,
      "evidence_path": "artifacts/runs/claim-20260528T074305571150Z-b284b2/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T074305571150Z-b284b2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 76.964,
      "evidence_path": "artifacts/runs/claim-20260528T074305619160Z-fb0717/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T074305619160Z-fb0717",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 170.841,
      "evidence_path": "artifacts/runs/claim-20260528T074305696309Z-0514c4/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T074305696309Z-0514c4",
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
