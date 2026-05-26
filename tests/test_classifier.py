import unittest

from tau_scaling.claims.classifier import classify_tsek


class TestClassifier(unittest.TestCase):
    def test_overclaim_blocks(self):
        record = {
            "source_boundary": {
                "source_declared": True,
                "reported_claims_separated_from_validation": True
            },
            "claim_card": {
                "claim_text": "validated chip",
                "claim_type": "reported_metric",
                "independent_validation_claimed": True
            },
            "workload_profile": {"workload_class": "mobile_soc", "dominant_tau_term": "circuit"},
            "tau_vector": {"baseline": {"circuit": 1}, "candidate": {"circuit": 0.8}, "weights_declared": True, "dominant_tau_improved": True},
            "logicfolding_margin": 1.0,
            "gamma_tau_ETP": 1.2,
            "pvt_closure": {"post_route_closure_passed": True, "pvt_variation_passed": True, "pdn_reported": True},
            "yield_method_disclosure": {"method_disclosed": True, "yield_reported": True},
            "evidence_disclosure": {"evidence_package_complete": True, "independent_validation_present": False},
            "overclaim": 0.0,
        }
        result = classify_tsek(record)
        self.assertEqual(result["class"], "TSEK-E")

    def test_partial_public_claim_is_c(self):
        record = {
            "source_boundary": {
                "source_declared": True,
                "reported_claims_separated_from_validation": True
            },
            "claim_card": {
                "claim_text": "reported roadmap",
                "claim_type": "roadmap",
                "independent_validation_claimed": False
            },
            "workload_profile": {"workload_class": "mobile_soc", "dominant_tau_term": "circuit"},
            "tau_vector": {"baseline": {"circuit": 1}, "candidate": {"circuit": 0.8}, "weights_declared": True, "dominant_tau_improved": True},
            "logicfolding_margin": 1.0,
            "gamma_tau_ETP": 1.2,
            "pvt_closure": {"post_route_closure_passed": True, "pvt_variation_passed": True, "pdn_reported": True},
            "yield_method_disclosure": {"method_disclosed": True, "yield_reported": False},
            "evidence_disclosure": {"evidence_package_complete": True, "independent_validation_present": False},
            "overclaim": 0.0,
        }
        result = classify_tsek(record)
        self.assertEqual(result["class"], "TSEK-C")


if __name__ == "__main__":
    unittest.main()
