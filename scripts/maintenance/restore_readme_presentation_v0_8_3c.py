from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "readme_presentation_restore"
BACKUP_DIR = REPORT_DIR / "v0_8_3c" / "backups"

EXACT_AI_RULE = "## AI Rule — Directory Box and Mini README Synchronization"

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def backup(path: Path) -> None:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    write(BACKUP_DIR / f"{path.name}_before_v0_8_3c_{stamp}.bak", read(path))

def normalize_fences(text: str) -> str:
    # Root cause: earlier repair converted broken inline `text markers into five-backtick fences.
    # That made GitHub render large boxes and visible "text" labels everywhere.
    text = text.replace("`````text", "```")
    text = text.replace("````text", "```")
    text = text.replace("```text", "```")
    text = re.sub(r"`\s*``\s*ext", "```", text)
    text = re.sub(r"`\s*ext", "```", text)
    text = re.sub(r"(?m)^`$", "```", text)
    return text

def normalize_top(text: str) -> str:
    text = re.sub(
        r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Current checkpoint: **TAU-SCALING-SA v0.8.3c - README Presentation Restore**",
        text,
    )
    text = re.sub(
        r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Previous seal: **TAU-SCALING-SA v0.8.3b - README Render and Alignment Repair**",
        text,
    )
    text = re.sub(
        r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|",
        "| Current checkpoint | TAU-SCALING-SA v0.8.3c |",
        text,
    )
    text = re.sub(
        r"\| Task routing matrix \| .*?\|",
        "| Task routing matrix | geometry-aware / v0.8.3c-ready |",
        text,
    )
    text = re.sub(
        r"\| Agent contract version sync \| .*?\|",
        "| Agent contract version sync | current / v0.8.3c |",
        text,
    )
    return text

def restore_intro_sections(text: str) -> str:
    start = text.find("Core law:")
    end = text.find("## Current Public Metrics")
    if start == -1 or end == -1 or end <= start:
        return text

    replacement = """Core law:

- No workload, no tau claim.
- No baseline, no gain.
- No gates, no validation.
- No evidence, no strong class.

## Showcase Tau Findings

This repository has moved from governance construction into **Tau Scaling research instrumentation**.

**Current public finding:** Tau Scaling can be studied as an evidence-gated claim system. Public claims can be separated into methodology, reported metrics, roadmap projections, topology arguments, and independent evidence.

| Finding | Current result |
|---|---:|
| TSEK-A public claims | 0 |
| TSEK-B public claims | 0 |
| TSEK-C public claims | 6 |
| TSEK-D public claims | 2 |
| TSEK-E public claims | 0 |
| Average missing evidence gates | 6.375 |
| LogicFolding aggressive best-case prior | 100.0% joint pass |
| LogicFolding conservative public prior | 0.0% joint pass |

**Interpretation:** LogicFolding is conditionally plausible, not automatically validated. The current repo can test plausibility and evidence sufficiency; it does not validate Huawei silicon, products, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.

Primary evidence surfaces:

- `claims/public_tau/`
- `reports/tau_claim_ledger/latest_tau_public_claim_ledger.md`
- `reports/logicfolding_plausibility/latest_logicfolding_plausibility_sweep.md`
- `visuals/logicfolding_plausibility/v0_8_3/`

## Tau Doctrine Alignment

- Time is the shared metric, not automatic proof.
- Topology helps only when overheads are dominated.
- Industrial roadmap coherence is not independent validation.
- Energy, thermal, yield, PDN/PVT, workload, and method data are required.

These four rules are the public Tau doctrine lock for this repository. They align the software runtime with TSEK v1.3: tau is treated as a cross-layer claim object that must survive workload, gate, method, and evidence constraints before promotion.

## Human Director Box

### What this repository is

This repo is a governed claim-evaluation workbench. It turns a tau-scaling claim into a structured audit path:

claim -> source boundary -> claim card -> workload profile -> tau vector -> baseline/candidate manifests -> LogicFolding survivability -> edge-surface boundary model -> energy/thermal/PDN/PVT gates -> Monte Carlo checker stress -> TSEK classifier -> evidence package -> reports/ledgers/visuals -> release manifest

### What this repository is not

This repo does **not** independently validate silicon, Huawei product metrics, manufacturing capability, benchmark superiority, process-node equivalence, investment value, or a universal Tau Scaling law. It is a local runtime for evidence discipline and claim classification.

## Public Tau Claim Ledger v0.8.2

The repo now begins source-bounded Tau Scaling research by turning public claims into explicit claim cards and a ledger.

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

Interpretation: the public claim set is currently research-worthy and structurally plausible in parts, but not independently validated. The ledger preserves the boundary between methodology, reported metrics, roadmap projections, topology arguments, and independent evidence.

Command:

```powershell
python scripts/benchmarks/generate_tau_public_claim_ledger.py
```

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
- All validators passed.
- This is local runtime governance, not silicon/product validation.

Stable Tau insight: sensitivity, penalty, and boundary review did not justify changing TSEK thresholds. The current policy remains stable until stronger evidence arrives.

Publication lock phrase: **defer threshold change pending more evidence**.

Active research question: **What evidence is sufficient to move a Tau Scaling claim from roadmap coherence to a stronger evidence class without overclaiming?**

"""
    return text[:start] + replacement + text[end:]

