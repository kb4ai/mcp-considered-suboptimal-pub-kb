# MCP Alternatives: Agent Guide

Quick reference for LLM agents working with this directory.

## Directory Layout

```
mcp-alternatives/
├── *.cli.yaml          # CLI tool entries (source of truth)
├── *.wanted.yaml       # Wanted entries (help needed)
├── spec/               # YAML schemas
│   ├── cli.spec.yaml
│   └── wanted.spec.yaml
├── sections/           # Static markdown sections + generated markers
│   ├── 00-intro.section.md
│   ├── 10-why-cli.section.md
│   ├── 20-cli-tools.generated    # Marker → inserts CLI entries
│   ├── 30-wanted.generated       # Marker → inserts wanted table
│   ├── 80-patterns.section.md
│   └── 90-contribute.section.md
└── scripts/            # Python utilities (all uv-runnable)
    ├── CODING_GUIDELINES.md
    ├── validate.py
    ├── query.py
    ├── stats.py
    └── lib/
        ├── loader.py
        └── renderer.py
```

**Generated output:** `mcp-alternatives.md` at repo root (do not edit directly).

**Main script:** `mcp-alternatives.regenerate.py` at repo root.

## Adding a CLI Tool

Create `mcp-alternatives/{name}.cli.yaml`. Only `repo` is required, all other fields optional:

```yaml
repo: github.com/owner/repo      # Required
name: Tool Name                   # Optional (derived from repo)
service: ServiceName              # What service it interfaces with
replaces_mcp: MCP Server Name     # Name of MCP server it replaces
token_comparison: "~13k → ~200"   # Before/after token usage
description: Brief explanation    # What the tool does
author: Author Name               # Tool author/maintainer
tags: [category1, category2]      # e.g. issue-tracking, vcs, chat
maturity: stable                  # alpha/beta/stable/unknown
last_verified: 2025-01-01         # When last confirmed working

quote:
  text: "Why this tool is great"  # Pull quote
  source: Author Name             # Quote attribution
  url: https://example.com        # Source link

resources:
  - label: Article Title
    url: https://example.com
    archived: archived-resources/filename.md  # Optional archived copy

examples:
  - command: "tool --flag | jq '.'"
    description: What this does
```

## Adding a Wanted Entry

Create `mcp-alternatives/{service}.wanted.yaml`. All fields optional:

```yaml
service: ServiceName
mcp_exists: true
existing_clis: [cli1, cli2]      # Unverified options
pain_points: What's wrong with current options
requested_by: github-username     # Or "anonymous"
```

## Adding/Editing Sections

Static sections live in `mcp-alternatives/sections/` with numeric prefix ordering.
Files ending in `.section.md` are included as-is. Files ending in `.generated` are
markers that tell the regeneration script where to insert data-driven content.

To add a new static section, create e.g. `mcp-alternatives/sections/45-new-topic.section.md`.

## Scripts

All scripts are standalone (`chmod +x`, `uv run` shebang) and importable as modules.
All support `--help` and `--json` output where applicable.

```bash
# Validate all YAML entries against specs
./mcp-alternatives/scripts/validate.py

# Query entries with filters
./mcp-alternatives/scripts/query.py --type=cli --has=quote
./mcp-alternatives/scripts/query.py --service=Linear
./mcp-alternatives/scripts/query.py --tag=vcs --json

# Show statistics (completeness, coverage, tags)
./mcp-alternatives/scripts/stats.py

# Regenerate mcp-alternatives.md (validates first, then builds)
./mcp-alternatives.regenerate.py
./mcp-alternatives.regenerate.py --dry-run     # Preview without writing
./mcp-alternatives.regenerate.py --no-validate # Skip validation
```

## Regeneration Workflow

After modifying YAML data files or section files:

```bash
./mcp-alternatives.regenerate.py
```

This:

1. Validates all YAML entries against specs (fails fast on errors)
2. Loads section files in numeric prefix order
3. Replaces `.generated` markers with rendered data
4. Writes `mcp-alternatives.md`

## GitHub Issue Templates

Contributors can also submit data via GitHub issues using templates at `.github/ISSUE_TEMPLATE/`:

* `submit-cli-tool.md` — Submit a CLI alternative (includes YAML codeblock template)
* `request-alternative.md` — Request a wanted entry
* `suggest-edit.md` — Typos, corrections, errata
* `add-resource.md` — Quotes, articles, sources

## Current Data

**CLI tools:** gh (GitHub), Linearis (Linear), slack-cli-mcp-wrapper (Slack)

**Wanted:** Asana, Confluence, Figma, Google Drive, Jira, Notion
