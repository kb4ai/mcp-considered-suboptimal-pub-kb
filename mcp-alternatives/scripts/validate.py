#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Validate YAML data files against their specs."""

import argparse
import sys
from pathlib import Path
from typing import Any

# Add lib to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from lib.loader import load_yaml, load_cli_entries, load_wanted_entries, load_spec, get_root_dir


def validate_entry(data: dict[str, Any], spec: dict[str, Any], path: Path) -> list[str]:
    """Validate a single entry against its spec. Returns list of errors."""
    errors = []

    # Check required fields
    for field in spec.get("required", []):
        if field not in data or data[field] is None or data[field] == "":
            errors.append(f"{path.name}: Missing required field '{field}'")

    # Check field types (basic validation)
    fields_spec = spec.get("fields", {})
    for field, value in data.items():
        if field not in fields_spec:
            continue  # Allow extra fields

        field_spec = fields_spec[field]
        expected_type = field_spec.get("type")

        if expected_type == "string" and not isinstance(value, str):
            errors.append(f"{path.name}: Field '{field}' should be string, got {type(value).__name__}")
        elif expected_type == "boolean" and not isinstance(value, bool):
            errors.append(f"{path.name}: Field '{field}' should be boolean, got {type(value).__name__}")
        elif expected_type == "list" and not isinstance(value, list):
            errors.append(f"{path.name}: Field '{field}' should be list, got {type(value).__name__}")
        elif expected_type == "object" and not isinstance(value, dict):
            errors.append(f"{path.name}: Field '{field}' should be object, got {type(value).__name__}")
        elif expected_type == "enum":
            valid_values = field_spec.get("values", [])
            if value not in valid_values:
                errors.append(f"{path.name}: Field '{field}' must be one of {valid_values}, got '{value}'")

    return errors


def validate_all(strict: bool = False) -> tuple[bool, list[str]]:
    """Validate all entries. Returns (success, errors)."""
    all_errors = []

    # Load specs
    cli_spec = load_spec("cli")
    wanted_spec = load_spec("wanted")

    # Validate CLI entries
    for path, data in load_cli_entries():
        errors = validate_entry(data, cli_spec, path)
        all_errors.extend(errors)

    # Validate wanted entries
    for path, data in load_wanted_entries():
        errors = validate_entry(data, wanted_spec, path)
        all_errors.extend(errors)

    success = len(all_errors) == 0
    return success, all_errors


def main():
    parser = argparse.ArgumentParser(description="Validate YAML data files")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    success, errors = validate_all(strict=args.strict)

    if args.json:
        import json
        print(json.dumps({"success": success, "errors": errors}))
    else:
        if errors:
            print("Validation errors:")
            for error in errors:
                print(f"  - {error}")
        else:
            print("All files valid.")

    sys.exit(0 if success else 2)


if __name__ == "__main__":
    main()
