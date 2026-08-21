def assess_data_readiness(profile):
 q=[];r=[]
 if not profile.get("dataset"):q.append("Dataset context is missing")
 if not profile.get("splits"):r.append("Train/validation/test split strategy not supplied")
 return {**profile,"questions":q,"risks":r}
def select_model_strategy(case):
 return {"task":case.get("task"),"target":case.get("target"),"candidate_models":case.get("candidate_models",[]),"selection_criteria":case.get("selection_criteria",[])}
def evaluate_model(summary):
 q=[]
 if not summary["metrics"]:q.append("Evaluation metric definition is missing")
 if not summary["results"]:q.append("Evaluation results are missing")
 return {**summary,"questions":q}
def audit_reproducibility(meta):
 missing=[k for k,v in meta.items() if v in (None,"")]
 return {"metadata":meta,"risks":(["Missing reproducibility metadata: "+", ".join(missing)] if missing else [])}
def prepare_deployment_handoff(case):
 return {"monitoring":case.get("monitoring"),"rollback":case.get("rollback"),"owner":case.get("owner"),"deployment_constraints":case.get("deployment_constraints",[])}
SKILL_MANIFEST=["assess_data_readiness","select_model_strategy","evaluate_model","audit_reproducibility","prepare_deployment_handoff"]
