#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Regenerate mcp-alternatives.md from YAML data and section files."""

import argparse
import sys
from pathlib import Path

# Add scripts to path
REPO_ROOT = Path(__file__).parent
MCP_ALT_DIR = REPO_ROOT / "mcp-alternatives"
SCRIPTS_DIR = MCP_ALT_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from lib.loader import load_cli_entries, load_wanted_entries
from lib.renderer import render_cli_entries, render_wanted_table
from validate import validate_all


def load_sections() -> list[tuple[str, str, str]]:
    """Load section files in order.

    Returns list of (filename, type, content) tuples.
    Type is 'static' for .section.md files, or the type from .generated files.
    """
    sections_dir = MCP_ALT_DIR / "sections"
    sections = []

    for path in sorted(sections_dir.glob("*")):
        if path.suffix == ".md" and ".section" in path.name:
            # Static section
            content = path.read_text(encoding="utf-8")
            sections.append((path.name, "static", content))
        elif path.name.endswith(".generated"):
            # Generated section - parse the marker
            content = path.read_text(encoding="utf-8")
            # Extract type from marker
            gen_type = "unknown"
            heading = ""
            for line in content.split("\n"):
                if line.startswith("type:"):
                    gen_type = line.split(":", 1)[1].strip()
                elif line.startswith("heading:"):
                    heading = line.split(":", 1)[1].strip().strip('"')
            sections.append((path.name, gen_type, heading))

    return sections


def generate_content(gen_type: str, heading: str) -> str:
    """Generate content for a generated section."""
    lines = []

    if heading:
        lines.append(heading)
        lines.append("")

    if gen_type == "cli":
        entries = load_cli_entries()
        lines.append(render_cli_entries(entries))
    elif gen_type == "wanted":
        entries = load_wanted_entries()
        lines.append(render_wanted_table(entries))
    else:
        lines.append(f"*Unknown generator type: {gen_type}*")

    return "\n".join(lines)


def regenerate(validate_first: bool = True, dry_run: bool = False) -> bool:
    """Regenerate mcp-alternatives.md.

    Returns True on success, False on failure.
    """
    # Validate first
    if validate_first:
        success, errors = validate_all()
        if not success:
            print("Validation failed:")
            for error in errors:
                print(f"  - {error}")
            return False

    # Load sections
    sections = load_sections()

    # Build output
    output_parts = []
    for filename, sec_type, content in sections:
        if sec_type == "static":
            output_parts.append(content.rstrip())
        else:
            generated = generate_content(sec_type, content)
            output_parts.append(generated.rstrip())

    output = "\n\n".join(output_parts) + "\n"

    # Write output
    output_path = REPO_ROOT / "mcp-alternatives.md"

    if dry_run:
        print("=== DRY RUN - Would write to mcp-alternatives.md ===")
        print(output)
        return True

    output_path.write_text(output, encoding="utf-8")
    print(f"Regenerated {output_path}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate mcp-alternatives.md from YAML data"
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="Skip validation before regenerating"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print output instead of writing to file"
    )
    args = parser.parse_args()

    success = regenerate(
        validate_first=not args.no_validate,
        dry_run=args.dry_run
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
