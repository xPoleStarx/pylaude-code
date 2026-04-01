from __future__ import annotations

from pydantic import BaseModel, Field


class PluginManifest(BaseModel):
    name: str
    root: str
    settings: dict[str, object] = Field(default_factory=dict)
