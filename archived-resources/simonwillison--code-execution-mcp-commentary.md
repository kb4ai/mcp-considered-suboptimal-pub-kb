# Code execution with MCP: Building more efficient agents

## Archive Metadata

* **Author**: Simon Willison
* **Original URL**: https://simonwillison.net/2025/Nov/4/code-execution-with-mcp/
* **Published**: November 4, 2025 at 11:56 pm
* **Archived**: 2026-01-23T01:32:55+01:00
* **Archive Method**: jina.ai reader + WebFetch
* **Tags**: ai, prompt-engineering, generative-ai, llms, anthropic, model-context-protocol, coding-agents

## Article Content

**[Code execution with MCP: Building more efficient agents](https://www.anthropic.com/engineering/code-execution-with-mcp)** ([via](https://x.com/AnthropicAI/status/1985846791842250860))

When I [wrote about Claude Skills](https://simonwillison.net/2025/Oct/16/claude-skills/) I mentioned that I don't use MCP at all any more when working with coding agents - I find CLI utilities and libraries like Playwright Python to be a more effective way of achieving the same goals.

This new piece from Anthropic proposes a way to bring the two worlds more closely together.

It identifies two challenges with MCP as it exists today. The first has been widely discussed before: all of those tool descriptions take up a lot of valuable real estate in the agent context even before you start using them.

The second is more subtle but equally interesting: chaining multiple MCP tools together involves passing their responses through the context, absorbing more valuable tokens and introducing chances for the LLM to make additional mistakes.

What if you could turn MCP tools into code functions instead, and then let the LLM wire them together with executable code?

Anthropic's example here imagines a system that turns MCP tools into TypeScript files on disk, looking something like this:

```ts
// ./servers/google-drive/getDocument.ts
interface GetDocumentInput {
  documentId: string;
}
interface GetDocumentResponse {
  content: string;
}
/* Read a document from Google Drive */
export async function getDocument(input: GetDocumentInput): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>('google_drive__get_document', input);
}
```

This takes up no tokens at all - it's a file on disk. In a similar manner to Skills the agent can navigate the filesystem to discover these definitions on demand.

Then it can wire them together by generating code:

```ts
const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

Notably, the example here avoids round-tripping the response from the `gdrive.getDocument()` call through the model on the way to the `salesforce.updateRecord()` call - which is faster, more reliable, saves on context tokens, and avoids the model being exposed to any potentially sensitive data in that document.

This all looks very solid to me! I think it's a sensible way to take advantage of the strengths of coding agents and address some of the major drawbacks of MCP as it is usually implemented today.

There's one catch: Anthropic outline the proposal in some detail but provide no code to execute on it! Implementation is left as an exercise for the reader:

> If you implement this approach, we encourage you to share your findings with the [MCP community](https://modelcontextprotocol.io/community/communication).

## Key Insights and Quotes

### Simon Willison's Position on MCP

> "When I wrote about Claude Skills I mentioned that I don't use MCP at all any more when working with coding agents - I find CLI utilities and libraries like Playwright Python to be a more effective way of achieving the same goals."

This is a significant statement from a leading voice in the AI development community, indicating that MCP in its current form is not competitive with traditional programming approaches for coding agents.

### Two Major Challenges with MCP

**Challenge 1: Token Consumption**

> "All of those tool descriptions take up a lot of valuable real estate in the agent context even before you start using them."

This is a widely discussed issue - MCP tools consume context window space just by existing, before any actual work is done.

**Challenge 2: Inefficient Tool Chaining**

> "Chaining multiple MCP tools together involves passing their responses through the context, absorbing more valuable tokens and introducing chances for the LLM to make additional mistakes."

This more subtle issue highlights the inefficiency of round-tripping data through the LLM when connecting multiple tools together.

### The Proposed Solution: Code-Based MCP

The proposal suggests converting MCP tools into TypeScript function definitions stored on disk, which:

* Takes up zero tokens (files on disk vs. descriptions in context)
* Allows discovery on-demand (similar to Claude Skills)
* Enables direct data passing between tools without round-tripping through the LLM
* Results in: faster execution, token savings, reduced error opportunities, better data privacy

### Benefits of Direct Code Execution

> "Notably, the example here avoids round-tripping the response from the `gdrive.getDocument()` call through the model on the way to the `salesforce.updateRecord()` call - which is faster, more reliable, saves on context tokens, and avoids the model being exposed to any potentially sensitive data in that document."

This highlights multiple advantages:

* **Performance**: Faster execution
* **Reliability**: More reliable operations
* **Efficiency**: Saves context tokens
* **Privacy**: Sensitive data doesn't pass through the LLM

### Willison's Assessment

> "This all looks very solid to me! I think it's a sensible way to take advantage of the strengths of coding agents and address some of the major drawbacks of MCP as it is usually implemented today."

Despite his general preference for CLI utilities over MCP, Willison sees this proposal as a sensible evolution.

### The Critical Gap: No Implementation

> "There's one catch: Anthropic outline the proposal in some detail but provide no code to execute on it! Implementation is left as an exercise for the reader"

This is a significant limitation - Anthropic provides the conceptual framework but no working code, leaving implementation to the community.

## Related Articles

* [Claude Skills](https://simonwillison.net/2025/Oct/16/claude-skills/) - Simon Willison's earlier article on Claude Skills
* [Code execution with MCP: Building more efficient agents](https://www.anthropic.com/engineering/code-execution-with-mcp) - The original Anthropic blog post being discussed

## Archive Notes

This commentary is particularly valuable because it comes from Simon Willison, a well-respected voice in the AI and web development communities. His frank admission that he doesn't use MCP anymore in favor of traditional programming approaches (CLI utilities, Playwright Python) is significant context for evaluating MCP's current state and this proposal.

The article highlights both the promise and the problem with Anthropic's proposal: while the approach seems sound and addresses real issues, the lack of implementation code means it remains theoretical until the community builds it.
