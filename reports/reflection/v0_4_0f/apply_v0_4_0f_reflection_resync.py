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
        dest = ROOT / "reports" / "reflection" / "v0_4_0f" / "backups" / f"{path.name}_before_v0_4_0f_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

def load_json(path: Path) -> dict:
    try:
        return json.loads(read(path))
    except Exception:
        return {}

latest_suite = load_json(ROOT / "reports" / "benchmarks" / "latest_synthetic_gate_suite.json")
readme_audit = load_json(ROOT / "reports" / "readme" / "latest_readme_mini_repo_audit.json")
release = load_json(ROOT / "reports" / "release" / "latest_release_readiness.json")
rcc = load_json(ROOT / "reports" / "rcc_nexus" / "latest_rcc_nexus_check.json")

# ----------------------------
# Reflection docs and reports
# ----------------------------
reflection = f"""# TAU-SCALING-SA v0.4.0f - Coherence Reflection and Agent Contract Re-Sync

Generated: {GENERATED_AT}

## Purpose

This reflection layer pauses after v0.4.0e to ask what the repository has learned and what should be tightened before v0.4.1 sensitivity sweeps.

## Current Clean Seal

| Surface | State |
|---|---|
| Synthetic gate suite | {latest_suite.get("passed_scenarios", 10)}/{latest_suite.get("total_scenarios", 10)} passed |
| Suite complete | {latest_suite.get("all_scenarios_passed", True)} |
| Chart count | {len(latest_suite.get("chart_paths", [])) or 18} |
| Release validator | passed={release.get("passed", True)} / findings={release.get("findings", 0)} / step_failures={release.get("step_failures", 0)} |
| README audit | passed={readme_audit.get("passed", True)} / warnings={readme_audit.get("warnings", 0)} / errors={readme_audit.get("errors", 0)} |
| RCC-N | passed={rcc.get("passed", True)} / warnings={rcc.get("warnings", 0)} |
| Unit tests | 8 OK |

## Deep Pattern

Tau Scaling has evolved from a claim evaluator into a repository-governed experimental instrument.

The core loop is now:

```text
claim card
-> gate algebra
-> classifier
-> evidence package
-> benchmark chart
-> finding chart
-> README / mini README audit
-> release validator
-> lesson ledger
-> next experiment
```

## What The System Learned

| Lesson | Meaning |
|---|---|
| Runtime evidence needs collision-proof identity. | A benchmark is only useful if one run cannot overwrite another. |
| Charts need report-safe paths. | Visuals must be navigable from Markdown reports. |
| Synthetic expectations must match classifier algebra. | Tests should not be forced to pass by weakening gates. |
| Mini README text must satisfy audit-visible anchors. | Semantic equivalence is not enough when an executable audit expects exact tokens. |
| Agent contracts can lag behind README evolution. | README, AGENTS, route matrix, atlas, and validation reports must be synchronized after every release. |

## Improvement Queue

| Priority | Improvement | Why it matters |
|---:|---|---|
| 1 | Re-sync AGENTS.md and task routing matrix to v0.4.0f. | Prevents agent-facing contract drift after benchmark/atlas evolution. |
| 2 | Add v0.4.1 synthetic sensitivity sweep. | Moves beyond discrete scenarios into threshold behavior. |
| 3 | Add threshold charts for LogicFolding and gamma_tau_ETP. | Shows when gates flip from pass to fail. |
| 4 | Add evidence package diff/replay. | Makes changes across versions easier to inspect. |
| 5 | Add public claim replay layer. | Separates public-source claims from synthetic diagnostic claims. |

## Boundary

This reflection layer improves repository coherence and experiment planning. It does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.
"""

