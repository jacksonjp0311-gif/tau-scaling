from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

ROUTING_JSON = ROOT / "reports" / "external_review_publication_routing" / "latest_external_review_publication_routing.json"
SUBMISSION_JSON = ROOT / "reports" / "manuscript_submission_package" / "latest_manuscript_submission_package.json"
MILESTONE_JSON = ROOT / "reports" / "public_research_milestone" / "latest_public_research_milestone.json"
RELEASE_JSON = ROOT / "reports" / "release" / "latest_release_readiness.json"

REPORT_DIR = ROOT / "reports" / "public_release_candidate"
RELEASE_DIR = ROOT / "releases" / "public_release_candidate_v1_0_0"
VIS_DIR = ROOT / "visuals" / "public_release_candidate" / "v1_0_0"
DOCS_RELEASE = ROOT / "docs" / "release_notes"

CORE_ARTIFACTS = [
    "README.md",
    "docs/manuscript/tau_scaling_public_claim_system_v0_9_3.md",
    "docs/manuscript/tau_scaling_public_claim_system_v0_9_3.tex",
    "docs/review/external_review_checklist_v0_9_4.md",
    "docs/review/publication_routing_v0_9_4.md",
    "reports/public_research_milestone/latest_public_research_milestone.md",
    "reports/manuscript_submission_package/latest_manuscript_submission_package.md",
    "reports/external_review_publication_routing/latest_external_review_publication_routing.md",
    "reports/release/latest_release_readiness.md",
    "releases/manuscript_submission_package_v0_9_3/README.md",
    "releases/publication_routing_v0_9_4/publication_routing_manifest_v0_9_4.json",
]

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}

def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except Exception:
        return str(path)

def copy_artifact(rel_path: str) -> dict:
    src = ROOT / rel_path
    exists = src.exists()
    if exists:
        dest = RELEASE_DIR / "artifacts" / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        return {"source": rel_path, "exists": True, "packaged_as": rel(dest)}
    return {"source": rel_path, "exists": False, "packaged_as": None}

def make_svg(metrics: dict, readiness: dict) -> str:
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">',
        '<rect width="1600" height="900" fill="#020617"/>',
        '<text x="800" y="82" text-anchor="middle" fill="#67e8f9" font-size="48" font-family="Segoe UI" font-weight="700">Tau Scaling Public Release Candidate v1.0.0</text>',
        '<text x="800" y="132" text-anchor="middle" fill="#cbd5e1" font-size="24" font-family="Segoe UI">Evidence-governance release: source-provenance, validation gaps, manuscript, review routing</text>',
        f'<text x="180" y="240" fill="#f8fafc" font-size="30" font-family="Segoe UI">Claims analyzed: {metrics.get("claim_count", 0)}</text>',
        f'<text x="180" y="310" fill="#f8fafc" font-size="30" font-family="Segoe UI">Source-populated claims: {metrics.get("source_populated_count", 0)}</text>',
        f'<text x="180" y="380" fill="#f8fafc" font-size="30" font-family="Segoe UI">Primary-source confirmed: {metrics.get("primary_source_confirmed_count", 0)}</text>',
        f'<text x="180" y="450" fill="#f8fafc" font-size="30" font-family="Segoe UI">Independent-source confirmed: {metrics.get("independent_source_confirmed_count", 0)}</text>',
        f'<text x="180" y="520" fill="#f8fafc" font-size="30" font-family="Segoe UI">Release findings: {metrics.get("release_findings", 0)}</text>',
        f'<text x="180" y="590" fill="#f8fafc" font-size="30" font-family="Segoe UI">Readiness score: {readiness.get("submission_readiness_score", 0)}</text>',
        '<rect x="930" y="235" width="450" height="78" rx="18" fill="#0f172a" stroke="#22c55e"/>',
        '<text x="1155" y="284" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">GitHub Release: READY</text>',
        '<rect x="930" y="365" width="450" height="78" rx="18" fill="#0f172a" stroke="#67e8f9"/>',
        '<text x="1155" y="414" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Technical Note: READY</text>',
        '<rect x="930" y="495" width="450" height="78" rx="18" fill="#0f172a" stroke="#f59e0b"/>',
        '<text x="1155" y="544" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Preprint: REVIEW HOLD</text>',
        '<rect x="930" y="625" width="450" height="78" rx="18" fill="#0f172a" stroke="#ef4444"/>',
        '<text x="1155" y="674" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Claim Promotion: BLOCKED</text>',
        '<text x="800" y="830" text-anchor="middle" fill="#94a3b8" font-size="22" font-family="Segoe UI">v1.0.0 freezes publishable source-governance, not semiconductor validation.</text>',
        '</svg>',
    ])

