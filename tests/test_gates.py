import unittest

from tau_scaling.gates.logicfolding_survivability import logicfolding_margin
from tau_scaling.gates.gamma_tau_etp import gamma_tau_etp
from tau_scaling.gates.edge_surface import edge_surface_ratio


class TestGates(unittest.TestCase):
    def test_logicfolding_margin_positive(self):
        record = {
            "rho_critical_paths": 0.75,
            "expected_wire_savings_ps": 42,
            "expected_vertical_penalty_ps": 8,
            "routing_penalty_ps": 5,
            "sync_penalty_ps": 3,
            "variation_penalty_ps": 2,
            "closure_penalty_ps": 4,
        }
        self.assertGreater(logicfolding_margin(record), 0)

    def test_gamma_tau_etp(self):
        record = {
            "tau_gain": 1.22,
            "energy_ratio_new_over_old": 0.95,
            "thermal_ratio_new_over_old": 1.05,
            "pdn_droop_ratio_new_over_old": 1.02,
        }
        self.assertGreater(gamma_tau_etp(record), 1.0)

    def test_edge_surface_ratio(self):
        result = edge_surface_ratio({"N": 16})
        self.assertLess(result["beta_edge"], result["beta_surface"])


if __name__ == "__main__":
    unittest.main()
