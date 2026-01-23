# 98% of MCP Servers Got This Wrong: The Reason Why the Protocol Never Worked

**Archive Metadata:**

* **Original URL:** https://hackernoon.com/98percent-of-mcp-servers-got-this-wrong-the-reason-why-the-protocol-never-worked
* **Author:** @hacker661972
* **Publication Date:** November 15, 2025
* **Platform:** HackerNoon
* **Archive Date:** 2026-01-23
* **Archived By:** Claude Code (Sonnet 4.5)

---

## TLDR

The article argues that Anthropic's Model Context Protocol (MCP) suffers from fundamental architectural flaws rather than implementation issues. The author contends that the recent "Code Execution with MCP" blog post represents damage control, not innovation. The core problem: LLMs function as pattern-matching systems where "every token in context adds noise." Production-ready MCP implementations maintain extremely limited toolsets (3-5 tools maximum), and approximately 98% of MCP servers lack essential production features like OAuth, permission enforcement, state management, and observability.

---

## Article Content

Three years ago, I read the Steve Jobs biography. The part about the iPhone obsessed me. Not the design. The philosophy: "People don't know what they want until you show it to them."

He was right about phones. But somewhere along the way, the AI industry got it backwards.

Last week, Anthropic published its engineering blog post on "Code Execution with MCP." The post celebrated a 98.7% token reduction by having agents write code instead of making direct tool calls.

The AI community erupted. "This is brilliant!" "This solves the context problem!"

But here's the thing: this isn't innovation. It's damage control.

## The Broken Design We Didn't Want to Admit

When the Model Context Protocol launched, it made sense. Direct function definitions seemed logical. Load the tool definitions into context, let the model pick which one to call, and observe the results.

Except it was broken from the start. Not in implementation. In design philosophy.

> **Key Quote:** "LLMs aren't traditional software systems where more data equals better decisions. They're pattern-matching machines. Every token in context adds noise."

Think of it like this => imagine a librarian trying to answer your question. Give her one shelf of relevant books, and she finds your answer quickly. Give her the entire library and ask her to answer in 30 seconds? She'll get confused. She'll miss the good information buried in mediocrity.

That's what we did to LLMs with MCP.

Context efficiency isn't a nice-to-have optimization. It's the entire game.

And if you look at actual MCP implementations in production, you see this clearly. The servers that work are exceptional. They have extremely limited, well-curated toolsets. Maybe 3-5 tools, max.

Anything more and you've instantly created a context nightmare.

Most MCP servers? They're architectural mistakes.

> **Key Quote:** "I can say this confidently because Anthropic saves 98.7% of tokens by having agents write code instead of calling tools directly. And do you know what else is 98%? The percentage of MCP servers in the wild that violate basic architectural principles. That's not a coincidence."

## What 98% of MCP Servers Got Wrong

The ecosystem is drowning in worthless MCP servers. Not because the people building them are incompetent. Because they started with the wrong assumption: that MCP is a user-facing tool integration standard.

It's not. It should have been backend infrastructure from day one.

**Here's what a non-worthless MCP server actually requires:**

* OAuth and proper authentication (not toy API keys)
* Permission management with enforcement (fine-grained access control)
* State management (a database backing the state)
* Observability (monitoring, logging, traces)

> **Key Quote:** "Do you know how many MCP servers have all of these? A handful. Maybe 2% of the ecosystem."

## The Signal-to-Noise Ratio Nobody Talks About

LLMs are pattern recognition systems. More tokens mean more data points. But it also means more noise.

At a certain ratio, noise overwhelms signal.

Think about forensics. Give a detective one piece of evidence, and it's compelling. Give them a million pieces of evidence, 99% of which are irrelevant? They'll miss the actual crime.

That's what we've been doing. Handing LLMs massive amounts of context and wondering why they're underperforming.

The real optimization isn't bigger context windows. It's ruthless context curation. Progressive, on-demand context loading. Only the information that matters.

## The Real Architecture: MCP as Backend, A2A as Frontend

Here's what's actually happening in the ecosystem:

A2A (Agent-to-Agent protocol) is becoming the user-facing standard. MCP is becoming what it should have been all along: a backend concern.

These aren't competing protocols. They're complementary.

