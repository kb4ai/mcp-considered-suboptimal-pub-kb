---
source_url: https://www.anthropic.com/news/claude-sonnet-4-6
title: "Introducing Claude Sonnet 4.6"
author: Anthropic
publication_date: 2026-02-17
access_date: 2026-02-20
content_type: official product announcement
---

# Introducing Claude Sonnet 4.6

**Published:** February 17, 2026
**Source:** https://www.anthropic.com/news/claude-sonnet-4-6
**Publisher:** Anthropic (official)

---

## Overview

Claude Sonnet 4.6 launched February 17, 2026, as Anthropic's most capable Sonnet model. It features a 1M token context window (beta) and represents a full upgrade across coding, computer use, long-context reasoning, agent planning, knowledge work, and design.

**Pricing:** $3/$15 per million tokens (same as Sonnet 4.5)

## Developer Platform Updates — Tool Use Features Now GA

The following features moved from beta to **generally available** with this release:

* **Code execution** — sandboxed execution environments
* **Memory tool** — persistent context across conversations
* **Programmatic tool calling** — Claude writes code to invoke tools in sandboxed containers instead of JSON function calls
* **Tool search** — on-demand tool discovery without loading all definitions upfront
* **Tool use examples** — concrete usage patterns beyond JSON schemas

### Web Search & Dynamic Filtering

> The API's web search and fetch tools now "automatically write and execute code to filter and process search results, keeping only relevant content in context — improving both response quality and token efficiency."

### Context Compaction

Context compaction (beta) "automatically summarizes older context as conversations approach limits, increasing effective context length."

## Key Benchmark Results

**Web Search Dynamic Filtering (powered by programmatic tool calling):**

| Benchmark | Model | Before | After | Improvement |
|-----------|-------|--------|-------|-------------|
| BrowserComp | Sonnet 4.6 | 33.3% | 46.6% | +13 pts |
| BrowserComp | Opus 4.6 | 45% | 61% | +16 pts |
| DeepSearchQA (F1) | Sonnet 4.6 | 52.6% | 59.4% | +7 pts |
| DeepSearchQA (F1) | Opus 4.6 | ~8% improvement | | |

**Average:** 11% accuracy improvement, 24% fewer input tokens

**User Preference (Claude Code testing):**

* 70% preferred Sonnet 4.6 over Sonnet 4.5
* 59% preferred it to Opus 4.5 (November 2025 frontier model)

**Coding Quality:**

* "More effectively read the context before modifying code"
* "Consolidated shared logic rather than duplicating it"
* "Significantly less prone to overengineering and laziness"
* "Meaningfully better at instruction following"

## Safety

Extensive safety evaluations concluded Sonnet 4.6 has "a broadly warm, honest, prosocial character, very strong safety behaviors, and no signs of major concerns."

Prompt injection resistance: Major improvement over 4.5; performs similarly to Opus 4.6.

---

## Relevance to Repository Thesis

This is the official announcement where Anthropic moved programmatic tool calling to GA — the culmination of their recognition that MCP-style tool definitions bloat context and degrade model performance. Key points:

1. **Anthropic itself is building escape hatches from MCP context bloat** — programmatic tool calling, tool search, dynamic filtering all exist because upfront tool loading hurts performance
2. **The 11% accuracy gain from filtering** validates our thesis that context pollution degrades quality — the model didn't get smarter, the information diet got cleaner
3. **Code execution as the default path** — Anthropic is making sandbox code execution the primary mechanism for tool orchestration, exactly what our CLI/SDK thesis advocates

---

*Archived from anthropic.com on 2026-02-20.*
