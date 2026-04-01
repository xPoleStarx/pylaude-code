from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class UiController:
    """Thin future home for the REPL controller.

    The real control flow still lives in TypeScript. This controller exists so
    the Python side has an explicit ownership boundary from the start.
    """

    notifications: list[str] = field(default_factory=list)
    dialogs: list[str] = field(default_factory=list)
    message_queue: list[str] = field(default_factory=list)

    def snapshot(self) -> dict[str, list[str]]:
        return {
            "notifications": list(self.notifications),
            "dialogs": list(self.dialogs),
            "message_queue": list(self.message_queue),
        }
