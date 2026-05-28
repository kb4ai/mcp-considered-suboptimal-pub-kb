---
source_url: https://github.com/operasoftware/opera-browser-cli
title: "opera-browser-cli: AXI-compliant browser CLI"
author: "Opera Software"
publication_date: "~2026 (pre-2026-05)"
archive_date: "2026-05-17"
archived_by: "Claude Code (Opus 4.7)"
fetch_status: "ok"
---

# opera-browser-cli

**Source:** https://github.com/operasoftware/opera-browser-cli
**Author:** operasoftware (Opera ASA)
**License:** MIT
**Archived:** 2026-05-17

---

## What It Is

`opera-browser-cli` is described as **"the most agent-ergonomic browser automation"** tool from Opera Software. It wraps `opera-devtools-mcp` with an **AXI-compliant CLI interface** — significant because it's a *corporate vendor* (not an individual hobbyist) adopting Kun Chen's AXI framework.

## AXI Compliance

The README explicitly states it provides an **"AXI-compliant CLI"** and emphasizes:

1. **Token efficiency** — TOON encoding reduces token consumption ~40% vs raw JSON
2. **Combined operations** — Single commands handle navigation, capture, and next-step suggestions
3. **Contextual suggestions** — Every response includes actionable hints

## Sample Commands

```bash
opera-browser-cli open https://example.com        # navigate + snapshot
opera-browser-cli click @1                        # interact with element
opera-browser-cli chat "summarize this page"      # AI integration (Opera Neon)
```

## Scope

40+ commands across: interaction, emulation, DevTools debugging, and AI-powered features (Opera Neon exclusive).

## Significance for AXI Movement

This is the **first major corporate adoption** of AXI principles. Opera shipping an AXI-compliant CLI signals that AXI is moving from individual-project experiment toward a de-facto convention for agent-tool design — analogous to how UX patterns spread from individual designers to corporate design systems.
