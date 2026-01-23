# We've Been Using MCP Wrong: How Anthropic Reduced AI Agent Costs by 98.7%

**Author:** Pawel (@meshuggah22)

**Publication Date:** November 6, 2025

**Archive Date:** 2026-01-23T00:28:58Z

**Original URL:** <https://medium.com/@meshuggah22/weve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589>

**Status:** Member-only story (paywalled) - partial content available

**Reading Time:** 5 min read

**Engagement:** 325 claps, 8 responses

---

## Key Quotes (from available preview)

> **"Anthropic's recent paper explores the biggest issue with the MCP - their AI agents were processing 150,000 tokens just to load tool definitions before even reading a user's request. The same functionality could use 2,000 tokens — a 98.7% reduction."**

> **"This is a critical, as AI agents scale from proof-of-concept to production, connecting them to dozens of MCP (Model Context Protocol) servers with hundreds of tools has become standard practice. But there's a problem hiding in plain sight: every tool definition loads into the context window upfront, and every intermediate result flows through the model."**

> **"The engineering teams at Anthropic and Cloudflare independently discovered the same solution: stop making models call tools directly. Instead, have them write code."**

---

## Summary

This article discusses a fundamental inefficiency in how Model Context Protocol (MCP) has been traditionally implemented. The key findings:

* **Token Bloat Problem:** Traditional MCP implementations load all tool definitions into the context window upfront, consuming massive amounts of tokens (150,000 tokens in some cases) before the agent even processes the user's request.

* **98.7% Cost Reduction:** The same functionality can be achieved using only 2,000 tokens - representing a 98.7% reduction in token usage.

* **The Solution:** Both Anthropic and Cloudflare independently arrived at the same solution: instead of having models call tools directly, have them write code to interact with tools.

* **Scale Challenge:** As AI agents move from proof-of-concept to production, connecting to dozens of MCP servers with hundreds of tools has become common, making this inefficiency a critical bottleneck.

* **Core Issue:** Every tool definition loads upfront, and every intermediate result flows through the model, creating unnecessary context window bloat.

---

## Available Content (Preview)

### The Traditional MCP Trap

Model Context Protocol has revolutionized how AI agents connect to external systems. Since its launch in November 2024, the community has built thousands of MCP servers, enabling agents to access everything from databases to cloud services.

But the standard implementation has a fundamental inefficiency problem.

Here's what happens when you ask an agent to "analyze this document, extract keywords, generate a summary, and save the results":

**Step 1: Load all tool definitions**

```json
{
  "read_file": {
    "description"…
```

[Content truncated due to paywall]

---

## Context and Significance

This article is part of a broader discussion about MCP optimization and cost reduction in AI agent systems. The author, Pawel, is identified as a "Gen AI director with a focus on AI & Data Strategy, FinOps, MLOps & LLM/LMMOps" with 301 followers on Medium.

The article was published on November 6, 2025, during a period of rapid development in AI agent frameworks and MCP adoption. It addresses a critical concern for production AI systems: cost efficiency and token usage optimization.

### Related Work by Author

* "Google's A2UI Protocol Just Changed How AI Agents Build User Interfaces" (Dec 28, 2025)
* "FunctionGemma: I Fine-Tuned Google's 270M Edge Model and Tested It on My S23" (Dec 19, 2025)
* "HuggingFace Skills: Fine-Tune Any Open-Source LLM with One Line of English" (Dec 7, 2025)
* "Hands-On with Bloom: Anthropic's Open-Source Framework for Automated AI Behavioral Evaluation" (Dec 22, 2025)

---

## Community Responses (Selected)

**Scot Campbell** (Nov 12, 2025):
> Wow...just did a quick and dirty test in python on a paper of mine (currently at maximal draft size, I have GOT to start editing), here's the analysis:
>
> Token Count Analysis
>
> Precise count for paper.md: 53,132 tokens
>
> Breakdown:
> - Characters: 245,147
> [7 claps, 1 reply]

**Megha Gupta** (Nov 16, 2025):
> Great article, want to understand how can I test from my side? Do I need to enable something from my side. I am using both cursor and Claude.
> [6 claps]

**Susan Apfel** (Nov 8, 2025):
> Hello I am a little confused, we still need to tell llm what kind of api functions it can use in the beginning, right? Kind of like telling llm all the tools information? If I understand correctly, we just ask llm to generate a work plan, then we…[more]
> [3 claps]

---

## Archive Notes

**Limitation:** This article is behind Medium's paywall. Only the introduction and preview content were accessible at the time of archival. The full methodology, technical details, code examples, and complete analysis are not included in this archive.

**Recommendation:** To access the complete article content:

* Subscribe to Medium membership
* Contact the author directly for access
* Check if the content has been republished on open platforms
* Look for related Anthropic papers or documentation that may contain the same information

**Related Resources to Explore:**

* Anthropic's official documentation on MCP optimization
* Cloudflare's engineering blog posts on similar optimizations
* Community discussions on MCP token efficiency
* Alternative articles discussing code-generation approaches vs. direct tool calling

---

## Metadata

* **Platform:** Medium
* **Article Type:** Technical analysis / Case study
* **Content Category:** AI/ML Engineering, LLMOps, Cost Optimization
* **Visibility:** Member-only (paywalled)
* **Archive Method:** jina.ai reader API
* **Archive Quality:** Partial (preview only)
* **Full Content Available:** No
* **Images Referenced:** 29 images (not archived due to paywall)
* **External Links:** Multiple (to other Medium articles and author's work)
