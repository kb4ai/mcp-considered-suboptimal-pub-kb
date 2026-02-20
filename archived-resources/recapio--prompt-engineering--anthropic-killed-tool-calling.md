---
source_url: https://recapio.com/digest/anthropic-just-killed-tool-calling-by-prompt-engineering
access_date: 2026-02-20
page_title: "Anthropic Just Killed Tool Calling - Transcript, Chat, and Summary with AI"
platform: "Recapio (AI-powered YouTube summarization service)"
source_video_url: https://www.youtube.com/watch?v=8dVCSPXG6Mw
source_video_channel: "Prompt Engineering"
source_video_upload_date: 2026-02-18
source_video_duration: "13 minutes 40 seconds"
content_type: "AI-generated digest of YouTube video"
---

# Anthropic Just Killed Tool Calling

**Platform:** Recapio (recapio.com) - AI-generated digest of YouTube video
**Source Video:** "Anthropic Just Killed Tool Calling" by channel "Prompt Engineering"
**YouTube Video ID:** 8dVCSPXG6Mw
**YouTube URL:** https://www.youtube.com/watch?v=8dVCSPXG6Mw
**Upload Date:** February 18, 2026
**Duration:** 13 minutes 40 seconds
**Recapio Page:** https://recapio.com/digest/anthropic-just-killed-tool-calling-by-prompt-engineering
**Archived:** 2026-02-20

---

## Note on Content Type

This Recapio page is an **AI-generated summary/digest** of a YouTube video, not a verbatim transcript. Recapio is a service that uses AI to summarize YouTube content. The summaries returned are abstracts, not the full original text.

The content below represents the digest summary as extracted from the Recapio page. For the full verbatim article text covering the same topic, see:

* `ai505--anthropic-killed-traditional-tool-calling.md` - Full text article from ai505.com (Feb 18, 2026)
* `aatventure--anthropic-killed-tool-calling.md` - aatventure.news article on same subject

---

## Recapio Digest Summary

### Main Innovation

Anthropic has released programmatic tool calling out of beta, which allows AI agents to "write code to invoke tools within a sandbox, defining the order of invocation" rather than using traditional JSON-based tool calling formats.

### Core Problem Solved

The approach addresses the "context window problem," where tool definitions and outputs "pollute the context window with unnecessary information." By executing code in a sandbox environment, only filtered summaries are passed back, reducing token usage.

### Why This Matters

LLMs are "primarily trained on code," making programmatic invocation more natural than JSON formats they were never specifically designed for. Industry adoption is expected, given Anthropic's track record with technologies like Model Context Protocol.

### Real-World Impact

Cloudflare's research showed "savings of 30% to 80% on tokens" using this approach. However, token reduction is not guaranteed - it depends on how much code the model writes for filtering.

### Dynamic Filtering Example

Anthropic's new web search tool demonstrates this by having Claude "write and execute code to post-process search results, injecting only the relevant information into the context window."

### Caveat on Token Costs

Token savings are not guaranteed. The actual savings depend on "the amount of code the model needs to write to filter the context," meaning some implementations may see increased overhead despite improved output efficiency.

### Practical Advice

Users of Anthropic's search API see automatic benefits with no required changes, while developers should explore available documentation for implementation details.

---

## Source Article: Full Verbatim Text (ai505.com, same topic)

The following is the complete verbatim text of the companion article by ai505.com (February 18, 2026), covering the same material as the YouTube video. Retrieved via jina.ai reader.

**Source:** https://ai505.com/anthropic-just-killed-traditional-tool-calling-here-s-what-replaces-it/

---

The Sonnet 4.6 release dropped Yesterday, and everyone's talking about the benchmark scores. Fair enough – they're impressive. But buried inside the same release notes is something that I think matters _more_ for the long-term trajectory of AI agents, and almost nobody is covering it.

Anthropic just moved its programmatic tool calling out of beta. And with it, they shipped dynamic web search filtering that cut input tokens by 24% while boosting BrowserComp accuracy from 33% to 46%. That's not a minor update. That's the kind of improvement you'd normally expect from a full model version jump.

Here's what's actually happening – and why I think this becomes the new industry standard within 18 months.

### The Context Window Problem Nobody Wants to Talk About

Every agentic AI company is quietly wrestling with the same crisis. The more capable your agent gets, the more it pollutes its own context window.

