from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class EvaluationAgent:
    name: str = "evaluation_agent"
    responsibility: str = "Evaluate candidate models against declared metrics, slices, thresholds, and uncertainty."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        metrics = dict(case.get("metrics", {}))
        thresholds = dict(case.get("thresholds", {}))
        failed = [m for m, t in thresholds.items() if float(metrics.get(m, float('-inf'))) < float(t)]
        return {"agent": self.name, "metrics": metrics, "thresholds": thresholds, "failed": failed, "pass": not failed and bool(metrics)}
