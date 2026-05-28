from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "nexus_surface_sync"
BACKUP_DIR = REPORT_DIR / "v0_8_4c" / "backups"

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

DIRECTORY_ROWS = [
    ("`reports/evidence_sufficiency/`", "Evidence sufficiency matrix reports and claim-level promotion/downgrade requirements"),
    ("`visuals/evidence_sufficiency/`", "Evidence sufficiency charts"),
    ("`reports/readme_information_architecture/`", "README information architecture compression reports"),
    ("`reports/release_finding_repair/`", "Release warning inspection and zero-finding repair reports"),
]

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def backup(path: Path) -> None:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    write(BACKUP_DIR / f"{path.name}_before_v0_8_4c_{stamp}.bak", read(path))

def normalize_state(text: str) -> str:
    text = re.sub(
        r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Current checkpoint: **TAU-SCALING-SA v0.8.4c - Nexus Surface Sync Polish**",
        text,
    )
    text = re.sub(
        r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Previous seal: **TAU-SCALING-SA v0.8.4b - README Information Architecture Compression**",
        text,
    )
    text = re.sub(
        r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|",
        "| Current checkpoint | TAU-SCALING-SA v0.8.4c |",
        text,
    )
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.4c-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.4c |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)
    return text

def update_research_snapshot(text: str) -> str:
    row = "| v0.8.4b README IA Compression | Did the README remain readable without weakening RCC-N? | `reports/readme_information_architecture/latest_readme_information_architecture_compression.md` |"
    if row not in text:
        text = text.replace(
            "| v0.8.4a Release Finding Zero-Finding Repair | Is the repo back to a zero-warning release state? | `reports/release/latest_release_readiness.md` |",
            "| v0.8.4a Release Finding Zero-Finding Repair | Is the repo back to a zero-warning release state? | `reports/release/latest_release_readiness.md` |\n" + row
        )
    if "| v0.8.4c Nexus Surface Sync Polish |" not in text:
        text = text.replace(
            row,
            row + "\n| v0.8.4c Nexus Surface Sync Polish | Are current report surfaces mirrored into the Nexus directory spine? | `reports/nexus_surface_sync/latest_nexus_surface_sync_polish.md` |"
        )
    return text

def update_metrics(text: str) -> str:
    rows = [
        "| README IA compression | `reports/readme_information_architecture/latest_readme_information_architecture_compression.md` |",
        "| Nexus surface sync polish | `reports/nexus_surface_sync/latest_nexus_surface_sync_polish.md` |",
    ]
    for row in rows:
        if row not in text:
            text = text.replace("| Release readiness report | `reports/release/latest_release_readiness.md` |", "| Release readiness report | `reports/release/latest_release_readiness.md` |\n" + row)
    return text

def update_echo_location(text: str) -> str:
    text = re.sub(r"\| Last verified \| [0-9]{4}-[0-9]{2}-[0-9]{2} \|", "| Last verified | 2026-05-28 |", text)
    return text

def update_directory_box(text: str) -> str:
    for surface, purpose in DIRECTORY_ROWS:
        row = f"| {surface} | {purpose} |"
        if row in text:
            continue
        anchor = "| `reports/logicfolding_plausibility/` | LogicFolding plausibility sweep outputs |"
        if surface.startswith("`reports/evidence_sufficiency"):
            text = text.replace(anchor, anchor + "\n" + row)
        elif surface.startswith("`visuals/evidence_sufficiency"):
            anchor2 = "| `visuals/logicfolding_plausibility/` | LogicFolding sweep charts |"
            text = text.replace(anchor2, anchor2 + "\n" + row)
        elif surface.startswith("`reports/readme_information_architecture"):
            anchor3 = "| `docs/release_notes/` | Versioned release notes |"
            text = text.replace(anchor3, row + "\n" + anchor3)
        elif surface.startswith("`reports/release_finding_repair"):
            anchor4 = "| `reports/evidence_sufficiency/` | Evidence sufficiency matrix reports and claim-level promotion/downgrade requirements |"
            if anchor4 in text:
                text = text.replace(anchor4, anchor4 + "\n" + row)
            else:
                text = text.replace(anchor, anchor + "\n" + row)
    return text

def update_archive(text: str) -> str:
    archive_rows = [
        "| `reports/evidence_sufficiency/latest_evidence_sufficiency_matrix.md` | Current evidence sufficiency matrix |",
        "| `reports/readme_information_architecture/latest_readme_information_architecture_compression.md` | README IA compression report |",
        "| `reports/nexus_surface_sync/latest_nexus_surface_sync_polish.md` | Nexus surface sync polish report |",
    ]
    for row in archive_rows:
        if row not in text:
            text = text.replace("| `reports/rcc_nexus/latest_rcc_nexus_check.md` | Current RCC-N navigation check |", "| `reports/rcc_nexus/latest_rcc_nexus_check.md` | Current RCC-N navigation check |\n" + row)
    return text

