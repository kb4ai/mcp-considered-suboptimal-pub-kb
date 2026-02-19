# Firecrawl in Claude Marketplace: CLI Skill Over MCP

*Discovered: 2026-02-18*

## The Finding

Anthropic's official Claude Code plugin marketplace (`anthropics/claude-plugins-official`) includes Firecrawl — a well-known web scraping service. The critical detail: **Firecrawl chose to build a Skill+CLI plugin, NOT a Skill+MCP plugin**, despite having an official MCP server available.

This is a clear, authoritative signal that the industry (including parties closest to Anthropic) prefers CLI over MCP for agent tooling.

---

## The Evidence Chain

### 1. Anthropic's Official Marketplace Entry

The `marketplace.json` in Anthropic's own repo lists the Firecrawl plugin:

```json
{
  "name": "firecrawl",
  "description": "Web scraping and crawling powered by Firecrawl. Turn any website into clean, LLM-ready markdown or structured data. Scrape single pages, crawl entire sites, search the web, and extract structured information. Includes an AI agent for autonomous multi-source data gathering - just describe what you need and it finds, navigates, and extracts automatically.",
  "category": "development",
  "source": {
    "source": "url",
    "url": "https://github.com/firecrawl/firecrawl-claude-plugin.git"
  },
  "homepage": "https://github.com/firecrawl/firecrawl-claude-plugin.git"
}
```

**Permalink:** [marketplace.json#L643-L652](https://github.com/anthropics/claude-plugins-official/blob/261ce4fba4f2c314c490302158909a32e5889c88/.claude-plugin/marketplace.json#L643C1-L652C6)

Note: The `source.url` points to a **git repository containing a Claude Code skill**, not an MCP server endpoint.

### 2. The Plugin Is a CLI Skill, Not MCP

The Firecrawl Claude plugin repository states:

> "This plugin adds the [Firecrawl CLI](https://github.com/firecrawl/cli) as a skill to Claude Code"

**Permalink:** [README.md#L5](https://github.com/firecrawl/firecrawl-claude-plugin/blob/684b975c8cc6bd0fcfa96f787900bf87fffeef57/README.md?plain=1#L5C1-L5C97)

The architecture is:

```
Claude Code Agent → Skill (prompt instructions) → Bash tool → Firecrawl CLI → Web
```

NOT:

```
Claude Code Agent → MCP Client → Firecrawl MCP Server → Web
```

### 3. Firecrawl Has an Official MCP Server

This is what makes the finding significant. Firecrawl explicitly offers MCP integration:

**Permalink:** [Firecrawl org README](https://github.com/firecrawl/.github/blob/eac6d8b43e11e1cc401a48e0e038a3c60fb53db9/profile/README.md)

The organization profile links to their MCP server alongside the CLI. They had both options. **They chose CLI for their Claude Code plugin.**

---

## Why This Matters

### Signal Strength: Very High

* **Authoritative source:** Anthropic's own official marketplace repository
* **Known brand:** Firecrawl is a widely-used web scraping service
* **Deliberate choice:** They maintain BOTH MCP and CLI — this wasn't a limitation, it was a preference
* **Cross-validation:** Firecrawl links to their Claude plugin from their own org profile, endorsing the CLI approach

### What This Validates

This directly supports the core thesis of this knowledge base:

1. **CLI > MCP for agent tooling** — Even service providers with MCP servers prefer CLI for agent integrations
2. **Skills + CLI is the emerging pattern** — The Claude Code ecosystem is converging on "skill as prompt + CLI as tool"
3. **MCP is not the default** — Despite being Anthropic's own protocol, their marketplace hosts CLI-based plugins
4. **Practitioners vote with their code** — When given a choice, builders choose the simpler, more composable approach

### The Pattern: Skill + CLI

The Claude Code plugin architecture that's emerging:

```
Plugin = Skill file (SKILL.md with instructions)
       + CLI tool (standard command-line interface)
       + Install script (setup.sh or similar)
```

This is essentially the UNIX philosophy applied to AI agent tooling:

* The **skill** tells the agent WHAT to do and WHEN
* The **CLI** does the actual work via Bash
* **Pipes, jq, filtering** happen in the shell, not in context
* The agent's context stays clean

---

## Permalink Archive

All permalinks captured at time of discovery (2026-02-18):

| Source | Permalink |
|--------|-----------|
| Marketplace entry | [anthropics/claude-plugins-official/.claude-plugin/marketplace.json#L643-L652](https://github.com/anthropics/claude-plugins-official/blob/261ce4fba4f2c314c490302158909a32e5889c88/.claude-plugin/marketplace.json#L643C1-L652C6) |
| Plugin README | [firecrawl/firecrawl-claude-plugin/README.md#L5](https://github.com/firecrawl/firecrawl-claude-plugin/blob/684b975c8cc6bd0fcfa96f787900bf87fffeef57/README.md?plain=1#L5C1-L5C97) |
| Firecrawl org profile | [firecrawl/.github/profile/README.md](https://github.com/firecrawl/.github/blob/eac6d8b43e11e1cc401a48e0e038a3c60fb53db9/profile/README.md) |
| Firecrawl CLI repo | [firecrawl/cli](https://github.com/firecrawl/cli) |
| Firecrawl MCP server | (referenced in org profile, available but NOT chosen for Claude plugin) |

---

## Connection to Existing Sources

This finding strengthens several existing arguments:

* **Ronacher's "Skills vs Dynamic MCP Loadouts"** — Skills + CLI is exactly what Firecrawl implements
* **Anthropic's own "Code Execution with MCP"** — Their marketplace now hosts CLI-first plugins
* **Linearis / webctl pattern** — Firecrawl joins the growing list of CLI-first agent tools
* **ainoya's "Why CLI instead of MCP"** — Same conclusion, now validated by a major service provider

---

*Part of [MCP Considered Suboptimal](../README.md)*
