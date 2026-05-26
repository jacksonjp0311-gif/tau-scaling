from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tau_scaling.utils.run_identity import ensure_unique_run_dir, generate_run_id


class RunIdentityTests(unittest.TestCase):
    def test_generate_run_id_is_collision_resistant(self) -> None:
        ids = [generate_run_id("claim") for _ in range(250)]
        self.assertEqual(len(ids), len(set(ids)))
        for run_id in ids:
            self.assertTrue(run_id.startswith("claim-"))
            self.assertNotIn(" ", run_id)

    def test_ensure_unique_run_dir_avoids_existing_path(self) -> None:
        with TemporaryDirectory() as tmp:
            base = Path(tmp)
            existing = "claim-existing"
            (base / existing).mkdir()
            run_id, run_dir = ensure_unique_run_dir(base, existing)
            self.assertNotEqual(run_id, existing)
            self.assertFalse(run_dir.exists())


if __name__ == "__main__":
    unittest.main()