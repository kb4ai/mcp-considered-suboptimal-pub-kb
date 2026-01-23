# Linearis: A Linear CLI Tool Built for Humans (and LLM Agents)

**Author:** Carlo Zottmann
**Published:** September 3, 2025
**Last Modified:** November 3, 2025
**Source URL:** https://zottmann.org/2025/09/03/linearis-my-linear-cli-built.html
**Archived:** 2026-01-23

---

## Overview

Carlo Zottmann created Linearis, a lightweight command-line interface for Linear.app designed specifically for LLM agents and developers who work with structured data. The tool addresses a critical problem: the official Linear MCP server consumed approximately 13,000 tokens just for connection and tool definitions, leaving less context window for actual work.

## The Problem

While using Claude Code and other AI tools, Zottmann noticed the Linear MCP server occupied a significant portion of his available token budget. The server offered 20+ features when he only needed "three or four" in practice. Additionally, the MCP server couldn't be used directly in shell scripts, limiting its utility for automation.

## Linearis Features

The tool focuses on core workflows:

* **Create and update tickets** with full context or minimal information
* **Manage relationships** between issues, including parent-child connections
* **Search and filter** issues with smart ID resolution
* **Add comments and labels** for progress tracking
* **JSON output** for integration with other tools like `jq`

### Usage Examples

```bash
# Display comprehensive usage information
linearis usage

# Create tickets with full context
linearis issues create "Fix login timeout" --team Backend \
  --assignee user123 --labels "Bug,Critical" --priority 1

# Smart ID resolution (supports ABC-123 format)
linearis issues read DEV-456
linearis issues update ABC-123 --state "In Review"

# JSON output for piping to other tools
linearis issues list -l 5 | jq '.[] | .identifier + ": " + .title'

# Add progress comments
linearis comments create ABC-123 --body "Fixed in PR #456"
```

## Agent-Friendly Design

The tool was built with LLM agents in mind. Running "linearis usage" provides comprehensive documentation that agents can incorporate directly into their context. Consistent flag structures and straightforward syntax enable agents to call the tool through bash without special integration.

Zottmann recommends including guidance in prompt documents, such as: "We use the `linearis` CLI tool for communicating with Linear. Use your Bash tool to call the `linearis` executable."

## Design Philosophy

Rather than attempting comprehensive feature coverage, Linearis excels at handling specific, frequently-used operations. Web UI tasks like workspace setup remain separate, keeping the CLI focused and token-efficient. This design choice reflects practical development experience: solve the problems you actually encounter.

## Key Design Decisions & CLI Ergonomics Patterns

### 1. Token Efficiency First

* **Problem:** Official Linear MCP server uses ~13,000 tokens for initialization
* **Solution:** Minimal tool that provides only essential features
* **Pattern:** Focus on "3-4" core operations instead of 20+ comprehensive features

### 2. Agent-Oriented Documentation

* **Pattern:** `linearis usage` command provides complete documentation
* **Benefit:** Agents can self-document by reading usage output
* **Design:** Single command gives full context for LLM consumption

### 3. Shell-First Philosophy

* **Pattern:** Standard CLI tool callable from bash
* **Benefit:** Works in scripts, automation, and agent tool calls
* **Contrast:** MCP servers require special integration, not shell-accessible

### 4. Smart ID Resolution

* **Pattern:** Accept Linear's natural format (e.g., `ABC-123`, `DEV-456`)
* **Benefit:** Matches how users think about issues
* **Ergonomics:** No need to look up internal IDs or UUIDs

### 5. Composable JSON Output

* **Pattern:** Output JSON for piping to `jq` and other tools
* **Benefit:** Integrates into Unix philosophy of small, composable tools
* **Example:** `linearis issues list | jq '.[] | select(.priority == 1)'`

### 6. Consistent Flag Structure

* **Pattern:** Similar flags across commands (--team, --assignee, --labels)
* **Benefit:** Predictable interface for both humans and LLMs
* **Ergonomics:** Once learned for one command, applies to all

### 7. Progressive Disclosure

* **Pattern:** Support both minimal and full-context operations
* **Example:** Quick create with just title vs. full ticket with all metadata
* **Benefit:** Accommodates different workflows and urgency levels

### 8. Focused Scope

* **Philosophy:** "Solve the problems you actually encounter"
* **Decision:** Skip workspace setup, team management (use web UI)
* **Pattern:** Core CRUD operations only - no administrative features
* **Benefit:** Stays lightweight, maintainable, token-efficient

### 9. Prompt Integration Guidance

* **Recommendation:** Add to project CLAUDE.md or similar
* **Example:** "We use the `linearis` CLI tool for Linear. Use Bash tool to call it."
* **Pattern:** Document tool availability in agent instructions

### 10. No Special Integration Required

* **Pattern:** Standard CLI, not an MCP server or plugin
* **Benefit:** Works immediately with any agent that can call bash
* **Design:** Leverage existing Bash tool instead of creating new tool type

## Installation

```bash
npm install -g --install-links czottmann/linearis
```

After installation, users authenticate through the standard Linear API process and begin using the tool immediately.

## Related Resources

* GitHub Repository: https://github.com/czottmann/linearis
* Linear API Documentation: https://developers.linear.app/docs/graphql/working-with-the-graphql-api

---

**Archive Notes:**

This article represents a critical critique of the MCP (Model Context Protocol) approach through a practical alternative. Key insights:

* Token budget matters: 13k tokens for tool definitions is prohibitive
* Simplicity wins: 3-4 features beats 20+ for real workflows
* Shell accessibility: Standard CLI tools integrate better than specialized servers
* Design for agents: Self-documenting commands (`linearis usage`) enable LLM autonomy
* Progressive disclosure: Support both quick and detailed operations
* Unix philosophy: Composable tools with JSON output integrate naturally

The author's experience demonstrates that purpose-built, minimal CLI tools can outperform comprehensive MCP servers for agent workflows.
