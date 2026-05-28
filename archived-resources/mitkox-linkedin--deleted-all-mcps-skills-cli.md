# Mitko Vasilev — "I just deleted all my MCPs. Skills + CLI is all you need."

**Source:** [LinkedIn post (urn:li:activity:7437591826464677888)](https://www.linkedin.com/feed/update/urn:li:activity:7437591826464677888/)
**Author:** Mitko Vasilev (CTO) — [profile](https://www.linkedin.com/in/mitkox/)
**Published:** ~March 2026 (LinkedIn shows "2mo" as of 2026-05-28)
**Engagement at archive time:** 140 reactions, 450 comments, 175 reposts
**Archived:** 2026-05-28

---

## Post Content

> I just deleted all my MCPs.
>
> Skills + CLI is all you need.

(Short declarative one-liner. The actual LinkedIn post body is a single statement; the rendered page surfaces a long pinned reply from SMARTHAUS as visual context, but the original post is the line above.)

---

## Why This Matters for the Repo

A practitioner-level (CTO) declaration that lines up directly with this repo's thesis: that **Skills + CLI tooling outperforms MCP** for real agent workflows. Notable as a *post-Sonnet-4.6* (Feb 2026) data point — i.e., after Anthropic graduated programmatic tool calling to GA and made Skills first-class, practitioners in the field are already acting on the implication and dropping MCP servers wholesale.

The 450-comment thread is itself a useful artifact, surfacing the standard counter-arguments and rebuttals:

* **Bora Celik (Founder, gentic.co):** disagrees, citing [Mario Zechner's MCP vs CLI benchmark](https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/) — argues CLI-only is a sub-1% use case.
* **Carsten Lindstedt:** nuanced reply — Zechner's controlled benchmark holds, but "large MCP servers inject dozens of tools and poison the context window… the real variable is whether you control tool surface entropy or let it explode." [Dedicated archive](./carsten-lindstedt-linkedin--tool-surface-entropy.md). Framing extracted to repo-level concept page: [`tool-surface-entropy.md`](../tool-surface-entropy.md).
* **SMARTHAUS (pinned reply):** governance counter-argument — claims their MCP fits 139 operations in ~3,900 tokens via domain-scoped dispatch, framing MCP as "a governance engine with mathematical teeth" rather than an API wrapper. Useful steel-manned opposition.
* **Rick Bullotta:** "MCP isn't exactly the best for handling access control — particularly when an agent is acting on behalf of a specific individual."
* **Alex C. (Tech Lead, Epam):** disagrees, argues MCP still useful for "more deterministic usage."
* **Heinrich Krupp:** "MCP servers that do serve in situations where there is no CLI equivalent solution available cannot simply be replaced with skills." (Valid scope caveat.)

---

## Repo Cross-References

* Aligns with: [THESIS.md](../THESIS.md), [cli-sdk-over-context-bloat.md](../cli-sdk-over-context-bloat.md), [mcp-alternatives.md](../mcp-alternatives.md)
* Counter-argument context: [Mario Zechner benchmark discussion](../mcp-critique-sources.md)
* Anthropic shift that primed this: [Sonnet 4.6 / PTC GA](./anthropic--sonnet-4-6-announcement.md), [Code Execution with MCP](./anthropic--code-execution-with-mcp.md)
* Related practitioner voices: [Theo t3.gg](./theo-t3gg--anthropic-admits-mcp-sucks--transcript.md), [Carlo Zottmann (Linearis)](./zottmann--linearis-linear-cli-built.md)

