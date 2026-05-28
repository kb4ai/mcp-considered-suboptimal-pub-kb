# AXI (Agent eXperience Interface): A Concrete Spec for Agent-Friendly CLIs

**Date:** 2026-05-17
**Author:** Research note (Claude Code, Opus 4.7)
**Status:** Investigation summary for repo thesis

---

## TL;DR

**AXI** is a 10-principle specification by **Kun Chen** ([@kunchenguid](https://x.com/kunchenguid)) for designing CLI tools that AI agents can use efficiently. Published at [axi.md](https://axi.md/), with reference implementations [`gh-axi`](https://github.com/kunchenguid/gh-axi) and [`chrome-devtools-axi`](https://github.com/kunchenguid/chrome-devtools-axi). Already adopted by **Opera Software** in [`opera-browser-cli`](https://github.com/operasoftware/opera-browser-cli).

Published benchmarks show AXI-style CLIs beat MCP equivalents on **cost (33–66% cheaper)**, **reliability (100% vs 82–87% success)**, and **turn count** — empirically reinforcing this repo's thesis.

AXI is **not** the same as [agentexperience.ax](https://agentexperience.ax/) — that's a broader, methodology-focused movement convened by Netlify ("AX" as a discipline parallel to UX/DX). AXI is the concrete technical spec; AX is the umbrella culture/process movement. They are aligned and complementary.

---

## What AXI Is — In Plain Terms

Strip the acronym and AXI says:

> When a CLI is going to be driven by an LLM agent rather than a human, you should redesign its output shape, its defaults, its errors, and its help text — because the agent has a **token budget**, a **turn budget**, and **no eyeballs**. A normal CLI wastes all three.

AXI is a CLI design discipline, not a new protocol. There is no "AXI runtime," no daemon, no schema registry. It's just: *here are 10 things to do when your CLI will be consumed by an agent*.

Crucially, AXI **sidesteps the CLI-vs-MCP holy war**. Its premise is: *"Neither CLI nor MCP gives [agents] enough love."* — meaning the protocol layer matters less than how you design the surface. But the empirical answer keeps coming out the same: when both an MCP server and an AXI-style CLI exist for the same backend, the CLI wins on cost and reliability. The two existing reference implementations (`chrome-devtools-axi`, `opera-browser-cli`) literally **wrap MCP servers behind a CLI** to apply AXI principles, because the MCP interface alone wasn't agent-ergonomic enough.

---

## The 10 AXI Principles

Grouped into four categories:

### Efficiency

1. **Token-efficient output** — Use [TOON](https://toonformat.dev/) format (~40% smaller than JSON). Tabular, indentation-based.
2. **Minimal default schemas** — Return 3–4 fields per item by default, not 10+. Provide `--full` for everything.
3. **Content truncation** — Cut long fields, but emit size hints (`[truncated, 12kb more available via --full]`).

### Robustness

4. **Pre-computed aggregates** — Include `totalCount`, CI status summaries, etc. so the agent doesn't have to ask follow-up questions.
5. **Definitive empty states** — Explicitly say "0 results found" instead of returning nothing. Eliminates "did the command fail or is it empty?" ambiguity.
6. **Structured errors & exit codes** — Idempotent operations; no interactive prompts; machine-readable error payloads.

### Discoverability

7. **Ambient context** — Self-installing session hooks that surface state (e.g. "you are in repo X on branch Y") before the agent invokes anything.
8. **Content first** — Running the bare command shows live data, not help text. Help is opt-in.
9. **Contextual disclosure** — Each command's output suggests the next plausible commands. Effectively a runtime tutorial baked into responses.

### Help access

10. **Consistent help access** — Concise per-subcommand `--help` available everywhere, identical shape.

---

## Concrete Examples: How AXI Differs from a Normal CLI

### `gh-axi` vs `gh`

| Concern | Normal `gh` | `gh-axi` |
|---|---|---|
| Output | Human table or verbose JSON | TOON, ~40% smaller |
| List fields | All 15+ fields | 3–4 most-relevant |
| Empty results | Silent or blank table | Explicit `0 results` row |
| Next steps | None | Each response suggests follow-up commands |
| Errors | Mixed stderr/exit codes | Structured + idempotent guarantees |

**Benchmark (425 runs, 17 tasks):**

* `gh-axi`: **100% success, $0.050/task**
* MCP GitHub tools: **82–87% success, $0.101–$0.148/task**

That's a ~3x cost reduction and a 13–18 percentage-point reliability gain.

### `chrome-devtools-axi` vs `chrome-devtools-mcp`

This is the most interesting case: `chrome-devtools-axi` **wraps the MCP server** but exposes a CLI. Same backend, different interface — and the CLI wins.

Key innovations:

* **Generation-prefixed element refs** (`@g1:1`) — when the page re-renders, refs from previous generation are explicitly invalidated rather than silently misfiring on a stale DOM node.
* **Unified commands** — `open <url>` does navigate + snapshot + return accessibility tree in one round trip, rather than three MCP calls.
* **Suggestion footers** — Output ends with "next likely action" hints.

**Benchmark (490 runs, 14 tasks, Claude Sonnet 4.6):**

* `chrome-devtools-axi`: **100% success, $0.074/task, 4.5 turns**
* MCP variants: **99–100% success, $0.091–$0.120/task**

### `opera-browser-cli` (corporate adoption signal)

Opera Software shipped an AXI-compliant CLI as the official agent interface to their browser. This is significant: it's the first **vendor** (not hobbyist) adoption of AXI. It signals AXI is on a trajectory from "one guy's spec" toward "de-facto convention," much like how design systems propagate from individual designers to corporate standards.

---

## How This Reinforces This Repo's Thesis

This repo argues (see `THESIS.md`, `cli-sdk-over-context-bloat.md`, `mcp-alternatives.md`) that MCP is suboptimal because:

* MCP bloats context (cost, quality, latency)
* CLI/SDK tools with UNIX-philosophy composability win
* Filtering/aggregation should happen *before* tokens hit the model

AXI **operationalizes** this thesis with:

### 1. A Named, Numbered Spec

This repo argued "agentic-friendly CLIs are the answer" but didn't have a checklist. AXI provides one: 10 principles, four categories. Now there's something concrete to point implementers at. Add it to `mcp-alternatives.md` as a recommended design standard.

### 2. Empirical Validation

The thesis was theoretical (token economics, attention dilution). AXI publishes **head-to-head benchmarks** across 915 total runs showing AXI CLIs beat MCP equivalents on cost (-18% to -66%) and reliability (+0 to +18 percentage points). This is the evidence the thesis needed.

### 3. The "MCP-Wrapper-As-CLI" Pattern

Most damning: the AXI reference browser tool literally **takes an existing MCP server (`chrome-devtools-mcp`), wraps it in a CLI, and beats raw MCP on every metric**. Same backend, same capabilities, different surface — and the CLI surface wins. This is the cleanest possible refutation of "MCP is sufficient if you just use it well."

### 4. Convergence with TOON

This repo already archived TOON (`archived-resources/toon--*`) as a context-efficient encoding. AXI principle #1 mandates TOON. So AXI = TOON + 9 more CLI-design principles. The two efforts are mutually reinforcing: TOON solves the *encoding* problem, AXI solves the *interface design* problem. Together they form a coherent stack.

### 5. Corporate Validation via Opera

The thesis predicts vendors will eventually ship CLI-first agent interfaces. Opera's adoption of AXI is an early concrete data point that this prediction is materializing.

---

## Cross-References

Within this repo:

* [`THESIS.md`](../THESIS.md) — the core argument AXI empirically validates
* [`cli-sdk-over-context-bloat.md`](../cli-sdk-over-context-bloat.md) — token-economics rationale AXI principles 1–3 implement
* [`mcp-alternatives.md`](../mcp-alternatives.md) — should list AXI as a recommended design spec
* [`archived-resources/ainoya--why-cli-instead-of-mcp.md`](../archived-resources/ainoya--why-cli-instead-of-mcp.md) — Ainoya's "small CLI tools" argument aligns with AXI principles 2 & 8
* [`archived-resources/anthropic--code-execution-with-mcp.md`](../archived-resources/anthropic--code-execution-with-mcp.md) — Anthropic's programmatic tool calling addresses the same problem at a different layer
* [`archived-resources/toon--github-repo.*`](../archived-resources/) — TOON, the encoding AXI principle #1 mandates

External:

* https://axi.md/ — AXI homepage
* https://github.com/kunchenguid/axi — Spec + benchmark code
* https://github.com/kunchenguid/gh-axi — Reference GitHub CLI
* https://github.com/kunchenguid/chrome-devtools-axi — Reference browser CLI
* https://github.com/operasoftware/opera-browser-cli — Opera's adoption
* https://toonformat.dev/ — TOON spec
* https://agentexperience.ax/ — Broader AX movement (Netlify-convened)

---

## Open Questions / Future Work

* Is there an AXI conformance test suite? Currently principles are prose, not testable.
* Will MCP itself adopt AXI principles (e.g. TOON output, contextual disclosure) at the protocol level? If yes, the CLI-vs-MCP framing collapses.
* How does AXI relate to Anthropic's "programmatic tool calling" (Sonnet 4.6)? Both address agent-tool ergonomics but at different layers — AXI at the tool surface, programmatic tool calling at the model's invocation strategy. They appear complementary.
* Does the `agentexperience.ax` (Netlify) effort have a competing or compatible spec? Worth tracking.

---

## Summary Table

| Layer | Concrete Artifact | Maintainer |
|---|---|---|
| Encoding | TOON format | toonformat.dev |
| Tool surface design | AXI (10 principles) | Kun Chen (axi.md) |
| Reference impls | gh-axi, chrome-devtools-axi | Kun Chen |
| Corporate adoption | opera-browser-cli | Opera Software |
| Broader movement | "Agent Experience" discipline | Netlify-convened community |
| Model-side complement | Programmatic tool calling (Sonnet 4.6) | Anthropic |

AXI sits in the middle of a coherent stack. This repo's thesis sits one level above it, arguing the whole stack matters more than MCP does.
