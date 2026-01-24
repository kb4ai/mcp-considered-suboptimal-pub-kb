# MCP Alternatives: Agent Guide

Quick reference for LLM agents working with this directory.

## Directory Layout

```
mcp-alternatives/
├── *.cli.yaml          # CLI tool entries (source of truth)
├── *.wanted.yaml       # Wanted entries (help needed)
├── spec/               # YAML schemas
├── sections/           # Static markdown sections
└── scripts/            # Python utilities
```

## Adding a CLI Tool

Create `{name}.cli.yaml`:

```yaml
repo: github.com/owner/repo      # Required
name: Tool Name                   # Optional (derived from repo)
service: ServiceName              # What it replaces
replaces_mcp: MCP Server Name     # Optional
token_comparison: "~13k → ~200"   # Optional
description: Brief explanation    # Optional
tags: [category1, category2]      # Optional
maturity: stable                  # alpha/beta/stable/unknown
```

## Adding a Wanted Entry

Create `{service}.wanted.yaml`:

```yaml
service: ServiceName
mcp_exists: true
existing_clis: [cli1, cli2]      # Unverified options
pain_points: What's wrong
```

## Scripts

All scripts support `--help` and `--json` output.

```bash
# Validate all entries
./mcp-alternatives/scripts/validate.py

# Query entries
./mcp-alternatives/scripts/query.py --service=Linear
./mcp-alternatives/scripts/query.py --type=cli --has=quote

# Show statistics
./mcp-alternatives/scripts/stats.py

# Regenerate the document
./mcp-alternatives.regenerate.py
```

## Regeneration

After modifying YAML files, run:

```bash
./mcp-alternatives.regenerate.py
```

This validates entries and rebuilds `mcp-alternatives.md`.

## Schemas

Full schemas in `spec/cli.spec.yaml` and `spec/wanted.spec.yaml`.

Key rules:

* CLI entries require `repo` field
* Wanted entries have no required fields
* All other fields optional (low contribution barrier)
