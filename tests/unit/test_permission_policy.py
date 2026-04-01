from pylaude.permissions.policy import Decision, PermissionCase, evaluate_case


def test_deny_beats_allow() -> None:
    decision = evaluate_case(
        PermissionCase(
            tool_name="bash",
            matched_deny_rule=True,
            matched_allow_rule=True,
        )
    )
    assert decision is Decision.DENY


def test_ask_is_default_fail_closed_mode() -> None:
    decision = evaluate_case(PermissionCase(tool_name="bash"))
    assert decision is Decision.ASK
