# Your MCP Doesn't Need 30 Tools: It Needs Code

**Author:** Armin Ronacher
**Published:** August 18, 2025
**Source URL:** https://lucumr.pocoo.org/2025/8/18/code-mcps/
**Archived:** 2026-01-23

---

## Overview

Armin Ronacher proposes that Model Context Protocol (MCP) servers are more effective when they expose a single tool accepting programming code rather than multiple specialized tools. This approach leverages what AI models already understand well: programming languages.

## Key Problems with CLI-Based Tools

The article identifies several critical challenges:

1. **Platform & Version Dependencies**: Tools often fail on first use due to platform-specific behavior and undocumented quirks
2. **Encoding Issues**: Models struggle with non-ASCII inputs, newlines, and control characters via shell arguments
3. **Security Preflight Delays**: Claude Code runs additional security checks through the Haiku model before execution, slowing multi-turn interactions
4. **State Management**: Agents lose track of stateful sessions (like tmux) when details diverge from expectations

## The "Ubertool" Solution

Rather than building 30+ specialized MCP tools, Ronacher advocates for a stateful Python or JavaScript interpreter as a single MCP tool. Key implementations:

* **pexpect-mcp**: A Python interpreter with pexpect library for interactive CLI debugging (demonstrated with LLDB)
* **playwrightess-mcp**: JavaScript interface to Playwright API, reducing ~30 tool definitions to 1

## Advantages of Code-Based MCPs

### Composability without inference

Code naturally chains operations that would require separate tool calls in traditional MCP design.

### Session persistence

The MCP maintains state across multiple invocations, enabling complex multi-step debugging workflows.

### Reusability

Generated code can be saved as standalone scripts and executed later, reducing re-run time from 45 seconds to under 5 seconds.

### Discovery mechanisms

Models can leverage built-in functions like `dir()`, `globals()`, and introspection to explore available functionality.

## Demonstrated Workflow Example

Using pexpect-mcp to debug a C program:

* Initial debugging session: ~7 tool calls over 45 seconds identifying segfault root cause
* Generated standalone Python script: One tool call under 5 seconds for re-execution
* Script output was immediately actionable without MCP involvement

The agent successfully identified both the NULL pointer dereference and an off-by-one loop error.

## Key Quotes

> "The command line really isn't just one tool — it's a series of tools that can be composed through a programming language: bash."

> "45s/7 calls initial → 5s/1 call scripted"

> "Token cost: Well-designed MCPs still consume ~8k tokens"

## Security Considerations

Ronacher acknowledges that exposing eval() appears less secure but argues this concern is somewhat overstated:

* Code execution through traditional tools (like pexpect spawning bash commands) poses equivalent risks
* AI agents already write and execute code in testing frameworks
* The fundamental challenge of securing AI agents transcends the choice between tool calls and eval()

## Design Recommendations

1. **Embrace programming languages** as the primary interface when building MCPs for complex tasks
2. **Minimize tool definitions** by consolidating into language-based execution models
3. **Preserve state** to enable agents to maintain context across operations without re-inference
4. **Expose discovery mechanisms** so agents can learn about available functionality independently
5. **Support output forwarding** (like console.log) to return data automatically rather than requiring explicit requests

---

**Archive Notes:**

This article provides a compelling case for code execution over tool proliferation. The 45s→5s performance improvement demonstrates the evolutionary advantage: agents can optimize their own workflows when given code execution capability, but cannot modify static MCP tool definitions.
