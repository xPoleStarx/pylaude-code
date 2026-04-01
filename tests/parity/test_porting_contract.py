from pathlib import Path

from pylaude.runtime.trace_manifest import build_default_manifest


ROOT = Path(__file__).resolve().parents[2]


def test_trace_manifest_covers_critical_subsystems() -> None:
    manifest = build_default_manifest()
    names = {scenario.name for scenario in manifest.scenarios}
    assert {
        "startup_order",
        "prompt_routing",
        "settings_precedence",
        "permission_matrix",
        "session_resume",
        "mcp_plugin_discovery",
    }.issubset(names)


def test_porting_docs_no_longer_contain_tbd_tables() -> None:
    docs = [
        ROOT / "docs" / "porting" / "architecture-map.md",
        ROOT / "docs" / "porting" / "invariants.md",
        ROOT / "docs" / "porting" / "parity-matrix.md",
    ]
    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        assert "TBD" not in text
