from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGE_DIR = ROOT / "releases" / "public_research_milestone_v0_9_0"
REPORT_DIR = ROOT / "reports" / "public_research_milestone"
VIS_DIR = ROOT / "visuals" / "public_research_milestone" / "v0_9_0"

INPUTS = {
    "tau_claim_ledger": ROOT / "reports" / "tau_claim_ledger" / "latest_tau_public_claim_ledger.md",
    "logicfolding_plausibility": ROOT / "reports" / "logicfolding_plausibility" / "latest_logicfolding_plausibility_sweep.md",
    "evidence_sufficiency": ROOT / "reports" / "evidence_sufficiency" / "latest_evidence_sufficiency_matrix.md",
    "public_source_ledger": ROOT / "reports" / "public_source_ledger" / "latest_public_source_ledger.md",
    "source_evidence_intake": ROOT / "reports" / "source_evidence_intake" / "latest_source_evidence_intake_cards.md",
    "primary_source_intake_queue": ROOT / "reports" / "primary_source_intake" / "latest_primary_source_intake_queue.md",
    "public_source_population": ROOT / "reports" / "public_source_population" / "latest_public_source_population_pass.md",
    "primary_source_gap_review": ROOT / "reports" / "primary_source_gap_review" / "latest_primary_source_gap_review.md",
    "publishable_findings": ROOT / "reports" / "publishable_findings" / "latest_publishable_findings_brief.md",
    "release_readiness": ROOT / "reports" / "release" / "latest_release_readiness.md",
}

JSON_INPUTS = {
    "tau_claim_ledger": ROOT / "reports" / "tau_claim_ledger" / "latest_tau_public_claim_ledger.json",
    "logicfolding_plausibility": ROOT / "reports" / "logicfolding_plausibility" / "latest_logicfolding_plausibility_sweep.json",
    "evidence_sufficiency": ROOT / "reports" / "evidence_sufficiency" / "latest_evidence_sufficiency_matrix.json",
    "public_source_population": ROOT / "reports" / "public_source_population" / "latest_public_source_population_pass.json",
    "primary_source_gap_review": ROOT / "reports" / "primary_source_gap_review" / "latest_primary_source_gap_review.json",
    "publishable_findings": ROOT / "reports" / "publishable_findings" / "latest_publishable_findings_brief.json",
    "release_readiness": ROOT / "reports" / "release" / "latest_release_readiness.json",
}

MANIFESTS = {
    "source_population_manifest": ROOT / "sources" / "primary_source_intake" / "source_population_manifest_v0_8_8.json",
    "source_seed_manifest": ROOT / "sources" / "primary_source_intake" / "source_seed_manifest_v0_8_7.json",
}

VISUALS = {
    "primary_source_gap_review": ROOT / "visuals" / "primary_source_gap_review" / "v0_8_9" / "primary_source_gap_review.svg",
    "public_source_population": ROOT / "visuals" / "public_source_population" / "v0_8_8" / "public_source_population_pass.svg",
    "evidence_sufficiency": ROOT / "visuals" / "evidence_sufficiency" / "v0_8_4" / "evidence_sufficiency_matrix.svg",
}

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def load_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))

def copy_input(label: str, path: Path, subdir: str) -> dict:
    exists = path.exists()
    dest_rel = None
    if exists:
        dest = PACKAGE_DIR / subdir / path.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
        dest_rel = str(dest.relative_to(ROOT))
    return {"label": label, "source": str(path.relative_to(ROOT)), "exists": exists, "packaged_as": dest_rel}

