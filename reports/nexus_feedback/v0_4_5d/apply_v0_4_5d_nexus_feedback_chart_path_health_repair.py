
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
        dest = ROOT / "reports" / "nexus_feedback" / "v0_4_5d" / "backups" / f"{path.name}_before_v0_4_5d_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

def replace_function_block(src: str, fn_name: str, replacement: str) -> str:
    marker = f"def {fn_name}("
    start = src.find(marker)
    if start < 0:
        raise RuntimeError(f"function not found: {fn_name}")
    matches = list(re.finditer(r"\ndef [A-Za-z_][A-Za-z0-9_]*\(", src[start + 1:]))
    end = len(src) if not matches else start + 1 + matches[0].start()
    return src[:start] + replacement.rstrip() + "\n" + src[end:]

target = ROOT / "scripts" / "feedback" / "run_nexus_feedback.py"
backup(target, "runner")
src = read(target)

# Ensure count_items exists and is stable.
helpers = """def count_items(value: Any) -> int:
    if value is None:
        return 0
    if isinstance(value, list):
        return len(value)
    if isinstance(value, dict):
        return len(value)
    if isinstance(value, (int, float)):
        return int(value)
    return 1

def bool_pass(payload: dict[str, Any]) -> bool:
    return bool(payload.get("passed") is True) and not payload.get("_missing_or_invalid")
"""
if "def count_items(" in src:
    src = replace_function_block(src, "count_items", helpers)
    src = re.sub(r'\ndef bool_pass\(payload: dict\[str, Any\]\) -> bool:\n    return bool\(payload.get\("passed"\) is True\) and not payload.get\("_missing_or_invalid"\)\n', "\n", src, count=1)
else:
    src = replace_function_block(src, "bool_pass", helpers)

health = """def health_score(inputs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    release = inputs["release_readiness"]
    readme = inputs["readme_audit"]
    rcc = inputs["rcc_nexus"]
    synthetic = inputs["synthetic_gate_suite"]
    sensitivity = inputs["sensitivity_sweep"]
    interactions = inputs["gate_interaction_matrix"]
    explanations = inputs["threshold_explanations"]
    policy = inputs["pair_policy_review"]

    sensitivity_points = int(sensitivity.get("total_points", 0) or len(sensitivity.get("results", [])))
    sensitivity_chart_count = int(sensitivity.get("chart_count", 0) or len(sensitivity.get("chart_paths", [])))
    release_findings_count = count_items(release.get("findings", 0))
    release_step_failures_count = count_items(release.get("step_failures", 0))
    readme_warnings_count = count_items(readme.get("warnings", 0))
    readme_errors_count = count_items(readme.get("errors", 0))
    rcc_warnings_count = count_items(rcc.get("warnings", 0))
    rcc_errors_count = count_items(rcc.get("errors", 0))

    validations = {
        "release_readiness": bool_pass(release) and release_step_failures_count == 0 and release_findings_count == 0,
        "readme_audit": bool_pass(readme) and readme_warnings_count == 0 and readme_errors_count == 0,
        "rcc_nexus": bool_pass(rcc) and rcc_warnings_count == 0 and rcc_errors_count == 0,
        "synthetic_suite": synthetic.get("all_scenarios_passed") is True and int(synthetic.get("failed_scenarios", 1)) == 0,
        "sensitivity_sweep": sensitivity_points >= 29 and sensitivity_chart_count >= 10,
        "gate_interactions": interactions.get("all_pairs_executed") is True and int(interactions.get("pair_count", 0)) == 55,
        "explanation_cards": int(explanations.get("card_count", 0)) >= 94,
        "policy_review": int(policy.get("pair_count", 0)) == 55 and policy.get("policy_enforced") is False,
    }

    details = {
        "release_findings_count": release_findings_count,
        "release_step_failures_count": release_step_failures_count,
        "readme_warnings_count": readme_warnings_count,
        "readme_errors_count": readme_errors_count,
        "rcc_warnings_count": rcc_warnings_count,
        "rcc_errors_count": rcc_errors_count,
        "sensitivity_points": sensitivity_points,
        "sensitivity_chart_count": sensitivity_chart_count,
        "sensitivity_chart_source": "chart_count if present else len(chart_paths)",
        "schema_alignment": "v0.4.5d chart-path normalization active",
    }

    score = sum(1 for v in validations.values() if v) / len(validations)
    return {"score": round(score, 4), "checks": validations, "details": details, "passed": score == 1.0}
"""
src = replace_function_block(src, "health_score", health)
src = src.replace('"schema": "tau-scaling-nexus-reflective-feedback-v0.4.5c",', '"schema": "tau-scaling-nexus-reflective-feedback-v0.4.5d",')
src = src.replace('"schema": "tau-scaling-nexus-reflective-feedback-v0.4.5b",', '"schema": "tau-scaling-nexus-reflective-feedback-v0.4.5d",')
src = src.replace('"schema": "tau-scaling-nexus-reflective-feedback-v0.4.5",', '"schema": "tau-scaling-nexus-reflective-feedback-v0.4.5d",')
src = src.replace("# Tau Scaling v0.4.5c Nexus Feedback Function-Block Repair", "# Tau Scaling v0.4.5d Nexus Feedback Chart-Path Health Repair")
src = src.replace("# Tau Scaling v0.4.5b Nexus Feedback Health Schema Alignment", "# Tau Scaling v0.4.5d Nexus Feedback Chart-Path Health Repair")
src = src.replace("# Tau Scaling v0.4.5 Nexus Reflective Feedback Loop", "# Tau Scaling v0.4.5d Nexus Feedback Chart-Path Health Repair")
write(target, src)

