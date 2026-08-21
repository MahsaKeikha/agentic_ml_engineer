from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class DeploymentHandoffAgent:
    name: str = "deployment_handoff_agent"
    responsibility: str = "Prepare a controlled handoff with model card, monitoring expectations, rollback owner, and approval evidence."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        required = ["model_card", "monitoring_plan", "rollback_owner"]
        missing: List[str] = [k for k in required if not case.get(k)]
        return {"agent": self.name, "missing": missing, "ready_for_human_handoff": not missing}
