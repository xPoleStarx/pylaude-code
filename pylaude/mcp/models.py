from __future__ import annotations

from pydantic import BaseModel, Field


class McpServerConfig(BaseModel):
    name: str
    transport: str
    enabled: bool = True
    metadata: dict[str, object] = Field(default_factory=dict)
