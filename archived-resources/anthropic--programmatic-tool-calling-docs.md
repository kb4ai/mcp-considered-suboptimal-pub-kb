---
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling
title: "Programmatic tool calling - Claude API Docs"
author: "Anthropic Developer Platform team"
archive_date: "2026-02-20"
archived_by: "Claude Code (Sonnet 4.6)"
---

# Programmatic tool calling

Programmatic tool calling allows Claude to write code that calls your tools programmatically within a code execution container, rather than requiring round trips through the model for each tool invocation. This reduces latency for multi-tool workflows and decreases token consumption by allowing Claude to filter or process data before it reaches the model's context window.

> Note: This feature requires the code execution tool to be enabled.

> Note: This feature is **not** covered by Zero Data Retention (ZDR) arrangements. Data is retained according to the feature's standard retention policy.

---

## Model compatibility

Programmatic tool calling is available on the following models:

| Model | Tool Version |
|-------|--------------|
| Claude Opus 4.6 (`claude-opus-4-6`) | `code_execution_20250825` |
| Claude Sonnet 4.6 (`claude-sonnet-4-6`) | `code_execution_20250825` |
| Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) | `code_execution_20250825` |
| Claude Opus 4.5 (`claude-opus-4-5-20251101`) | `code_execution_20250825` |

> Warning: Programmatic tool calling is available via the Claude API and Microsoft Foundry.

---

## Quick start

Here's a simple example where Claude programmatically queries a database multiple times and aggregates results:

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Query sales data for the West, East, and Central regions, then tell me which region had the highest revenue",
        }
    ],
    tools=[
        {"type": "code_execution_20250825", "name": "code_execution"},
        {
            "name": "query_database",
            "description": "Execute a SQL query against the sales database. Returns a list of rows as JSON objects.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "sql": {"type": "string", "description": "SQL query to execute"}
                },
                "required": ["sql"],
            },
            "allowed_callers": ["code_execution_20250825"],
        },
    ],
)
```

---

## How programmatic tool calling works

When you configure a tool to be callable from code execution and Claude decides to use that tool:

1. Claude writes Python code that invokes the tool as a function, potentially including multiple tool calls and pre/post-processing logic
2. Claude runs this code in a sandboxed container via code execution
3. When a tool function is called, code execution pauses and the API returns a `tool_use` block
4. You provide the tool result, and code execution continues (intermediate results are not loaded into Claude's context window)
5. Once all code execution completes, Claude receives the final output and continues working on the task

This approach is particularly useful for:

* **Large data processing**: Filter or aggregate tool results before they reach Claude's context
* **Multi-step workflows**: Save tokens and latency by calling tools serially or in a loop without sampling Claude in-between tool calls
* **Conditional logic**: Make decisions based on intermediate tool results

> Note: Custom tools are converted to async Python functions to support parallel tool calling. When Claude writes code that calls your tools, it uses `await` (e.g., `result = await query_database("<sql>")`) and automatically includes the appropriate async wrapper function.

---

## Core concepts

### The `allowed_callers` field

The `allowed_callers` field specifies which contexts can invoke a tool:

```json
{
  "name": "query_database",
  "description": "Execute a SQL query against the database",
  "input_schema": {},
  "allowed_callers": ["code_execution_20250825"]
}
```

**Possible values:**

* `["direct"]` - Only Claude can call this tool directly (default if omitted)
* `["code_execution_20250825"]` - Only callable from within code execution
* `["direct", "code_execution_20250825"]` - Callable both directly and from code execution

> Tip: Choose either `["direct"]` or `["code_execution_20250825"]` for each tool rather than enabling both, as this provides clearer guidance to Claude for how best to use the tool.

### The `caller` field in responses

Every tool use block includes a `caller` field indicating how it was invoked:

**Direct invocation (traditional tool use):**

```json
{
  "type": "tool_use",
  "id": "toolu_abc123",
  "name": "query_database",
  "input": {"sql": "<sql>"},
  "caller": {"type": "direct"}
}
```

**Programmatic invocation:**

```json
{
  "type": "tool_use",
  "id": "toolu_xyz789",
  "name": "query_database",
  "input": {"sql": "<sql>"},
  "caller": {
    "type": "code_execution_20250825",
    "tool_id": "srvtoolu_abc123"
  }
}
```

The `tool_id` references the code execution tool that made the programmatic call.

### Container lifecycle

Programmatic tool calling uses the same containers as code execution:

* **Container creation**: A new container is created for each session unless you reuse an existing one
* **Expiration**: Containers expire after approximately 4.5 minutes of inactivity (subject to change)
* **Container ID**: Returned in responses via the `container` field
* **Reuse**: Pass the container ID to maintain state across requests

> Warning: When a tool is called programmatically and the container is waiting for your tool result, you must respond before the container expires. Monitor the `expires_at` field. If the container expires, Claude may treat the tool call as timed out and retry it.

---

## Advanced patterns

### Batch processing with loops

Claude can write code that processes multiple items efficiently:

```python
# async wrapper omitted for clarity
regions = ["West", "East", "Central", "North", "South"]
results = {}
for region in regions:
    data = await query_database(f"<sql for {region}>")
    results[region] = sum(row["revenue"] for row in data)

