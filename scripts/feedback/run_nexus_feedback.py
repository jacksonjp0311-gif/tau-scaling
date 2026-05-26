from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "reports" / "nexus_feedback"
VIS_DIR = REPO_ROOT / "visuals" / "nexus_feedback" / "v0_4_5"

INPUTS = {
    "release_readiness": REPO_ROOT / "reports" / "release" / "latest_release_readiness.json",
    "readme_audit": REPO_ROOT / "reports" / "readme" / "latest_readme_mini_repo_audit.json",
    "rcc_nexus": REPO_ROOT / "reports" / "rcc_nexus" / "latest_rcc_nexus_check.json",
    "synthetic_gate_suite": REPO_ROOT / "reports" / "benchmarks" / "latest_synthetic_gate_suite.json",
    "sensitivity_sweep": REPO_ROOT / "reports" / "sensitivity" / "latest_sensitivity_sweep.json",
    "gate_interaction_matrix": REPO_ROOT / "reports" / "interactions" / "latest_gate_interaction_matrix.json",
    "threshold_explanations": REPO_ROOT / "reports" / "explanations" / "latest_threshold_explanation_cards.json",
    "pair_policy_review": REPO_ROOT / "reports" / "policy" / "latest_pair_policy_review.json",
}

def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_missing_or_invalid": True, "_path": str(path), "_error": str(exc)}

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def count_items(value: Any) -> int:
    if value is None:
        return 0
    if isinstance(value, list):
        return len(value)
    if isinstance(value, dict):
        return len(value)
    if isinstance(value, (int, float)):
        return int(value)
    return 1

def bool_pass(payload: dict[str, Any]) -> bool:
    return bool(payload.get("passed") is True) and not payload.get("_missing_or_invalid")

