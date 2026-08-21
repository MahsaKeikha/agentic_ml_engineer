import argparse,json
from .system import run_system
EXAMPLE={"dataset":"customer_churn_v3","splits":"time-aware 70/15/15","data_quality":"validated fixture","task":"binary classification","target":"churn_30d","candidate_models":["logistic regression","gradient boosting"],"metrics":["AUROC","calibration"],"evaluation_results":{"AUROC":0.84,"calibration":"reviewed"},"code_version":"abc123","data_version":"v3","random_seed":42,"environment":"python-3.12","monitoring":"drift and performance","rollback":"retain prior model","owner":"ML platform team","evidence":[{"claim":"AUROC=0.84","source":"offline evaluation fixture","status":"supplied"}]}
def main():
 p=argparse.ArgumentParser();p.add_argument("--example",action="store_true");p.add_argument("--approve",action="store_true");a=p.parse_args();print(json.dumps(run_system(EXAMPLE if a.example else {},a.approve),indent=2))
if __name__=="__main__":main()
