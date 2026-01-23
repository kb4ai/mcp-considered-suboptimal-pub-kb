# CLI/SDK Tools Over Context Window Bloat

**Thesis:** LLMs work better with scriptable CLI tools and SDK interfaces than with bloated context-window protocols like MCP.

---

## The Core Problem: Context is Not Infinite

LLMs are pattern-matching machines, not databases. Every token in context adds noise.

> "Give a detective one piece of evidence, and it's compelling. Give them a million pieces of evidence, 99% of which are irrelevant? They'll miss the actual crime."
> — HackerNoon, "98% of MCP Servers Got This Wrong"

**The Numbers:**

| Approach | Tokens | Reduction |
|----------|--------|-----------|
| Traditional MCP (load all tools) | 150,000 | — |
| Code execution / CLI | 2,000 | **98.7%** |

Source: Anthropic Engineering Blog, November 2025

---

## Why CLI/SDK Beats Context Bloat

### 1. Ad-Hoc Scripting

LLMs excel at writing code. Let them compose solutions:

```bash
# Instead of 20+ MCP tools in context...
linearis issues list -l 5 | jq '.[] | select(.priority == 1)'
```

The model writes the glue code. Data stays local. Tokens stay minimal.

> "Models do not get smarter when you give them more tools. They get smarter when you give them a small subset of really good tools."
> — Theo, t3.gg

### 2. Ergonomic Wrappers for Common Patterns

When patterns repeat, LLMs can create reusable functions:

```typescript
// Agent-generated wrapper
async function syncSalesforceFromDrive(docId: string) {
  const transcript = await gdrive.getDocument(docId);
  const pendingItems = transcript.sections
    .filter(s => s.type === 'action_item');
  return salesforce.batchUpdate(pendingItems);
}
```

The model evolves its own toolkit. Skills persist. No context waste.

### 3. Automation for Check/Update/Sync/Report Cycles

```bash
# Declarative automation, not token-burning tool chains
./sync-crm.sh --source=drive --dest=salesforce --filter=pending
./report-weekly.sh | mail -s "Status" team@company.com
```

Data flows through scripts, never through the model's context window.

### 4. Progressive Discovery

CLI tools are self-documenting:

```bash
linearis usage      # Model reads only what it needs
gdrive --help       # Not 13,000 tokens of definitions
```

> "Presenting tools as code on a file system allows models to read tool definitions on demand rather than reading them all up front."
> — Anthropic, "Code Execution with MCP"

---

## The Industrialization Argument

From Chris Loy's "The Rise of Industrial Software":

> "Innovation is fundamentally different to industrialization, because it is not focused on more efficiently replicating what already exists today. It instead advances through finding and solving new problems, building on what came before."

**Translation for AI tooling:**

* MCP = industrialization attempt (replicate integration patterns)
* CLI/SDK = innovation enabler (solve new problems via composition)

The tools should be **building blocks**, not **prescriptive workflows**.

---

## Mass Software Customization

Every user's needs differ. Generic MCP servers fail because:

* 20+ features when 3-4 are used
* 13,000 tokens for a Linear integration (Linearis uses ~200)
* No OAuth, no permissions, no observability in 98% of servers

**Better approach:** Minimal CLIs that users (and LLMs) customize:

| Pattern | Example |
|---------|---------|
| Quick lookup | `gh issue view 123` |
| Filtered search | `linearis issues list \| jq` |
| Batch operations | `for id in $(cat ids.txt); do ...; done` |
| Custom automation | Agent writes `sync-script.sh` |

---

## What LLMs Should Have Access To

Instead of:
```
[500 MCP tool definitions in system prompt]
```

Provide:
```
- Bash shell with standard CLI tools
- `--help` flags that explain usage
- JSON output for piping to jq
- SDK libraries importable in sandboxed code
```

> "We need more engineers in high places. This is what happens when we let LLM people make the things devs have to use."
> — Theo, t3.gg

---

## Practical Implementation

### Minimum Viable CLI for LLM Agents

1. **Self-documenting:** `tool usage` or `tool --help`
2. **JSON output:** Composable with `jq`
3. **Smart IDs:** Accept natural identifiers (`ABC-123` not UUIDs)
4. **Focused scope:** 3-5 core operations, not 20+
5. **Shell-first:** Callable from Bash, no special integration

### Agent Instruction Pattern

```markdown
## Available Tools

Use your Bash tool to call these CLIs:

- `linearis` for Linear (run `linearis usage` for docs)
- `gh` for GitHub (standard GitHub CLI)
- `curl` + `jq` for REST APIs
```

---

## The Privacy Bonus

When data flows through code, not context:

* PII never reaches the model
* Sensitive data stays in sandbox
* Audit trails are deterministic

> "The content of the document never becomes part of the context. It's never seen by the model because the model doesn't need to know what's in the doc. It needs to know what to do with it."
> — Theo, t3.gg

---

## Summary

| MCP Pattern | CLI/SDK Pattern |
|-------------|-----------------|
| Load 500 tools upfront | `tool --help` on demand |
| 150K tokens baseline | 2K tokens |
| Data through context | Data through code |
| Hallucination-prone | Deterministic execution |
| Generic workflows | Custom composition |
| Complex orchestration | Simple scripts |

**The future is not protocols. It's programmable tools.**

---

## Further Reading

* [Anthropic: Code Execution with MCP](archived-resources/anthropic--code-execution-with-mcp.md)
* [Linearis: CLI Built for Agents](archived-resources/zottmann--linearis-linear-cli-built.md)
* [Rise of Industrial Software](archived-resources/chrisloy--rise-of-industrial-software.md)
* [98% of MCP Servers Got This Wrong](archived-resources/hackernoon--98-percent-mcp-servers-wrong.md)
