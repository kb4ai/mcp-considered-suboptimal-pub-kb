# FAQ: MCP Alternatives & Advanced Patterns

*See [Core Thesis](THESIS.md) for concise summary.*

---

## "Isn't MCP's problem just token cost?"

No. The problem is **threefold**:

| Issue | Impact |
|-------|--------|
| **Cost** | More tokens = more $$$ |
| **Quality** | Context saturation → distracted model → worse outputs |
| **Latency** | More tokens = slower responses |

**Quality degradation is the most insidious:**

When models process 100k+ tokens of tool definitions, they become "distracted" — attention diluted across irrelevant context. This manifests as:

* Missing obvious solutions
* Hallucinating tool parameters
* Failing to compose tools effectively

**In agentic workflows, errors compound:**

* Lower quality step → wrong direction
* Wrong direction → more errors
* Recovery → more tokens + time
* May miss optimal path entirely

<!-- TODO: Archive sources showing quality degradation from context saturation -->
<!-- TODO: Find benchmark studies on model performance vs. context size -->

**The Opus 4.5 proof:**

Anthropic made Opus 4.5 the default for Claude Code despite higher per-token cost because:

* Higher intelligence per token → more accomplished per token
* Better decisions → fewer steps needed
* Net result: **cheaper overall**

This proves: **context efficiency > raw token price**

<!-- TODO: Archive Anthropic announcement about Opus 4.5 as Claude Code default -->
<!-- TODO: Find cost comparison studies: smart model + small context vs. cheap model + large context -->

---

## "What about MCP aggregators and gateways?"

**Projects:** Docker MCP Gateway, Microsoft MCP Gateway, MetaMCP, Magg, etc.

**Position:** These are **legacy architecture adapters**, not solutions:

* Aggregators consolidate endpoints but still load all tool definitions
* Gateways add auth/routing/K8s but don't address token bloat
* You're wrapping MCP with more MCP

> "Aggregation ≠ token reduction. Still exposes full definitions, just from single endpoint."

If you're going to use wrappers anyway, CLI/SDK wrappers are better because:

* Leverage model's pre-training on bash/git/grep
* Enable Unix-style composition (pipes, filters)
* Data filtered BEFORE reaching LLM context
* Benchmarks: CLI $0.37 vs MCP $0.48 for identical tasks

---

## "What about lazy loading / progressive discovery?"

**Projects:** Claude Code's Tool Search, lazy-mcp proxy, Speakeasy's Dynamic Toolsets

These DO reduce tokens (85-98%) but:

* Still MCP-on-MCP architecture
* Added complexity (search→describe→execute = 2-3x calls)
* +50% execution time trade-off

CLI/SDK approach is simpler:

* `tool --help` IS lazy loading (load docs only when needed)
* No protocol overhead
* Agents trained on these patterns already

---

## "How do we secure agent code execution?"

**Reference:** Anthropic's sandbox-runtime

Key points:

* OS-level sandboxing (macOS sandbox-exec, Linux bubblewrap)
* No container overhead
* Filesystem isolation (deny-read sensitive, allow-write explicit)
* Network isolation (domain allowlist)
* 84% reduction in permission prompts

Links:

* https://github.com/anthropic-experimental/sandbox-runtime
* https://github.com/kb4ai/claude-code-sandbox-runtime-pub-kb (examples)

Code execution + sandboxing = secure 98.7% token reduction

---

## "Can agents self-optimize their workflows?"

Yes — this is a key CLI/SDK advantage:

**Pattern:** Agent writes ad-hoc scripts for repeating workflows

* First time: multiple tool calls, exploration
* Agent notices pattern, writes script
* Subsequent: single script call

Example from research:

> "45s/7 calls initial → 5s/1 call scripted" (Armin Ronacher)

MCP can't do this — tool definitions are static.
CLI/SDK enables agent evolution.

---

## "Why not just use function calling?"

| Aspect | Function Calling | MCP | CLI/SDK |
|--------|-----------------|-----|---------|
| Setup | Minimal | High (server + protocol) | None (existing tools) |
| Token cost | Per-call definition | All upfront | On-demand (--help) |
| Composition | Limited | Protocol-bound | Unix pipes |
| Agent learning | None | None | Pre-trained knowledge |

Function calling for simple cases, CLI/SDK for complex workflows.
MCP is the worst of both worlds for token efficiency.

---

*See also: [MCP Critique: Sources & Commentary](mcp-critique-sources.md) for comprehensive sourcing.*
