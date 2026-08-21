from src.system import run_system

def case():
 return {"dataset":"d","splits":"train/val/test","data_quality":"checked","task":"classification","target":"y","candidate_models":["baseline"],"metrics":["accuracy"],"evaluation_results":{"accuracy":0.9},"code_version":"1","data_version":"1","random_seed":1,"environment":"py","monitoring":"metric","rollback":"prior","owner":"team","evidence":[{"claim":"accuracy=.9","source":"fixture","status":"supplied"}]}
def test_clean_waits_for_human():assert run_system(case())["status"]=="awaiting_human_approval"
def test_clean_can_be_approved():assert run_system(case(),True)["status"]=="approved_for_human_follow_through"
def test_missing_eval_blocks_approval():
 c=case();c["evaluation_results"]={};assert run_system(c,True)["status"]=="blocked"
def test_missing_repro_metadata_blocks():
 c=case();c["random_seed"]=None;assert run_system(c,True)["status"]=="blocked"
