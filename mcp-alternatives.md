# MCP Alternatives: CLI Tools for LLM Agents

*CLI tools that replace MCP servers — scriptable, auditable, token-efficient.*

---

## Why CLI Over MCP?

| Benefit | How CLI Delivers |
|---------|------------------|
| **Token efficiency** | No upfront tool definitions (~13k → ~200 tokens) |
| **Scriptability** | Chain commands, loops, conditionals |
| **Fuzzy search** | Filter results with `sk -f`, `fzf`, `rg` before context |
| **Audit logs** | Wrap CLI calls with logging, validation |
| **Composability** | Pipe JSON through `jq`, combine tools freely |

---

## Alternatives by Service

### GitHub

| MCP Server | CLI Alternative |
|------------|-----------------|
| GitHub MCP servers | [gh](https://github.com/cli/cli) |

Official GitHub CLI - pre-trained in LLMs, fully scriptable

**Resources:**

* [GitHub Repository](https://github.com/cli/cli)
* [Documentation](https://cli.github.com/manual/)

**Examples:**

```bash
# List issue titles
gh issue list --limit 20 --json title,number | jq '.[].title'
# View PR details
gh pr view 123 --json body,reviews
# List commit SHAs
gh api repos/owner/repo/commits --paginate | jq '.[].sha'
```

---

### Linear

| MCP Server | CLI Alternative |
|------------|-----------------|
| Official Linear MCP (~13k) | [Linearis](https://github.com/czottmann/linearis) (~200) |

CLI tool for Linear issue tracking, built for LLM agents

**Resources:**

* [GitHub Repository](https://github.com/czottmann/linearis)
* [Design Article](https://zottmann.org/2025/09/03/linearis-my-linear-cli-built.html) ([archived](archived-resources/zottmann--linearis-linear-cli-built.md))
* [Workarounds & Extensions](https://gist.github.com/g-click-trade/3d73f0492abd2e5c75baa863053867dc)

**Why it wins:**

> "Token budget matters: 13k tokens for tool definitions is prohibitive. Simplicity wins: 3-4 features beats 20+ for real workflows."
> — Carlo Zottmann

---

### Slack

| MCP Server | CLI Alternative |
|------------|-----------------|
| Official Slack MCP | [slack-cli-mcp-wrapper](https://github.com/CLIAI/slack-cli-mcp-wrapper) |

CLI wrapper providing Slack access that agents can script, filter, and audit

---

### Browser Automation

| MCP Server | CLI Alternative |
|------------|-----------------|
| Playwright MCP, browser MCP servers | [webctl](https://github.com/cosinusalpha/webctl) |

CLI browser automation for AI agents and humans. Filters output before it enters context — the agent controls what it sees, not the server.


**Resources:**

* [GitHub Repository](https://github.com/cosinusalpha/webctl)

**Why it wins:**

> "MCP browser tools have a fundamental problem: the server controls what enters your context. With Playwright MCP, every response includes the full accessibility tree plus console messages. After a few page queries, your context window is full. CLI flips this around: you control what enters context.
"
> — webctl README

**Examples:**

```bash
# Only buttons, links, inputs (skip full accessibility tree)
webctl snapshot --interactive-only --limit 30
# Scope to main content (skip nav, footer, ads)
webctl snapshot --within "role=main"
# Find specific elements via Unix pipes
webctl snapshot | grep -i "submit"
# Extract structured data with jq
webctl --format jsonl snapshot | jq ".data.role"
```

---

## More Services (Help Wanted)

We're tracking CLI alternatives for common MCP servers. See "Contribute" below.

| Service | MCP Server Exists? | CLI Alternative? |
|---------|-------------------|------------------|
| Asana | Yes | ? |
| Confluence | Yes | ? |
| Figma | Yes | ? |
| Google Drive | Yes | `gdrive`?, `rclone`? |
| Jira | Yes | `jira-cli`? |
| Notion | Yes | ? |

---

## Design Patterns for Agent-Friendly CLIs

When building or choosing CLI tools for LLM agents:

1. **`usage` or `--help` command** — Self-documenting for agents
2. **JSON output** — Composable with `jq`, `yq`
3. **Focused scope** — 3-5 core operations, not 20+
4. **Smart ID resolution** — Accept natural formats (e.g., `ABC-123`)
5. **Exit codes** — Clear success/failure for scripting
6. **Streaming support** — Don't buffer huge responses

See [CLI/SDK Over Context Bloat](cli-sdk-over-context-bloat.md) for detailed patterns.

---

## Contribute: Share Your CLI Tools

**We want to hear from you!**

### Ways to Contribute

| Method | Best For |
|--------|----------|
| [Submit CLI Tool](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/issues/new?template=submit-cli-tool.md) | Share a CLI alternative you've found or built |
| [Request Alternative](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/issues/new?template=request-alternative.md) | Ask for a CLI replacement for an MCP server |
| [Suggest Edit](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/issues/new?template=suggest-edit.md) | Typos, corrections, improvements |
| [Add Resource](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/issues/new?template=add-resource.md) | Share quotes, articles, sources |
| [Pull Request](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/pulls) | Direct contributions (preferred!) |

### For Contributors

Data lives in `mcp-alternatives/` directory:

- `*.cli.yaml` — CLI tool entries
- `*.wanted.yaml` — Wanted entries
- Run `./mcp-alternatives.regenerate.py` to rebuild the document

See [`mcp-alternatives/AGENTS.md`](mcp-alternatives/AGENTS.md) for schema details.

---

## Further Reading

* [Core Thesis](THESIS.md) — Why CLI beats MCP
* [FAQ](FAQ.md) — Sandboxing, lazy loading, self-optimization
* [MCP Critique Sources](mcp-critique-sources.md) — Industry voices

---

*Part of [MCP Considered Suboptimal](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb)*