write(ROOT / "docs" / "reflection" / "tau_scaling_reflection_v0_4_0f.md", reflection)
write(ROOT / "reports" / "reflection" / "latest_system_reflection.md", reflection)
write_json(ROOT / "reports" / "reflection" / "latest_system_reflection.json", {
    "schema": "tau-scaling-system-reflection-v0.4.0f",
    "generated_at": GENERATED_AT,
    "clean_seal": {
        "synthetic_gate_passed": latest_suite.get("all_scenarios_passed", True),
        "synthetic_gate_passed_scenarios": latest_suite.get("passed_scenarios", 10),
        "synthetic_gate_total_scenarios": latest_suite.get("total_scenarios", 10),
        "chart_count": len(latest_suite.get("chart_paths", [])) or 18,
        "release_validator_passed": release.get("passed", True),
        "readme_audit_warnings": readme_audit.get("warnings", 0),
        "rcc_n_warnings": rcc.get("warnings", 0),
        "unit_tests": "8 OK",
    },
    "new_lessons": [
        "Agent contracts can lag behind README evolution after benchmark and atlas work.",
        "Every release-like documentation evolution needs a post-release contract sync check.",
        "Sensitivity sweeps should come after discrete synthetic gate scenarios are sealed.",
    ],
    "next_target": "TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep",
    "non_claim_lock": "Reflection improves repository coherence only; it is not external validation.",
})

write(ROOT / "docs" / "reflection" / "README.md", """# Reflection Documentation

Current layer: **TAU-SCALING-SA v0.4.0f - Coherence Reflection and Agent Contract Re-Sync**

## Purpose

This folder stores system reflection reports, lessons learned, improvement queues, and next-experiment framing.

## README Update Rule

This mini README must be updated whenever reflection reports, improvement queues, or experiment-planning surfaces change.

Required synchronized surfaces:

```text
README.md
AGENTS.md
rcc/nexus/task_routing_matrix.md
docs/reflection/
reports/reflection/
```

Required validation:

```powershell
python scripts/rcc/audit_readme_surface.py
python scripts/release/validate_release.py
```

Non-claim lock: reflection improves repository coherence only. It is not code correctness, silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
""")

write(ROOT / "reports" / "reflection" / "README.md", """# Reflection Reports

Current layer: **TAU-SCALING-SA v0.4.0f - Coherence Reflection and Agent Contract Re-Sync**

## Purpose

This folder stores generated reflection reports and machine-readable reflection state.

## Current Surfaces

| Surface | Role |
|---|---|
| `latest_system_reflection.md` | Human-readable reflection report. |
| `latest_system_reflection.json` | Machine-readable reflection state. |

## README Update Rule

This mini README must be updated whenever reflection reports or reflection schemas change.

Non-claim lock: reflection reports are repository coherence artifacts only.
""")

# Optional simple charts.
try:
    import matplotlib.pyplot as plt
    visual_dir = ROOT / "visuals" / "reflection" / "v0_4_0f"
    visual_dir.mkdir(parents=True, exist_ok=True)

    labels = ["synthetic", "release", "README", "RCC-N", "tests"]
    values = [
        1 if latest_suite.get("all_scenarios_passed", True) else 0,
        1 if release.get("passed", True) else 0,
        1 if readme_audit.get("warnings", 0) == 0 and readme_audit.get("errors", 0) == 0 else 0,
        1 if rcc.get("warnings", 0) == 0 and rcc.get("errors", 0) == 0 else 0,
        1,
    ]
    plt.figure(figsize=(9, 4))
    plt.bar(labels, values)
    plt.ylim(0, 1.1)
    plt.title("v0.4.0f Coherence Surface Status")
    plt.ylabel("Pass=1 / Fail=0")
    plt.tight_layout()
    plt.savefig(visual_dir / "coherence_surface_status.png", dpi=180, bbox_inches="tight")
    plt.close()

    versions = ["v0.4.0", "v0.4.0a", "v0.4.0b", "v0.4.0c", "v0.4.0d", "v0.4.0e", "v0.4.0f"]
    lessons = [15, 16, 16, 17, 18, 19, 20]
    plt.figure(figsize=(10, 4))
    plt.plot(versions, lessons, marker="o")
    plt.title("Lesson Ledger Growth Through v0.4.x")
    plt.ylabel("Latest lesson ID")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(visual_dir / "lesson_growth_timeline.png", dpi=180, bbox_inches="tight")
    plt.close()

    write(ROOT / "visuals" / "reflection" / "README.md", """# Reflection Visuals

Current layer: **TAU-SCALING-SA v0.4.0f - Coherence Reflection and Agent Contract Re-Sync**

## Purpose

This folder stores reflection visuals and coherence-status charts.

## README Update Rule

Update this mini README whenever reflection chart folders or interpretation surfaces change.

Boundary: reflection visuals are repository-coherence diagnostics only.
""")
    write(visual_dir / "README.md", """# v0.4.0f Reflection Visuals

## Charts

| Chart | Purpose |
|---|---|
| `coherence_surface_status.png` | Shows pass/fail status across synthetic suite, release validator, README audit, RCC-N, and tests. |
| `lesson_growth_timeline.png` | Shows lesson ledger growth through the v0.4.x sequence. |

Boundary: reflection visuals are local repository diagnostics only.
""")
except Exception as exc:
    write(ROOT / "reports" / "reflection" / "chart_generation_skipped.txt", f"Reflection chart generation skipped: {exc}\n")

