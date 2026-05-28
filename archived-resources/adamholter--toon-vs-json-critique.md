---
source_url: https://adam.holter.com/toon-vs-json-for-llms-token-efficiency-retrieval-accuracy-and-where-it-actually-helps/
title: "TOON vs JSON for LLMs: Token Efficiency, Retrieval Accuracy, and Where It Actually Helps"
author: "Adam Holter"
publication_date: "2025-11-17"
archive_date: "2026-05-17"
archived_by: "Claude Code (Opus 4.7)"
fetch_status: "ok"
---

# TOON vs JSON for LLMs: Where It Actually Helps

**Source:** [adam.holter.com](https://adam.holter.com/toon-vs-json-for-llms-token-efficiency-retrieval-accuracy-and-where-it-actually-helps/)
**Author:** Adam Holter
**Published:** 2025-11-17
**Archived:** 2026-05-17

---

## Headline numbers

* "TOON often cuts token usage by something like 30 to 60 percent compared to JSON" on flat, repetitive data
* Models reportedly return **more accurate results** on certain retrieval tasks when given TOON instead of JSON (specific %'s not given by this author)

## Main critiques

1. **Wide-row brittleness** - removing repeated field names eliminates structural anchors; with dense datasets, models can lose column alignment ("header decay")
2. **Thin ecosystem** - tooling is small compared to JSON/YAML/XML
3. **Weak type handling** - null/undefined are not cleanly representable
4. **Limited benchmark depth** - existing benchmarks favor friendly structures; no independent tests on hundred-column analytic tables
5. **Training-data gap** - models have seen far less TOON than JSON

## When to use TOON

**Good fit:**

* Flat or near-flat data (user lists, logs, product catalogs)
* Cost-sensitive workflows hitting context limits
* Temporary prompt-only conversions

**Bad fit:**

* Nested or graph-shaped data
* Data requiring validation/schemas
* Storage or API contracts
* Wide tables with dozens of columns

## Author's framing

> "Treat TOON as a compression codec for prompts, not like a new foundation for data engineering."

This is the most useful critique angle: TOON is a prompt-layer optimization, not a replacement for JSON as an interchange format.
