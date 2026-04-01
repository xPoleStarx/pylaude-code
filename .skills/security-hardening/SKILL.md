---
name: security-hardening
description: Use this skill when improving safety, reducing hidden side effects, tightening execution boundaries, or auditing trust boundaries during the Python port.
---

Security hardening must be behavior-aware.

Tasks:
- identify trust boundaries
- identify unsafe implicit state
- identify fail-open risks
- identify side-effect-heavy startup assumptions
- propose hardening changes that preserve user-visible behavior

Rules:
- do not use security as an excuse for semantic drift
- document each hardening change with:
  - prior risk
  - preserved invariant
  - verification method
