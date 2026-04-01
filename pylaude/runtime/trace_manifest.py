from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


Comparator = Literal["exact", "normalized", "rule_based"]


class TraceScenario(BaseModel):
    name: str
    ts_authorities: list[str]
    comparator: Comparator
    fixture: str
    python_owner: str
    status: Literal["planned", "in_progress", "pass", "drift", "blocked"] = "planned"
    notes: str = ""


class TraceManifest(BaseModel):
    version: int = 1
    scenarios: list[TraceScenario] = Field(default_factory=list)


def build_default_manifest() -> TraceManifest:
    return TraceManifest(
        scenarios=[
            TraceScenario(
                name="startup_order",
                ts_authorities=["src/entrypoints/cli.tsx", "src/main.tsx", "src/setup.ts"],
                comparator="exact",
                fixture="tests/parity/fixtures/startup_order.json",
                python_owner="pylaude.bootstrap",
            ),
            TraceScenario(
                name="prompt_routing",
                ts_authorities=[
                    "src/screens/REPL.tsx",
                    "src/utils/handlePromptSubmit.ts",
                    "src/utils/processUserInput/processUserInput.ts",
                    "src/utils/processUserInput/processSlashCommand.tsx",
                ],
                comparator="exact",
                fixture="tests/parity/fixtures/prompt_routing.json",
                python_owner="pylaude.ui",
            ),
            TraceScenario(
                name="settings_precedence",
                ts_authorities=[
                    "src/utils/config.ts",
                    "src/utils/settings/settings.ts",
                    "src/utils/settings/settingsCache.ts",
                ],
                comparator="exact",
                fixture="tests/parity/fixtures/settings_precedence.json",
                python_owner="pylaude.settings",
            ),
            TraceScenario(
                name="permission_matrix",
                ts_authorities=[
                    "src/utils/permissions/permissions.ts",
                    "src/utils/permissions/permissionSetup.ts",
                    "src/utils/sandbox/sandbox-adapter.ts",
                ],
                comparator="exact",
                fixture="tests/parity/fixtures/permission_matrix.json",
                python_owner="pylaude.permissions",
            ),
            TraceScenario(
                name="session_resume",
                ts_authorities=[
                    "src/utils/sessionStorage.ts",
                    "src/utils/sessionRestore.ts",
                ],
                comparator="exact",
                fixture="tests/replay/fixtures/session_resume.json",
                python_owner="pylaude.sessions",
            ),
            TraceScenario(
                name="mcp_plugin_discovery",
                ts_authorities=[
                    "src/services/mcp/config.ts",
                    "src/services/mcp/client.ts",
                    "src/utils/plugins/pluginLoader.ts",
                    "src/utils/plugins/loadPluginCommands.ts",
                ],
                comparator="exact",
                fixture="tests/parity/fixtures/mcp_plugin_discovery.json",
                python_owner="pylaude.mcp",
            ),
        ]
    )
