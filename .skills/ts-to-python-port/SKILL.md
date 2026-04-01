---
name: ts-to-python-port
description: Use this skill when migrating a TypeScript subsystem to Python while preserving external behavior, control flow, and edge cases.
---

This is a behavior-preserving port, not a rewrite.

Process:
1. identify subsystem boundaries
2. map TS inputs, outputs, state, side effects, and async semantics
3. identify hidden dependencies
4. define Python module layout
5. port incrementally
6. preserve error semantics where externally observable
7. add parity tests
8. document known drift

Rules:
- preserve observable behavior over stylistic purity
- preserve edge cases unless explicitly removed and documented
- preserve async/cancellation semantics where they affect turn behavior
- preserve serialization and persistence formats unless a migration path is implemented

Preferred outputs:
- Python modules with clear adapters
- boundary models
- tests comparing TS traces vs Python traces
