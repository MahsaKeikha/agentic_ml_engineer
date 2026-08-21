def dataset_profile(case):
 return {"dataset":case.get("dataset"),"splits":case.get("splits"),"data_quality":case.get("data_quality")}
def metric_summary(case):
 return {"metrics":case.get("metrics",[]),"results":case.get("evaluation_results",{}),"baseline":case.get("baseline")}
def reproducibility_fingerprint(case):
 return {k:case.get(k) for k in ("code_version","data_version","random_seed","environment")}
TOOL_MANIFEST=[{"name":"dataset_profile","side_effects":False},{"name":"metric_summary","side_effects":False},{"name":"reproducibility_fingerprint","side_effects":False}]
