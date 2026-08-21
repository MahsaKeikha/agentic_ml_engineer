# F31 Agentic ML Engineer

Standalone multi-agent reference system for reproducible machine-learning engineering from problem framing through evaluation and deployment handoff.

## Repository map

```text
.github/workflows/tests.yml   CI on Python 3.10, 3.11, 3.12
src/agents.py                 5 executable specialist agents
src/state.py                  shared run state and trace
src/gates.py                  fail-closed human handoff gate
src/orchestrator.py           multi-agent coordinator
src/system.py                 stable public API
src/run.py                    CLI / offline example
evals/evaluator.py            reference evaluation adapter
examples/ml_case.json         reproducible fixture
benchmarks/README.md          F31 benchmark contract
docs/ARCHITECTURE.md          system architecture
tests/                        behavior and architecture tests
SECURITY.md                   security policy
CONTRIBUTING.md               contribution standard
CITATION.cff                  citation metadata
CHANGELOG.md                  release history
CODE_OF_CONDUCT.md            community conduct
LICENSE                       MIT license
pyproject.toml                package metadata
```

## Multi-agent team
Data Assessment Agent, Modeling Strategy Agent, Evaluation Agent, Reproducibility Auditor, Deployment Handoff Agent, and ML Engineering Orchestrator.

```bash
python -m src.run --example
pytest -q
```

**Maturity: Reference implementation.** Production readiness requires representative data, domain validation, privacy/security review, operational testing, monitoring, and accountable human review.

AI Engineering Handbook Series by Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H
