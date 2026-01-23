# Building Small CLI Tools for AI Agents

**Author:** Naoki Ainoya
**Published:** December 6, 2025
**Source URL:** https://ainoya.dev/posts/why-cli-instead-of-mcp/
**Archived:** 2026-01-23

---

## Overview

The author advocates for CLI-based approaches over Model Context Protocol (MCP) servers for AI agent operations, emphasizing practical efficiency over feature richness.

## CLI vs. MCP Comparison

### MCP Approach

* Designed to pass rich, comprehensive information into LLM context
* Requires server-side code modifications for behavior changes
* Better suited for operations requiring complex state management

### CLI Approach

* Enables pre-filtering of data using Unix pipeline processing before AI processing
* Adjustable through prompt/configuration modifications
* Described as more "AI Native" for read operations like log checking or document retrieval

## Key Philosophy

The author frames this as the "economics of information"—since LLM context windows are finite and costly, filtering unnecessary data *before* reaching the model improves both accuracy and cost efficiency. Rather than sending all available information, humans intentionally narrow scope using Unix pipeline tools.

## Key Quotes

> "MCP approach: Pass all Slack data to LLM [50k tokens raw JSON]"

> "CLI approach: Filter first [...] → [2k tokens relevant subset]"

## Practical Example

The author references filtering Slack logs:

```bash
slack-cli log --channel "dev-ops" | grep "ERROR" | tail -n 20
```

This demonstrates how targeted queries reduce noise compared to comprehensive data dumps.

## Token Comparison

| Approach | Token Usage |
|----------|-------------|
| MCP (raw JSON dump) | ~50,000 tokens |
| CLI (filtered subset) | ~2,000 tokens |
| **Reduction** | **96%** |

## Tools Created

The author built CLI utilities in Go for Slack, Atlassian, and Esa integrations, available on GitHub.

---

**Archive Notes:**

This article provides a clear philosophical foundation for CLI-first design. The 50k→2k token comparison (96% reduction) demonstrates the core efficiency argument. Key insight: Unix pipes enable pre-filtering before LLM context consumption, something MCP's "pass everything" approach cannot achieve.
