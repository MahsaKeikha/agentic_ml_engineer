from typing import Any, Dict, Iterable

def model_selection(candidates: Iterable[Dict[str, Any]], metric: str) -> Dict[str, Any]:
    items = list(candidates)
    if not items:
        return {"selected": None, "reason": "no candidates"}
    best = max(items, key=lambda x: float(x.get("metrics", {}).get(metric, float('-inf'))))
    return {"selected": best.get("name"), "metric": metric, "value": best.get("metrics", {}).get(metric)}
