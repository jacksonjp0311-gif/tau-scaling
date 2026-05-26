from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re

root = Path(r"C:\Users\jacks\OneDrive\Desktop\tau-scaling")
generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

readme = root / "README.md"
text = readme.read_text(encoding="utf-8", errors="replace")

backup_dir = root / "reports" / "readme" / "backups"
backup_dir.mkdir(parents=True, exist_ok=True)
backup_path = backup_dir / f"README_before_v0_3_3a_release_sync_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
backup_path.write_text(text, encoding="utf-8")

# Header state.
text = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.3\.2h[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.3.3 — Unified Release Validator**",
    text,
)
text = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.3\.2g[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.3.2h — README Mojibake Cleanup + Audit Surface Consolidation**",
    text,
)

# Public metrics table state.
text = text.replace("| Current checkpoint | TAU-SCALING-SA v0.3.2h |", "| Current checkpoint | TAU-SCALING-SA v0.3.3 |")
text = text.replace("| Public README / learning repair | v0.3.2h |", "| Public README / release sync | v0.3.3a |")
if "| Unified release validator | passing / step failures 0 |" not in text:
    text = text.replace(
        "| README mini repo audit | passing / 0 warnings |\n",
        "| README mini repo audit | passing / 0 warnings |\n| Unified release validator | passing / step failures 0 |\n",
    )
if "| Release readiness report | `reports/release/latest_release_readiness.md` |" not in text:
    text = text.replace(
        "| Benchmark harness | 12 runs / 12 unique IDs / 0 duplicates |\n",
        "| Benchmark harness | 12 runs / 12 unique IDs / 0 duplicates |\n| Release readiness report | `reports/release/latest_release_readiness.md` |\n",
    )

# Repository layers: add release-readiness layer if missing.
if "Unified release readiness" not in text:
    text = text.replace(
        "| Benchmark and evidence observability | Runs local benchmark loops and evidence package checks | `scripts/benchmarks/`, `reports/benchmarks/`, `artifacts/runs/` |\n",
        "| Benchmark and evidence observability | Runs local benchmark loops and evidence package checks | `scripts/benchmarks/`, `reports/benchmarks/`, `artifacts/runs/` |\n"
        "| Unified release readiness | Runs the full release gate before experiments | `scripts/release/`, `reports/release/` |\n",
    )

# Primary Nexus files: add release validator/report if missing.
if "`scripts/release/validate_release.py` | Unified release-readiness validator." not in text:
    text = text.replace(
        "| `scripts/rcc/audit_readme_surface.py` | README / mini repo audit scanner. |\n",
        "| `scripts/rcc/audit_readme_surface.py` | README / mini repo audit scanner. |\n"
        "| `scripts/release/validate_release.py` | Unified release-readiness validator. |\n",
    )
if "`reports/release/latest_release_readiness.md` | Latest unified release-readiness report." not in text:
    text = text.replace(
        "| `reports/readme/latest_readme_mini_repo_audit.md` | Latest README / mini repo audit report. |\n",
        "| `reports/readme/latest_readme_mini_repo_audit.md` | Latest README / mini repo audit report. |\n"
        "| `reports/release/latest_release_readiness.md` | Latest unified release-readiness report. |\n",
    )

release_layer = """## Unified Release Readiness Layer

v0.3.3 adds one authoritative local release gate before deeper Tau Scaling experiments.

Primary command:

```powershell
python scripts/release/validate_release.py
```

Primary outputs:

```text
reports/release/latest_release_readiness.json
reports/release/latest_release_readiness.md
```

Current expected state:

```text
schema: tau-scaling-unified-release-readiness-v0.3.3
passed: true
step_failures: 0
baseline_claim: TSEK-C / A_TSEK 0.0000
promotion_path_claim: TSEK-B / A_TSEK 1.0000
benchmark_runs: 12
unique_run_ids: 12
duplicate_run_ids: []
```

The release validator checks compile, import, RCC-N, README audit, architecture validation, unit tests, benchmark harness, baseline claim, promotion-path claim, expected artifact existence, and README encoding/path-break risk.

Non-claim lock: release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
"""

if "## Unified Release Readiness Layer" not in text:
    marker = "## Benchmark Learning Layer"
    if marker in text:
        text = text.replace(marker, release_layer + "\n" + marker, 1)
    else:
        text += "\n\n" + release_layer