write(ROOT / "reports" / "nexus_feedback" / "v0_4_5d" / "README.md", """# v0.4.5d Nexus Feedback Chart-Path Health Repair

## Purpose

This folder stores the chart-path normalization repair for Nexus feedback health scoring.

## Cause

v0.4.5c repaired list-valued findings and step failures, but sensitivity health still failed because the persisted sensitivity JSON stores chart evidence under `chart_paths`, while the feedback scorer checked only top-level `chart_count`.

## Repair

- Derive sensitivity chart count from `chart_count` if present.
- Fall back to `len(chart_paths)` when `chart_count` is absent.
- Assert feedback health becomes `1.0`.

## README Update Rule

Update this mini README whenever sensitivity report schema or feedback health scoring changes.

Boundary: feedback health repair is repository self-observation only.
""")

# README update.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.5c[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.4.5d - Nexus Feedback Chart-Path Health Repair**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.5b[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.4.5c - Nexus Feedback Function-Block Repair**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.5c \|", "| Current checkpoint | TAU-SCALING-SA v0.4.5d |", r)

section = """## Nexus Feedback Chart-Path Health Repair v0.4.5d

v0.4.5d repairs the final feedback-health mismatch.

Cause found:

```text
v0.4.5c normalized findings and step_failures correctly.
The remaining failed check was sensitivity_sweep.
The sensitivity report stores chart evidence as chart_paths, not always chart_count.
```

Repair:

```text
sensitivity_chart_count = chart_count if present else len(chart_paths)
```

Expected result:

```text
health_score: 1.0
health_passed: true
schema: tau-scaling-nexus-reflective-feedback-v0.4.5d
```

Boundary: chart-path health repair is repository self-observation only. It does not mutate classifier behavior and does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Nexus Feedback Chart-Path Health Repair v0.4.5d" not in r:
    r = r.replace("## Nexus Feedback Function-Block Repair v0.4.5c", section + "## Nexus Feedback Function-Block Repair v0.4.5c", 1)

lesson = "| L-027 | v0.4.5c repaired list counters but `sensitivity_sweep` still failed health scoring. | The persisted sensitivity JSON used `chart_paths` while the feedback health scorer checked only `chart_count`. | Feedback health scoring must normalize both count fields and evidence-list fields such as chart_paths. |"
if lesson not in r:
    r = r.replace(
        "| L-026 | v0.4.5b changed the feedback schema label but `health_score` still used the old comparisons. | Regex patching did not replace the intended function body, so labels advanced faster than executable logic. | Function repairs must verify the target function body changed, not just schema strings or docs. |\n",
        "| L-026 | v0.4.5b changed the feedback schema label but `health_score` still used the old comparisons. | Regex patching did not replace the intended function body, so labels advanced faster than executable logic. | Function repairs must verify the target function body changed, not just schema strings or docs. |\n" + lesson + "\n",
    )

if "| v0.4.5d | Nexus feedback chart-path health repair for sensitivity sweep chart evidence. |" not in r:
    r = r.replace(
        "| v0.4.5c | Nexus feedback function-block repair to ensure health scorer logic actually updates. |\n",
        "| v0.4.5c | Nexus feedback function-block repair to ensure health scorer logic actually updates. |\n| v0.4.5d | Nexus feedback chart-path health repair for sensitivity sweep chart evidence. |\n",
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
a = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.5c[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.5d - Nexus Feedback Chart-Path Health Repair**", a)
if "Feedback health must normalize evidence-list fields" not in a:
    a += """

