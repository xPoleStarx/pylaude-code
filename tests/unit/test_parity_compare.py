from pylaude.runtime.parity import compare_exact, compare_normalized_text


def test_compare_exact_matches_equal_values() -> None:
    ok, message = compare_exact({"a": 1}, {"a": 1})
    assert ok is True
    assert message == ""


def test_compare_normalized_text_ignores_whitespace_only_drift() -> None:
    ok, message = compare_normalized_text("a   b\nc", "a b c")
    assert ok is True
    assert message == ""
