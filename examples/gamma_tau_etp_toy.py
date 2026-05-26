from tau_scaling.gates.gamma_tau_etp import gamma_tau_etp
from tau_scaling.utils.safe_json import read_json

record = read_json("configs/seeds/gamma_tau_etp_toy.json")
print({"gamma_tau_ETP": gamma_tau_etp(record)})
