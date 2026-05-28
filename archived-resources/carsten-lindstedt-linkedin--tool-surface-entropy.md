# Carsten Lindstedt — Tool-Surface Entropy Framing

**Source:** [LinkedIn comment](https://www.linkedin.com/feed/update/urn:li:activity:7437591826464677888/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287437614753553821698%2Curn%3Ali%3Aactivity%3A7437591826464677888%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287444686006341128192%2Curn%3Ali%3Aactivity%3A7437591826464677888%29) (reply to Bora Celik in Mitko Vasilev's "deleted all my MCPs" thread)
**Author:** Carsten Lindstedt — Industrial AI · Industry World Models · Virtual Twins · Agentic Systems · Physical AI
**Reply URN:** `urn:li:fsd_comment:(7444686006341128192,urn:li:activity:7437591826464677888)`
**Parent post:** Mitko Vasilev — [archived](./mitkox-linkedin--deleted-all-mcps-skills-cli.md)
**Archived:** 2026-05-28

---

## Comment Content (verbatim)

> Bora Celik Zechner's result holds in a controlled setup with a small tool surface, but it explicitly shows what breaks in practice: large MCP servers inject dozens of tools and poison the context window.
> That's why people see different outcomes: CLI keeps the action space implicitly bounded, while naive MCP expands it and increases selection entropy.
> Progressive disclosure helps, but just shifts the problem to tool discovery and retrieval, which is still unreliable at scale.
>
> So this isn't MCP vs CLI; the real variable is whether you control tool surface entropy or let it explode.

## Bora Celik's preceding comment (verbatim, for context)

> sorry but nope. if your only use case is running an agent on your local machine in terminal (less than 1% of the world's agent use cases), then maybe. but even then nope. this article explains how CLI vs MCP makes no difference. https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/ That Github MCP example is also getting tired now.

---

## Why This Matters for the Repo

Carsten reframes the entire MCP-vs-CLI debate around a **single underlying variable** the repo had not yet named: **tool-surface entropy** (the size and unpredictability of the action space the model has to select from).

Implications captured in [`tool-surface-entropy.md`](../tool-surface-entropy.md):

* **MCP isn't intrinsically bad** — *naive large* MCP is. Anything that injects many tool definitions inflates entropy.
* **CLI wins implicitly**, not by design: each shell invocation scopes the action space to a single command surface.
* **Progressive disclosure isn't a solution** — it shifts entropy from selection to retrieval, which is itself unreliable at scale.
* **Zechner's controlled benchmark is consistent with this** — it explicitly does *not* test the high-entropy regime where the divergence appears.

This framing **steel-mans MCP defenders** while preserving the repo's thesis, and gives the repo a unifying vocabulary for the entire critique.

## Repo Cross-References

* Concept page: [`tool-surface-entropy.md`](../tool-surface-entropy.md)
* Critique sources index: [`mcp-critique-sources.md`](../mcp-critique-sources.md) (new "Tool-Surface Entropy" section)
* Parent thread archive: [`mitkox-linkedin--deleted-all-mcps-skills-cli.md`](./mitkox-linkedin--deleted-all-mcps-skills-cli.md)
* Reply drafted: [`ramblings/2026-05-28--reply-to-carsten-on-tool-surface-entropy.md`](../ramblings/2026-05-28--reply-to-carsten-on-tool-surface-entropy.md)
