from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
EXPLAIN_PATH = REPO_ROOT / "reports" / "explanations" / "latest_threshold_explanation_cards.json"
INTERACTION_PATH = REPO_ROOT / "reports" / "interactions" / "latest_gate_interaction_matrix.json"
OUT_DIR = REPO_ROOT / "reports" / "policy"
VIS_DIR = REPO_ROOT / "visuals" / "policy" / "v0_4_4"

GATE_ORDER = [
    "B_source",
    "B_metric",
    "B_baseline",
    "B_method",
    "B_workload",
    "B_tau",
    "B_LF",
    "B_ETP",
    "B_PVT",
    "B_yield",
    "B_evidence",
]

SEVERITY_SCORE = {
    "TSEK-C_RETAIN": 1,
    "TSEK-D_CANDIDATE": 2,
    "TSEK-E_CANDIDATE": 3,
    "HUMAN_REVIEW": 4,
}

def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}

def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def pair_policy(gate_a: str, gate_b: str, result: dict[str, Any]) -> dict[str, Any]:
    pair = {gate_a, gate_b}
    classification = result.get("classification")
    findings = result.get("finding_codes", [])

    if "B_source" in pair and ("B_evidence" in pair or "B_baseline" in pair or "B_metric" in pair):
        return {
            "policy_class": "HUMAN_REVIEW",
            "recommended_action": "Require human review before promotion because source boundary is paired with metric/baseline/evidence failure.",
            "reason": "Source-boundary failures affect interpretability of the entire claim.",
        }

    if "B_evidence" in pair and ("B_yield" in pair or "B_PVT" in pair or "B_method" in pair):
        return {
            "policy_class": "TSEK-D_CANDIDATE",
            "recommended_action": "Candidate downgrade below TSEK-C unless evidence package, yield/method, and closure disclosures are repaired.",
            "reason": "Evidence plus physical-disclosure failure weakens auditability beyond ordinary single-gate downgrade.",
        }

    if "B_LF" in pair and "B_ETP" in pair:
        return {
            "policy_class": "TSEK-D_CANDIDATE",
            "recommended_action": "Candidate downgrade below TSEK-C because survivability and energy/thermal/PDN gain fail together.",
            "reason": "LogicFolding viability and normalized tau gain are both central to the runtime claim path.",
        }

    if "B_tau" in pair and ("B_workload" in pair or "B_baseline" in pair):
        return {
            "policy_class": "TSEK-D_CANDIDATE",
            "recommended_action": "Candidate downgrade below TSEK-C until tau vector, workload, and baseline are simultaneously repaired.",
            "reason": "Tau improvements are not interpretable without workload and baseline context.",
        }

    if classification == "TSEK-C" and len(findings) >= 2:
        return {
            "policy_class": "TSEK-C_RETAIN",
            "recommended_action": "Retain TSEK-C under current policy, but keep pair visible in explanation cards.",
            "reason": "Paired failure is controlled and interpretable; no overclaim or hard rejection condition detected.",
        }

    return {
        "policy_class": "TSEK-C_RETAIN",
        "recommended_action": "Retain current classifier behavior.",
        "reason": "No policy escalation rule matched.",
    }

def interaction_records() -> list[dict[str, Any]]:
    payload = read_json(INTERACTION_PATH)
    return payload.get("results", [])

def build_policy_rows() -> list[dict[str, Any]]:
    rows = []
    for result in interaction_records():
        gate_a = result.get("gate_a")
        gate_b = result.get("gate_b")
        policy = pair_policy(gate_a, gate_b, result)
        rows.append({
            "gate_a": gate_a,
            "gate_b": gate_b,
            "current_classification": result.get("classification"),
            "current_A_TSEK": result.get("A_TSEK"),
            "current_diagnostic_average": result.get("diagnostic_average"),
            "findings_count": result.get("findings_count"),
            "finding_codes": result.get("finding_codes", []),
            "policy_class": policy["policy_class"],
            "recommended_action": policy["recommended_action"],
            "reason": policy["reason"],
            "policy_enforced": False,
            "non_claim_lock": "Pair policy review is classifier governance only; it does not validate silicon or product claims.",
        })
    return rows

def generate_charts(rows: list[dict[str, Any]]) -> list[str]:
    chart_paths: list[str] = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        write_text(OUT_DIR / "chart_generation_skipped.txt", f"matplotlib unavailable: {exc}\n")
        return chart_paths

    VIS_DIR.mkdir(parents=True, exist_ok=True)

    def savefig(path: Path) -> None:
        plt.tight_layout()
        plt.savefig(path, dpi=180, bbox_inches="tight")
        plt.close()
        chart_paths.append(str(path.relative_to(REPO_ROOT)).replace("\\", "/"))

    # Policy class counts.
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["policy_class"]] = counts.get(row["policy_class"], 0) + 1
    plt.figure(figsize=(8, 4))
    plt.bar(list(counts.keys()), list(counts.values()))
    plt.title("Pair Policy Review Classes")
    plt.ylabel("Pair count")
    plt.xticks(rotation=25, ha="right")
    savefig(VIS_DIR / "pair_policy_class_counts.png")

    # Matrix.
    idx = {g: i for i, g in enumerate(GATE_ORDER)}
    matrix = [[0 for _ in GATE_ORDER] for _ in GATE_ORDER]
    for row in rows:
        i = idx[row["gate_a"]]
        j = idx[row["gate_b"]]
        score = SEVERITY_SCORE[row["policy_class"]]
        matrix[i][j] = score
        matrix[j][i] = score
    plt.figure(figsize=(9, 8))
    img = plt.imshow(matrix, aspect="auto", vmin=0, vmax=4)
    plt.title("Pair Policy Severity Matrix")
    plt.xticks(range(len(GATE_ORDER)), GATE_ORDER, rotation=45, ha="right")
    plt.yticks(range(len(GATE_ORDER)), GATE_ORDER)
    plt.colorbar(img, label="policy severity")
    savefig(VIS_DIR / "pair_policy_severity_matrix.png")

    # Candidate escalation by gate.
    gate_counts = {g: 0 for g in GATE_ORDER}
    for row in rows:
        if row["policy_class"] != "TSEK-C_RETAIN":
            gate_counts[row["gate_a"]] += 1
            gate_counts[row["gate_b"]] += 1
    plt.figure(figsize=(9, 4))
    plt.bar(list(gate_counts.keys()), list(gate_counts.values()))
    plt.title("Escalation Candidate Frequency by Gate")
    plt.ylabel("Escalation candidate count")
    plt.xticks(rotation=45, ha="right")
    savefig(VIS_DIR / "escalation_candidate_frequency_by_gate.png")

    return chart_paths

