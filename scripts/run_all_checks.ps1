$ErrorActionPreference = "Stop"

Write-Host "Running Tau Scaling checks..." -ForegroundColor Cyan
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python -m unittest discover -s tests
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
Write-Host "All Tau Scaling checks completed." -ForegroundColor Green