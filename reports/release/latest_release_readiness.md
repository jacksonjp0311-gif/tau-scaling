# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T14:56:18.739383+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `92.224` |
| `import_runtime` | `true` | `0` | `145.965` |
| `rcc_nexus_check` | `true` | `0` | `101.349` |
| `readme_mini_repo_audit` | `true` | `0` | `102.154` |
| `architecture_contract_validation` | `true` | `0` | `77.099` |
| `unit_tests` | `true` | `0` | `241.983` |
| `benchmark_harness` | `true` | `0` | `594.606` |
| `baseline_claim` | `true` | `0` | `426.877` |
| `promotion_path_claim` | `true` | `0` | `188.801` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T145618461546Z-de6c71",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T145618461546Z-de6c71\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T145618461546Z-de6c71"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T145618648334Z-2d0586",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T145618648334Z-2d0586\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T145618648334Z-2d0586"
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
      "max_elapsed_ms": 44.1759,
      "mean_elapsed_ms": 39.3309,
      "min_elapsed_ms": 36.0794,
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
      "max_elapsed_ms": 40.2322,
      "mean_elapsed_ms": 37.8299,
      "min_elapsed_ms": 35.0547,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T14:56:17.604431+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 44.1759,
  "mean_elapsed_ms": 38.5804,
  "median_elapsed_ms": 38.8834,
  "min_elapsed_ms": 35.0547,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.1759,
      "evidence_path": "artifacts/runs/claim-20260528T145617604431Z-3df285/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T145617604431Z-3df285",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.8888,
      "evidence_path": "artifacts/runs/claim-20260528T145617648451Z-39c1f5/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T145617648451Z-39c1f5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.4825,
      "evidence_path": "artifacts/runs/claim-20260528T145617687447Z-a81b45/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T145617687447Z-a81b45",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.8779,
      "evidence_path": "artifacts/runs/claim-20260528T145617728886Z-adfe6a/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T145617728886Z-adfe6a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.4807,
      "evidence_path": "artifacts/runs/claim-20260528T145617767025Z-799635/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T145617767025Z-799635",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.0794,
      "evidence_path": "artifacts/runs/claim-20260528T145617805376Z-69e0c0/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T145617805376Z-69e0c0",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.8435,
      "evidence_path": "artifacts/runs/claim-20260528T145617842165Z-611c63/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T145617842165Z-611c63",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0547,
      "evidence_path": "artifacts/runs/claim-20260528T145617879211Z-ddfad6/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T145617879211Z-ddfad6",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.8996,
      "evidence_path": "artifacts/runs/claim-20260528T145617914618Z-ea869e/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T145617914618Z-ea869e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.2322,
      "evidence_path": "artifacts/runs/claim-20260528T145617951497Z-241db7/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T145617951497Z-241db7",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.0422,
      "evidence_path": "artifacts/runs/claim-20260528T145617992076Z-19ed05/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T145617992076Z-19ed05",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.9072,
      "evidence_path": "artifacts/runs/claim-20260528T145618030996Z-ab9aa7/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T145618030996Z-ab9aa7",
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
