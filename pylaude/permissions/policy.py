from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel


class Decision(StrEnum):
    ALLOW = "allow"
    DENY = "deny"
    ASK = "ask"


class PermissionCase(BaseModel):
    tool_name: str
    matched_deny_rule: bool = False
    matched_allow_rule: bool = False
    requires_user_confirmation: bool = False


def evaluate_case(case: PermissionCase) -> Decision:
    """Conservative default aligned with the TS migration contract.

    The full TypeScript permission graph is not ported yet. This function
    exists so the Python side starts from fail-closed semantics instead of
    optimistic placeholder behavior.
    """

    if case.matched_deny_rule:
        return Decision.DENY
    if case.matched_allow_rule and not case.requires_user_confirmation:
        return Decision.ALLOW
    return Decision.ASK


def evaluate_cases(cases: list[PermissionCase]) -> list[Decision]:
    return [evaluate_case(case) for case in cases]
