from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "readme_information_architecture"
BACKUP_DIR = REPORT_DIR / "v0_8_4b" / "backups"

EXACT_AI_RULE = "## AI Rule — Directory Box and Mini README Synchronization"

REQUIRED_ANCHORS = [
    "PART I - Human README",
    "PART II - RCC Nexus README",
    "PART III - AI Agent README",
    "AI Operating Contract",
    "Patch Routing Matrix",
    "README + Mini Repo Audit Map",
    "AI Failure Learning Ledger",
    EXACT_AI_RULE,
    "Full Directory Box",
    "Public Non-Claim Locks",
]

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def backup(path: Path) -> None:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    write(BACKUP_DIR / f"{path.name}_before_v0_8_4b_{stamp}.bak", read(path))

def section(text: str, heading: str) -> str:
    pattern = rf"(^## {re.escape(heading)}\s*$.*?)(?=^## |\Z)"
    m = re.search(pattern, text, flags=re.S | re.M)
    return m.group(1).strip() if m else ""

def normalize_state(text: str) -> str:
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.8.4b - README Information Architecture Compression**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.8.4a - Release Finding Zero-Finding Repair**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|", "| Current checkpoint | TAU-SCALING-SA v0.8.4b |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.4b-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.4b |", text)
    text = re.sub(r"\| Release warning findings \| .*?\|", "| Release warning findings | 0 / v0.8.4a zero-finding repair preserved |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)
    return text

def update_lineage(text: str) -> str:
    if "| v0.8.4b |" in text:
        return text
    if "| v0.8.4a |" in text:
        return text.replace(
            "| v0.8.4a | Release Finding Zero-Finding Repair; removes remaining path-break warning after v0.8.4. |",
            "| v0.8.4a | Release Finding Zero-Finding Repair; removes remaining path-break warning after v0.8.4. |\n| v0.8.4b | README Information Architecture Compression; compresses the public README while preserving RCC-N anchors and archive routing. |"
        )
    return text

def ensure_next(text: str) -> str:
    return re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.8.5 - Public Source Ledger / Claim Provenance Map**

Recommended goals:

- Tie every public Tau claim to source category, claim type, and extraction boundary.
- Separate methodology claims, reported metrics, roadmap claims, media interpretation, and independent evidence.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

def ensure_lesson(text: str) -> str:
    if "| L-070 |" in text:
        return text
    start = text.find("### Current Lessons")
    end = text.find("### Failure Response Protocol")
    if start == -1 or end == -1 or end <= start:
        return text
    lesson = "| L-070 | v0.8.4a made the repo validator-clean, but the root README had become a historical command/report archive. | Root README accumulated every layer instead of routing historical detail to archive reports and mini READMEs. | Root README should present current research, essential validation, RCC-N anchors, and archive pointers; detailed history belongs in reports, release notes, and folder-level READMEs. |"
    block = text[start:end].rstrip() + "\n" + lesson + "\n\n"
    return text[:start] + block + text[end:]

def current_root() -> str:
    return """# Tau Scaling - Evidence-Gated Tau-Claim Runtime

![RCC-N](https://img.shields.io/badge/RCC--N-passing-brightgreen)
![Architecture](https://img.shields.io/badge/architecture-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-8%20OK-brightgreen)
![README Audit](https://img.shields.io/badge/README%20audit-passing-brightgreen)
![Benchmarks](https://img.shields.io/badge/benchmarks-12%20runs%20%2F%200%20duplicates-brightgreen)
![Claim Class](https://img.shields.io/badge/latest%20baseline-TSEK--C-blue)
![Promotion Path](https://img.shields.io/badge/promotion%20seed-TSEK--B-purple)

Repository: `tau-scaling`  
Package / CLI: `tau_scaling` / `tau-scaling`  
Current checkpoint: **TAU-SCALING-SA v0.8.4b - README Information Architecture Compression**  
Previous seal: **TAU-SCALING-SA v0.8.4a - Release Finding Zero-Finding Repair**

Tau Scaling is a local-first, evidence-gated Python runtime for evaluating Tau Scaling claims through structured claim cards, workload declarations, tau vectors, LogicFolding survivability checks, energy / thermal / PDN / PVT gates, TSEK classification, evidence packages, and RCC-N / OMN-style repository navigation.

Core law:

- No workload, no tau claim.
- No baseline, no gain.
- No gates, no validation.
- No evidence, no strong class.

## Current Research Snapshot

This repository is now in the **v0.8 public Tau research spine**.

| Layer | What it answers | Primary output |
|---|---|---|
| v0.8.2 Public Tau Claim Ledger | What are the public Tau claims and current classes? | `reports/tau_claim_ledger/latest_tau_public_claim_ledger.md` |
| v0.8.3 LogicFolding Plausibility Sweep | Under what regimes is LogicFolding plausible or fragile? | `reports/logicfolding_plausibility/latest_logicfolding_plausibility_sweep.md` |
| v0.8.4 Evidence Sufficiency Matrix | What evidence would preserve, promote, downgrade, or reject each claim? | `reports/evidence_sufficiency/latest_evidence_sufficiency_matrix.md` |
| v0.8.4a Release Finding Zero-Finding Repair | Is the repo back to a zero-warning release state? | `reports/release/latest_release_readiness.md` |

Current public finding: Tau Scaling can be studied as an evidence-gated claim system. Public claims can be separated into methodology, reported metrics, roadmap projections, topology arguments, and independent evidence.

| Finding | Current result |
|---|---:|
| Public Tau claims | 8 |
| TSEK-A public claims | 0 |
| TSEK-B public claims | 0 |
| TSEK-C public claims | 6 |
| TSEK-D public claims | 2 |
| TSEK-E public claims | 0 |
| Average missing evidence gates | 6.375 |
| Evidence sufficiency average score | 0.375 |
| LogicFolding aggressive best-case prior | 100.0% joint pass |
| LogicFolding conservative public prior | 0.0% joint pass |
| Release findings | 0 |

Interpretation: LogicFolding is conditionally plausible, not automatically validated. The repo can test plausibility and evidence sufficiency; it does not validate Huawei silicon, products, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.

## Evidence Sufficiency Matrix v0.8.4

This layer converts public Tau claim classes into explicit promotion and downgrade requirements.

- TSEK-C is not failure; it means evidence is structurally plausible but incomplete.
- TSEK-B requires declared workload, baseline, method, and companion gate evidence.
- TSEK-A requires independent reproduction, measurement protocol, uncertainty bounds, and negative controls.
- TSEK-D/E pressure appears when roadmap, density, timing, or topology claims are treated as stronger than disclosed evidence permits.

Primary outputs:

- `reports/evidence_sufficiency/latest_evidence_sufficiency_matrix.md`
- `reports/evidence_sufficiency/latest_evidence_sufficiency_matrix.json`
- `reports/evidence_sufficiency/claim_matrices/`
- `visuals/evidence_sufficiency/v0_8_4/`

Boundary: evidence sufficiency matrices define promotion conditions only. They do not promote claims, mutate thresholds, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.

## Tau Doctrine Alignment

- Time is the shared metric, not automatic proof.
- Topology helps only when overheads are dominated.
- Industrial roadmap coherence is not independent validation.
- Energy, thermal, yield, PDN/PVT, workload, and method data are required.

These rules align the software runtime with TSEK v1.3: tau is treated as a cross-layer claim object that must survive workload, gate, method, and evidence constraints before promotion.

## Human Director Box

### What this repository is

This repo is a governed claim-evaluation workbench:

claim -> source boundary -> claim card -> workload profile -> tau vector -> baseline/candidate manifests -> LogicFolding survivability -> energy/thermal/PDN/PVT gates -> TSEK classifier -> evidence package -> reports/ledgers/visuals -> release manifest

### What this repository is not

This repo does **not** independently validate silicon, Huawei product metrics, manufacturing capability, benchmark superiority, process-node equivalence, investment value, or a universal Tau Scaling law. It is a local runtime for evidence discipline and claim classification.

## Current Public Metrics

| Surface | Result |
|---|---:|
| Current checkpoint | TAU-SCALING-SA v0.8.4b |
| Release validator | passing / findings 0 / step failures 0 |
| README mini repo audit | passing / 0 warnings |
| RCC-N checker | passing / 0 warnings |
| Unit tests | 8 OK |
| Benchmark harness | 12 runs / 12 unique IDs / 0 duplicates |
| Public Tau claim ledger | `reports/tau_claim_ledger/latest_tau_public_claim_ledger.md` |
| LogicFolding plausibility sweep | `reports/logicfolding_plausibility/latest_logicfolding_plausibility_sweep.md` |
| Evidence sufficiency matrix | `reports/evidence_sufficiency/latest_evidence_sufficiency_matrix.md` |
| Evidence sufficiency visual | `visuals/evidence_sufficiency/v0_8_4/evidence_sufficiency_matrix.svg` |
| Release readiness report | `reports/release/latest_release_readiness.md` |
| Claim status | local runtime evidence + benchmark observability only |

## Quick Start

### Essential validation

```powershell
cd "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling"
.\\.venv\\Scripts\\Activate.ps1

python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
```

### Current research generators

```powershell
python scripts/benchmarks/generate_tau_public_claim_ledger.py
python scripts/benchmarks/run_logicfolding_plausibility_sweep.py
python scripts/benchmarks/generate_evidence_sufficiency_matrix.py
```

### Baseline claim checks

```powershell
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_promotion_path_claim_card.json
```

For historical benchmark commands, use the benchmark atlas and release lineage instead of expanding the root README into a command archive.

## Repository Layers

| Layer | Purpose | Main paths |
|---|---|---|
| Tau Scaling runtime | Executes claim cards, gates, classifier, evidence emission | `src/tau_scaling/`, `configs/seeds/`, `tests/` |
| Public Tau claim research | Claim ledger, LogicFolding sweep, evidence sufficiency matrix | `claims/public_tau/`, `reports/tau_claim_ledger/`, `reports/logicfolding_plausibility/`, `reports/evidence_sufficiency/` |
| RCC-N navigation | Makes the repo self-locating for humans and AI agents | `rcc/nexus/`, `docs/context/`, folder `README.md` files |
| Benchmark and evidence observability | Runs local benchmark loops and evidence package checks | `scripts/benchmarks/`, `reports/benchmarks/`, `artifacts/runs/` |
| Unified release readiness | Runs the full release gate before experiments | `scripts/release/`, `reports/release/` |
| Codex documentation shell | Records source boundaries, releases, architecture, non-claim locks | `docs/`, `reports/`, `releases/`, `visuals/` |

## Public Tau Claim Ledger v0.8.2

The repo begins source-bounded Tau Scaling research by turning public claims into explicit claim cards and a ledger.

Primary outputs:

- `claims/public_tau/`
- `reports/tau_claim_ledger/latest_tau_public_claim_ledger.md`
- `visuals/tau_claim_ledger/v0_8_2/`

Current public Tau claim status:

| TSEK class | Count |
|---|---:|
| TSEK-A | 0 |
| TSEK-B | 0 |
| TSEK-C | 6 |
| TSEK-D | 2 |
| TSEK-E | 0 |

Boundary: this ledger classifies disclosed evidence only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.

## Benchmark Finding - Stable Tau Threshold Governance v0.8.0

![Tau Scaling Benchmark Findings](visuals/stable_tau_threshold_governance/v0_8_0/tau_scaling_benchmark_findings_dashboard.svg)

The publishable result is **not** that Tau Scaling is independently validated. The publishable result is that Tau Scaling can be operationalized as an evidence-gated claim-governance runtime.

Current benchmark finding:

- Baseline claim remains TSEK-C.
- Promotion-path seed can reach TSEK-B with stronger disclosed evidence.
- v0.8.0 deferred threshold changes pending more evidence.
- No classifier mutation occurred.
- No threshold mutation occurred.
- This is local runtime governance, not silicon/product validation.

Publication lock phrase: **defer threshold change pending more evidence**.

## Historical Report Archive

The full historical chain remains available, but the root README now keeps only the current research spine and navigation essentials.

| Archive surface | Use |
|---|---|
| `docs/benchmarks/benchmark_atlas.md` | Historical benchmark and chart registry |
| `docs/release_notes/` | Versioned release notes |
| `reports/stable_tau_threshold_governance/` | v0.8.0 stable threshold milestone |
| `reports/threshold_governance_summary/` | v0.7.x threshold summary |
| `reports/approval_corridor/` | v0.6-v0.7 approval-governance corridor |
| `reports/release/latest_release_readiness.md` | Current release readiness report |
| `reports/readme/latest_readme_mini_repo_audit.md` | Current README / mini repo audit |
| `reports/rcc_nexus/latest_rcc_nexus_check.md` | Current RCC-N navigation check |

Historical detail should live in archive reports and mini READMEs, not in the root README body.
"""

def human_part() -> str:
    return """## PART I - Human README

### What Tau Scaling Tests

| Seed / surface | Purpose |
|---|---|
| `logicfolding_claim_card.json` | Tests global LogicFolding survivability and downgrade behavior. |
| `logicfolding_promotion_path_claim_card.json` | Demonstrates the evidence-promotion path to TSEK-B without weakening gates. |
| `edge_surface_boundary_toy.json` | Tests edge-bound resource starvation vs. surface-coupled scaling. |
| `gamma_tau_etp_toy.json` | Tests energy / thermal / PDN-normalized tau gain. |
| `monte_carlo_stress_toy.json` | Tests checker sensitivity under synthetic priors. |
| `codex_tau_vector_toy.json` | Tests Codex governance-latency analogy while preserving physical non-equivalence. |

Tau Scaling rewards bounded evidence emission, not confident overclaiming.

### Evidence Artifacts

Primary runtime artifacts are written under:

```
artifacts/runs/<unique-run-id>/
artifacts/runs/latest/
```

Mirrored evidence surfaces are written under:

```
outputs/evidence/
outputs/reports/
outputs/plots/
outputs/ledger/
```

Release and validation surfaces are written under:

```
releases/
reports/rcc_nexus/
reports/architecture/
reports/readme/
reports/benchmarks/
docs/benchmarks/
```
"""

def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    backup(README)
    old = read(README)
    old = normalize_state(old)
    old = ensure_lesson(old)
    old = update_lineage(old)
    old = ensure_next(old)

    tail_names = [
        "PART II - RCC Nexus README",
        "PART III - AI Agent README",
        "README + Mini Repo Audit Map",
        "AI Failure Learning Ledger",
        "Agent Geometry Layer",
        "Process Alignment Layer",
        "AI Rule — Directory Box and Mini README Synchronization",
        "Full Directory Box",
        "Unified Release Readiness Layer",
        "Public Non-Claim Locks",
        "Release Lineage",
        "Next Recommended Version",
    ]
    tail = "\n\n".join([section(old, name) for name in tail_names if section(old, name)])

    new_text = "\n\n".join([current_root(), human_part(), tail])
    new_text = normalize_state(new_text)
    new_text = ensure_lesson(new_text)
    new_text = update_lineage(new_text)
    new_text = ensure_next(new_text)
    new_text = re.sub(r"\n{3,}", "\n\n", new_text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in new_text]
    if missing:
        raise RuntimeError(f"README compression would remove required anchors: {missing}")

    write(README, new_text)

    report = {
        "schema": "tau-scaling-readme-information-architecture-compression-v0.8.4b",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.4b - README Information Architecture Compression",
        "repairs": [
            "merged current research story into Current Research Snapshot",
            "compressed Current Public Metrics to current operational rows",
            "split Quick Start into Essential Validation, Current Research Generators, and Baseline Claim Checks",
            "added Historical Report Archive pointers",
            "preserved RCC-N / Nexus audit anchors",
            "preserved AI Operating Contract and Patch Routing Matrix",
            "preserved AI Failure Learning Ledger and added L-070",
            "preserved Public Non-Claim Locks and Release Lineage",
        ],
        "anchors_preserved": REQUIRED_ANCHORS,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "boundary": "README information architecture compression improves public readability and routing only. It does not reduce RCC-N, remove evidence, validate silicon, validate products, mutate thresholds, or mutate classifier behavior.",
    }
    write(REPORT_DIR / "readme_information_architecture_compression_v0_8_4b.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "latest_readme_information_architecture_compression.json", json.dumps(report, indent=2, sort_keys=True) + "\n")

    md = "# README Information Architecture Compression v0.8.4b\n\n## Repairs\n\n"
    for item in report["repairs"]:
        md += f"- {item}\n"
    md += "\n## Anchors Preserved\n\n"
    for anchor in REQUIRED_ANCHORS:
        md += f"- {anchor}\n"
    md += "\n## Boundary\n\n" + report["boundary"] + "\n"
    write(REPORT_DIR / "readme_information_architecture_compression_v0_8_4b.md", md)
    write(REPORT_DIR / "latest_readme_information_architecture_compression.md", md)

    write(REPORT_DIR / "README.md", "# README Information Architecture Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.4b - README Information Architecture Compression**\n\n## Purpose\n\nThis folder stores reports for root README compression, routing cleanup, and public readability repairs.\n\n## README Update Rule\n\nUpdate this mini README whenever the root README public information architecture changes.\n\nBoundary: README IA compression is repository hygiene only; it does not weaken RCC-N.\n")

    release_note = "# TAU-SCALING-SA v0.8.4b - README Information Architecture Compression\n\n"
    release_note += "## Purpose\n\nCompress the root README into a clearer public landing page while preserving RCC-N / Nexus anchors and archive routing.\n\n"
    release_note += "## Added\n\n- Current Research Snapshot.\n- Compact current public metrics.\n- Essential validation commands.\n- Current research generator commands.\n- Historical Report Archive pointers.\n\n"
    release_note += "## Preserved\n\n- RCC-N / Nexus anchors.\n- AI Operating Contract.\n- Patch Routing Matrix.\n- README + Mini Repo Audit Map.\n- AI Failure Learning Ledger.\n- Full Directory Box.\n- Public Non-Claim Locks.\n- Release Lineage.\n\n"
    release_note += "## Boundary\n\nThis is public README compression only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.\n"
    write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_8_4b_readme_information_architecture_compression.md", release_note)

    print(json.dumps({
        "schema": report["schema"],
        "anchors_preserved": len(REQUIRED_ANCHORS),
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "report": "reports/readme_information_architecture/latest_readme_information_architecture_compression.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()