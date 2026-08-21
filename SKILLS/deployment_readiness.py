from typing import Any, Dict, List

def deployment_readiness(case: Dict[str, Any]) -> Dict[str, Any]:
    required = ["model_card", "monitoring_plan", "rollback_owner", "approval_owner"]
    missing: List[str] = [k for k in required if not case.get(k)]
    return {"missing": missing, "ready": not missing}
