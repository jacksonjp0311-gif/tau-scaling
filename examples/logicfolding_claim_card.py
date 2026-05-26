from tau_scaling.core.runtime import TauScalingRuntime
from tau_scaling.utils.safe_json import read_json

seed = read_json("configs/seeds/logicfolding_claim_card.json")
result = TauScalingRuntime(".").run(seed)
print(result)