Picture what happens when you connect an MCP server to Claude. The moment that connection is established, every single tool definition gets loaded into the model's context. We're talking about tool names, descriptions, input schemas, output schemas – all of it, upfront, before the user has typed a single character. Then the user sends a query.

The agent makes a tool call. The result comes back and gets appended to the context. Then another tool call. Another result. System prompt, user memory, conversation history – it all piles up.

By the time a complex agentic task is halfway done, the majority of that context window is occupied by scaffolding – not actual useful information. It's like trying to think clearly while someone reads you the instruction manual for every appliance in your house, simultaneously.

This problem got dramatically worse with MCP adoption. As we covered in our Claude Sonnet 4.6 article, the model context protocol has become the connective tissue of the agentic ecosystem. But every MCP server you connect multiplies the context bloat. The more powerful your toolset, the more your agent chokes on its own overhead.

Context engineering – the discipline of deciding _what_ information actually belongs in the context window – became a hot topic in 2025 precisely because this problem was getting out of hand. Programmatic tool calling is Anthropic's most direct answer to it yet.

### What Programmatic Tool Calling Actually Does

Here's the core insight: LLMs are trained on billions of lines of code. They are _not_ trained on JSON tool-calling schemas. Writing code is natural to them. Parsing synthetic JSON function signatures is not.

Traditional tool calling works like this: the model sees a JSON definition of a tool, decides to call it, emits a structured JSON response, the runtime executes the tool, and the result gets injected back into the context. Every single intermediate step – every tool call, every result, every error – becomes part of the context the model has to carry forward.

Programmatic tool calling flips the model. Instead of emitting a JSON tool call, Claude writes actual code to invoke the tool inside a sandboxed execution environment. The agent can define the _sequence_ of tool invocations in that code – it can chain calls, filter results, handle errors, transform outputs – all within the sandbox. The only thing that comes back to the model's context is the final result.

Think of it like the difference between a chef who shouts every ingredient request to a runner (who shouts back the result, every time, in the middle of the kitchen) versus a chef who writes a prep list, hands it to the kitchen team, and gets back a finished mise en place. The intermediate chaos stays in the kitchen. The chef sees only what matters.

The token savings are not theoretical. Anthropic's own testing showed a 37% token reduction in their November 2025 advanced tool use release. Cloudflare, which independently arrived at the same idea and published their "Code Mode" report in September 2025, showed 32% savings for simple tasks and 81% for complex batch operations. For extreme cases – like Anthropic's example of reducing a 150,000-token MCP interaction to 2,000 tokens – the savings are closer to 99%.

### The Timeline: This Wasn't Just Anthropic's Idea

I want to be precise about the history here, because the narrative that "Anthropic invented this" isn't quite right – and understanding the convergence is actually more interesting.

**September 2025**: Cloudflare publishes their "Code Mode" report, framing it as "the better way to use MCP." They demonstrate that programmatically invoking tools through sandboxed code – rather than through sequential LLM tool calls – cuts token usage between 30% and 81% depending on task complexity. They're running this on Cloudflare Workers.

**November 2025**: Anthropic publishes "Code Execution with MCP: Building More Efficient Agents," arriving at nearly identical conclusions. Their headline number: token usage dropped from 150,000 to 2,000 in their test case. They also release the advanced tool use platform in beta, which includes programmatic tool calling plus the Tool Search Tool (which lets Claude search a library of tools without loading all definitions upfront – an 85% token reduction on its own).

**Late 2025 – Early 2026**: The open-source community runs with it. Blocks Goose Agent adds "code mode" MCP support. Multiple GitHub repos implement the pattern. LiteLLM adds native support across providers.

**February 17, 2026**: Anthropic moves programmatic tool calling to general availability with Sonnet 4.6. It's no longer experimental. It's the default path forward.

The pattern here mirrors what happened with MCP itself. As we noted in our Claude Opus 4.6 analysis, Anthropic has a track record of shipping something that looks like an internal engineering decision and watching it become an industry standard. MCP is now everywhere. Agent skills are now everywhere. The chat completion API format from OpenAI is the other major example of this dynamic – one company's API design becoming the lingua franca for an entire ecosystem.

Programmatic tool calling is next.

### Dynamic Web Search Filtering: The Immediate Win

The most tangible application of this in the Sonnet 4.6 release is dynamic web search filtering, and the benchmark numbers here deserve a closer look.

