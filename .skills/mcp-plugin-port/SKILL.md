---
name: mcp-plugin-port
description: Use this skill when porting MCP config, client lifecycle, memoized connections, tool/resource discovery, plugin loading, or extension behavior.
---

This subsystem is extension-critical and cache-sensitive.

Tasks:
- identify merge/dedup precedence
- identify connection lifecycle and invalidation rules
- identify auth/session coupling
- identify where discovered tools/commands/resources are folded back into runtime state
- preserve lazy/eager loading behavior where it affects startup or stale state

Rules:
- do not assume UI-level MCP code is authoritative
- do not replace memoization without defining invalidation semantics
