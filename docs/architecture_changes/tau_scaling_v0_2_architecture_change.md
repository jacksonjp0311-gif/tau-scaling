# Architecture Change — Tau Scaling v0.2

Change: add RCC-N / OMN-style repository structure and documentation context.

Runtime behavior: unchanged except validation/checker scripts and mirrored output surfaces.

Required validation:

    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py
    python -m unittest discover -s tests