Previously, when Claude used web search, it would dump everything into the context window. Full page content, navigation menus, ads, boilerplate – all of it. The model would then have to reason through the noise to find the relevant signal. This is expensive and inaccurate.

With dynamic filtering, Claude now writes and executes code _before_ injecting search results into the context. The code post-processes the raw search output, filters for relevance, and only passes the useful content forward. The filtering step happens in the sandbox. The context window sees only the curated result.

The benchmark results on two specific evaluations:

**BrowserComp** tests whether an agent can navigate multiple websites to find deliberately hard-to-find information. With dynamic filtering:

* Claude Sonnet 4.6: 33.3% → 46.6% (a 13-point jump)
* Claude Opus 4.6: 45% → 61% (a 16-point jump)

**DeepSearchQA** tests whether an agent can find _all_ correct answers to a multi-answer question via web search. With dynamic filtering:

* Sonnet 4.6 F1 score: 52.6% → 59.4%
* Opus 4.6: also improved by approximately 8%

Average improvement across both benchmarks: 11%. Average input token reduction: 24%.

To put that 11% accuracy improvement in context – that's the kind of gain you'd typically associate with a major model upgrade, not a change to how search results are processed. The model didn't get smarter. The _information diet_ got cleaner.

One important caveat Anthropic is honest about: token costs don't always go down. For Opus 4.6, the price-weighted token count actually _increased_ despite fewer input tokens, because Opus was writing significantly more code to do the filtering. More code generation = more output tokens = higher cost per token. The net efficiency depends on how complex the filtering task is and which model you're using. For Sonnet, the math works cleanly in your favor. For Opus, it's more nuanced.

### What This Means If You're Building Agents

If you're using Anthropic's search API with data fetching enabled, you don't need to change anything. Dynamic filtering is now on by default. You get the accuracy improvements and token savings automatically.

For programmatic tool calling more broadly, the API structure looks similar to traditional tool definitions – you still provide a tool name, description, and input/output schema. The difference is that Claude now has the option to write code to invoke the tool rather than emitting a JSON function call. Here's the basic structure:

```python
tools = [
    {
        "name": "search_database",
        "description": "Query the product database for items matching criteria",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "filters": {"type": "object"}
            },
            "required": ["query"]
        }
    }
]
response = client.messages.create(
    model="claude-sonnet-4-6",
    tools=tools,
    messages=[{"role": "user", "content": "Find all products under $50 in the electronics category"}]
)
```

The practical implications for agent builders:

* **Multi-step workflows**: Instead of 10 sequential tool calls (each adding to context), Claude can write a script that executes all 10 in the sandbox and returns one consolidated result.
* **Data transformation**: Filtering, aggregating, and reshaping tool outputs happens in code before the context sees it.
* **Error handling**: Retry logic and fallback behavior can be encoded in the generated script, not in the context.
* **Cost predictability**: For Sonnet-class models, you get more predictable token costs because intermediate steps don't accumulate.

This is also why the Tool Search Tool matters alongside programmatic tool calling. If you have 200 MCP tools connected, loading all 200 definitions into context is brutal.

Tool Search lets Claude query a tool library and retrieve only the definitions it actually needs – an 85% reduction in tool-definition tokens according to Anthropic's internal MCP evaluations. Combine that with programmatic execution, and you've addressed both the "loading" problem and the "execution" problem simultaneously.

### The Broader Shift: Why Code Is the Right Abstraction

There's a deeper reason this works that goes beyond token counting.

LLMs are trained on code. Enormous amounts of it. When you ask a model to write a Python function that calls an API, filters the results, and returns a summary, you're asking it to do something it has seen millions of examples of. The cognitive load is low. The accuracy is high.

When you ask a model to emit a precisely formatted JSON object that conforms to a specific schema, with the right field names and types, in the right nesting structure – you're asking it to do something it was never explicitly trained for.

JSON tool calling is a synthetic format that emerged from engineering necessity, not from how models naturally operate. Every JSON tool call is a small act of translation from the model's native language (code and prose) into a format the runtime can parse.

Programmatic tool calling removes that translation layer. The model writes code. The sandbox runs code. The result comes back. It's a much more natural loop.

This is the same insight that made GPT-5.3-Codex-Spark compelling when it launched – the idea that coding agents should lean into code generation as the primary interface for tool orchestration, not fight against it with structured output formats.

Gemini has had code execution as part of its offering since Gemini 2.0. OpenAI's GPT-5.2 now supports 20+ tools behind its API with similar sandboxed execution patterns. The convergence is real. The question isn't whether programmatic tool calling becomes standard – it's how fast.

