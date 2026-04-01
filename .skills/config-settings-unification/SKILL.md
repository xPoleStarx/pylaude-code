---
name: config-settings-unification
description: Use this skill when touching configuration, settings, caches, plugin-injected settings, or precedence rules during migration.
---

This repository likely has split-brain configuration behavior.

Tasks:
- identify all config authorities
- map precedence rules
- map cache invalidation rules
- distinguish persisted config from runtime-resolved settings
- document plugin influence on effective settings

Rules:
- do not unify config systems unless equivalence is proven
- if unification is attempted, preserve externally visible precedence
- prefer an adapter layer first, consolidation second
