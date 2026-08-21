from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class ModelCardBuilder:
    def build(self, case: Dict[str, Any]) -> Dict[str, Any]:
        return {"model_name": case.get("model_name"), "intended_use": case.get("intended_use"), "data_version": case.get("data_version"), "metrics": dict(case.get("metrics", {})), "limitations": list(case.get("limitations", []))}
