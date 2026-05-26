from __future__ import annotations

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

def backup(path: Path, label: str) -> None:
    if path.exists():
        dest = ROOT / "reports" / "benchmarks" / "v0_4_0a" / "backups" / f"{path.name}_before_v0_4_0a_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner = ROOT / "scripts" / "benchmarks" / "run_synthetic_gate_suite.py"
backup(runner, "runner")
text = read(runner)

# Fix chart markdown links: reports/benchmarks/v0_4_0 markdown cannot relative_to visuals path.
# Use GitHub-safe repo-root relative links from reports/benchmarks/v0_4_0 to ../../../visuals/...
text = text.replace(
    'rel = Path(REPO_ROOT / chart).relative_to(REPORT_DIR).as_posix()',
    'rel = Path("../../../") / chart\n            rel = rel.as_posix()',
)

# Ensure the suite fails before reports are considered complete when scenario expectations fail.
if '"suite_complete": summary["all_scenarios_passed"]' not in text:
    text = text.replace(
        '"chart_count": len(charts), "report": "reports/benchmarks/latest_synthetic_gate_suite.md"}, indent=2, sort_keys=True))',
        '"chart_count": len(charts), "suite_complete": summary["all_scenarios_passed"], "report": "reports/benchmarks/latest_synthetic_gate_suite.md"}, indent=2, sort_keys=True))',
    )

write(runner, text)

# Update README to v0.4.0a repair checkpoint.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.0[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.0a - Synthetic Gate Report Link Repair**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.3\.3e[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.0 - Synthetic Gate Test Suite + Benchmark Finding Charts**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.0 \|", "| Current checkpoint | TAU-SCALING-SA v0.4.0a |", r)
if "| Synthetic gate report links | repaired / v0.4.0a |" not in r:
    r = r.replace(
        "| Synthetic gate report | `reports/gates/latest_synthetic_gate_report.md` |\n",
        "| Synthetic gate report | `reports/gates/latest_synthetic_gate_report.md` |\n| Synthetic gate report links | repaired / v0.4.0a |\n",
    )

lesson = "| L-015 | v0.4.0 synthetic suite generated charts but failed Markdown rendering. | The report renderer tried to make visual paths relative to `reports/benchmarks/v0_4_0`, although visuals live outside that subtree. | Benchmark reports must use repo-root-safe relative links for visuals, and failed synthetic-suite runs must be repaired before being treated as complete. |"
if lesson not in r and "| L-014 |" in r:
    r = r.replace(
        "| L-014 | README contract became more advanced than AGENTS.md and task routing matrix. | Human-facing Nexus evolved faster than agent-facing operating contract. | Agent contracts and routing matrices must be synchronized before experiments begin. |\n",
        "| L-014 | README contract became more advanced than AGENTS.md and task routing matrix. | Human-facing Nexus evolved faster than agent-facing operating contract. | Agent contracts and routing matrices must be synchronized before experiments begin. |\n" + lesson + "\n",
    )

if "| v0.4.0a | Synthetic gate report link repair and complete report regeneration. |" not in r:
    r = r.replace(
        "| v0.4.0 | Synthetic gate suite with benchmark charts and finding charts. |\n",
        "| v0.4.0 | Synthetic gate suite with benchmark charts and finding charts. |\n| v0.4.0a | Synthetic gate report link repair and complete report regeneration. |\n",
    )

write(readme, r)

# Release note + status
write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_0a_synthetic_gate_report_link_repair.md", f"""# TAU-SCALING-SA v0.4.0a - Synthetic Gate Report Link Repair

Generated: {GENERATED_AT}

## Purpose

Repair the v0.4.0 synthetic gate report renderer after charts were generated but Markdown report rendering failed.

## Root Cause

`run_synthetic_gate_suite.py` attempted to compute image links with:

```python
Path(REPO_ROOT / chart).relative_to(REPORT_DIR)
```

That fails because chart files live under `visuals/`, while `REPORT_DIR` is `reports/benchmarks/v0_4_0`.

## Repair

The Markdown renderer now emits repo-root-safe relative links from `reports/benchmarks/v0_4_0` to `visuals/...`.

## Required Validation

```powershell
python scripts/benchmarks/run_synthetic_gate_suite.py
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
```

## Boundary

This repair affects report rendering only. It does not alter Tau Scaling gate math, classifier thresholds, silicon evidence, product evidence, manufacturing evidence, or universal-law claims.
""")

write(ROOT / "reports" / "benchmarks" / "v0_4_0a" / "latest_v0_4_0a_repair_status.md", f"""# Tau Scaling v0.4.0a Repair Status

Generated: {GENERATED_AT}

Status: patched; validation must pass before commit/push.

Repair:
- Fixed synthetic gate suite chart Markdown links.
- Added L-015 failure-learning lesson.
- Updated README checkpoint and release lineage.

Boundary:
- Report rendering repair only.
""")

print("v0.4.0a repair patch written")
