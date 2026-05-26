from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json, re

root = Path.cwd()
generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def backup(path: Path, label: str) -> None:
    if not path.exists():
        return
    d = root / "reports" / "agent" / "backups"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{path.name}_before_v0_3_3e_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak").write_text(
        path.read_text(encoding="utf-8", errors="replace"), encoding="utf-8"
    )

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

for rel in [
    "README.md",
    "AGENTS.md",
    "rcc/nexus/task_routing_matrix.md",
    "rcc/nexus/agent_handoff_contract.md",
    "rcc/nexus/route_map.json",
]:
    backup(root / rel, rel.replace("/", "_"))

readme_path = root / "README.md"
readme = readme_path.read_text(encoding="utf-8", errors="replace")
readme = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.3\.3[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.3.3e — Agent Contract Geometry Sync**",
    readme,
)
readme = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.3\.3[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.3.3d — README Render, Lineage, and Warning Polish**",
    readme,
)
readme = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.3\.3[a-z]? \|", "| Current checkpoint | TAU-SCALING-SA v0.3.3e |", readme)
readme = re.sub(r"\| Public README / render-lineage polish \| v0\.3\.3d \|", "| Public README / agent-geometry sync | v0.3.3e |", readme)

if "| AGENTS.md contract | synchronized with release validator |" not in readme:
    readme = readme.replace(
        "| Unified release validator | passing / step failures 0 |\n",
        "| Unified release validator | passing / step failures 0 |\n| AGENTS.md contract | synchronized with release validator |\n| Task routing matrix | geometry-aware / v0.4-ready |\n",
    )

geometry_layer = """## Agent Geometry Layer

v0.3.3e synchronizes the agent-facing contract with the Nexus geometry before v0.4.0 experiments begin.

### Geometry Principle

The repo is treated as a navigable coherence field:

```text
center  = source boundaries, non-claim locks, architecture, context indexes
inner   = claim cards, tau vectors, gates, schemas, classifier state
middle  = CLI flows, tests, scripts, benchmarks, release validator
outer   = reports, evidence packages, ledgers, visuals, release notes
```

Every patch must preserve route coherence:

```text
intent -> shell -> meridian -> sector -> files -> validation -> evidence -> lesson
```

### Coherence Gate

A patch is coherent only when these surfaces agree:

```text
README.md
AGENTS.md
rcc/nexus/task_routing_matrix.md
rcc/nexus/route_map.json
docs/context/repository_context_index.json
docs/context/rcc_nexus_index.json
target folder README.md
latest validation reports
```

### v0.4 Readiness Rule

Synthetic gate tests may begin only after the agent contract, task routing matrix, release validator, README audit, and unit tests all pass.

Non-claim lock: geometric routing improves repository orientation. It is not AI understanding, code correctness, silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling proof.
"""

if "## Agent Geometry Layer" not in readme:
    readme = readme.replace("## Process Alignment Layer", geometry_layer + "\n## Process Alignment Layer", 1)

if "Synthetic gate test patch" not in readme:
    readme = readme.replace(
        "| Release / benchmark patch | `releases/`, `docs/benchmarks/`, `reports/benchmarks/`, `reports/release/` | `python scripts/release/validate_release.py` |",
        "| Release / benchmark patch | `releases/`, `docs/benchmarks/`, `reports/benchmarks/`, `reports/release/` | `python scripts/release/validate_release.py` |\n"
        "| Synthetic gate test patch | `configs/seeds/tests/`, `reports/gates/`, `tests/`, `src/tau_scaling/gates/` | `python scripts/release/validate_release.py` + gate suite |\n"
        "| Public claim replay patch | `configs/seeds/public_claims/`, `reports/public_claims/`, source boundary docs | release validator + claim replay report |\n"
        "| Agent contract patch | `AGENTS.md`, `rcc/nexus/task_routing_matrix.md`, route map, README | README audit + release validator |",
    )

