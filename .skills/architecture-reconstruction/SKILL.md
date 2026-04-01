---
name: architecture-reconstruction
description: Use this skill when the task involves understanding the real control plane of the repository, identifying authoritative modules, mapping startup order, call chains, and hidden side effects before any refactor or migration.
---

You are performing architecture reconstruction, not casual code reading.

Your job:
- identify real runtime ownership
- separate apparent architecture from actual execution authority
- map startup order and import-time side effects
- identify control-plane files and global singletons
- document trust boundaries and precedence rules

Required outputs:
1. authoritative files
2. call chains for major flows
3. startup order map
4. side-effect map
5. trust boundaries
6. do-not-touch-blindly list
7. unresolved ambiguities

Rules:
- do not propose refactors before mapping architecture
- do not trust folder names like component, screen, service, loader
- treat caches, registries, startup hooks, permissions, persistence, and runtime loops as likely authorities
- write findings into docs/porting/architecture-map.md
