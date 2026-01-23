# Anthropic Admits That MCP Sucks — Video Transcript

## Metadata

| Field | Value |
|-------|-------|
| **Source URL** | https://www.youtube.com/watch?v=1piFEKA9XL0 |
| **Channel** | Theo - t3.gg (https://www.youtube.com/@t3dotgg) |
| **Title** | Anthropic admits they were wrong about MCP |
| **Published** | November 2025 |
| **Archived** | 2026-01-23 |
| **Referenced Blog** | https://www.anthropic.com/engineering/code-execution-with-mcp |
| **Transcript Type** | Auto-generated / Manual cleanup |

---

## Key Quotes

> "Models do not get smarter when you give them more tools. They get smarter when you give a small subset of really good tools."

> "This reduced the token usage from 150,000 tokens to 2,000 tokens. A time and cost savings of 98.7%."

> "How the fuck can you pretend that MCP is the right standard when doing a shitty codegen solution instead saves you 99% of the wasted [stuff]?"

> "The creators of MCP are sitting here and telling us that writing [TypeScript] code is 99% more effective than using their spec as they wrote it."

> "Whenever somebody tells you AI is going to replace developers, just... this is all the proof I need that we are good."

---

## Full Transcript

Oh boy, it's time for another MCP video. If you're not familiar with my takes on MCP, it's my favorite example of AI being a bubble. I know way more companies building observability tools for MCP stuff than I know companies actually making useful stuff with MCP. When you see everyone building the tool layer for a new thing and nobody building the product around the new thing, you know that new thing is probably crap. I still remember back in the day when web 3 was blowing up that I knew about six companies doing OOTH for web 3 and one single company that could potentially benefit from that existing. Yet here we are with MCP and thankfully people are waking up to the fact that it kind of sucks. Not that the spec sucks, which it does, or that the implementations suck, which they do, but the models suck at using it too.

I covered this before with code mode from Cloudflare, which was them realizing that MCP is bad and solving it by letting agents write code to call these things instead of just bundling it all in as a giant pile of context that makes everything run like shit. And it seems like our friends over at Anthropic, you know, the people who made this spec and curse us all with it, are waking up to the same thing because they just wrote a new article, code execution with MCP, building more efficient agents.

And depending on how you choose to read this article, you can see it as them admitting that MCP is not a good protocol because MCP requires you to add a bunch of shit context that makes the models dumber and worse. **Models do not get smarter when you give them more tools. They get smarter when you give them a small subset of really good tools.** An MCP does not encourage that way of thinking. MCP encourages you to add 500 plus tools to a model and then nothing fucking works anymore.

[Sponsor segment omitted]

I'm actually really excited to go into this because I secretly deep down do want something like MCP to work, but the current implementations just don't. I've yet to have one impress me with its capabilities. There are some that are really cool, but none that are actually useful for my experience. Let's see if they succeeded in making them useful here.

Code execution with MCP. Building more efficient agents. Direct tool calls consume context for each definition and result. agents scale better by writing code to call tools instead. Here's how it works with MCP. There we go. There it is. Thank you, Anthropic, for admitting I was right the whole shit time.

It makes no sense to just clog up your system prompt with a bunch of shit that probably isn't relevant for the majority of work you're doing. There just isn't enough data for the models to be trained to do that well. Do you know what they do well? Because there's a lot of examples. Write code. It's so funny to see this line in an official thing on the Anthropic blog. They're admitting that their spec doesn't work for the thing they build, which is AI models. Hilarious.

Let's see how they actually implemented this because I am curious.

## On MCP's Missing Features

The model context protocol is an open standard for connecting AI agents to external systems and making them dumber in the process. Connecting agents to tools and data traditionally requires a custom integration for each pairing, creating fragmentation and duplicated effort that makes it difficult to scale truly connected systems.

You know, if you were trying to solve this problem to make a generic solution for models connecting to things, you'd probably want to make sure it handles the things that you need with those connection layers. You know, like OAuth. **Did you know MCP has no concept of OAuth at all? At all.** Now, there's like 18 implementations of it because there's no way to do proper handshakes with MCP. Your best bets to go and hardcode a custom URL that has a signed like parameter in it that allows it to work. Actually, insane. I hate the standard. I really do.

Ah, MCP provides a universal protocol that does a third of what you need. Developers implement MCP once in their agent and then five additional layers to make it work.

## On Tool Definition Bloat

Today, developers routinely build agents with access to hundreds or thousands of tools across dozens of MCP servers. However, as the number of connected tools grows, loading all tool definitions up front and passing intermediate results through the context window slows down agents and increases costs. It also makes them way dumber. Weird how you missed that one.

In this blog, we'll explore how code execution can enable agents to interact with MCP servers more efficiently, handling more tools while using fewer tokens. Excessive token consumption from tools make agents less efficient and less effective. As MCP usage scales, there are two common patterns that can increase agent cost and latency. The first is tool definition overloading the context window and the second is intermediate tool results consuming additional tokens.

## On Context Window Consumption

Every additional tool call is carrying all of the previous context. So every time a tool is being called the entire history is being re hit as input tokens. Insane. It's so much bloat. It uses so much context. It burns through so many tokens and so much money. And if you don't have caching set up properly for your inputs, you're just burning cash. It sucks. It's such a bad implementation. We need parallel tool calls. We need better tool design to prevent this. Or you can write code because if this was just writing code to go find the documents and then for each of them go do this thing and then return all of the results with a single tool call, that's a lot less shit.

In Anthropic's own words, every intermediate result must pass through the model. In this example, the full call transcript flows through twice. For a 2-hour sales meeting, that could mean processing an additional 50,000 tokens. Even larger documents may exceed context window limits, which would break the flow entirely.

## On Token Savings

The agent discovers tools by exploring the file system, listing the /servers directory to find all available servers like Google Drive and Salesforce, then reading the specific tool files that it needs like get document.ts and update record.ts to understand each tool's interface. This lets the agent load only the definitions it needs for the current task.

**This reduced the token usage from 150,000 tokens to 2,000 tokens. A time and cost savings of 98.7%.**

How the fuck can you pretend that MCP is the right standard when doing a shitty codegen solution instead saves you 99% of the wasted shit? That is so funny to me. The creators of MCP are sitting here and telling us that writing shit TypeScript code is 99% more effective than using their spec as they wrote it. This is so amusing to me.

## On Code vs Protocol

So what are the benefits of code execution with MCP? Code execution with MCP enables agents to use context more efficiently by loading tools on demand, filtering data before it reaches the model and executing complex logic in single steps.

For example, you don't have to dump the entire document into the LLM and then send it over to our friends at Anthropic or Google or AWS, whoever is hosting your model because all of that's just happening inside of the sandbox that the code is executing in. That's so much better than loading the entire document.

Now the content of this document never becomes part of the context. It's never seen by the model because it's not touching any of that because the model doesn't need to know what's in the doc. It needs to know what to do with it. That's the whole fucking point.

## On Progressive Discovery

There are other benefits too like progressive disclosure. Models are great at navigating file systems. Presenting tools as code on a file system allows for models to read tool definitions on demand rather than reading them all up front because crazy MCP had no concept of progressive discovery. There was no way to give more context via MCP when it was necessary.

I saw people doing crazy shit like having a separate model that would pick which different agent to use and different subsets of tools depending on what task was being completed for those sub agents. Entire orchestration layers of shit in order to try and make the spec usable. Turns out writing code is easier. Crazy.

## Critique of Tool Bloat in Existing Products (Trey)

I'm going to pick on my friends at Trey really quick here. When I was playing with it and I noticed the quality of outputs not being great, I decided to analyze what tools their agents have access to. There are 23 tools available for the solo coding environment agent. This includes seven separate tools for doing file management stuff, three for running commands, and my personal favorite, three for Superbase. I don't use Superbase. I don't even have an account. I've never built anything with Superbase, but when I use Trey, every single request I send has this context included for things I don't even use. Ah, this is awful.

How is this where we ended up and we assumed everything was okay? This is when I complain about AI bros not building software or understanding how the software world works. This is what I'm talking about. All of these things are obviously wrong and dumb. You just have to look at it to realize.

## On Privacy Benefits

When agents use code execution with MCP, intermediate results stay in the execution environment by default. This way, the agent only sees what you explicitly log or return. Meaning data you don't wish to share with the model can flow through your workflows without ever entering the model's context.

When you think about it, if you're using a tool like in Trey here, the get tables tool, that one's not giving you PII because it's data about what tables exist in their definitions. But if there was a get rows tool here that you just gave the model access to all of the data in your database and anything in there could hypothetically be included in context and therefore sent to Anthropic or OpenAI or whoever else you're hosting from. This is the easiest way to not have to do that.

## On Skills and the Ironic Loop

Agents can also persist their own code as reusable functions. Once an agent develops working code for a task, it can save the implementation for future use. This ties in closely to the concept of skills, folders of reusable instructions, scripts, and resources for models to improve performance on specialized tasks.

Is this not reinventing MCP again? Let me get this straight. So let's say we have this API. We could tell the model about this API, but then we have to do that for every single thing. So we want to standardize this. We need a standard. So we create an MCP tool that includes all of the definitions and all of the other things that are needed to call this endpoint. But then we realize, oh no, we have too many tools. So we do the very obvious thing of changing this into an SDK interface. And then now that we've done this, this code is useful. We should save it. And now we have this skill. And then these should be documented.

**And then we end up roughly where we started. And I'm sure this loop won't continue indefinitely as we reinvent the same 15 things over and over and over again in the AI world. That's definitely not going to happen. This is the real agentic loop everybody's talking about.**

## Conclusion

Note that code execution introduces own complexity. Running agent generated code requires a secure environment for execution with appropriate sandboxing, resource limits, and monitoring.

The benefits of code execution are reduced token cost, lower latency, and improved tool composition. Should be weighed against those implementation costs. No, this is bullshit bullshit. This is absolute bullshit bullshit. Every implementation of MCP I've seen that can do anything is way more insecure than a basic fucking sandbox with some environment variables. This is delusion.

MCP provides a foundational protocol for agents to connect to many tools and systems. However, once too many servers are connected, tool definitions and results can consume excessive tokens, reducing agent efficiency. Although many of these problems here feel novel, context management, tool composition, and state persistence, they have known solutions from software engineering. Code execution applies these established patterns to agents, letting them use familiar programming constructs to interact with MCP servers more efficiently.

**We need more engineers in high places. This is what happens when we let these LLM people make the things that we have to use as devs. Devs should be defining what devs use. And if you don't let them do that, then you'll end up realizing they were right all along.**

Whenever somebody tells you AI is going to replace developers, just like them this is all the proof I need that we are good. This is what happens when you let LLMs and more importantly you let LLM people design our APIs we get something so useless that we reinvent the whole wheel multiple times in the process.

And I'm going to continue to not really use MCP. I hope this helps you understand why. Let me know what you guys think. Let me know how you're executing your MCP tools. And until next time, peace nerds.

---

## Summary of Key Arguments

1. **MCP encourages tool bloat** — adding 500+ tools to context makes models dumber, not smarter
2. **Token waste is massive** — 150K tokens reduced to 2K (98.7% savings) by switching to code execution
3. **MCP lacks essential features** — no OAuth, no progressive discovery, no parallel tool calls
4. **Code is deterministic** — less hallucination than context-heavy tool calling
5. **Privacy benefits** — data can flow through workflows without entering model context
6. **The ironic loop** — MCP → code execution → skills → documentation → back to where we started
7. **Software engineering principles apply** — existing patterns (code, SDKs, APIs) work better than new protocols
