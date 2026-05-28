from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]

SUBMISSION_JSON = ROOT / "reports" / "manuscript_submission_package" / "latest_manuscript_submission_package.json"
EVIDENCE_JSON = ROOT / "reports" / "manuscript_evidence_pack" / "latest_manuscript_evidence_pack.json"
GAP_JSON = ROOT / "reports" / "primary_source_gap_review" / "latest_primary_source_gap_review.json"
RELEASE_JSON = ROOT / "reports" / "release" / "latest_release_readiness.json"

REPORT_DIR = ROOT / "reports" / "external_review_publication_routing"
REVIEW_DIR = ROOT / "docs" / "review"
ROUTING_DIR = ROOT / "releases" / "publication_routing_v0_9_4"
VIS_DIR = ROOT / "visuals" / "external_review_publication_routing" / "v0_9_4"

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

def review_checklist() -> list[dict]:
    return [
        {
            "id": "R1",
            "check": "Does the manuscript clearly state that Tau Scaling is not validated by this artifact?",
            "required_response": "Yes; non-claim lock must remain visible in abstract, limitations, and conclusion.",
            "blocking": True,
        },
        {
            "id": "R2",
            "check": "Does every source-populated claim remain separated from primary-source confirmation?",
            "required_response": "Yes; source-populated is not source-validated.",
            "blocking": True,
        },
        {
            "id": "R3",
            "check": "Does the artifact distinguish public secondary reporting from first-party evidence?",
            "required_response": "Yes; public reports must not be promoted to primary validation.",
            "blocking": True,
        },
        {
            "id": "R4",
            "check": "Are claim ledger, source ledger, evidence table, gap matrix, and release checks reproducible?",
            "required_response": "Yes; commands and paths must be listed.",
            "blocking": True,
        },
        {
            "id": "R5",
            "check": "Does the paper avoid semiconductor performance, product, investment, or process-node claims?",
            "required_response": "Yes; scope remains evidence-governance.",
            "blocking": True,
        },
        {
            "id": "R6",
            "check": "Are limitations explicit enough for an external reviewer to reject overclaiming?",
            "required_response": "Yes; limitations table and ethics/non-claim statement must be present.",
            "blocking": True,
        },
        {
            "id": "R7",
            "check": "Is the publication route appropriate for a repository-based artifact?",
            "required_response": "Technical note or GitHub release first; preprint only after external review.",
            "blocking": False,
        },
    ]

def reviewer_questions() -> list[dict]:
    return [
        {
            "question": "Is the contribution framed as evidence governance rather than semiconductor validation?",
            "why_it_matters": "This is the central boundary condition.",
        },
        {
            "question": "Are the source categories and validation gaps legible to a reader outside the project?",
            "why_it_matters": "Publication value depends on external readability.",
        },
        {
            "question": "Does the evidence table make it impossible to confuse source-populated with source-validated?",
            "why_it_matters": "This prevents accidental overclaiming.",
        },
        {
            "question": "Are the non-claim locks too conservative, too weak, or correctly calibrated?",
            "why_it_matters": "Over-restraint can obscure the contribution; under-restraint creates false validation.",
        },
        {
            "question": "Which route is most appropriate: GitHub release, technical note, Gist, or preprint?",
            "why_it_matters": "Publication channel should match evidence maturity.",
        },
    ]

def publication_routes(metrics: dict) -> list[dict]:
    no_primary = metrics.get("primary_source_confirmed_count", 0) == 0
    no_independent = metrics.get("independent_source_confirmed_count", 0) == 0
    release_clean = metrics.get("release_findings", 1) == 0
    source_populated = metrics.get("source_populated_count", 0) >= metrics.get("claim_count", 999)

    return [
        {
            "route": "GitHub Release",
            "status": "READY",
            "reason": "Repository artifacts, release checks, manifests, reports, and non-claim locks are present.",
            "required_before_publish": ["tag release", "attach release notes", "link manuscript package"],
        },
        {
            "route": "Technical Note",
            "status": "READY_WITH_BOUNDARY",
            "reason": "Evidence-governance result is bounded and reproducible; should avoid validation claims.",
            "required_before_publish": ["shorten abstract", "include table and limitation summary", "state non-claim lock early"],
        },
        {
            "route": "Gist Summary",
            "status": "READY",
            "reason": "Gist can present the publishable finding and link the repo package.",
            "required_before_publish": ["include repo link", "include result statement", "include limitations"],
        },
        {
            "route": "Preprint Draft",
            "status": "HOLD_FOR_REVIEW",
            "reason": "Preprint should wait for external review because primary and independent confirmations are zero.",
            "required_before_publish": ["external review checklist complete", "reviewer comments addressed", "preprint framing audited"],
        },
        {
            "route": "Claim Promotion / Technical Validation",
            "status": "BLOCKED",
            "reason": "No primary-source confirmation and no independent confirmation in current state.",
            "required_before_publish": ["first-party evidence", "independent reproduction", "workload/baseline/energy/thermal/yield gates"],
        },
    ]