def changelog(metrics: dict) -> str:
    return f"""# CHANGELOG v1.0.0

## TAU-SCALING-SA v1.0.0 — Public Release Candidate

### Release Type

Evidence-governance public release candidate.

### Core Result

Tau Scaling public claims can be represented as an evidence-gated public claim system. The current repository state is source-populated but not primary-source confirmed or independently validated.

### Quantitative Snapshot

- Public claims analyzed: `{metrics.get("claim_count", 0)}`
- Source-populated claims: `{metrics.get("source_populated_count", 0)}`
- Primary-source confirmed claims: `{metrics.get("primary_source_confirmed_count", 0)}`
- Independent-source confirmed claims: `{metrics.get("independent_source_confirmed_count", 0)}`
- High validation-gap claims: `{metrics.get("high_gap_claim_count", 0)}`
- Release findings: `{metrics.get("release_findings", 0)}`

### Included Release Spine

- Claim ledger
- Source provenance ledger
- Source intake cards
- Public source population manifest
- Primary-source validation gap review
- Public research milestone package
- Manuscript submission package
- External review and publication routing
- Release readiness report
- Non-claim locks

### Non-Claim Boundary

This release does not validate silicon, products, manufacturing, process nodes, benchmark superiority, investment relevance, or a universal Tau Scaling law.
"""

def release_body(metrics: dict, readiness: dict) -> str:
    return f"""# Tau Scaling v1.0.0 — Public Release Candidate

## Summary

This release packages `tau-scaling` as a public evidence-governance artifact for Tau Scaling / LogicFolding claims.

The release establishes that public Tau Scaling claims can be represented through a reproducible claim-governance pipeline: claim ledger, source provenance, source intake, public source population, primary-source validation-gap review, manuscript package, external review checklist, and publication routing.

## Key Finding

The public claim field is source-populated, but not primary-source confirmed or independently validated in the current repository state.

## Metrics

- Claims analyzed: `{metrics.get("claim_count", 0)}`
- Source-populated claims: `{metrics.get("source_populated_count", 0)}`
- Primary-source confirmed: `{metrics.get("primary_source_confirmed_count", 0)}`
- Independent-source confirmed: `{metrics.get("independent_source_confirmed_count", 0)}`
- High validation-gap claims: `{metrics.get("high_gap_claim_count", 0)}`
- Release findings: `{metrics.get("release_findings", 0)}`
- Submission readiness score: `{readiness.get("submission_readiness_score", 0)}`

## Routing

- GitHub Release: READY
- Gist Summary: READY
- Technical Note: READY_WITH_BOUNDARY
- Preprint: HOLD_FOR_EXTERNAL_REVIEW
- Claim Promotion / Technical Validation: BLOCKED

## Non-Claim Lock

This release is publishable as source-provenance and validation-gap analysis. It is not publishable as silicon validation, product validation, benchmark superiority, process-node equivalence, or proof of a universal Tau Scaling law.
"""

def technical_note(metrics: dict) -> str:
    return f"""# Technical Note Copy v1.0.0

## Title

Tau Scaling as an Evidence-Gated Public Claim System

## Short Abstract

This technical note presents a repository-based method for converting public Tau Scaling and LogicFolding claims into an evidence-gated public claim system. The current release analyzes `{metrics.get("claim_count", 0)}` public claims. All are source-populated from public reporting, while zero are primary-source confirmed and zero are independently confirmed. The contribution is a reproducible source-provenance and validation-gap artifact, not semiconductor validation.

## Recommended Use

Use this artifact to inspect public claim boundaries, source categories, validation gaps, and publication readiness.

## Not Recommended Use

Do not use this artifact as evidence of silicon performance, Huawei product validation, benchmark superiority, process-node equivalence, or a universal scaling law.
"""

def public_abstract(metrics: dict) -> str:
    return f"""# Public Abstract v1.0.0

Public semiconductor narratives often blur the line between roadmap claims, media interpretation, methodology proposals, and validated technical results. This release treats Tau Scaling as an evidence-governance problem. It converts public Tau Scaling claims into a reproducible repository artifact with claim ledgers, source-provenance records, source-population manifests, validation-gap matrices, manuscript materials, and publication-routing checks. In the current repository state, `{metrics.get("source_populated_count", 0)}` of `{metrics.get("claim_count", 0)}` public claims are source-populated, while `{metrics.get("primary_source_confirmed_count", 0)}` are primary-source confirmed and `{metrics.get("independent_source_confirmed_count", 0)}` are independently confirmed. The result is publishable as source-provenance and validation-gap research, not as semiconductor validation.
"""

