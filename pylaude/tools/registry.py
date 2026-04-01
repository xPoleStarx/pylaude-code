from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ToolDescriptor:
    name: str
    authority: str
    python_owner: str