def compute_readiness(metrics: dict, release: dict, checklist: list[dict]) -> dict:
    release_score = 1.0 if metrics.get("release_findings", 1) == 0 and metrics.get("release_passed", False) else 0.0
    source_score = 1.0 if metrics.get("source_populated_count", 0) >= metrics.get("claim_count", 1) else 0.0
    lock_score = 1.0 if metrics.get("claim_promotion_allowed", False) is False and metrics.get("source_validation_claimed", False) is False else 0.0
    primary_penalty = 0.0 if metrics.get("primary_source_confirmed_count", 0) == 0 else 0.0
    review_score = 0.75  # scaffold is present but human review has not occurred yet
    ready_for_github_release = release_score == 1.0 and source_score == 1.0 and lock_score == 1.0
    ready_for_preprint = False

    score = round(mean([release_score, source_score, lock_score, review_score]) - primary_penalty, 4)
    return {
        "submission_readiness_score": score,
        "release_score": release_score,
        "source_score": source_score,
        "lock_score": lock_score,
        "review_score": review_score,
        "ready_for_github_release": ready_for_github_release,
        "ready_for_technical_note": ready_for_github_release,
        "ready_for_gist_summary": ready_for_github_release,
        "ready_for_preprint": ready_for_preprint,
        "preprint_hold_reason": "External review required before preprint because primary and independent confirmations are zero.",
    }