def summarize(rows: list[dict[str, Any]], charts: list[str]) -> dict[str, Any]:
    policy_counts: dict[str, int] = {}
    gate_escalation_counts = {g: 0 for g in GATE_ORDER}
    for row in rows:
        policy_counts[row["policy_class"]] = policy_counts.get(row["policy_class"], 0) + 1
        if row["policy_class"] != "TSEK-C_RETAIN":
            gate_escalation_counts[row["gate_a"]] += 1
            gate_escalation_counts[row["gate_b"]] += 1

    review = read_json(EXPLAIN_PATH)
    return {
        "schema": "tau-scaling-pair-policy-review-gate-v0.4.4",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pair_count": len(rows),
        "policy_counts": policy_counts,
        "gate_escalation_counts": gate_escalation_counts,
        "policy_rows": rows,
        "chart_paths": charts,
        "inputs": {
            "explanation_card_count": review.get("card_count"),
            "review_counts": review.get("review_counts"),
            "interaction_matrix": str(INTERACTION_PATH.relative_to(REPO_ROOT)).replace("\\", "/"),
            "explanation_cards": str(EXPLAIN_PATH.relative_to(REPO_ROOT)).replace("\\", "/"),
        },
        "policy_enforced": False,
        "next_recommendation": "v0.4.5 should add a dry-run policy simulator before changing classifier output.",
        "boundary": "Pair policy review proposes classifier-governance candidates only. It does not change classifier behavior and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }

def render_md(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.4.4 Pair Policy Review Gate",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Pair count: `{summary['pair_count']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        f"- Chart count: `{len(summary['chart_paths'])}`",
        "",
        "## Policy Counts",
        "",
        "| Policy class | Count | Meaning |",
        "|---|---:|---|",
    ]
    meanings = {
        "TSEK-C_RETAIN": "Keep current controlled downgrade policy.",
        "TSEK-D_CANDIDATE": "Candidate for lower class in future policy simulator.",
        "TSEK-E_CANDIDATE": "Candidate hard rejection; none should be enforced without dry-run evidence.",
        "HUMAN_REVIEW": "Require explicit human review before promotion.",
    }
    for k, v in sorted(summary["policy_counts"].items()):
        lines.append(f"| `{k}` | {v} | {meanings.get(k, '')} |")

    lines += [
        "",
        "## Gate Escalation Candidate Frequency",
        "",
        "| Gate | Candidate count |",
        "|---|---:|",
    ]
    for gate, count in sorted(summary["gate_escalation_counts"].items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| `{gate}` | {count} |")

    lines += [
        "",
        "## Policy Rows",
        "",
        "| Gate A | Gate B | Current class | Policy class | Action | Reason |",
        "|---|---|---|---|---|---|",
    ]
    for row in summary["policy_rows"]:
        action = row["recommended_action"].replace("|", "\\|")
        reason = row["reason"].replace("|", "\\|")
        lines.append(f"| `{row['gate_a']}` | `{row['gate_b']}` | `{row['current_classification']}` | `{row['policy_class']}` | {action} | {reason} |")

    lines += ["", "## Charts", ""]
    for chart in summary["chart_paths"]:
        rel = os.path.relpath(REPO_ROOT / chart, OUT_DIR).replace("\\", "/")
        lines += [f"![{Path(chart).stem}]({rel})", ""]

    lines += [
        "## Boundary",
        "",
        summary["boundary"],
        "",
    ]
    return "\n".join(lines)

def main() -> None:
    rows = build_policy_rows()
    charts = generate_charts(rows)
    summary = summarize(rows, charts)
    write_json(OUT_DIR / "pair_policy_review_v0_4_4.json", summary)
    write_json(OUT_DIR / "latest_pair_policy_review.json", summary)
    md = render_md(summary)
    write_text(OUT_DIR / "pair_policy_review_v0_4_4.md", md)
    write_text(OUT_DIR / "latest_pair_policy_review.md", md)

    print(json.dumps({
        "schema": summary["schema"],
        "pair_count": summary["pair_count"],
        "policy_counts": summary["policy_counts"],
        "chart_count": len(summary["chart_paths"]),
        "policy_enforced": summary["policy_enforced"],
        "report": "reports/policy/latest_pair_policy_review.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
