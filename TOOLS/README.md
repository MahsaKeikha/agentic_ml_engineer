# F31 Tools

Executable ML engineering tools live in [`src/tools/`](../src/tools/).

This layer contains deterministic operations supporting data inspection, model/evaluation artifacts, reproducibility checks, and deployment handoff. Agents select tools through domain skills rather than embedding every operation in agent prompts.

See [`src/tools/domain_tools.py`](../src/tools/domain_tools.py).