# If Your MCP is an API Wrapper, You're Doing It Wrong

**Author:** Fokke Dekker
**Published:** August 13, 2025
**Source URL:** https://liquidmetal.ai/casesAndBlogs/mcp-api-wrapper-antipattern/
**Archived:** 2026-01-23

---

## Overview

The article critiques the common practice of building MCPs (Model Context Protocol servers) as straightforward API wrappers. The author argues this approach fundamentally misunderstands the nature of LLM users versus traditional software users.

## The Core Problem

Most companies "wrap their existing API, slap an MCP server on top, and ship it," resulting in MCPs that barely function. The author identifies three critical mistakes:

1. **Misidentifying the user** – MCPs serve language models, not deterministic software
2. **Poor error messaging** – Generic API errors don't help LLMs recover
3. **Multi-step workflows** – Forcing AI agents through sequential API calls instead of handling intent directly

## Wrong Usage Example

The GitHub ticket scenario illustrates the problem: requesting "Create a ticket and assign it to John" requires four separate MCP calls:

1. Projects endpoint lookup
2. Users endpoint search
3. Name-to-UUID resolution
4. Finally, ticket creation

This forces unnecessary context pollution and token waste.

## Key Quotes

> "Wrong User Model: LLM guesses UUID from ambiguous 'John'"

> "4-step workflow (projects→users→search→create) for 1 action"

## Recommended Alternatives

### Build for intent, not endpoints

* Start with actual user workflows ("Create and assign a ticket") rather than API mappings
* Embed intelligence in the MCP server to handle ambiguity
* Return structured, LLM-optimized responses with minimal extraneous data
* Design error messages that suggest recovery paths

### Implementation example

The Raindrop MCP implements a state machine guiding AI through application deployment, with each response including explicit `next_action` instructions rather than raw data dumps.

---

**Archive Notes:**

This article identifies a fundamental antipattern in MCP design: treating LLMs as deterministic API consumers. The 4-step workflow example demonstrates how poorly designed MCPs multiply token usage and context pollution. The recommended approach — intent-based design with embedded intelligence — aligns with the CLI/SDK philosophy of filtering data before it reaches the LLM.
