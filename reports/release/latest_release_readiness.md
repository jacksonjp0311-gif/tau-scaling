# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T14:20:08.638893+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `73.248` |
| `import_runtime` | `true` | `0` | `134.651` |
| `rcc_nexus_check` | `true` | `0` | `93.655` |
| `readme_mini_repo_audit` | `true` | `0` | `91.406` |
| `architecture_contract_validation` | `true` | `0` | `67.125` |
| `unit_tests` | `true` | `0` | `212.289` |
| `benchmark_harness` | `true` | `0` | `547.378` |
| `baseline_claim` | `true` | `0` | `161.716` |
| `promotion_path_claim` | `true` | `0` | `159.827` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T142008396682Z-9cd776",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T142008396682Z-9cd776\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T142008396682Z-9cd776"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T142008557151Z-5d4cb2",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T142008557151Z-5d4cb2\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T142008557151Z-5d4cb2"
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
      "max_elapsed_ms": 40.3411,
      "mean_elapsed_ms": 36.4916,
      "min_elapsed_ms": 34.7167,
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
      "max_elapsed_ms": 37.8478,
      "mean_elapsed_ms": 35.5497,
      "min_elapsed_ms": 33.5134,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T14:20:07.831982+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 40.3411,
  "mean_elapsed_ms": 36.0206,
  "median_elapsed_ms": 35.1574,
  "min_elapsed_ms": 33.5134,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.3411,
      "evidence_path": "artifacts/runs/claim-20260528T142007831982Z-f76fe6/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T142007831982Z-f76fe6",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1825,
      "evidence_path": "artifacts/runs/claim-20260528T142007872439Z-92f16a/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T142007872439Z-92f16a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.7167,
      "evidence_path": "artifacts/runs/claim-20260528T142007907550Z-3907f5/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T142007907550Z-3907f5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.6421,
      "evidence_path": "artifacts/runs/claim-20260528T142007942450Z-0f2cb2/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T142007942450Z-0f2cb2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.9347,
      "evidence_path": "artifacts/runs/claim-20260528T142007980147Z-dade90/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T142007980147Z-dade90",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1324,
      "evidence_path": "artifacts/runs/claim-20260528T142008016862Z-dafb94/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T142008016862Z-dafb94",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0707,
      "evidence_path": "artifacts/runs/claim-20260528T142008051712Z-140cf0/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T142008051712Z-140cf0",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.7455,
      "evidence_path": "artifacts/runs/claim-20260528T142008087801Z-23f82b/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T142008087801Z-23f82b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.8478,
      "evidence_path": "artifacts/runs/claim-20260528T142008122204Z-e5083b/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T142008122204Z-e5083b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.5134,
      "evidence_path": "artifacts/runs/claim-20260528T142008160718Z-bdf52a/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T142008160718Z-bdf52a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0772,
      "evidence_path": "artifacts/runs/claim-20260528T142008194008Z-3d6305/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T142008194008Z-3d6305",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.0437,
      "evidence_path": "artifacts/runs/claim-20260528T142008229029Z-66b543/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T142008229029Z-66b543",
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
