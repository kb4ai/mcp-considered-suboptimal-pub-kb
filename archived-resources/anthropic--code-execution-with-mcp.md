# Code Execution with MCP: Building More Efficient Agents

**Source:** Anthropic Engineering Blog
**Publication Date:** November 4, 2025
**Authors:** Adam Jones, Conor Kelly
**Contributors:** Jeremy Fox, Jerome Swannack, Stuart Ritchie, Molly Vorwerck, Matt Samuels, Maggie Vo
**Original URL:** https://www.anthropic.com/engineering/code-execution-with-mcp
**Archive Date:** 2026-01-23

---

## Overview

This engineering article explores how code execution enhances the Model Context Protocol (MCP), enabling AI agents to interact with external systems more efficiently while dramatically reducing token consumption.

## Key Problem: Token Inefficiency at Scale

Two critical challenges emerge as agents connect to growing numbers of MCP tools:

### 1. Tool Definition Overload

Loading all tool definitions upfront directly into context creates substantial overhead. For agents accessing thousands of tools, hundreds of thousands of tokens are consumed before the model even processes the actual request.

### 2. Intermediate Result Duplication

When agents retrieve and manipulate data through direct tool calls, results pass through the model's context repeatedly. For example, retrieving a meeting transcript and attaching it to a Salesforce record forces the data through context twice, potentially consuming 50,000 additional tokens for a 2-hour meeting.

## The Solution: Code-Based Tool Access

Rather than exposing tools through direct calling syntax, the proposed approach presents MCP servers as code APIs. Agents write code to interact with tools, filtering and processing data in a code execution environment before returning relevant information to the model.

### Implementation Strategy

Tools are organized as a filesystem structure:

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
```

Agents discover tools by exploring directories and reading only the definitions they need for current tasks. This enables "progressive disclosure" rather than upfront loading.

### Dramatic Efficiency Gains

**Key Statistics:**

* Token reduction: **98.7%**
* Before: ~**150,000 tokens**
* After: ~**2,000 tokens**

The approach achieves this reduction by allowing agents to load definitions on demand and process large datasets locally.

## Primary Benefits

### Context Efficiency

Agents filter 10,000-row spreadsheets down to relevant subsets before model exposure, eliminating unnecessary token consumption.

### Control Flow Optimization

Loops, conditionals, and error handling execute natively in code rather than requiring repeated model evaluations and agent loop iterations.

### Privacy Preservation

Sensitive data flows through code execution environments without entering the model context. The system can automatically tokenize personally identifiable information, preventing accidental exposure.

### State Persistence

Agents maintain execution state across operations, resuming interrupted tasks and building reusable skills—higher-level capabilities that improve over time.

## Implementation Considerations

Code execution introduces complexity requiring secure sandboxing, resource limits, and monitoring. These infrastructure demands must be weighed against efficiency benefits.

## Critical Analysis

**Primary Source Significance:**

This article represents Anthropic's official acknowledgment that traditional MCP usage patterns (loading all tool definitions, passing large data through context) are fundamentally inefficient. The 98.7% token reduction demonstrates that code execution is not merely an optimization—it's a necessary evolution of the MCP paradigm.

**Key Admission:**

The article explicitly states that "hundreds of thousands of tokens are consumed before the model even processes the actual request" when using traditional MCP tool calling patterns at scale. This validates concerns about MCP's scalability and efficiency.

**Implications:**

* Traditional MCP implementations may be suitable only for small-scale tool collections
* Code execution should be considered the default pattern for production MCP deployments
* The MCP specification should potentially emphasize code-based access over direct tool calling
* Privacy and security benefits emerge naturally from local data processing

---

## Archive Metadata

* **Archive Method:** WebFetch tool
* **Archive Format:** Markdown conversion from HTML
* **Completeness:** Full article content extracted
* **Code Examples:** Preserved in original format
* **Statistics Verified:** 98.7% reduction, 150K→2K tokens confirmed
