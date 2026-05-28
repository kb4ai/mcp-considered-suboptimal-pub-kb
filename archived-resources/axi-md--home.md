---
source_url: https://axi.md/
title: "AXI: Agent eXperience Interface"
author: "Kun Chen (@kunchenguid)"
publication_date: "~2026 (pre-2026-05)"
archive_date: "2026-05-17"
archived_by: "Claude Code (Opus 4.7)"
fetch_status: "ok"
---

# AXI: Agent eXperience Interface

**Source:** https://axi.md/
**Creator:** Kun Chen ([@kunchenguid on X/Twitter](https://x.com/kunchenguid))
**Archived:** 2026-05-17

---

## What is AXI?

AXI is a framework of **10 design principles for creating CLI tools optimized for AI agent interactions**. Rather than debating CLI versus MCP (Model Context Protocol), AXI proposes that *principled design of agent-tool interfaces matters more than the underlying protocol choice*.

The core premise: **"Neither CLI nor MCP gives [agents] enough love."** AXI achieves the reliability advantages MCP promises while maintaining the cost efficiency of CLI-based approaches.

## The 10 Principles

Organized into four categories:

**Efficiency:**

1. Token-efficient output (TOON format for ~40% savings over JSON)
2. Minimal default schemas (3–4 fields per item, not 10+)
3. Content truncation with size hints and escape hatches

**Robustness:**

4. Pre-computed aggregates (e.g., `totalCount`, CI summaries)
5. Definitive empty states (explicit "0 results")
6. Structured errors & exit codes (idempotent, no interactive prompts)

**Discoverability:**

7. Ambient context (self-install session hooks)
8. Content first (live data before help text)
9. Contextual disclosure (next-step commands in output)
10. Consistent help access (concise `--help` per subcommand)

## Benchmark Results

**Browser Automation (490 runs, 14 tasks, Claude Sonnet 4.6):**

* `chrome-devtools-axi`: 100% success, $0.074/task, 21.5s, 4.5 turns
* MCP variants: 99–100% success, $0.091–$0.120/task

**GitHub API (425 runs, 17 tasks):**

* `gh-axi`: 100% success, $0.050/task
* MCP: 82–87% success, $0.101–$0.148/task

## Key Links

* [GitHub Repo](https://github.com/kunchenguid/axi)
* [gh-axi](https://github.com/kunchenguid/gh-axi)
* [chrome-devtools-axi](https://github.com/kunchenguid/chrome-devtools-axi)
* [GitHub Benchmark Study](https://github.com/kunchenguid/axi/blob/main/bench-github/published-results/STUDY.md)

## How to Try It

```bash
npx -y gh-axi                    # GitHub operations
npx -y chrome-devtools-axi       # Browser automation
npx skills add kunchenguid/axi   # Install AXI scaffolding
```
