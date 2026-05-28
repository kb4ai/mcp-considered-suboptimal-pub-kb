---
source_url: https://t.me/llmaitools/3854
title: "TOON: Token-Oriented Object Notation (llmaitools Telegram post)"
author: "@llmaitools (Telegram channel)"
publication_date: "~2026-05 (pre-archive)"
archive_date: "2026-05-17"
archived_by: "Claude Code (Opus 4.7)"
fetch_status: "partial - Telegram public preview rendered via JS; content reconstructed from preview snippet + primary source"
---

# llmaitools Telegram post on TOON

**Source:** [t.me/llmaitools/3854](https://t.me/llmaitools/3854)
**Archived:** 2026-05-17

## Fetch note

Telegram's `/s/` public preview returned the channel-embed template without inline post text on both direct and `r.jina.ai` proxied fetches. Reconstructed content from the preview snippet that surfaced via WebFetch (mode=tme variant) plus the upstream sources the post links to (the toon-format GitHub repo and benchmark articles).

## Reconstructed summary

The post promotes **TOON (Token-Oriented Object Notation)** as a JSON alternative for LLM context windows, highlighting:

* "Sparse Trees, Dense Lists" design - YAML-style indentation for nested objects, CSV-style tabular headers for uniform arrays
* Official benchmark across 5,016 LLM calls: TOON 27.7 efficiency points / 76.4% accuracy / 2,759 tokens vs JSON 16.4 points / 4,587 tokens
* Best fit: large uniform arrays, tight token budgets, RAG and agent pipelines
* Cautions: "header decay" on wide rows; minified JSON sometimes matches TOON; reduced accuracy on shorter prompts
* Ecosystem: TypeScript, Python, Rust, Go ports; spec and playground on GitHub

## Linked / referenced resources

* https://github.com/toon-format/toon (reference implementation)
* https://github.com/toon-format/spec (spec)
* https://toonformat.dev/playground

## Why it matters for this repo

This post is the pointer that brought TOON to our attention as a data-layer (wire format) angle on the same problem MCP exposes at the protocol layer: too many tokens spent on syntactic overhead that doesn't carry information. See `ramblings/2026-05-17--toon-token-oriented-object-notation.md`.
