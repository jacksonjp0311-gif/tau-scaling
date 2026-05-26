# Tau Scaling Repair Status v2

Repo: C:\Users\jacks\OneDrive\Desktop\tau-scaling

Repair actions:
- Rewrote valid UTF-8 no-BOM pyproject.toml
- Fixed root-level file writer behavior
- Avoided Bash-style Python heredoc syntax
- Ensured package __init__.py anchors
- Reinstalled editable package
- Ran import smoke test
- Ran demo/tests according to selected switches

Quick commands:

``powershell
cd "C:\Users\jacks\OneDrive\Desktop\tau-scaling"
.\.venv\Scripts\Activate.ps1
python -m tau_scaling run-claim --seed configs\seeds\logicfolding_claim_card.json
python -m unittest discover -s tests
``

Non-claim lock:
Roadmap coherence is not validation. Simulation is not silicon evidence.