def update_lineage(text: str) -> str:
    if "| v0.8.4c |" not in text and "| v0.8.4b |" in text:
        text = text.replace(
            "| v0.8.4b | README Information Architecture Compression; compresses the public README while preserving RCC-N anchors and archive routing. |",
            "| v0.8.4b | README Information Architecture Compression; compresses the public README while preserving RCC-N anchors and archive routing. |\n| v0.8.4c | Nexus Surface Sync Polish; mirrors current report surfaces into the directory box and RCC echo state. |"
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
    if "| L-071 |" in text:
        return text
    start = text.find("### Current Lessons")
    end = text.find("### Failure Response Protocol")
    if start == -1 or end == -1 or end <= start:
        return text
    block = text[start:end].rstrip()
    lesson = "| L-071 | v0.8.4b compressed the README successfully, but new current report surfaces needed to be mirrored into the directory/Nexus spine. | Compression improves readability but can hide new durable surfaces if the directory box and archive pointers are not updated. | After README compression, run a Nexus surface sync pass to ensure current reports, visuals, and verification dates are visible in the navigation spine. |"
    block += "\n" + lesson + "\n\n"
    return text[:start] + block + text[end:]

def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    backup(README)

    text = read(README)
    text = normalize_state(text)
    text = update_research_snapshot(text)
    text = update_metrics(text)
    text = update_echo_location(text)
    text = update_directory_box(text)
    text = update_archive(text)
    text = update_lineage(text)
    text = ensure_next(text)
    text = ensure_lesson(text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"Nexus surface sync would remove required anchors: {missing}")

    write(README, text)

    report = {
        "schema": "tau-scaling-nexus-surface-sync-polish-v0.8.4c",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.4c - Nexus Surface Sync Polish",
        "repairs": [
            "added current evidence_sufficiency surfaces to Full Directory Box",
            "added readme_information_architecture report surface to Full Directory Box",
            "added release_finding_repair report surface to Full Directory Box",
            "added evidence sufficiency and README IA reports to Historical Report Archive",
            "updated RCC Nexus Echo Location verified date to 2026-05-28",
            "added v0.8.4c to Current Research Snapshot and Release Lineage",
            "preserved all RCC-N / README audit anchors",
        ],
        "anchors_preserved": REQUIRED_ANCHORS,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "boundary": "Nexus surface sync polish improves navigation and report discoverability only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    write(REPORT_DIR / "nexus_surface_sync_polish_v0_8_4c.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "latest_nexus_surface_sync_polish.json", json.dumps(report, indent=2, sort_keys=True) + "\n")

    md = "# Nexus Surface Sync Polish v0.8.4c\n\n## Repairs\n\n"
    for item in report["repairs"]:
        md += f"- {item}\n"
    md += "\n## Anchors Preserved\n\n"
    for anchor in REQUIRED_ANCHORS:
        md += f"- {anchor}\n"
    md += "\n## Boundary\n\n" + report["boundary"] + "\n"
    write(REPORT_DIR / "nexus_surface_sync_polish_v0_8_4c.md", md)
    write(REPORT_DIR / "latest_nexus_surface_sync_polish.md", md)

    write(REPORT_DIR / "README.md", "# Nexus Surface Sync Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.4c - Nexus Surface Sync Polish**\n\n## Purpose\n\nThis folder stores reports for synchronizing current public surfaces into the README/Nexus navigation spine.\n\n## README Update Rule\n\nUpdate this mini README whenever durable current report surfaces are added to the public navigation layer.\n\nBoundary: Nexus surface sync is repository navigation hygiene only.\n")

    release_note = "# TAU-SCALING-SA v0.8.4c - Nexus Surface Sync Polish\n\n"
    release_note += "## Purpose\n\nMirror current evidence and README-compression surfaces into the README/Nexus navigation spine after v0.8.4b.\n\n"
    release_note += "## Added\n\n- Current evidence sufficiency surfaces in Full Directory Box.\n- README information architecture report surface in Full Directory Box.\n- Release finding repair report surface in Full Directory Box.\n- Nexus surface sync report folder.\n- Updated RCC Echo Location verified date.\n\n"
    release_note += "## Boundary\n\nThis is navigation polish only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.\n"
    write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_8_4c_nexus_surface_sync_polish.md", release_note)

    print(json.dumps({
        "schema": report["schema"],
        "anchors_preserved": len(REQUIRED_ANCHORS),
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "report": "reports/nexus_surface_sync/latest_nexus_surface_sync_polish.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()