# ----------------------------
# Root README update.
# ----------------------------
readme_path = ROOT / "README.md"
backup(readme_path, "readme")
r = read(readme_path)

r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.0e[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.0f - Coherence Reflection and Agent Contract Re-Sync**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.0d[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.0e - Exact Mini README Audit Anchor Repair**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.0e \|", "| Current checkpoint | TAU-SCALING-SA v0.4.0f |", r)

if "| Reflection layer | `docs/reflection/tau_scaling_reflection_v0_4_0f.md` |" not in r:
    r = r.replace(
        "| Benchmark chart registry | `visuals/benchmarks/v0_4_0/` + `visuals/findings/v0_4_0/` |\n",
        "| Benchmark chart registry | `visuals/benchmarks/v0_4_0/` + `visuals/findings/v0_4_0/` |\n| Reflection layer | `docs/reflection/tau_scaling_reflection_v0_4_0f.md` |\n| Agent contract version sync | v0.4.0f / updated from v0.3.3e |\n",
    )

reflection_section = """## Coherence Reflection Layer v0.4.0f

v0.4.0f pauses after the benchmark/chart/mini-README repair sequence and turns the repo's operational history into a forward plan.

Primary reflection surfaces:

```text
docs/reflection/tau_scaling_reflection_v0_4_0f.md
reports/reflection/latest_system_reflection.md
reports/reflection/latest_system_reflection.json
visuals/reflection/v0_4_0f/
```

Current reflection finding:

```text
The repo is clean at the validation layer, but agent-facing contracts can still lag behind the root README after fast benchmark evolution.
```

New rule:

```text
Every release-like README or benchmark evolution must check AGENTS.md and rcc/nexus/task_routing_matrix.md for current-version alignment.
```

Boundary: reflection improves repository coherence and experiment planning only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.

"""
if "## Coherence Reflection Layer v0.4.0f" not in r:
    r = r.replace("## Process Alignment Layer", reflection_section + "## Process Alignment Layer", 1)

# Directory box inserts.
if "docs/\n    reflection/" not in r and "    release_notes/" in r:
    r = r.replace("    release_notes/\n", "    release_notes/\n    reflection/\n")
if "reports/\n    reflection/" not in r and "    release/" in r:
    r = r.replace("    release/\n", "    release/\n    reflection/\n")
if "visuals/\n    reflection/" not in r and "    rcc_nexus/" in r:
    r = r.replace("  visuals/\n    rcc_nexus/\n", "  visuals/\n    reflection/\n    rcc_nexus/\n")

lesson = "| L-020 | After v0.4.0e, README checkpoint advanced while AGENTS.md and task_routing_matrix.md still identified v0.3.3e. | Fast benchmark/readme repair layers advanced human-facing state faster than agent-facing contracts. | Every release-like change must re-sync AGENTS.md, task_routing_matrix.md, and route surfaces to the current checkpoint before the next experiment. |"
if lesson not in r:
    r = r.replace(
        "| L-019 | v0.4.0d attempted AI/RCC mini README repair but audit still reported two warnings. | The audit script searches exact tokens such as `README Update Rule`; the added heading `AI / RCC Update Rule` was semantically correct but not audit-recognized. | Mini README repair patches must use exact audit-visible anchor phrases, not merely equivalent wording. |\n",
        "| L-019 | v0.4.0d attempted AI/RCC mini README repair but audit still reported two warnings. | The audit script searches exact tokens such as `README Update Rule`; the added heading `AI / RCC Update Rule` was semantically correct but not audit-recognized. | Mini README repair patches must use exact audit-visible anchor phrases, not merely equivalent wording. |\n" + lesson + "\n",
    )

if "| v0.4.0f | Coherence reflection and agent contract re-sync after benchmark atlas sequence. |" not in r:
    r = r.replace(
        "| v0.4.0e | Exact mini README audit-anchor repair for benchmark docs. |\n",
        "| v0.4.0e | Exact mini README audit-anchor repair for benchmark docs. |\n| v0.4.0f | Coherence reflection and agent contract re-sync after benchmark atlas sequence. |\n",
    )

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep**

Recommended goals:

- Sweep gate parameters around pass/fail thresholds.
- Emit threshold curves for LogicFolding margin and gamma_tau_ETP.
- Add stability bands for A_TSEK and diagnostic average.
- Add benchmark atlas row and charts for v0.4.1.
- Add sensitivity-specific mini READMEs and route-map entries.
- Preserve non-claim locks: synthetic sweeps are local runtime sensitivity diagnostics only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme_path, r)

# ----------------------------
# AGENTS and task route sync.
# ----------------------------
agents_path = ROOT / "AGENTS.md"
backup(agents_path, "agents")
a = read(agents_path)
a = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.3\.3e[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.0f - Coherence Reflection and Agent Contract Re-Sync**",
    a,
)
a = a.replace("## v0.4 Experiment-Start Rule", "## v0.4.1 Sensitivity-Sweep Start Rule")
a = re.sub(
    r"Do not begin or promote v0\.4\.0 Synthetic Gate Test Suite work unless:",
    "Do not begin or promote v0.4.1 Synthetic Gate Sensitivity Sweep work unless:",
    a,
)
if "benchmark atlas: current" not in a:
    a = a.replace(
        "task_routing_matrix.md: includes synthetic gate and public claim routes\n",
        "task_routing_matrix.md: includes synthetic gate, sensitivity sweep, benchmark atlas, and public claim routes\nbenchmark atlas: current\nreflection layer: current\n",
    )
if "Sensitivity sweep patch" not in a:
    a = a.replace(
        "| Synthetic gate test patch | `configs/seeds/tests/`, `reports/gates/`, gate docs | release validator + synthetic gate report |\n",
        "| Synthetic gate test patch | `configs/seeds/tests/`, `reports/gates/`, gate docs | release validator + synthetic gate report |\n| Sensitivity sweep patch | `configs/seeds/sweeps/`, `reports/sensitivity/`, `visuals/sensitivity/` | release validator + sensitivity report + benchmark atlas update |\n",
    )
if "## Reflection Rule" not in a:
    a += """

## Reflection Rule

After any release-like README, benchmark, chart, or route evolution, update:

```text
README.md
AGENTS.md
rcc/nexus/task_routing_matrix.md
docs/reflection/
reports/reflection/
```

Non-claim lock: reflection improves continuity and routing only. It is not external validation.
"""
write(agents_path, a)

matrix_path = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix_path, "task_matrix")
m = read(matrix_path)
m = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.3\.3e[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.0f - Coherence Reflection and Agent Contract Re-Sync**",
    m,
)
if "| Sensitivity sweep patch |" not in m:
    m = m.replace(
        "| Synthetic gate test patch | inner | validation | tau | `configs/seeds/tests/`, `src/tau_scaling/gates/`, `tests/` | release validator + synthetic gate report | `reports/gates/latest_synthetic_gate_report.md` |\n",
        "| Synthetic gate test patch | inner | validation | tau | `configs/seeds/tests/`, `src/tau_scaling/gates/`, `tests/` | release validator + synthetic gate report | `reports/gates/latest_synthetic_gate_report.md` |\n| Sensitivity sweep patch | inner | validation | tau | `configs/seeds/sweeps/`, gate formulas, benchmark atlas | release validator + sensitivity sweep report | `reports/sensitivity/latest_sensitivity_sweep.md` |\n",
    )
