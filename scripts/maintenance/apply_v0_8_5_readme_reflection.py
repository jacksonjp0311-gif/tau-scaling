from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "public_source_ledger"
BACKUP_DIR = REPORT_DIR / "v0_8_5" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v0_8_5_{stamp}.bak", read(path))

def normalize_state(text: str) -> str:
    text = re.sub(
        r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Current checkpoint: **TAU-SCALING-SA v0.8.5 - Public Source Ledger / Claim Provenance Map**",
        text,
    )
    text = re.sub(
        r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Previous seal: **TAU-SCALING-SA v0.8.4c - Nexus Surface Sync Polish**",
        text,
    )
    text = re.sub(
        r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|",
        "| Current checkpoint | TAU-SCALING-SA v0.8.5 |",
        text,
    )
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.5-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.5 |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)
    return text

def insert_after(text: str, anchor_heading: str, section: str) -> str:
    if section.splitlines()[0] in text:
        return text
    pattern = rf"(^## {re.escape(anchor_heading)}\s*$.*?)(?=^## |\Z)"
    m = re.search(pattern, text, flags=re.S | re.M)
    if not m:
        return text + "\n\n" + section
    return text[:m.end()] + "\n\n" + section + text[m.end():]

def update_research_snapshot(text: str) -> str:
    row = "| v0.8.5 Public Source Ledger | Which source category produced each claim, and how far can it carry the claim? | `reports/public_source_ledger/latest_public_source_ledger.md` |"
    if row not in text:
        text = text.replace(
            "| v0.8.4c Nexus Surface Sync Polish | Are current report surfaces mirrored into the Nexus directory spine? | `reports/nexus_surface_sync/latest_nexus_surface_sync_polish.md` |",
            "| v0.8.4c Nexus Surface Sync Polish | Are current report surfaces mirrored into the Nexus directory spine? | `reports/nexus_surface_sync/latest_nexus_surface_sync_polish.md` |\n" + row
        )
    return text

def update_metrics(text: str) -> str:
    rows = [
        "| Public source ledger | `reports/public_source_ledger/latest_public_source_ledger.md` |",
        "| Source ledger visual | `visuals/public_source_ledger/v0_8_5/public_source_ledger.svg` |",
        "| Law of Sufficient Form | `docs/reflection/law_of_sufficient_form_v0_8_5.md` |",
    ]
    for row in rows:
        if row not in text:
            text = text.replace("| Evidence sufficiency matrix | `reports/evidence_sufficiency/latest_evidence_sufficiency_matrix.md` |", "| Evidence sufficiency matrix | `reports/evidence_sufficiency/latest_evidence_sufficiency_matrix.md` |\n" + row)
    return text

def add_reflection_section(text: str) -> str:
    section = """## Reflection: Law of Sufficient Form

> When enough governed form is in place, structure begins to hold itself.

Operational form: A system becomes self-stabilizing when its claims, evidence, routing, validation, memory, and non-claim locks are all visible to both humans and agents.

This reflection is part of the repository's operating memory. It can be expanded occasionally as the system matures, but it must remain bounded: reflection names process insight; it does not replace validation, evidence, source provenance, or non-claim locks.

Primary reflection surface:

- `docs/reflection/law_of_sufficient_form_v0_8_5.md`
"""
    return insert_after(text, "Tau Doctrine Alignment", section)

def add_source_ledger_section(text: str) -> str:
    section = """## Public Source Ledger / Claim Provenance Map v0.8.5

This layer maps each public Tau claim to a source category, source-carry boundary, allowed carry, blocked carry, and promotion blockers.

Primary outputs:

- `reports/public_source_ledger/latest_public_source_ledger.md`
- `reports/public_source_ledger/latest_public_source_ledger.json`
- `reports/public_source_ledger/claim_sources/`
- `visuals/public_source_ledger/v0_8_5/`
- `docs/reflection/law_of_sufficient_form_v0_8_5.md`

Source categories:

- methodology_claim
- reported_metric
- roadmap_projection
- media_interpretation
- architecture_interpretation
- independent_evidence
- unknown_or_unresolved

Boundary: source provenance maps source-carry boundaries only. It does not promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.
"""
    return insert_after(text, "Evidence Sufficiency Matrix v0.8.4", section)

def update_quick_start(text: str) -> str:
    cmd = "python scripts/benchmarks/generate_public_source_ledger.py"
    if cmd not in text:
        text = text.replace(
            "python scripts/benchmarks/generate_evidence_sufficiency_matrix.py",
            "python scripts/benchmarks/generate_evidence_sufficiency_matrix.py\n" + cmd
        )
    return text

