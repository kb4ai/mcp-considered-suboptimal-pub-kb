#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Shared utilities for loading YAML data files."""

from pathlib import Path
from typing import Any
import yaml

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent.parent  # mcp-alternatives/


def get_root_dir() -> Path:
    """Return the mcp-alternatives directory."""
    return ROOT_DIR


def load_yaml(path: Path) -> dict[str, Any]:
    """Load a single YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_yaml_files(pattern: str) -> list[tuple[Path, dict[str, Any]]]:
    """Load all YAML files matching pattern from root directory.

    Returns list of (path, data) tuples.
    """
    results = []
    for path in sorted(ROOT_DIR.glob(pattern)):
        if path.is_file():
            try:
                data = load_yaml(path)
                results.append((path, data))
            except yaml.YAMLError as e:
                print(f"Warning: Failed to parse {path}: {e}")
    return results


def load_cli_entries() -> list[tuple[Path, dict[str, Any]]]:
    """Load all CLI tool entries."""
    return load_yaml_files("*.cli.yaml")


def load_wanted_entries() -> list[tuple[Path, dict[str, Any]]]:
    """Load all wanted entries."""
    return load_yaml_files("*.wanted.yaml")


def load_spec(spec_type: str) -> dict[str, Any]:
    """Load a spec file by type (cli, wanted)."""
    spec_path = ROOT_DIR / "spec" / f"{spec_type}.spec.yaml"
    if spec_path.exists():
        return load_yaml(spec_path)
    return {}


if __name__ == "__main__":
    # Quick test
    print("CLI entries:", len(load_cli_entries()))
    print("Wanted entries:", len(load_wanted_entries()))
