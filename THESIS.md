# MCP Considered Suboptimal: Core Thesis

**TL;DR:** MCP bloats context, making LLMs slower, dumber, and more expensive. CLI/SDK tools are better.

---

## The Problem: MCP is Fourfold Bad

| Issue | Mechanism | Impact |
|-------|-----------|--------|
| **Cost** | More tokens consumed | Higher API bills |
| **Quality** | Context saturation dilutes attention | Worse outputs, hallucinations |
| **Latency** | More tokens to process | Slower responses |
| **Compounding** | Lower quality → wrong direction → more steps → error accumulation → recovery loops | Multiplied waste |

**Compounding is most insidious** — in agentic workflows, one bad decision cascades:

```
Wrong tool choice → partial result → retry with different tool →
still wrong → LLM "explores" → 5 steps become 15 → context bloats further → quality degrades more
```

**Expert consensus:** "Models do not get smarter when you give them more tools" (Theo, t3.gg)

---

## The Alternative: UNIX-Philosophy CLI Tools

Not just "any CLI" — tools designed for composability:

| Principle | What It Means | Why It Matters |
|-----------|---------------|----------------|
| **KISS** | 3-5 focused operations, not 20+ | Less to load, less to confuse |
| **JSON/JSONL output** | Machine-readable, pipe to `jq` | Filter data BEFORE it hits context |
| **Self-documenting** | `--help` / `usage` on demand | Load docs only when needed |
| **Shell-first** | Standard CLI, no special integration | Works with any agent that has bash |
| **Composable** | Pipes, filters, scripts | Agents chain tools freely |
| **Leverage pre-training** | bash, git, jq already known | No protocol overhead to learn |

| MCP Approach | CLI/SDK Approach |
|--------------|------------------|
| Load all tool definitions upfront | `--help` on demand, `search_tools(...)` |
| All output goes through model | Filter first (pipes, [`jq`][jq], [`yq`][yq], [`rg`][ripgrep], [`sk`][skim]/[`fzf`][fzf]) |
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

9. **Executors minimize latency** — Keep slow actors (LLM inference) out of fast loops (API chaining, filtering); a 4-call MCP workflow becomes 1 executor call with 97% fewer tokens ([details](time-travel-latency.md))

10. **The market is converging on CLI** — Even when MCP is available, practitioners choose CLI. Firecrawl maintains both MCP and CLI; for their [Claude Code marketplace plugin](https://github.com/anthropics/claude-plugins-official/blob/261ce4fba4f2c314c490302158909a32e5889c88/.claude-plugin/marketplace.json#L643C1-L652C6) (in Anthropic's own repo), they built a [Skill+CLI integration](https://github.com/firecrawl/firecrawl-claude-plugin/blob/684b975c8cc6bd0fcfa96f787900bf87fffeef57/README.md), not MCP

---

## Further Reading

* [README.md](README.md) — Full argument with quotes
* [mcp-alternatives.md](mcp-alternatives.md) — CLI tools that replace MCP servers
* [time-travel-latency.md](time-travel-latency.md) — Latency analysis: why executors beat MCP
* [FAQ.md](FAQ.md) — Aggregators, lazy loading, sandboxing, self-optimization
* [mcp-critique-sources.md](mcp-critique-sources.md) — Industry voices collection
* [cli-sdk-over-context-bloat.md](cli-sdk-over-context-bloat.md) — Detailed analysis
* [archived-resources/](archived-resources/) — Primary sources with timestamps

---

*Part of [MCP Considered Suboptimal](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb)*

[jq]: https://github.com/jqlang/jq
[yq]: https://github.com/mikefarah/yq
[ripgrep]: https://github.com/BurntSushi/ripgrep
[skim]: https://github.com/skim-rs/skim
[fzf]: https://github.com/junegunn/fzf
