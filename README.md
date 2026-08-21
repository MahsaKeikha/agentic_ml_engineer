# F31 Agentic ML Engineer

Standalone multi-agent reference system for reproducible machine-learning engineering from problem framing through evaluation and deployment handoff.

## Agent team

- Data Assessment Agent
- Modeling Strategy Agent
- Evaluation Agent
- Reproducibility Auditor
- Deployment Handoff Agent
- ML Engineering Orchestrator

The agents coordinate through explicit shared state and produce a traceable engineering package rather than a single opaque recommendation.

## Quick start

```bash
python -m src.run --example
pytest -q
```

## Engineering gates

A clean handoff requires supplied dataset context, target/metric definition, evaluation evidence, reproducibility metadata, and no unresolved conflicts. Human approval cannot erase missing evidence.

## Maturity

**Reference implementation.** It does not claim that a model is production-ready without domain validation, representative data, security/privacy review, operational testing, monitoring, and accountable human review.

## AI Engineering Handbook Series

By Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H

MIT licensed.
