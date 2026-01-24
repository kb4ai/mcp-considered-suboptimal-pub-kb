#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Query and filter YAML data entries."""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from lib.loader import load_cli_entries, load_wanted_entries


def query(
    entry_type: str = "all",
    service: str | None = None,
    has_field: str | None = None,
    tag: str | None = None,
) -> list[dict[str, Any]]:
    """Query entries with filters.

    Args:
        entry_type: "cli", "wanted", or "all"
        service: Filter by service name (case-insensitive substring)
        has_field: Only entries that have this field set
        tag: Filter by tag (cli entries only)

    Returns:
        List of matching entries with metadata.
    """
    results = []

    # Load entries
    if entry_type in ("cli", "all"):
        for path, data in load_cli_entries():
            entry = {"_type": "cli", "_file": path.name, **data}
            results.append(entry)

    if entry_type in ("wanted", "all"):
        for path, data in load_wanted_entries():
            entry = {"_type": "wanted", "_file": path.name, **data}
            results.append(entry)

    # Apply filters
    if service:
        service_lower = service.lower()
        results = [
            e for e in results
            if service_lower in e.get("service", "").lower()
        ]

    if has_field:
        results = [
            e for e in results
            if has_field in e and e[has_field] is not None and e[has_field] != ""
        ]

    if tag:
        tag_lower = tag.lower()
        results = [
            e for e in results
            if tag_lower in [t.lower() for t in e.get("tags", [])]
        ]

    return results


def main():
    parser = argparse.ArgumentParser(description="Query YAML data entries")
    parser.add_argument(
        "--type",
        choices=["cli", "wanted", "all"],
        default="all",
        help="Entry type to query"
    )
    parser.add_argument("--service", help="Filter by service name")
    parser.add_argument("--has", dest="has_field", help="Filter by field presence")
    parser.add_argument("--tag", help="Filter by tag")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    results = query(
        entry_type=args.type,
        service=args.service,
        has_field=args.has_field,
        tag=args.tag,
    )

    if args.json:
        print(json.dumps(results, indent=2, default=str))
    else:
        if not results:
            print("No matching entries.")
        else:
            for entry in results:
                print(f"[{entry['_type']}] {entry['_file']}")
                if entry.get("service"):
                    print(f"  Service: {entry['service']}")
                if entry.get("name"):
                    print(f"  Name: {entry['name']}")
                if entry.get("repo"):
                    print(f"  Repo: {entry['repo']}")
                print()

    sys.exit(0)


if __name__ == "__main__":
    main()
