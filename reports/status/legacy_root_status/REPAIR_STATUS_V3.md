# Tau Scaling Repair Status v3

Repo: C:\Users\jacks\OneDrive\Desktop\tau-scaling

Repair actions:
- Stripped UTF-8 BOM from all JSON files.
- Hardened src/tau_scaling/utils/safe_json.py to read utf-8-sig safely.
- Validated all JSON files with Python.
- Reinstalled editable package.
- Ran import smoke test.
- Ran demo/tests according to selected switches.

Quick commands:

``powershell
cd "C:\Users\jacks\OneDrive\Desktop\tau-scaling"
.\.venv\Scripts\Activate.ps1
python -m tau_scaling run-claim --seed configs\seeds\logicfolding_claim_card.json
python -m unittest discover -s tests
``

Non-claim lock:
Roadmap coherence is not validation. Simulation is not silicon evidence.