# TODO: MCP Considered Suboptimal

*Created: 2026-01-23*

This file tracks all pending archival and research tasks for the repository.

---

## Priority 1: Archive New Critic Sources

These sources are referenced in `mcp-critique-sources.md` but not yet archived locally.

### Armin Ronacher (Flask/Rye/uv creator)

- [ ] **Archive:** https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/
  - Title: "Skills vs Dynamic MCP Loadouts"
  - Key quote: "45s/7 calls initial → 5s/1 call scripted"
  - Save as: `archived-resources/ronacher--skills-vs-dynamic-mcp-loadouts.md`

- [ ] **Archive:** https://lucumr.pocoo.org/2025/8/18/code-mcps/
  - Title: "Your MCP Doesn't Need 30 Tools"
  - Key quote: "Token cost: Well-designed MCPs still consume ~8k tokens"
  - Save as: `archived-resources/ronacher--mcp-doesnt-need-30-tools.md`

### Mario Zechner (Benchmarking)

- [ ] **Archive:** https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/
  - Title: "MCP vs CLI: Benchmarking Tools"
  - Key data: CLI $0.37 vs MCP $0.48
  - Save as: `archived-resources/zechner--mcp-vs-cli-benchmarks.md`

### LiquidMetal AI

- [ ] **Archive:** https://liquidmetal.ai/casesAndBlogs/mcp-api-wrapper-antipattern/
  - Title: "If Your MCP is an API Wrapper, You're Doing It Wrong"
  - Key concept: API wrapper antipattern
  - Save as: `archived-resources/liquidmetal--mcp-api-wrapper-antipattern.md`

### Shrivu Shankar

- [ ] **Archive:** https://blog.sshh.io/p/everything-wrong-with-mcp
  - Title: "Everything Wrong with MCP"
  - Key points: No standard auth, rug-pull attacks, performance degradation
  - Save as: `archived-resources/shankar--everything-wrong-with-mcp.md`

### ainoya.dev

- [ ] **Archive:** https://ainoya.dev/posts/why-cli-instead-of-mcp/
  - Title: "Why CLI instead of MCP"
  - Key contrast: 50k tokens raw JSON vs 2k filtered
  - Save as: `archived-resources/ainoya--why-cli-instead-of-mcp.md`

---

## Priority 2: Archive Further Reading Sources

These are linked in `mcp-critique-sources.md` "Further Reading" section.

- [ ] **Archive:** https://www.speakeasy.com/blog/how-we-reduced-token-usage-by-100x-dynamic-toolsets-v2
  - Title: "Speakeasy: 100x Token Reduction"
  - Key: Dynamic Toolsets approach
  - Save as: `archived-resources/speakeasy--100x-token-reduction.md`

- [ ] **Archive:** https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1576
  - Title: "SEP-1576: Token Bloat Mitigation"
  - Key: Official MCP issue acknowledging problem
  - Save as: `archived-resources/mcp-issue-1576--token-bloat-mitigation.md`

- [ ] **Archive:** https://jduncan.io/blog/2025-11-07-mcp-context-bloat/
  - Title: "MCP Context Bloat Analysis"
  - Save as: `archived-resources/jduncan--mcp-context-bloat-analysis.md`

---

## Priority 3: Quality & Intelligence Research

Find and archive sources supporting the "quality degradation" thesis in FAQ.md.

### Context Size vs. Model Performance

- [ ] **Find & Archive:** Studies showing model performance degradation with larger contexts
  - Search terms: "LLM context window performance", "attention dilution large context"
  - Needed for: FAQ.md claim about models becoming "distracted"

- [ ] **Find & Archive:** "Lost in the middle" phenomenon research
  - Key paper: Liu et al. "Lost in the Middle: How Language Models Use Long Contexts"
  - Shows: Models struggle with information in middle of long contexts
  - Supports: Quality degradation claim

### Agentic Workflow Error Compounding

- [ ] **Find & Archive:** Studies on error propagation in multi-step LLM workflows
  - Search terms: "agentic workflow error compounding", "LLM chain error propagation"
  - Needed for: FAQ.md claim about cascading failures

### Opus 4.5 as Claude Code Default

- [ ] **Find & Archive:** Anthropic announcement about Opus 4.5 as Claude Code default
  - Search: Anthropic blog, release notes, changelog
  - Key claim: More expensive model chosen because "higher intelligence per token"
  - Needed for: FAQ.md "context efficiency > raw token price" argument

### Intelligence vs. Context Trade-off Studies

- [ ] **Find & Archive:** Cost comparison studies
  - Compare: Smart model + small context vs. cheap model + large context
  - Search: Academic papers, industry benchmarks
  - Needed for: Supporting the core thesis

---

## Priority 4: Security Research

Find and archive sources for security concerns mentioned in FAQ.md and mcp-critique-sources.md.

- [ ] **Find & Archive:** MCP security vulnerabilities documented
  - Search: CVEs, security advisories, blog posts
  - Already have: Shrivu Shankar's "Everything Wrong with MCP" (covers some)

- [ ] **Find & Archive:** Prompt injection via tool definitions
  - Search: "MCP prompt injection", "tool definition injection"
  - Needed for: Security critique section

- [ ] **Find & Archive:** OAuth/auth fragmentation in MCP ecosystem
  - Already mentioned: Theo's quote "18 implementations"
  - Find: Detailed analysis of auth landscape

---

## Priority 5: MCP Aggregator/Gateway Documentation

Document these projects for reference (not endorsement).

- [ ] **Document:** Docker MCP Gateway
  - URL: Find official repo/docs
  - Purpose: Container isolation, secrets management

- [ ] **Document:** Microsoft MCP Gateway
  - URL: Find official repo/docs
  - Purpose: K8s-native, session-aware routing

- [ ] **Document:** MetaMCP
  - URL: Find official repo/docs
  - Purpose: Namespace-based aggregation

- [ ] **Document:** Magg
  - URL: Find official repo/docs
  - Purpose: Self-modifying MCP with discovery tools

---

## Archive Format Reminder

Each archived source should include:

1. **Main file:** `archived-resources/{author}--{slug}.md`
   - Full content with timestamps
   - Key quotes highlighted

2. **URL file:** `archived-resources/{author}--{slug}.md.url`
   - Original source URL

3. **Metadata:** `archived-resources/{author}--{slug}.md.meta.json`
   - Structured metadata (title, author, date, archive date)

---

## Completion Tracking

| Category | Total | Done | Remaining |
|----------|-------|------|-----------|
| New Critic Sources | 6 | 0 | 6 |
| Further Reading | 3 | 0 | 3 |
| Quality Research | 4 | 0 | 4 |
| Security Research | 3 | 0 | 3 |
| Aggregator Docs | 4 | 0 | 4 |
| **Total** | **20** | **0** | **20** |

---

*Last updated: 2026-01-23*
