# Parity Matrix

## Purpose

This matrix gates the TypeScript-to-Python migration. A row is not complete because code exists; it is complete because comparable evidence exists.

## Status Legend

- `Not started`: no Python owner or fixture
- `Scaffolded`: Python owner and fixtures exist, but no TS-vs-Python execution proof yet
- `In progress`: some proof exists, but coverage is incomplete
- `Pass`: parity proven for the tracked scope
- `Drift`: behavior differs and is explicitly accepted
- `Blocked`: proof cannot be gathered yet

## Matrix

| Area | Scenario | TS baseline evidence | Python evidence | Status | Notes |
|---|---|---|---|---|---|
| Startup | Bootstrap ordering and side effects | authoritative files identified in `docs/porting/architecture-map.md` | `pylaude.bootstrap.pipeline`, `tests/parity/fixtures/startup_order.json` | Scaffolded | runtime execution comparison still missing |
| Call chain | Slash vs natural prompt routing | authoritative chain documented from `REPL.tsx` through `processSlashCommand.tsx` | `tests/parity/fixtures/prompt_routing.json` | Scaffolded | Python UI controller not implemented yet |
| Config precedence | Effective setting resolution | authorities documented in `config.ts` and `settings.ts` | `pylaude.settings.precedence`, `tests/unit/test_settings_precedence.py`, `tests/parity/fixtures/settings_precedence.json` | In progress | only core precedence scaffolded |
| Permissions | allow/deny/ask order | authorities documented in `permissions.ts` and `permissionSetup.ts` | `pylaude.permissions.policy`, `tests/unit/test_permission_policy.py`, `tests/parity/fixtures/permission_matrix.json` | In progress | special-case branches not ported yet |
| Golden transcripts | Transcript replay compatibility | authorities documented in `sessionStorage.ts` and `sessionRestore.ts` | `pylaude.sessions.models`, `tests/replay/test_session_models.py`, `tests/replay/fixtures/session_resume.json` | In progress | real transcript parser not implemented yet |
| MCP/plugin discovery | Merge/dedup/invalidation behavior | authorities documented in MCP and plugin loaders | `tests/parity/fixtures/mcp_plugin_discovery.json`, `pylaude.mcp.models`, `pylaude.plugins.models` | Scaffolded | no Python merge logic yet |
| Runtime orchestration | Partial failure semantics | authoritative chain documented from `query.ts` to streaming tool executor | no Python execution proof yet | Not started | critical before cutover |
| Runtime orchestration | Cancellation propagation | authoritative chain documented from `query.ts` to streaming tool executor | no Python execution proof yet | Not started | critical before cutover |
| Interactive TUI | Core REPL rendering and controls | authorities documented in `replLauncher.tsx` and `REPL.tsx` | `pylaude.ui.controller` | Scaffolded | no Prompt Toolkit app yet |

## Required Evidence Per Row

Each row must eventually provide:

1. fixture or replay input
2. TypeScript capture
3. Python capture
4. comparison method
5. explicit note for any accepted drift

## Drift Policy

- undocumented drift is prohibited
- security drift is prohibited by default
- file-format drift requires a versioned compatibility adapter
- UI drift must still preserve command names, flags, routing, and permission semantics unless explicitly approved

## Current Gate

Cutover to a Python-default runtime is blocked until all critical rows are `Pass` or approved `Drift`, with no unresolved security-critical gaps.
