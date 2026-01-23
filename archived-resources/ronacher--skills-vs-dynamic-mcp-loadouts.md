# Skills vs Dynamic MCP Loadouts

**Author:** Armin Ronacher
**Published:** December 13, 2025
**Source URL:** https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/
**Archived:** 2026-01-23

---

## Overview

Armin Ronacher, creator of Flask, Rye, and uv, argues that manually-maintained skills outperform Model Context Protocol (MCP) implementations, even with Anthropic's newer dynamic tool loading approach. He contends that having agents write their own tools as skills provides better control and adaptability than relying on external MCP servers.

## Key Findings

### On Tool Loading

Ronacher explains that MCP defers tool definitions but requires significant LLM API engineering, whereas skills use summaries that don't load full tool definitions into context. The agent learns "tips and tricks for how to use these tools more effectively" rather than new tool definitions.

### The MCP Problem

MCP servers lack API stability—they continuously modify tool descriptions to preserve tokens. This creates tension: descriptions become "too long to eagerly load it, and too short to really tell the agent how to use it."

### Practical Preference

Ronacher's current approach is straightforward: "I tend to go with what is easiest, which is to ask the agent to write its own tools as a skill." While potentially buggy, having agents maintain their own tools proves more practical than external MCP management.

### Token Cost Impact

The Sentry MCP consumed approximately 8,000 tokens immediately upon loading, making it economically inefficient compared to maintained skills.

## Key Quotes

> "I tend to go with what is easiest, which is to ask the agent to write its own tools as a skill."

> Tool descriptions are "too long to eagerly load it, and too short to really tell the agent how to use it."

> Sentry MCP: "~8,000 tokens immediately upon loading"

## Conclusion

Without protocol stability improvements and built-in manual systems for MCP tools, manually-maintained skills remain superior for agentic workflows.

---

**Archive Notes:**

This article represents a critical perspective from a highly respected developer on the fundamental tension in MCP design: balancing comprehensive documentation with token efficiency. Key insight: agent-authored skills provide better adaptability than static MCP definitions.
