import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tau_scaling.core.runtime import TauScalingRuntime


class TestRuntime(unittest.TestCase):
    def test_runtime_emits_evidence(self):
        seed_path = Path("configs/seeds/logicfolding_claim_card.json")
        seed = json.loads(seed_path.read_text(encoding="utf-8"))
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "artifacts" / "runs").mkdir(parents=True, exist_ok=True)
            result = TauScalingRuntime(root).run(seed)
            self.assertTrue(Path(result.evidence_path).exists())
            self.assertIn(result.classification, {"TSEK-A", "TSEK-B", "TSEK-C", "TSEK-D", "TSEK-E"})


if __name__ == "__main__":
    unittest.main()
