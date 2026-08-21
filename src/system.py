from dataclasses import dataclass, field
from typing import Any, Dict, List
from uuid import uuid4
from .agents import build_agents

SYSTEM_ID, SYSTEM_NAME, VERSION = "F31", "Agentic ML Engineer", "0.2.0"

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

def run_system(case:Dict[str,Any],approve:bool=False)->Dict[str,Any]:
    s=State(case)
    s.record("ml_engineering_orchestrator","run started",{"system_id":SYSTEM_ID,"version":VERSION})
    for a in build_agents(): a.run(s)
    for e in case.get("evidence",[]): s.evidence.append({"claim":str(e.get("claim","")),"source":str(e.get("source","")),"status":str(e.get("status","supplied"))})
    s.conflicts.extend(case.get("conflicts",[]))
    blockers=bool(s.unresolved_questions or s.conflicts or s.risks)
    status="approved_for_human_follow_through" if approve and not blockers else "blocked" if blockers else "awaiting_human_approval"
    rec="Resolve ML engineering blockers before handoff." if blockers else "Engineering package is ready for accountable human review."
    s.record("ml_engineering_orchestrator","handoff gate evaluated",{"approve":approve,"blockers":blockers,"status":status})
    return {"system_id":SYSTEM_ID,"system_name":SYSTEM_NAME,"version":VERSION,"run_id":s.run_id,"domain":"ml_engineering","analyses":s.analyses,"evidence":s.evidence,"unresolved_questions":s.unresolved_questions,"conflicts":s.conflicts,"risks":s.risks,"recommendation":rec,"status":status,"trace":s.trace}
