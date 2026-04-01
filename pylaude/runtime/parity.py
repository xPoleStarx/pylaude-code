from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json_fixture(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def compare_exact(actual: Any, expected: Any) -> tuple[bool, str]:
    if actual == expected:
        return True, ""
    return False, f"expected {expected!r}, got {actual!r}"


def compare_normalized_text(actual: str, expected: str) -> tuple[bool, str]:
    normalized_actual = " ".join(actual.split())
    normalized_expected = " ".join(expected.split())
    if normalized_actual == normalized_expected:
        return True, ""
    return False, f"expected normalized {normalized_expected!r}, got {normalized_actual!r}"
