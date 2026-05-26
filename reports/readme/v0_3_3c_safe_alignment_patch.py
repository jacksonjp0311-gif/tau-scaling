from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re

root = Path.cwd()
generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

readme = root / "README.md"
text = readme.read_text(encoding="utf-8", errors="replace")

backup_dir = root / "reports" / "readme" / "backups"
backup_dir.mkdir(parents=True, exist_ok=True)
backup = backup_dir / f"README_before_v0_3_3c_safe_alignment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
backup.write_text(text, encoding="utf-8")

# Current public state.
text = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.3\.3[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.3.3c — Safe README Process Alignment Repair**",
    text,
)
text = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.3\.2h[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.3.3a — Main README Release-State Sync**",
    text,
)
text = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.3\.3a[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.3.3a — Main README Release-State Sync**",
    text,
)
text = text.replace("| Current checkpoint | TAU-SCALING-SA v0.3.3 |", "| Current checkpoint | TAU-SCALING-SA v0.3.3c |")
text = text.replace("| Current checkpoint | TAU-SCALING-SA v0.3.3b |", "| Current checkpoint | TAU-SCALING-SA v0.3.3c |")
text = text.replace("| Public README / release sync | v0.3.3a |", "| Public README / process alignment | v0.3.3c |")
text = text.replace("| Public README / process alignment | v0.3.3b |", "| Public README / process alignment | v0.3.3c |")

# Quick Start should include release validator once.
head, sep, tail = text.partition("## Repository Layers")
if "python scripts/release/validate_release.py" not in head:
    head = head.replace(
        "python scripts/benchmarks/run_tau_scaling_benchmarks.py",
        "python scripts/benchmarks/run_tau_scaling_benchmarks.py\npython scripts/release/validate_release.py",
        1,
    )
text = head + sep + tail

# Patch routing should route release changes through validator.
text = text.replace(
    "| Release / benchmark patch | `releases/`, `docs/benchmarks/`, `reports/benchmarks/` | full validation set |",
    "| Release / benchmark patch | `releases/`, `docs/benchmarks/`, `reports/benchmarks/`, `reports/release/` | `python scripts/release/validate_release.py` |",
)

# Latest reports scan should include reports/release.
text = text.replace(
    "| 10 | Latest reports | `reports/rcc_nexus/`, `reports/architecture/`, `reports/readme/`, and `reports/benchmarks/`. |",
    "| 10 | Latest reports | `reports/rcc_nexus/`, `reports/architecture/`, `reports/readme/`, `reports/benchmarks/`, and `reports/release/`. |",
)

# Required validation block should include release validator once.
marker = "### Required Validation"
end_marker = "## AI Failure Learning Ledger"
if marker in text and end_marker in text:
    before, rest = text.split(marker, 1)
    block, after = rest.split(end_marker, 1)
    if "python scripts/release/validate_release.py" not in block:
        block = block.replace(
            "python -m tau_scaling run-claim --seed configs/seeds/logicfolding_promotion_path_claim_card.json",
            "python -m tau_scaling run-claim --seed configs/seeds/logicfolding_promotion_path_claim_card.json\npython scripts/release/validate_release.py",
        )
    text = before + marker + block + end_marker + after

# Fix duplicate scripts/release in directory box.
text = text.replace(
    "  scripts/\n    benchmarks/\n    release/\n    maintenance/\n    rcc/\n    release/\n    validation/",
    "  scripts/\n    benchmarks/\n    maintenance/\n    rcc/\n    release/\n    validation/",
)

process_layer = """## Process Alignment Layer

This layer keeps the repository synchronized after every evolution step.

### Alignment Rules

| Rule | Requirement |
|---|---|
| Version-state rule | After every commit that changes runtime, reports, validators, or public docs, the main README current checkpoint must be updated. |
| Release-readiness rule | `python scripts/release/validate_release.py` is the final local gate before commit/push. |
| Warning-inspection rule | A passing validator with warnings is not ignored; warning findings must be inspected and either repaired or explicitly classified as non-blocking. |
| Directory-box rule | The Full Directory Box must not contain duplicate top-level or durable child entries. |
| File-run rule | Large repair scripts must be run with `powershell -File`, not pasted line by line. |
| Experiment-start rule | No v0.4+ Tau Scaling experiment starts until release readiness, README audit, and unit tests pass. |
| Boundary rule | Process alignment is repository hygiene. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, or universal-law proof. |

### Pre-Experiment Checklist

```powershell
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python -m unittest discover -s tests
```

Expected minimum state:

```text
release_readiness: passed
step_failures: 0
README audit: passed
unit_tests: OK
```
"""

