# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T09:41:17.401367+00:00`

Passed: `false`
Step count: `9`
Step failures: `1`
Findings: `2`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `77.72` |
| `import_runtime` | `true` | `0` | `138.466` |
| `rcc_nexus_check` | `true` | `0` | `88.958` |
| `readme_mini_repo_audit` | `false` | `1` | `101.594` |
| `architecture_contract_validation` | `true` | `0` | `73.455` |
| `unit_tests` | `true` | `0` | `230.232` |
| `benchmark_harness` | `true` | `0` | `621.588` |
| `baseline_claim` | `true` | `0` | `172.954` |
| `promotion_path_claim` | `true` | `0` | `253.916` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T094117038252Z-476cf5",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T094117038252Z-476cf5\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T094117038252Z-476cf5"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T094117282644Z-bd697d",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T094117282644Z-bd697d\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T094117282644Z-bd697d"
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
      "max_elapsed_ms": 49.836,
      "mean_elapsed_ms": 42.6756,
      "min_elapsed_ms": 39.7625,
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
      "max_elapsed_ms": 43.1146,
      "mean_elapsed_ms": 39.7034,
      "min_elapsed_ms": 37.0399,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T09:41:16.402845+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 49.836,
  "mean_elapsed_ms": 41.1895,
  "median_elapsed_ms": 40.5367,
  "min_elapsed_ms": 37.0399,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 49.836,
      "evidence_path": "artifacts/runs/claim-20260528T094116403848Z-54d6d6/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T094116403848Z-54d6d6",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.2907,
      "evidence_path": "artifacts/runs/claim-20260528T094116453940Z-da0f2a/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T094116453940Z-da0f2a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.1817,
      "evidence_path": "artifacts/runs/claim-20260528T094116496357Z-e2a12c/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T094116496357Z-e2a12c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.8263,
      "evidence_path": "artifacts/runs/claim-20260528T094116536839Z-d16af3/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T094116536839Z-d16af3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.1565,
      "evidence_path": "artifacts/runs/claim-20260528T094116577514Z-1798bb/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T094116577514Z-1798bb",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.7625,
      "evidence_path": "artifacts/runs/claim-20260528T094116621056Z-0b65fe/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T094116621056Z-0b65fe",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.8813,
      "evidence_path": "artifacts/runs/claim-20260528T094116661137Z-8aa25f/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T094116661137Z-8aa25f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.247,
      "evidence_path": "artifacts/runs/claim-20260528T094116700166Z-dc3024/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T094116700166Z-dc3024",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 43.1146,
      "evidence_path": "artifacts/runs/claim-20260528T094116741257Z-b32de7/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T094116741257Z-b32de7",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.0006,
      "evidence_path": "artifacts/runs/claim-20260528T094116784018Z-12f582/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T094116784018Z-12f582",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.9368,
      "evidence_path": "artifacts/runs/claim-20260528T094116823207Z-7c7f68/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T094116823207Z-7c7f68",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.0399,
      "evidence_path": "artifacts/runs/claim-20260528T094116863359Z-72f96b/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T094116863359Z-72f96b",
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
| warning | `possible_mojibake` | `README.md` | utf8_quote_dash_mojibake: \xe2\u20ac |
| error | `readme_audit_reported_failed` | `reports/readme/latest_readme_mini_repo_audit.json` |  |

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
