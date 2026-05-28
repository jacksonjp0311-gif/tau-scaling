# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T08:40:20.762881+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `82.419` |
| `import_runtime` | `true` | `0` | `120.894` |
| `rcc_nexus_check` | `true` | `0` | `95.79` |
| `readme_mini_repo_audit` | `true` | `0` | `92.424` |
| `architecture_contract_validation` | `true` | `0` | `69.722` |
| `unit_tests` | `true` | `0` | `236.7` |
| `benchmark_harness` | `true` | `0` | `668.169` |
| `baseline_claim` | `true` | `0` | `168.08` |
| `promotion_path_claim` | `true` | `0` | `188.274` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T084020486147Z-a9679b",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T084020486147Z-a9679b\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T084020486147Z-a9679b"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T084020666434Z-f17578",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T084020666434Z-f17578\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T084020666434Z-f17578"
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
      "max_elapsed_ms": 47.3416,
      "mean_elapsed_ms": 43.8909,
      "min_elapsed_ms": 42.7004,
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
      "max_elapsed_ms": 61.7553,
      "mean_elapsed_ms": 43.8609,
      "min_elapsed_ms": 39.0101,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T08:40:19.818422+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 61.7553,
  "mean_elapsed_ms": 43.8759,
  "median_elapsed_ms": 42.7841,
  "min_elapsed_ms": 39.0101,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.3416,
      "evidence_path": "artifacts/runs/claim-20260528T084019818422Z-b73104/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T084019818422Z-b73104",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.7127,
      "evidence_path": "artifacts/runs/claim-20260528T084019865343Z-176bff/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T084019865343Z-176bff",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.8554,
      "evidence_path": "artifacts/runs/claim-20260528T084019909118Z-efa729/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T084019909118Z-efa729",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.037,
      "evidence_path": "artifacts/runs/claim-20260528T084019952128Z-1db843/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T084019952128Z-1db843",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.7004,
      "evidence_path": "artifacts/runs/claim-20260528T084019995007Z-f9e223/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T084019995007Z-f9e223",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.6981,
      "evidence_path": "artifacts/runs/claim-20260528T084020037588Z-ec24da/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T084020037588Z-ec24da",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.5688,
      "evidence_path": "artifacts/runs/claim-20260528T084020082869Z-db183a/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T084020082869Z-db183a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.4786,
      "evidence_path": "artifacts/runs/claim-20260528T084020122742Z-2325a5/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T084020122742Z-2325a5",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 43.3054,
      "evidence_path": "artifacts/runs/claim-20260528T084020163585Z-587e6c/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T084020163585Z-587e6c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.0101,
      "evidence_path": "artifacts/runs/claim-20260528T084020206980Z-f978d3/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T084020206980Z-f978d3",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 61.7553,
      "evidence_path": "artifacts/runs/claim-20260528T084020246284Z-ef1a10/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T084020246284Z-ef1a10",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.0474,
      "evidence_path": "artifacts/runs/claim-20260528T084020308301Z-d51f8c/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T084020308301Z-d51f8c",
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