## The Contrarian Takes

Let me say the things nobody wants to say:

> **Key Quote:** "Early MCP adoption was a mistake. Too many companies built on MCP, thinking it was production-ready. The ecosystem wasted cycles."

* Most developers won't implement this correctly. Code execution with MCP requires security thinking. Systems programming knowledge. Most teams have none of these.

## Practical Reality: What This Means for You

If you're building with MCP right now, here's what I'd do:

* **Audit your MCP tools immediately.** If you're at 5+, you have a context problem. If you're at 10+, your implementation is almost certainly broken.
* **Don't build toy MCP servers.** If you're thinking of building one, start by assuming it needs OAuth, permissions, and a database.
* **Migrate toward code execution patterns now.** Start having agents write code instead of calling tools directly.
* **Plan for the A2A transition.** Build abstraction layers so you can swap implementations without rewriting your entire system.
* **Monitor token efficiency obsessively.** Start measuring context window usage per request.

## The Bigger Picture

The MCP story is actually the story of how the AI industry approaches problem-solving.

We saw a problem (tools don't integrate with models well) and picked a solution quickly. It made sense at the time. It even worked, for a while.

Then reality hit. The solution didn't scale. We tried patching it with better tools, better definitions, and bigger context windows.

Finally, we realized: the problem wasn't the tools. The problem was the architecture.

When you fix the architecture. When you shift from "load all tool definitions upfront" to "load tools on demand via code execution", you solve it cleanly.

> **Key Quote:** "This is what expertise looks like. Not intelligence. Not raw capability. But the hard-earned pattern recognition that comes from shipping broken systems and fixing them."

## The Bottom Line

Context efficiency. On-demand tool discovery. Separation of concerns.

MCP will evolve to support this. A2A will mature alongside it. The ecosystem will consolidate.

And 98% of the MCP servers built in 2025? They'll be quietly archived, reminders of what happens when you optimize for the wrong metric.

But here's what gives me hope: the industry is learning. We're being honest about what didn't work. We're building better architecture. We're respecting constraints instead of ignoring them.

That's not failure.

That's expertise.

> **Key Quote:** "And expertise, unlike intelligence, can't be automated."

---

## Resources

* Anthropic's Code Execution with MCP: https://www.anthropic.com/engineering/code-execution-with-mcp
* A2A Protocol Specification: https://a2aprotocol.ai/
* MCP Protocol Documentation: https://modelcontextprotocol.io/
* On Context Engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
* Signal-to-Noise in LLMs: https://huggingface.co/papers/2406.06623
* Original Blog: https://tyingshoelaces.com/blog/mcp-reckoning

---

## Related Topics / Tags

#model-context-protocol #mcp #anthropic #what-is-mcp #mcp-problems #mcp-flaws #mcp-as-backend #a2a #machine-learning #artificial-intelligence #context-efficiency #llm-architecture

---

## Archive Notes

This article presents a critical analysis of Anthropic's Model Context Protocol (MCP) from a practitioner's perspective. The author argues that the protocol's fundamental design philosophy is flawed because it treats LLMs as traditional software systems rather than pattern-matching machines sensitive to context noise.

**Key Arguments:**

1. **Token Efficiency is Critical:** The 98.7% token reduction achieved by code execution approaches reveals that most MCP implementations are architecturally inefficient.

2. **Production Requirements Gap:** Only ~2% of MCP servers implement essential production features (OAuth, permissions, state management, observability).

3. **Context Management:** The core issue is that loading all tool definitions upfront creates excessive context noise, degrading LLM performance.

4. **Architectural Evolution:** MCP should be backend infrastructure, while A2A (Agent-to-Agent) serves as user-facing protocol.

5. **Practical Guidance:** Production systems should limit tools to 3-5 maximum and migrate toward code execution patterns.

The article is notable for its contrarian stance, openly criticizing early MCP adoption as premature and calling out the ecosystem's "worthless" implementations. The author uses the Jobs biography philosophy ("People don't know what they want until you show it to them") to argue the AI industry built what seemed logical rather than what actually works.

**Publication Context:** Published November 15, 2025, shortly after Anthropic's blog post about code execution with MCP, this article represents community pushback and critical technical analysis of a major protocol initiative.
