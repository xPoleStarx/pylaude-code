---
name: runtime-invariants
description: Use this skill when preserving behavior matters more than rewriting style, especially during TypeScript-to-Python migration of orchestration-heavy systems.
---

Your job is to extract invariants that must survive the Python port.

Look for:
- startup sequencing invariants
- config/settings precedence invariants
- cwd/worktree invariants
- permission policy invariants
- transcript/session restore invariants
- MCP/plugin merge and cache invariants
- cancellation / partial failure semantics
- command routing invariants
- slash-command vs natural-prompt branching behavior

For each invariant, document:
- name
- source files
- why it exists
- what breaks if it changes
- how to verify it in Python

Write results to docs/porting/invariants.md

Never implement migration before listing invariants for the touched subsystem.
