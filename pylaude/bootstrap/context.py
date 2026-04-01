from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class BootstrapContext:
    """Startup state shared across Python bootstrap phases.

    This is the one allowed singleton-shaped container for startup parity.
    It replaces the Node/Bun import-time mutation pattern with an explicit
    object that records side effects and the order they were applied.
    """

    cwd: Path
    argv: list[str]
    env: dict[str, str]
    feature_flags: dict[str, bool] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)
    state: dict[str, Any] = field(default_factory=dict)

    def checkpoint(self, name: str) -> None:
        self.notes.append(name)
