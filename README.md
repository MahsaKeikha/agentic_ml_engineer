# F31 Agentic ML Engineer

Standalone multi-agent reference system for reproducible machine-learning engineering from problem framing through evaluation and deployment handoff.

## Architecture

```text
src/
├── agents/          executable ML specialist agents
├── tools/           deterministic ML inspection/build helpers
├── skills/          reusable ML engineering procedures
├── memory/          experiment memory abstraction
├── schemas/         canonical evidence contracts
├── prompts/         engineering principles
├── config/          reference configuration
├── safety/          release/handoff policy
├── observability/   trace summaries
├── state.py         shared run state
├── gates.py         fail-closed human handoff gate
├── orchestrator.py  multi-agent coordinator
├── system.py        public API
└── run.py           offline CLI example
```

### Agents
Data Assessment Agent, Modeling Strategy Agent, Evaluation Agent, Reproducibility Auditor, Deployment Handoff Agent, coordinated by the ML Engineering Orchestrator.

### Skills
Data-readiness assessment, model-strategy selection, model evaluation, reproducibility audit, deployment handoff preparation.

### Tools
Dataset profiling, metric summarization, reproducibility fingerprinting.

See `docs/AGENTS_TOOLS_SKILLS.md`.

```bash
python -m src.run --example
pytest -q
```

**Maturity: Reference implementation.** Production readiness requires representative data, domain validation, privacy/security review, operational testing, monitoring, and accountable human review.

AI Engineering Handbook Series by Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H
