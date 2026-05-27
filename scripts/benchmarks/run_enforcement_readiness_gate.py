
from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
REGRESSION_PATH = REPO_ROOT / "reports" / "regression_review" / "latest_regression_over_penalty_review.json"
OUT_DIR = REPO_ROOT / "reports" / "enforcement_readiness"
VIS_DIR = REPO_ROOT / "visuals" / "enforcement_readiness" / "v0_5_0"

THRESHOLDS = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def threshold_flags(row: dict[str, Any], threshold: float) -> dict[str, Any]:
    diag = row.get("current_diagnostic_average")
    findings_count = int(row.get("findings_count", 0) or 0)
    severity = int(row.get("drift_severity", 0) or 0)

    high_support = isinstance(diag, (int, float)) and diag >= threshold
    missing_findings = findings_count == 0
    high_severity = severity >= 2

    reasons = []
    if high_support:
        reasons.append("high_diagnostic_support")
    if missing_findings:
        reasons.append("missing_finding_provenance")
    if high_severity:
        reasons.append("high_drift_severity")

    return {
        "threshold": threshold,
        "high_support_flag": high_support,
        "missing_findings_flag": missing_findings,
        "high_severity_flag": high_severity,
        "active_reasons": reasons,
        "over_penalty_flag": bool(reasons),
    }

def readiness_row(row: dict[str, Any]) -> dict[str, Any]:
    candidate = row.get("decision") == "APPROVE_FOR_REGRESSION_REVIEW"
    human_review = row.get("decision") == "DEFER_TO_HUMAN_REVIEW"
    baseline = threshold_flags(row, 0.75)

    if human_review:
        status = "HUMAN_REVIEW_ONLY"
        action = "Preserve human-review routing. Do not convert to automatic downgrade."
    elif candidate and baseline["over_penalty_flag"]:
        status = "BLOCKED_BY_OVER_PENALTY"
        action = "Do not enforce. Candidate must be calibrated or narrowed before any enforcement design."
    elif candidate:
        status = "ELIGIBLE_FOR_CANDIDATE_DESIGN"
        action = "Eligible for disabled enforcement-candidate design only."
    else:
        status = "RETAIN_CURRENT_BEHAVIOR"
        action = "No enforcement path."

    return {
        "gate_pair": row.get("gate_pair"),
        "gate_a": row.get("gate_a"),
        "gate_b": row.get("gate_b"),
        "decision": row.get("decision"),
        "current_classification": row.get("current_classification"),
        "simulated_policy_classification": row.get("simulated_policy_classification"),
        "current_diagnostic_average": row.get("current_diagnostic_average"),
        "findings_count": row.get("findings_count"),
        "drift_severity": row.get("drift_severity"),
        "baseline_over_penalty_reasons": baseline["active_reasons"],
        "readiness_status": status,
        "recommended_action": action,
        "mutation_allowed": False,
        "policy_enforced": False,
    }

