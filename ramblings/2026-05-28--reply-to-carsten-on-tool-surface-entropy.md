# Reply to Carsten Lindstedt on tool-surface entropy (2026-05-28)

**Context:** Carsten's LinkedIn comment ([archived](../archived-resources/carsten-lindstedt-linkedin--tool-surface-entropy.md)) in [Mitko Vasilev's "deleted all my MCPs" thread](../archived-resources/mitkox-linkedin--deleted-all-mcps-skills-cli.md) introduced the **tool-surface entropy** framing. This rambling captures the reply text and the repo changes it inspired, for future readers tracing how this concept entered the repo.

---

## What Carsten said (verbatim)

> Zechner's result holds in a controlled setup with a small tool surface, but it explicitly shows what breaks in practice: large MCP servers inject dozens of tools and poison the context window.
> That's why people see different outcomes: CLI keeps the action space implicitly bounded, while naive MCP expands it and increases selection entropy.
> Progressive disclosure helps, but just shifts the problem to tool discovery and retrieval, which is still unreliable at scale.
>
> So this isn't MCP vs CLI; the real variable is whether you control tool surface entropy or let it explode.

## Reply posted

> @Carsten — very well put. It's not MCP vs CLI in the abstract, it's whether you control **tool-surface entropy** or let it explode. That's exactly the right axis.
>
> One mechanism worth naming: **code as the disclosure layer**. Progressive tool-discovery retrieval is unreliable at scale, you're right — but `--help` / `man` / `jq` / `grep` aren't *retrieval*, they're *execution*. The LLM doesn't pick from N injected tool schemas; it runs `tool --help | grep -A3 thing` and reads exactly what it asked for. The action space stays bounded because it's *scoped by the shell call site*, not by what was preloaded into context.
>
> This is also why Anthropic's Code Execution with MCP (Nov 2025) and Sonnet 4.6's programmatic tool calling GA matter: even *inside* the MCP ecosystem, the fix is to stop injecting tool definitions and let the model **write code** that calls them. Entropy control via code, not via better retrieval.
>
> Naive MCP makes entropy control opt-in and architecturally hard; CLI/Skills make it the default. Same axis, different gradient.
>
> Promoted your framing to a concept page in the repo: https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/blob/master/tool-surface-entropy.md — and archived your comment + the changes it inspired in this commit: https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/commit/94cd8eb

(SHA is backfilled by the agent immediately after `git push`. If you are reading this while the placeholder is still present, the commit hadn't propagated yet at archive time.)

## Repo changes inspired by this comment

* New concept page: [`tool-surface-entropy.md`](../tool-surface-entropy.md)
* New archive: [`archived-resources/carsten-lindstedt-linkedin--tool-surface-entropy.{md,url,meta.json}`](../archived-resources/carsten-lindstedt-linkedin--tool-surface-entropy.md)
* New "Tool-Surface Entropy" section in [`mcp-critique-sources.md`](../mcp-critique-sources.md)
* "Industry Voices" line in [README.md](../README.md)
* Cross-link added in Mitko thread archive

## Why it matters going forward

The repo previously argued "CLI > MCP" without naming the underlying variable. Naming it (a) generalizes the critique, (b) steel-mans MCP defenders (small/domain-scoped MCP isn't the problem; naive *large* MCP is), and (c) gives a single yardstick by which to evaluate future protocols/architectures: **does it make low entropy the default, or does it require discipline to achieve?**
