AUTHORITATIVE_TS_FILES = {
    "startup": [
        "src/entrypoints/cli.tsx",
        "src/main.tsx",
        "src/setup.ts",
    ],
    "interactive_controller": [
        "src/replLauncher.tsx",
        "src/screens/REPL.tsx",
        "src/utils/handlePromptSubmit.ts",
        "src/utils/processUserInput/processUserInput.ts",
        "src/utils/processUserInput/processSlashCommand.tsx",
    ],
    "query_runtime": [
        "src/query.ts",
        "src/services/tools/toolOrchestration.ts",
        "src/services/tools/toolExecution.ts",
        "src/services/tools/StreamingToolExecutor.ts",
        "src/services/api/claude.ts",
    ],
    "settings": [
        "src/utils/config.ts",
        "src/utils/settings/settings.ts",
        "src/utils/settings/settingsCache.ts",
    ],
    "permissions": [
        "src/utils/permissions/permissions.ts",
        "src/utils/permissions/permissionSetup.ts",
        "src/utils/sandbox/sandbox-adapter.ts",
    ],
    "sessions": [
        "src/utils/sessionStorage.ts",
        "src/utils/sessionRestore.ts",
    ],
    "extensions": [
        "src/services/mcp/config.ts",
        "src/services/mcp/client.ts",
        "src/utils/plugins/pluginLoader.ts",
        "src/utils/plugins/loadPluginCommands.ts",
    ],
}
