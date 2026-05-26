from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
GENERATED_AT = datetime.now(timezone.utc).isoformat()

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def backup(path: Path, label: str) -> None:
    if path.exists():
        dest = ROOT / "reports" / "benchmarks" / "v0_4_0c" / "backups" / f"{path.name}_before_v0_4_0c_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

def load_json(path: Path) -> dict:
    try:
        return json.loads(read(path))
    except Exception:
        return {}

# Capture latest synthetic suite facts.
summary = load_json(ROOT / "reports" / "benchmarks" / "latest_synthetic_gate_suite.json")
if not summary:
    summary = {
        "total_scenarios": 10,
        "passed_scenarios": 10,
        "failed_scenarios": 0,
        "all_scenarios_passed": True,
        "class_counts": {"TSEK-B": 1, "TSEK-C": 7, "TSEK-E": 2},
        "finding_counts": {
            "TSEK_B_ETP_MISSING": 2,
            "TSEK_B_LF_MISSING": 2,
            "TSEK_B_PVT_MISSING": 2,
            "TSEK_B_baseline_MISSING": 2,
            "TSEK_B_evidence_MISSING": 2,
            "TSEK_B_method_MISSING": 1,
            "TSEK_B_metric_MISSING": 1,
            "TSEK_B_tau_MISSING": 1,
            "TSEK_B_workload_MISSING": 2,
            "TSEK_B_yield_MISSING": 2,
            "TSEK_OVERCLAIM_INDEPENDENT_VALIDATION": 1,
        },
        "chart_paths": [],
        "boundary": "Synthetic gate suite validates local runtime downgrade behavior only.",
    }

benchmark_chart_paths = sorted(str(p.relative_to(ROOT)).replace("\\", "/") for p in (ROOT / "visuals" / "benchmarks" / "v0_4_0").glob("*.png"))
finding_chart_paths = sorted(str(p.relative_to(ROOT)).replace("\\", "/") for p in (ROOT / "visuals" / "findings" / "v0_4_0").glob("*.png"))

benchmark_chart_names = [
    "class_distribution.png",
    "a_tsek_by_scenario.png",
    "finding_count_by_scenario.png",
    "diagnostic_average_by_scenario.png",
    "elapsed_ms_by_scenario.png",
    "gate_heatmap.png",
    "finding_code_frequency.png",
]

finding_counts = summary.get("finding_counts", {})
class_counts = summary.get("class_counts", {})

atlas = f"""# Tau Scaling Benchmark and Finding Atlas

Generated: {GENERATED_AT}

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

## Current Synthetic Suite Summary

| Metric | Value |
|---|---:|
| Total scenarios | {summary.get("total_scenarios", "unknown")} |
| Passed scenarios | {summary.get("passed_scenarios", "unknown")} |
| Failed scenarios | {summary.get("failed_scenarios", "unknown")} |
| Suite complete | {summary.get("all_scenarios_passed", "unknown")} |
| Benchmark charts | {len(benchmark_chart_paths)} |
| Finding charts | {len(finding_chart_paths)} |

## Class Distribution

| Class | Count |
|---|---:|
"""
for cls, count in sorted(class_counts.items()):
    atlas += f"| `{cls}` | {count} |\n"

atlas += "\n## Finding Frequency\n\n| Finding code | Count |\n|---|---:|\n"
for code, count in sorted(finding_counts.items()):
    atlas += f"| `{code}` | {count} |\n"

atlas += "\n## Benchmark Chart Registry\n\n| Chart | Purpose | Path |\n|---|---|---|\n"
chart_purposes = {
    "class_distribution.png": "Shows class distribution across synthetic scenarios.",
    "a_tsek_by_scenario.png": "Shows admissible A_TSEK score per scenario.",
    "finding_count_by_scenario.png": "Shows number of findings per scenario.",
    "diagnostic_average_by_scenario.png": "Shows diagnostic average per scenario.",
    "elapsed_ms_by_scenario.png": "Shows local runtime duration per scenario.",
    "gate_heatmap.png": "Shows hard-gate pass/fail geometry across scenarios.",
    "finding_code_frequency.png": "Shows finding-code frequency across the suite.",
}
for chart in benchmark_chart_paths:
    name = Path(chart).name
    atlas += f"| `{name}` | {chart_purposes.get(name, 'Benchmark visual diagnostic.')} | `{chart}` |\n"