def shrink_directory_box(text: str) -> str:
    compact = """## Full Directory Box

This section is intentionally compact. The full repository is validated by RCC-N and mini READMEs; this box gives the human/AI navigation spine without creating a giant rendered block.

| Surface | Purpose |
|---|---|
| `src/tau_scaling/` | Runtime, gates, claims, evidence, schemas, simulation, tau utilities |
| `configs/seeds/` | Claim seeds and demo/promotion-path claim cards |
| `claims/public_tau/` | Public Tau claim cards created in v0.8.2 |
| `scripts/benchmarks/` | Benchmark, sweep, report, and governance generators |
| `scripts/rcc/` | RCC-N checker and README audit scanner |
| `scripts/release/` | Unified release readiness validator |
| `reports/tau_claim_ledger/` | Public Tau claim ledger reports |
| `reports/logicfolding_plausibility/` | LogicFolding plausibility sweep outputs |
| `visuals/logicfolding_plausibility/` | LogicFolding sweep charts |
| `visuals/stable_tau_threshold_governance/` | Stable threshold governance charts |
| `docs/release_notes/` | Versioned release notes |
| `rcc/nexus/` | Route map, task matrix, Nexus handoff surfaces |
| `tests/` | Unit tests |

Update this section when a durable top-level research/report surface becomes part of the public interface.

"""
    pattern = r"## Full Directory Box.*?## Unified Release Readiness Layer"
    if re.search(pattern, text, flags=re.S):
        return re.sub(pattern, compact + "## Unified Release Readiness Layer", text, count=1, flags=re.S)
    return text

def ensure_anchor(text: str) -> str:
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)
    if EXACT_AI_RULE not in text:
        block = f"""{EXACT_AI_RULE}

This exact heading uses a Unicode em dash (U+2014) because `scripts/rcc/audit_readme_surface.py` checks this anchor literally.

This repository uses RCC-N style navigation. Repository structure is part of the public interface.

Any AI or human patch that adds, removes, renames, or repurposes a folder must update these surfaces in the same commit.

Non-claim lock: directory navigation is not correctness, but stale navigation is repository drift.

"""
        text = text.replace("## Full Directory Box", block + "## Full Directory Box", 1)
    return text

def ensure_lesson(text: str) -> str:
    if "| L-067 |" in text:
        return text
    start = text.find("### Current Lessons")
    end = text.find("### Failure Response Protocol")
    if start == -1 or end == -1:
        return text
    block = text[start:end]
    lesson = "| L-067 | v0.8.3b made validators clean but created visually heavy README boxes and visible text labels. | Repair optimized for validation and directory completeness instead of public readability. | Presentation repairs must preserve human-readable README layout: use bullets/tables for short findings and reserve fenced blocks for commands or true code. |"
    lines = block.rstrip().splitlines()
    # Insert before blank line before Failure Response Protocol by appending inside lesson table.
    if lines and lines[-1].strip() == "":
        lines = lines[:-1]
    lines.append(lesson)
    return text[:start] + "\n".join(lines) + "\n\n" + text[end:]