def calibration_sweep(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    candidates = [r for r in rows if r.get("decision") == "APPROVE_FOR_REGRESSION_REVIEW"]
    sweep = []
    for threshold in THRESHOLDS:
        flags = [threshold_flags(r, threshold) for r in candidates]
        over_count = sum(1 for f in flags if f["over_penalty_flag"])
        pass_count = len(candidates) - over_count
        sweep.append({
            "threshold": threshold,
            "candidate_count": len(candidates),
            "over_penalty_count": over_count,
            "pass_count": pass_count,
            "high_support_count": sum(1 for f in flags if f["high_support_flag"]),
            "missing_findings_count": sum(1 for f in flags if f["missing_findings_flag"]),
            "high_severity_count": sum(1 for f in flags if f["high_severity_flag"]),
        })
    return sweep

def generate_charts(summary: dict[str, Any]) -> list[str]:
    paths = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        write_text(OUT_DIR / "chart_generation_skipped.txt", f"matplotlib unavailable: {exc}\n")
        return paths

    VIS_DIR.mkdir(parents=True, exist_ok=True)

    def save(path: Path) -> None:
        plt.tight_layout()
        plt.savefig(path, dpi=180, bbox_inches="tight")
        plt.close()
        paths.append(str(path.relative_to(REPO_ROOT)).replace("\\", "/"))

    readiness_counts = summary["readiness_status_counts"]
    plt.figure(figsize=(9, 4))
    plt.bar(list(readiness_counts.keys()), list(readiness_counts.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Case count")
    plt.title("v0.5.0 Enforcement Readiness Status")
    save(VIS_DIR / "enforcement_readiness_status_counts.png")

    sweep = summary["calibration_sweep"]
    x = [r["threshold"] for r in sweep]
    over = [r["over_penalty_count"] for r in sweep]
    passed = [r["pass_count"] for r in sweep]
    plt.figure(figsize=(8, 4))
    plt.plot(x, over, marker="o", label="over-penalty count")
    plt.plot(x, passed, marker="o", label="pass count")
    plt.xlabel("Diagnostic support threshold")
    plt.ylabel("Candidate count")
    plt.title("v0.5.0 Calibration Sweep")
    plt.legend()
    save(VIS_DIR / "enforcement_readiness_calibration_sweep.png")

    gate_counts = summary["blocked_gate_counts"]
    plt.figure(figsize=(9, 4))
    plt.bar(list(gate_counts.keys()), list(gate_counts.values()))
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Blocked candidate involvement")
    plt.title("Blocked Candidate Involvement by Gate")
    save(VIS_DIR / "blocked_candidate_gate_counts.png")

    return paths

def render_md(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.5.0 Enforcement Readiness Gate",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Input review rows: `{summary['input_review_rows']}`",
        f"- Controlled downgrade candidates: `{summary['controlled_downgrade_candidate_count']}`",
        f"- Blocked by over-penalty: `{summary['blocked_by_over_penalty_count']}`",
        f"- Human review only: `{summary['human_review_only_count']}`",
        f"- Eligible for disabled candidate design: `{summary['eligible_candidate_design_count']}`",
        f"- Enforcement candidate enabled: `{summary['enforcement_candidate_enabled']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        f"- Final recommendation: `{summary['final_recommendation']}`",
        "",
        "## Readiness Status Counts",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for k, v in summary["readiness_status_counts"].items():
        lines.append(f"| `{k}` | {v} |")

    lines += [
        "",
        "## Readiness Rows",
        "",
        "| Gate pair | Decision | Status | Reasons | Action |",
        "|---|---|---|---|---|",
    ]
    for row in summary["readiness_rows"]:
        reasons = ", ".join(row["baseline_over_penalty_reasons"]) or "none"
        action = row["recommended_action"].replace("|", "\\|")
        lines.append(f"| `{row['gate_pair']}` | `{row['decision']}` | `{row['readiness_status']}` | `{reasons}` | {action} |")

    lines += [
        "",
        "## Calibration Sweep",
        "",
        "| Threshold | Over-penalty | Pass count | High support | Missing findings | High severity |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary["calibration_sweep"]:
        lines.append(
            f"| {row['threshold']:.2f} | {row['over_penalty_count']} | {row['pass_count']} | "
            f"{row['high_support_count']} | {row['missing_findings_count']} | {row['high_severity_count']} |"
        )

    lines += ["", "## Charts", ""]
    for chart in summary["chart_paths"]:
        rel = os.path.relpath(REPO_ROOT / chart, OUT_DIR).replace("\\", "/")
        lines += [f"![{Path(chart).stem}]({rel})", ""]

    lines += [
        "## v0.5.0 Lock",
        "",
        "v0.5.0 is a major governance checkpoint, not classifier activation.",
        "",
        "```text",
        "enforcement_candidate_enabled: false",
        "mutation_allowed: false",
        "policy_enforced: false",
        "```",
        "",
        "## Boundary",
        "",
        summary["boundary"],
        "",
    ]
    return "\n".join(lines)

def main() -> None:
    regression = read_json(REGRESSION_PATH)
    review_rows = regression.get("review_rows", [])
    rows = [readiness_row(row) for row in review_rows]
    status_counts = Counter(row["readiness_status"] for row in rows)
    controlled = [r for r in rows if r["decision"] == "APPROVE_FOR_REGRESSION_REVIEW"]
    blocked = [r for r in rows if r["readiness_status"] == "BLOCKED_BY_OVER_PENALTY"]

    gate_counts = Counter()
    for row in blocked:
        gate_counts[row["gate_a"]] += 1
        gate_counts[row["gate_b"]] += 1

    eligible = status_counts.get("ELIGIBLE_FOR_CANDIDATE_DESIGN", 0)
    final = (
        "do_not_design_enforcement_candidate__all_controlled_downgrades_blocked"
        if eligible == 0 and len(controlled) > 0
        else "disabled_enforcement_candidate_design_allowed_after_manual_review"
        if eligible > 0
        else "no_enforcement_candidate_path"
    )

    summary = {
        "schema": "tau-scaling-enforcement-readiness-gate-v0.5.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input": "reports/regression_review/latest_regression_over_penalty_review.json",
        "input_review_rows": len(review_rows),
        "controlled_downgrade_candidate_count": len(controlled),
        "blocked_by_over_penalty_count": len(blocked),
        "human_review_only_count": status_counts.get("HUMAN_REVIEW_ONLY", 0),
        "eligible_candidate_design_count": eligible,
        "readiness_status_counts": dict(status_counts),
        "blocked_gate_counts": dict(gate_counts),
        "calibration_sweep": calibration_sweep(review_rows),
        "readiness_rows": rows,
        "enforcement_candidate_enabled": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "final_recommendation": final,
        "boundary": "Enforcement readiness is local classifier-governance analysis only. It does not change classifier behavior and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.5.1 should repair the Nexus feedback target so completed v0.4.x surfaces are recognized and stale recommendations are retired.",
    }
    summary["chart_paths"] = generate_charts(summary)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(OUT_DIR / "enforcement_readiness_gate_v0_5_0.json", summary)
    write_json(OUT_DIR / "latest_enforcement_readiness_gate.json", summary)
    write_text(OUT_DIR / "enforcement_readiness_gate_v0_5_0.md", render_md(summary))
    write_text(OUT_DIR / "latest_enforcement_readiness_gate.md", render_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "input_review_rows": summary["input_review_rows"],
        "controlled_downgrade_candidate_count": summary["controlled_downgrade_candidate_count"],
        "blocked_by_over_penalty_count": summary["blocked_by_over_penalty_count"],
        "human_review_only_count": summary["human_review_only_count"],
        "eligible_candidate_design_count": summary["eligible_candidate_design_count"],
        "enforcement_candidate_enabled": summary["enforcement_candidate_enabled"],
        "mutation_allowed": summary["mutation_allowed"],
        "policy_enforced": summary["policy_enforced"],
        "final_recommendation": summary["final_recommendation"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/enforcement_readiness/latest_enforcement_readiness_gate.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