def health_score(inputs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    release = inputs["release_readiness"]
    readme = inputs["readme_audit"]
    rcc = inputs["rcc_nexus"]
    synthetic = inputs["synthetic_gate_suite"]
    sensitivity = inputs["sensitivity_sweep"]
    interactions = inputs["gate_interaction_matrix"]
    explanations = inputs["threshold_explanations"]
    policy = inputs["pair_policy_review"]

    validations = {
        "release_readiness": bool_pass(release) and release.get("step_failures", 0) == 0 and release.get("findings", 0) == 0,
        "readme_audit": bool_pass(readme) and readme.get("warnings", 0) == 0 and readme.get("errors", 0) == 0,
        "rcc_nexus": bool_pass(rcc) and rcc.get("warnings", 0) == 0 and rcc.get("errors", 0) == 0,
        "synthetic_suite": synthetic.get("all_scenarios_passed") is True and synthetic.get("failed_scenarios", 1) == 0,
        "sensitivity_sweep": sensitivity.get("total_points", 0) >= 29 and sensitivity.get("chart_count", 0) >= 10,
        "gate_interactions": interactions.get("all_pairs_executed") is True and interactions.get("pair_count", 0) == 55,
        "explanation_cards": explanations.get("card_count", 0) >= 94,
        "policy_review": policy.get("pair_count", 0) == 55 and policy.get("policy_enforced") is False,
    }

    score = sum(1 for v in validations.values() if v) / len(validations)
    return {"score": round(score, 4), "checks": validations, "passed": score == 1.0}

def feedback_signals(inputs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    signals: list[dict[str, Any]] = []
    policy = inputs["pair_policy_review"]
    explanations = inputs["threshold_explanations"]
    route_map = read_json(REPO_ROOT / "rcc" / "nexus" / "route_map.json")
    agents = read_text(REPO_ROOT / "AGENTS.md")
    readme = read_text(REPO_ROOT / "README.md")

    policy_counts = policy.get("policy_counts", {})
    pair_count = max(1, int(policy.get("pair_count", 1)))
    escalation = int(policy_counts.get("TSEK-D_CANDIDATE", 0)) + int(policy_counts.get("HUMAN_REVIEW", 0)) + int(policy_counts.get("TSEK-E_CANDIDATE", 0))
    escalation_ratio = escalation / pair_count

    signals.append({
        "id": "NF-001",
        "surface": "pair_policy",
        "severity": "high" if escalation_ratio >= 0.15 else "medium" if escalation_ratio > 0 else "low",
        "signal": "pair_policy_escalation_pressure",
        "evidence": {
            "pair_count": pair_count,
            "policy_counts": policy_counts,
            "escalation_ratio": round(escalation_ratio, 4),
        },
        "recommendation": "Run a dry-run simulator before enforcing pair-policy changes.",
        "target_next": "TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator",
    })

    review_counts = explanations.get("review_counts", {})
    hard_reject_without_finding = int(review_counts.get("hard_reject_without_finding", 0))
    signals.append({
        "id": "NF-002",
        "surface": "explanations",
        "severity": "medium" if hard_reject_without_finding else "low",
        "signal": "hard_reject_without_finding",
        "evidence": {"count": hard_reject_without_finding, "review_counts": review_counts},
        "recommendation": "Add explicit finding provenance for any TSEK-E collapse path that currently emits no finding code.",
        "target_next": "Diagnostic finding provenance repair",
    })

    stale_agents_rule = "## v0.4.1 Sensitivity-Sweep Start Rule" in agents
    signals.append({
        "id": "NF-003",
        "surface": "agent_contract",
        "severity": "medium" if stale_agents_rule else "low",
        "signal": "stale_specific_start_rule" if stale_agents_rule else "agent_contract_current",
        "evidence": {"found_v0_4_1_specific_rule": stale_agents_rule},
        "recommendation": "Generalize the AGENTS experiment-start rule so future layers do not carry stale version-specific language.",
        "target_next": "Agent contract feedback sync",
    })

    feedback_route_exists = "nexus_feedback" in route_map.get("v0_4_routes", {})
    signals.append({
        "id": "NF-004",
        "surface": "rcc_nexus",
        "severity": "low" if feedback_route_exists else "medium",
        "signal": "feedback_route_present" if feedback_route_exists else "feedback_route_missing",
        "evidence": {"route_exists": feedback_route_exists},
        "recommendation": "Keep a route-map entry for Nexus feedback so agents know where reflective reports live.",
        "target_next": "Route-map feedback continuity",
    })

    feedback_command_in_readme = "python scripts/feedback/run_nexus_feedback.py" in readme
    signals.append({
        "id": "NF-005",
        "surface": "readme",
        "severity": "low" if feedback_command_in_readme else "medium",
        "signal": "feedback_command_present" if feedback_command_in_readme else "feedback_command_missing",
        "evidence": {"command_present": feedback_command_in_readme},
        "recommendation": "Expose Nexus feedback as a first-class README command.",
        "target_next": "README feedback command sync",
    })

    return signals

def priorities(signals: list[dict[str, Any]]) -> list[dict[str, Any]]:
    weight = {"high": 3, "medium": 2, "low": 1}
    ordered = sorted(signals, key=lambda s: (-weight.get(s["severity"], 0), s["id"]))
    return [
        {
            "rank": i + 1,
            "id": s["id"],
            "surface": s["surface"],
            "severity": s["severity"],
            "signal": s["signal"],
            "recommendation": s["recommendation"],
            "target_next": s["target_next"],
        }
        for i, s in enumerate(ordered)
    ]

def generate_charts(summary: dict[str, Any]) -> list[str]:
    paths: list[str] = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        write_text(OUT_DIR / "chart_generation_skipped.txt", f"matplotlib unavailable: {exc}\n")
        return paths

    VIS_DIR.mkdir(parents=True, exist_ok=True)

    def savefig(path: Path) -> None:
        plt.tight_layout()
        plt.savefig(path, dpi=180, bbox_inches="tight")
        plt.close()
        paths.append(str(path.relative_to(REPO_ROOT)).replace("\\", "/"))

    # Validation health bars.
    checks = summary["health"]["checks"]
    plt.figure(figsize=(10, 4))
    plt.bar(list(checks.keys()), [1 if v else 0 for v in checks.values()])
    plt.ylim(0, 1.1)
    plt.ylabel("Pass = 1")
    plt.title("Nexus Validation Health Surface")
    plt.xticks(rotation=45, ha="right", fontsize=8)
    savefig(VIS_DIR / "nexus_validation_health.png")

    # Feedback severity counts.
    sev_counts: dict[str, int] = {}
    for s in summary["signals"]:
        sev_counts[s["severity"]] = sev_counts.get(s["severity"], 0) + 1
    plt.figure(figsize=(6, 4))
    plt.bar(list(sev_counts.keys()), list(sev_counts.values()))
    plt.title("Nexus Feedback Severity Counts")
    plt.ylabel("Signal count")
    savefig(VIS_DIR / "nexus_feedback_severity_counts.png")

    # Priority rank chart.
    pr = summary["priorities"]
    plt.figure(figsize=(10, 4))
    plt.bar([p["id"] for p in pr], list(range(len(pr), 0, -1)))
    plt.title("Nexus Improvement Priority Stack")
    plt.ylabel("Relative priority")
    savefig(VIS_DIR / "nexus_priority_stack.png")

    return paths

def render_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.4.5b Nexus Feedback Health Schema Alignment",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Health score: `{summary['health']['score']}`",
        f"- Health passed: `{summary['health']['passed']}`",
        f"- Feedback signal count: `{len(summary['signals'])}`",
        f"- Chart count: `{len(summary['chart_paths'])}`",
        "",
        "## Health Checks",
        "",
        "| Check | Passed |",
        "|---|---:|",
    ]
    for k, v in summary["health"]["checks"].items():
        lines.append(f"| `{k}` | `{v}` |")

    lines += [
        "",
        "## Improvement Priorities",
        "",
        "| Rank | Signal | Severity | Surface | Recommendation | Target next |",
        "|---:|---|---|---|---|---|",
    ]
    for p in summary["priorities"]:
        lines.append(f"| {p['rank']} | `{p['signal']}` | `{p['severity']}` | `{p['surface']}` | {p['recommendation']} | {p['target_next']} |")

    lines += [
        "",
        "## Feedback Signals",
        "",
        "| ID | Surface | Severity | Signal | Evidence | Recommendation |",
        "|---|---|---|---|---|---|",
    ]
    for s in summary["signals"]:
        ev = json.dumps(s["evidence"], sort_keys=True).replace("|", "\\|")
        lines.append(f"| `{s['id']}` | `{s['surface']}` | `{s['severity']}` | `{s['signal']}` | `{ev}` | {s['recommendation']} |")

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
    inputs = {name: read_json(path) for name, path in INPUTS.items()}
    health = health_score(inputs)
    signals = feedback_signals(inputs)
    summary = {
        "schema": "tau-scaling-nexus-reflective-feedback-v0.4.5b",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "inputs": {k: str(v.relative_to(REPO_ROOT)).replace("\\", "/") for k, v in INPUTS.items()},
        "health": health,
        "signals": signals,
        "priorities": priorities(signals),
        "boundary": "Nexus feedback is repository self-observation and improvement prioritization only. It does not mutate classifier behavior and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, AI understanding, or universal Tau Scaling law.",
    }
    charts = generate_charts(summary)
    summary["chart_paths"] = charts

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(OUT_DIR / "nexus_feedback_v0_4_5.json", summary)
    write_json(OUT_DIR / "latest_nexus_feedback.json", summary)
    md = render_markdown(summary)
    write_text(OUT_DIR / "nexus_feedback_v0_4_5.md", md)
    write_text(OUT_DIR / "latest_nexus_feedback.md", md)

    print(json.dumps({
        "schema": summary["schema"],
        "health_score": summary["health"]["score"],
        "health_passed": summary["health"]["passed"],
        "signal_count": len(summary["signals"]),
        "priorities": summary["priorities"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/nexus_feedback/latest_nexus_feedback.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