lesson = "| L-014 | README contract became more advanced than AGENTS.md and task routing matrix. | Human-facing Nexus evolved faster than agent-facing operating contract. | Agent contracts and routing matrices must be synchronized before experiments begin. |"
if lesson not in readme:
    readme = readme.replace(
        "| L-013 | v0.3.3c README had out-of-order release lineage. | Emergency repair appended rows without chronological normalization. | Release lineage and lesson ledgers must be ordered before push. |\n",
        "| L-013 | v0.3.3c README had out-of-order release lineage. | Emergency repair appended rows without chronological normalization. | Release lineage and lesson ledgers must be ordered before push. |\n" + lesson + "\n",
    )

if "| v0.3.3e | Agent contract geometry sync and v0.4 routing readiness. |" not in readme:
    readme = readme.replace(
        "| v0.3.3d | README render, lineage, and validator-warning polish. |\n",
        "| v0.3.3d | README render, lineage, and validator-warning polish. |\n| v0.3.3e | Agent contract geometry sync and v0.4 routing readiness. |\n",
    )

write(readme_path, readme)

agents = """# AGENTS.md — Tau Scaling Agent Operating Contract

Current contract: **TAU-SCALING-SA v0.3.3e — Agent Contract Geometry Sync**

## Mission

Operate inside the Tau Scaling Nexus without drifting repository state, claim boundaries, validation surfaces, or public README.

This repository is a local-first, evidence-gated tau-claim runtime. It does not independently validate silicon, product metrics, manufacturing capability, benchmark superiority, process-node equivalence, or a universal Tau Scaling law.

## Required Read Order

Before editing, read:

1. `README.md`
2. `README_90_SECONDS.md`
3. `AGENTS.md`
4. `docs/context/repository_context_index.json`
5. `docs/context/rcc_nexus_index.json`
6. `rcc/nexus/route_map.json`
7. `rcc/nexus/task_routing_matrix.md`
8. the target folder `README.md`
9. relevant source, tests, evidence, reports, or claim cards

## Geometry Route Rule

Every patch must identify its route:

```text
intent -> shell -> meridian -> sector -> files -> validation -> evidence -> lesson
```

Shell meanings:

```text
center  = source boundaries, non-claim locks, architecture, context indexes
inner   = claim cards, tau vectors, gates, schemas, classifier state
middle  = CLI flows, tests, scripts, benchmarks, release validator
outer   = reports, evidence packages, ledgers, visuals, release notes
```

## Required Validation

For every non-trivial patch, run:

```powershell
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python -m unittest discover -s tests
```

## Task-Specific Routing

| Task | Read first | Required validation |
|---|---|---|
| Runtime patch | `src/tau_scaling/README.md`, `tests/`, latest evidence | `python scripts/release/validate_release.py` |
| Claim classifier patch | `src/tau_scaling/claims/README.md`, claim cards, evidence packages | release validator + baseline/promotion claims |
| Gate logic patch | `src/tau_scaling/gates/README.md`, gate tests, synthetic claim cards | release validator + gate suite |
| README / mini README patch | root README, target mini README, route map | README audit + release validator |
| RCC-N patch | `docs/context/`, `rcc/nexus/`, route map | RCC-N checker + README audit + release validator |
| Benchmark patch | `scripts/benchmarks/`, `reports/benchmarks/`, `docs/benchmarks/` | release validator + benchmark summary |
| Synthetic gate test patch | `configs/seeds/tests/`, `reports/gates/`, gate docs | release validator + synthetic gate report |
| Public claim replay patch | source boundary docs, `configs/seeds/public_claims/`, claim reports | release validator + claim replay report |
| Directory structure patch | Full Directory Box, affected mini READMEs, context indexes | README audit + RCC-N + release validator |

## v0.4 Experiment-Start Rule

Do not begin or promote v0.4.0 Synthetic Gate Test Suite work unless:

```text
release validator: passed
README audit: passed
unit tests: OK
AGENTS.md: synchronized with README Required Validation
task_routing_matrix.md: includes synthetic gate and public claim routes
```

## Failure Learning Rule

If a failure occurs, update the AI Failure Learning Ledger in `README.md` and the affected local mini README when the failure teaches a reusable rule.

Failures are repository memory, not blame records.

## Non-Claim Locks

- navigation_is_not_validation
- documentation_is_not_correctness
- simulation_is_not_silicon_validation
- simulation_is_not_silicon_evidence
- density_equivalence_is_not_node_equivalence
- local_path_win_is_not_full_chip_win
- context_reconstruction_is_not_correctness_proof
- validation_remains_required
- release_readiness_is_not_silicon_validation
- synthetic_gate_tests_are_not_product_validation
- geometric_routing_is_not_ai_understanding
"""
write(root / "AGENTS.md", agents)

