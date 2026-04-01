# Python Port Plan

## Goal

Port the TypeScript/Bun runtime to Python 3.12 while preserving externally observable CLI/TUI behavior and trust boundaries.

## Fixed Technology Choices

- Python 3.12
- `uv` for package/environment management
- `prompt_toolkit` for terminal input and event-loop control
- `rich` for rendering
- `anyio` for structured async concurrency
- `pydantic` for trust-boundary models
- `pytest` for parity, replay, and unit tests

## Delivery Model

- `src/` remains the production authority during migration.
- Python is developed in parallel under `pylaude/`.
- Migration proceeds by vertical slices with parity evidence.
- The cutover stages are:
  1. `ts-baseline`
  2. `dual-run`
  3. `python-default`

## Implemented Foundation

The current repository now contains:

- `pyproject.toml` defining the Python package and toolchain
- `pylaude.bootstrap` as an explicit startup pipeline replacement
- `pylaude.runtime.trace_manifest` describing critical parity scenarios
- `pylaude.settings` with an explicit precedence model
- `pylaude.permissions` with fail-closed default decision logic
- `pylaude.sessions`, `pylaude.mcp`, and `pylaude.plugins` boundary models
- `tests/parity`, `tests/replay`, and `tests/unit` scaffolding with initial fixtures

This is foundation work only. It does not claim runtime parity.

## Migration Order

1. Pure shared models, IDs, and constants
2. Config/settings precedence and cache invalidation
3. Permissions and sandbox behavior
4. Session append/rewrite/restore semantics
5. MCP/plugin merge, cache, and invalidation behavior
6. Tool registry and orchestration
7. Model/API streaming adapters
8. Prompt Toolkit / Rich REPL controller
9. Secondary entrypoints and feature-gated modes

## Rules For Every Slice

1. identify the authoritative TypeScript files
2. update `docs/porting/architecture-map.md`
3. update `docs/porting/invariants.md`
4. update `docs/porting/parity-matrix.md`
5. add fixture or replay evidence
6. implement the Python slice
7. verify against the TypeScript baseline

## Immediate Next Work

1. extract real TypeScript trace captures for startup order, prompt routing, and permission decisions
2. port settings/config loading beyond the current precedence scaffold
3. add transcript parser and compatibility replay tests using real session logs
4. implement MCP/plugin merge logic with deterministic dedup
5. start the Prompt Toolkit controller only after routing and persistence traces exist

## Current Risks

- Python runtime is not verifiable in this environment yet because no `python` or `py` executable is on `PATH`
- TypeScript baseline traces are not captured yet, only modeled
- `sessionStorage.ts`, `permissions.ts`, and `services/mcp/client.ts` remain unported high-risk authorities

## Acceptance Gate

The Python runtime cannot replace the TypeScript runtime until:

- critical rows in `docs/porting/parity-matrix.md` are proven
- transcript compatibility is replay-tested
- permission behavior is proven fail-closed
- startup order and cwd semantics are trace-matched
- MCP/plugin invalidation semantics are validated
