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
        dest = ROOT / "reports" / "benchmarks" / "v0_4_0e" / "backups" / f"{path.name}_before_v0_4_0e_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

EXACT_RULE = """
## README Update Rule

This mini README must be updated whenever benchmark commands, benchmark reports, chart folders, chart registries, benchmark interpretation, or non-claim boundary language changes.

Required synchronized surfaces:

```text
README.md
docs/benchmarks/benchmark_atlas.md
reports/benchmarks/README.md
reports/benchmarks/benchmark_chart_registry_v0_4_0c.json
visuals/benchmarks/README.md
visuals/findings/README.md
rcc/nexus/route_map.json
```

Required validation:

```powershell
python scripts/rcc/audit_readme_surface.py
python scripts/release/validate_release.py
```

Non-claim lock: README update guidance improves repository context alignment only. It is not code correctness, silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
"""

targets = [
    ROOT / "docs" / "benchmarks" / "README.md",
    ROOT / "reports" / "benchmarks" / "README.md",
]

for target in targets:
    backup(target, target.parent.name)
    text = read(target).rstrip() + "\n"
    if "## README Update Rule" not in text:
        text += EXACT_RULE
    write(target, text)

readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)

r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.0d[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.0e - Exact Mini README Audit Anchor Repair**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.0c[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.0d - Benchmark Mini README AI/RCC Warning Repair**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.0d \|", "| Current checkpoint | TAU-SCALING-SA v0.4.0e |", r)

if "| Mini README audit warnings | exact anchor repair / expected 0 warnings |" not in r:
    r = r.replace(
        "| Benchmark mini README AI/RCC guidance | repaired / expected 0 warnings |\n",
        "| Benchmark mini README AI/RCC guidance | repaired / expected 0 warnings |\n| Mini README audit warnings | exact anchor repair / expected 0 warnings |\n",
    )

lesson = "| L-019 | v0.4.0d attempted AI/RCC mini README repair but audit still reported two warnings. | The audit script searches exact tokens such as `README Update Rule`; the added heading `AI / RCC Update Rule` was semantically correct but not audit-recognized. | Mini README repair patches must use exact audit-visible anchor phrases, not merely equivalent wording. |"
if lesson not in r:
    r = r.replace(
        "| L-018 | v0.4.0c benchmark atlas passed but README audit found two warnings. | `docs/benchmarks/README.md` and `reports/benchmarks/README.md` lacked explicit AI/RCC update guidance. | Every benchmark mini README must include an AI/RCC update rule when benchmark charts, reports, or interpretation surfaces change. |\n",
        "| L-018 | v0.4.0c benchmark atlas passed but README audit found two warnings. | `docs/benchmarks/README.md` and `reports/benchmarks/README.md` lacked explicit AI/RCC update guidance. | Every benchmark mini README must include an AI/RCC update rule when benchmark charts, reports, or interpretation surfaces change. |\n" + lesson + "\n",
    )

if "| v0.4.0e | Exact mini README audit-anchor repair for benchmark docs. |" not in r:
    r = r.replace(
        "| v0.4.0d | Benchmark mini README AI/RCC warning repair. |\n",
        "| v0.4.0d | Benchmark mini README AI/RCC warning repair. |\n| v0.4.0e | Exact mini README audit-anchor repair for benchmark docs. |\n",
    )

write(readme, r)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_0e_exact_mini_readme_audit_anchor_repair.md", f"""# TAU-SCALING-SA v0.4.0e - Exact Mini README Audit Anchor Repair

Generated: {GENERATED_AT}

## Purpose

Repair the v0.4.0d benchmark mini README warnings using the exact audit-visible anchor phrase required by `scripts/rcc/audit_readme_surface.py`.

## Diagnosis

v0.4.0d added an `AI / RCC Update Rule` section. That was semantically correct, but the audit scanner recognizes exact tokens including:

```text
README / Mini Repo Audit Rule
Mini README Update Rule
README Update Rule
AI Failure Learning Note
RCC Nexus Echo Location
```

Therefore the two benchmark mini READMEs still warned.

## Repair

- Add exact `README Update Rule` sections to:
  - `docs/benchmarks/README.md`
  - `reports/benchmarks/README.md`
- Update root README checkpoint, metrics, lineage, and learning ledger.
- Add L-019.

## Boundary

This repair affects audit-visible documentation anchors only. It does not alter Tau Scaling gate math, classifier thresholds, benchmark results, charts, silicon evidence, product evidence, manufacturing evidence, process-node equivalence, or universal-law claims.
""")

write(ROOT / "reports" / "benchmarks" / "v0_4_0e" / "latest_v0_4_0e_exact_anchor_repair_status.md", f"""# Tau Scaling v0.4.0e Exact Mini README Audit Anchor Repair Status

Generated: {GENERATED_AT}

Status: patched; validation must pass before commit/push.

Expected repaired warnings:

```text
mini_readme_lacks_ai_update_rule: docs/benchmarks/README.md
mini_readme_lacks_ai_update_rule: reports/benchmarks/README.md
```

Audit-visible token added:

```text
README Update Rule
```

Boundary:
- Documentation audit-anchor repair only.
""")

print("v0.4.0e exact mini README audit anchor repair patch written")
