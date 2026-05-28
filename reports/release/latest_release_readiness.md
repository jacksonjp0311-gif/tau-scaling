# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T08:03:05.832439+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `69.982` |
| `import_runtime` | `true` | `0` | `102.661` |
| `rcc_nexus_check` | `true` | `0` | `84.3` |
| `readme_mini_repo_audit` | `true` | `0` | `80.069` |
| `architecture_contract_validation` | `true` | `0` | `67.094` |
| `unit_tests` | `true` | `0` | `225.44` |
| `benchmark_harness` | `true` | `0` | `549.457` |
| `baseline_claim` | `true` | `0` | `170.406` |
| `promotion_path_claim` | `true` | `0` | `162.305` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T080305580407Z-999d68",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T080305580407Z-999d68\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T080305580407Z-999d68"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T080305748523Z-bf6003",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T080305748523Z-bf6003\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T080305748523Z-bf6003"
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
      "max_elapsed_ms": 39.5539,
      "mean_elapsed_ms": 36.9208,
      "min_elapsed_ms": 34.9315,
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
      "max_elapsed_ms": 39.1423,
      "mean_elapsed_ms": 35.711,
      "min_elapsed_ms": 33.4624,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T08:03:05.009093+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.5539,
  "mean_elapsed_ms": 36.3159,
  "median_elapsed_ms": 35.9135,
  "min_elapsed_ms": 33.4624,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.5539,
      "evidence_path": "artifacts/runs/claim-20260528T080305009093Z-0c83a3/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T080305009093Z-0c83a3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.9315,
      "evidence_path": "artifacts/runs/claim-20260528T080305049224Z-144a34/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T080305049224Z-144a34",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.7096,
      "evidence_path": "artifacts/runs/claim-20260528T080305084176Z-6403b3/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T080305084176Z-6403b3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.6715,
      "evidence_path": "artifacts/runs/claim-20260528T080305120019Z-87ce17/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T080305120019Z-87ce17",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.0934,
      "evidence_path": "artifacts/runs/claim-20260528T080305157715Z-d8fc86/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T080305157715Z-d8fc86",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.5649,
      "evidence_path": "artifacts/runs/claim-20260528T080305193594Z-88127a/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T080305193594Z-88127a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.1423,
      "evidence_path": "artifacts/runs/claim-20260528T080305232326Z-510379/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T080305232326Z-510379",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.7336,
      "evidence_path": "artifacts/runs/claim-20260528T080305270795Z-e1f1c9/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T080305270795Z-e1f1c9",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.2338,
      "evidence_path": "artifacts/runs/claim-20260528T080305306891Z-9f5b0f/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T080305306891Z-9f5b0f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.4624,
      "evidence_path": "artifacts/runs/claim-20260528T080305343926Z-e2226e/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T080305343926Z-e2226e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.016,
      "evidence_path": "artifacts/runs/claim-20260528T080305377000Z-5033c4/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T080305377000Z-5033c4",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.6778,
      "evidence_path": "artifacts/runs/claim-20260528T080305412172Z-17c7c1/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T080305412172Z-17c7c1",
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
