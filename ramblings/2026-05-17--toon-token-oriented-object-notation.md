# TOON (Token-Oriented Object Notation) - and why it reinforces the "MCP is suboptimal" thesis

**Date:** 2026-05-17
**Author:** Claude Code (Opus 4.7), at the request of repo owner
**Status:** rambling / synthesis

Cross-refs:

* [THESIS.md](../THESIS.md)
* [cli-sdk-over-context-bloat.md](../cli-sdk-over-context-bloat.md)
* Archived sources: `archived-resources/toon--github-repo.md`, `archived-resources/toon--official-spec.md`, `archived-resources/telegram-llmaitools--toon-post.md`, `archived-resources/adamholter--toon-vs-json-critique.md`

---

## 1. What TOON is, in one sentence

TOON is a lossless, JSON-compatible serialization format that strips out JSON's per-row syntactic overhead (quotes, braces, repeated keys) by combining YAML-style indentation for nested objects with CSV-style tabular headers for uniform arrays - producing roughly 30-60% fewer tokens than JSON on tabular data with comparable or slightly better LLM accuracy.

## 2. The core trick: "Sparse Trees, Dense Lists"

JSON spends a huge fraction of its bytes on:

* Quoting every key and most string values
* Repeating every key once per array element
* Structural punctuation (`{`, `}`, `[`, `]`, `,`, `:`)

TOON keeps nested objects tree-like (one key per line, indented), but collapses uniform arrays into a **single header + comma-separated rows**, so field names appear *once* regardless of array length.

### Side-by-side example (from the official README)

**JSON - 4,587 tokens:**

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

**TOON - 2,759 tokens (-40%):**

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

Notice: field names appear **once** as `{id,name,distanceKm,...}`; the `[3]` tells the model the row count to validate against; no quotes, no per-row `{}`.

## 3. Benchmarks

From the official 5,016-LLM-call benchmark (`toon-format/toon`):

| Format          | Tokens (example) | Accuracy | Notes                                  |
|-----------------|------------------|----------|----------------------------------------|
| JSON            | 4,587            | 75.0%    | baseline                               |
| TOON            | 2,759 (-40%)     | 76.4%    | wins on both axes                      |
| Minified JSON   | (lower than TOON) | ~       | TOON is **+14.7%** vs minified JSON    |
| YAML            | similar          | ~        | TOON -5.7% vs YAML                      |
| XML             | much higher      | ~        | TOON -31.0% vs XML                      |

Per-model accuracy (TOON vs JSON): Claude Haiku 59.8 vs 57.4; Gemini Flash 96.7 vs 97.1; GPT-5 Nano 90.9 vs 89.0; Grok-4 58.4 vs 56.5.

Dataset highlights: time-series analytics 59.0% token reduction (22,245 -> 9,115); GitHub repo listings 42.3% reduction (15,144 -> 8,744).

## 4. Honest caveats (from Adam Holter's critique)

* **Wide-row "header decay":** with dozens of columns, the model can lose alignment because field names are no longer anchored to each value
* **Minified JSON can win** when data is deeply nested rather than tabular
* **Weak null handling**, thin ecosystem, low training-data exposure for models
* Holter's framing: *"a compression codec for prompts, not a new foundation for data engineering"*
* An arxiv benchmark (2603.03306) finds plain JSON still wins on one-shot generation in short contexts; TOON's advantage grows with scale

## 5. Why this matters for the repo thesis

This repo argues that **MCP bloats context windows** because it forces verbose JSON-RPC payloads, verbose tool schemas, and verbose tool results into the model's working memory - and that **CLI/SDK-style tool use** (programmatic tool calling, code-execution-with-MCP, AXI-style stdin/stdout) is materially cheaper.

TOON is independent evidence that **format-level overhead alone is a massive line item** in agent token spend:

* If just switching the *wire format for one tool result* saves ~40% tokens with the same data and same accuracy, then every tool-result envelope MCP ships in raw JSON is leaving ~40% on the floor before we even talk about the protocol overhead, tool-schema preamble, or JSON-RPC framing.
* The programmatic-tool-calling story (see `archived-resources/anthropic--code-execution-with-mcp.md`, `anthropic-docs--programmatic-tool-calling.md`) saves tokens by moving tool *invocation* out of context. TOON saves tokens by making the *data that does flow through context* denser. **They compose.**
* A CLI/AXI tool that emits TOON (or any tabular-dense format) on stdout, consumed inside a code-execution sandbox, would stack: protocol savings (no MCP envelope) + invocation savings (no per-call JSON tool block) + payload savings (TOON instead of JSON).
* This is consistent with the broader pattern documented in `cli-sdk-over-context-bloat.md`: the model doesn't need to see the syntactic skeleton of a structured-output protocol; it needs to see the *information*.

## 6. Where TOON fits in the repo's mental model

| Layer                     | JSON-RPC + MCP today        | Programmatic tool calling (Anthropic) | CLI/AXI + TOON (hypothetical stack) |
|---------------------------|-----------------------------|---------------------------------------|-------------------------------------|
| Tool discovery overhead   | full schema in every turn   | schema loaded once, referenced in code | manpage / `--help` once, referenced in code |
| Invocation cost           | JSON tool-use block         | Python call inside sandbox            | shell pipeline inside sandbox       |
| Result payload cost       | verbose JSON                | verbose JSON                          | TOON / compact tabular              |
| Net context spend         | high                        | lower (~37-98% in published cases)    | lower still (additive ~30-60%)      |

## 7. Action items for this repo

* [ ] Consider adding a short section on `cli-sdk-over-context-bloat.md` or `mcp-alternatives.md` that mentions TOON as the **payload-layer** complement to the **protocol-layer** critique
* [ ] If a future benchmark page is added, include TOON as a comparator alongside minified JSON and raw stdout
* [ ] Watch for the arxiv 2603.03306 follow-ups - the "prompt tax" finding (TOON's instructional overhead eats savings on short prompts) is exactly the kind of nuance worth surfacing

## 8. One-line takeaway

> TOON proves that even the **wire format** of LLM tool data is overpaying for syntax; MCP's JSON-RPC + per-call tool schemas are paying that tax *and several more on top*.
