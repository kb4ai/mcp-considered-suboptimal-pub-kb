# Tool-Surface Entropy

> "This isn't MCP vs CLI; the real variable is whether you control tool surface entropy or let it explode."
> — [Carsten Lindstedt](archived-resources/carsten-lindstedt-linkedin--tool-surface-entropy.md), LinkedIn (Mar 2026)

A unifying framing for the whole MCP critique.

---

## The Variable

**Tool-surface entropy** = the size, unpredictability, and selection cost of the action space the model can choose from at any decision point.

Higher entropy →

* more tokens spent on tool definitions / discovery
* higher selection ambiguity → worse tool choice
* deeper error-recovery loops when the wrong tool was picked
* context-window poisoning even before the first real step runs

Lower entropy →

* fewer tokens spent on "what could I do"
* deterministic dispatch via code / shell / known interface
* short, recoverable chains

## Why This Re-Frames "MCP vs CLI"

The argument isn't categorical. It's about which architecture **defaults to low entropy** and which **defaults to high entropy**:

| Architecture | Default entropy posture | Why |
|---|---|---|
| **Naive large MCP** | High | Injects N tool schemas into context up-front. Every action lives in a flat N-wide selection space. |
| **MCP with progressive disclosure** | Medium | Schemas loaded on demand — but the model now has to *retrieve* the right tool, and retrieval is unreliable at scale ([Carsten, 2026](archived-resources/carsten-lindstedt-linkedin--tool-surface-entropy.md)). Entropy is moved, not removed. |
| **MCP via programmatic tool calling (code execution)** | Low | Model writes code; tool calls happen via function names in a code environment, not via injected schemas. Anthropic's own architectural shift ([Code Execution with MCP, Nov 2025](archived-resources/anthropic--code-execution-with-mcp.md); [Sonnet 4.6 GA, Feb 2026](archived-resources/anthropic--sonnet-4-6-announcement.md)). |
| **CLI / Skills** | Low | Each invocation scopes action space to one command. Discovery is execution: `tool --help \| grep -A3 thing`. The action space is implicitly bounded by the syscall surface, not preloaded. |

**Key consequence:** CLI/Skills win by *making low entropy the path of least resistance*. MCP can reach low entropy too — but only by adopting code-execution patterns that look more and more like calling a CLI.

## Mechanisms That Control Entropy

1. **Scope by call site, not by manifest.** Don't preload a tool catalog; let the call site (a shell line, a function call in code) define the surface.
2. **Code as disclosure layer.** `--help`, `man`, `jq -h`, `python -c "import x; help(x)"` — execution, not retrieval. The model fetches *exactly* what it asked for.
3. **Composition over enumeration.** Three primitives (`grep`, `jq`, `xargs`) cover what twenty MCP tools each ad-hoc define. Composition keeps the visible surface tiny.
4. **TOON / dense encodings at the wire.** Don't pay tokens to *describe* the surface you're not using. See [TOON analysis](ramblings/2026-05-17--toon-token-oriented-object-notation.md).
5. **AXI principles.** Minimal default schemas, definitive empty states, contextual next-step hints — all reduce entropy per invocation. See [AXI analysis](ramblings/2026-05-17--axi-agent-experience-initiative.md).

## What This Steel-Mans

* **MCP defenders.** A well-designed, domain-scoped MCP server *can* be low-entropy (e.g. SMARTHAUS's claim of 139 ops in ~3,900 tokens via dispatch). The repo's critique is about *naive large* MCP — the dominant deployment pattern — not MCP-as-such.
* **Zechner's "CLI vs MCP makes no difference" benchmark.** True in a controlled small-tool-surface setup. The framing predicts exactly this: at low entropy, the architecture doesn't matter. The divergence appears as entropy grows.

## What This Predicts

* Large unscoped MCP servers will keep underperforming, regardless of model upgrades.
* MCP servers that adopt code-execution + domain-scoped dispatch will close most of the gap to CLI.
* The winning architecture across all camps is whichever one makes **low entropy the default**, not whichever one is labeled "MCP" or "CLI".

## Related Reading in This Repo

* [Core Thesis](THESIS.md)
* [CLI/SDK Over Context Bloat](cli-sdk-over-context-bloat.md)
* [MCP Alternatives](mcp-alternatives.md)
* [MCP Critique Sources](mcp-critique-sources.md) — see "Tool-Surface Entropy" section
* Carsten Lindstedt comment archive: [`archived-resources/carsten-lindstedt-linkedin--tool-surface-entropy.md`](archived-resources/carsten-lindstedt-linkedin--tool-surface-entropy.md)
* Parent thread (Mitko Vasilev): [`archived-resources/mitkox-linkedin--deleted-all-mcps-skills-cli.md`](archived-resources/mitkox-linkedin--deleted-all-mcps-skills-cli.md)
