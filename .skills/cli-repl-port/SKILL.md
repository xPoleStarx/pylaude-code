---
name: cli-repl-port
description: Use this skill when migrating the terminal app, REPL loop, prompt submission flow, command dispatch, and interactive runtime behavior to Python.
---

Focus on the real interactive loop.

Map:
- CLI entrypoint
- environment/bootstrap timing
- REPL controller responsibilities
- prompt submission path
- slash command path
- query execution path
- streaming updates
- cancellation and retry behavior

Do not reduce the REPL to a simplistic input/output loop if the TS implementation acts as an application controller.

Candidate Python targets may include:
- Typer for CLI commands
- prompt_toolkit or Textual/Rich for interactive terminal behavior

But:
- choose tools only after parity requirements are clear
- do not impose a new interaction model that changes semantics
