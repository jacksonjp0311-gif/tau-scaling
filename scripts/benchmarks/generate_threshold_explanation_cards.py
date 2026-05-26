from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "reports" / "explanations"
CARD_DIR = OUT_DIR / "cards" / "v0_4_3"
VIS_DIR = REPO_ROOT / "visuals" / "explanations" / "v0_4_3"

SOURCES = {
    "synthetic_gate_suite": REPO_ROOT / "reports" / "benchmarks" / "latest_synthetic_gate_suite.json",
    "sensitivity_sweep": REPO_ROOT / "reports" / "sensitivity" / "latest_sensitivity_sweep.json",
    "gate_interaction_matrix": REPO_ROOT / "reports" / "interactions" / "latest_gate_interaction_matrix.json",
}

CLASS_RANK = {"TSEK-E": 0, "TSEK-D": 1, "TSEK-C": 2, "TSEK-B": 3, "TSEK-A": 4}

GATE_REPAIRS = {
    "TSEK_B_source_MISSING": "Declare source boundary and separate reported claims from validation.",
    "TSEK_B_metric_MISSING": "Add a measurable claim text/type and metric definition.",
    "TSEK_B_baseline_MISSING": "Add explicit baseline manifest and baseline tau vector.",
    "TSEK_B_method_MISSING": "Disclose method and yield methodology.",
    "TSEK_B_workload_MISSING": "Declare workload class and dominant tau term.",
    "TSEK_B_tau_MISSING": "Declare tau weights and dominant tau improvement.",
    "TSEK_B_LF_MISSING": "Restore positive LogicFolding survivability margin.",
    "TSEK_B_ETP_MISSING": "Improve energy/thermal/PDN-normalized tau gain above threshold.",
    "TSEK_B_PVT_MISSING": "Provide closure, PVT, and PDN evidence.",
    "TSEK_B_yield_MISSING": "Report yield or downgrade the claim.",
    "TSEK_B_evidence_MISSING": "Complete the evidence package.",
    "TSEK_OVERCLAIM_INDEPENDENT_VALIDATION": "Remove independent-validation claim or provide independent validation evidence.",
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

def normalize_code(code: str) -> str:
    return code.replace("_baseline_", "_baseline_").strip()

def minimum_repair(finding_codes: list[str], classification: str) -> list[str]:
    if not finding_codes:
        if classification == "TSEK-B":
            return ["Independent validation would be required for TSEK-A promotion."]
        return ["No explicit finding codes were emitted; inspect gate values and classifier thresholds."]
    repairs = []
    for code in finding_codes:
        repairs.append(GATE_REPAIRS.get(code, f"Repair finding `{code}`."))
    return repairs

def explain_class(record: dict[str, Any]) -> str:
    cls = record.get("classification", "unknown")
    findings = record.get("finding_codes", [])
    a_tsek = record.get("A_TSEK")
    diag = record.get("diagnostic_average")
    if cls == "TSEK-B" and not findings:
        return "Promoted to TSEK-B because all local hard gates are disclosed and no independent-validation claim is made. TSEK-A remains blocked without independent validation."
    if cls == "TSEK-C":
        return f"Downgraded to TSEK-C because one or more required evidence gates are missing while the claim remains interpretable. A_TSEK={a_tsek}, diagnostic_average={diag}."
    if cls == "TSEK-D":
        return f"Downgraded to TSEK-D because diagnostic support is weak but not fully rejected. A_TSEK={a_tsek}, diagnostic_average={diag}."
    if cls == "TSEK-E":
        if "TSEK_OVERCLAIM_INDEPENDENT_VALIDATION" in findings:
            return "Rejected to TSEK-E because an independent-validation claim was made without corresponding independent-validation evidence."
        return f"Rejected or severe downgrade to TSEK-E because classifier support collapsed. A_TSEK={a_tsek}, diagnostic_average={diag}."
    return "Class explanation unavailable."

def suspicion_label(record: dict[str, Any], source: str) -> str:
    cls = record.get("classification")
    findings = record.get("finding_codes", [])
    if source == "gate_interaction_matrix" and cls == "TSEK-C" and len(findings) >= 2:
        return "review_pair_policy"
    if cls == "TSEK-B" and findings:
        return "unexpected_promotion_with_findings"
    if cls == "TSEK-E" and not findings:
        return "hard_reject_without_finding"
    return "expected"

def make_card(source: str, record: dict[str, Any], idx: int) -> dict[str, Any]:
    finding_codes = record.get("finding_codes", [])
    if "id" in record:
        subject_id = record["id"]
    elif "sweep" in record:
        subject_id = f"{record.get('sweep')}:{record.get('x_name')}={record.get('x_value')}"
    elif "gate_a" in record:
        subject_id = f"{record.get('gate_a')}+{record.get('gate_b')}"
    else:
        subject_id = f"{source}-{idx:04d}"
    card = {
        "schema": "tau-scaling-threshold-explanation-card-v0.4.3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "subject_id": subject_id,
        "classification": record.get("classification"),
        "A_TSEK": record.get("A_TSEK"),
        "diagnostic_average": record.get("diagnostic_average"),
        "findings_count": record.get("findings_count", len(finding_codes)),
        "finding_codes": finding_codes,
        "why_this_class": explain_class(record),
        "minimum_repair_for_promotion": minimum_repair(finding_codes, record.get("classification", "")),
        "review_label": suspicion_label(record, source),
        "evidence_path": record.get("evidence_path"),
        "non_claim_lock": "Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.",
    }
    if "sweep" in record:
        card["threshold_context"] = {
            "sweep": record.get("sweep"),
            "x_name": record.get("x_name"),
            "x_value": record.get("x_value"),
            "logicfolding_margin": record.get("logicfolding_margin"),
            "gamma_tau_ETP": record.get("gamma_tau_ETP"),
        }
    if "gate_a" in record:
        card["interaction_context"] = {
            "gate_a": record.get("gate_a"),
            "gate_b": record.get("gate_b"),
            "gate_values": record.get("gate_values"),
            "logicfolding_margin": record.get("logicfolding_margin"),
            "gamma_tau_ETP": record.get("gamma_tau_ETP"),
        }
    return card

def collect_records() -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    for source, path in SOURCES.items():
        payload = read_json(path)
        results = payload.get("results", [])
        for idx, rec in enumerate(results):
            cards.append(make_card(source, rec, idx))
    return cards

def summarize(cards: list[dict[str, Any]], chart_paths: list[str]) -> dict[str, Any]:
    class_counts: dict[str, int] = {}
    review_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {}
    finding_counts: dict[str, int] = {}
    for c in cards:
        class_counts[c["classification"]] = class_counts.get(c["classification"], 0) + 1
        review_counts[c["review_label"]] = review_counts.get(c["review_label"], 0) + 1
        source_counts[c["source"]] = source_counts.get(c["source"], 0) + 1
        for code in c["finding_codes"]:
            finding_counts[code] = finding_counts.get(code, 0) + 1

    review_examples = [c for c in cards if c["review_label"] != "expected"][:25]
    return {
        "schema": "tau-scaling-threshold-explanation-cards-v0.4.3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "card_count": len(cards),
        "class_counts": class_counts,
        "source_counts": source_counts,
        "review_counts": review_counts,
        "finding_counts": finding_counts,
        "review_examples": review_examples,
        "chart_paths": chart_paths,
        "card_directory": str(CARD_DIR.relative_to(REPO_ROOT)).replace("\\", "/"),
        "boundary": "Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.",
    }

def generate_charts(cards: list[dict[str, Any]]) -> list[str]:
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

    def counts_for(key: str) -> dict[str, int]:
        d: dict[str, int] = {}
        for c in cards:
            d[str(c.get(key))] = d.get(str(c.get(key)), 0) + 1
        return d

    for key, title, fname in [
        ("classification", "Explanation Card Class Counts", "explanation_class_counts.png"),
        ("review_label", "Explanation Card Review Labels", "explanation_review_labels.png"),
        ("source", "Explanation Card Source Counts", "explanation_source_counts.png"),
    ]:
        data = counts_for(key)
        plt.figure(figsize=(8, 4))
        plt.bar(list(data.keys()), list(data.values()))
        plt.title(title)
        plt.ylabel("Card count")
        plt.xticks(rotation=30, ha="right")
        savefig(VIS_DIR / fname)

    finding_counts: dict[str, int] = {}
    for c in cards:
        for code in c["finding_codes"]:
            finding_counts[code] = finding_counts.get(code, 0) + 1
    if finding_counts:
        labels = list(finding_counts.keys())
        values = [finding_counts[k] for k in labels]
        plt.figure(figsize=(12, 5))
        plt.bar(labels, values)
        plt.title("Finding Frequency Across Explanation Cards")
        plt.ylabel("Count")
        plt.xticks(rotation=65, ha="right", fontsize=7)
        savefig(VIS_DIR / "explanation_finding_frequency.png")

    return chart_paths

def render_card_md(card: dict[str, Any]) -> str:
    repairs = "\n".join(f"- {r}" for r in card["minimum_repair_for_promotion"])
    findings = "\n".join(f"- `{c}`" for c in card["finding_codes"]) or "None"
    return f"""# Explanation Card — {card['subject_id']}

Generated: `{card['generated_at']}`

| Field | Value |
|---|---|
| Source | `{card['source']}` |
| Classification | `{card['classification']}` |
| A_TSEK | `{card['A_TSEK']}` |
| Diagnostic average | `{card['diagnostic_average']}` |
| Findings count | `{card['findings_count']}` |
| Review label | `{card['review_label']}` |

## Why This Class

{card['why_this_class']}

## Finding Codes

{findings}

## Minimum Repair For Promotion

{repairs}

## Evidence Path

```text
{card.get('evidence_path')}
```

## Boundary

{card['non_claim_lock']}
"""

def render_summary_md(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.4.3 Threshold Explanation Cards",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Card count: `{summary['card_count']}`",
        f"- Card directory: `{summary['card_directory']}`",
        f"- Chart count: `{len(summary['chart_paths'])}`",
        "",
        "## Source Counts",
        "",
        "| Source | Count |",
        "|---|---:|",
    ]
    for k, v in sorted(summary["source_counts"].items()):
        lines.append(f"| `{k}` | {v} |")

    lines += ["", "## Class Counts", "", "| Class | Count |", "|---|---:|"]
    for k, v in sorted(summary["class_counts"].items()):
        lines.append(f"| `{k}` | {v} |")

    lines += ["", "## Review Labels", "", "| Label | Count | Meaning |", "|---|---:|---|"]
    meanings = {
        "expected": "Classifier behavior matches current policy.",
        "review_pair_policy": "Paired failures remained controlled downgrade; review whether this should become stricter.",
        "unexpected_promotion_with_findings": "Promotion occurred despite findings; inspect immediately.",
        "hard_reject_without_finding": "Hard reject occurred without clear finding; inspect immediately.",
    }
    for k, v in sorted(summary["review_counts"].items()):
        lines.append(f"| `{k}` | {v} | {meanings.get(k, '')} |")

    lines += ["", "## Review Examples", "", "| Source | Subject | Class | Review label | Why |", "|---|---|---|---|---|"]
    for c in summary["review_examples"]:
        why = c["why_this_class"].replace("|", "\\|")
        lines.append(f"| `{c['source']}` | `{c['subject_id']}` | `{c['classification']}` | `{c['review_label']}` | {why} |")

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
    cards = collect_records()
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    for idx, card in enumerate(cards):
        safe_id = "".join(ch if ch.isalnum() or ch in "-_." else "_" for ch in card["subject_id"]).strip("_")[:140]
        json_path = CARD_DIR / f"{idx:04d}_{safe_id}.json"
        md_path = CARD_DIR / f"{idx:04d}_{safe_id}.md"
        write_json(json_path, card)
        write_text(md_path, render_card_md(card))

    chart_paths = generate_charts(cards)
    summary = summarize(cards, chart_paths)
    write_json(OUT_DIR / "threshold_explanation_cards_v0_4_3.json", summary)
    write_json(OUT_DIR / "latest_threshold_explanation_cards.json", summary)
    write_text(OUT_DIR / "threshold_explanation_cards_v0_4_3.md", render_summary_md(summary))
    write_text(OUT_DIR / "latest_threshold_explanation_cards.md", render_summary_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "card_count": summary["card_count"],
        "class_counts": summary["class_counts"],
        "source_counts": summary["source_counts"],
        "review_counts": summary["review_counts"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/explanations/latest_threshold_explanation_cards.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
