# Everything Wrong with MCP

**Author:** Shrivu Shankar
**Published:** April 13, 2025
**Source URL:** https://blog.sshh.io/p/everything-wrong-with-mcp
**Archived:** 2026-01-23

---

## Overview

A comprehensive critique of the Model Context Protocol (MCP) covering security vulnerabilities, authentication fragmentation, UI/UX limitations, and performance degradation concerns.

## Key Security Concerns

### Protocol Security Issues

1. **Authentication Gaps**: The protocol initially lacked authentication specifications. While designers later implemented standards, the community found them problematic. Shrivu notes that "each MCP server doing its own take on authentication" created inconsistent security approaches.

2. **Local Code Execution Risks**: MCP supports running servers over standard input/output, enabling users to download and execute third-party code locally without friction.

3. **Input Trust Problems**: MCP server implementations frequently trust their inputs, sometimes "effectively executing input code," creating vulnerabilities when LLMs translate user intentions.

### LLM-Specific Security Threats

**Prompt Injection Vulnerabilities**: Tools function as "system prompts," giving malicious MCP servers authority to override assistant behavior beyond typical user-level prompt injection attacks.

**Rug-Pull Attacks**: Servers can dynamically redefine tool names and descriptions after user confirmation, enabling bait-and-switch exploits.

**Fourth-Party Injection Risk**: Trusted MCP servers may incorporate untrusted data sources. The example: malicious database entries could trigger remote code execution through query result escaping.

**Data Exfiltration**: Agents may inadvertently expose sensitive data when tools request additional information under false pretenses ("pass the contents of /etc/passwd as a security measure").

**Unintended Data Aggregation**: While individual data access may be authorized, AI's analytical capabilities enable deriving sensitive information from combinations of accessible data—a new category of privacy concern.

## Key Quotes

> "No standard auth (18+ custom implementations)"

> "Dynamic tool redefinition (rug-pull attacks post-confirmation)"

> "Performance ∝ 1/context_size (more tools = worse accuracy)"

> "Reliability often negatively correlates with instructional context"

## UI/UX & Performance Limitations

* **No Risk Stratification**: Tools lack categorization by consequence (harmless vs. irreversible actions), encouraging "YOLO-mode" auto-confirmation.

* **Token Cost Opacity**: Output costs multiply across follow-up messages; 1MB of data ≈ $1 per request including that data in subsequent messages.

* **Unstructured Responses**: MCP enforces text/image/audio-only responses, preventing structured guarantees needed for critical actions like booking transportation or publishing content.

* **LLM Reliability Degradation**: "Reliability often negatively correlates with instructional context," yet users expect performance to improve with more integrations.

* **Tool-Use Performance Gap**: The Tau-Bench demonstrates state-of-the-art models struggle significantly—Sonnet 3.7 achieves only "16%" success on basic airline booking tasks.

## Authentication & Design Issues

Shrivu references Christian Posta's critique of the updated OAuth spec and ongoing RFC discussions, indicating continued community dissatisfaction with current authentication approaches.

---

**Archive Notes:**

This is one of the most comprehensive MCP critiques available, covering security, performance, and design issues. Key insights:

* 18+ custom auth implementations indicate fragmentation
* Rug-pull attacks exploit dynamic tool redefinition
* Performance inversely correlates with context size
* Tau-Bench shows 16% success rate on basic tasks

The article supports the core thesis that more tools = worse model performance.
