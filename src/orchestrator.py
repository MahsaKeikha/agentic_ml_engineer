from .agents import build_agents
from .gates import evaluate_human_gate
from .state import RunState
SYSTEM_ID,SYSTEM_NAME,VERSION="F31","Agentic ML Engineer","0.2.0"
def run_system(case,approve=False):
 s=RunState(case);s.record("ml_engineering_orchestrator","run started",{"system_id":SYSTEM_ID,"version":VERSION})
 for a in build_agents():a.run(s)
 for e in case.get("evidence",[]):s.evidence.append({"claim":str(e.get("claim","")),"source":str(e.get("source","")),"status":str(e.get("status","supplied"))})
 s.conflicts.extend(case.get("conflicts",[]));status=evaluate_human_gate(s,approve);s.record("ml_engineering_orchestrator","handoff gate evaluated",{"approve":approve,"status":status})
 return {"system_id":SYSTEM_ID,"system_name":SYSTEM_NAME,"version":VERSION,"run_id":s.run_id,"domain":"ml_engineering","analyses":s.analyses,"evidence":s.evidence,"unresolved_questions":s.unresolved_questions,"conflicts":s.conflicts,"risks":s.risks,"recommendation":"Resolve ML engineering blockers before handoff." if status=="blocked" else "Engineering package is ready for accountable human review.","status":status,"trace":s.trace}
