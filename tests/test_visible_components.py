from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"AGENTS": ["data_assessment_agent.py", "modeling_strategy_agent.py", "evaluation_agent.py", "reproducibility_auditor_agent.py", "deployment_handoff_agent.py"], "TOOLS": ["dataset_profiler.py", "split_validator.py", "metric_calculator.py", "artifact_hasher.py", "model_card_builder.py"], "SKILLS": ["problem_framing.py", "leakage_analysis.py", "model_selection.py", "error_analysis.py", "deployment_readiness.py"]}
def test_visible_components_exist_and_compile():
    for folder, names in EXPECTED.items():
        for name in names:
            path = ROOT / folder / name
            assert path.exists(), path
            compile(path.read_text(), str(path), "exec")
