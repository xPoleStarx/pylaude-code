from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class TranscriptEntry(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]
    content: str


class SessionTranscript(BaseModel):
    session_id: str
    entries: list[TranscriptEntry] = Field(default_factory=list)
