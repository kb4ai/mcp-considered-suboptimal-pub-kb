---
source_url: https://github.com/kunchenguid/gh-axi
title: "gh-axi: GitHub CLI for Agents"
author: "Kun Chen (kunchenguid)"
publication_date: "~2026 (pre-2026-05)"
archive_date: "2026-05-17"
archived_by: "Claude Code (Opus 4.7)"
fetch_status: "ok"
---

# gh-axi: GitHub CLI for Agents

**Source:** https://github.com/kunchenguid/gh-axi
**Author:** kunchenguid (Kun Chen)
**License:** MIT
**Archived:** 2026-05-17

---

## What is gh-axi?

`gh-axi` is a wrapper around GitHub's official `gh` CLI tool, designed specifically for autonomous AI agents. It enhances the standard CLI with:

* Token-efficient TOON output (structured formatting)
* Contextual next-step suggestions
* Structured error handling

**Requirements:** Node 20+, `gh` CLI, GitHub authentication.

## Key Differences from `gh` CLI

While `gh` is a general-purpose CLI built for humans, `gh-axi` optimizes for agent interactions by:

* Reducing token consumption (TOON encoding ~40% smaller than JSON)
* Providing actionable hints on next operations
* Returning minimal default schemas — agents request `--full` when needed
* Pre-computing aggregates (counts, CI status summaries)
* Structured non-interactive errors

This is critical for AI systems operating with limited context windows and constrained turn budgets.

## AXI Principles Demonstrated

The project explicitly references **AXI (Agent eXperience Interface)** and embodies:

* Clarity in structured output
* Efficiency in communication (TOON, minimal schemas)
* Guidance for autonomous decision-making (contextual disclosure)

## Core Commands

Subcommands cover: issue, PR, workflow run, workflow, release, repo, label, search, raw API. Each supports list/view/create/manage operations.

## Usage Examples

```bash
gh-axi issue list
gh-axi pr view 42
gh-axi run view 123456 --job 789012
```

## Benchmark Result

Per the AXI GitHub benchmark (425 runs, 17 tasks):

* `gh-axi`: 100% success, $0.050/task average
* MCP-based GitHub tooling: 82–87% success, $0.101–$0.148/task

## Repo Stats (at archive time)

47 stars, 5 forks
