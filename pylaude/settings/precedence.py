from __future__ import annotations

from collections.abc import Mapping

from pydantic import BaseModel, Field

from pylaude.settings.sources import SETTINGS_PRECEDENCE, SettingSource


class EffectiveSettings(BaseModel):
    values: dict[str, object] = Field(default_factory=dict)
    provenance: dict[str, SettingSource] = Field(default_factory=dict)


def build_effective_settings(
    settings_by_source: Mapping[SettingSource, Mapping[str, object]],
) -> EffectiveSettings:
    values: dict[str, object] = {}
    provenance: dict[str, SettingSource] = {}
    for source in SETTINGS_PRECEDENCE:
        for key, value in settings_by_source.get(source, {}).items():
            values[key] = value
            provenance[key] = source
    return EffectiveSettings(values=values, provenance=provenance)