def make_svg(metrics: dict) -> str:
    claims = metrics["claim_count"]
    populated = metrics["source_populated_count"]
    primary = metrics["primary_source_confirmed_count"]
    independent = metrics["independent_source_confirmed_count"]
    high_gap = metrics["high_gap_claim_count"]
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">',
        '<rect width="1600" height="900" fill="#020617"/>',
        '<text x="800" y="78" text-anchor="middle" fill="#67e8f9" font-size="46" font-family="Segoe UI" font-weight="700">Tau Scaling Public Research Milestone v0.9.0</text>',
        '<text x="800" y="126" text-anchor="middle" fill="#cbd5e1" font-size="24" font-family="Segoe UI">Evidence-gated public claim system; source-populated, not primary-validated</text>',
        f'<text x="180" y="230" fill="#f8fafc" font-size="28" font-family="Segoe UI">Public claims analyzed: {claims}</text>',
        f'<rect x="180" y="260" width="{max(1,populated)*105}" height="50" rx="12" fill="#22c55e"/>',
        f'<text x="180" y="350" fill="#f8fafc" font-size="28" font-family="Segoe UI">Source-populated claims: {populated}</text>',
        f'<rect x="180" y="380" width="{max(1,primary)*105}" height="50" rx="12" fill="#f59e0b"/>',
        f'<text x="180" y="470" fill="#f8fafc" font-size="28" font-family="Segoe UI">Primary-source confirmed: {primary}</text>',
        f'<rect x="180" y="500" width="{max(1,independent)*105}" height="50" rx="12" fill="#a78bfa"/>',
        f'<text x="180" y="590" fill="#f8fafc" font-size="28" font-family="Segoe UI">Independent-source confirmed: {independent}</text>',
        f'<rect x="180" y="620" width="{max(1,high_gap)*105}" height="50" rx="12" fill="#ef4444"/>',
        f'<text x="180" y="710" fill="#f8fafc" font-size="28" font-family="Segoe UI">High validation-gap claims: {high_gap}</text>',
        '<text x="800" y="830" text-anchor="middle" fill="#94a3b8" font-size="22" font-family="Segoe UI">Publishable as source-provenance and validation-gap analysis; not as silicon validation.</text>',
        '</svg>',
    ])

