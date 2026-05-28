---
source_url: https://github.com/kunchenguid/chrome-devtools-axi
title: "chrome-devtools-axi: Agent-ergonomic browser automation"
author: "Kun Chen (kunchenguid)"
publication_date: "~2026 (pre-2026-05)"
archive_date: "2026-05-17"
archived_by: "Claude Code (Opus 4.7)"
fetch_status: "ok"
---

# chrome-devtools-axi

**Source:** https://github.com/kunchenguid/chrome-devtools-axi
**Author:** kunchenguid (Kun Chen)
**License:** MIT
**Archived:** 2026-05-17

---

## What It Is

`chrome-devtools-axi` is a CLI wrapper around `chrome-devtools-mcp` that provides **"the most agent-ergonomic browser automation."** It's designed specifically for AI agents to control browsers through a command-line interface — turning MCP-style browser tooling back into a CLI that respects the agent's context budget.

## Key Differences from Standard Chrome DevTools / MCP

Standard Chrome DevTools provides low-level protocol access. `chrome-devtools-axi` adds:

* **Token efficiency** — TOON encoding reduces token usage ~40% vs raw JSON
* **Unified operations** — Single commands handle navigation, capture, and suggest next actions
* **Agent-friendly output** — Every response includes actionable hints
* **Stale reference detection** — Refs carry generation prefixes (e.g. `@g1:1`) preventing silent failures when pages re-render

## AXI Principles Demonstrated

1. **Structured, efficient output** — TOON format balances readability with token economy
2. **Contextual guidance** — Help blocks explain next steps within each response
3. **Reliable state tracking** — Generation-prefixed UIDs let agents detect outdated references

## Core Commands

| Category | Examples |
|----------|----------|
| Navigation | `open <url>`, `snapshot`, `scroll <dir>`, `back` |
| Interaction | `click @<uid>`, `fill @<uid> <text>`, `type <text>` |
| Page Management | `pages`, `newpage <url>`, `selectpage <id>` |
| Performance | `lighthouse`, `perf-start`, `heap <path>` |
| Bridge Control | `start`, `stop` |

## Example Workflow

```bash
$ chrome-devtools-axi open https://example.com
# Returns page title, accessibility tree, and suggestions

$ chrome-devtools-axi click @g1:1
# Executes action on previously captured element
```

## Benchmark

Per AXI browser benchmark (490 runs, 14 tasks, Claude Sonnet 4.6):

* `chrome-devtools-axi`: 100% success, $0.074/task, 21.5s, 4.5 turns
* MCP variants: 99–100% success, $0.091–$0.120/task

Cost reduction ~18–38% vs MCP at comparable reliability.
