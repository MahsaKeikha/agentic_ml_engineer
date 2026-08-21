from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class ReproducibilityAuditorAgent:
    name: str = "reproducibility_auditor_agent"
    responsibility: str = "Verify dataset, code, configuration, random seed, environment, and artifact provenance."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        required = ["data_version", "code_version", "config", "seed", "environment"]
        missing: List[str] = [k for k in required if case.get(k) in (None, "", {})]
        return {"agent": self.name, "missing": missing, "reproducible": not missing}
