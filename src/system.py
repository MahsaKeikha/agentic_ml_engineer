from dataclasses import dataclass, field
from typing import Any, Dict, List
from uuid import uuid4

SYSTEM_ID, SYSTEM_NAME, VERSION = "F31", "Agentic ML Engineer", "0.1.0"

@dataclass
class State:
    case: Dict[str, Any]
    run_id: str = field(default_factory=lambda: str(uuid4()))
    analyses: Dict[str, Any] = field(default_factory=dict)
    evidence: List[Dict[str, str]] = field(default_factory=list)
    unresolved_questions: List[str] = field(default_factory=list)
    conflicts: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    trace: List[Dict[str, Any]] = field(default_factory=list)
    def record(self, actor, event, artifact=None):
        self.trace.append({"step": len(self.trace)+1, "actor": actor, "event": event, "artifact": artifact})

class DataAssessmentAgent:
    name="data_assessment"
    def run(self,s):
        data=s.case.get("dataset")
        s.analyses[self.name]={"dataset":data,"splits":s.case.get("splits"),"data_quality":s.case.get("data_quality")}
        if not data: s.unresolved_questions.append("Dataset context is missing")
        if not s.case.get("splits"): s.risks.append("Train/validation/test split strategy not supplied")
        s.record(self.name,"assessed data context",s.analyses[self.name])

class ModelingStrategyAgent:
    name="modeling_strategy"
    def run(self,s):
        s.analyses[self.name]={"task":s.case.get("task"),"target":s.case.get("target"),"candidate_models":s.case.get("candidate_models",[])}
        if not s.case.get("target"): s.unresolved_questions.append("Target definition is missing")
        s.record(self.name,"prepared modeling strategy",s.analyses[self.name])

class EvaluationAgent:
    name="evaluation"
    def run(self,s):
        metrics=s.case.get("metrics",[]); results=s.case.get("evaluation_results",{})
        s.analyses[self.name]={"metrics":metrics,"results":results}
        if not metrics: s.unresolved_questions.append("Evaluation metric definition is missing")
        if not results: s.unresolved_questions.append("Evaluation results are missing")
        s.record(self.name,"reviewed evaluation evidence",s.analyses[self.name])

class ReproducibilityAuditor:
    name="reproducibility"
    def run(self,s):
        meta={k:s.case.get(k) for k in ["code_version","data_version","random_seed","environment"]}
        s.analyses[self.name]=meta
        missing=[k for k,v in meta.items() if v in (None,"")]
        if missing: s.risks.append("Missing reproducibility metadata: "+", ".join(missing))
        s.record(self.name,"audited reproducibility",meta)

class DeploymentHandoffAgent:
    name="deployment_handoff"
    def run(self,s):
        s.analyses[self.name]={"monitoring":s.case.get("monitoring"),"rollback":s.case.get("rollback"),"owner":s.case.get("owner")}
        if not s.case.get("owner"): s.unresolved_questions.append("Deployment/accountability owner is missing")
        s.record(self.name,"prepared deployment handoff",s.analyses[self.name])

AGENTS=[DataAssessmentAgent(),ModelingStrategyAgent(),EvaluationAgent(),ReproducibilityAuditor(),DeploymentHandoffAgent()]

def run_system(case:Dict[str,Any],approve:bool=False)->Dict[str,Any]:
    s=State(case); s.record("orchestrator","run started",{"system_id":SYSTEM_ID,"version":VERSION})
    for a in AGENTS:a.run(s)
    for e in case.get("evidence",[]): s.evidence.append({"claim":str(e.get("claim","")),"source":str(e.get("source","")),"status":str(e.get("status","supplied"))})
    s.conflicts.extend(case.get("conflicts",[]))
    blockers=bool(s.unresolved_questions or s.conflicts or s.risks)
    status="approved_for_human_follow_through" if approve and not blockers else "blocked" if blockers else "awaiting_human_approval"
    rec="Resolve ML engineering blockers before handoff." if blockers else "Engineering package is ready for accountable human review."
    s.record("orchestrator","handoff gate evaluated",{"approve":approve,"blockers":blockers,"status":status})
    return {"system_id":SYSTEM_ID,"system_name":SYSTEM_NAME,"version":VERSION,"run_id":s.run_id,"domain":"ml_engineering","analyses":s.analyses,"evidence":s.evidence,"unresolved_questions":s.unresolved_questions,"conflicts":s.conflicts,"risks":s.risks,"recommendation":rec,"status":status,"trace":s.trace}