# Process results programmatically
top_region = max(results.items(), key=lambda x: x[1])
print(f"Top region: {top_region[0]} with ${top_region[1]:,} in revenue")
```

This pattern:

* Reduces model round-trips from N (one per region) to 1
* Processes large result sets programmatically before returning to Claude
* Saves tokens by only returning aggregated conclusions instead of raw data

### Early termination

Claude can stop processing as soon as success criteria are met:

```python
# async wrapper omitted for clarity
endpoints = ["us-east", "eu-west", "apac"]
for endpoint in endpoints:
    status = await check_health(endpoint)
    if status == "healthy":
        print(f"Found healthy endpoint: {endpoint}")
        break  # Stop early, don't check remaining
```

### Conditional tool selection

```python
# async wrapper omitted for clarity
file_info = await get_file_info(path)
if file_info["size"] < 10000:
    content = await read_full_file(path)
else:
    content = await read_file_summary(path)
print(content)
```

### Data filtering

```python
# async wrapper omitted for clarity
logs = await fetch_logs(server_id)
errors = [log for log in logs if "ERROR" in log]
print(f"Found {len(errors)} errors")
for error in errors[-10:]:  # Only return last 10 errors
    print(error)
```

---

## Constraints and limitations

### Feature incompatibilities

* **Structured outputs**: Tools with `strict: true` are not supported with programmatic calling
* **Tool choice**: You cannot force programmatic calling of a specific tool via `tool_choice`
* **Parallel tool use**: `disable_parallel_tool_use: true` is not supported with programmatic calling

### Tool restrictions

The following tools cannot currently be called programmatically, but support may be added in future releases:

* Web search
* Web fetch
* Tools provided by an MCP connector

### Message formatting restrictions

When responding to programmatic tool calls, there are strict formatting requirements:

If there are pending programmatic tool calls waiting for results, your response message must contain **only** `tool_result` blocks. You cannot include any text content, even after the tool results.

```json
// INVALID - Cannot include text when responding to programmatic tool calls
{
  "role": "user",
  "content": [
    {"type": "tool_result", "tool_use_id": "toolu_01", "content": "..."},
    {"type": "text", "text": "What should I do next?"}
  ]
}

// VALID - Only tool results when responding to programmatic tool calls
{
  "role": "user",
  "content": [
    {"type": "tool_result", "tool_use_id": "toolu_01", "content": "..."}
  ]
}
```

---

## Token efficiency

Programmatic tool calling can significantly reduce token consumption:

* **Tool results from programmatic calls are not added to Claude's context** - only the final code output is
* **Intermediate processing happens in code** - filtering, aggregation, etc. don't consume model tokens
* **Multiple tool calls in one code execution** - reduces overhead compared to separate model turns

For example, calling 10 tools directly uses ~10x the tokens of calling them programmatically and returning a summary.

> Note: Tool results from programmatic invocations do not count toward your input/output token usage. Only the final code execution result and Claude's response count.

---

## Why programmatic tool calling works

Claude's training includes extensive exposure to code, making it effective at reasoning through and chaining function calls. When tools are presented as callable functions within a code execution environment, Claude can leverage this strength to:

* **Reason naturally about tool composition**: Chain operations and handle dependencies as naturally as writing any Python code
* **Process large results efficiently**: Filter down large tool outputs, extract only relevant data, or write intermediate results to files before returning summaries to the context window
* **Reduce latency significantly**: Eliminate the overhead of re-sampling Claude between each tool call in multi-step workflows

This approach enables workflows that would be impractical with traditional tool use (such as processing files over 1M tokens) by allowing Claude to work with data programmatically rather than loading everything into the conversation context.

---

## Alternative implementations

Programmatic tool calling is a generalizable pattern that can be implemented outside of Anthropic's managed code execution.

### Client-side direct execution

Provide Claude with a code execution tool and describe what functions are available in that environment. When Claude invokes the tool with code, your application executes it locally where those functions are defined.

**Advantages:** Simple to implement with minimal re-architecting; full control over environment.
**Disadvantages:** Executes untrusted code outside of a sandbox; tool invocations can be vectors for code injection.

### Self-managed sandboxed execution

Same approach from Claude's perspective, but code runs in a sandboxed container with security restrictions.

**Advantages:** Safe programmatic tool calling on your own infrastructure; full control over execution environment.
**Disadvantages:** Complex to build and maintain; requires managing both infrastructure and inter-process communication.

### Anthropic-managed execution

Anthropic's programmatic tool calling is a managed version of sandboxed execution with an opinionated Python environment tuned for Claude. Anthropic handles container management, code execution, and secure tool invocation communication.

**Advantages:** Safe and secure by default; easy to enable with minimal configuration; environment and instructions optimized for Claude.

Consider using Anthropic's managed solution if you are using the Claude API.
