from tau_scaling.simulation.monte_carlo import run_monte_carlo
from tau_scaling.utils.safe_json import read_json

seed = read_json("configs/seeds/monte_carlo_stress_toy.json")
print(run_monte_carlo(seed["monte_carlo_stress"]))
