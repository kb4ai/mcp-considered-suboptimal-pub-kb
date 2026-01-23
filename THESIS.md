# MCP Considered Suboptimal: Core Thesis

**TL;DR:** MCP bloats context, making LLMs slower, dumber, and more expensive. CLI/SDK tools are better.

---

## The Problem: MCP is Threefold Bad

| Issue | Mechanism | Impact |
|-------|-----------|--------|
| **Cost** | More tokens consumed | Higher API bills |
| **Quality** | Context saturation dilutes attention | Worse outputs, hallucinations |
| **Latency** | More tokens to process | Slower responses |

**Quality degradation is most insidious** — errors compound in agentic workflows.

---

## The Evidence

1. **Anthropic's own data:** 150,000 → 2,000 tokens (98.7% reduction) when agents write code instead of calling MCP tools
2. **Industry benchmarks:** CLI $0.37 vs MCP $0.48 for identical tasks (Mario Zechner)
3. **Expert consensus:** "Models do not get smarter when you give them more tools" (Theo, t3.gg)

---

## The Alternative: CLI/SDK Tools

| MCP Approach | CLI/SDK Approach |
|--------------|------------------|
| Load all tool definitions upfront | `--help` on demand |
| Intermediate results through model | Data filtered locally (pipes, jq) |
| Static tool definitions | Agents write ad-hoc scripts |
| Protocol overhead | Pre-trained bash/git knowledge |

---

## Core Statements

1. **Context efficiency > raw token price** — Opus 4.5 is Claude Code default despite higher cost because smarter decisions = fewer steps = cheaper overall

2. **CLI tools leverage pre-training** — Models already know bash, git, grep; no definitions needed

3. **Self-documenting beats pre-loaded** — `tool --help` is lazy loading without protocol overhead

4. **Code execution enables evolution** — Agents can optimize their own workflows; MCP tools are static

5. **Aggregators don't solve bloat** — Docker/Microsoft gateways, MetaMCP consolidate endpoints but still load all definitions

6. **Security via sandboxing** — OS-level isolation (bubblewrap, sandbox-exec) enables safe code execution

---

## Key Numbers

| Metric | Value |
|--------|-------|
| Token reduction (code exec vs MCP) | **98.7%** |
| CLI vs MCP cost (benchmarked) | **$0.37 vs $0.48** |
| MCP servers with production features | **~2%** |
| Recommended max tools per agent | **3-5** |

---

## Further Reading

* [README.md](README.md) — Full argument with quotes
* [FAQ.md](FAQ.md) — Aggregators, lazy loading, sandboxing, self-optimization
* [mcp-critique-sources.md](mcp-critique-sources.md) — Industry voices collection
* [cli-sdk-over-context-bloat.md](cli-sdk-over-context-bloat.md) — Detailed analysis
* [archived-resources/](archived-resources/) — Primary sources with timestamps

---

*Part of [MCP Considered Suboptimal](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb)*
