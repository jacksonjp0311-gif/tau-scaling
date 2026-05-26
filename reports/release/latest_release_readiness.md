# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T13:30:29.359923+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `83.209` |
| `import_runtime` | `true` | `0` | `121.491` |
| `rcc_nexus_check` | `true` | `0` | `94.272` |
| `readme_mini_repo_audit` | `true` | `0` | `117.041` |
| `architecture_contract_validation` | `true` | `0` | `66.785` |
| `unit_tests` | `true` | `0` | `223.304` |
| `benchmark_harness` | `true` | `0` | `566.617` |
| `baseline_claim` | `true` | `0` | `166.118` |
| `promotion_path_claim` | `true` | `0` | `173.088` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T133029100819Z-e99381",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T133029100819Z-e99381\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T133029100819Z-e99381"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T133029273315Z-d305e3",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T133029273315Z-d305e3\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T133029273315Z-d305e3"
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
      "max_elapsed_ms": 39.7534,
      "mean_elapsed_ms": 37.5735,
      "min_elapsed_ms": 36.2056,
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
      "max_elapsed_ms": 38.9626,
      "mean_elapsed_ms": 37.3588,
      "min_elapsed_ms": 34.4565,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T13:30:28.516824+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.7534,
  "mean_elapsed_ms": 37.4661,
  "median_elapsed_ms": 37.4395,
  "min_elapsed_ms": 34.4565,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.7534,
      "evidence_path": "artifacts/runs/claim-20260526T133028516824Z-0abc3c/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T133028516824Z-0abc3c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.2056,
      "evidence_path": "artifacts/runs/claim-20260526T133028557295Z-79f2a1/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T133028557295Z-79f2a1",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.0521,
      "evidence_path": "artifacts/runs/claim-20260526T133028593406Z-4d4bfc/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T133028593406Z-4d4bfc",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.6717,
      "evidence_path": "artifacts/runs/claim-20260526T133028630602Z-f13629/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T133028630602Z-f13629",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.8029,
      "evidence_path": "artifacts/runs/claim-20260526T133028669272Z-e07b2f/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T133028669272Z-e07b2f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.955,
      "evidence_path": "artifacts/runs/claim-20260526T133028705845Z-8a151d/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T133028705845Z-8a151d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.827,
      "evidence_path": "artifacts/runs/claim-20260526T133028744101Z-15370c/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T133028744101Z-15370c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.9626,
      "evidence_path": "artifacts/runs/claim-20260526T133028781785Z-878367/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T133028781785Z-878367",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.1408,
      "evidence_path": "artifacts/runs/claim-20260526T133028821565Z-9d1cbd/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T133028821565Z-9d1cbd",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.7607,
      "evidence_path": "artifacts/runs/claim-20260526T133028860054Z-f36a11/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T133028860054Z-f36a11",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.0053,
      "evidence_path": "artifacts/runs/claim-20260526T133028896158Z-edb274/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T133028896158Z-edb274",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.4565,
      "evidence_path": "artifacts/runs/claim-20260526T133028935087Z-886b60/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T133028935087Z-886b60",
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