## Feedback Evidence-List Normalization Rule

Feedback health must normalize evidence-list fields as well as explicit count fields.

Examples:

```text
chart_count = chart_count if present else len(chart_paths)
point_count = total_points if present else len(results)
finding_count = findings if numeric else len(findings)
```

Non-claim lock: evidence-list normalization is repository self-observation, not external validation.
"""
write(agents, a)

# route map.
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.5d"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["feedback_chart_path_health_repair"] = {
    "read_first": ["scripts/feedback/run_nexus_feedback.py", "reports/sensitivity/latest_sensitivity_sweep.json", "reports/nexus_feedback/latest_nexus_feedback.json"],
    "validate": [
        "python -m py_compile scripts/feedback/run_nexus_feedback.py",
        "python -c \"from pathlib import Path; s=Path('scripts/feedback/run_nexus_feedback.py').read_text(); assert 'chart_paths' in s and 'sensitivity_chart_source' in s\"",
        "python scripts/feedback/run_nexus_feedback.py",
        "python -c \"import json; p=json.load(open('reports/nexus_feedback/latest_nexus_feedback.json')); assert p['health']['passed'] is True\"",
        "python scripts/release/validate_release.py"
    ],
    "evidence": ["reports/nexus_feedback/latest_nexus_feedback.md", "reports/nexus_feedback/v0_4_5d/latest_v0_4_5d_status.md"],
    "mutation_lock": "Does not change classifier behavior; repairs feedback sensitivity chart health only."
}
write_json(route_path, route)

# task matrix.
matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.5c[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.5d - Nexus Feedback Chart-Path Health Repair**", m)
if "| Feedback chart-path health repair |" not in m:
    m = m.replace(
        "| Feedback function-block repair | outer | drift | agent | feedback runner function body | compile + function-body assertion + feedback health score 1.0 | `reports/nexus_feedback/latest_nexus_feedback.md` |\n",
        "| Feedback function-block repair | outer | drift | agent | feedback runner function body | compile + function-body assertion + feedback health score 1.0 | `reports/nexus_feedback/latest_nexus_feedback.md` |\n| Feedback chart-path health repair | outer | drift | agent | feedback runner + sensitivity chart_paths | compile + chart-path assertion + feedback health score 1.0 | `reports/nexus_feedback/latest_nexus_feedback.md` |\n",
    )
write(matrix, m)

# atlas.
atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.5d | Nexus feedback chart-path health repair |" not in t:
    t = t.replace(
        "| v0.4.5c | Nexus feedback function-block repair | function-body assertion + feedback run | Ensures health scorer executable logic actually changed | `reports/nexus_feedback/latest_nexus_feedback.md` | `reports/nexus_feedback/v0_4_5c/` |\n",
        "| v0.4.5c | Nexus feedback function-block repair | function-body assertion + feedback run | Ensures health scorer executable logic actually changed | `reports/nexus_feedback/latest_nexus_feedback.md` | `reports/nexus_feedback/v0_4_5c/` |\n| v0.4.5d | Nexus feedback chart-path health repair | chart-path assertion + feedback health assertion | Normalizes sensitivity chart evidence from `chart_paths` | `reports/nexus_feedback/latest_nexus_feedback.md` | `reports/nexus_feedback/v0_4_5d/` |\n",
    )
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_5d_nexus_feedback_chart_path_health_repair.md", f"""# TAU-SCALING-SA v0.4.5d - Nexus Feedback Chart-Path Health Repair

Generated: {GENERATED_AT}

## Purpose

Repair the final Nexus feedback health mismatch by normalizing sensitivity chart evidence.

## Cause

v0.4.5c fixed release/readme/RCC counters, but sensitivity health still failed because persisted sensitivity JSON may expose chart evidence via `chart_paths` instead of `chart_count`.

## Repair

- `sensitivity_chart_count = chart_count if present else len(chart_paths)`
- Assert final feedback health score equals 1.0.

## Boundary

This version does not change classifier behavior. It repairs repository self-observation only.
""")

write(ROOT / "reports" / "nexus_feedback" / "v0_4_5d" / "latest_v0_4_5d_status.md", f"""# Tau Scaling v0.4.5d Nexus Feedback Chart-Path Health Repair Status

Generated: {GENERATED_AT}

Status: patched; sensitivity chart evidence now normalizes from chart_paths.

Expected:

```text
health_score: 1.0
health_passed: true
schema: tau-scaling-nexus-reflective-feedback-v0.4.5d
```
""")

print("v0.4.5d Nexus feedback chart-path health repair patch written")
