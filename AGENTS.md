# AGENTS.md

## Mission

This repository is being migrated from a TypeScript implementation to a Python implementation.

The goal is NOT to redesign product behavior.
The goal is NOT to simplify by deleting edge cases.
The goal is NOT to "Python-ify" semantics if that changes runtime behavior.

The goal IS:
- preserve Claude Code's observable behavior, control flow, and trust boundaries
- make the system easier to audit, safer to operate, and more educational to study
- produce a Python implementation that is behaviorally consistent with the TypeScript runtime
- reduce hidden side effects where possible, but only after documenting and verifying invariants

## Non-negotiable rules

1. Behavior preservation first.
   - Before changing code, identify the invariant being preserved.
   - If behavior is unclear, document uncertainty instead of guessing.

2. Never rewrite blindly.
   - Do not mass-convert files from TS to Python without mapping runtime ownership, startup order, and side effects.

3. Respect the real architecture, not just folder names.
   - Treat entrypoints, runtime loop, permissions, session persistence, MCP client, config/settings, and plugin loading as system authorities.

4. Do not collapse trust boundaries without proof.
   - Model boundary
   - Tool execution boundary
   - Permission boundary
   - Sandbox boundary
   - Extension/plugin/MCP boundary
   - Persistence boundary

5. Do not touch critical files blindly.
   - startup/composition root
   - query/runtime loop
   - REPL/controller layer
   - permissions policy
   - session persistence and resume
   - MCP client/cache
   - config/settings precedence

6. Preserve startup and precedence semantics.
   - import-time environment assumptions
   - cwd/worktree mutation timing
   - config vs settings precedence
   - plugin-injected settings
   - MCP dedup/merge order
   - permission allow/deny/ask semantics
   - transcript restore rules

7. Refactor only behind evidence.
   - Every structural change must be justified by a documented invariant, test, or trace.

8. Prefer vertical slices.
   - For each subsystem, complete:
     - architecture map
     - invariant list
     - parity tests
     - Python port
     - regression verification
   - Do not produce isolated UI-only or infra-only migration work if the subsystem spans multiple layers.

## Required workflow

For every substantial task, follow this order:

1. Read relevant skills before changing anything.
2. Reconstruct architecture and call chain.
3. Write/update docs:
   - docs/porting/architecture-map.md
   - docs/porting/invariants.md
   - docs/porting/parity-matrix.md
4. Create an explicit migration plan for the target slice.
5. Add or update parity tests and golden-path traces.
6. Implement Python version incrementally.
7. Run verification.
8. Review diff for security, reliability, and behavior drift.
9. Summarize:
   - what changed
   - what invariant was preserved
   - what remains risky
   - what was not proven

## Definition of done

A slice is not done unless all are true:
- behaviorally mapped from TS to Python
- invariants documented
- parity verified with tests or trace comparison
- security/trust-boundary impact reviewed
- no hidden "cleanup" that changes semantics
- remaining uncertainty explicitly documented

## Output expectations

When working, always report:
- current subsystem
- authoritative files
- invariants discovered
- migration risks
- parity test status
- whether any assumption is unverified

## Hard constraints

- Do not delete edge-case logic just because it looks complex.
- Do not merge config/settings systems without proving precedence equivalence.
- Do not simplify permission logic without enumerating allow/deny/ask behavior.
- Do not rewrite session persistence/resume logic without transcript compatibility checks.
- Do not replace MCP/plugin semantics without documenting cache, dedup, auth, and invalidation behavior.
- Do not trust apparent UI/component boundaries.

## Preferred Python target style

- explicit modules over magic
- typed Python where practical
- dataclasses / pydantic-style boundary models when useful
- deterministic orchestration
- no implicit global mutation unless required for parity and documented
- narrow adapters around filesystem, subprocess, MCP, model API, and sandboxing

## Verification commands

Before marking work done, always:
- run the relevant test suite
- run lint/format/type checks if configured
- compare traces against the TypeScript behavior for the touched flow
- update docs/porting/*
