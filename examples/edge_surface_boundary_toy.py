from tau_scaling.gates.edge_surface import edge_surface_ratio
from tau_scaling.utils.safe_json import read_json

record = read_json("configs/seeds/edge_surface_boundary_toy.json")
print(edge_surface_ratio(record))