def update_directory_box(text: str) -> str:
    rows = [
        "| `reports/public_source_ledger/` | Public source provenance and source-carry boundary reports |",
        "| `visuals/public_source_ledger/` | Public source ledger charts |",
        "| `docs/reflection/` | Reflection notes including the Law of Sufficient Form |",
    ]
    for row in rows:
        if row not in text:
            if "reports/public_source_ledger" in row:
                text = text.replace("| `reports/evidence_sufficiency/` | Evidence sufficiency matrix reports and claim-level promotion/downgrade requirements |", "| `reports/evidence_sufficiency/` | Evidence sufficiency matrix reports and claim-level promotion/downgrade requirements |\n" + row)
            elif "visuals/public_source_ledger" in row:
                text = text.replace("| `visuals/evidence_sufficiency/` | Evidence sufficiency charts |", "| `visuals/evidence_sufficiency/` | Evidence sufficiency charts |\n" + row)
            elif "docs/reflection" in row:
                text = text.replace("| `docs/release_notes/` | Versioned release notes |", "| `docs/release_notes/` | Versioned release notes |\n" + row)
    return text

def update_archive(text: str) -> str:
    rows = [
        "| `reports/public_source_ledger/latest_public_source_ledger.md` | Public source ledger and claim provenance map |",
        "| `docs/reflection/law_of_sufficient_form_v0_8_5.md` | Law of Sufficient Form reflection |",
    ]
    for row in rows:
        if row not in text:
            text = text.replace("| `reports/nexus_surface_sync/latest_nexus_surface_sync_polish.md` | Nexus surface sync polish report |", "| `reports/nexus_surface_sync/latest_nexus_surface_sync_polish.md` | Nexus surface sync polish report |\n" + row)
    return text

def update_lineage(text: str) -> str:
    if "| v0.8.5 |" not in text and "| v0.8.4c |" in text:
        text = text.replace(
            "| v0.8.4c | Nexus Surface Sync Polish; mirrors current report surfaces into the directory box and RCC echo state. |",
            "| v0.8.4c | Nexus Surface Sync Polish; mirrors current report surfaces into the directory box and RCC echo state. |\n| v0.8.5 | Public Source Ledger / Claim Provenance Map; maps source categories, source-carry boundaries, and reflection law into the public Tau claim spine. |"
        )
    return text

def update_next(text: str) -> str:
    return re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.8.6 - Source Evidence Intake Cards**

Recommended goals:

- Add source evidence intake cards for each public Tau claim.
- Require URL/citation, source type, quote/paraphrase boundary, and claim-carry limit.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

def ensure_lesson(text: str) -> str:
    if "| L-072 |" in text:
        return text
    start = text.find("### Current Lessons")
    end = text.find("### Failure Response Protocol")
    if start == -1 or end == -1 or end <= start:
        return text
    block = text[start:end].rstrip()
    lesson = "| L-072 | The Law of Sufficient Form emerged during the v0.8.4c stabilization sequence. | Once claim, evidence, routing, validation, memory, and non-claim locks were visible, the repo began acting like a self-stabilizing substrate. | Major process insights should be added to a reflection surface, but reflection must remain bounded by validation and source provenance. |"
    block += "\n" + lesson + "\n\n"
    return text[:start] + block + text[end:]

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    backup(README)

    text = read(README)
    text = normalize_state(text)
    text = update_research_snapshot(text)
    text = add_source_ledger_section(text)
    text = add_reflection_section(text)
    text = update_metrics(text)
    text = update_quick_start(text)
    text = update_directory_box(text)
    text = update_archive(text)
    text = update_lineage(text)
    text = update_next(text)
    text = ensure_lesson(text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.8.5 README patch would remove required anchors: {missing}")

    write(README, text)

    report = {
        "schema": "tau-scaling-v0.8.5-readme-reflection-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.5 - Public Source Ledger / Claim Provenance Map",
        "repairs": [
            "added Law of Sufficient Form reflection section",
            "added public source ledger section",
            "updated current research snapshot",
            "updated current metrics and quick start",
            "updated directory box and archive pointers",
            "updated release lineage and next version target",
            "added L-072 failure/reflection lesson",
        ],
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "boundary": "README/reflection patch is source provenance and reflection routing only. It does not validate silicon or promote claims.",
    }
    write(REPORT_DIR / "readme_reflection_patch_v0_8_5.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_reflection_patch_v0_8_5.md", "# README Reflection Patch v0.8.5\n\n" + "\n".join(f"- {x}" for x in report["repairs"]) + "\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "report": "reports/public_source_ledger/readme_reflection_patch_v0_8_5.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()