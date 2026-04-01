# Architecture Map

## Purpose

This document records the real execution authorities that the Python port must preserve.
It is not a folder summary. It is the migration control-plane map.

## Authoritative Files

| Subsystem | Authoritative files | Why authoritative | Confidence |
|---|---|---|---|
| Startup/composition | `src/entrypoints/cli.tsx`, `src/main.tsx`, `src/setup.ts` | Own startup order, feature-gated entrypaths, cwd/worktree mutation, initial plugin/skill/MCP registration | High |
| Query/runtime loop | `src/query.ts`, `src/services/tools/toolOrchestration.ts`, `src/services/tools/toolExecution.ts`, `src/services/tools/StreamingToolExecutor.ts`, `src/services/api/claude.ts` | Own model request shaping, tool execution, streaming, cancellations, and partial failure behavior | High |
| CLI/REPL controller | `src/replLauncher.tsx`, `src/screens/REPL.tsx`, `src/utils/handlePromptSubmit.ts`, `src/utils/processUserInput/processUserInput.ts`, `src/utils/processUserInput/processSlashCommand.tsx` | Own input capture, routing, event loop integration, queueing, and interactive UX behavior | High |
| Permissions/sandbox | `src/utils/permissions/permissions.ts`, `src/utils/permissions/permissionSetup.ts`, `src/utils/sandbox/sandbox-adapter.ts`, `src/hooks/useCanUseTool.tsx` | Own allow/deny/ask policy, dangerous-command handling, and sandbox runtime shape | High |
| Session persistence | `src/utils/sessionStorage.ts`, `src/utils/sessionRestore.ts`, `src/bootstrap/state.ts` | Define transcript compatibility, append/rewrite semantics, metadata recovery, and resume reconstruction | High |
| MCP/plugin lifecycle | `src/services/mcp/config.ts`, `src/services/mcp/client.ts`, `src/utils/plugins/pluginLoader.ts`, `src/utils/plugins/loadPluginCommands.ts` | Own discovery, dedup, cache invalidation, plugin settings injection, and extension command loading | High |
| Config/settings | `src/utils/config.ts`, `src/utils/settings/settings.ts`, `src/utils/settings/settingsCache.ts` | Own effective runtime settings, precedence, and mutation/persistence rules | High |

## Startup Order Map

1. Entry command enters through `src/entrypoints/cli.tsx`.
   - Side effects: environment flags are mutated before later imports.
   - Dependency: import-time tool constants already depend on env.
   - Failure mode: wrong env at import time changes tool behavior.
2. Heavy startup shifts into `src/main.tsx`.
   - Side effects: MDM reads and keychain prefetch start at module import time.
   - Dependency: those side effects happen before most of the app graph loads.
   - Failure mode: startup latency or stale managed settings/auth state.
3. Runtime setup passes through `src/setup.ts`.
   - Side effects: process cwd may be rewritten for worktree mode.
   - Dependency: command/plugin discovery after this point depends on mutated cwd.
   - Failure mode: wrong command roots, wrong relative path semantics.
4. Skills, plugins, commands, tools, and MCP clients are composed in `src/main.tsx`.
   - Side effects: registries are filtered by feature flags, settings, and policy.
   - Dependency: setup, config, auth, and plugin seed directories must already be established.
   - Failure mode: missing commands/tools or wrong extension set.
5. Interactive app launches through `src/replLauncher.tsx` and `src/screens/REPL.tsx`.
   - Side effects: hooks establish background pollers, notification channels, and queue processors.
   - Dependency: fully populated startup state and registries.
   - Failure mode: broken UX, wrong routing, hidden background drift.

## Call Chains

### Flow: natural prompt submission

1. Input captured in `src/screens/REPL.tsx`
2. Submission normalized in `src/utils/handlePromptSubmit.ts`
3. Routing performed in `src/utils/processUserInput/processUserInput.ts`
4. Runtime query executes in `src/query.ts`
5. Tool uses run through `src/services/tools/toolOrchestration.ts` and `src/services/tools/toolExecution.ts`
6. Streamed model output and tool results return to `src/screens/REPL.tsx`
7. Persistence is updated by `src/utils/sessionStorage.ts`

### Flow: slash command submission

1. Input captured in `src/screens/REPL.tsx`
2. Submission normalized in `src/utils/handlePromptSubmit.ts`
3. Slash branch selected in `src/utils/processUserInput/processUserInput.ts`
4. Slash semantics resolved in `src/utils/processUserInput/processSlashCommand.tsx`
5. Registries come from `src/commands.ts` and plugin command loaders
6. Output and side effects feed back into `src/screens/REPL.tsx` and session persistence