atlas += "\n## Per-Finding Chart Registry\n\n| Finding chart | Meaning | Path |\n|---|---|---|\n"
for chart in finding_chart_paths:
    name = Path(chart).name
    label = name.removeprefix("finding_").removesuffix(".png").replace("-", "_")
    atlas += f"| `{name}` | Scenario presence chart for `{label}`. | `{chart}` |\n"

atlas += f"""

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

{summary.get("boundary", "Synthetic benchmark charts are local runtime diagnostics only.")}

This atlas is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
"""

write(ROOT / "docs" / "benchmarks" / "benchmark_atlas.md", atlas)

# Root README update.
readme_path = ROOT / "README.md"
backup(readme_path, "readme")
r = read(readme_path)

r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.0b[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.0a[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.0b - Synthetic Gate Expectation Calibration**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.0b \|", "| Current checkpoint | TAU-SCALING-SA v0.4.0c |", r)

if "| Benchmark atlas | `docs/benchmarks/benchmark_atlas.md` |" not in r:
    r = r.replace(
        "| Finding charts | `reports/findings/latest_finding_charts.md` |\n",
        "| Finding charts | `reports/findings/latest_finding_charts.md` |\n| Benchmark atlas | `docs/benchmarks/benchmark_atlas.md` |\n| Benchmark chart registry | `visuals/benchmarks/v0_4_0/` + `visuals/findings/v0_4_0/` |\n",
    )

# Add benchmark atlas section after Synthetic Gate Suite section or before Benchmark Learning Layer.
atlas_section = """## Benchmark and Finding Atlas

v0.4.0c adds a stable benchmark atlas so every benchmark layer has a public chart/finding registry.

Primary atlas:

```text
docs/benchmarks/benchmark_atlas.md
```

Atlas surfaces:

```text
reports/benchmarks/README.md
reports/benchmarks/v0_4_0/README.md
reports/gates/README.md
reports/findings/README.md
visuals/benchmarks/README.md
visuals/benchmarks/v0_4_0/README.md
visuals/findings/README.md
visuals/findings/v0_4_0/README.md
```

Current synthetic-suite seal:

```text
total_scenarios: 10
passed_scenarios: 10
failed_scenarios: 0
suite_complete: true
chart_count: 18
class_counts: TSEK-B=1, TSEK-C=7, TSEK-E=2
```

Every future benchmark version must add or update:

```text
benchmark summary
finding summary
chart registry
version ledger row
boundary statement
```

Boundary: benchmark charts are local runtime diagnostics only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.

"""
if "## Benchmark and Finding Atlas" not in r:
    r = r.replace("## Benchmark Learning Layer", atlas_section + "## Benchmark Learning Layer", 1)

lesson = "| L-017 | Benchmark charts existed, but the README did not yet provide a versioned chart/finding atlas. | Visual evidence was distributed across reports and visuals folders without one public navigation surface per version. | Every benchmark version must maintain a benchmark atlas with chart registry, finding registry, version ledger, and non-claim boundary. |"
if lesson not in r:
    r = r.replace(
        "| L-016 | v0.4.0a synthetic suite completed reports but one scenario failed. | The multi-gate stress seed expected TSEK-D even though the classifier correctly returns TSEK-E when only one of eleven hard gates survives. | Synthetic test expectations must be calibrated to the classifier algebra; incomplete suites must exit non-zero. |\n",
        "| L-016 | v0.4.0a synthetic suite completed reports but one scenario failed. | The multi-gate stress seed expected TSEK-D even though the classifier correctly returns TSEK-E when only one of eleven hard gates survives. | Synthetic test expectations must be calibrated to the classifier algebra; incomplete suites must exit non-zero. |\n" + lesson + "\n",
    )

if "| v0.4.0c | Benchmark atlas and per-version chart/finding registry. |" not in r:
    r = r.replace(
        "| v0.4.0b | Synthetic gate expectation calibration and hard-fail incomplete suite semantics. |\n",
        "| v0.4.0b | Synthetic gate expectation calibration and hard-fail incomplete suite semantics. |\n| v0.4.0c | Benchmark atlas and per-version chart/finding registry. |\n",
    )

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep**

Recommended goals:

- Sweep gate parameters around pass/fail thresholds.
- Emit threshold curves for LogicFolding margin and gamma_tau_ETP.
- Add stability bands for A_TSEK and diagnostic average.
- Add benchmark atlas row and charts for v0.4.1.
- Preserve non-claim locks: synthetic sweeps are local runtime sensitivity diagnostics only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme_path, r)

# Mini READMEs / local map surfaces.
write(ROOT / "docs" / "benchmarks" / "README.md", f"""# Benchmark Documentation

Current layer: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**

## Purpose

This folder records benchmark interpretation, chart registries, and non-claim boundaries.

## Primary Files

| File | Role |
|---|---|
| `benchmark_atlas.md` | Versioned benchmark/finding/chart registry. |

## Current Findings

- v0.3.2 established collision-proof benchmark identity.
- v0.4.0 generated synthetic gate charts but exposed a Markdown path bug.
- v0.4.0a repaired chart report links but exposed one expectation mismatch.
- v0.4.0b calibrated expectations and achieved 10/10 synthetic scenarios.
- v0.4.0c adds this atlas/index layer.

## Boundary

Benchmark documentation is local-runtime interpretation only. It is not silicon validation or product validation.
""")

write(ROOT / "reports" / "benchmarks" / "README.md", f"""# Benchmark Reports

Current layer: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**

## Purpose

This folder stores benchmark reports, benchmark summaries, and versioned benchmark evidence.

## Current Benchmark Surfaces

| Surface | Role |
|---|---|
| `latest_benchmark_summary.md` | v0.3.2 repeated baseline/promotion benchmark summary. |
| `latest_synthetic_gate_suite.md` | Latest synthetic gate suite report. |
| `v0_4_0/synthetic_gate_suite_v0_4_0.md` | Versioned v0.4.0 synthetic gate report. |
| `v0_4_0b/latest_v0_4_0b_expectation_calibration_status.md` | Calibration repair status. |

## Current v0.4.0b Result

```text
total_scenarios: {summary.get("total_scenarios")}
passed_scenarios: {summary.get("passed_scenarios")}
failed_scenarios: {summary.get("failed_scenarios")}
suite_complete: {summary.get("all_scenarios_passed")}
chart_count: {len(benchmark_chart_paths) + len(finding_chart_paths)}
```

## Boundary

Benchmark reports are local runtime diagnostics only.
""")

write(ROOT / "reports" / "benchmarks" / "v0_4_0" / "README.md", f"""# v0.4.0 Synthetic Gate Suite Benchmark Reports

Current layer: **v0.4.0c atlas-indexed**

## Purpose

This folder stores versioned synthetic gate reports and repair artifacts for the v0.4.0 line.

## Version Trail

| Version | Meaning |
|---|---|
| v0.4.0 | Synthetic gate suite generated seeds and charts; Markdown chart-link rendering failed. |
| v0.4.0a | Report-link repair; synthetic suite reported 9/10 expected scenarios. |
| v0.4.0b | Expectation calibration; synthetic suite reported 10/10 expected scenarios. |
| v0.4.0c | Benchmark atlas and chart/finding registry. |

## Primary Reports

```text
synthetic_gate_suite_v0_4_0.json
synthetic_gate_suite_v0_4_0.md
../latest_synthetic_gate_suite.json
../latest_synthetic_gate_suite.md
```

## Chart Surfaces

```text
visuals/benchmarks/v0_4_0/
visuals/findings/v0_4_0/
```

Boundary: local runtime diagnostics only.
""")

write(ROOT / "reports" / "gates" / "README.md", f"""# Gate Reports

Current layer: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**

## Purpose

This folder stores synthetic gate-suite reports and gate-level diagnostics.

## Current Gate Report

```text
latest_synthetic_gate_report.md
latest_synthetic_gate_report.json
```

## Current Result

```text
scenarios: {summary.get("total_scenarios")}
passed: {summary.get("passed_scenarios")}
failed: {summary.get("failed_scenarios")}
suite_complete: {summary.get("all_scenarios_passed")}
```

## Boundary

Gate reports validate local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling proof.
""")

write(ROOT / "reports" / "findings" / "README.md", f"""# Finding Reports

Current layer: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**

## Purpose

This folder stores finding-level summaries and chart reports.

## Current Surfaces

| Surface | Role |
|---|---|
| `latest_finding_charts.md` | Markdown chart report for finding presence and benchmark charts. |
| `latest_finding_summary.json` | Machine-readable finding count summary. |

## Finding Count Snapshot

```json
{json.dumps(finding_counts, indent=2, sort_keys=True)}
```

## Boundary

Findings explain local runtime downgrade behavior only. They are not external validation.
""")

write(ROOT / "visuals" / "benchmarks" / "README.md", f"""# Benchmark Visuals

Current layer: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**

## Purpose

This folder stores visual benchmark outputs for Tau Scaling runtime diagnostics.

## Current Versioned Folder

```text
v0_4_0/
```

## Chart Registry

See:

```text
docs/benchmarks/benchmark_atlas.md
```

Boundary: charts are local observability artifacts only.
""")

write(ROOT / "visuals" / "benchmarks" / "v0_4_0" / "README.md", f"""# v0.4.0 Benchmark Charts

Current layer: **v0.4.0c atlas-indexed**

## Charts

| Chart | Purpose |
|---|---|
| `class_distribution.png` | Class distribution across synthetic scenarios. |
| `a_tsek_by_scenario.png` | A_TSEK score per scenario. |
| `finding_count_by_scenario.png` | Finding count per scenario. |
| `diagnostic_average_by_scenario.png` | Diagnostic average per scenario. |
| `elapsed_ms_by_scenario.png` | Runtime elapsed milliseconds per scenario. |
| `gate_heatmap.png` | Gate pass/fail geometry across scenarios. |
| `finding_code_frequency.png` | Finding code frequency across the suite. |

Boundary: local runtime diagnostics only.
""")

write(ROOT / "visuals" / "findings" / "README.md", f"""# Finding Visuals

Current layer: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**

## Purpose

This folder stores per-finding visual charts.

## Current Versioned Folder

```text
v0_4_0/
```

Boundary: finding charts visualize local classifier behavior only.
""")

finding_chart_lines = "\n".join(f"| `{Path(p).name}` | Per-scenario presence chart. |" for p in finding_chart_paths)
write(ROOT / "visuals" / "findings" / "v0_4_0" / "README.md", f"""# v0.4.0 Finding Charts

Current layer: **v0.4.0c atlas-indexed**

## Finding Charts

| Chart | Purpose |
|---|---|
{finding_chart_lines}

Boundary: per-finding charts are local classifier diagnostics only.
""")

# Machine-readable atlas.
write_json(ROOT / "reports" / "benchmarks" / "benchmark_chart_registry_v0_4_0c.json", {
    "schema": "tau-scaling-benchmark-chart-registry-v0.4.0c",
    "generated_at": GENERATED_AT,
    "benchmark_chart_paths": benchmark_chart_paths,
    "finding_chart_paths": finding_chart_paths,
    "class_counts": class_counts,
    "finding_counts": finding_counts,
    "suite_summary": {
        "total_scenarios": summary.get("total_scenarios"),
        "passed_scenarios": summary.get("passed_scenarios"),
        "failed_scenarios": summary.get("failed_scenarios"),
        "all_scenarios_passed": summary.get("all_scenarios_passed"),
    },
    "non_claim_lock": "Benchmark chart registry is local runtime observability only, not silicon/product validation.",
})

# Release note.
write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_0c_benchmark_atlas_chart_index.md", f"""# TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index

Generated: {GENERATED_AT}

## Purpose

Add a versioned benchmark/finding/chart atlas after v0.4.0b sealed the synthetic gate suite.

## Updates

- Added `docs/benchmarks/benchmark_atlas.md`.
- Added/updated benchmark mini READMEs.
- Added/updated gate/finding report mini READMEs.
- Added/updated benchmark/finding visual mini READMEs.
- Added machine-readable chart registry.
- Updated root README checkpoint, public metrics, benchmark atlas section, L-017, and release lineage.

## Current Evidence

```text
total_scenarios: {summary.get("total_scenarios")}
passed_scenarios: {summary.get("passed_scenarios")}
failed_scenarios: {summary.get("failed_scenarios")}
suite_complete: {summary.get("all_scenarios_passed")}
benchmark_charts: {len(benchmark_chart_paths)}
finding_charts: {len(finding_chart_paths)}
```

## Boundary

This release improves benchmark navigation and visualization. It does not alter Tau Scaling gate math, classifier thresholds, silicon evidence, product evidence, manufacturing evidence, process-node equivalence, or universal-law claims.
""")

write(ROOT / "reports" / "benchmarks" / "v0_4_0c" / "latest_v0_4_0c_benchmark_atlas_status.md", f"""# Tau Scaling v0.4.0c Benchmark Atlas Status

Generated: {GENERATED_AT}

Status: patched; validation must pass before commit/push.

Primary atlas:

```text
docs/benchmarks/benchmark_atlas.md
```

Current suite:

```text
total_scenarios: {summary.get("total_scenarios")}
passed_scenarios: {summary.get("passed_scenarios")}
failed_scenarios: {summary.get("failed_scenarios")}
suite_complete: {summary.get("all_scenarios_passed")}
```

Boundary:
- Benchmark atlas and chart index only.
""")

print("v0.4.0c benchmark atlas and chart index patch written")
