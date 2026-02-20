---
source_url: https://www.anthropic.com/engineering/advanced-tool-use
title: "Introducing Advanced Tool Use on the Claude Developer Platform"
author: "Bin Wu"
contributors: "Adam Jones, Artur Renault, Henry Tay, Jake Noble, Nathan McCandlish, Noah Picard, Sam Jiang, Claude Developer Platform team"
publication_date: "2025-11-24"
archive_date: "2026-02-20"
archived_by: "Claude Code (Sonnet 4.6)"
---

# Introducing Advanced Tool Use on the Claude Developer Platform

**Published:** November 24, 2025
**Author:** Bin Wu
**Contributors:** Adam Jones, Artur Renault, Henry Tay, Jake Noble, Nathan McCandlish, Noah Picard, Sam Jiang, and the Claude Developer Platform team

## Overview

Anthropic has released three beta features enabling Claude to discover, learn, and execute tools dynamically: Tool Search Tool, Programmatic Tool Calling, and Tool Use Examples.

## The Three Features

**Tool Search Tool** allows Claude to access thousands of tools without consuming context by discovering them on-demand rather than loading all definitions upfront.

**Programmatic Tool Calling** enables Claude to invoke tools within code execution environments, reducing context pollution from intermediate results and eliminating multiple inference passes.

**Tool Use Examples** provides concrete usage patterns beyond JSON schemas, showing "format conventions, nested structure patterns, and optional parameter correlations."

---

## Tool Search Tool Details

### The Problem

Tool definitions consume enormous token budgets. A five-server setup (GitHub, Slack, Sentry, Grafana, Splunk) requires approximately 55K tokens before conversation begins. Anthropic observed 134K token consumption in internal systems.

### The Solution

Instead of loading all tools upfront (~72K tokens for 50+ tools), the Tool Search Tool loads only what's needed (~500 tokens initially). Tools marked with `defer_loading: true` become discoverable on-demand. Internal testing showed accuracy improvements: Opus 4 improved from 49% to 74%; Opus 4.5 from 79.5% to 88.1%.

### When to Use

* Tool definitions consuming >10K tokens
* Experiencing tool selection accuracy issues
* Building MCP-powered systems with multiple servers
* 10+ tools available

Less beneficial for small libraries (<10 tools) or compact definitions.

---

## Programmatic Tool Calling Details

### The Challenge

Traditional tool calling creates two problems: context pollution from intermediate results (2,000+ expense line items consuming 50KB) and inference overhead (each tool call requires full model inference).

### The Solution

Claude writes Python code orchestrating multiple tools. The code runs in a sandboxed environment, processing tool results without adding them to Claude's context. Only final output reaches the model.

**Example efficiency gains:**

* Token savings: 37% reduction (from 43,588 to 27,297 tokens)
* Reduced latency: Eliminates 19+ inference passes for 20+ tool calls
* Improved accuracy: Internal knowledge retrieval improved 25.6% to 28.5%; GIA benchmarks 46.5% to 51.2%

### Implementation Steps

1. Mark tools with `allowed_callers: ["code_execution_20250825"]`
2. Claude generates Python code using tool functions
3. Tool requests include a `caller` field indicating code execution context
4. Only final code output enters Claude's context

### When to Use

* Processing large datasets needing only aggregates
* Multi-step workflows with three+ dependent calls
* Filtering or transforming results before Claude sees them
* Parallel operations (checking multiple endpoints)

Less beneficial for simple single-tool invocations or tasks requiring Claude to see all intermediate results.

---

## Tool Use Examples Details

### The Challenge

JSON schemas define structural validity but cannot express usage patterns, optional parameter inclusion, API conventions, or parameter correlations. This leads to malformed calls.

### The Solution

Provide 1-5 realistic examples showing minimal, partial, and full specification patterns. Examples demonstrate "date formats use YYYY-MM-DD, user IDs follow USR-XXXXX, labels use kebab-case."

Internal testing improved accuracy from 72% to 90% on complex parameter handling.

### When to Use

* Complex nested structures where valid JSON doesn't guarantee correct usage
* Tools with many optional parameters where inclusion patterns matter
* Domain-specific API conventions not captured in schemas
* Similar tools needing disambiguation

Less beneficial for simple single-parameter tools or standard formats Claude already understands.

---

## Best Practices

### Layer Features Strategically

Address specific bottlenecks:

* Context bloat -> Tool Search Tool
* Large intermediate results -> Programmatic Tool Calling
* Parameter errors -> Tool Use Examples

### Tool Search Tool Setup

Clear, descriptive tool names and descriptions improve discovery accuracy. Keep three to five most-used tools always loaded; defer others.

### Programmatic Tool Calling Setup

Document return formats clearly so Claude writes correct parsing logic. Include tools that run in parallel and support retry operations.

### Tool Use Examples Setup

Use realistic data. Show variety with different specification levels. Focus on ambiguities where correct usage isn't obvious from schema alone.

---

## Getting Started

Enable features with the beta header:

```python
client.beta.messages.create(
    betas=["advanced-tool-use-2025-11-20"],
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    tools=[
        {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
        {"type": "code_execution_20250825", "name": "code_execution"},
        # Your tools with defer_loading, allowed_callers, and input_examples
    ]
)
```

Documentation available for each feature with examples and cookbooks.