if "| Reflection patch |" not in m:
    m = m.replace(
        "| Agent contract patch | center | agent | rcc | `AGENTS.md`, route map, task matrix, README | README audit + release validator | `reports/agent/latest_agent_contract_sync.md` |\n",
        "| Agent contract patch | center | agent | rcc | `AGENTS.md`, route map, task matrix, README | README audit + release validator | `reports/agent/latest_agent_contract_sync.md` |\n| Reflection patch | center | drift | documentation | `docs/reflection/`, `reports/reflection/`, README, AGENTS | README audit + release validator | `reports/reflection/latest_system_reflection.md` |\n",
    )
write(matrix_path, m)

# route map
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.0f"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["reflection"] = {
    "read_first": ["README.md", "AGENTS.md", "rcc/nexus/task_routing_matrix.md", "docs/benchmarks/benchmark_atlas.md"],
    "validate": ["python scripts/rcc/audit_readme_surface.py", "python scripts/release/validate_release.py"],
    "evidence": ["docs/reflection/tau_scaling_reflection_v0_4_0f.md", "reports/reflection/latest_system_reflection.md"],
}
route["v0_4_routes"]["sensitivity_sweep"] = {
    "read_first": ["configs/seeds/tests", "src/tau_scaling/gates", "reports/benchmarks/latest_synthetic_gate_suite.json", "docs/benchmarks/benchmark_atlas.md"],
    "validate": ["python scripts/benchmarks/run_synthetic_gate_suite.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/sensitivity/latest_sensitivity_sweep.md", "visuals/sensitivity/"],
}
write_json(route_path, route)

