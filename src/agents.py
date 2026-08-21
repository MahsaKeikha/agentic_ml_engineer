"""Specialist agents for F31 Agentic ML Engineer."""
from typing import Any


class BaseAgent:
    name = "agent"
    responsibility = ""
    def run(self, state: Any) -> None:
        raise NotImplementedError


class DataAssessmentAgent(BaseAgent):
    name = "data_assessment"
    responsibility = "Assess dataset context, split strategy, quality, leakage, and suitability."
    def run(self, s):
        x={"dataset":s.case.get("dataset"),"splits":s.case.get("splits"),"data_quality":s.case.get("data_quality"),"leakage_review":s.case.get("leakage_review")}
        s.analyses[self.name]=x
        if not x["dataset"]: s.unresolved_questions.append("Dataset context is missing")
        if not x["splits"]: s.risks.append("Train/validation/test split strategy not supplied")
        s.record(self.name,"assessed data context",x)


class ModelingStrategyAgent(BaseAgent):
    name = "modeling_strategy"
    responsibility = "Define task, target, baselines, candidates, constraints, and model-selection rationale."
    def run(self,s):
        x={"task":s.case.get("task"),"target":s.case.get("target"),"candidate_models":s.case.get("candidate_models",[]),"constraints":s.case.get("constraints",[])}
        s.analyses[self.name]=x
        if not x["target"]: s.unresolved_questions.append("Target definition is missing")
        if not x["candidate_models"]: s.risks.append("No candidate or baseline models supplied")
        s.record(self.name,"prepared modeling strategy",x)


class EvaluationAgent(BaseAgent):
    name = "evaluation"
    responsibility = "Review metrics, benchmark results, robustness, subgroup checks, and acceptance thresholds."
    def run(self,s):
        x={"metrics":s.case.get("metrics",[]),"results":s.case.get("evaluation_results",{}),"thresholds":s.case.get("acceptance_thresholds",{}),"robustness":s.case.get("robustness_results",{})}
        s.analyses[self.name]=x
        if not x["metrics"]: s.unresolved_questions.append("Evaluation metric definition is missing")
        if not x["results"]: s.unresolved_questions.append("Evaluation results are missing")
        s.record(self.name,"reviewed evaluation evidence",x)


class ReproducibilityAuditor(BaseAgent):
    name = "reproducibility"
    responsibility = "Audit code, data, seed, environment, feature, and experiment provenance."
    def run(self,s):
        keys=["code_version","data_version","random_seed","environment"]
        x={k:s.case.get(k) for k in keys}
        s.analyses[self.name]=x
        missing=[k for k,v in x.items() if v in (None,"")]
        if missing: s.risks.append("Missing reproducibility metadata: "+", ".join(missing))
        s.record(self.name,"audited reproducibility",x)


class DeploymentHandoffAgent(BaseAgent):
    name = "deployment_handoff"
    responsibility = "Prepare monitoring, rollback, ownership, model-card, and deployment-readiness handoff."
    def run(self,s):
        x={"monitoring":s.case.get("monitoring"),"rollback":s.case.get("rollback"),"owner":s.case.get("owner"),"model_card":s.case.get("model_card")}
        s.analyses[self.name]=x
        if not x["owner"]: s.unresolved_questions.append("Deployment/accountability owner is missing")
        if not x["rollback"]: s.risks.append("Rollback plan is missing")
        s.record(self.name,"prepared deployment handoff",x)


def build_agents():
    return [DataAssessmentAgent(),ModelingStrategyAgent(),EvaluationAgent(),ReproducibilityAuditor(),DeploymentHandoffAgent()]

AGENT_MANIFEST=[{"name":c.name,"responsibility":c.responsibility} for c in [DataAssessmentAgent,ModelingStrategyAgent,EvaluationAgent,ReproducibilityAuditor,DeploymentHandoffAgent]]
