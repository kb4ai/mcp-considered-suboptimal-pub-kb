# Design: Data-Driven mcp-alternatives.md Generation

**Date:** 2026-01-24
**Status:** Approved

---

## Overview

Transform the hand-maintained `mcp-alternatives.md` into a data-driven system where:

- YAML files are the source of truth for CLI tools and "wanted" entries
- Static markdown sections are sourced from files
- Python scripts generate, validate, query, and maintain the data
- GitHub issue templates enable crowdsourced contributions

---

## Directory Structure

```
mcp-alternatives/
├── AGENTS.md                    # Instructions for LLM agents
├── spec/
│   ├── cli.spec.yaml            # Schema for CLI tool entries
│   └── wanted.spec.yaml         # Schema for wanted entries
├── sections/
│   ├── 00-intro.section.md
│   ├── 10-why-cli.section.md
│   ├── 20-cli-tools.generated   # Marker for generated content
│   ├── 30-wanted.generated
│   ├── 80-patterns.section.md
│   └── 90-contribute.section.md
├── scripts/
│   ├── CODING_GUIDELINES.md
│   ├── validate.py
│   ├── query.py
│   ├── stats.py
│   ├── table.py
│   └── lib/                     # Shared code if needed
├── linearis.cli.yaml            # CLI tool entries (flat at root)
├── gh.cli.yaml
├── slack-cli-mcp-wrapper.cli.yaml
├── notion.wanted.yaml           # Wanted entries
├── jira.wanted.yaml
└── ...

.github/
└── ISSUE_TEMPLATE/
    ├── config.yml
    ├── generic.md
    ├── submit-cli-tool.md
    ├── request-alternative.md
    ├── suggest-edit.md
    └── add-resource.md

mcp-alternatives.regenerate.py   # Main entry point
mcp-alternatives.md              # Generated output (git-tracked)
```

---

## Data Types

### CLI Tools (`*.cli.yaml`)

All fields optional except `repo`:

| Field | Type | Description |
|-------|------|-------------|
| `repo` | string | **Required.** GitHub/GitLab URL or owner/repo |
| `name` | string | Display name (derived from repo if omitted) |
| `service` | string | What service it interfaces with (e.g., "Linear") |
| `replaces_mcp` | string | Name of MCP server it replaces |
| `token_comparison` | string | Before/after token usage (e.g., "~13k → ~200") |
| `description` | string | Brief explanation |
| `quote` | object | `{text, source, url}` |
| `resources` | list | `[{label, url, archived}]` |
| `author` | string | Tool author |
| `tags` | list | Categories (e.g., ["issue-tracking"]) |
| `maturity` | enum | alpha, beta, stable, unknown |
| `last_verified` | date | When last confirmed working |

### Wanted Entries (`*.wanted.yaml`)

All fields optional:

| Field | Type | Description |
|-------|------|-------------|
| `service` | string | Service name (e.g., "Notion") |
| `mcp_exists` | boolean | Is there an MCP server for this? |
| `existing_clis` | list | Known CLI tools that might work (unverified) |
| `pain_points` | string | What's wrong with current options |
| `requested_by` | string | GitHub username or "anonymous" |

---

## Section Ordering

Convention-based using numeric prefixes:

- `00-intro.section.md` — Title, subtitle
- `10-why-cli.section.md` — Benefits table
- `20-cli-tools.generated` — Marker; script inserts CLI tools table
- `30-wanted.generated` — Marker; script inserts wanted table
- `80-patterns.section.md` — Design patterns for agent-friendly CLIs
- `90-contribute.section.md` — How to contribute, links to issue templates

Files are globbed and sorted by prefix. `.generated` files signal where to insert data-driven content.

---

## Scripts

### Core Principles

- Each script is standalone (`chmod +x`, `uv run` shebang)
- Each script is also importable as a module
- PEP 723 inline metadata for dependencies
- Minimal dependencies: PyYAML, optionally `rich` for CLI output

### Script Inventory

| Script | CLI Usage | Importable Functions |
|--------|-----------|---------------------|
| `validate.py` | `./validate.py [--strict]` | `validate_file()`, `validate_all()` |
| `query.py` | `./query.py --service=Linear` | `query()`, `load_all()` |
| `stats.py` | `./stats.py [--json]` | `get_stats()` |
| `table.py` | `./table.py --type=cli` | `render_table()` |

### Main Regenerator

`mcp-alternatives.regenerate.py` at repo root:

1. Validate all YAML (fail fast on errors)
2. Load section files in numeric order
3. For `.generated` markers, insert rendered tables
4. Write `mcp-alternatives.md`

---

## GitHub Issue Templates

### config.yml

```yaml
blank_issues_enabled: true
contact_links:
  - name: Pull Request
    url: https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/pulls
    about: Prefer PRs for direct contributions
```

### Templates

| Template | Purpose | Labels |
|----------|---------|--------|
| `submit-cli-tool.md` | Submit a CLI alternative | cli-tool, contribution |
| `request-alternative.md` | Request a wanted entry | wanted, help-wanted |
| `suggest-edit.md` | Typos, corrections | documentation |
| `add-resource.md` | Quotes, articles, sources | resource, contribution |

Each structured template includes a YAML codeblock with commented fields.

---

## AGENTS.md

Located at `mcp-alternatives/AGENTS.md`, provides:

- Quick reference for where data lives
- How to add new entries
- How to run validation
- How to regenerate the document
- Schema summaries

---

## Migration Plan

1. Create directory structure
2. Write specs and CODING_GUIDELINES.md
3. Extract current data into YAML files
4. Extract static sections from current mcp-alternatives.md
5. Implement scripts (validate first, then regenerate)
6. Verify regenerated output matches original (content-wise)
7. Add GitHub issue templates
8. Update contribution instructions
9. Commit and document

---

## Design Principles

- **Low barrier:** Most fields optional for easy contributions
- **Evolvable:** Scripts directory is a living toolbox
- **Convention over configuration:** Numeric prefixes, file extensions
- **Self-documenting:** AGENTS.md, --help on all scripts
- **Fail fast:** Validation runs before regeneration