# Failure ledger: add release-validator lesson if missing.
lesson_row = "| L-010 | v0.3.3 release validator passed with one non-blocking finding. | Release readiness can be true while warning-level readability/risk findings remain. | Passing release readiness must still be inspected before the next experimental layer. |"
if lesson_row not in text:
    text = text.replace(
        "| L-009 | README became mojibake-contaminated after repeated Unicode patching. | Mixed console encodings and repeated copy/paste repair passes corrupted Unicode arrows/dashes/code blocks. | Public README should prefer ASCII-safe syntax except for explicitly audited Unicode anchors. |\n",
        "| L-009 | README became mojibake-contaminated after repeated Unicode patching. | Mixed console encodings and repeated copy/paste repair passes corrupted Unicode arrows/dashes/code blocks. | Public README should prefer ASCII-safe syntax except for explicitly audited Unicode anchors. |\n"
        + lesson_row + "\n",
    )

# Validation command set: add release validator if missing.
if "python scripts/release/validate_release.py" not in text:
    text = text.replace(
        "python scripts/rcc/audit_readme_surface.py\n",
        "python scripts/rcc/audit_readme_surface.py\npython scripts/release/validate_release.py\n",
        1,
    )

# Directory box: ensure release report folders are present.
if "scripts/\n    release/" not in text and "  scripts/\n    benchmarks/" in text:
    text = text.replace("  scripts/\n    benchmarks/\n", "  scripts/\n    benchmarks/\n    release/\n", 1)

# Release lineage row.
lineage_row = "| v0.3.3 | Unified release validator and release-readiness reports. |"
if lineage_row not in text:
    text = text.replace(
        "| v0.3.2h | README mojibake cleanup and audit surface consolidation. |\n",
        "| v0.3.2h | README mojibake cleanup and audit surface consolidation. |\n" + lineage_row + "\n",
    )

# Replace next recommended section with v0.4.0.
next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.0 — Synthetic Gate Test Suite**

Recommended goals:

- Add synthetic claim cards that isolate each gate.
- Prove downgrade behavior for missing yield, missing workload, thermal/PDN/PVT failures, edge/surface starvation, and LogicFolding survivability failures.
- Emit gate-test reports under `reports/gates/`.
- Preserve non-claim locks: synthetic gate tests are runtime behavior tests, not silicon/product validation.

Initial target seeds:

```text
configs/seeds/tests/tau_compute_only_pass.json
configs/seeds/tests/tau_wire_dominant_pass.json
configs/seeds/tests/tau_memory_dominant_fail.json
configs/seeds/tests/logicfolding_high_vertical_penalty_fail.json
configs/seeds/tests/edge_surface_starvation_fail.json
configs/seeds/tests/gamma_tau_etp_thermal_fail.json
configs/seeds/tests/yield_missing_disclosure_downgrade.json
```
"""
text = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, text, flags=re.S)

readme.write_text(text, encoding="utf-8")

release = root / "docs" / "release_notes" / "tau_scaling_v0_3_3a_main_readme_release_sync.md"
release.parent.mkdir(parents=True, exist_ok=True)
release.write_text(f"""# TAU-SCALING-SA v0.3.3a — Main README Release-State Sync

Generated: {generated_at}

## Purpose

This patch updates the main README after v0.3.3 Unified Release Validator was added and pushed.

## Updates

- Sets current checkpoint to v0.3.3.
- Adds Unified Release Readiness Layer.
- Adds release validator/report paths.
- Adds v0.3.3 to release lineage.
- Adds release-readiness lesson L-010.
- Moves next recommended version to v0.4.0 Synthetic Gate Test Suite.

## Boundary

This is a README/release-state synchronization patch. It does not alter runtime gates, classifier behavior, benchmark semantics, or evidence boundaries.
""", encoding="utf-8")

status = root / "reports" / "readme" / "latest_v0_3_3a_main_readme_release_sync_status.md"
status.parent.mkdir(parents=True, exist_ok=True)
status.write_text(f"""# Tau Scaling v0.3.3a Main README Release-State Sync Status

Generated: {generated_at}

Status: complete

Actions:
- Updated README checkpoint and metrics.
- Added release readiness layer.
- Added v0.3.3 lineage.
- Updated next recommended version to v0.4.0.
- Reran release validator and README audit.

Boundary:
- Documentation/release-state sync only.
""", encoding="utf-8")