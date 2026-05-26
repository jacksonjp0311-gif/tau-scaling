
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
        dest = ROOT / "reports" / "nexus_feedback" / "v0_4_5b" / "backups" / f"{path.name}_before_v0_4_5b_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

target = ROOT / "scripts" / "feedback" / "run_nexus_feedback.py"
backup(target, "runner")
src = read(target)

new_helpers = """def count_items(value: Any) -> int:
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

src = re.sub(
    r'def bool_pass\(payload: dict\[str, Any\]\) -> bool:\n    return bool\(payload.get\("passed"\) is True\) and not payload.get\("_missing_or_invalid"\)\n',
    new_helpers,
    src,
)

new_health = """def health_score(inputs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    release = inputs["release_readiness"]
    readme = inputs["readme_audit"]
    rcc = inputs["rcc_nexus"]
    synthetic = inputs["synthetic_gate_suite"]
    sensitivity = inputs["sensitivity_sweep"]
    interactions = inputs["gate_interaction_matrix"]
    explanations = inputs["threshold_explanations"]
    policy = inputs["pair_policy_review"]

    sensitivity_points = int(sensitivity.get("total_points", 0) or len(sensitivity.get("results", [])))
    release_findings_count = count_items(release.get("findings", 0))
    release_step_failures_count = count_items(release.get("step_failures", 0))

    validations = {
        "release_readiness": bool_pass(release) and release_step_failures_count == 0 and release_findings_count == 0,
        "readme_audit": bool_pass(readme) and count_items(readme.get("warnings", 0)) == 0 and count_items(readme.get("errors", 0)) == 0,
        "rcc_nexus": bool_pass(rcc) and count_items(rcc.get("warnings", 0)) == 0 and count_items(rcc.get("errors", 0)) == 0,
        "synthetic_suite": synthetic.get("all_scenarios_passed") is True and int(synthetic.get("failed_scenarios", 1)) == 0,
        "sensitivity_sweep": sensitivity_points >= 29 and int(sensitivity.get("chart_count", 0)) >= 10,
        "gate_interactions": interactions.get("all_pairs_executed") is True and int(interactions.get("pair_count", 0)) == 55,
        "explanation_cards": int(explanations.get("card_count", 0)) >= 94,
        "policy_review": int(policy.get("pair_count", 0)) == 55 and policy.get("policy_enforced") is False,
    }

    details = {
        "release_findings_count": release_findings_count,
        "release_step_failures_count": release_step_failures_count,
        "sensitivity_points": sensitivity_points,
        "sensitivity_chart_count": int(sensitivity.get("chart_count", 0)),
        "note": "v0.4.5b normalizes list-valued findings/step_failures and derives sensitivity points from results when total_points is absent.",
    }

    score = sum(1 for v in validations.values() if v) / len(validations)
    return {"score": round(score, 4), "checks": validations, "details": details, "passed": score == 1.0}
"""

src = re.sub(r'def health_score\(inputs: dict\[str, dict\[str, Any\]\) -> dict\[str, Any\]:.*?\ndef feedback_signals', new_health + "\ndef feedback_signals", src, flags=re.S)
src = src.replace('"schema": "tau-scaling-nexus-reflective-feedback-v0.4.5",', '"schema": "tau-scaling-nexus-reflective-feedback-v0.4.5b",')
src = src.replace("# Tau Scaling v0.4.5 Nexus Reflective Feedback Loop", "# Tau Scaling v0.4.5b Nexus Feedback Health Schema Alignment")
write(target, src)

write(ROOT / "reports" / "nexus_feedback" / "v0_4_5b" / "README.md", "# v0.4.5b Nexus Feedback Health Schema Alignment\n\n## Purpose\n\nThis folder stores the schema-alignment repair for Nexus feedback health scoring.\n\n## Repair\n\n- Treat `findings: []` as zero findings.\n- Treat `step_failures: []` as zero step failures.\n- Derive sensitivity point count from `results` when `total_points` is absent.\n- Emit health details explaining normalized inputs.\n\n## README Update Rule\n\nUpdate this mini README whenever feedback health scoring, schema normalization, or input report interpretation changes.\n\nBoundary: feedback health schema alignment is repository self-observation only.\n")

# README.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.5a[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.4.5b - Nexus Feedback Health Schema Alignment**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.5[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.4.5a - Feedback Health Ordering Repair**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.5a \|", "| Current checkpoint | TAU-SCALING-SA v0.4.5b |", r)

section = """## Nexus Feedback Health Schema Alignment v0.4.5b

v0.4.5b repairs the feedback health scorer, not the runtime.

Cause found:

```text
release readiness writes findings and step_failures as lists.
sensitivity sweep stores point count in results, not always as top-level total_points.
```

Repair:

```text
[] counts as zero findings.
[] counts as zero step failures.
sensitivity_points = total_points if present, else len(results).
```

Primary command:

```powershell
python scripts/feedback/run_nexus_feedback.py
```

Expected result after fresh validators:

```text
health_score: 1.0
health_passed: true
```

Boundary: feedback health schema alignment is repository self-observation only. It does not mutate classifier behavior and does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Nexus Feedback Health Schema Alignment v0.4.5b" not in r:
    r = r.replace("## Feedback Health Ordering Repair v0.4.5a", section + "## Feedback Health Ordering Repair v0.4.5a", 1)

lesson = "| L-025 | v0.4.5a proved ordering was correct but `health_passed` stayed false. | The feedback scorer expected numeric `findings`, numeric `step_failures`, and top-level `total_points`, while actual reports used lists and `results`. | Feedback health checks must normalize report schemas before scoring; schema mismatch is not validation failure. |"
if lesson not in r:
    r = r.replace(
        "| L-024 | v0.4.5 feedback emitted correct priorities but `health_passed` was false because it read validation surfaces before the final validators refreshed. | Reflective feedback can be logically correct while its health score is stale relative to the final seal. | Run prerequisite validators before Nexus feedback, then run Nexus feedback, then run final validators again before commit/push. |\n",
        "| L-024 | v0.4.5 feedback emitted correct priorities but `health_passed` was false because it read validation surfaces before the final validators refreshed. | Reflective feedback can be logically correct while its health score is stale relative to the final seal. | Run prerequisite validators before Nexus feedback, then run Nexus feedback, then run final validators again before commit/push. |\n" + lesson + "\n",
    )

if "| v0.4.5b | Nexus feedback health schema alignment for list-valued findings and derived sensitivity points. |" not in r:
    r = r.replace(
        "| v0.4.5a | Feedback health ordering repair so Nexus feedback reads fresh validation surfaces. |\n",
        "| v0.4.5a | Feedback health ordering repair so Nexus feedback reads fresh validation surfaces. |\n| v0.4.5b | Nexus feedback health schema alignment for list-valued findings and derived sensitivity points. |\n",
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
a = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.5a[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.5b - Nexus Feedback Health Schema Alignment**", a)
if "Feedback health checks must normalize report schemas" not in a:
    a += "\n\n## Feedback Schema Normalization Rule\n\nFeedback health checks must normalize report schemas before scoring.\n\nExamples:\n\n```text\nfindings: [] == 0 findings\nstep_failures: [] == 0 step failures\nsensitivity_points = total_points if present else len(results)\n```\n\nNon-claim lock: schema-normalized health is repository self-observation, not external validation.\n"
write(agents, a)

# route map.
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.5b"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["feedback_health_schema_alignment"] = {
    "read_first": ["scripts/feedback/run_nexus_feedback.py", "reports/release/latest_release_readiness.json", "reports/sensitivity/latest_sensitivity_sweep.json", "reports/nexus_feedback/latest_nexus_feedback.json"],
    "validate": ["python scripts/release/validate_release.py", "python scripts/rcc/audit_readme_surface.py", "python scripts/rcc/check_rcc_nexus.py", "python scripts/feedback/run_nexus_feedback.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/nexus_feedback/latest_nexus_feedback.md", "reports/nexus_feedback/v0_4_5b/latest_v0_4_5b_status.md"],
    "mutation_lock": "Does not change classifier behavior; repairs feedback health scoring only."
}
write_json(route_path, route)

# task matrix.
matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.5a[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.5b - Nexus Feedback Health Schema Alignment**", m)
if "| Feedback health schema alignment |" not in m:
    m = m.replace(
        "| Feedback health ordering repair | outer | drift | agent | validation reports, feedback report, AGENTS ordering rule | validators before feedback + feedback + validators after | `reports/nexus_feedback/latest_nexus_feedback.md` |\n",
        "| Feedback health ordering repair | outer | drift | agent | validation reports, feedback report, AGENTS ordering rule | validators before feedback + feedback + validators after | `reports/nexus_feedback/latest_nexus_feedback.md` |\n| Feedback health schema alignment | outer | drift | agent | feedback runner, release report, sensitivity report | feedback health score 1.0 + validators | `reports/nexus_feedback/latest_nexus_feedback.md` |\n",
    )
write(matrix, m)

# atlas.
atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.5b | Nexus feedback health schema alignment |" not in t:
    t = t.replace(
        "| v0.4.5a | Feedback health ordering repair | validators -> feedback -> validators | Ensures Nexus feedback reads fresh validation surfaces before health scoring | `reports/nexus_feedback/latest_nexus_feedback.md` | `reports/nexus_feedback/v0_4_5a/` |\n",
        "| v0.4.5a | Feedback health ordering repair | validators -> feedback -> validators | Ensures Nexus feedback reads fresh validation surfaces before health scoring | `reports/nexus_feedback/latest_nexus_feedback.md` | `reports/nexus_feedback/v0_4_5a/` |\n| v0.4.5b | Nexus feedback health schema alignment | `python scripts/feedback/run_nexus_feedback.py` | Normalizes list-valued findings/step_failures and derives sensitivity points from results | `reports/nexus_feedback/latest_nexus_feedback.md` | `reports/nexus_feedback/v0_4_5b/` |\n",
    )
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_5b_nexus_feedback_health_schema_alignment.md", f"# TAU-SCALING-SA v0.4.5b - Nexus Feedback Health Schema Alignment\n\nGenerated: {GENERATED_AT}\n\n## Purpose\n\nRepair Nexus feedback health scoring to match actual report schemas.\n\n## Cause\n\n- `reports/release/latest_release_readiness.json` stores `findings` and `step_failures` as lists.\n- `reports/sensitivity/latest_sensitivity_sweep.json` stores sweep point detail under `results`.\n\n## Repair\n\n- Normalize list-valued findings and step failures before scoring.\n- Derive sensitivity point count from `results` when `total_points` is absent.\n- Emit health details in the feedback JSON.\n\n## Boundary\n\nThis version does not change classifier behavior. It repairs repository self-observation only.\n")

write(ROOT / "reports" / "nexus_feedback" / "v0_4_5b" / "latest_v0_4_5b_status.md", f"# Tau Scaling v0.4.5b Nexus Feedback Health Schema Alignment Status\n\nGenerated: {GENERATED_AT}\n\nStatus: patched; health scorer now normalizes report schemas.\n\nExpected after run:\n\n```text\nhealth_score: 1.0\nhealth_passed: true\n```\n")

print("v0.4.5b Nexus feedback health schema alignment patch written")