### Flow: resume session

1. Session resolution begins during startup in `src/main.tsx`
2. Metadata and transcript are loaded from `src/utils/sessionStorage.ts`
3. Resume reconstruction runs through `src/utils/sessionRestore.ts`
4. Interactive state is restored inside `src/screens/REPL.tsx`

## Side-Effect Map

| Location | Side effect | Trigger | Observable impact | Safe to move? |
|---|---|---|---|---|
| `src/entrypoints/cli.tsx` | top-level env mutation | module import | affects import-time tool flags | No |
| `src/main.tsx` | MDM raw read prefetch | module import | startup timing and managed settings freshness | No |
| `src/main.tsx` | keychain prefetch | module import | auth/cache warm-up timing | No |
| `src/setup.ts` | `process.chdir(...)` | setup execution | relative-path behavior, worktree targeting | No |
| `src/screens/REPL.tsx` | background hook startup | component mount | notifications, polling, queue semantics | No |
| `src/utils/sessionStorage.ts` | transcript append/rewrite | runtime events | session durability and resume compatibility | No |

## Trust Boundaries

1. Model boundary
   - Owner: `src/services/api/claude.ts`
   - Inputs: internal messages, tool schemas, model settings
   - Outputs: streamed model/tool events
   - Failure posture: mixed, but schema shaping should remain strict
2. Tool execution boundary
   - Owner: `src/services/tools/toolExecution.ts`
   - Inputs: model-issued tool requests
   - Outputs: real filesystem/network/process side effects
   - Failure posture: should remain conservative
3. Permission policy boundary
   - Owner: `src/utils/permissions/permissions.ts`
   - Inputs: tool name, context, rules, sandbox mode
   - Outputs: allow/deny/ask decision
   - Failure posture: fail closed
4. Sandbox boundary
   - Owner: `src/utils/sandbox/sandbox-adapter.ts`
   - Inputs: tool/runtime request and policy
   - Outputs: executable sandbox config
   - Failure posture: fail closed
5. MCP/plugin extension boundary
   - Owner: `src/services/mcp/client.ts`, `src/utils/plugins/pluginLoader.ts`
   - Inputs: config files, remote/server metadata, plugin manifests
   - Outputs: tools, commands, resources, settings
   - Failure posture: depends on subsystem, but stale state is a core risk
6. Persistence boundary
   - Owner: `src/utils/sessionStorage.ts`, `src/utils/config.ts`
   - Inputs: session/config mutations
   - Outputs: durable logs, metadata, settings
   - Failure posture: should not silently corrupt historical state

## Precedence Rules

- `src/utils/settings/settings.ts` resolves effective settings with plugin-provided base settings lower than user/project/local sources.
- `src/utils/config.ts` remains a separate authority for global/project config persistence and must not be merged casually with settings.
- CLI/env overrides in `src/main.tsx` and bootstrap state sit above on-disk defaults.
- MCP dedup and merge order is defined in `src/services/mcp/config.ts`, not in UI code.
- Permission allow/deny/ask evaluation order is defined in `src/utils/permissions/permissions.ts`.

## Do Not Touch Blindly

- `src/main.tsx`
- `src/query.ts`
- `src/screens/REPL.tsx`
- `src/utils/sessionStorage.ts`
- `src/utils/permissions/permissions.ts`
- `src/services/mcp/client.ts`
- `src/utils/settings/settings.ts`
- `src/utils/config.ts`
- `src/bootstrap/state.ts`

## Current Python Owners

| Python package | Target authority |
|---|---|
| `pylaude.bootstrap` | startup order and stateful bootstrap replacement |
| `pylaude.runtime` | parity trace manifest and authority tracking |
| `pylaude.settings` | explicit settings precedence model |
| `pylaude.permissions` | fail-closed policy base |
| `pylaude.sessions` | transcript/session boundary models |
| `pylaude.mcp` | MCP schema and merge owner |
| `pylaude.plugins` | plugin schema and loader owner |
| `pylaude.ui` | future REPL controller and TUI state |

## Unresolved Ambiguities

| Ambiguity | Why unresolved | Risk if wrong | Validation plan |
|---|---|---|---|
| Exact transcript wire format edge cases | `sessionStorage.ts` is large and not yet replay-proven | session resume incompatibility | add replay fixtures from TS logs before porting write path |
| Full permission branch matrix | policy code has many special cases and UI adapters | fail-open or noisy regressions | extract matrix fixtures from TS before deeper Python policy port |
| MCP stale-cache invalidation edge cases | client memoization and auth expiry handling are cross-cutting | missing or stale tools/resources | trace reconnect and expiry scenarios before port |
