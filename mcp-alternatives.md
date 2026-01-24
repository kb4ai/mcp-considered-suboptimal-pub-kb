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

### Slack

| MCP Server | CLI Alternative |
|------------|-----------------|
| Official Slack MCP | [slack-cli-mcp-wrapper](https://github.com/CLIAI/slack-cli-mcp-wrapper) |

The wrapper provides CLI access that agents can script, filter, and audit.

---

### Linear

| MCP Server | CLI Alternative |
|------------|-----------------|
| Official Linear MCP (~13k tokens) | [Linearis](https://github.com/czottmann/linearis) (~200 tokens) |

**Resources:**

* [Linearis GitHub](https://github.com/czottmann/linearis)
* [Design article](https://zottmann.org/2025/09/03/linearis-my-linear-cli-built.html) ([archived](archived-resources/zottmann--linearis-linear-cli-built.md))
* [Workarounds & extensions](https://gist.github.com/g-click-trade/3d73f0492abd2e5c75baa863053867dc) (suggested for upstream integration)

**Why Linearis wins:**

> "Token budget matters: 13k tokens for tool definitions is prohibitive. Simplicity wins: 3-4 features beats 20+ for real workflows."

---

### GitHub

| MCP Server | CLI Alternative |
|------------|-----------------|
| GitHub MCP servers | [`gh`](https://github.com/cli/cli) (official GitHub CLI) |

The `gh` CLI is already installed on most dev machines, pre-trained in LLMs, and fully scriptable:

```bash
# Examples agents can run directly
gh issue list --limit 20 --json title,number | jq '.[].title'
gh pr view 123 --json body,reviews
gh api repos/owner/repo/commits --paginate | jq '.[].sha'
```

---

### More Services (Help Wanted)

We're tracking CLI alternatives for common MCP servers. See "Contribute" below.

| Service | MCP Server Exists? | CLI Alternative? |
|---------|-------------------|------------------|
| Jira | Yes | `jira-cli`? |
| Notion | Yes | ? |
| Confluence | Yes | ? |
| Google Drive | Yes | `gdrive`? `rclone`? |
| Figma | Yes | ? |
| Asana | Yes | ? |

---

## Contribute: Share Your CLI Tools

**We want to hear from you!**

If you have a CLI tool that works well with LLM agents, or an MCP server you'd like to see replaced, please [open a GitHub issue](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/issues/new).

### Share a CLI alternative

Tell us:

* What service does it replace?
* Link to the CLI tool
* Why is it better for agents? (scripting, fuzzy search, audit logs, token savings...)

### Request an MCP replacement

Tell us:

* Which MCP server do you want replaced?
* What's wrong with it? (token bloat, no scripting, missing features...)
* What would make a CLI version better?

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

## Further Reading

* [Core Thesis](THESIS.md) — Why CLI beats MCP
* [FAQ](FAQ.md) — Sandboxing, lazy loading, self-optimization
* [MCP Critique Sources](mcp-critique-sources.md) — Industry voices

---

*Part of [MCP Considered Suboptimal](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb)*
