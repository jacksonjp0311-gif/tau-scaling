
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "tsek_boundary_cards"
VIS = ROOT / "visuals" / "tsek_boundary_cards" / "v0_7_5"

THRESHOLD_REVIEW = ROOT / "reports" / "tsek_threshold_review" / "latest_tsek_threshold_boundary_review.json"
GATE_ALGEBRA = ROOT / "reports" / "gate_algebra" / "latest_gate_algebra_map.json"
TAU_VECTOR = ROOT / "reports" / "tau_vector_semantics" / "latest_tau_vector_semantics_ledger.json"
RELEASE = ROOT / "reports" / "release" / "latest_release_readiness.json"

CLASSES = [
    {
        "class": "TSEK-A",
        "role": "reserved_strong_claim_class",
        "boundary_question": "What would be required for a strong Tau claim beyond local runtime evidence?",
        "default_action": "keep_unassigned_without_external_evidence",
        "risk": "overclaim_risk",
    },
    {
        "class": "TSEK-B",
        "role": "stronger_local_evidence_class",
        "boundary_question": "Does the claim show coherent local evidence while preserving non-claim locks?",
        "default_action": "allow_local_strong_evidence_label_only",
        "risk": "promotion_without_scope_boundary",
    },
    {
        "class": "TSEK-C",
        "role": "bounded_baseline_or_partial_evidence_class",
        "boundary_question": "Does the claim have enough structure for local analysis but insufficient evidence for stronger promotion?",
        "default_action": "preserve_controlled_downgrade",
        "risk": "under_explained_partial_evidence",
    },
    {
        "class": "TSEK-D",
        "role": "weak_or_high_uncertainty_class",
        "boundary_question": "Is the claim structurally present but too weak, sparse, or unstable for C/B?",
        "default_action": "explain_weakness_without_rejection",
        "risk": "missing_intermediate_downgrade_path",
    },
    {
        "class": "TSEK-E",
        "role": "rejected_or_severe_failure_class",
        "boundary_question": "Does the claim fail hard gates, evidence sufficiency, or non-claim discipline?",
        "default_action": "reject_or_block_promotion",
        "risk": "over_penalty_if_high_support_claim_is_rejected",
    },
]

def read_json(path: Path):
    if not path.exists():
        return {"missing": True, "path": str(path)}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"parse_error": str(exc), "path": str(path)}

