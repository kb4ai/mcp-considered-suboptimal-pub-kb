# Anthropic Claude Plugins Marketplace - Firecrawl Entry

**Source:** Anthropic's official `claude-plugins-official` repository
**File:** `.claude-plugin/marketplace.json` (lines 643-652)
**Commit:** `261ce4fba4f2c314c490302158909a32e5889c88`
**Archived:** 2026-02-18
**Permalink:** https://github.com/anthropics/claude-plugins-official/blob/261ce4fba4f2c314c490302158909a32e5889c88/.claude-plugin/marketplace.json#L643C1-L652C6

---

## Why This Matters

This is the firecrawl entry in Anthropic's own curated Claude Code plugin marketplace (`claude-plugins-official`). The marketplace lists approximately 50 plugins. The firecrawl entry is significant because:

1. It is hosted in **Anthropic's own repository** - this is the official, curated list
2. The source type is `"url"` pointing to a **git repository that implements a CLI-based Skill**, NOT an MCP server
3. Firecrawl already had a working MCP server (`firecrawl-mcp-server`) when this entry was created
4. The deliberate choice to use the CLI/Skill approach over MCP in Anthropic's own marketplace is strong architectural evidence

---

## The Firecrawl Marketplace Entry (JSON)

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

---

## Key Observations

* **source.source = "url"**: The plugin type is a git URL, meaning Claude Code will clone and install it as a Skill, not configure it as an MCP server
* **Points to `firecrawl-claude-plugin`**: This is the CLI-wrapping Skill repo, not the `firecrawl-mcp-server` repo
* **Category: "development"**: Standard tool category
* **Last entry in the ~50-plugin marketplace**: Firecrawl is entry #50 in the array

---

## Relevance to CLI-over-MCP Thesis

This entry constitutes direct primary evidence from Anthropic's own curation decisions. When Anthropic added Firecrawl to their official marketplace, they listed the CLI-based Skill plugin, not the MCP server that Firecrawl also offers. This is not an accident of availability - Firecrawl explicitly built and published both options. Anthropic chose to feature the CLI variant.

See also:

* `firecrawl--claude-plugin-cli-skill.md` - The actual CLI Skill implementation
* `firecrawl--org-profile-mcp-and-cli.md` - Proof that both MCP and CLI exist for Firecrawl
