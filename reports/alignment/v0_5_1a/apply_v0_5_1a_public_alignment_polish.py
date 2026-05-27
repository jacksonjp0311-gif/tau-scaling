
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

def backup(path: Path, label: str) -> None:
    if path.exists():
        dest = ROOT / "reports" / "alignment" / "v0_5_1a" / "backups" / f"{path.name}_before_v0_5_1a_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

# README public metric alignment.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = r.replace("| Task routing matrix | geometry-aware / v0.4.8-ready |", "| Task routing matrix | geometry-aware / v0.5.1-ready |")
r = r.replace("| Agent contract version sync | current / v0.4.8 |", "| Agent contract version sync | current / v0.5.1 |")

alignment_note = """## v0.5.1a Public Alignment Polish

v0.5.1a is a documentation-alignment polish layer. It does not add runtime behavior.

Repairs:

```text
README public metrics now identify AGENTS.md as current / v0.5.1.
README public metrics now identify task routing as v0.5.1-ready.
AGENTS.md Required Validation now includes the current v0.4.6-v0.5.1 governance chain.
```

Boundary: alignment polish is repository hygiene only. It is not code correctness, silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.

"""
if "## v0.5.1a Public Alignment Polish" not in r:
    r = r.replace("## Nexus Target Refresh and Completed-Signal Retirement v0.5.1", alignment_note + "## Nexus Target Refresh and Completed-Signal Retirement v0.5.1", 1)

if "| v0.5.1a | Public alignment polish for README metrics and AGENTS validation chain. |" not in r:
    r = r.replace("| v0.5.1 | Nexus target refresh and completed-signal retirement after v0.5.0. |\n",
                  "| v0.5.1 | Nexus target refresh and completed-signal retirement after v0.5.0. |\n| v0.5.1a | Public alignment polish for README metrics and AGENTS validation chain. |\n")

write(readme, r)

# AGENTS required validation alignment.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)

required_block = """## Required Validation

For every non-trivial patch, run:

```powershell
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python scripts/benchmarks/run_synthetic_gate_suite.py
python scripts/benchmarks/run_sensitivity_sweep.py
python scripts/benchmarks/run_gate_interaction_matrix.py
python scripts/benchmarks/generate_threshold_explanation_cards.py
python scripts/benchmarks/run_pair_policy_review.py
python scripts/benchmarks/run_pair_policy_dry_run.py
python scripts/benchmarks/generate_policy_impact_cards.py
python scripts/benchmarks/generate_policy_decision_record.py
python scripts/benchmarks/run_regression_over_penalty_review.py
python scripts/benchmarks/run_enforcement_readiness_gate.py
python scripts/feedback/run_nexus_feedback.py
python scripts/feedback/run_nexus_target_refresh.py
python -m unittest discover -s tests
```
"""
a = re.sub(r"## Required Validation\s+For every non-trivial patch, run:\s+```powershell.*?```\s+", required_block + "\n", a, flags=re.S)
write(agents, a)

# Route map timestamp only; route content is already aligned.
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
    route["updated_at"] = GENERATED_AT
    route["version"] = "v0.5.1"
    write(route_path, json.dumps(route, indent=2, sort_keys=True) + "\n")
except Exception:
    pass

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_5_1a_public_alignment_polish.md", f"""# TAU-SCALING-SA v0.5.1a - Public Alignment Polish

Generated: {GENERATED_AT}

## Purpose

Repair small documentation drift after v0.5.1.

## Repairs

- README public metrics now identify AGENTS.md as current / v0.5.1.
- README public metrics now identify task routing as v0.5.1-ready.
- AGENTS.md Required Validation now includes the v0.4.6-v0.5.1 governance chain.

## Boundary

Public alignment polish is repository hygiene only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.5.1a public alignment polish patch written")
