from typing import Any
from .base import BaseAgent
from ..skills import assess_data_readiness, select_model_strategy, evaluate_model, audit_reproducibility, prepare_deployment_handoff
from ..tools import dataset_profile, metric_summary, reproducibility_fingerprint

class DataAssessmentAgent(BaseAgent):
 name="data_assessment";responsibility="Assess dataset context, split strategy and quality.";required_skills=("assess_data_readiness",);allowed_tools=("dataset_profile",)
 def run(self,s:Any):
  a=assess_data_readiness(dataset_profile(s.case));s.analyses[self.name]=a;s.unresolved_questions.extend(a["questions"]);s.risks.extend(a["risks"]);s.record(self.name,"assessed data readiness",a)
class ModelingStrategyAgent(BaseAgent):
 name="modeling_strategy";responsibility="Frame task, target, baselines and candidate model strategy.";required_skills=("select_model_strategy",);allowed_tools=()
 def run(self,s:Any):
  a=select_model_strategy(s.case);s.analyses[self.name]=a
  if not a["target"]:s.unresolved_questions.append("Target definition is missing")
  s.record(self.name,"prepared modeling strategy",a)
class EvaluationAgent(BaseAgent):
 name="evaluation";responsibility="Evaluate model evidence against explicit metrics and baselines.";required_skills=("evaluate_model",);allowed_tools=("metric_summary",)
 def run(self,s:Any):
  a=evaluate_model(metric_summary(s.case));s.analyses[self.name]=a;s.unresolved_questions.extend(a["questions"]);s.record(self.name,"evaluated model evidence",a)
class ReproducibilityAuditor(BaseAgent):
 name="reproducibility";responsibility="Audit code, data, seed and environment provenance.";required_skills=("audit_reproducibility",);allowed_tools=("reproducibility_fingerprint",)
 def run(self,s:Any):
  a=audit_reproducibility(reproducibility_fingerprint(s.case));s.analyses[self.name]=a;s.risks.extend(a["risks"]);s.record(self.name,"audited reproducibility",a)
class DeploymentHandoffAgent(BaseAgent):
 name="deployment_handoff";responsibility="Prepare monitoring, rollback and accountable ownership handoff.";required_skills=("prepare_deployment_handoff",);allowed_tools=()
 def run(self,s:Any):
  a=prepare_deployment_handoff(s.case);s.analyses[self.name]=a
  if not a["owner"]:s.unresolved_questions.append("Deployment/accountability owner is missing")
  s.record(self.name,"prepared deployment handoff",a)
CLASSES=[DataAssessmentAgent,ModelingStrategyAgent,EvaluationAgent,ReproducibilityAuditor,DeploymentHandoffAgent]
def build_agents():return [c() for c in CLASSES]
AGENT_MANIFEST=[{"name":c.name,"responsibility":c.responsibility,"skills":list(c.required_skills),"tools":list(c.allowed_tools)} for c in CLASSES]