def wjson(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def wtext(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def rel(path: Path):
    return str(path.relative_to(ROOT)).replace("\\", "/")

def make_cards(threshold, gate, tau):
    review_counts = threshold.get("report_tsek_class_counts", {}) or {}
    core_counts = threshold.get("core_tsek_class_counts", {}) or {}
    gate_gap_count = gate.get("gap_count", 0)
    tau_gap_count = tau.get("gap_count", 0)

    cards = []
    for item in CLASSES:
        cls = item["class"]
        observed_report_mentions = int(review_counts.get(cls, 0))
        observed_core_mentions = int(core_counts.get(cls, 0))
        needs_attention = (
            observed_report_mentions == 0
            or observed_core_mentions == 0
            or (cls == "TSEK-D" and observed_report_mentions == 0)
            or (cls == "TSEK-A" and observed_report_mentions == 0)
        )
        cards.append({
            "schema": "tau-scaling-tsek-boundary-explanation-card-v0.7.5",
            "class": cls,
            "role": item["role"],
            "boundary_question": item["boundary_question"],
            "default_action": item["default_action"],
            "risk": item["risk"],
            "observed_report_mentions": observed_report_mentions,
            "observed_core_mentions": observed_core_mentions,
            "gate_gap_count_context": gate_gap_count,
            "tau_gap_count_context": tau_gap_count,
            "needs_attention": bool(needs_attention),
            "threshold_change_allowed": False,
            "classifier_change_allowed": False,
            "mutation_allowed": False,
            "evidence_note": "This card explains a class boundary using local repo evidence only. It does not validate silicon, product performance, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        })
    return cards

def charts(summary):
    paths = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        wtext(OUT / "chart_generation_skipped.txt", str(exc))
        return paths

    VIS.mkdir(parents=True, exist_ok=True)

    def save(name):
        p = VIS / name
        plt.tight_layout()
        plt.savefig(p, dpi=180, bbox_inches="tight")
        plt.close()
        paths.append(rel(p))

    cards = summary["cards"]
    labels = [c["class"] for c in cards]

    plt.figure(figsize=(8, 4))
    plt.bar(labels, [c["observed_report_mentions"] for c in cards])
    plt.ylabel("Report mentions")
    plt.title("TSEK Boundary Card Report Visibility")
    save("tsek_boundary_report_visibility.png")

    plt.figure(figsize=(8, 4))
    plt.bar(labels, [int(c["needs_attention"]) for c in cards])
    plt.ylabel("Needs attention")
    plt.title("TSEK Boundary Attention Flags")
    save("tsek_boundary_attention_flags.png")

    health = {
        "release_passed": int(summary["release_passed"]),
        "threshold_ready": int(summary["threshold_ready"]),
        "attention_cards": summary["attention_card_count"],
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(health.keys()), list(health.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Value")
    plt.title("TSEK Boundary Cards Health")
    save("tsek_boundary_cards_health.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.7.5 TSEK Boundary Explanation Cards",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Card Result",
        "",
        f"- Card status: `{summary['card_status']}`",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Threshold review ready: `{summary['threshold_ready']}`",
        f"- Card count: `{summary['card_count']}`",
        f"- Attention cards: `{summary['attention_card_count']}`",
        f"- Thresholds changed: `{summary['thresholds_changed']}`",
        f"- Classifier changed: `{summary['classifier_changed']}`",
        "",
        "## Boundary Cards",
        "",
        "| Class | Role | Report mentions | Core mentions | Needs attention | Default action |",
        "|---|---|---:|---:|---:|---|",
    ]
    for c in summary["cards"]:
        lines.append(f"| `{c['class']}` | `{c['role']}` | {c['observed_report_mentions']} | {c['observed_core_mentions']} | `{c['needs_attention']}` | `{c['default_action']}` |")

    lines += [
        "",
        "## Interpretation",
        "",
        "These cards explain class boundaries. They do not tune thresholds, alter downgrade policy, or mutate the classifier.",
        "",
        "## Next Tau Work",
        "",
        "1. Build over/under-penalty negative controls for the class boundaries flagged here.",
        "2. Ensure TSEK-D and TSEK-A absence/presence is intentional rather than accidental.",
        "3. Separate evidence sufficiency from hard-gate collapse in explanation language.",
        "4. Keep thresholds unchanged until dry-run sensitivity evidence exists.",
        "",
        "## Charts",
        "",
    ]
    for p in summary["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")
    lines += ["## Boundary", "", summary["boundary"], ""]
    return "\n".join(lines)

def main():
    threshold = read_json(THRESHOLD_REVIEW)
    gate = read_json(GATE_ALGEBRA)
    tau = read_json(TAU_VECTOR)
    release = read_json(RELEASE)

    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0
    threshold_ready = threshold.get("threshold_review_status") == "TSEK_THRESHOLD_BOUNDARY_REVIEW_READY__NO_THRESHOLD_CHANGE"

    cards = make_cards(threshold, gate, tau)
    for card in cards:
        wjson(OUT / "cards" / f"{card['class'].lower().replace('-', '_')}_boundary_card_v0_7_5.json", card)

    attention_count = sum(1 for c in cards if c["needs_attention"])
    card_status = "TSEK_BOUNDARY_CARDS_READY__NO_THRESHOLD_CHANGE" if release_passed and threshold_ready else "TSEK_BOUNDARY_CARDS_NEED_REVIEW"

    summary = {
        "schema": "tau-scaling-tsek-boundary-explanation-cards-v0.7.5",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "card_status": card_status,
        "release_passed": bool(release_passed),
        "threshold_ready": bool(threshold_ready),
        "card_count": len(cards),
        "attention_card_count": attention_count,
        "cards": cards,
        "replay_allowed": False,
        "executor_ran": False,
        "branch_created": False,
        "branch_creation_allowed": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "thresholds_changed": False,
        "classifier_changed": False,
        "next_recommendation": "Move to v0.7.6 Over/Under-Penalty Negative Controls before any threshold dry-run or tuning.",
        "boundary": "TSEK boundary explanation cards are local classifier-governance analysis artifacts. They explain class-boundary semantics without changing classifier behavior. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "tsek_boundary_explanation_cards_v0_7_5.json", summary)
    wjson(OUT / "latest_tsek_boundary_explanation_cards.json", summary)
    wtext(OUT / "tsek_boundary_explanation_cards_v0_7_5.md", make_md(summary))
    wtext(OUT / "latest_tsek_boundary_explanation_cards.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "card_status": summary["card_status"],
        "release_passed": summary["release_passed"],
        "threshold_ready": summary["threshold_ready"],
        "card_count": summary["card_count"],
        "attention_card_count": summary["attention_card_count"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
