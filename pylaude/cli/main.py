from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from pylaude.bootstrap import BootstrapContext, default_bootstrap_pipeline
from pylaude.runtime.authorities import AUTHORITATIVE_TS_FILES
from pylaude.runtime.trace_manifest import build_default_manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pylaude",
        description="Python port bootstrap for the pylaude-code migration.",
    )
    parser.add_argument(
        "--print-bootstrap",
        action="store_true",
        help="Print the current Python bootstrap order and exit.",
    )
    parser.add_argument(
        "--print-authorities",
        action="store_true",
        help="Print the authoritative TypeScript files tracked by the migration.",
    )
    parser.add_argument(
        "--print-trace-manifest",
        action="store_true",
        help="Print the parity trace manifest and exit.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    context = BootstrapContext(
        cwd=Path.cwd(),
        argv=list(argv or []),
        env=dict(os.environ),
    )
    pipeline = default_bootstrap_pipeline()
    context = pipeline.run(context)

    if args.print_bootstrap:
        print(json.dumps({"checkpoints": context.notes, "state": context.state}, indent=2))
        return 0
    if args.print_authorities:
        print(json.dumps(AUTHORITATIVE_TS_FILES, indent=2))
        return 0
    if args.print_trace_manifest:
        print(json.dumps(build_default_manifest().model_dump(mode="json"), indent=2))
        return 0

    parser.print_help()
    return 0