def main():
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    gap = load_json(JSON_INPUTS["primary_source_gap_review"]) or {}
    release = load_json(JSON_INPUTS["release_readiness"]) or {}
    claim = load_json(JSON_INPUTS["tau_claim_ledger"]) or {}

    metrics = {
        "claim_count": int(gap.get("claim_count", claim.get("claim_count", 0))),
        "source_populated_count": int(gap.get("source_populated_count", 0)),
        "primary_source_confirmed_count": int(gap.get("primary_source_confirmed_count", 0)),
        "independent_source_confirmed_count": int(gap.get("independent_source_confirmed_count", 0)),
        "high_gap_claim_count": int(gap.get("high_gap_claim_count", 0)),
        "average_gap_count": float(gap.get("average_gap_count", 0.0)),
        "average_source_confidence": float(gap.get("average_source_confidence", 0.0)),
        "release_findings": len(release.get("findings", [])) if isinstance(release.get("findings", []), list) else int(release.get("findings", 0) or 0),
        "release_passed": bool(release.get("passed", False)),
    }

    package_items = []
    for label, path in INPUTS.items():
        package_items.append(copy_input(label, path, "reports"))
    for label, path in JSON_INPUTS.items():
        package_items.append(copy_input(label, path, "json"))
    for label, path in MANIFESTS.items():
        package_items.append(copy_input(label, path, "manifests"))
    for label, path in VISUALS.items():
        package_items.append(copy_input(label, path, "visuals"))

    milestone = {
        "schema": "tau-scaling-public-research-milestone-v0.9.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "title": "Tau Scaling as an Evidence-Gated Public Claim System",
        "subtitle": "Source Population, Primary-Validation Gaps, and Non-Claim Locks",
        "metrics": metrics,
        "package_dir": str(PACKAGE_DIR.relative_to(ROOT)),
        "package_items": package_items,
        "publishable_claim": "Tau Scaling public claims can be represented as an evidence-gated claim system with reproducible source-provenance and primary-validation gap surfaces.",
        "non_claims": [
            "This package does not validate silicon.",
            "This package does not validate Huawei products.",
            "This package does not prove benchmark superiority.",
            "This package does not establish process-node equivalence.",
            "This package does not establish a universal Tau Scaling law.",
            "This package does not promote any public Tau claim beyond its evidence gates.",
        ],
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "primary_source_validation_claimed": False,
        "independent_validation_claimed": False,
    }

    write_json(PACKAGE_DIR / "public_research_milestone_manifest_v0_9_0.json", milestone)
    write_json(REPORT_DIR / "latest_public_research_milestone.json", milestone)
    write_json(REPORT_DIR / "public_research_milestone_v0_9_0.json", milestone)

    summary = "# Tau Scaling Public Research Milestone v0.9.0\n\n"
    summary += "## Title\n\nTau Scaling as an Evidence-Gated Public Claim System\n\n"
    summary += "## Core Publishable Finding\n\n"
    summary += milestone["publishable_claim"] + "\n\n"
    summary += "## Quantitative Snapshot\n\n"
    for key, val in metrics.items():
        summary += f"- {key}: `{val}`\n"
    summary += "\n## What This Package Includes\n\n"
    for item in package_items:
        status = "included" if item["exists"] else "missing"
        summary += f"- `{item['label']}`: {status}"
        if item["packaged_as"]:
            summary += f" -> `{item['packaged_as']}`"
        summary += "\n"
    summary += "\n## Non-Claim Locks\n\n"
    for item in milestone["non_claims"]:
        summary += f"- {item}\n"
    summary += "\n## Interpretation\n\n"
    summary += "The v0.8 spine has matured into a release-quality public research package. Its contribution is not proof of Tau Scaling, LogicFolding, or silicon performance. Its contribution is a reproducible evidence machine for public semiconductor claims: claim ledger, source ledger, source population, validation-gap matrix, visuals, release checks, and explicit non-claim locks.\n"
    write(PACKAGE_DIR / "README.md", summary)
    write(REPORT_DIR / "latest_public_research_milestone.md", summary)
    write(REPORT_DIR / "public_research_milestone_v0_9_0.md", summary)

    citation = "# Citation / Reference Note v0.9.0\n\n"
    citation += "James Paul Jackson. Tau Scaling as an Evidence-Gated Public Claim System: Source Population, Primary-Validation Gaps, and Non-Claim Locks. Public Research Milestone Package v0.9.0.\n\n"
    citation += "Boundary: cite as a repository-based evidence-governance artifact, not as semiconductor validation.\n"
    write(PACKAGE_DIR / "CITATION_NOTE.md", citation)

    visual = make_svg(metrics)
    write(VIS_DIR / "public_research_milestone.svg", visual)
    write(VIS_DIR / "README.md", "# Public Research Milestone Visuals v0.9.0\n\n- `public_research_milestone.svg`\n\nBoundary: visualizes source-provenance / validation-gap state only.\n")

    print(json.dumps({
        "schema": milestone["schema"],
        "claim_count": metrics["claim_count"],
        "source_populated_count": metrics["source_populated_count"],
        "primary_source_confirmed_count": metrics["primary_source_confirmed_count"],
        "independent_source_confirmed_count": metrics["independent_source_confirmed_count"],
        "high_gap_claim_count": metrics["high_gap_claim_count"],
        "release_passed": metrics["release_passed"],
        "release_findings": metrics["release_findings"],
        "thresholds_changed": milestone["thresholds_changed"],
        "classifier_changed": milestone["classifier_changed"],
        "mutation_allowed": milestone["mutation_allowed"],
        "application_allowed": milestone["application_allowed"],
        "claim_promotion_allowed": milestone["claim_promotion_allowed"],
        "source_validation_claimed": milestone["source_validation_claimed"],
        "report": "reports/public_research_milestone/latest_public_research_milestone.md",
        "package": "releases/public_research_milestone_v0_9_0/README.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()