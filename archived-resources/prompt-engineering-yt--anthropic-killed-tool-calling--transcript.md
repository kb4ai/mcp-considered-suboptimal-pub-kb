---
source_url: https://www.youtube.com/watch?v=8dVCSPXG6Mw
channel: "Prompt Engineering"
channel_url: "https://www.youtube.com/@engineerprompt"
title: "Anthropic Just Killed Tool Calling"
upload_date: 2026-02-18
duration: 820
view_count: 42382
access_date: 2026-02-20
transcript_source: auto-generated (speech recognition)
may_contain_errors: true
content_type: YouTube video transcript
---

# Anthropic Just Killed Tool Calling — Transcript

**Channel:** [Prompt Engineering](https://www.youtube.com/@engineerprompt)
**YouTube:** https://www.youtube.com/watch?v=8dVCSPXG6Mw
**Upload Date:** February 18, 2026
**Duration:** ~13 minutes 40 seconds
**Views at archive time:** 42,382

---

## Transcript (auto-generated, lightly formatted)

Okay, so with Sonnet 4.6 release, Anthropic also introduced a few very interesting and important developer tools that nobody is talking about. These are not only going to save you money, but they will also improve the performance of your agent. Now, in particular, I'm talking about programmatic tool calling. This feature has been available for a while. The idea is that instead of your agent trying to load everything into the context window, you can make specific calls to a specific tool just by writing code. And this way you will not only save on the tokens that the agent is going to be using, but you're also improving on the accuracy of the calling.

Now Anthropic has been doing some really really interesting engineering work and they have been one of the companies that is actually openly discussing their innovations which is really really cool to see.

Now the question is why this works better than JSON structure that you provide to your agent for tool calling. Well these agents, these LLMs, are specifically trained with code. They are not trained for tool calling and writing code is pretty natural to them.

Now the question is why even pay attention to this? Well, I think Anthropic has a track record of when they release certain tools or technologies the rest of the industry actually tends to adopt them. This happened with the introduction of MCPs or Model Context Protocol. Now every company is building MCPs. We saw a very similar trend with agent skills. Pretty much every coding agent out there is introducing agent skills or supporting them. Now the only other time that we have seen wide adoption of something coming out of a frontier lab was probably the chat completion API from OpenAI.

### The Context Window Problem

Okay. So let's put things in the context and why exactly do we need programmatic tool calling. So for that we need to look at this context window problem that every agentic company is trying to solve. And this has been made worse with the introduction of protocols like MCP.

Now here's what usually happens. Let's say if you have an MCP connected it's going to have different tools. All of those tool definitions are loaded into the context of your large language model. Now during interaction with the user, it's going to make tool calls. The input outputs of every tool call and then subsequent tool calls are also put into the context window. You also have the system prompt plus user memory and the actual user messages and responses. And as a result you can see that most of the context window is going to be polluted or used by unnecessary things that you should be able to avoid.

Now last year we started seeing this concept of context engineering appearing everywhere and the idea is that you want to provide just useful information in the context window and discard everything else.

### How Traditional vs Programmatic Tool Calling Works

Now here's what usually happens. When the user query comes in a coding agent like Claude Code is going to make a tool call. The results are passed on to the context, that is going to make another tool call and this process repeats. Every time you invoke a tool, the results are passed on to Claude Code and put it in the context window.

Now the idea of programmatic tool calling is a little different. In this case, instead of directly calling the tool, Claude or your coding agent is going to write code to invoke certain tools in a sandbox environment. The coding agent can define the order of how those tools are going to be invoked in this sandbox environment. Now in this case we will provide the code written to the sandbox along with the actual input and the only output is going to be the final summary or final answer. So anything that happens in between stays within the sandbox environment and as a result the coding agent is going to be only seeing the final results. Hence, you're going to be using a lot less tokens compared to if you are doing traditional tool calling.

### Timeline of Development

Now, one thing is very important that this is not just one company's idea. Other companies have been exploring the same idea. Let me walk you through a timeline.

* **September 2025:** Cloudflare published a report called "Code Mode, the Better Way to Use MCP." And they also came up with this idea of programmatically invoking different tools rather than going the traditional tool calling within an MCP server. And they showed that you can save from 30% all the way up to 80% on tokens if you adopt this sandboxed approach.

* **November 2025:** Anthropic published this article called "Code Execution with MCP: Building More Efficient Agents" and they pretty much came to the exact same conclusions as Cloudflare. Then later in the month Anthropic released the full advanced tool use. So this included tools like Tool Search Tool which is another way of looking for specific tools within an MCP server which saves you on tokens that are going to be used by the agent. And with that they also had this concept of programmatic tool calling. Now their results at that point showed about 37% token reduction and improved accuracy on several benchmarks.

* **Late 2025 - Early 2026:** And just like anything released by Anthropic the usage kind of exploded within the open source community. So you had implementation from Block's Goose Agent which added code mode MCP support. Then there were other GitHub repos that implemented the programmatic tool call. A good example of this is LiteLLM which basically added native support across different providers.

* **February 17, 2026:** This brings us to today. Anthropic moved this from beta so it's now fully supported and they also added dynamic filtering for web search.

### Dynamic Web Search Filtering — Benchmarks

Both of these concepts together can really save you not only on token cost but also can improve the performance. Code execution has been part of Gemini offering since Gemini 2.0 and now even OpenAI GPT since 5.2 has added support for 20 plus different tools behind their API.

Now the key insight is that LLMs are trained on billions of lines of code especially with coding agents. You can see that they can produce and understand code but barely any synthetic JSON tool calling formats. So you want to let the agent do what they are good at and that is writing code.

With Sonnet 4.6 release, Anthropic also introduced two different set of tools — one is web search and the second is dynamic filtering capabilities. Both of these are powered by programmatic tool calling. These tools were previously available but now Anthropic is introducing improved versions of these. And with this they say Claude can now natively write and execute code during web searches to filter search results before they reach the context windows, improving the accuracy and token efficiency.

So like maniacs these models used to just dump everything into the context window whenever they used to do web search. So this will pollute the context window with irrelevant information. Now they say that after doing the initial search, Claude writes and executes code to do post-processing on the query results and using the programmatic tool calling by doing dynamic filtering they are going to post-process the results and only put the relevant results in the context window. So this is a step that happens before injecting information into the context window.

So they were specifically looking at two different benchmarks — one is BrowserComp and the other one is DeepSearchQA — and they saw an average of **11% improvement** while average of **24% fewer input tokens**. This is significant. This kind of improvements are usually expected if you have a major model version upgrade.

* The BrowserComp benchmark tests whether an agent can navigate many websites to find a specific piece of information that is deliberately hard to find. With this new dynamic filtering they saw that Sonnet went from **33% to 46%**. We're talking about almost 13% improvement, whereas Opus went from **45% to 61%**. And again, this is dramatic improvement on this one specific benchmark.

* The second benchmark DeepSearchQA basically tests the capability of the model to find all the correct answers via web search. So a question has more than one correct answer and it's supposed to find those. Now in this case again we see an **F1 score improvement from 52 to 59%** for Sonnet 4.6 and Opus also saw almost 8% improvement.

### Important Caveat on Token Costs

Now here's the most important thing. They say token cost will vary depending on how much code the model needs to write to filter context. So the price weighted token decreased for Sonnet 4.6 on both the benchmarks but **increased for Opus 4.6**. So that means Opus was writing a lot more code; although the number of tokens in the final output were reduced, but since Opus was writing a lot more code to filter those results, the price weighted token actually increased for Opus. So this is important to keep in mind. You're not always going to see reduction in token price, but that is an expectation.

### How to Use It

If you're using the search API, you don't have to do anything whatsoever. You just provide or use the exact same search API with data fetching enabled. And Anthropic is now going to automatically use this capability to reduce the number of tokens that are going to be returned with only the most relevant information.

Now there are also a number of other tools that went out of beta and are now generally available. So one is code execution sandboxes. Memory is another one. Programmatic tool calling. Then tool search and tool examples.

They also released detailed documentation on how to use this with some really quick examples. So for example, you will just provide a list of tools. The structure remains very similar to normal tool definition. You provide what the tool does along with the name. Then the input schema, what are the required parameters and what is going to be the output schema along with the definition of the tool, and then if Claude needs it, instead of doing function calling it's going to just write code to execute this specific tool for you.

Now I suspect this is probably going to become a standard in the industry just like MCP and agent skills.

---

## Key Quotes (for repository thesis)

> "All of those tool definitions are loaded into the context of your large language model... most of the context window is going to be polluted or used by unnecessary things"

> "LLMs are specifically trained with code. They are not trained for tool calling and writing code is pretty natural to them."

> "Like maniacs these models used to just dump everything into the context window whenever they used to do web search."

> "I think Anthropic has a track record of when they release certain tools or technologies the rest of the industry actually tends to adopt them."

> "This kind of improvements [11% accuracy, 24% fewer tokens] are usually expected if you have a major model version upgrade."

---

## Relevance to Repository Thesis

This video directly validates our core thesis points:

1. **Context pollution from MCP tools is a recognized industry problem** — the video describes exactly the mechanism we document: tool definitions + intermediate results consuming context window
2. **Code execution > JSON tool calling** — Anthropic's own engineering validates that LLMs writing code to invoke tools is superior to JSON schema-based tool calling
3. **98.7% token reduction** from Cloudflare's benchmarks (150K → 2K tokens) matches our documented figure
4. **Industry convergence on code-over-protocol** — Cloudflare, Anthropic, OpenAI, Google all moving to sandbox code execution for tool invocation
5. **The market validates our thesis** — even Anthropic (MCP's creator) is building infrastructure to route around MCP's context bloat problem

---

*Archived 2026-02-20. Auto-generated transcript from YouTube, lightly formatted with section headers for readability. May contain speech recognition errors.*
