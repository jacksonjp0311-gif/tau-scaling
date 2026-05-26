from __future__ import annotations

from typing import Any


def _f(x: Any, default: float = 1.0) -> float:
    try:
        return float(x)
    except Exception:
        return default


def gamma_tau_etp(record: dict[str, Any]) -> float:
    tau_gain = _f(record.get("tau_gain"), 0.0)
    e_ratio = _f(record.get("energy_ratio_new_over_old"), 1.0)
    thermal_ratio = _f(record.get("thermal_ratio_new_over_old"), 1.0)
    pdn_ratio = _f(record.get("pdn_droop_ratio_new_over_old"), 1.0)
    if e_ratio <= 0 or thermal_ratio <= 0 or pdn_ratio <= 0:
        return 0.0
    return round(tau_gain / (e_ratio * thermal_ratio * pdn_ratio), 6)
