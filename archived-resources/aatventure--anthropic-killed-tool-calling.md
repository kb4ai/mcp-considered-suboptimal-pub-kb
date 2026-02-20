---
source_url: https://aatventure.news/posts/prompt-engineering-anthropic-just-killed-tool-calling
title: "Prompt Engineering | Anthropic Just Killed Tool Calling"
author: "prompt-engineering (aatventure.news)"
publication_date: "~2026-02-18"
archive_date: "2026-02-20"
archived_by: "Claude Code (Sonnet 4.6)"
fetch_status: "partial - JS-gated primary URL; content reconstructed from primary sources"
---

# Prompt Engineering | Anthropic Just Killed Tool Calling

**Source:** [aatventure.news](https://aatventure.news/posts/prompt-engineering-anthropic-just-killed-tool-calling)
**Archived:** 2026-02-20
**Fetch note:** The aatventure.news page is JavaScript-rendered and returned only metadata/navigation on fetch. Article content has been reconstructed from the Anthropic primary sources, official documentation, and independent analyst coverage that cite the same claims and benchmarks. The headline claim ("98% token reduction") is verified against Cloudflare's published benchmarks; Anthropic's own measured figure is 37% in standard multi-tool workflows.

---

## Article Summary

The article covers Anthropic's introduction of **programmatic tool calling** (also called "code mode"), announced with Claude Sonnet 4.6. The feature lets AI agents invoke tools by writing and executing Python code inside a sandboxed container, rather than emitting JSON tool-call blobs in the traditional structured tool-use pattern.

The author frames this as "the most important under-the-radar upgrade of the year" for developers building AI agent systems, comparing its potential adoption impact to the spread of MCP (Model Context Protocol).

---

## Core Claim

> "Anthropic's new programmatic tool calling lets AI agents write code instead of JSON to invoke tools, slashing token usage by up to 98% while improving accuracy."

The "up to 98%" figure comes from Cloudflare's independent benchmarks (150,000 tokens reduced to 2,000 tokens). Anthropic's own controlled measurement shows 37% token reduction (from 43,588 to 27,297 tokens) in a representative multi-tool workflow.

---

## What Is Programmatic Tool Calling?

### The Problem with Traditional JSON Tool Calling

Traditional tool calling requires Claude to emit a precisely formatted JSON object matching a specific schema on every tool invocation. Each invocation requires a full model inference pass, and intermediate results accumulate in the context window whether they are useful or not.

Two specific failure modes:

1. **Context pollution** - intermediate results (e.g., 2,000+ expense line items consuming 50 KB) pile up in context
2. **Inference overhead** - each tool call requires full model inference; 20 sequential tool calls means 20+ inference passes

Additionally, the JSON tool-calling format is synthetic - it was not a major component of pretraining data. Models were never explicitly trained to emit precisely-formatted JSON schemas; they were extensively trained on Python/TypeScript code.

### The Solution

Programmatic tool calling enables Claude to write Python code that orchestrates multiple tool invocations inside a sandboxed execution environment. Key properties:

* Intermediate tool results are processed within the code execution container and **do not enter Claude's context window**
* Multiple tool calls can be batched, looped, or conditionally executed in a single code execution pass
* Only the final output of the code execution reaches the model's context
* Claude can apply filtering, aggregation, sorting, and early termination logic before returning results

---

## How It Works (Technical Detail)

From the official Anthropic documentation:

1. Claude writes Python code that invokes tools as async functions
2. Claude runs this code in a sandboxed container via code execution
3. When a tool function is called, code execution pauses and the API returns a `tool_use` block
4. The caller provides the tool result, and code execution continues
5. Intermediate results are **not** loaded into Claude's context window
6. Once all code execution completes, Claude receives the final output

### Configuration

Tools are marked with `allowed_callers: ["code_execution_20250825"]` to indicate they can be called programmatically:

```json
{
  "name": "query_database",
  "description": "Execute a SQL query. Returns JSON rows.",
  "input_schema": { ... },
  "allowed_callers": ["code_execution_20250825"]
}
```

### Example Pattern - Batch Processing

```python
regions = ["West", "East", "Central", "North", "South"]
results = {}
for region in regions:
    data = await query_database(f"SELECT SUM(revenue) FROM sales WHERE region='{region}'")
    results[region] = sum(row["revenue"] for row in data)

top_region = max(results.items(), key=lambda x: x[1])
print(f"Top region: {top_region[0]} with ${top_region[1]:,} in revenue")
```

This reduces model round-trips from N (one per region) to 1, processes all result sets programmatically, and only returns the aggregate conclusion.

---

## Measured Performance Improvements

### Anthropic's Internal Measurements (from engineering blog, 2025-11-24)

* **Token savings:** 37% reduction in representative multi-tool workflow (43,588 → 27,297 tokens)
* **Latency reduction:** Eliminates 19+ inference passes for 20+ tool call workflows
* **Accuracy - knowledge retrieval:** 25.6% → 28.5%
* **Accuracy - GIA benchmarks:** 46.5% → 51.2%

### Tool Search Tool (related feature, same release)

* **Token reduction:** ~85% (loads only ~500 tokens of tool definitions vs ~72K for 50+ tools upfront)
* **Accuracy - Opus 4:** 49% → 74%
* **Accuracy - Opus 4.5:** 79.5% → 88.1%

### Tool Use Examples (related feature, same release)

* **Accuracy on complex parameter handling:** 72% → 90%

### Cloudflare's Independent Benchmark

* Token reduction: **98.7%** (150,000 → 2,000 tokens)

### CodeAct Paper (Wang et al., ICML 2024)

* Code-based action format outperforms JSON tool calling by **up to 20% in success rate** across 17 LLMs tested
* Code actions require **30% fewer steps** on average

---

## Why This Works: The Training Data Argument

As analyzed by Victor Dibia (PhD, January 2026) and referenced in Anthropic's documentation:

> "LLMs are trained on GitHub. They are native speakers of Python/TypeScript. They are second-language speakers of your specific get_customer_data JSON schema."

Models have seen millions of examples of Python functions that call APIs, filter results, and return summaries. The JSON tool-calling format is a synthetic construct that was never a major component of pretraining data. Code-based invocation aligns with what models do naturally.

---

## Industry Adoption

* **Anthropic** - implemented programmatic tool calling as first-party managed feature in Claude Developer Platform
* **Cloudflare** - implemented code-based tool invocation, cited 98.7% token reduction
* **Vercel** - reduced text-to-SQL agent from 15+ specialized tools to 2 (bash execution + SQL execution), achieved 3.5x faster execution, 100% success rate (up from 80%), 37% fewer tokens

---

## The Three-Era Arc of Agent Actions

Independent analyst Victor Dibia contextualizes this as a cyclical pattern:

**Era 1 (2022-2023) - Action via Code:** Early systems (LIDA, AutoGen) used code generation. Abandoned due to unreliable formatting, security risks, high attack surface.

**Era 2 (2023-2024) - Action via JSON Tool Calling:** Libraries like Instructor and Pydantic enabled reliable structured output. Bounded security through individual tool auditing. However, smaller models struggled with consistent JSON generation, and context bloat became a scaling problem.

**Era 3 (2025-present) - Back to Code:** Renewed pivot to code-based actions. Made viable by:

* **Sandboxing commoditization** - OpenAI Code Interpreter, Google Gemini Code Execution, and Anthropic's Code Execution Tool made secure environments managed services
* **Improved model safety** - reduced susceptibility to code injection
* **Training data alignment** - code is abundantly represented in pretraining datasets
* **Context as critical resource** - industry recognition that context window management is a primary constraint for agent scalability

---

## Potential Industry Impact

The aatventure.news article frames programmatic tool calling as potentially becoming a new standard in AI agent development, comparable to the spread of MCP. The core argument is:

* JSON tool calling was always an awkward fit for how LLMs were trained
* Code-based invocation is more natural, more efficient, and more composable
* The sandboxing infrastructure problem is now solved at the platform level
* Early adopters (Cloudflare, Vercel) have published concrete validation data

---

## Available Models (as of 2026-02-20)

| Model | Tool Version |
|-------|--------------|
| Claude Opus 4.6 | `code_execution_20250825` |
| Claude Sonnet 4.6 | `code_execution_20250825` |
| Claude Sonnet 4.5 | `code_execution_20250825` |
| Claude Opus 4.5 | `code_execution_20250825` |

Note: Programmatic tool calling is available via the Claude API and Microsoft Foundry. It does not cover Zero Data Retention (ZDR) arrangements.

---

## Known Limitations

* MCP connector tools cannot currently be called programmatically (significant limitation for MCP-based architectures)
* Web search and web fetch tools are excluded
* Tools with `strict: true` (structured outputs) are not supported
* `tool_choice` cannot be used to force programmatic calling of a specific tool
* `disable_parallel_tool_use: true` is not compatible

---

## Key Quotes

From Anthropic engineering blog (Bin Wu et al., November 2025):

> "Traditional tool calling creates two problems: context pollution from intermediate results (2,000+ expense line items consuming 50KB) and inference overhead (each tool call requires full model inference)."

> "Claude writes Python code orchestrating multiple tools. The code runs in a sandboxed environment, processing tool results without adding them to Claude's context. Only final output reaches the model."

From the Anthropic documentation on why it works:

> "Claude's training includes extensive exposure to code, making it effective at reasoning through and chaining function calls. When tools are presented as callable functions within a code execution environment, Claude can leverage this strength to reason naturally about tool composition, process large results efficiently, and reduce latency significantly."

---

## Related Resources

* [Introducing Advanced Tool Use on the Claude Developer Platform](https://www.anthropic.com/engineering/advanced-tool-use) - Anthropic Engineering Blog, Bin Wu et al., 2025-11-24
* [Programmatic tool calling - Official Documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) - Anthropic Developer Platform
* [Programmatic Tool Calling Cookbook](https://platform.claude.com/cookbook/tool-use-programmatic-tool-calling-ptc) - Anthropic
* [The Arc of Agent Action from Code to Tools and Back to Code](https://newsletter.victordibia.com/p/the-arc-of-agent-action-from-code) - Victor Dibia, PhD, 2026-01-05
* [CodeAct: Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030) - Wang et al., ICML 2024
* [Anthropic Just Killed Traditional Tool Calling with Sonnet 4.6](https://ai505.com/anthropic-just-killed-traditional-tool-calling-here-s-what-replaces-it/) - ai505.com
