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
        dest = ROOT / "reports" / "benchmarks" / "v0_4_0d" / "backups" / f"{path.name}_before_v0_4_0d_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

AI_RULE = """
## AI / RCC Update Rule

If benchmark commands, reports, charts, folders, or interpretation boundaries change, update this mini README, the root `README.md`, `docs/benchmarks/benchmark_atlas.md`, and the relevant RCC route surfaces in the same commit.

Required follow-up validation:

```powershell
python scripts/rcc/audit_readme_surface.py
python scripts/release/validate_release.py
```

Non-claim lock: AI/RCC update guidance improves navigation and context alignment only. It is not code correctness, silicon validation, product validation, benchmark superiority proof, or universal Tau Scaling proof.
"""

targets = [
    ROOT / "docs" / "benchmarks" / "README.md",
    ROOT / "reports" / "benchmarks" / "README.md",
]

for target in targets:
    backup(target, target.parent.name)
    text = read(target).rstrip() + "\n"
    if "## AI / RCC Update Rule" not in text:
        text += AI_RULE
    write(target, text)

# Update README checkpoint and metrics.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)

r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.0c[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.0d - Benchmark Mini README AI/RCC Warning Repair**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.0b[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.0c \|", "| Current checkpoint | TAU-SCALING-SA v0.4.0d |", r)

if "| Benchmark mini README AI/RCC guidance | repaired / expected 0 warnings |" not in r:
    r = r.replace(
        "| Benchmark atlas | `docs/benchmarks/benchmark_atlas.md` |\n",
        "| Benchmark atlas | `docs/benchmarks/benchmark_atlas.md` |\n| Benchmark mini README AI/RCC guidance | repaired / expected 0 warnings |\n",
    )

lesson = "| L-018 | v0.4.0c benchmark atlas passed but README audit found two warnings. | `docs/benchmarks/README.md` and `reports/benchmarks/README.md` lacked explicit AI/RCC update guidance. | Every benchmark mini README must include an AI/RCC update rule when benchmark charts, reports, or interpretation surfaces change. |"
if lesson not in r:
    r = r.replace(
        "| L-017 | Benchmark charts existed, but the README did not yet provide a versioned chart/finding atlas. | Visual evidence was distributed across reports and visuals folders without one public navigation surface per version. | Every benchmark version must maintain a benchmark atlas with chart registry, finding registry, version ledger, and non-claim boundary. |\n",
        "| L-017 | Benchmark charts existed, but the README did not yet provide a versioned chart/finding atlas. | Visual evidence was distributed across reports and visuals folders without one public navigation surface per version. | Every benchmark version must maintain a benchmark atlas with chart registry, finding registry, version ledger, and non-claim boundary. |\n" + lesson + "\n",
    )

if "| v0.4.0d | Benchmark mini README AI/RCC warning repair. |" not in r:
    r = r.replace(
        "| v0.4.0c | Benchmark atlas and per-version chart/finding registry. |\n",
        "| v0.4.0c | Benchmark atlas and per-version chart/finding registry. |\n| v0.4.0d | Benchmark mini README AI/RCC warning repair. |\n",
    )

write(readme, r)

# Release note and status.
write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_0d_benchmark_mini_readme_ai_rcc_warning_repair.md", f"""# TAU-SCALING-SA v0.4.0d - Benchmark Mini README AI/RCC Warning Repair

Generated: {GENERATED_AT}

## Purpose

Repair the two README audit warnings produced after v0.4.0c.

## Warnings Repaired

```text
docs/benchmarks/README.md lacks explicit AI/RCC update guidance
reports/benchmarks/README.md lacks explicit AI/RCC update guidance
```

## Updates

- Added AI/RCC update guidance to `docs/benchmarks/README.md`.
- Added AI/RCC update guidance to `reports/benchmarks/README.md`.
- Updated root README checkpoint, metrics, lineage, and failure-learning ledger.
- Added L-018.

## Boundary

This repair affects benchmark documentation navigation only. It does not alter Tau Scaling gate math, classifier thresholds, benchmark results, silicon evidence, product evidence, manufacturing evidence, process-node equivalence, or universal-law claims.
""")

write(ROOT / "reports" / "benchmarks" / "v0_4_0d" / "latest_v0_4_0d_warning_repair_status.md", f"""# Tau Scaling v0.4.0d Benchmark Mini README Warning Repair Status

Generated: {GENERATED_AT}

Status: patched; validation must pass before commit/push.

Expected repaired warnings:

```text
mini_readme_lacks_ai_update_rule: docs/benchmarks/README.md
mini_readme_lacks_ai_update_rule: reports/benchmarks/README.md
```

Boundary:
- Documentation warning repair only.
""")

print("v0.4.0d benchmark mini README warning repair patch written")
