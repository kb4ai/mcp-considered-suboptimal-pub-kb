# Firecrawl Claude Plugin - CLI Skill Implementation

**Source:** `firecrawl/firecrawl-claude-plugin` GitHub repository
**File:** `README.md`
**Commit:** `684b975c8cc6bd0fcfa96f787900bf87fffeef57`
**Archived:** 2026-02-18
**Permalink:** https://github.com/firecrawl/firecrawl-claude-plugin/blob/684b975c8cc6bd0fcfa96f787900bf87fffeef57/README.md
**Repository:** https://github.com/firecrawl/firecrawl-claude-plugin

---

## Why This Matters

This is the implementation of the Firecrawl plugin for Claude Code. It is explicitly architected as a **Skill that wraps a CLI tool** (`firecrawl-cli`), not as an MCP server integration. Firecrawl already had and maintained a separate `firecrawl-mcp-server` repository. This plugin was built as a deliberate CLI-first alternative.

The README itself states: "adds the Firecrawl CLI as a skill to Claude Code."

---

## Architecture: Skill + CLI

The plugin works by:

1. Claude Code installs the plugin (from Anthropic's marketplace)
2. The user installs the `firecrawl-cli` npm package globally
3. Claude Code invokes `firecrawl` CLI commands as a Skill
4. Results are written to `.firecrawl/` directory (not passed back through MCP protocol)

This means:

* **No MCP server process** to manage
* **No JSON-RPC** overhead
* **File-based output** keeps context window clean
* **Standard CLI auth** (env vars or `firecrawl login`)

---

## Installation

### 1. Install the Plugin
```
/plugin -> search "firecrawl" -> install
```

### 2. Install Firecrawl CLI
```bash
npm install -g firecrawl-cli
```

### 3. Authenticate

Option A - Browser authentication:
```bash
firecrawl login --browser
```

Option B - API key:
```bash
firecrawl login --api-key "fc-YOUR-API-KEY"
```

Option C - Environment variable:
```bash
export FIRECRAWL_API_KEY=fc-YOUR-API-KEY
```

### 4. Verify
```bash
firecrawl --status
```

---

## CLI Commands Available as Skills

| Command | Description |
|---------|-------------|
| `firecrawl search "query"` | Web search (supports --sources, --scrape, --tbs) |
| `firecrawl scrape <url>` | Scrape single page to markdown |
| `firecrawl map <url>` | Discover all URLs on a site |
| `firecrawl crawl <url>` | Extract content from entire site |
| `firecrawl browser launch/execute/list/close` | Cloud browser + Playwright execution |
| `firecrawl --status` | Check auth, concurrency, remaining credits |

---

## Output File Organization

Results are saved to `.firecrawl/` directory:

```
.firecrawl/search-react_server_components.json
.firecrawl/docs.github.com-actions-overview.md
.firecrawl/firecrawl.dev.md
```

This file-based approach preserves Claude Code's context window - results are not injected inline, they are written to disk and referenced by path.

---

## Natural Language Usage Examples

```
Search for "best practices for React testing" and compile the key recommendations
```

```
Scrape https://docs.firecrawl.dev/introduction and summarize the key points
```

```
Map all URLs on https://firecrawl.dev
```

```
Research the latest developments in AI agents and give me a summary
```

---

## Configuration

| Variable | Required | Purpose |
|----------|----------|---------|
| `FIRECRAWL_API_KEY` | Yes (if not using login) | API authentication |
| `FIRECRAWL_API_URL` | No | Custom endpoint for self-hosted |

---

## License

AGPL-3.0 (consistent with main Firecrawl project)

---

## Relevance to CLI-over-MCP Thesis

This implementation demonstrates the Skill+CLI pattern in practice:

* The Skill definition tells Claude Code what capabilities exist and when to use them
* The actual work is delegated to the `firecrawl-cli` binary via shell invocation
* File-based output avoids MCP protocol overhead and context window pollution
* Authentication is handled by the CLI tool itself, not by MCP server configuration
* Works identically whether Claude Code runs locally or remotely - no server lifecycle management

Compare with `firecrawl-mcp-server`: that requires running a persistent server process, JSON-RPC communication, MCP tool registration, and injects all results directly into the LLM context.

See also:

* `anthropic-marketplace--firecrawl-cli-plugin-entry.md` - The marketplace entry that listed this plugin
* `firecrawl--org-profile-mcp-and-cli.md` - Proof both MCP and CLI options exist
