#!/usr/bin/env python3
"""Validate that pi theme files use only ANSI 0-15 indices and "" in colors.

The export section is exempt since HTML output can't use ANSI indices.
"""

import json
import sys
from glob import glob
from pathlib import Path


def validate_theme(path: str) -> list[str]:
    with open(path) as f:
        theme = json.load(f)

    errors = []
    var_names = set(theme.get("vars", {}).keys())

    # Vars: every value must be int 0-15 or ""
    for key, val in theme.get("vars", {}).items():
        if isinstance(val, int):
            if val < 0 or val > 15:
                errors.append(f"vars.{key}: {val} is outside ANSI 0-15")
        elif isinstance(val, str):
            if val.startswith("#"):
                errors.append(f"vars.{key}: hex value {val} not allowed")
        else:
            errors.append(f"vars.{key}: unexpected type {type(val).__name__}")

    # Colors: every value must be int 0-15, "" (terminal default), or a var ref
    for key, val in theme.get("colors", {}).items():
        if isinstance(val, int):
            if val < 0 or val > 15:
                errors.append(f"colors.{key}: {val} is outside ANSI 0-15")
        elif isinstance(val, str):
            if val.startswith("#"):
                errors.append(f"colors.{key}: hex value {val} not allowed")
            elif val != "" and val not in var_names:
                errors.append(f"colors.{key}: references unknown var '{val}'")
        else:
            errors.append(f"colors.{key}: unexpected type {type(val).__name__}")

    return errors


def main() -> int:
    themes = sorted(glob(str(Path(__file__).resolve().parent.parent / "themes" / "*.json")))

    if not themes:
        print("No theme files found in themes/")
        return 1

    failed = False
    for path in themes:
        name = Path(path).name
        errors = validate_theme(path)
        if errors:
            failed = True
            print(f"FAIL {name}")
            for err in errors:
                print(f"  {err}")
        else:
            print(f"OK   {name}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
