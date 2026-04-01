from pylaude.sessions.models import SessionTranscript, TranscriptEntry


def test_session_transcript_preserves_entry_order() -> None:
    transcript = SessionTranscript(
        session_id="s1",
        entries=[
            TranscriptEntry(role="user", content="hi"),
            TranscriptEntry(role="assistant", content="hello"),
        ],
    )
    assert [entry.role for entry in transcript.entries] == ["user", "assistant"]