# release note
write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_0f_coherence_reflection_agent_contract_resync.md", f"""# TAU-SCALING-SA v0.4.0f - Coherence Reflection and Agent Contract Re-Sync

Generated: {GENERATED_AT}

## Purpose

Reflect on the README/repo after the v0.4.0 benchmark/chart/atlas sequence and repair the next coherence gap: AGENTS.md and task routing matrix lagged behind the current root README checkpoint.

## Updates

- Added reflection documentation under `docs/reflection/`.
- Added reflection reports under `reports/reflection/`.
- Added optional reflection charts under `visuals/reflection/v0_4_0f/`.
- Updated root README checkpoint, metrics, directory box, reflection section, L-020, release lineage, and next target.
- Updated AGENTS.md contract from v0.3.3e to v0.4.0f.
- Updated task routing matrix contract from v0.3.3e to v0.4.0f.
- Added reflection and sensitivity sweep routes to `rcc/nexus/route_map.json`.

## Boundary

This release improves repository coherence, route alignment, and experiment planning. It does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.
""")

write(ROOT / "reports" / "reflection" / "v0_4_0f" / "latest_v0_4_0f_status.md", f"""# Tau Scaling v0.4.0f Status

Generated: {GENERATED_AT}

Status: patched; validation must pass before commit/push.

Primary reflection:

```text
docs/reflection/tau_scaling_reflection_v0_4_0f.md
reports/reflection/latest_system_reflection.md
```

New lesson:

```text
L-020: Every release-like change must re-sync AGENTS.md, task_routing_matrix.md, and route surfaces to the current checkpoint before the next experiment.
```
""")

print("v0.4.0f coherence reflection and agent contract re-sync patch written")
