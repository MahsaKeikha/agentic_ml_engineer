from typing import Any, Dict

def problem_framing(case: Dict[str, Any]) -> Dict[str, Any]:
    return {"task_type": case.get("task_type"), "target": case.get("dataset", {}).get("target"), "primary_metric": case.get("primary_metric"), "decision_context": case.get("decision_context")}
