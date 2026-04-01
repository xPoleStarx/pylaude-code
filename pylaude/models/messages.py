from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class MessageEnvelope(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]
    text: str
