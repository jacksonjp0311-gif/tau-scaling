from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLAIM_DIR = ROOT / "claims" / "public_tau"
OUT = ROOT / "reports" / "tau_claim_ledger"

def load_claims():
    claims = []
    for path in sorted(CLAIM_DIR.glob("tau-public-*.json")):
        claims.append(json.loads(path.read_text(encoding="utf-8")))
    return claims

def class_counts(claims):
    counts = {"TSEK-A": 0, "TSEK-B": 0, "TSEK-C": 0, "TSEK-D": 0, "TSEK-E": 0}
    for claim in claims:
        klass = claim.get("current_tsek_class", "TSEK-E")
        counts[klass] = counts.get(klass, 0) + 1
    return counts

def missing_gate_count(claim):
    fields = [
        "baseline_disclosed",
        "method_disclosed",
        "energy_reported",
        "thermal_reported",
        "yield_reported",
        "pdn_pvt_reported",
        "independent_validation_present",
    ]
    return sum(1 for field in fields if claim.get(field) is False or claim.get(field) is None)

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main():
    claims = load_claims()
    counts = class_counts(claims)
    avg_missing = round(sum(missing_gate_count(c) for c in claims) / max(len(claims), 1), 3)

    data = {
        "schema": "tau-scaling-public-tau-claim-ledger-v0.8.2",
        "claim_count": len(claims),
        "class_counts": counts,
        "tsek_a_count": counts.get("TSEK-A", 0),
        "tsek_b_count": counts.get("TSEK-B", 0),
        "tsek_c_count": counts.get("TSEK-C", 0),
        "tsek_d_count": counts.get("TSEK-D", 0),
        "tsek_e_count": counts.get("TSEK-E", 0),
        "average_missing_evidence_gates": avg_missing,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "public_result": "The current public Tau claim set is mostly TSEK-C with roadmap/system claims in TSEK-D. This supports continued investigation, not independent validation.",
        "boundary": "Public Tau claim ledgers classify disclosed evidence only. They do not validate Huawei silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "claims": claims,
    }

    lines = [
        "# Public Tau Claim Ledger v0.8.2",
        "",
        "## Result",
        "",
        f"- Claim count: `{data['claim_count']}`",
        f"- TSEK-A: `{data['tsek_a_count']}`",
        f"- TSEK-B: `{data['tsek_b_count']}`",
        f"- TSEK-C: `{data['tsek_c_count']}`",
        f"- TSEK-D: `{data['tsek_d_count']}`",
        f"- TSEK-E: `{data['tsek_e_count']}`",
        f"- Average missing evidence gates: `{data['average_missing_evidence_gates']}`",
        "",
        "## Public Result",
        "",
        data["public_result"],
        "",
        "| Claim ID | Title | Class | Downgrade reason |",
        "|---|---|---|---|",
    ]
    for claim in claims:
        lines.append(f"| `{claim['claim_id']}` | {claim['title']} | `{claim['current_tsek_class']}` | {claim['downgrade_reason']} |")
    lines += ["", "## Boundary", "", data["boundary"], ""]

    write_json(OUT / "latest_tau_public_claim_ledger.json", data)
    write_json(OUT / "tau_public_claim_ledger_v0_8_2.json", data)
    write(OUT / "latest_tau_public_claim_ledger.md", "\n".join(lines))
    write(OUT / "tau_public_claim_ledger_v0_8_2.md", "\n".join(lines))

    print(json.dumps({
        "schema": data["schema"],
        "claim_count": data["claim_count"],
        "class_counts": data["class_counts"],
        "average_missing_evidence_gates": data["average_missing_evidence_gates"],
        "thresholds_changed": data["thresholds_changed"],
        "classifier_changed": data["classifier_changed"],
        "mutation_allowed": data["mutation_allowed"],
        "application_allowed": data["application_allowed"],
        "report": "reports/tau_claim_ledger/latest_tau_public_claim_ledger.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()