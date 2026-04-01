---
name: session-persistence-port
description: Use this skill when porting transcripts, append/rewrite logic, resume behavior, storage limits, tombstones, or session restoration.
---

This subsystem is correctness-critical.

Tasks:
- map transcript format
- map append vs rewrite semantics
- map resume rules
- map corruption handling
- map size-limit behavior
- verify compatibility expectations

Rules:
- do not break old session compatibility without an explicit migration path
- do not rewrite persistence logic from memory
- use golden fixtures and replay tests
