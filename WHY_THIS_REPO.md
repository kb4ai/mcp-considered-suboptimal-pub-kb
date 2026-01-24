# Why This Repository?

*Quick reference for "why should I care?" and "how can I use this?"*

---

## The Situation

Anthropic created MCP (Model Context Protocol) to let LLMs use tools. Then in November 2025, they published a blog post effectively admitting it doesn't scale:

> **150,000 → 2,000 tokens. A 98.7% reduction.**

Their solution? Have agents write code instead of calling MCP tools directly.

This repository documents that admission, collects industry critiques, and catalogs better alternatives.

---

## Who Benefits?

| Audience | Value |
|----------|-------|
| **Developers building LLM agents** | Design patterns for token-efficient tools |
| **AI/ML engineers** | Industry consensus on MCP limitations |
| **Tech leads / architects** | Reference for MCP vs CLI/SDK decisions |
| **LLM agents themselves** | Curated context for learning better patterns |
| **Anyone debating MCP** | High signal-to-noise quote collection |

---

## Potential Uses

### 1. Feed to Your LLM Agent

Point your agentic coding assistant at this repo to update its understanding:

```
Read https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb
and update your tool-usage patterns accordingly.
```

The repo contains:

* Design patterns for CLI tools ([mcp-alternatives.md](mcp-alternatives.md))
* Latency analysis with diagrams ([time-travel-latency.md](time-travel-latency.md))
* Archived primary sources with quotes

### 2. Win Arguments Without Arguing

Instead of debating, share a link:

* **Quick summary:** [THESIS.md](THESIS.md)
* **Full argument:** [README.md](README.md)
* **Industry voices:** [mcp-critique-sources.md](mcp-critique-sources.md)

All quotes are archived with attribution and timestamps.

### 3. Learn Alternative Patterns

The repo documents specific alternatives:

| Pattern | Example |
|---------|---------|
| **CLI over MCP** | [Linearis](https://github.com/czottmann/linearis) (13k→200 tokens) |
| **MCP wrappers** | [slack-cli-mcp-wrapper](https://github.com/CLIAI/slack-cli-mcp-wrapper) |
| **Executor delegation** | [time-travel-latency.md](time-travel-latency.md) |
| **Sandboxed code execution** | [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) |

### 4. Reference for Technical Writing

All archived resources include:

* Original URLs
* Archive timestamps
* Full text/transcript
* Metadata JSON

Use as citations in your own articles, documentation, or internal RFCs.

---

## Key Numbers (Quick Reference)

| Metric | Value | Source |
|--------|-------|--------|
| Token reduction (code exec vs MCP) | **98.7%** | Anthropic |
| MCP servers with production features | **~2%** | HackerNoon |
| Recommended max tools per agent | **3-5** | Industry consensus |
| Linear MCP server token cost | **~13,000** | Carlo Zottmann |
| Equivalent CLI token cost | **~200** | Carlo Zottmann |
| CLI vs MCP cost for identical task | **$0.37 vs $0.48** | Mario Zechner |

---

## Why Not Just Use MCP Gateways/Aggregators?

Projects like Docker MCP Gateway, Microsoft MCP Gateway, MetaMCP exist but:

> Aggregation ≠ token reduction. Still exposes full definitions, just from single endpoint.

They solve operational problems (auth, routing, K8s) but not the fundamental token bloat. If you're wrapping anyway, CLI wrappers are better — they leverage models' pre-training on bash/git/grep.

---

## Share This Repository

### Telegram / Chat Template

```
🤖 MCP Considered Suboptimal

Anthropic admitted their Model Context Protocol doesn't scale:
150,000 → 2,000 tokens (98.7% reduction via code execution)

This repo collects:
• Industry critiques (Ronacher, Willison, t3.gg, etc.)
• Better alternatives (CLI/SDK tools, executors, wrappers)
• Archived sources with quotes

Useful for: LLM agent developers, architecture decisions,
or feeding to your AI assistant to learn better patterns.

https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb
```

### Twitter/X Template

```
Anthropic admitted MCP doesn't scale: 98.7% token reduction via code execution.

Curated collection of industry critiques + better alternatives (CLI/SDK tools, executors, wrappers).

Useful as reference or feed it to your LLM agent.

https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb
```

### LinkedIn Template

```
I've compiled a technical analysis repository on MCP (Model Context Protocol) limitations.

Key finding: Anthropic's own engineering blog shows 98.7% token reduction when using code execution instead of MCP tool calls.

The repo includes:
• Industry voices (Armin Ronacher, Simon Willison, Theo t3.gg)
• Alternative patterns (CLI tools, executors, sandboxing)
• Archived sources with full attribution

Useful for AI/ML engineers, tech leads making architecture decisions, or as curated context for your LLM agents.

https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb
```

---

## Contributing

* Share CLI tools that work well with LLM agents
* Report MCP servers you'd like to see replaced
* Submit archived resources with proper attribution

See [mcp-alternatives.md](mcp-alternatives.md) for contribution guidelines.

---

*Part of [MCP Considered Suboptimal](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb)*
