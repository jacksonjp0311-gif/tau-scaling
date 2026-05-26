# Tau Scaling Benchmark and Finding Atlas

Generated: 2026-05-26T13:30:21.550530+00:00

Current atlas version: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**

## Purpose

This atlas gives humans and AI agents one stable place to understand benchmark evolution, finding evidence, chart locations, and claim boundaries.

## Benchmark Version Ledger

| Version | Benchmark layer | Command | Result | Primary reports | Chart surface |
|---|---|---|---|---|---|
| v0.3.2 | Collision-proof benchmark loop | `python scripts/benchmarks/run_tau_scaling_benchmarks.py` | 12 runs / 12 unique IDs / 0 duplicates; class split TSEK-B:6 and TSEK-C:6 | `reports/benchmarks/latest_benchmark_summary.md` | none |
| v0.4.0 | Synthetic gate suite genesis | `python scripts/benchmarks/run_synthetic_gate_suite.py` | Seeds and charts generated; Markdown chart-link render failed | `reports/benchmarks/v0_4_0/synthetic_gate_suite_v0_4_0.json` | `visuals/benchmarks/v0_4_0/`, `visuals/findings/v0_4_0/` |
| v0.4.0a | Report-link repair | `python scripts/benchmarks/run_synthetic_gate_suite.py` | Reports rendered; 9/10 scenarios passed; one expectation mismatch found | `reports/benchmarks/latest_synthetic_gate_suite.md` | 18 charts |
| v0.4.0b | Expectation calibration | `python scripts/benchmarks/run_synthetic_gate_suite.py` | 10/10 scenarios passed; suite complete true | `reports/benchmarks/latest_synthetic_gate_suite.md` | 18 charts |
| v0.4.0c | Benchmark atlas | `python scripts/release/validate_release.py` | Adds benchmark/finding navigation and per-version chart registry | `docs/benchmarks/benchmark_atlas.md` | indexed charts |
| v0.4.1 | Sensitivity sweep | `python scripts/benchmarks/run_sensitivity_sweep.py` | Threshold curves for LogicFolding, gamma_tau_ETP, and overclaim pressure | `reports/sensitivity/latest_sensitivity_sweep.md` | `visuals/sensitivity/v0_4_1/` |

## Current Synthetic Suite Summary

| Metric | Value |
|---|---:|
| Total scenarios | 10 |
| Passed scenarios | 10 |
| Failed scenarios | 0 |
| Suite complete | True |
| Benchmark charts | 7 |
| Finding charts | 11 |

## Class Distribution

| Class | Count |
|---|---:|
| `TSEK-B` | 1 |
| `TSEK-C` | 7 |
| `TSEK-E` | 2 |

## Finding Frequency

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

## Benchmark Chart Registry

| Chart | Purpose | Path |
|---|---|---|
| `a_tsek_by_scenario.png` | Shows admissible A_TSEK score per scenario. | `visuals/benchmarks/v0_4_0/a_tsek_by_scenario.png` |
| `class_distribution.png` | Shows class distribution across synthetic scenarios. | `visuals/benchmarks/v0_4_0/class_distribution.png` |
| `diagnostic_average_by_scenario.png` | Shows diagnostic average per scenario. | `visuals/benchmarks/v0_4_0/diagnostic_average_by_scenario.png` |
| `elapsed_ms_by_scenario.png` | Shows local runtime duration per scenario. | `visuals/benchmarks/v0_4_0/elapsed_ms_by_scenario.png` |
| `finding_code_frequency.png` | Shows finding-code frequency across the suite. | `visuals/benchmarks/v0_4_0/finding_code_frequency.png` |
| `finding_count_by_scenario.png` | Shows number of findings per scenario. | `visuals/benchmarks/v0_4_0/finding_count_by_scenario.png` |
| `gate_heatmap.png` | Shows hard-gate pass/fail geometry across scenarios. | `visuals/benchmarks/v0_4_0/gate_heatmap.png` |

## Per-Finding Chart Registry

| Finding chart | Meaning | Path |
|---|---|---|
| `finding_b-baseline-missing.png` | Scenario presence chart for `b_baseline_missing`. | `visuals/findings/v0_4_0/finding_b-baseline-missing.png` |
| `finding_b-etp-missing.png` | Scenario presence chart for `b_etp_missing`. | `visuals/findings/v0_4_0/finding_b-etp-missing.png` |
| `finding_b-evidence-missing.png` | Scenario presence chart for `b_evidence_missing`. | `visuals/findings/v0_4_0/finding_b-evidence-missing.png` |
| `finding_b-lf-missing.png` | Scenario presence chart for `b_lf_missing`. | `visuals/findings/v0_4_0/finding_b-lf-missing.png` |
| `finding_b-method-missing.png` | Scenario presence chart for `b_method_missing`. | `visuals/findings/v0_4_0/finding_b-method-missing.png` |
| `finding_b-metric-missing.png` | Scenario presence chart for `b_metric_missing`. | `visuals/findings/v0_4_0/finding_b-metric-missing.png` |
| `finding_b-pvt-missing.png` | Scenario presence chart for `b_pvt_missing`. | `visuals/findings/v0_4_0/finding_b-pvt-missing.png` |
| `finding_b-tau-missing.png` | Scenario presence chart for `b_tau_missing`. | `visuals/findings/v0_4_0/finding_b-tau-missing.png` |
| `finding_b-workload-missing.png` | Scenario presence chart for `b_workload_missing`. | `visuals/findings/v0_4_0/finding_b-workload-missing.png` |
| `finding_b-yield-missing.png` | Scenario presence chart for `b_yield_missing`. | `visuals/findings/v0_4_0/finding_b-yield-missing.png` |
| `finding_overclaim-independent-validation.png` | Scenario presence chart for `overclaim_independent_validation`. | `visuals/findings/v0_4_0/finding_overclaim-independent-validation.png` |


## Interpretation

v0.4.0b is the first complete synthetic gate-test seal. It shows that the current classifier can distinguish:

- one promotable fully disclosed local scenario,
- seven controlled downgrade scenarios,
- two hard rejection / severe downgrade scenarios.

The most important operational finding was not just that the charts were generated. It was that the benchmark system caught two real benchmark-process failures:

1. v0.4.0 chart render path failure.
2. v0.4.0a expectation mismatch for multi-gate stress.

Both were converted into durable README lessons.

## Boundary

Synthetic gate suite validates local runtime downgrade behavior only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.

This atlas is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