if "## Process Alignment Layer" not in text:
    text = text.replace("## AI Rule — Directory Box and Mini README Synchronization", process_layer + "\n## AI Rule — Directory Box and Mini README Synchronization", 1)
else:
    # Ensure file-run rule exists.
    if "File-run rule" not in text:
        text = text.replace(
            "| Directory-box rule | The Full Directory Box must not contain duplicate top-level or durable child entries. |",
            "| Directory-box rule | The Full Directory Box must not contain duplicate top-level or durable child entries. |\n| File-run rule | Large repair scripts must be run with `powershell -File`, not pasted line by line. |",
        )

# Learning rows.
rows = [
    "| L-011 | README release-state drift recurred after v0.3.3. | The release validator was added and pushed before the public README was fully synchronized. | Every release patch must update README checkpoint, metrics, lineage, next target, and process rules before promotion. |",
    "| L-012 | v0.3.3b repair failed when pasted line by line. | PowerShell line wrapping split paths such as `reports\\readme` and `scripts\\release`. | Large scripts must be run from downloaded `.ps1` files using `powershell -ExecutionPolicy Bypass -File ...`. |",
]
for row in rows:
    if row not in text:
        insert_after = "| L-010 | v0.3.3 release validator passed with one non-blocking finding. | Release readiness can be true while warning-level readability/risk findings remain. | Passing release readiness must still be inspected before the next experimental layer. |"
        if insert_after in text:
            text = text.replace(insert_after, insert_after + "\n" + row, 1)

# Release lineage.
for row in [
    "| v0.3.3a | Main README release-state synchronization. |",
    "| v0.3.3c | Safe README process alignment repair after pasted-script path break. |",
]:
    if row not in text:
        text = text.replace("| v0.3.3 | Unified release validator and release-readiness reports. |", "| v0.3.3 | Unified release validator and release-readiness reports. |\n" + row, 1)

# Keep v0.4.0 next target.
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

# Create protocol.
protocol = root / "docs" / "protocols" / "process_alignment_protocol.md"
protocol.parent.mkdir(parents=True, exist_ok=True)
protocol.write_text(f"""# Tau Scaling Process Alignment Protocol

Generated: {generated_at}

## Purpose

This protocol prevents repository drift after each Tau Scaling evolution step.

## Required Promotion Sequence

1. Patch the intended runtime/documentation/report surface.
2. Update the root README checkpoint, metrics, release lineage, and next target.
3. Update affected mini READMEs and route maps when directory meaning changes.
4. Run `python scripts/release/validate_release.py`.
5. Inspect warnings even when `passed: true`.
6. Run `python scripts/rcc/audit_readme_surface.py`.
7. Run `python -m unittest discover -s tests`.
8. Commit only after validator, README audit, and tests pass.
9. Push only after the README public state matches the actual repo state.

## Hard Rules

- A release is not aligned if README still points to the previous next version.
- A release is not aligned if the Full Directory Box contains duplicate durable entries.
- A release is not aligned if validator warnings are ignored.
- A release is not aligned if public claims imply silicon/product validation.
- Large repair scripts must be run as files, not pasted line by line.

## Non-Claim Lock

Process alignment improves repository hygiene and experiment discipline. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
""", encoding="utf-8")

release = root / "docs" / "release_notes" / "tau_scaling_v0_3_3c_safe_readme_process_alignment.md"
release.parent.mkdir(parents=True, exist_ok=True)
release.write_text(f"""# TAU-SCALING-SA v0.3.3c — Safe README Process Alignment Repair

Generated: {generated_at}

## Purpose

This patch safely reapplies README process alignment after the v0.3.3b script was pasted line by line and PowerShell split paths.

## Updates

- Sets current checkpoint to v0.3.3c.
- Fixes duplicate `scripts/release/` directory-box entry.
- Adds Process Alignment Layer.
- Adds File-run rule.
- Adds L-012 failure-learning lesson.
- Adds process alignment protocol.
- Keeps v0.4.0 as the next experimental target.

## Boundary

This is process/readme repair only. It does not alter Tau Scaling gate math, classifier thresholds, evidence semantics, or claim classes.
""", encoding="utf-8")

status = root / "reports" / "readme" / "latest_v0_3_3c_safe_readme_process_alignment_status.md"
status.parent.mkdir(parents=True, exist_ok=True)
status.write_text(f"""# Tau Scaling v0.3.3c Safe README Process Alignment Status

Generated: {generated_at}

Status: complete

Boundary:
- Repository alignment only.
""", encoding="utf-8")