def make_svg(summary: dict) -> str:
    metrics = summary["metrics"]
    readiness = summary["readiness"]
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">',
        '<rect width="1600" height="900" fill="#020617"/>',
        '<text x="800" y="82" text-anchor="middle" fill="#67e8f9" font-size="46" font-family="Segoe UI" font-weight="700">External Review + Publication Routing v0.9.4</text>',
        '<text x="800" y="130" text-anchor="middle" fill="#cbd5e1" font-size="24" font-family="Segoe UI">Route the manuscript without weakening its non-claim boundary</text>',
        f'<text x="180" y="240" fill="#f8fafc" font-size="30" font-family="Segoe UI">Readiness score: {readiness["submission_readiness_score"]}</text>',
        f'<text x="180" y="310" fill="#f8fafc" font-size="30" font-family="Segoe UI">GitHub release ready: {readiness["ready_for_github_release"]}</text>',
        f'<text x="180" y="380" fill="#f8fafc" font-size="30" font-family="Segoe UI">Technical note ready: {readiness["ready_for_technical_note"]}</text>',
        f'<text x="180" y="450" fill="#f8fafc" font-size="30" font-family="Segoe UI">Preprint ready: {readiness["ready_for_preprint"]}</text>',
        f'<text x="180" y="520" fill="#f8fafc" font-size="30" font-family="Segoe UI">Primary confirmed: {metrics.get("primary_source_confirmed_count", 0)}</text>',
        f'<text x="180" y="590" fill="#f8fafc" font-size="30" font-family="Segoe UI">Independent confirmed: {metrics.get("independent_source_confirmed_count", 0)}</text>',
        '<rect x="930" y="245" width="430" height="76" rx="18" fill="#0f172a" stroke="#22c55e"/>',
        '<text x="1145" y="293" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Release / Gist: READY</text>',
        '<rect x="930" y="375" width="430" height="76" rx="18" fill="#0f172a" stroke="#f59e0b"/>',
        '<text x="1145" y="423" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Technical note: BOUNDED</text>',
        '<rect x="930" y="505" width="430" height="76" rx="18" fill="#0f172a" stroke="#ef4444"/>',
        '<text x="1145" y="553" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Preprint: HOLD</text>',
        '<text x="800" y="820" text-anchor="middle" fill="#94a3b8" font-size="22" font-family="Segoe UI">Publication routing is ready; claim validation remains blocked.</text>',
        '</svg>',
    ])

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    ROUTING_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    submission = load_json(SUBMISSION_JSON)
    evidence = load_json(EVIDENCE_JSON)
    gap = load_json(GAP_JSON)
    release = load_json(RELEASE_JSON)

    metrics = dict(submission.get("metrics", {}))
    metrics.setdefault("claim_count", evidence.get("claim_count", 0))
    metrics.setdefault("source_populated_count", evidence.get("source_populated_count", 0))
    metrics.setdefault("primary_source_confirmed_count", evidence.get("primary_source_confirmed_count", 0))
    metrics.setdefault("independent_source_confirmed_count", evidence.get("independent_source_confirmed_count", 0))
    metrics.setdefault("high_gap_claim_count", gap.get("high_gap_claim_count", 0))
    metrics["release_findings"] = len(release.get("findings", [])) if isinstance(release.get("findings", []), list) else int(release.get("findings", 0) or 0)
    metrics["release_passed"] = bool(release.get("passed", False))
    metrics["claim_promotion_allowed"] = False
    metrics["source_validation_claimed"] = False

    checklist = review_checklist()
    questions = reviewer_questions()
    routes = publication_routes(metrics)
    readiness = compute_readiness(metrics, release, checklist)

    summary = {
        "schema": "tau-scaling-external-review-publication-routing-v0.9.4",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "metrics": metrics,
        "readiness": readiness,
        "review_checklist_count": len(checklist),
        "reviewer_question_count": len(questions),
        "publication_route_count": len(routes),
        "routes": routes,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "publication_routing_claims_silicon_validation": False,
        "boundary": "v0.9.4 creates external review and publication routing artifacts. It does not validate sources, promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.",
    }

    checklist_md = "# External Review Checklist v0.9.4\n\n"
    checklist_md += "| ID | Blocking | Check | Required response |\n|---|---:|---|---|\n"
    for item in checklist:
        checklist_md += f"| {item['id']} | {item['blocking']} | {item['check']} | {item['required_response']} |\n"
    checklist_md += "\nBoundary: review checklist completion is not claim validation.\n"

    questions_md = "# Reviewer Questions v0.9.4\n\n"
    for i, item in enumerate(questions, 1):
        questions_md += f"## Q{i}. {item['question']}\n\nWhy it matters: {item['why_it_matters']}\n\n"

    response_md = "# Reviewer Response Template v0.9.4\n\n"
    response_md += "## Reviewer Comment\n\n> Paste reviewer comment here.\n\n"
    response_md += "## Response\n\nExplain the response while preserving non-claim locks.\n\n"
    response_md += "## Artifact Changes\n\n- Files changed:\n- Reports updated:\n- Validation rerun:\n\n"
    response_md += "## Boundary Check\n\n- [ ] Does not promote Tau claims.\n- [ ] Does not imply silicon validation.\n- [ ] Does not treat public reporting as primary validation.\n"

    routing_md = "# Publication Routing v0.9.4\n\n"
    routing_md += "## Route Table\n\n| Route | Status | Reason | Required before publish |\n|---|---|---|---|\n"
    for route in routes:
        routing_md += f"| {route['route']} | {route['status']} | {route['reason']} | {'; '.join(route['required_before_publish'])} |\n"
    routing_md += "\n## Recommendation\n\nPublish first as a GitHub release and/or technical note. Hold preprint submission until external review confirms that the non-claim locks and evidence boundary are clear.\n"

    github_release_md = "# GitHub Release Checklist v0.9.4\n\n"
    github_release_md += "- [ ] Tag release after final review.\n"
    github_release_md += "- [ ] Link `releases/manuscript_submission_package_v0_9_3/README.md`.\n"
    github_release_md += "- [ ] Link `reports/manuscript_submission_package/latest_manuscript_submission_package.md`.\n"
    github_release_md += "- [ ] Include non-claim boundary in release notes.\n"
    github_release_md += "- [ ] State that the artifact is source-provenance / validation-gap analysis only.\n"
    github_release_md += "- [ ] Attach or link figure pack and evidence table.\n"

    gist_summary_md = "# Gist / Technical Note Summary v0.9.4\n\n"
    gist_summary_md += "## Title\n\nTau Scaling as an Evidence-Gated Public Claim System\n\n"
    gist_summary_md += "## One-paragraph summary\n\nThis repository turns public Tau Scaling and LogicFolding claims into an evidence-gated public claim system. Eight public claims are source-populated from public reporting, but zero are primary-source confirmed and zero are independently confirmed in the current repository state. The contribution is a reproducible source-provenance and validation-gap artifact, not silicon validation or claim promotion.\n\n"
    gist_summary_md += "## Link targets\n\n- Manuscript submission package\n- Public research milestone package\n- Evidence table\n- Primary source gap review\n- Release readiness report\n"

    write(REVIEW_DIR / "external_review_checklist_v0_9_4.md", checklist_md)
    write(REVIEW_DIR / "reviewer_questions_v0_9_4.md", questions_md)
    write(REVIEW_DIR / "reviewer_response_template_v0_9_4.md", response_md)
    write(REVIEW_DIR / "publication_routing_v0_9_4.md", routing_md)
    write(REVIEW_DIR / "github_release_checklist_v0_9_4.md", github_release_md)
    write(REVIEW_DIR / "gist_technical_note_summary_v0_9_4.md", gist_summary_md)
    write(REVIEW_DIR / "README.md", "# Review and Publication Routing\n\nCurrent layer: **TAU-SCALING-SA v0.9.4 - External Review Checklist and Publication Routing**\n\nBoundary: review routing is not claim validation.\n")

    for path in [
        REVIEW_DIR / "external_review_checklist_v0_9_4.md",
        REVIEW_DIR / "reviewer_questions_v0_9_4.md",
        REVIEW_DIR / "reviewer_response_template_v0_9_4.md",
        REVIEW_DIR / "publication_routing_v0_9_4.md",
        REVIEW_DIR / "github_release_checklist_v0_9_4.md",
        REVIEW_DIR / "gist_technical_note_summary_v0_9_4.md",
    ]:
        write(ROUTING_DIR / path.name, path.read_text(encoding="utf-8"))

    write_json(ROUTING_DIR / "publication_routing_manifest_v0_9_4.json", summary)

    report_md = "# External Review Checklist and Publication Routing v0.9.4\n\n"
    report_md += "## Readiness\n\n"
    for key, val in readiness.items():
        report_md += f"- {key}: `{val}`\n"
    report_md += "\n## Route Summary\n\n"
    for route in routes:
        report_md += f"- {route['route']}: **{route['status']}** — {route['reason']}\n"
    report_md += "\n## Outputs\n\n"
    report_md += "- `docs/review/external_review_checklist_v0_9_4.md`\n"
    report_md += "- `docs/review/reviewer_questions_v0_9_4.md`\n"
    report_md += "- `docs/review/reviewer_response_template_v0_9_4.md`\n"
    report_md += "- `docs/review/publication_routing_v0_9_4.md`\n"
    report_md += "- `docs/review/github_release_checklist_v0_9_4.md`\n"
    report_md += "- `docs/review/gist_technical_note_summary_v0_9_4.md`\n"
    report_md += f"- `{rel(ROUTING_DIR)}`\n"
    report_md += "\n## Boundary\n\n" + summary["boundary"] + "\n"

    write_json(REPORT_DIR / "external_review_publication_routing_v0_9_4.json", summary)
    write_json(REPORT_DIR / "latest_external_review_publication_routing.json", summary)
    write(REPORT_DIR / "external_review_publication_routing_v0_9_4.md", report_md)
    write(REPORT_DIR / "latest_external_review_publication_routing.md", report_md)
    write(REPORT_DIR / "README.md", "# External Review and Publication Routing Reports\n\nCurrent layer: **TAU-SCALING-SA v0.9.4 - External Review Checklist and Publication Routing**\n\nBoundary: publication routing is not claim validation.\n")

    write(VIS_DIR / "external_review_publication_routing.svg", make_svg(summary))
    write(VIS_DIR / "README.md", "# v0.9.4 External Review and Publication Routing Visuals\n\n- `external_review_publication_routing.svg`\n\nBoundary: route visualization only.\n")

    print(json.dumps({
        "schema": summary["schema"],
        "submission_readiness_score": readiness["submission_readiness_score"],
        "ready_for_github_release": readiness["ready_for_github_release"],
        "ready_for_technical_note": readiness["ready_for_technical_note"],
        "ready_for_gist_summary": readiness["ready_for_gist_summary"],
        "ready_for_preprint": readiness["ready_for_preprint"],
        "claim_count": metrics.get("claim_count", 0),
        "source_populated_count": metrics.get("source_populated_count", 0),
        "primary_source_confirmed_count": metrics.get("primary_source_confirmed_count", 0),
        "independent_source_confirmed_count": metrics.get("independent_source_confirmed_count", 0),
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "claim_promotion_allowed": summary["claim_promotion_allowed"],
        "source_validation_claimed": summary["source_validation_claimed"],
        "report": "reports/external_review_publication_routing/latest_external_review_publication_routing.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()