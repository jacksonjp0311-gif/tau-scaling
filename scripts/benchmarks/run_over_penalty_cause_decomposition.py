
from __future__ import annotations
import json, os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
READINESS = ROOT / "reports" / "enforcement_readiness" / "latest_enforcement_readiness_gate.json"
OUT = ROOT / "reports" / "over_penalty_causes"
CARDS = OUT / "cards" / "v0_5_2"
VIS = ROOT / "visuals" / "over_penalty_causes" / "v0_5_2"

def rjson(p): return json.loads(p.read_text(encoding="utf-8"))
def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")
def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def causes(row):
    reasons = row.get("baseline_over_penalty_reasons", []) or []
    findings = int(row.get("findings_count", 0) or 0)
    severity = int(row.get("drift_severity", 0) or 0)
    out = []
    if "missing_finding_provenance" in reasons or findings == 0:
        out.append("missing_finding_provenance")
    if "high_diagnostic_support" in reasons:
        out.append("high_diagnostic_support")
    if "high_drift_severity" in reasons or severity >= 2:
        out.append("high_drift_severity")
    if out == ["high_diagnostic_support"]:
        out.append("heuristic_over_sensitivity")
    return out or ["undifferentiated_over_penalty"]

REMEDY = {
    "missing_finding_provenance": "Add explicit finding provenance before reconsidering the downgrade.",
    "high_diagnostic_support": "Add a secondary evidence-pressure test before downgrading high-support cases.",
    "high_drift_severity": "Separate severe drift cases and require manual review.",
    "heuristic_over_sensitivity": "Prepare a disabled calibration plan; do not mutate classifier behavior.",
    "undifferentiated_over_penalty": "Retain the block and collect more diagnostic features.",
}

def card(row, i):
    cs = causes(row)
    return {
        "schema": "tau-scaling-over-penalty-cause-card-v0.5.2",
        "card_id": f"over-penalty-cause-v0-5-2-{i:03d}",
        "gate_pair": row.get("gate_pair"),
        "gate_a": row.get("gate_a"),
        "gate_b": row.get("gate_b"),
        "readiness_status": row.get("readiness_status"),
        "decision": row.get("decision"),
        "current_classification": row.get("current_classification"),
        "simulated_policy_classification": row.get("simulated_policy_classification"),
        "current_diagnostic_average": row.get("current_diagnostic_average"),
        "findings_count": row.get("findings_count"),
        "drift_severity": row.get("drift_severity"),
        "causes": cs,
        "primary_cause": cs[0],
        "remediation": REMEDY[cs[0]],
        "candidate_status": "blocked_until_remediated",
        "mutation_allowed": False,
        "policy_enforced": False,
        "non_claim_lock": "Cause cards are local classifier-governance diagnostics only.",
    }

def card_md(c):
    return f"""# {c['card_id']}

- Gate pair: `{c['gate_pair']}`
- Primary cause: `{c['primary_cause']}`
- Causes: `{', '.join(c['causes'])}`
- Candidate status: `{c['candidate_status']}`
- Mutation allowed: `{c['mutation_allowed']}`
- Policy enforced: `{c['policy_enforced']}`

## Remediation

{c['remediation']}

## Boundary

{c['non_claim_lock']}
"""

def charts(summary):
    paths = []
    try:
        import matplotlib.pyplot as plt
    except Exception as e:
        wtext(OUT / "chart_generation_skipped.txt", str(e))
        return paths
    VIS.mkdir(parents=True, exist_ok=True)
    def save(name):
        p = VIS / name
        plt.tight_layout()
        plt.savefig(p, dpi=180, bbox_inches="tight")
        plt.close()
        paths.append(str(p.relative_to(ROOT)).replace("\\", "/"))
    for title, data, fname in [
        ("Over-Penalty Cause Counts", summary["cause_counts"], "over_penalty_cause_counts.png"),
        ("Primary Cause Counts", summary["primary_cause_counts"], "over_penalty_primary_cause_counts.png"),
        ("Blocked Gate Involvement", summary["gate_involvement_counts"], "over_penalty_gate_involvement.png"),
    ]:
        plt.figure(figsize=(9,4))
        plt.bar(list(data.keys()), list(data.values()))
        plt.xticks(rotation=25, ha="right")
        plt.ylabel("Count")
        plt.title(title)
        save(fname)
    return paths