def ensure_next(text: str) -> str:
    next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.8.4 - Evidence Sufficiency Matrix**

Recommended goals:

- Convert public Tau claim classes into explicit evidence sufficiency requirements.
- Define what evidence would promote TSEK-C to TSEK-B and TSEK-B to TSEK-A.
- Preserve downgrade discipline and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
"""
    if "## Next Recommended Version" in text:
        return re.sub(r"## Next Recommended Version\s+.*\Z", next_section, text, flags=re.S)
    return text.rstrip() + "\n\n" + next_section

def main() -> None:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    write(BACKUP_DIR / f"README_before_v0_8_3c_{stamp}.bak", read(README))

    text = read(README)
    text = normalize_fences(text)
    text = normalize_top(text)
    text = restore_intro_sections(text)
    text = shrink_directory_box(text)
    text = ensure_anchor(text)
    text = ensure_lesson(text)
    text = ensure_next(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    write(README, text)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "schema": "tau-scaling-readme-presentation-restore-v0.8.3c",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.3c - README Presentation Restore",
        "repairs": [
            "replaced malformed five-backtick text fences",
            "converted top finding blocks back to bullets and tables",
            "shrunk Full Directory Box into a compact navigation table",
            "preserved exact audited AI Rule em-dash heading",
            "kept Tau findings and LogicFolding sweep visible",
            "added L-067 presentation-readability lesson",
        ],
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "boundary": "README presentation restore improves public readability only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    write(REPORT_DIR / "readme_presentation_restore_v0_8_3c.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "latest_readme_presentation_restore.json", json.dumps(report, indent=2, sort_keys=True) + "\n")

    md = "# README Presentation Restore v0.8.3c\n\n## Repairs\n\n"
    for item in report["repairs"]:
        md += f"- {item}\n"
    md += "\n## Boundary\n\n" + report["boundary"] + "\n"
    write(REPORT_DIR / "readme_presentation_restore_v0_8_3c.md", md)
    write(REPORT_DIR / "latest_readme_presentation_restore.md", md)

    readme_report = "# README Presentation Restore Reports\n\n"
    readme_report += "Current layer: **TAU-SCALING-SA v0.8.3c - README Presentation Restore**\n\n"
    readme_report += "## Purpose\n\nThis folder stores reports for README presentation restoration, code-fence cleanup, and compact navigation repair.\n\n"
    readme_report += "## README Update Rule\n\nUpdate this mini README whenever public README presentation or navigation layout is repaired.\n\n"
    readme_report += "Boundary: README presentation repair is repository hygiene only.\n"
    write(REPORT_DIR / "README.md", readme_report)

    release_note = "# TAU-SCALING-SA v0.8.3c - README Presentation Restore\n\n"
    release_note += "## Purpose\n\nRestore the README presentation after v0.8.3b made the public page visually heavy with malformed code fences and a giant directory box.\n\n"
    release_note += "## Repairs\n\n- Replaces malformed five-backtick `text` fences.\n- Converts top findings back to bullets and tables.\n- Shrinks Full Directory Box into a compact navigation table.\n- Preserves the exact audited heading: `AI Rule — Directory Box and Mini README Synchronization`.\n- Keeps v0.8.3 LogicFolding findings and v0.8.2 claim-ledger findings visible.\n\n"
    release_note += "## Boundary\n\nThis is README presentation repair only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.\n"
    write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_8_3c_readme_presentation_restore.md", release_note)

    print(json.dumps({
        "schema": report["schema"],
        "repairs": len(report["repairs"]),
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "report": "reports/readme_presentation_restore/latest_readme_presentation_restore.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()