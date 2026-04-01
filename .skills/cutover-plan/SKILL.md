---
name: cutover-plan
description: Use this skill when planning the staged transition from the TypeScript implementation to the Python implementation with minimal behavior drift.
---

Your task is to produce a staged migration plan.

Plan must include:
- subsystem order
- blockers
- parity gates
- rollback points
- documentation checkpoints
- dual-run or shadow-run opportunities
- acceptance criteria per slice

Preferred migration order:
1. architecture mapping
2. invariant extraction
3. test harness
4. pure utility modules
5. config/settings adapters
6. permissions/sandbox
7. session persistence
8. MCP/plugin lifecycle
9. query/runtime loop
10. CLI/REPL integration
11. cutover and cleanup
