# Tau Scaling v0.4.0 Synthetic Gate Suite

Generated: `2026-05-26T13:22:31.264895+00:00`

## Result

- Total scenarios: `10`
- Passed scenarios: `10`
- Failed scenarios: `0`
- All scenarios passed: `True`
- Mean elapsed ms: `37.3734`

## Benchmark Charts

![class_distribution](../../../visuals/benchmarks/v0_4_0/class_distribution.png)

![a_tsek_by_scenario](../../../visuals/benchmarks/v0_4_0/a_tsek_by_scenario.png)

![finding_count_by_scenario](../../../visuals/benchmarks/v0_4_0/finding_count_by_scenario.png)

![diagnostic_average_by_scenario](../../../visuals/benchmarks/v0_4_0/diagnostic_average_by_scenario.png)

![elapsed_ms_by_scenario](../../../visuals/benchmarks/v0_4_0/elapsed_ms_by_scenario.png)

![gate_heatmap](../../../visuals/benchmarks/v0_4_0/gate_heatmap.png)

![finding_code_frequency](../../../visuals/benchmarks/v0_4_0/finding_code_frequency.png)

## Scenario Findings

| Scenario | Expected | Actual | A_TSEK | Diagnostic avg | Findings | Passed |
|---|---|---|---:|---:|---:|---|
| `control_all_disclosed_promotable` | TSEK-B | TSEK-B | 1.0 | 1.0 | 0 | True |
| `yield_missing_downgrade` | TSEK-C | TSEK-C | 0.0 | 0.9091 | 1 | True |
| `missing_workload_downgrade` | TSEK-C | TSEK-C | 0.0 | 0.9091 | 1 | True |
| `missing_baseline_downgrade` | TSEK-C | TSEK-C | 0.0 | 0.9091 | 1 | True |
| `logicfolding_high_vertical_penalty_downgrade` | TSEK-C | TSEK-C | 0.0 | 0.9091 | 1 | True |
| `etp_thermal_pdn_fail_downgrade` | TSEK-C | TSEK-C | 0.0 | 0.9091 | 1 | True |
| `pvt_closure_fail_downgrade` | TSEK-C | TSEK-C | 0.0 | 0.9091 | 1 | True |
| `evidence_package_missing_downgrade` | TSEK-C | TSEK-C | 0.0 | 0.9091 | 1 | True |
| `independent_validation_overclaim_block` | TSEK-E | TSEK-E | 0.0 | 1.0 | 1 | True |
| `multi_gate_stress_low_disclosure` | TSEK-E | TSEK-E | 0.0 | 0.0909 | 10 | True |

## Finding Code Frequency

| Finding code | Count |
|---|---:|
| `TSEK_B_ETP_MISSING` | 2 |
| `TSEK_B_LF_MISSING` | 2 |
| `TSEK_B_PVT_MISSING` | 2 |
| `TSEK_B_baseline_MISSING` | 2 |
| `TSEK_B_evidence_MISSING` | 2 |
| `TSEK_B_method_MISSING` | 1 |
| `TSEK_B_metric_MISSING` | 1 |
| `TSEK_B_tau_MISSING` | 1 |
| `TSEK_B_workload_MISSING` | 2 |
| `TSEK_B_yield_MISSING` | 2 |
| `TSEK_OVERCLAIM_INDEPENDENT_VALIDATION` | 1 |

## Finding Charts

![finding_b-etp-missing](../../../visuals/findings/v0_4_0/finding_b-etp-missing.png)

![finding_b-lf-missing](../../../visuals/findings/v0_4_0/finding_b-lf-missing.png)

![finding_b-pvt-missing](../../../visuals/findings/v0_4_0/finding_b-pvt-missing.png)

![finding_b-baseline-missing](../../../visuals/findings/v0_4_0/finding_b-baseline-missing.png)

![finding_b-evidence-missing](../../../visuals/findings/v0_4_0/finding_b-evidence-missing.png)

![finding_b-method-missing](../../../visuals/findings/v0_4_0/finding_b-method-missing.png)

![finding_b-metric-missing](../../../visuals/findings/v0_4_0/finding_b-metric-missing.png)

![finding_b-tau-missing](../../../visuals/findings/v0_4_0/finding_b-tau-missing.png)

![finding_b-workload-missing](../../../visuals/findings/v0_4_0/finding_b-workload-missing.png)

![finding_b-yield-missing](../../../visuals/findings/v0_4_0/finding_b-yield-missing.png)

![finding_overclaim-independent-validation](../../../visuals/findings/v0_4_0/finding_overclaim-independent-validation.png)

## Gate Failure Counts

| Gate | Failures |
|---|---:|
| `B_ETP` | 2 |
| `B_LF` | 2 |
| `B_PVT` | 2 |
| `B_baseline` | 2 |
| `B_evidence` | 2 |
| `B_method` | 1 |
| `B_metric` | 1 |
| `B_source` | 0 |
| `B_tau` | 1 |
| `B_workload` | 2 |
| `B_yield` | 2 |

## Boundary

Synthetic gate suite validates local runtime downgrade behavior only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
