# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T08:43:30.578234+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `70.596` |
| `import_runtime` | `true` | `0` | `104.027` |
| `rcc_nexus_check` | `true` | `0` | `86.365` |
| `readme_mini_repo_audit` | `true` | `0` | `81.316` |
| `architecture_contract_validation` | `true` | `0` | `60.123` |
| `unit_tests` | `true` | `0` | `207.165` |
| `benchmark_harness` | `true` | `0` | `576.786` |
| `baseline_claim` | `true` | `0` | `150.565` |
| `promotion_path_claim` | `true` | `0` | `166.405` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T084330324096Z-e8d43e",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T084330324096Z-e8d43e\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T084330324096Z-e8d43e"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T084330473781Z-639ed7",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T084330473781Z-639ed7\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T084330473781Z-639ed7"
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
      "max_elapsed_ms": 44.8273,
      "mean_elapsed_ms": 40.4316,
      "min_elapsed_ms": 36.7542,
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
      "max_elapsed_ms": 38.266,
      "mean_elapsed_ms": 36.7174,
      "min_elapsed_ms": 34.9918,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T08:43:29.736697+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 44.8273,
  "mean_elapsed_ms": 38.5745,
  "median_elapsed_ms": 38.034,
  "min_elapsed_ms": 34.9918,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.7203,
      "evidence_path": "artifacts/runs/claim-20260528T084329737700Z-268cfa/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T084329737700Z-268cfa",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.8273,
      "evidence_path": "artifacts/runs/claim-20260528T084329781643Z-63106f/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T084329781643Z-63106f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.1003,
      "evidence_path": "artifacts/runs/claim-20260528T084329825691Z-ae5e52/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T084329825691Z-ae5e52",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.3575,
      "evidence_path": "artifacts/runs/claim-20260528T084329867686Z-6eaa92/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T084329867686Z-6eaa92",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.83,
      "evidence_path": "artifacts/runs/claim-20260528T084329906052Z-d27fda/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T084329906052Z-d27fda",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.7542,
      "evidence_path": "artifacts/runs/claim-20260528T084329944004Z-2948a9/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T084329944004Z-2948a9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.3226,
      "evidence_path": "artifacts/runs/claim-20260528T084329981059Z-60a403/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T084329981059Z-60a403",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.266,
      "evidence_path": "artifacts/runs/claim-20260528T084330018277Z-d9f496/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T084330018277Z-d9f496",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.2379,
      "evidence_path": "artifacts/runs/claim-20260528T084330057152Z-7be414/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T084330057152Z-7be414",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.9918,
      "evidence_path": "artifacts/runs/claim-20260528T084330095374Z-7e0211/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T084330095374Z-7e0211",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.8946,
      "evidence_path": "artifacts/runs/claim-20260528T084330130889Z-fa1851/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T084330130889Z-fa1851",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.5917,
      "evidence_path": "artifacts/runs/claim-20260528T084330166289Z-4459d3/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T084330166289Z-4459d3",
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
