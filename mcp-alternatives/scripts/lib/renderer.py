#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Markdown rendering utilities."""

from pathlib import Path
from typing import Any


def render_cli_entry(data: dict[str, Any]) -> str:
    """Render a single CLI entry as markdown."""
    lines = []

    # Header with service name
    service = data.get("service", "Unknown Service")
    lines.append(f"### {service}")
    lines.append("")

    # Comparison table
    name = data.get("name", data.get("repo", "").split("/")[-1])
    repo = data.get("repo", "")
    replaces = data.get("replaces_mcp", "MCP Server")
    token_comp = data.get("token_comparison", "")

    # Build repo link
    if repo:
        if not repo.startswith("http"):
            repo_url = f"https://{repo}"
        else:
            repo_url = repo
        name_link = f"[{name}]({repo_url})"
    else:
        name_link = name

    lines.append("| MCP Server | CLI Alternative |")
    lines.append("|------------|-----------------|")

    if token_comp:
        lines.append(f"| {replaces} ({token_comp.split('→')[0].strip()}) | {name_link} ({token_comp.split('→')[-1].strip()}) |")
    else:
        lines.append(f"| {replaces} | {name_link} |")

    # Description
    if data.get("description"):
        lines.append("")
        lines.append(data["description"])

    # Resources
    resources = data.get("resources", [])
    if resources:
        lines.append("")
        lines.append("**Resources:**")
        lines.append("")
        for res in resources:
            label = res.get("label", "Link")
            url = res.get("url", "")
            archived = res.get("archived", "")
            if archived:
                lines.append(f"* [{label}]({url}) ([archived]({archived}))")
            else:
                lines.append(f"* [{label}]({url})")

    # Quote
    quote = data.get("quote")
    if quote:
        lines.append("")
        lines.append("**Why it wins:**")
        lines.append("")
        lines.append(f"> \"{quote.get('text', '')}\"")
        if quote.get("source"):
            lines.append(f"> — {quote['source']}")

    # Examples
    examples = data.get("examples", [])
    if examples:
        lines.append("")
        lines.append("**Examples:**")
        lines.append("")
        lines.append("```bash")
        for ex in examples:
            if ex.get("description"):
                lines.append(f"# {ex['description']}")
            lines.append(ex.get("command", ""))
        lines.append("```")

    lines.append("")
    lines.append("---")

    return "\n".join(lines)


def render_cli_entries(entries: list[tuple[Path, dict[str, Any]]]) -> str:
    """Render all CLI entries as markdown."""
    if not entries:
        return "*No CLI alternatives documented yet.*"

    parts = []
    for path, data in entries:
        parts.append(render_cli_entry(data))

    return "\n\n".join(parts)


def render_wanted_table(entries: list[tuple[Path, dict[str, Any]]]) -> str:
    """Render wanted entries as a table."""
    if not entries:
        return "*No requests yet.*"

    lines = []
    lines.append("We're tracking CLI alternatives for common MCP servers. See \"Contribute\" below.")
    lines.append("")
    lines.append("| Service | MCP Server Exists? | CLI Alternative? |")
    lines.append("|---------|-------------------|------------------|")

    for path, data in entries:
        service = data.get("service", path.stem)
        mcp_exists = "Yes" if data.get("mcp_exists", True) else "No"
        existing = data.get("existing_clis", [])
        if existing:
            cli_alt = ", ".join(f"`{c}`?" for c in existing)
        else:
            cli_alt = "?"

        lines.append(f"| {service} | {mcp_exists} | {cli_alt} |")

    lines.append("")
    lines.append("---")

    return "\n".join(lines)


if __name__ == "__main__":
    # Quick test
    print("Renderer module loaded successfully")