matrix = """# Task Routing Matrix

Current contract: **TAU-SCALING-SA v0.3.3e — Agent Contract Geometry Sync**

## Geometry Route

```text
intent -> shell -> meridian -> sector -> files -> validation -> evidence -> lesson
```

| Task | Shell | Meridian | Sector | Read first | Validate | Evidence output |
|---|---|---|---|---|---|---|
| Runtime patch | middle | runtime | core | `src/tau_scaling/README.md`, `tests/` | `python scripts/release/validate_release.py` | `reports/release/latest_release_readiness.md` |
| Claim classifier patch | inner | validation | runtime | `src/tau_scaling/claims/README.md`, claim cards, evidence | release validator + baseline/promotion claims | `artifacts/runs/latest/evidence_package.json` |
| Gate logic patch | inner | validation | tau | `src/tau_scaling/gates/README.md`, synthetic seeds | release validator + gate-specific tests | `reports/gates/` |
| RCC docs patch | center | agent | rcc | `README.md`, `docs/context/`, `rcc/nexus/` | `python scripts/rcc/check_rcc_nexus.py` + release validator | `reports/rcc_nexus/latest_rcc_nexus_check.md` |
| README / mini README patch | center | documentation | agent | root README, target mini README, route map | `python scripts/rcc/audit_readme_surface.py` + release validator | `reports/readme/latest_readme_mini_repo_audit.md` |
| Architecture docs patch | center | source | architecture | `docs/software_architecture/`, `docs/architecture/` | architecture validator + release validator | `reports/architecture/latest_architecture_contract_validation.md` |
| Directory structure patch | center | drift | rcc | Full Directory Box, context indexes, affected mini READMEs | README audit + RCC-N + release validator | README + context index diffs |
| Release / benchmark patch | outer | release | evidence | `releases/`, `docs/benchmarks/`, `reports/benchmarks/`, `reports/release/` | `python scripts/release/validate_release.py` | `reports/release/latest_release_readiness.md` |
| Synthetic gate test patch | inner | validation | tau | `configs/seeds/tests/`, `src/tau_scaling/gates/`, `tests/` | release validator + synthetic gate report | `reports/gates/latest_synthetic_gate_report.md` |
| Public claim replay patch | outer | evidence | release | source boundary docs, `configs/seeds/public_claims/` | release validator + claim replay report | `reports/public_claims/latest_claim_replay_report.md` |
| Agent contract patch | center | agent | rcc | `AGENTS.md`, route map, task matrix, README | README audit + release validator | `reports/agent/latest_agent_contract_sync.md` |

## Non-Claim Lock

Task routing improves repository orientation. It does not prove code correctness, patch safety, AI understanding, silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling truth.
"""
write(root / "rcc" / "nexus" / "task_routing_matrix.md", matrix)

handoff = """# Agent Handoff Contract

Current contract: **TAU-SCALING-SA v0.3.3e — Agent Contract Geometry Sync**

## Handoff Rule

An agent must leave the repository more navigable, not merely changed.

Before handoff, report:

```text
intent
shell
meridian
sector
files changed
validation run
evidence outputs
claim-boundary impact
failure lessons added
next safe action
```

## Required Final Gate

```powershell
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python -m unittest discover -s tests
```

## Non-Claim Lock

Agent handoff improves continuity and routing. It does not prove correctness, patch safety, AI understanding, silicon validation, product validation, or universal Tau Scaling law.
"""
write(root / "rcc" / "nexus" / "agent_handoff_contract.md", handoff)

route_map_path = root / "rcc" / "nexus" / "route_map.json"
try:
    route = json.loads(route_map_path.read_text(encoding="utf-8", errors="replace"))
except Exception:
    route = {}
