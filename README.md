# MCP Considered Suboptimal (A technical analysis — not a software project)

**Premise:** Anthropic's Model Context Protocol (MCP) bloats context windows and makes LLMs dumber. Better alternative: give LLMs CLI tools they can script.

**Quick reference:** [Core Thesis](THESIS.md) — concise summary to share

---

## The Smoking Gun

In November 2025, Anthropic published a blog post effectively admitting MCP doesn't scale:

> **150,000 → 2,000 tokens. A 98.7% reduction.**

Their solution? Have agents write code instead of calling MCP tools directly.

Source: [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) (archived: [local copy](archived-resources/anthropic--code-execution-with-mcp.md))

---

## The Core Insight

> "Models do not get smarter when you give them more tools. They get smarter when you give them a small subset of really good tools."
> — Theo, t3.gg ([video transcript](archived-resources/theo-t3gg--anthropic-admits-mcp-sucks--transcript.md))

**MCP's Fatal Flaw:**

* Encourages adding hundreds of tools to context
* Each tool definition = tokens consumed before any work
* Intermediate results pass through model repeatedly
* No progressive discovery—all definitions loaded upfront

---

## The Alternative: CLI/SDK Tools

Instead of bloating context with MCP definitions, give LLMs:

| What | Why |
|------|-----|
| **Bash shell access** | Compose tools freely |
| **Self-documenting CLIs** | `tool --help` loads only what's needed |
| **JSON output** | Pipe to [`jq`][jq], filter locally |
| **SDK libraries** | Write code, not protocol calls |

> "Standard CLI tool callable from bash (...) `usage` command provides complete documentation—agents self-document by reading output (...) Output JSON for piping to `jq` (...) Unix philosophy of small, composable tools (...) Leverage existing Bash tool instead of creating new tool type (...) Solve the problems you actually encounter."
> — Carlo Zottmann, Linearis design principles ([archived](archived-resources/zottmann--linearis-linear-cli-built.md))

**Result:** Data stays in sandbox. Tokens stay minimal. Code is deterministic.

**Detailed analysis:** [CLI/SDK Over Context Bloat](cli-sdk-over-context-bloat.md)

---

## Key Numbers

| Metric | Value | Source |
|--------|-------|--------|
| Token reduction (code exec vs MCP) | **98.7%** | Anthropic |
| MCP servers with production features | **~2%** | HackerNoon |
| Recommended max tools per agent | **3-5** | Industry consensus |
| Linear MCP server token cost | **~13,000** | Linearis author |
| Equivalent CLI token cost | **~200** | Linearis author |

---

## Featured Quotes

**On Context Efficiency:**

> "LLMs aren't traditional software systems where more data equals better decisions. They're pattern-matching machines. Every token in context adds noise."
> — HackerNoon ([archived](archived-resources/hackernoon--98-percent-mcp-servers-wrong.md))

**On Software Industrialization:**

> "Technical debt is the pollution of the digital world, invisible until it chokes the systems that depend on it. In an era of mass automation, we may find that the hardest problem is not production, but stewardship. **Who maintains the software that no one owns?**"
> — Chris Loy ([archived](archived-resources/chrisloy--rise-of-industrial-software.md))

**On MCP's Design Flaws:**

> "Did you know MCP has no concept of OAuth at all? At all. Now, there's like 18 implementations of it because there's no way to do proper handshakes."
> — Theo, t3.gg

**On Practical Alternatives:**

> "Token budget matters: 13k tokens for tool definitions is prohibitive. Simplicity wins: 3-4 features beats 20+ for real workflows."
> — Carlo Zottmann, Linearis ([archived](archived-resources/zottmann--linearis-linear-cli-built.md))

---

## Repository Structure

```
.
├── README.md                          ← You are here
├── FAQ.md                             ← Advanced questions & patterns
├── mcp-critique-sources.md            ← Industry voices & references
├── cli-sdk-over-context-bloat.md      ← Detailed analysis & patterns
├── TODO.md                            ← Pending archival & research tasks
└── archived-resources/                ← Source material with timestamps
    ├── anthropic--code-execution-with-mcp.md
    ├── chrisloy--rise-of-industrial-software.md
    ├── devto--beyond-hype-mcp-limitations.md
    ├── hackernoon--98-percent-mcp-servers-wrong.md
    ├── medium--mcp-wrong-98-percent-cost-reduction.md
    ├── simonwillison--code-execution-mcp-commentary.md
    ├── theo-t3gg--anthropic-admits-mcp-sucks--transcript.md
    ├── zottmann--linearis-linear-cli-built.md
    └── artofsmart--anthropic-admits-mcp-wrong.md
```

All archives include `.url` (source pointer) and `.meta.json` (structured metadata) companions.

---

## Further Reading

* **[Core Thesis](THESIS.md)** — Concise summary of the argument (shareable)
* **[FAQ: MCP Alternatives & Advanced Patterns](FAQ.md)** — Aggregators, sandboxing, self-optimization
* **[MCP Critique: Sources & Commentary](mcp-critique-sources.md)** — Comprehensive collection of industry voices

---

## The Argument in Brief

1. **MCP bloats context** — 500+ tool definitions make models dumber
2. **Code execution works** — 98.7% token savings prove it
3. **CLIs are self-documenting** — `--help` on demand, not upfront
4. **Scripts are deterministic** — No hallucination in execution
5. **Industrialization needs stewardship** — Generic tools, custom composition
6. **Software engineering patterns apply** — APIs > Protocols

---

## Call to Action

When building for LLM agents:

1. **Prefer CLI tools** over MCP servers
2. **Expose `--help`** or `usage` commands
3. **Output JSON** for composability
4. **Limit scope** to 3-5 core operations
5. **Let agents script** their own workflows

The future is not bigger context windows. It's smarter tool design.

---

## Primary Sources

* **Anthropic Engineering Blog:** [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) (Nov 2025) ([archived](archived-resources/anthropic--code-execution-with-mcp.md))
* **Theo t3.gg:** [Anthropic admits they were wrong about MCP](https://www.youtube.com/watch?v=1piFEKA9XL0) (Nov 2025) ([archived](archived-resources/theo-t3gg--anthropic-admits-mcp-sucks--transcript.md))
* **HackerNoon:** [98% of MCP Servers Got This Wrong](https://hackernoon.com/98percent-of-mcp-servers-got-this-wrong-the-reason-why-the-protocol-never-worked) (Nov 2025) ([archived](archived-resources/hackernoon--98-percent-mcp-servers-wrong.md))
* **Chris Loy:** [The Rise of Industrial Software](https://chrisloy.dev/post/2025/12/30/the-rise-of-industrial-software) (Dec 2025) ([archived](archived-resources/chrisloy--rise-of-industrial-software.md))
* **Carlo Zottmann:** [Linearis: CLI Built for Agents](https://zottmann.org/2025/09/03/linearis-my-linear-cli-built.html) (Sep 2025) ([archived](archived-resources/zottmann--linearis-linear-cli-built.md))
* **Dev.to:** [Beyond the Hype: MCP Limitations](https://dev.to/ramkey982/beyond-the-hype-understanding-the-limitations-of-anthropics-model-context-protocol-for-tool-48kk) ([archived](archived-resources/devto--beyond-hype-mcp-limitations.md))
* **Simon Willison:** [Code Execution with MCP Commentary](https://simonwillison.net/2025/Nov/4/code-execution-with-mcp/) (Nov 2025) ([archived](archived-resources/simonwillison--code-execution-mcp-commentary.md))

---

*Archived 2026-01-23. All sources preserved with full attribution in `archived-resources/`.*

[jq]: https://github.com/jqlang/jq