### The Bottom Line

Anthropic didn't just ship a feature. They graduated a philosophy.

The idea that agents should write code to orchestrate tools – rather than emitting JSON schemas and watching the context window fill up with intermediate results – is now production-ready, generally available, and backed by benchmark data that's hard to argue with. A 13-point accuracy improvement on BrowserComp. A 24% reduction in input tokens. A 37% token reduction in multi-tool workflows. These aren't marginal gains.

The pattern Anthropic has established – ship something that looks like an internal engineering decision, watch the open-source community adopt it, then graduate it to GA – has worked with MCP, with agent skills, and now with programmatic tool calling. I'd be surprised if every major coding agent doesn't have some version of this within the next 12 months.

If you're building agents today, the immediate action is simple: make sure you're on the Sonnet 4.6 API with data fetching enabled for web search. You get the dynamic filtering improvements for free. For more complex multi-tool workflows, start experimenting with the programmatic tool calling pattern – the token savings compound quickly as task complexity grows.

The context window is still finite. But now, at least, you have a much better way to decide what goes in it.

---

## FAQ (from ai505.com article)

### What is programmatic tool calling in Claude Sonnet 4.6?

Programmatic tool calling lets Claude write and execute code to invoke tools inside a sandboxed environment, rather than making sequential JSON function calls. Only the final result is returned to the model's context window, significantly reducing token usage and improving accuracy on complex multi-step tasks.

### How much can programmatic tool calling reduce token costs?

Results vary by task complexity and model. Anthropic's testing showed a 37% token reduction in multi-tool workflows. Cloudflare's independent testing showed 32% savings for simple tasks and 81% for complex batch operations. In extreme cases, token usage dropped from 150,000 to 2,000 tokens. Note that for Opus-class models, the cost of generating the filtering code can offset some savings.

### Do I need to change my code to use dynamic web search filtering?

No. If you're using Anthropic's search API with data fetching enabled, dynamic filtering is now on by default with Sonnet 4.6. You automatically get the 24% input token reduction and the accuracy improvements (BrowserComp: 33% → 46.6%) without any code changes.

### Is programmatic tool calling unique to Anthropic?

No. Cloudflare published their "Code Mode" approach in September 2025, arriving at the same idea independently. Gemini has offered code execution since Gemini 2.0, and OpenAI's GPT-5.2 supports sandboxed tool execution across 20+ tools. The convergence across frontier labs suggests this is becoming the standard architecture for agentic tool use.

### What is the Tool Search Tool and how does it relate?

The Tool Search Tool lets Claude query a library of available tools and retrieve only the definitions it needs, rather than loading all tool definitions into context upfront. Anthropic's internal testing showed an 85% reduction in tool-definition tokens. Combined with programmatic tool calling (which reduces execution-time context bloat), the two features address the full lifecycle of context pollution in MCP-connected agents.

---

## Key Claims Summary Table

| Claim | Evidence / Source |
|---|---|
| 37% token reduction in multi-tool workflows | Anthropic internal testing (November 2025 beta) |
| 32-81% token savings depending on task complexity | Cloudflare Code Mode research (September 2025) |
| Extreme case: 150,000 tokens reduced to 2,000 | Anthropic's MCP test case |
| BrowserComp accuracy: 33.3% → 46.6% (Sonnet 4.6) | Sonnet 4.6 benchmark results |
| BrowserComp accuracy: 45% → 61% (Opus 4.6) | Opus 4.6 benchmark results |
| DeepSearchQA F1 score: 52.6% → 59.4% (Sonnet 4.6) | Sonnet 4.6 benchmark results |
| 24% average input token reduction | Dual benchmark average |
| Tool Search Tool reduces tool-definition tokens by 85% | Anthropic internal MCP evaluations |
| GA release date for programmatic tool calling | February 17, 2026 (Sonnet 4.6 release) |
| Cloudflare published "Code Mode" independently | September 2025 |
| Anthropic beta release | November 2025 |

---

*Archived 2026-02-20. Source: Recapio digest at https://recapio.com/digest/anthropic-just-killed-tool-calling-by-prompt-engineering (AI summary of YouTube video "Anthropic Just Killed Tool Calling" by "Prompt Engineering" channel, Feb 18 2026). Full article content sourced from companion ai505.com article covering the same material.*