def report(summary):
    lines = [
        "# Tau Scaling v0.5.2 Over-Penalty Cause Decomposition",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Blocked candidate count: `{summary['blocked_candidate_count']}`",
        f"- Cause card count: `{summary['cause_card_count']}`",
        f"- Final recommendation: `{summary['final_recommendation']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        "",
        "## Cause Counts",
        "",
        "| Cause | Count |",
        "|---|---:|",
    ]
    for k,v in summary["cause_counts"].items():
        lines.append(f"| `{k}` | {v} |")
    lines += ["", "## Cards", "", "| Card | Gate pair | Primary cause | Remediation |", "|---|---|---|---|"]
    for c in summary["cause_cards"]:
        lines.append(f"| `{c['card_id']}` | `{c['gate_pair']}` | `{c['primary_cause']}` | {c['remediation']} |")
    lines += ["", "## Charts", ""]
    for p in summary["chart_paths"]:
        rel = os.path.relpath(ROOT / p, OUT).replace("\\", "/")
        lines.append(f"![{Path(p).stem}]({rel})")
        lines.append("")
    lines += ["## Boundary", "", summary["boundary"], ""]
    return "\n".join(lines)

def main():
    readiness = rjson(READINESS)
    blocked = [x for x in readiness.get("readiness_rows", []) if x.get("readiness_status") == "BLOCKED_BY_OVER_PENALTY"]
    cards = [card(x, i+1) for i,x in enumerate(blocked)]
    CARDS.mkdir(parents=True, exist_ok=True)
    for c in cards:
        wjson(CARDS / f"{c['card_id']}.json", c)
        wtext(CARDS / f"{c['card_id']}.md", card_md(c))
    cause_counts, primary, gates = Counter(), Counter(), Counter()
    for c in cards:
        primary[c["primary_cause"]] += 1
        for cause in c["causes"]: cause_counts[cause] += 1
        gates[c["gate_a"]] += 1
        gates[c["gate_b"]] += 1
    final = "repair_finding_provenance_before_policy_design" if cause_counts.get("missing_finding_provenance",0) else "prepare_disabled_calibration_plan"
    summary = {
        "schema": "tau-scaling-over-penalty-cause-decomposition-v0.5.2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "blocked_candidate_count": len(blocked),
        "cause_card_count": len(cards),
        "cause_counts": dict(cause_counts),
        "primary_cause_counts": dict(primary),
        "gate_involvement_counts": dict(gates),
        "cause_cards": cards,
        "mutation_allowed": False,
        "policy_enforced": False,
        "final_recommendation": final,
        "boundary": "Over-penalty cause decomposition is local classifier-governance analysis only. It does not change classifier behavior and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.5.3 should implement cause-specific remediation planning without classifier mutation.",
    }
    summary["chart_paths"] = charts(summary)
    wjson(OUT / "over_penalty_cause_decomposition_v0_5_2.json", summary)
    wjson(OUT / "latest_over_penalty_cause_decomposition.json", summary)
    wtext(OUT / "over_penalty_cause_decomposition_v0_5_2.md", report(summary))
    wtext(OUT / "latest_over_penalty_cause_decomposition.md", report(summary))
    print(json.dumps({
        "schema": summary["schema"],
        "blocked_candidate_count": summary["blocked_candidate_count"],
        "cause_card_count": summary["cause_card_count"],
        "cause_counts": summary["cause_counts"],
        "final_recommendation": summary["final_recommendation"],
        "mutation_allowed": summary["mutation_allowed"],
        "policy_enforced": summary["policy_enforced"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md",
    }, indent=2, sort_keys=True))
if __name__ == "__main__":
    main()
