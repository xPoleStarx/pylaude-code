# Runtime Invariants

## Purpose

These are the behavior-defining invariants the Python port must preserve. No subsystem is considered migrated until the matching invariant has proof.

## Invariant Catalog

### Startup sequencing before runtime activation

- **Source files**
  - `src/entrypoints/cli.tsx`
  - `src/main.tsx`
  - `src/setup.ts`
- **Why it exists**
  - environment flags, managed settings reads, keychain prefetch, and cwd mutation all happen before the interactive runtime fully composes
- **What breaks if changed**
  - wrong tool feature flags, wrong auth or managed settings state, wrong command roots
- **Verification in Python**
  - parity fixture `tests/parity/fixtures/startup_order.json`
  - bootstrap checkpoints from `pylaude.bootstrap.pipeline`
- **Status**
  - partially verified

### Effective settings precedence chain

- **Source files**
  - `src/utils/settings/settings.ts`
  - `src/utils/settings/settingsCache.ts`
  - `src/utils/config.ts`
  - `src/utils/plugins/pluginLoader.ts`
- **Why it exists**
  - policy, plugin defaults, and local/user/project settings all feed runtime behavior
- **What breaks if changed**
  - silent policy drift, wrong tool behavior, surprising effective config
- **Verification in Python**
  - `tests/unit/test_settings_precedence.py`
  - fixture `tests/parity/fixtures/settings_precedence.json`
- **Status**
  - partially verified

### Working directory mutation timing

- **Source files**
  - `src/setup.ts`
  - `src/main.tsx`
  - `src/bootstrap/state.ts`
- **Why it exists**
  - command discovery and relative paths depend on post-setup cwd
- **What breaks if changed**
  - commands run in the wrong repo or worktree; session restore targets drift
- **Verification in Python**
  - startup-order trace plus future worktree integration fixtures
- **Status**
  - unverified

### Permission policy evaluation order

- **Source files**
  - `src/utils/permissions/permissions.ts`
  - `src/utils/permissions/permissionSetup.ts`
  - `src/utils/sandbox/sandbox-adapter.ts`
- **Why it exists**
  - security posture depends on exact allow/deny/ask resolution order
- **What breaks if changed**
  - fail-open execution or excessive false denies
- **Verification in Python**
  - `tests/unit/test_permission_policy.py`
  - fixture `tests/parity/fixtures/permission_matrix.json`
- **Status**
  - partially verified

### Transcript compatibility and resume semantics

- **Source files**
  - `src/utils/sessionStorage.ts`
  - `src/utils/sessionRestore.ts`
- **Why it exists**
  - historical sessions must remain readable without conversion by default
- **What breaks if changed**
  - resume failures, transcript corruption, user trust loss
- **Verification in Python**
  - `tests/replay/test_session_models.py`
  - fixture `tests/replay/fixtures/session_resume.json`
- **Status**
  - partially verified

### MCP/plugin merge, dedup, and invalidation

- **Source files**
  - `src/services/mcp/config.ts`
  - `src/services/mcp/client.ts`
  - `src/utils/plugins/pluginLoader.ts`
  - `src/utils/plugins/loadPluginCommands.ts`
- **Why it exists**
  - extension tools, commands, resources, and injected settings must be deterministic and fresh
- **What breaks if changed**
  - duplicated or missing tools, stale capabilities, wrong settings baseline
- **Verification in Python**
  - fixture `tests/parity/fixtures/mcp_plugin_discovery.json`
  - future reconnect and auth-expiry trace cases
- **Status**
  - unverified

### Slash command versus natural prompt routing

- **Source files**
  - `src/screens/REPL.tsx`
  - `src/utils/handlePromptSubmit.ts`
  - `src/utils/processUserInput/processUserInput.ts`
  - `src/utils/processUserInput/processSlashCommand.tsx`
- **Why it exists**
  - the same input surface routes to two different execution systems
- **What breaks if changed**
  - commands are treated as prompts or prompts are treated as commands
- **Verification in Python**
  - fixture `tests/parity/fixtures/prompt_routing.json`
  - future UI controller routing tests
- **Status**
  - unverified

### Cancellation propagation and sibling failure semantics

- **Source files**
  - `src/query.ts`
  - `src/services/tools/toolOrchestration.ts`
  - `src/services/tools/toolExecution.ts`
  - `src/services/tools/StreamingToolExecutor.ts`
- **Why it exists**
  - user-visible turn behavior depends on how parallel tool failures cancel or continue work
- **What breaks if changed**
  - hung turns, duplicated tool results, hidden partial execution
- **Verification in Python**
  - future parity traces for tool orchestration
- **Status**
  - unverified

## Migration Rule

When porting a subsystem:

1. identify the exact TS authority
2. declare the Python owner module
3. add or update a fixture or replay case
4. implement only behind that evidence
5. mark status only after proof exists
