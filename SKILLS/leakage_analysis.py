from typing import Any, Dict, List

def leakage_analysis(case: Dict[str, Any]) -> Dict[str, Any]:
    suspects: List[str] = list(case.get("leakage_suspects", []))
    if not case.get("split", {}).get("temporal_leakage_checked", False) and case.get("time_dependent"):
        suspects.append("Temporal leakage not checked")
    return {"suspects": suspects, "clear": not suspects}
