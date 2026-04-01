from pylaude.settings.precedence import build_effective_settings
from pylaude.settings.sources import SettingSource


def test_plugin_base_is_lower_priority_than_user_and_policy() -> None:
    effective = build_effective_settings(
        {
            SettingSource.PLUGIN_BASE: {"theme": "plugin", "safe": False},
            SettingSource.USER: {"theme": "user"},
            SettingSource.POLICY: {"safe": True},
        }
    )
    assert effective.values["theme"] == "user"
    assert effective.values["safe"] is True
    assert effective.provenance["theme"] is SettingSource.USER
    assert effective.provenance["safe"] is SettingSource.POLICY
