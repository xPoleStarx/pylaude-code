from __future__ import annotations

from enum import StrEnum


class SettingSource(StrEnum):
    DEFAULTS = "defaults"
    PLUGIN_BASE = "pluginBase"
    USER = "user"
    PROJECT = "project"
    LOCAL = "local"
    POLICY = "policySettings"
    CLI = "cli"


# Ordered low to high priority.
SETTINGS_PRECEDENCE: tuple[SettingSource, ...] = (
    SettingSource.DEFAULTS,
    SettingSource.PLUGIN_BASE,
    SettingSource.USER,
    SettingSource.PROJECT,
    SettingSource.LOCAL,
    SettingSource.POLICY,
    SettingSource.CLI,
)
