---
name: permissions-sandbox-port
description: Use this skill when working on permission policy, tool allow/deny/ask behavior, sandbox enforcement, or execution safety during the Python migration.
---

This subsystem is security-critical.

Tasks:
- enumerate allow / deny / ask rules
- identify special cases and shortcuts
- identify sandbox-aware exceptions
- map policy evaluation order
- preserve fail-closed behavior where relevant
- document every rule before porting

Never:
- simplify policy because it looks messy
- merge permission branches without proving equivalence
- default to permissive behavior

Outputs:
- policy matrix
- Python policy evaluator design
- regression tests for allow/deny/ask cases
