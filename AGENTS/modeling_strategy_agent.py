from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class ModelingStrategyAgent:
    name: str = "modeling_strategy_agent"
    responsibility: str = "Design baselines, candidate model families, validation strategy, and selection criteria."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        task = case.get("task_type", "unknown")
        candidates = case.get("candidate_models", ["baseline"])
        return {"agent": self.name, "task_type": task, "candidates": candidates, "selection_metric": case.get("primary_metric")}
