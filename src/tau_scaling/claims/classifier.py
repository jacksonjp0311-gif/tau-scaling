from __future__ import annotations

from typing import Any


def clamp01(x: Any) -> float:
    try:
        return max(0.0, min(1.0, float(x)))
    except Exception:
        return 0.0


def _bool_gate(value: Any) -> float:
    return 1.0 if bool(value) else 0.0


def classify_tsek(record: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, str]] = []

    source = record.get("source_boundary", {})
    claim = record.get("claim_card", {})
    workload = record.get("workload_profile", {})
    tau_vector = record.get("tau_vector", {})
    pvt = record.get("pvt_closure", {})
    method = record.get("yield_method_disclosure", {})
    evidence = record.get("evidence_disclosure", {})
    overclaim = clamp01(record.get("overclaim", 0.0))

    B_source = _bool_gate(source.get("source_declared") and source.get("reported_claims_separated_from_validation"))
    B_metric = _bool_gate(claim.get("claim_text") and claim.get("claim_type"))
    B_baseline = _bool_gate(tau_vector.get("baseline") and tau_vector.get("candidate"))
    B_method = _bool_gate(method.get("method_disclosed"))
    B_workload = _bool_gate(workload.get("workload_class") and workload.get("dominant_tau_term"))
    B_tau = _bool_gate(tau_vector.get("weights_declared") and tau_vector.get("dominant_tau_improved"))
    B_LF = _bool_gate(record.get("logicfolding_margin", 0.0) > 0)
    B_ETP = _bool_gate(record.get("gamma_tau_ETP", 0.0) > 1.0)
    B_PVT = _bool_gate(pvt.get("post_route_closure_passed") and pvt.get("pvt_variation_passed") and pvt.get("pdn_reported"))
    B_yield = _bool_gate(method.get("yield_reported"))
    B_evidence = _bool_gate(evidence.get("evidence_package_complete"))

    hard_gates = {
        "B_source": B_source,
        "B_metric": B_metric,
        "B_baseline": B_baseline,
        "B_method": B_method,
        "B_workload": B_workload,
        "B_tau": B_tau,
        "B_LF": B_LF,
        "B_ETP": B_ETP,
        "B_PVT": B_PVT,
        "B_yield": B_yield,
        "B_evidence": B_evidence,
    }

    for gate, value in hard_gates.items():
        if value == 0:
            findings.append({
                "code": f"TSEK_{gate}_MISSING",
                "severity": "warning",
                "message": f"{gate} failed or was not disclosed."
            })

    if claim.get("independent_validation_claimed") and not evidence.get("independent_validation_present"):
        findings.append({
            "code": "TSEK_OVERCLAIM_INDEPENDENT_VALIDATION",
            "severity": "blocking",
            "message": "Independent validation was claimed but not provided."
        })
        overclaim = max(overclaim, 1.0)

    product = 1.0
    for value in hard_gates.values():
        product *= value

    average_score = sum(hard_gates.values()) / len(hard_gates)
    A_TSEK = round(product * (1.0 - overclaim), 4)

    has_blocking = any(f["severity"] == "blocking" for f in findings)

    if has_blocking or overclaim >= 1.0:
        klass = "TSEK-E"
    elif evidence.get("independent_validation_present") and A_TSEK >= 0.95:
        klass = "TSEK-A"
    elif A_TSEK >= 0.75:
        klass = "TSEK-B"
    elif average_score >= 0.45 and not has_blocking:
        klass = "TSEK-C"
    elif average_score >= 0.20:
        klass = "TSEK-D"
    else:
        klass = "TSEK-E"

    return {
        "schema": "TAU-SCALING-SA-v0.1-classification-result",
        "class": klass,
        "admissible": klass in {"TSEK-A", "TSEK-B"},
        "admissible_claim": {
            **hard_gates,
            "O": overclaim,
            "A_TSEK": A_TSEK,
            "diagnostic_average": round(average_score, 4),
        },
        "findings": findings,
        "non_claim_locks": {
            "roadmap_coherence_is_not_validation": True,
            "simulation_is_not_silicon_validation": True,
            "density_equivalence_is_not_node_equivalence": True,
            "local_path_win_is_not_full_chip_win": True,
        }
    }