route.setdefault("schema", "tau-scaling-rcc-nexus-route-map")
route["version"] = "v0.3.3e"
route["updated_at"] = generated_at
route["non_claim_lock"] = "Geometric routing is not code correctness, silicon validation, product validation, AI understanding, or universal Tau Scaling proof."
route["geometry"] = {
    "center": ["README.md", "AGENTS.md", "docs/context", "rcc/nexus"],
    "inner": ["configs/seeds", "src/tau_scaling/gates", "src/tau_scaling/claims", "src/tau_scaling/schemas"],
    "middle": ["src/tau_scaling", "tests", "scripts", "scripts/release"],
    "outer": ["artifacts", "outputs", "reports", "visuals", "releases"],
}
route["v0_4_routes"] = {
    "synthetic_gate_tests": {
        "read_first": ["configs/seeds/tests", "src/tau_scaling/gates", "tests", "rcc/nexus/task_routing_matrix.md"],
        "validate": ["python scripts/release/validate_release.py"],
        "evidence": ["reports/gates/latest_synthetic_gate_report.md"],
    },
    "public_claim_replay": {
        "read_first": ["docs/theory", "configs/seeds/public_claims", "reports/public_claims"],
        "validate": ["python scripts/release/validate_release.py"],
        "evidence": ["reports/public_claims/latest_claim_replay_report.md"],
    },
}
write(route_map_path, json.dumps(route, indent=2, sort_keys=True) + "\n")

agent_report = f"""# Tau Scaling Agent Contract Sync

Generated: {generated_at}

Version: TAU-SCALING-SA v0.3.3e — Agent Contract Geometry Sync

## Purpose

Synchronize the agent-facing operating contract with the README, RCC-N task routing matrix, route map, and v0.4.0 experiment-start requirements.

## Geometry Upgrade

```text
intent -> shell -> meridian -> sector -> files -> validation -> evidence -> lesson
```

## Updated Surfaces

- `README.md`
- `AGENTS.md`
- `rcc/nexus/task_routing_matrix.md`
- `rcc/nexus/agent_handoff_contract.md`
- `rcc/nexus/route_map.json`

## Non-Claim Lock

Agent contract sync improves repository coherence and routing only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, AI understanding, or universal Tau Scaling proof.
"""
write(root / "reports" / "agent" / "latest_agent_contract_sync.md", agent_report)
write(root / "reports" / "agent" / "latest_agent_contract_sync.json", json.dumps({
    "schema": "tau-scaling-agent-contract-sync-v0.3.3e",
    "generated_at": generated_at,
    "version": "v0.3.3e",
    "updated": ["README.md", "AGENTS.md", "rcc/nexus/task_routing_matrix.md", "rcc/nexus/agent_handoff_contract.md", "rcc/nexus/route_map.json"],
    "v0_4_ready_routes": ["synthetic_gate_tests", "public_claim_replay"],
    "non_claim_lock": "Agent contract sync is repository coherence only, not validation of silicon/product/universal law.",
}, indent=2, sort_keys=True) + "\n")

write(root / "docs" / "release_notes" / "tau_scaling_v0_3_3e_agent_contract_geometry_sync.md", f"""# TAU-SCALING-SA v0.3.3e — Agent Contract Geometry Sync

Generated: {generated_at}

## Purpose

This patch synchronizes AGENTS.md, the RCC-N task routing matrix, route map, and README with the v0.3.3d Nexus state before v0.4.0 synthetic gate testing begins.

## Additions

- Geometry route rule: `intent -> shell -> meridian -> sector -> files -> validation -> evidence -> lesson`
- Agent contract upgraded to use release validator as the default final gate.
- Task routing matrix expanded for synthetic gate tests, public claim replay, agent contract patches, and directory structure patches.
- Route map updated with v0.4 experiment paths.
- Agent handoff contract updated.
- L-014 added to README failure-learning ledger.

## Boundary

This is agent-routing and repository-coherence infrastructure. It does not alter Tau Scaling gate math, classifier thresholds, silicon evidence, product evidence, manufacturing evidence, or universal-law claims.
""")

write(root / "reports" / "agent" / "latest_v0_3_3e_agent_contract_geometry_sync_status.md", f"""# Tau Scaling v0.3.3e Agent Contract Geometry Sync Status

Generated: {generated_at}

Status: patched

Validation must pass before commit/push:

```powershell
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python -m unittest discover -s tests
```

Boundary:
- Agent contract and routing sync only.
""")
