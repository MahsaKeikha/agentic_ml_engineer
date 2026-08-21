def evaluate_result(r):
 return {"has_evaluation":bool(r.get("analyses",{}).get("evaluation")),"has_reproducibility":bool(r.get("analyses",{}).get("reproducibility")),"trace_steps":len(r.get("trace",[])),"blocked":r.get("status")=="blocked"}
