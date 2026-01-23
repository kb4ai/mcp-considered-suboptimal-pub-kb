# MCP Considered Suboptimal: Core Thesis

**TL;DR:** MCP bloats context, making LLMs slower, dumber, and more expensive. CLI/SDK tools are better.

---

## The Problem: MCP is Threefold Bad

| Issue | Mechanism | Impact |
|-------|-----------|--------|
| **Cost** | More tokens consumed | Higher API bills |
| **Quality** | Context saturation dilutes attention | Worse outputs, hallucinations |
| **Latency** | More tokens to process | Slower responses |
| **Compounding cost** | Lower quality, leads to errors accumulation, more tokens required to solve problem, more turn-arounds for agents (or they end up looping) | TODO clean up this line |

**Quality degradation is most insidious** — errors compound in agentic workflows.

**Expert consensus:** "Models do not get smarter when you give them more tools" (Theo, t3.gg)

---

## The Alternative: CLI/SDK Tools

| MCP Approach | CLI/SDK Approach |
|--------------|------------------|
| Load all tool definitions upfront | `--help` on demand or `tools_search(...)` fun |
| All output goes through model | Model can decida on how data be processed without need of directly rewviewing all that data (pipes, `jq`, `yq`, `sk`, `rg`, scripting) |
| Static tool definitions | Agents write ad-hoc scripts |
| Fixed endpoints | Continous adaptation and optimization |
| Protocol overhead | Pre-trained programming/git knowledge |

---

## Core Statements

1. **Context efficiency > raw token price** — higher per-token-cost model may be cheaper, because smarter decisions = less tokens to solve problem = fewer steps = fewer turn arounds for agents = cheaper overall or maybe even faster

2. **CLI tools leverage pre-training** — Models already know python, lua, js/ts, bash, git, grep, unix tools; no definitions needed

3. **Self-documenting beats pre-loaded** — `tool --help`/`search_tools(...)` is loading on demand without protocol overhead

4. **Code execution enables evolution** — Agents can optimize their own workflows; MCP tools are static

5. **Aggregators don't solve bloat** — Docker/Microsoft gateways, MetaMCP consolidate endpoints but still load all definitions, don't give scripting/programmability flexibilty, require processing all output as is by LLMs, and fundamentally as intermadiary like CLI tools (e.g. cli wrappers for existing mcp tools or directly to apis, etc)

6. **Security via sandboxing** — OS-level isolation (bubblewrap, sandbox-exec) enables safe code execution

7. **Reliabilty, security via asserts and sanity checks** — ability to program constraints, asserts, etc into CLI wrappers or own CLI wrappers around CLI wrappers, or functions to interface SDKs so users or even LLM can introduce additional sanity checks, **programmatic** validation of inputs, parameters, permissions before exeuction...

8. **Integration costs** - CLI tools are easier to produce, maintain in long term, build testing, run static dyanmic analyzers, fuzzers , etc...

---

## Further Reading

* [README.md](README.md) — Full argument with quotes
* [FAQ.md](FAQ.md) — Aggregators, lazy loading, sandboxing, self-optimization
* [mcp-critique-sources.md](mcp-critique-sources.md) — Industry voices collection
* [cli-sdk-over-context-bloat.md](cli-sdk-over-context-bloat.md) — Detailed analysis
* [archived-resources/](archived-resources/) — Primary sources with timestamps

---

*Part of [MCP Considered Suboptimal](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb)*
