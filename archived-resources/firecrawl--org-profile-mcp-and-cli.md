# Firecrawl GitHub Organization Profile - Both MCP Server and CLI Available

**Source:** `firecrawl/.github` repository, organization profile
**File:** `profile/README.md`
**Commit:** `eac6d8b43e11e1cc401a48e0e038a3c60fb53db9`
**Archived:** 2026-02-18
**Permalink:** https://github.com/firecrawl/.github/blob/eac6d8b43e11e1cc401a48e0e038a3c60fb53db9/profile/README.md
**Organization:** https://github.com/firecrawl

---

## Why This Matters

This is the critical "smoking gun" document. Firecrawl's own organization profile explicitly lists **both** their MCP server and their CLI/Skill tool as distinct, maintained products. This proves that when Firecrawl built the official Claude Code marketplace plugin as a CLI Skill, it was a **deliberate architectural choice** - not a workaround due to lack of MCP capability.

They had both. They chose CLI for the Anthropic marketplace.

---

## Firecrawl Product Ecosystem (from org profile)

### Main Repository - `firecrawl`
- Core API and SDK
- 40,000+ GitHub stars
- Converts entire websites into markdown or structured data
- The foundation product

### Cloud API - `firecrawl.dev`
- Production-ready hosted service
- Eliminates infrastructure management
- API key based access

### MCP Integration - `firecrawl-mcp-server`
- **Model Context Protocol Server** for LLM integration
- Adds web scraping capabilities to Claude, Cursor, and compatible clients
- A fully working, maintained MCP server product

### Skill + CLI - `firecrawl-cli` / `firecrawl-claude-plugin`
- **Agent skill and command-line tool**
- Installable via: `npx skills add firecrawl/cli`
- Enables AI agents (Claude Code, Codex, Gemini CLI) autonomous web capabilities
- The product used in Anthropic's official marketplace

---

## The Choice

| Option | Exists? | Used in Anthropic Marketplace? |
|--------|---------|-------------------------------|
| firecrawl-mcp-server | Yes | No |
| firecrawl-claude-plugin (CLI Skill) | Yes | **Yes** |

Firecrawl explicitly supports multiple AI coding assistant platforms via the CLI/Skill approach:

* Claude Code
* Codex
* Gemini CLI

The MCP server supports Claude (Desktop/generic) and Cursor - tools where MCP is the primary integration mechanism. For agentic coding assistants that have a plugin/skill system, Firecrawl chose CLI.

---

## Community and Resources

* Discord community
* X (Twitter): @firecrawl\_dev
* GitHub Discussions
* Documentation: docs.firecrawl.dev
* Playground: firecrawl.dev/playground
* Main repository: github.com/mendableai/firecrawl

---

## Relevance to CLI-over-MCP Thesis

This document closes the argument that "Firecrawl used CLI because they didn't have MCP." They maintained both simultaneously. The Firecrawl team made a product decision about which integration pattern to publish to Anthropic's curated marketplace. They selected:

* CLI Skill: for Claude Code, Codex, Gemini CLI (agentic coding tools)
* MCP Server: for Claude Desktop, Cursor (IDE/chat tools where MCP is native)

This is a real-world practitioner's segmentation of when to use MCP vs CLI - and for the agentic coding assistant context, CLI won.

See also:

* `anthropic-marketplace--firecrawl-cli-plugin-entry.md` - The Anthropic marketplace entry
* `firecrawl--claude-plugin-cli-skill.md` - The CLI Skill implementation details
