---
name: parity-test-harness
description: Use this skill when building verification harnesses that prove the Python port matches the TypeScript implementation for key user flows.
---

Build proof, not vibes.

Required test layers:
1. call-chain / trace tests
2. golden transcript tests
3. command routing tests
4. permission matrix tests
5. config precedence tests
6. session resume tests
7. plugin/MCP discovery tests
8. tool orchestration failure/cancellation tests

Rules:
- compare observable behavior, not internal implementation style
- prefer deterministic fixtures
- store parity matrix in docs/porting/parity-matrix.md
