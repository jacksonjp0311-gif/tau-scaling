# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T10:05:31.159855+00:00`

Passed: `false`
Step count: `9`
Step failures: `1`
Findings: `4`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `74.757` |
| `import_runtime` | `true` | `0` | `118.303` |
| `rcc_nexus_check` | `true` | `0` | `76.069` |
| `readme_mini_repo_audit` | `false` | `1` | `91.263` |
| `architecture_contract_validation` | `true` | `0` | `86.73` |
| `unit_tests` | `true` | `0` | `232.224` |
| `benchmark_harness` | `true` | `0` | `571.581` |
| `baseline_claim` | `true` | `0` | `159.02` |
| `promotion_path_claim` | `true` | `0` | `160.829` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T100530911665Z-f7a86e",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T100530911665Z-f7a86e\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T100530911665Z-f7a86e"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T100531073675Z-6217ae",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T100531073675Z-6217ae\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T100531073675Z-6217ae"
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
      "max_elapsed_ms": 43.9389,
      "mean_elapsed_ms": 39.4529,
      "min_elapsed_ms": 37.5847,
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
      "max_elapsed_ms": 37.0393,
      "mean_elapsed_ms": 35.5191,
      "min_elapsed_ms": 33.9491,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T10:05:30.335618+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 43.9389,
  "mean_elapsed_ms": 37.486,
  "median_elapsed_ms": 37.312,
  "min_elapsed_ms": 33.9491,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.9389,
      "evidence_path": "artifacts/runs/claim-20260528T100530335618Z-10b4e1/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T100530335618Z-10b4e1",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.2407,
      "evidence_path": "artifacts/runs/claim-20260528T100530380420Z-07d5eb/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T100530380420Z-07d5eb",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.9797,
      "evidence_path": "artifacts/runs/claim-20260528T100530419304Z-d329e3/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T100530419304Z-d329e3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.3144,
      "evidence_path": "artifacts/runs/claim-20260528T100530459669Z-b30487/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T100530459669Z-b30487",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.5847,
      "evidence_path": "artifacts/runs/claim-20260528T100530498366Z-73d414/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T100530498366Z-73d414",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.6591,
      "evidence_path": "artifacts/runs/claim-20260528T100530535575Z-b167b3/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T100530535575Z-b167b3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.0156,
      "evidence_path": "artifacts/runs/claim-20260528T100530574572Z-998c30/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T100530574572Z-998c30",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.3134,
      "evidence_path": "artifacts/runs/claim-20260528T100530609911Z-62f44e/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T100530609911Z-62f44e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.0393,
      "evidence_path": "artifacts/runs/claim-20260528T100530646352Z-28df19/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T100530646352Z-28df19",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.9491,
      "evidence_path": "artifacts/runs/claim-20260528T100530684293Z-95e168/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T100530684293Z-95e168",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.6796,
      "evidence_path": "artifacts/runs/claim-20260528T100530718560Z-de3217/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T100530718560Z-de3217",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.1179,
      "evidence_path": "artifacts/runs/claim-20260528T100530753168Z-a60e24/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T100530753168Z-a60e24",
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
| warning | `possible_mojibake` | `README.md` | latin1_mojibake_A_tilde: \xc3 |
| warning | `possible_mojibake` | `README.md` | latin1_mojibake_A_circumflex: \xc2 |
| warning | `possible_mojibake` | `README.md` | utf8_quote_dash_mojibake: \xe2\u20ac |
| error | `readme_audit_reported_failed` | `reports/readme/latest_readme_mini_repo_audit.json` |  |

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
