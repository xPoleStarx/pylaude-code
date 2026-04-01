from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass

from pylaude.bootstrap.context import BootstrapContext

BootstrapStep = Callable[[BootstrapContext], None]


@dataclass(slots=True)
class BootstrapPipeline:
    """Explicit replacement for the TS import-order startup chain."""

    steps: list[tuple[str, BootstrapStep]]

    def run(self, context: BootstrapContext) -> BootstrapContext:
        for name, step in self.steps:
            context.checkpoint(name)
            step(context)
        return context

    @classmethod
    def from_steps(cls, steps: Iterable[tuple[str, BootstrapStep]]) -> "BootstrapPipeline":
        return cls(list(steps))


def _apply_env_defaults(context: BootstrapContext) -> None:
    context.state["env_applied"] = True


def _resolve_initial_paths(context: BootstrapContext) -> None:
    context.state["resolved_cwd"] = str(context.cwd)


def _initialize_settings(context: BootstrapContext) -> None:
    context.state["settings_loaded"] = False


def _register_extensions(context: BootstrapContext) -> None:
    context.state["extensions_loaded"] = False


def _prepare_runtime(context: BootstrapContext) -> None:
    context.state["runtime_ready"] = False


def default_bootstrap_pipeline() -> BootstrapPipeline:
    return BootstrapPipeline.from_steps(
        [
            ("env_defaults", _apply_env_defaults),
            ("resolve_initial_paths", _resolve_initial_paths),
            ("initialize_settings", _initialize_settings),
            ("register_extensions", _register_extensions),
            ("prepare_runtime", _prepare_runtime),
        ]
    )
