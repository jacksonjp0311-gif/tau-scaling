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
        dest = ROOT / "reports" / "nexus_feedback" / "v0_4_5a" / "backups" / f"{path.name}_before_v0_4_5a_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

write(ROOT / "reports" / "nexus_feedback" / "v0_4_5a" / "README.md", """# v0.4.5a Feedback Health Ordering Repair

## Purpose

This folder stores the feedback-health ordering repair status and backups.

## README Update Rule

Update this mini README whenever feedback ordering, feedback health logic, or validation sequencing changes.

Boundary: feedback health is repository self-observation only.
""")

# README update.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.5[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.5a - Feedback Health Ordering Repair**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.4[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.5 - Nexus Reflective Feedback Loop**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.5 \|", "| Current checkpoint | TAU-SCALING-SA v0.4.5a |", r)

section = """## Feedback Health Ordering Repair v0.4.5a

v0.4.5a repairs the execution order for reflective feedback.

Primary sequence:

```powershell
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python scripts/feedback/run_nexus_feedback.py
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
```

The purpose is to ensure Nexus feedback reads freshly generated validation reports before it emits its health score and improvement priorities.

Boundary: feedback health ordering is repository self-observation only. It does not mutate classifier behavior and does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Feedback Health Ordering Repair v0.4.5a" not in r:
    r = r.replace("## Nexus Reflective Feedback Loop v0.4.5", section + "## Nexus Reflective Feedback Loop v0.4.5", 1)

lesson = "| L-024 | v0.4.5 feedback emitted correct priorities but `health_passed` was false because it read validation surfaces before the final validators refreshed. | Reflective feedback can be logically correct while its health score is stale relative to the final seal. | Run prerequisite validators before Nexus feedback, then run Nexus feedback, then run final validators again before commit/push. |"
if lesson not in r:
    r = r.replace(
        "| L-023 | v0.4.4 created policy candidates but the repo still needed a way to turn outputs into improvement priorities. | Validation, benchmark, explanation, and policy reports were readable, but not yet synthesized into a feedback surface for the next agent. | Every mature runtime should emit a Nexus feedback report that ranks improvement targets without mutating classifier behavior. |\n",
        "| L-023 | v0.4.4 created policy candidates but the repo still needed a way to turn outputs into improvement priorities. | Validation, benchmark, explanation, and policy reports were readable, but not yet synthesized into a feedback surface for the next agent. | Every mature runtime should emit a Nexus feedback report that ranks improvement targets without mutating classifier behavior. |\n" + lesson + "\n",
    )

if "| v0.4.5a | Feedback health ordering repair so Nexus feedback reads fresh validation surfaces. |" not in r:
    r = r.replace(
        "| v0.4.5 | Nexus reflective feedback loop for ranked improvement signals. |\n",
        "| v0.4.5 | Nexus reflective feedback loop for ranked improvement signals. |\n| v0.4.5a | Feedback health ordering repair so Nexus feedback reads fresh validation surfaces. |\n",
    )

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator**

Recommended goals:

- Simulate policy-class changes without mutating the classifier.
- Compare current class vs proposed policy class.
- Emit drift impact charts.
- Decide whether policy enforcement is safe.
- Preserve non-claim locks: dry-run policy simulation is local classifier governance only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.5[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.5a - Feedback Health Ordering Repair**",
    a,
)
if "## Feedback Ordering Rule" not in a:
    a += """

## Feedback Ordering Rule

Reflective feedback must read fresh validation surfaces.

Required order for feedback-layer patches:

```powershell
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python scripts/feedback/run_nexus_feedback.py
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
```

Non-claim lock: feedback health is repository self-observation, not external validation.
"""
write(agents, a)

# route map.
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.5a"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["feedback_health_ordering_repair"] = {
    "read_first": [
        "reports/nexus_feedback/latest_nexus_feedback.json",
        "reports/release/latest_release_readiness.json",
        "reports/readme/latest_readme_mini_repo_audit.json",
        "reports/rcc_nexus/latest_rcc_nexus_check.json"
    ],
    "validate": [
        "python scripts/release/validate_release.py",
        "python scripts/rcc/audit_readme_surface.py",
        "python scripts/rcc/check_rcc_nexus.py",
        "python scripts/feedback/run_nexus_feedback.py",
        "python scripts/release/validate_release.py"
    ],
    "evidence": [
        "reports/nexus_feedback/latest_nexus_feedback.md",
        "reports/nexus_feedback/v0_4_5a/latest_v0_4_5a_status.md"
    ],
    "mutation_lock": "Does not change classifier behavior; repairs feedback ordering only."
}
write_json(route_path, route)

# task matrix.
matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.5[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.5a - Feedback Health Ordering Repair**",
    m,
)
if "| Feedback health ordering repair |" not in m:
    m = m.replace(
        "| Nexus feedback patch | outer | drift | agent | `scripts/feedback/`, `reports/nexus_feedback/`, latest reports | release validator + feedback report | `reports/nexus_feedback/latest_nexus_feedback.md` |\n",
        "| Nexus feedback patch | outer | drift | agent | `scripts/feedback/`, `reports/nexus_feedback/`, latest reports | release validator + feedback report | `reports/nexus_feedback/latest_nexus_feedback.md` |\n| Feedback health ordering repair | outer | drift | agent | validation reports, feedback report, AGENTS ordering rule | validators before feedback + feedback + validators after | `reports/nexus_feedback/latest_nexus_feedback.md` |\n",
    )
write(matrix, m)

# benchmark atlas.
atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.5a | Feedback health ordering repair |" not in t:
    t = t.replace(
        "| v0.4.5 | Nexus reflective feedback | `python scripts/feedback/run_nexus_feedback.py` | Synthesizes latest reports into ranked improvement signals | `reports/nexus_feedback/latest_nexus_feedback.md` | `visuals/nexus_feedback/v0_4_5/` |\n",
        "| v0.4.5 | Nexus reflective feedback | `python scripts/feedback/run_nexus_feedback.py` | Synthesizes latest reports into ranked improvement signals | `reports/nexus_feedback/latest_nexus_feedback.md` | `visuals/nexus_feedback/v0_4_5/` |\n| v0.4.5a | Feedback health ordering repair | validators -> feedback -> validators | Ensures Nexus feedback reads fresh validation surfaces before health scoring | `reports/nexus_feedback/latest_nexus_feedback.md` | `reports/nexus_feedback/v0_4_5a/` |\n",
    )
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_5a_feedback_health_ordering_repair.md", f"""# TAU-SCALING-SA v0.4.5a - Feedback Health Ordering Repair

Generated: {GENERATED_AT}

## Purpose

Repair execution order so Nexus feedback reads fresh validation reports before it emits health status.

## Change

This version changes process order, not classifier behavior.

## Required Sequence

```powershell
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python scripts/feedback/run_nexus_feedback.py
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
```

## Boundary

Feedback health ordering is repository self-observation only. It does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.
""")

write(ROOT / "reports" / "nexus_feedback" / "v0_4_5a" / "latest_v0_4_5a_status.md", f"""# Tau Scaling v0.4.5a Feedback Health Ordering Repair Status

Generated: {GENERATED_AT}

Status: patched; validators must run before and after feedback.

Primary repair:

```text
validators -> Nexus feedback -> validators
```
""")

print("v0.4.5a feedback health ordering repair patch written")
