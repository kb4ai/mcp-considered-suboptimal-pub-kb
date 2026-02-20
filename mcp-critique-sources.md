# MCP Critique: Sources & Commentary

*See [Core Thesis](THESIS.md) for concise summary.*

A curated collection of industry voices questioning MCP's design decisions.

---

## Authoritative Critiques

### Armin Ronacher (Creator of Flask, Rye, uv)

**Source:** [Skills vs Dynamic MCP Loadouts](https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/) ([archived](archived-resources/ronacher--skills-vs-dynamic-mcp-loadouts.md))
**Source:** [Your MCP Doesn't Need 30 Tools](https://lucumr.pocoo.org/2025/8/18/code-mcps/) ([archived](archived-resources/ronacher--mcp-doesnt-need-30-tools.md))

Key insights:

> "Token cost: Well-designed MCPs still consume ~8k tokens"

> "Protocol instability: Servers change tool definitions frequently"

> "45s/7 calls initial → 5s/1 call scripted" (on code execution advantage)

**Position:** Agents should write tools using existing capabilities, not consume pre-defined MCP tools.

---

### Mario Zechner (Benchmarking Expert)

**Source:** [MCP vs CLI: Benchmarking Tools](https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/) ([archived](archived-resources/zechner--mcp-vs-cli-benchmarks.md))

Benchmark results:

| Tool | Avg Cost |
|------|----------|
| tmux (CLI) | $0.37 |
| MCP wrapper | $0.48 |

> "CLI tools leverage model pre-training knowledge"

> "Context pollution: MCPs flood with unnecessary output"

---

### LiquidMetal AI

**Source:** [If Your MCP is an API Wrapper, You're Doing It Wrong](https://liquidmetal.ai/casesAndBlogs/mcp-api-wrapper-antipattern/) ([archived](archived-resources/liquidmetal--mcp-api-wrapper-antipattern.md))

The API wrapper antipattern:

> "Wrong User Model: LLM guesses UUID from ambiguous 'John'"

> "4-step workflow (projects→users→search→create) for 1 action"

---

### Shrivu Shankar

**Source:** [Everything Wrong with MCP](https://blog.sshh.io/p/everything-wrong-with-mcp) ([archived](archived-resources/shankar--everything-wrong-with-mcp.md))

Security concerns:

> "No standard auth (18+ custom implementations)"

> "Dynamic tool redefinition (rug-pull attacks post-confirmation)"

> "Performance ∝ 1/context_size (more tools = worse accuracy)"

---

### ainoya.dev

**Source:** [Why CLI instead of MCP](https://ainoya.dev/posts/why-cli-instead-of-mcp/) ([archived](archived-resources/ainoya--why-cli-instead-of-mcp.md))

CLI philosophy:

> "MCP approach: Pass all Slack data to LLM [50k tokens raw JSON]"

> "CLI approach: Filter first [...] → [2k tokens relevant subset]"

---

### webctl (cosinusalpha)

**Source:** [webctl README — Why CLI Instead of MCP?](https://github.com/cosinusalpha/webctl)

On who controls context:

> "MCP browser tools have a fundamental problem: **the server controls what enters your context**. With Playwright MCP, every response includes the full accessibility tree plus console messages. After a few page queries, your context window is full."

> "CLI flips this around: **you control what enters context**."

**Position:** Browser automation should use CLI with built-in filtering (`--interactive-only`, `--within`, pipes to grep/jq) instead of MCP servers that dump entire page trees into context.

---

### Firecrawl (Claude Code Plugin Marketplace)

**Source:** [Anthropic's official marketplace](https://github.com/anthropics/claude-plugins-official/blob/261ce4fba4f2c314c490302158909a32e5889c88/.claude-plugin/marketplace.json#L643C1-L652C6) → [firecrawl-claude-plugin](https://github.com/firecrawl/firecrawl-claude-plugin/blob/684b975c8cc6bd0fcfa96f787900bf87fffeef57/README.md)

The finding: Firecrawl maintains **both** an [MCP server](https://github.com/firecrawl/.github/blob/eac6d8b43e11e1cc401a48e0e038a3c60fb53db9/profile/README.md) and a [CLI tool](https://github.com/firecrawl/cli). For their Claude Code plugin — hosted in **Anthropic's own official marketplace repo** — they chose **Skill + CLI**, not MCP.

> "This plugin adds the Firecrawl CLI as a skill to Claude Code"

**Position:** Even service providers with MCP servers prefer CLI for agent tooling when both options are available. ([detailed analysis](ramblings/2026-02-18--firecrawl-claude-marketplace-cli-over-mcp.md))

---

## Anthropic's Own Architectural Shift (February 2026)

### Programmatic Tool Calling Goes GA — Sonnet 4.6

**Source:** [Introducing Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) ([archived](archived-resources/anthropic--sonnet-4-6-announcement.md))
**Source:** [Advanced Tool Use Engineering Blog](https://www.anthropic.com/engineering/advanced-tool-use) ([archived](archived-resources/anthropic--advanced-tool-use-engineering.md))
**Source:** [Programmatic Tool Calling Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) ([archived](archived-resources/anthropic-docs--programmatic-tool-calling.md))

With the Sonnet 4.6 release (Feb 17, 2026), Anthropic moved programmatic tool calling from beta to GA. Claude now writes Python code to invoke tools in sandboxed containers instead of emitting JSON function calls. Intermediate results stay in the sandbox; only final output enters context.

Key results:

| Feature | Token Reduction | Accuracy Gain |
|---------|----------------|---------------|
| Programmatic tool calling | 37% (multi-tool workflows) | +5% on GIA benchmarks |
| Tool Search Tool | 85% (tool definitions) | Opus 4: 49% → 74% |
| Dynamic web search filtering | 24% (input tokens) | BrowserComp: +13 pts (Sonnet), +16 pts (Opus) |
| Extreme case (Cloudflare) | 98.7% (150K → 2K) | — |

From official docs:

> "Claude's training includes extensive exposure to code, making it effective at reasoning through and chaining function calls."

> "Tool results from programmatic invocations do not count toward your input/output token usage."

**Position:** MCP's creator is building layered escape hatches from MCP's own context bloat. Code execution is now the recommended path for multi-tool workflows.

### Third-Party Coverage of the Shift

* **Prompt Engineering (YouTube):** [Anthropic Just Killed Tool Calling](https://www.youtube.com/watch?v=8dVCSPXG6Mw) ([transcript](archived-resources/prompt-engineering-yt--anthropic-killed-tool-calling--transcript.md)) — 42K+ views, Feb 18, 2026. "LLMs are specifically trained with code. They are not trained for tool calling."
* **ai505.com:** [Anthropic Just Killed Traditional Tool Calling](https://ai505.com/anthropic-just-killed-traditional-tool-calling-here-s-what-replaces-it/) ([archived](archived-resources/ai505--anthropic-killed-traditional-tool-calling.md)) — "Anthropic didn't just ship a feature. They graduated a philosophy."
* **aatventure.news:** [Prompt Engineering | Anthropic Just Killed Tool Calling](https://aatventure.news/posts/prompt-engineering-anthropic-just-killed-tool-calling) ([archived](archived-resources/aatventure--anthropic-killed-tool-calling.md)) — Detailed technical analysis with CodeAct paper references
* **Recapio:** [Digest of Prompt Engineering video](https://recapio.com/digest/anthropic-just-killed-tool-calling-by-prompt-engineering) ([archived](archived-resources/recapio--prompt-engineering--anthropic-killed-tool-calling.md))

**Analysis:** [Rambling: Anthropic Graduates Programmatic Tool Calling — Thesis Validation](ramblings/2026-02-20--anthropic-graduates-programmatic-tool-calling-thesis-validation.md)

---

## From This Repository's Primary Sources

* **Anthropic Engineering:** [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) ([archived](archived-resources/anthropic--code-execution-with-mcp.md))
* **Theo t3.gg:** [Anthropic admits MCP sucks](https://www.youtube.com/watch?v=1piFEKA9XL0) ([archived](archived-resources/theo-t3gg--anthropic-admits-mcp-sucks--transcript.md))
* **HackerNoon:** [98% of MCP Servers Got This Wrong](https://hackernoon.com/98percent-of-mcp-servers-got-this-wrong-the-reason-why-the-protocol-never-worked) ([archived](archived-resources/hackernoon--98-percent-mcp-servers-wrong.md))
* **Chris Loy:** [The Rise of Industrial Software](https://chrisloy.dev/post/2025/12/30/the-rise-of-industrial-software) ([archived](archived-resources/chrisloy--rise-of-industrial-software.md))
* **Carlo Zottmann:** [Linearis: CLI Built for Agents](https://zottmann.org/2025/09/03/linearis-my-linear-cli-built.html) ([archived](archived-resources/zottmann--linearis-linear-cli-built.md))
* **Dev.to:** [Beyond the Hype: MCP Limitations](https://dev.to/ramkey982/beyond-the-hype-understanding-the-limitations-of-anthropics-model-context-protocol-for-tool-48kk) ([archived](archived-resources/devto--beyond-hype-mcp-limitations.md))
* **Simon Willison:** [Code Execution with MCP Commentary](https://simonwillison.net/2025/Nov/4/code-execution-with-mcp/) ([archived](archived-resources/simonwillison--code-execution-mcp-commentary.md))

---

## MCP Aggregator/Gateway Projects (for reference)

Projects that try to mitigate MCP issues (but don't solve fundamental token bloat):

* **Docker MCP Gateway** — container isolation, secrets management
* **Microsoft MCP Gateway** — K8s-native, session-aware routing
* **MetaMCP** — namespace-based aggregation
* **Magg** — self-modifying MCP with discovery tools

These add operational sophistication but don't address context efficiency.

---

## Token Optimization Research

| Technique | Reduction | Trade-off |
|-----------|-----------|-----------|
| Code execution (Anthropic) | 98.7% | Requires sandbox |
| Tool Search (Claude Code) | 95% | Built-in |
| Progressive disclosure | 96% | +2-3x calls |
| CLI --help | ~99% | Already available |

---

## Further Reading

* [Speakeasy: 100x Token Reduction](https://www.speakeasy.com/blog/how-we-reduced-token-usage-by-100x-dynamic-toolsets-v2)
* [SEP-1576: Token Bloat Mitigation](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1576)
* [MCP Context Bloat Analysis](https://jduncan.io/blog/2025-11-07-mcp-context-bloat/)

<!-- TODO: Archive the above sources to archived-resources/ -->

---

## Quality & Intelligence Research

<!-- TODO: Find and archive sources on:
- Model performance degradation vs. context size
- Attention dilution in large contexts
- Agentic workflow error compounding studies
- Opus 4.5 announcement as Claude Code default
- Cost studies: intelligent model + small context vs. cheap model + large context
- "Lost in the middle" phenomenon research
-->

---

## Security Critiques

<!-- TODO: Find and archive sources on:
- MCP security vulnerabilities documented
- Prompt injection via tool definitions
- OAuth/auth fragmentation in MCP ecosystem
-->

---

*Part of [MCP Considered Suboptimal](README.md). See also: [FAQ](FAQ.md) for quick answers.*
