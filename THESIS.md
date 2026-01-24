# MCP Considered Suboptimal: Core Thesis

**TL;DR:** MCP bloats context, making LLMs slower, dumber, and more expensive. CLI/SDK tools are better.

---

## The Problem: MCP is Threefold Bad

| Issue | Mechanism | Impact |
|-------|-----------|--------|
| **Cost** | More tokens consumed | Higher API bills |
| **Quality** | Context saturation dilutes attention | Worse outputs, hallucinations |
| **Latency** | More tokens to process | Slower responses |
| **Compounding** | Lower quality → error accumulation → more tokens to recover → agent loops | Multiplied waste |

**Quality degradation is most insidious** — errors compound in agentic workflows.

**Expert consensus:** "Models do not get smarter when you give them more tools" (Theo, t3.gg)

---

## The Alternative: CLI/SDK Tools

| MCP Approach | CLI/SDK Approach |
|--------------|------------------|
| Load all tool definitions upfront | `--help` on demand, `search_tools(...)` |
| All output goes through model | Model decides processing without reviewing all data (pipes, `jq`, `yq`, `rg`, `sk`/`fzf`, scripts) |
| Static tool definitions | Agents write ad-hoc scripts |
| Fixed endpoints | Continuous adaptation and optimization |
| Protocol overhead | Pre-trained programming/git knowledge |

---

## Core Statements

1. **Context efficiency > raw token price** — higher per-token-cost model may be cheaper: smarter decisions → fewer tokens → fewer steps → fewer agent turnarounds → cheaper overall (and often faster)

2. **CLI tools leverage pre-training** — Models already know python, lua, js/ts, bash, git, grep, unix tools; no definitions needed

3. **Self-documenting beats pre-loaded** — `tool --help`/`search_tools(...)` is loading on demand without protocol overhead

4. **Code execution enables evolution** — Agents can optimize their own workflows; MCP tools are static

5. **Aggregators don't solve bloat** — Docker/Microsoft gateways, MetaMCP consolidate endpoints but still load all definitions, lack scripting/programmability flexibility, require LLMs to process all output as-is, and are fundamentally intermediaries (like CLI wrappers for MCP tools or direct API calls)

6. **Security via sandboxing** — OS-level isolation (bubblewrap, sandbox-exec) enables safe code execution

7. **Reliability via programmatic checks** — CLI wrappers enable constraints, asserts, sanity checks; users or LLMs can add **programmatic** validation of inputs, parameters, and permissions before execution

8. **Lower integration costs** — CLI tools are easier to produce, maintain long-term, test, and analyze (static/dynamic analyzers, fuzzers)

---

## Further Reading

* [README.md](README.md) — Full argument with quotes
* [FAQ.md](FAQ.md) — Aggregators, lazy loading, sandboxing, self-optimization
* [mcp-critique-sources.md](mcp-critique-sources.md) — Industry voices collection
* [cli-sdk-over-context-bloat.md](cli-sdk-over-context-bloat.md) — Detailed analysis
* [archived-resources/](archived-resources/) — Primary sources with timestamps

---

*Part of [MCP Considered Suboptimal](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb)*
