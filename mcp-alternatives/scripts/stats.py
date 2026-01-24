#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Generate statistics about the data."""

import argparse
import json
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent))
from lib.loader import load_cli_entries, load_wanted_entries


def get_stats() -> dict:
    """Compute statistics about the data."""
    cli_entries = load_cli_entries()
    wanted_entries = load_wanted_entries()

    stats = {
        "cli_count": len(cli_entries),
        "wanted_count": len(wanted_entries),
        "total_count": len(cli_entries) + len(wanted_entries),
    }

    # CLI completeness
    cli_fields = ["name", "service", "description", "quote", "resources", "tags"]
    completeness = Counter()
    for path, data in cli_entries:
        for field in cli_fields:
            if field in data and data[field]:
                completeness[field] += 1

    stats["cli_completeness"] = {
        field: f"{completeness[field]}/{len(cli_entries)}"
        for field in cli_fields
    }

    # Tags distribution
    all_tags = []
    for path, data in cli_entries:
        all_tags.extend(data.get("tags", []))
    stats["tag_counts"] = dict(Counter(all_tags))

    # Services covered
    services = set()
    for path, data in cli_entries:
        if data.get("service"):
            services.add(data["service"])
    stats["services_with_cli"] = sorted(services)

    # Services wanted
    wanted_services = set()
    for path, data in wanted_entries:
        if data.get("service"):
            wanted_services.add(data["service"])
    stats["services_wanted"] = sorted(wanted_services)

    return stats


def main():
    parser = argparse.ArgumentParser(description="Show data statistics")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    stats = get_stats()

    if args.json:
        print(json.dumps(stats, indent=2))
    else:
        print("=== MCP Alternatives Statistics ===")
        print()
        print(f"CLI tools documented: {stats['cli_count']}")
        print(f"Wanted entries: {stats['wanted_count']}")
        print()
        print("CLI field completeness:")
        for field, count in stats["cli_completeness"].items():
            print(f"  {field}: {count}")
        print()
        print(f"Services with CLI alternatives: {', '.join(stats['services_with_cli'])}")
        print(f"Services wanted: {', '.join(stats['services_wanted'])}")
        if stats["tag_counts"]:
            print()
            print("Tags:")
            for tag, count in sorted(stats["tag_counts"].items()):
                print(f"  {tag}: {count}")

    sys.exit(0)


if __name__ == "__main__":
    main()
