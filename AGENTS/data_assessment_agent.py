from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class DataAssessmentAgent:
    name: str = "data_assessment_agent"
    responsibility: str = "Assess dataset fitness, target definition, leakage risk, missingness, and representativeness."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        data = case.get("dataset", {})
        return {"agent": self.name, "rows": int(data.get("rows", 0)), "features": list(data.get("features", [])), "target": data.get("target"), "ready": bool(data.get("rows") and data.get("target"))}
