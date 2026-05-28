# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T09:04:51.887550+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `71.894` |
| `import_runtime` | `true` | `0` | `111.71` |
| `rcc_nexus_check` | `true` | `0` | `91.845` |
| `readme_mini_repo_audit` | `true` | `0` | `92.811` |
| `architecture_contract_validation` | `true` | `0` | `95.273` |
| `unit_tests` | `true` | `0` | `371.238` |
| `benchmark_harness` | `true` | `0` | `752.016` |
| `baseline_claim` | `true` | `0` | `178.18` |
| `promotion_path_claim` | `true` | `0` | `221.276` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T090451571805Z-df1c2d",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T090451571805Z-df1c2d\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T090451571805Z-df1c2d"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T090451746160Z-020960",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T090451746160Z-020960\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T090451746160Z-020960"
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
      "max_elapsed_ms": 62.4466,
      "mean_elapsed_ms": 50.6301,
      "min_elapsed_ms": 44.2496,
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
      "max_elapsed_ms": 67.3346,
      "mean_elapsed_ms": 47.5084,
      "min_elapsed_ms": 38.8585,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T09:04:50.831799+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 67.3346,
  "mean_elapsed_ms": 49.0693,
  "median_elapsed_ms": 46.7344,
  "min_elapsed_ms": 38.8585,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 62.4466,
      "evidence_path": "artifacts/runs/claim-20260528T090450831799Z-d2b95d/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T090450831799Z-d2b95d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 53.0996,
      "evidence_path": "artifacts/runs/claim-20260528T090450894140Z-18751d/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T090450894140Z-18751d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 50.6267,
      "evidence_path": "artifacts/runs/claim-20260528T090450947556Z-b06477/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T090450947556Z-b06477",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 48.2754,
      "evidence_path": "artifacts/runs/claim-20260528T090450998315Z-1a43b8/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T090450998315Z-1a43b8",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 45.0825,
      "evidence_path": "artifacts/runs/claim-20260528T090451047139Z-7c5f34/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T090451047139Z-7c5f34",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.2496,
      "evidence_path": "artifacts/runs/claim-20260528T090451092270Z-603c5f/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T090451092270Z-603c5f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 54.1316,
      "evidence_path": "artifacts/runs/claim-20260528T090451136886Z-f568c6/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T090451136886Z-f568c6",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.3496,
      "evidence_path": "artifacts/runs/claim-20260528T090451191741Z-05af92/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T090451191741Z-05af92",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.1829,
      "evidence_path": "artifacts/runs/claim-20260528T090451232541Z-3ca8f3/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T090451232541Z-3ca8f3",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.8585,
      "evidence_path": "artifacts/runs/claim-20260528T090451271272Z-84197d/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T090451271272Z-84197d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 67.3346,
      "evidence_path": "artifacts/runs/claim-20260528T090451310194Z-9442ea/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T090451310194Z-9442ea",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 45.1935,
      "evidence_path": "artifacts/runs/claim-20260528T090451378037Z-9ba0b6/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T090451378037Z-9ba0b6",
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
