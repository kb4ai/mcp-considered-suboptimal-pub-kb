# Time-Traveling RPC for LLM Executors

**The Cap'n Proto insight applied to AI agents:** Keep slow actors (LLM token processing) out of fast decision loops (API chaining, filtering, aggregation).

---

## The Cap'n Proto Principle

[Cap'n Proto's time-traveling RPC](https://capnproto.org/rpc.html) achieves low latency by eliminating round trips. Instead of:

```
Client → Server → Client → Server → Client
```

It batches operations so dependent calls execute without returning to the caller:

```
Client → Server (chains internally) → Client
```

**The same principle applies to LLM tool execution.**

---

## The Problem: LLM as Bottleneck

When an LLM makes sequential MCP tool calls, each round trip requires:

1. **Tool result → LLM context** (tokens in)
2. **LLM processing** (inference latency)
3. **LLM decision → next tool call** (tokens out)

This creates a fundamental latency bottleneck: **the LLM sits in every decision loop**, even for deterministic operations that don't require intelligence.

---

## Visual Comparison

### Approach A: Direct MCP Calls (LLM in the Loop)

```mermaid
sequenceDiagram
    participant User
    participant LLM
    participant API1 as Slack API
    participant API2 as Linear API
    participant API3 as GitHub API

    User->>LLM: "Find urgent bugs mentioned in #engineering"

    Note over LLM: Process request (~2s)
    LLM->>API1: MCP: slack.search("urgent bug")
    API1-->>LLM: 50 messages (3,000 tokens)

    Note over LLM: Process results (~5s)
    LLM->>API2: MCP: linear.search(extracted_keywords)
    API2-->>LLM: 30 issues (4,000 tokens)

    Note over LLM: Process results (~5s)
    LLM->>API3: MCP: github.search(issue_refs)
    API3-->>LLM: 20 PRs (2,500 tokens)

    Note over LLM: Process results (~5s)
    LLM->>API1: MCP: slack.post(summary)
    API1-->>LLM: Confirmation (100 tokens)

    Note over LLM: Final processing (~3s)
    LLM-->>User: "Posted summary to #engineering"
```

**Totals:**
- **Round trips:** 4 (each through LLM)
- **Tokens processed:** ~11,000
- **LLM processing time:** ~20 seconds
- **Total latency:** 30-80 seconds (depending on model/load)

### Approach B: Executor Delegation (LLM out of the Loop)

```mermaid
sequenceDiagram
    participant User
    participant LLM
    participant Executor as Code Executor
    participant API1 as Slack API
    participant API2 as Linear API
    participant API3 as GitHub API

    User->>LLM: "Find urgent bugs mentioned in #engineering"

    Note over LLM: Generate execution plan (~2s)
    LLM->>Executor: Execute script

    Note over Executor: Runs without LLM intervention
    Executor->>API1: slack search "urgent bug"
    API1-->>Executor: 50 messages

    Note over Executor: Filter locally with jq/grep
    Executor->>API2: linear search --filter keywords
    API2-->>Executor: 30 issues

    Note over Executor: Filter & correlate locally
    Executor->>API3: gh search --refs extracted
    API3-->>Executor: 20 PRs

    Note over Executor: Format summary locally
    Executor->>API1: slack post --channel engineering
    API1-->>Executor: Confirmation

    Executor-->>LLM: "Done: 15 urgent bugs found, summary posted"

    Note over LLM: Minimal processing (~1s)
    LLM-->>User: "Found 15 urgent bugs, posted summary"
```

**Totals:**
- **LLM round trips:** 1
- **Tokens processed:** ~300 (plan + confirmation)
- **LLM processing time:** ~3 seconds
- **Total latency:** 5-15 seconds

---

## The Math

| Metric | MCP (LLM in loop) | Executor (LLM out of loop) | Improvement |
|--------|-------------------|---------------------------|-------------|
| LLM round trips | 4 | 1 | **75% fewer** |
| Tokens processed | 11,000 | 300 | **97% reduction** |
| LLM inference time | ~20s | ~3s | **85% faster** |
| Total latency | 30-80s | 5-15s | **75-80% faster** |
| API cost (at $3/1M tokens) | $0.033 | $0.0009 | **97% cheaper** |

---

## Why This Matters for Agents

### Latency Compounds in Agentic Loops

In autonomous workflows, agents often iterate:

```
Plan → Execute → Evaluate → Adjust → Execute → ...
```

If each "Execute" step involves 4 LLM round trips instead of 1, a 10-step workflow becomes:

- **MCP approach:** 40 LLM round trips, 110,000 tokens
- **Executor approach:** 10 LLM round trips, 3,000 tokens

**The gap widens with complexity.**

### Quality Degrades with Context Size

As documented in [THESIS.md](THESIS.md), more tokens in context means:

- Diluted attention across irrelevant data
- "Lost in the middle" phenomenon
- Higher hallucination rates
- Slower inference

By keeping intermediate results out of LLM context, executors preserve model quality for decisions that actually require intelligence.

---

## Implementation Pattern

```python
# MCP approach: LLM sees everything
async def mcp_workflow(llm, query):
    # Round trip 1: Search Slack
    slack_results = await llm.call_tool("slack.search", query)  # 3,000 tokens

    # Round trip 2: Search Linear (LLM extracts keywords)
    keywords = await llm.extract_keywords(slack_results)  # LLM processing
    linear_results = await llm.call_tool("linear.search", keywords)  # 4,000 tokens

    # Round trip 3: Search GitHub (LLM extracts refs)
    refs = await llm.extract_refs(linear_results)  # LLM processing
    github_results = await llm.call_tool("github.search", refs)  # 2,500 tokens

    # Round trip 4: Post summary (LLM generates)
    summary = await llm.generate_summary(slack_results, linear_results, github_results)
    await llm.call_tool("slack.post", summary)  # 100 tokens


# Executor approach: LLM plans, executor runs
async def executor_workflow(llm, query):
    # Single LLM round trip: generate execution plan
    plan = await llm.generate_plan(query)  # ~200 tokens

    # Executor runs without LLM intervention
    result = await executor.run("""
        slack search "urgent bug" --json | jq '.[] | .text' > /tmp/slack.txt
        grep -oE '[A-Z]+-[0-9]+' /tmp/slack.txt | sort -u > /tmp/refs.txt

        linear search --refs $(cat /tmp/refs.txt) --json | \
            jq '.[] | {id, title, priority}' > /tmp/issues.json

        gh search prs --json --refs $(cat /tmp/refs.txt) > /tmp/prs.json

        # Format summary locally (no LLM needed for formatting)
        jq -s '{issues: .[0], prs: .[1]}' /tmp/issues.json /tmp/prs.json | \
            slack post --channel engineering --format summary
    """)

    # Single confirmation back to LLM
    return f"Done: {result.summary}"  # ~100 tokens
```

---

## The Principle

> **Keep slow actors out of fast loops.**

| Actor | Speed | Role |
|-------|-------|------|
| LLM inference | Slow (~1-5s per call) | High-level planning, ambiguity resolution |
| Code execution | Fast (~10-100ms) | Data transformation, filtering, API chaining |
| API calls | Medium (~100-500ms) | External data retrieval |

**MCP puts the slow actor (LLM) in every loop. Executors keep it where it belongs: making intelligent decisions, not shuffling data.**

---

## Related Concepts

- **Cap'n Proto Time-Traveling RPC** — The original insight about minimizing round trips
- **Continuation-Passing Style** — Passing "what to do next" rather than returning intermediate results
- **Dataflow Programming** — Operations chain without central coordination
- **Unix Pipes** — Data flows through transformations without returning to shell

---

## Further Reading

- [THESIS.md](THESIS.md) — Core argument for CLI/SDK over MCP
- [cli-sdk-over-context-bloat.md](cli-sdk-over-context-bloat.md) — Detailed patterns for executor-style workflows
- [FAQ.md](FAQ.md) — Agent self-optimization patterns
- [Cap'n Proto RPC](https://capnproto.org/rpc.html) — Original time-traveling RPC documentation

---

*Part of [MCP Considered Suboptimal](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb)*