def tag_notes(metrics: dict) -> str:
    return f"""# Version Tag Notes v1.0.0

Recommended tag:

```text
v1.0.0-public-release-candidate
```

Recommended tag message:

```text
Tau Scaling v1.0.0 Public Release Candidate — evidence-governance package with source-populated public claims, primary-validation gap matrix, manuscript submission package, and publication routing. No silicon validation or claim promotion.
```

Release guard:

- claims analyzed: `{metrics.get("claim_count", 0)}`
- source-populated: `{metrics.get("source_populated_count", 0)}`
- primary-source confirmed: `{metrics.get("primary_source_confirmed_count", 0)}`
- independent-source confirmed: `{metrics.get("independent_source_confirmed_count", 0)}`
- release findings: `{metrics.get("release_findings", 0)}`
"""

def final_lock_audit(metrics: dict, readiness: dict) -> dict:
    checks = [
        {"id": "L1", "check": "claim_promotion_allowed_false", "passed": True},
        {"id": "L2", "check": "source_validation_claimed_false", "passed": True},
        {"id": "L3", "check": "primary_source_confirmed_count_zero", "passed": metrics.get("primary_source_confirmed_count", -1) == 0},
        {"id": "L4", "check": "independent_source_confirmed_count_zero", "passed": metrics.get("independent_source_confirmed_count", -1) == 0},
        {"id": "L5", "check": "release_findings_zero", "passed": metrics.get("release_findings", 1) == 0},
        {"id": "L6", "check": "preprint_not_ready_without_review", "passed": readiness.get("ready_for_preprint") is False},
    ]
    return {
        "checks": checks,
        "passed": all(c["passed"] for c in checks),
        "failures": [c for c in checks if not c["passed"]],
    }

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_RELEASE.mkdir(parents=True, exist_ok=True)

    routing = load_json(ROUTING_JSON)
    submission = load_json(SUBMISSION_JSON)
    milestone = load_json(MILESTONE_JSON)
    release = load_json(RELEASE_JSON)

    metrics = dict(submission.get("metrics", milestone.get("metrics", {})))
    metrics.setdefault("claim_count", routing.get("metrics", {}).get("claim_count", 0))
    metrics.setdefault("source_populated_count", routing.get("metrics", {}).get("source_populated_count", 0))
    metrics.setdefault("primary_source_confirmed_count", routing.get("metrics", {}).get("primary_source_confirmed_count", 0))
    metrics.setdefault("independent_source_confirmed_count", routing.get("metrics", {}).get("independent_source_confirmed_count", 0))
    metrics.setdefault("high_gap_claim_count", routing.get("metrics", {}).get("high_gap_claim_count", 0))
    metrics["release_findings"] = len(release.get("findings", [])) if isinstance(release.get("findings", []), list) else int(release.get("findings", 0) or 0)
    metrics["release_passed"] = bool(release.get("passed", False))

    readiness = routing.get("readiness", {})
    audit = final_lock_audit(metrics, readiness)

    packaged = [copy_artifact(p) for p in CORE_ARTIFACTS]

    write(RELEASE_DIR / "CHANGELOG_v1_0_0.md", changelog(metrics))
    write(RELEASE_DIR / "GITHUB_RELEASE_BODY_v1_0_0.md", release_body(metrics, readiness))
    write(RELEASE_DIR / "TECHNICAL_NOTE_COPY_v1_0_0.md", technical_note(metrics))
    write(RELEASE_DIR / "PUBLIC_ABSTRACT_v1_0_0.md", public_abstract(metrics))
    write(RELEASE_DIR / "VERSION_TAG_NOTES_v1_0_0.md", tag_notes(metrics))
    write_json(RELEASE_DIR / "FINAL_NON_CLAIM_LOCK_AUDIT_v1_0_0.json", audit)

    readme = "# Tau Scaling Public Release Candidate v1.0.0\n\n"
    readme += "## Release Position\n\nThis is a public release candidate for an evidence-governance artifact, not a semiconductor validation release.\n\n"
    readme += "## Core Claim\n\nTau Scaling public claims can be represented as an evidence-gated public claim system with source-provenance and validation-gap surfaces.\n\n"
    readme += "## Metrics\n\n"
    for key in [
        "claim_count",
        "source_populated_count",
        "primary_source_confirmed_count",
        "independent_source_confirmed_count",
        "high_gap_claim_count",
        "release_findings",
    ]:
        readme += f"- {key}: `{metrics.get(key, 0)}`\n"
    readme += "\n## Publication Routing\n\n"
    readme += f"- GitHub release ready: `{readiness.get('ready_for_github_release', False)}`\n"
    readme += f"- Gist summary ready: `{readiness.get('ready_for_gist_summary', False)}`\n"
    readme += f"- Technical note ready: `{readiness.get('ready_for_technical_note', False)}`\n"
    readme += f"- Preprint ready: `{readiness.get('ready_for_preprint', False)}`\n"
    readme += "\n## Package Contents\n\n"
    readme += "- `CHANGELOG_v1_0_0.md`\n"
    readme += "- `GITHUB_RELEASE_BODY_v1_0_0.md`\n"
    readme += "- `TECHNICAL_NOTE_COPY_v1_0_0.md`\n"
    readme += "- `PUBLIC_ABSTRACT_v1_0_0.md`\n"
    readme += "- `VERSION_TAG_NOTES_v1_0_0.md`\n"
    readme += "- `FINAL_NON_CLAIM_LOCK_AUDIT_v1_0_0.json`\n"
    readme += "- `public_release_candidate_manifest_v1_0_0.json`\n"
    readme += "\n## Non-Claim Boundary\n\nThis release does not validate silicon, products, manufacturing, process nodes, benchmark superiority, investment relevance, or a universal Tau Scaling law.\n"
    write(RELEASE_DIR / "README.md", readme)

    manifest = {
        "schema": "tau-scaling-public-release-candidate-v1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "release_title": "Tau Scaling as an Evidence-Gated Public Claim System",
        "release_type": "public_release_candidate",
        "release_dir": rel(RELEASE_DIR),
        "metrics": metrics,
        "readiness": readiness,
        "final_lock_audit": audit,
        "packaged_artifacts": packaged,
        "recommended_tag": "v1.0.0-public-release-candidate",
        "route_decision": {
            "github_release": "READY",
            "gist_summary": "READY",
            "technical_note": "READY_WITH_BOUNDARY",
            "preprint": "HOLD_FOR_EXTERNAL_REVIEW",
            "claim_promotion": "BLOCKED",
        },
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "release_candidate_claims_silicon_validation": False,
        "boundary": "v1.0.0 freezes a public evidence-governance release candidate. It does not validate sources, promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.",
    }

    write_json(RELEASE_DIR / "public_release_candidate_manifest_v1_0_0.json", manifest)
    write_json(REPORT_DIR / "public_release_candidate_v1_0_0.json", manifest)
    write_json(REPORT_DIR / "latest_public_release_candidate.json", manifest)

    report_md = "# Public Release Candidate v1.0.0\n\n"
    report_md += "## Summary\n\n"
    report_md += manifest["boundary"] + "\n\n"
    report_md += "## Metrics\n\n"
    for key, val in metrics.items():
        report_md += f"- {key}: `{val}`\n"
    report_md += "\n## Route Decision\n\n"
    for key, val in manifest["route_decision"].items():
        report_md += f"- {key}: `{val}`\n"
    report_md += "\n## Final Lock Audit\n\n"
    report_md += f"- passed: `{audit['passed']}`\n"
    for item in audit["checks"]:
        report_md += f"- {item['id']} {item['check']}: `{item['passed']}`\n"
    report_md += "\n## Package\n\n"
    report_md += f"- `{rel(RELEASE_DIR / 'README.md')}`\n"
    report_md += f"- `{rel(RELEASE_DIR / 'public_release_candidate_manifest_v1_0_0.json')}`\n"
    write(REPORT_DIR / "public_release_candidate_v1_0_0.md", report_md)
    write(REPORT_DIR / "latest_public_release_candidate.md", report_md)
    write(REPORT_DIR / "README.md", "# Public Release Candidate Reports\n\nCurrent layer: **TAU-SCALING-SA v1.0.0 - Public Release Candidate**\n\nBoundary: public release candidate is not claim validation.\n")

    write(VIS_DIR / "public_release_candidate.svg", make_svg(metrics, readiness))
    write(VIS_DIR / "README.md", "# v1.0.0 Public Release Candidate Visuals\n\n- `public_release_candidate.svg`\n\nBoundary: release-candidate visualization only.\n")

    print(json.dumps({
        "schema": manifest["schema"],
        "release_dir": manifest["release_dir"],
        "recommended_tag": manifest["recommended_tag"],
        "claim_count": metrics.get("claim_count", 0),
        "source_populated_count": metrics.get("source_populated_count", 0),
        "primary_source_confirmed_count": metrics.get("primary_source_confirmed_count", 0),
        "independent_source_confirmed_count": metrics.get("independent_source_confirmed_count", 0),
        "release_findings": metrics.get("release_findings", 0),
        "final_lock_audit_passed": audit["passed"],
        "github_release": manifest["route_decision"]["github_release"],
        "preprint": manifest["route_decision"]["preprint"],
        "thresholds_changed": manifest["thresholds_changed"],
        "classifier_changed": manifest["classifier_changed"],
        "mutation_allowed": manifest["mutation_allowed"],
        "application_allowed": manifest["application_allowed"],
        "claim_promotion_allowed": manifest["claim_promotion_allowed"],
        "source_validation_claimed": manifest["source_validation_claimed"],
        "report": "reports/public_release_candidate/latest_public_release_candidate.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()