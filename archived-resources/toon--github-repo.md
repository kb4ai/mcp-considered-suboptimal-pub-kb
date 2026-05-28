---
source_url: https://github.com/toon-format/toon
title: "toon-format/toon - Token-Oriented Object Notation (TOON)"
author: "Johann Schopplich"
publication_date: "2025-10 (initial); v3.0 2025-11-24"
archive_date: "2026-05-17"
archived_by: "Claude Code (Opus 4.7)"
fetch_status: "ok"
---

# toon-format/toon - Token-Oriented Object Notation (TOON)

**Source:** [github.com/toon-format/toon](https://github.com/toon-format/toon)
**Archived:** 2026-05-17
**Stars (at archive time):** ~24.3k
**License:** MIT

---

## What TOON is

> "Token-Oriented Object Notation is a compact, human-readable encoding of the JSON data model that minimizes tokens and makes structure easy for models to follow."

TOON is a lossless serialization of the JSON data model designed specifically for LLM prompts. It combines:

* YAML-style indentation for nested objects
* CSV-style tabular layout for uniform arrays of objects
* Array length declarations `[N]` and field-header lists `{f1,f2,...}` so models (and parsers) get explicit structure
* Minimal quoting

Design philosophy: **"Sparse Trees, Dense Lists"** - keep nested structures tree-like; collapse repetitive arrays into tables.

---

## Side-by-side example (from the README)

**JSON (4,587 tokens in the official benchmark mix):**

```json
{
  "context": {
    "task": "Our favorite hikes together",
    "location": "Boulder",
    "season": "spring_2025"
  },
  "friends": ["ana", "luis", "sam"],
  "hikes": [
    { "id": 1, "name": "Blue Lake Trail", "distanceKm": 7.5,
      "elevationGain": 320, "companion": "ana", "wasSunny": true },
    { "id": 2, "name": "Ridge Overlook", "distanceKm": 9.2,
      "elevationGain": 540, "companion": "luis", "wasSunny": false },
    { "id": 3, "name": "Wildflower Loop", "distanceKm": 5.1,
      "elevationGain": 180, "companion": "sam", "wasSunny": true }
  ]
}
```

**TOON equivalent (2,759 tokens - ~40% fewer):**

```
context:
  task: Our favorite hikes together
  location: Boulder
  season: spring_2025
friends[3]: ana,luis,sam
hikes[3]{id,name,distanceKm,elevationGain,companion,wasSunny}:
  1,Blue Lake Trail,7.5,320,ana,true
  2,Ridge Overlook,9.2,540,luis,false
  3,Wildflower Loop,5.1,180,sam,true
```

The savings come from: no repeated field names per row, no `{`/`}`/`,`/`"` syntactic overhead per value, no quoted keys, length declared once as `[3]`.

---

## Headline benchmarks (5,016 LLM calls)

* TOON: 76.4% accuracy, 2,759 tokens, 27.7 "efficiency points"
* JSON:  75.0% accuracy, 4,587 tokens, 16.4 "efficiency points"
* TOON uses ~39.9% fewer tokens on average than JSON
* vs JSON: -21.9% tokens; vs minified JSON: **+14.7%** (compact JSON beats TOON on tokens); vs YAML: -5.7%; vs XML: -31.0%

**Per-model accuracy (TOON vs JSON):**

* Claude Haiku: 59.8% vs 57.4%
* Gemini Flash: 96.7% vs 97.1%
* GPT-5 Nano: 90.9% vs 89.0%
* Grok-4: 58.4% vs 56.5%

**Dataset examples:**

* Time-series analytics: 59.0% token reduction (9,115 vs 22,245)
* GitHub repositories: 42.3% reduction (8,744 vs 15,144)

---

## When TOON wins / loses (per the README)

* **Wins:** uniform arrays of objects (tabular data), large repetitive datasets, retrieval/RAG output dumps.
* **Loses:** deeply nested or non-uniform data; minified JSON can beat TOON when nesting dominates.

---

## Ecosystem

* Spec: https://github.com/toon-format/spec
* Playground: https://toonformat.dev/playground
* npm: `@toon-format/toon`, CLI: `npx @toon-format/cli`
* Ports: Python, PHP, Rust, Go, Dart, InterSystems IRIS, etc.
