from pathlib import Path

from pylaude.bootstrap import BootstrapContext, default_bootstrap_pipeline


def test_bootstrap_pipeline_records_checkpoints_in_order() -> None:
    context = BootstrapContext(cwd=Path("."), argv=[], env={})
    result = default_bootstrap_pipeline().run(context)
    assert result.notes == [
        "env_defaults",
        "resolve_initial_paths",
        "initialize_settings",
        "register_extensions",
        "prepare_runtime",
    ]
