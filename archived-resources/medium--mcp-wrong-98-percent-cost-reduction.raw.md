Title: We’ve Been Using MCP Wrong: How Anthropic Reduced AI Agent Costs by 98.7%

URL Source: https://medium.com/@meshuggah22/weve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589

Published Time: 2025-11-06T22:52:24Z

Markdown Content:
We’ve Been Using MCP Wrong: How Anthropic Reduced AI Agent Costs by 98.7% | by Pawel | Medium
===============

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 2](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

We’ve Been Using MCP Wrong: How Anthropic Reduced AI Agent Costs by 98.7%
=========================================================================

[![Image 3: Pawel](https://miro.medium.com/v2/resize:fill:64:64/1*axcXEgSlEMqpEtRExV2r2Q.jpeg)](https://medium.com/@meshuggah22?source=post_page---byline--7c102fc22589---------------------------------------)

[Pawel](https://medium.com/@meshuggah22?source=post_page---byline--7c102fc22589---------------------------------------)

Follow

5 min read

·

Nov 6, 2025

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F7c102fc22589&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589&user=Pawel&userId=47223e747bee&source=---header_actions--7c102fc22589---------------------clap_footer------------------)

325

8

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7c102fc22589&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589&source=---header_actions--7c102fc22589---------------------bookmark_footer------------------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D7c102fc22589&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589&source=---header_actions--7c102fc22589---------------------post_audio_button------------------)

Share

Anthropic’s recent paper explores the biggest issue with the MCP - their AI agents were processing 150,000 tokens just to load tool definitions before even reading a user’s request. The same functionality could use 2,000 tokens — **a 98.7% reduction**.

This is a critical, as AI agents scale from proof-of-concept to production, connecting them to dozens of MCP (Model Context Protocol) servers with hundreds of tools has become standard practice. But there’s a problem hiding in plain sight: **every tool definition loads into the context window upfront, and every intermediate result flows through the model.**

The engineering teams at Anthropic and Cloudflare independently discovered the same solution: stop making models call tools directly. Instead, have them write code.

### The Traditional MCP Trap

Model Context Protocol has revolutionized how AI agents connect to external systems. Since its launch in November 2024, the community has built thousands of MCP servers, enabling agents to access everything from databases to cloud services.

But the standard implementation has a fundamental inefficiency problem.

Here’s what happens when you ask an agent to “analyze this document, extract keywords, generate a summary, and save the results”:

**Step 1: Load all tool definitions**

{

 "read_file": {

 "description"…

Create an account to read the full story.
-----------------------------------------

The author made this story available to Medium members only.

If you’re new to Medium, create a new account to read this story on us.

[Continue in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3Dregwall&source=-----7c102fc22589---------------------post_regwall------------------)

Or, continue in mobile web

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589%3Fsource%3D-----7c102fc22589---------------------post_regwall------------------%26skipOnboarding%3D1%7Cregister&source=-----7c102fc22589---------------------post_regwall------------------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589%3Fsource%3D-----7c102fc22589---------------------post_regwall------------------%26skipOnboarding%3D1%7Cregister&source=-----7c102fc22589---------------------post_regwall------------------)

Sign up with email

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589&source=-----7c102fc22589---------------------post_regwall------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F7c102fc22589&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589&user=Pawel&userId=47223e747bee&source=---footer_actions--7c102fc22589---------------------clap_footer------------------)

325

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F7c102fc22589&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589&user=Pawel&userId=47223e747bee&source=---footer_actions--7c102fc22589---------------------clap_footer------------------)

325

8

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7c102fc22589&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589&source=---footer_actions--7c102fc22589---------------------bookmark_footer------------------)

[![Image 4: Pawel](https://miro.medium.com/v2/resize:fill:96:96/1*axcXEgSlEMqpEtRExV2r2Q.jpeg)](https://medium.com/@meshuggah22?source=post_page---post_author_info--7c102fc22589---------------------------------------)

[![Image 5: Pawel](https://miro.medium.com/v2/resize:fill:128:128/1*axcXEgSlEMqpEtRExV2r2Q.jpeg)](https://medium.com/@meshuggah22?source=post_page---post_author_info--7c102fc22589---------------------------------------)

Follow

[Written by Pawel ----------------](https://medium.com/@meshuggah22?source=post_page---post_author_info--7c102fc22589---------------------------------------)

[301 followers](https://medium.com/@meshuggah22/followers?source=post_page---post_author_info--7c102fc22589---------------------------------------)

·[3 following](https://medium.com/@meshuggah22/following?source=post_page---post_author_info--7c102fc22589---------------------------------------)

Gen AI director with a focus on AI & Data Strategy, FinOps, MLOps & LLM/LMMOps.

Follow

Responses (8)
-------------

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--7c102fc22589---------------------------------------)

![Image 6: Susan Apfel](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fweve-been-using-mcp-wrong-how-anthropic-reduced-ai-agent-costs-by-98-7-7c102fc22589&source=---post_responses--7c102fc22589---------------------respond_sidebar------------------)

Cancel

Respond

[![Image 7: Scot Campbell](https://miro.medium.com/v2/resize:fill:32:32/1*zu73XHbMh5g5nVEBESycUA.png)](https://medium.com/@prefrontalsys?source=post_page---post_responses--7c102fc22589----0-----------------------------------)

[Scot Campbell he/him](https://medium.com/@prefrontalsys?source=post_page---post_responses--7c102fc22589----0-----------------------------------)

[Nov 12, 2025](https://prefrontalsys.medium.com/wow-just-did-a-quick-and-dirty-test-in-python-on-a-paper-of-mine-currently-at-maximal-draft-725e5d05e9f3?source=post_page---post_responses--7c102fc22589----0-----------------------------------)

Wow...just did a quick and dirty test in python on a paper of mine (currently at maximal draft size, I have GOT to start editing), here's the analysis:

Token Count Analysis

Precise count for paper.md: 53,132 tokens

Breakdown:

- Characters: 245,147

…more

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F725e5d05e9f3&operation=register&redirect=https%3A%2F%2Fprefrontalsys.medium.com%2Fwow-just-did-a-quick-and-dirty-test-in-python-on-a-paper-of-mine-currently-at-maximal-draft-725e5d05e9f3&user=Scot+Campbell&userId=6f8e7b3e165a&source=---post_responses--725e5d05e9f3----0-----------------respond_sidebar------------------)

7

1 reply

Reply

[![Image 8: Megha Gupta](https://miro.medium.com/v2/resize:fill:32:32/0*L_2ypA3Dgf1iIZpJ)](https://medium.com/@meghagupta.biet?source=post_page---post_responses--7c102fc22589----1-----------------------------------)

[Megha Gupta](https://medium.com/@meghagupta.biet?source=post_page---post_responses--7c102fc22589----1-----------------------------------)

[Nov 16, 2025](https://medium.com/@meghagupta.biet/great-article-want-to-understand-how-can-i-test-from-my-side-e0b7e507e62e?source=post_page---post_responses--7c102fc22589----1-----------------------------------)

Great article, want to understand how can I test from my side? Do I need to enable something from my side. I am using both cursor and Claude.

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fe0b7e507e62e&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meghagupta.biet%2Fgreat-article-want-to-understand-how-can-i-test-from-my-side-e0b7e507e62e&user=Megha+Gupta&userId=9c7e70046ce2&source=---post_responses--e0b7e507e62e----1-----------------respond_sidebar------------------)

6

Reply

[![Image 9: Susan Apfel](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@susan.apfel?source=post_page---post_responses--7c102fc22589----2-----------------------------------)

[Susan Apfel](https://medium.com/@susan.apfel?source=post_page---post_responses--7c102fc22589----2-----------------------------------)

[Nov 8, 2025](https://medium.com/@susan.apfel/hello-i-am-a-little-confused-we-still-need-to-tell-llm-what-kind-of-api-functions-it-can-use-in-b25a37d3191c?source=post_page---post_responses--7c102fc22589----2-----------------------------------)

Hello I am a little confused, we still need to tell llm what kind of api functions it can use in the beginning, right? Kind of like telling llm all the tools information? If I understand correctly, we just ask llm to generate a work plan, then we…more

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fb25a37d3191c&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40susan.apfel%2Fhello-i-am-a-little-confused-we-still-need-to-tell-llm-what-kind-of-api-functions-it-can-use-in-b25a37d3191c&user=Susan+Apfel&userId=13dd82bb11f0&source=---post_responses--b25a37d3191c----2-----------------respond_sidebar------------------)

3

Reply

See all responses

More from Pawel
---------------

![Image 10: Google’s A2UI Protocol Just Changed How AI Agents Build User Interfaces — Here’s My First Project…](https://miro.medium.com/v2/resize:fit:679/format:webp/1*sU-20Q1Rx4Nx0SMJtDBwzw.png)

[![Image 11: Pawel](https://miro.medium.com/v2/resize:fill:20:20/1*axcXEgSlEMqpEtRExV2r2Q.jpeg)](https://medium.com/@meshuggah22?source=post_page---author_recirc--7c102fc22589----0---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[Pawel](https://medium.com/@meshuggah22?source=post_page---author_recirc--7c102fc22589----0---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[Google’s A2UI Protocol Just Changed How AI Agents Build User Interfaces — Here’s My First Project… -------------------------------------------------------------------------------------------------- ### Two weeks ago, Google open-sourced something that might reshape how we think about AI-generated interfaces: A2UI (Agent-to-User Interface).](https://medium.com/@meshuggah22/googles-a2ui-protocol-just-changed-how-ai-agents-build-user-interfaces-here-s-my-first-project-1d3b258984ac?source=post_page---author_recirc--7c102fc22589----0---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

Dec 28, 2025

[67](https://medium.com/@meshuggah22/googles-a2ui-protocol-just-changed-how-ai-agents-build-user-interfaces-here-s-my-first-project-1d3b258984ac?source=post_page---author_recirc--7c102fc22589----0---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F1d3b258984ac&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fgoogles-a2ui-protocol-just-changed-how-ai-agents-build-user-interfaces-here-s-my-first-project-1d3b258984ac&source=---author_recirc--7c102fc22589----0-----------------bookmark_preview----e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

![Image 12: FunctionGemma: I Fine-Tuned Google’s 270M Edge Model and Tested It on My S23](https://miro.medium.com/v2/resize:fit:679/format:webp/1*CRDKPgobZVH_jAQ_ArqBtA.png)

[![Image 13: Pawel](https://miro.medium.com/v2/resize:fill:20:20/1*axcXEgSlEMqpEtRExV2r2Q.jpeg)](https://medium.com/@meshuggah22?source=post_page---author_recirc--7c102fc22589----1---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[Pawel](https://medium.com/@meshuggah22?source=post_page---author_recirc--7c102fc22589----1---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[FunctionGemma: I Fine-Tuned Google’s 270M Edge Model and Tested It on My S23 ---------------------------------------------------------------------------- ### Google just dropped something interesting for edge AI developers: FunctionGemma, a 270M parameter model specifically designed for function…](https://medium.com/@meshuggah22/functiongemma-i-fine-tuned-googles-270m-edge-model-and-tested-it-on-my-s23-4105d7f45d39?source=post_page---author_recirc--7c102fc22589----1---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

Dec 19, 2025

[88 2](https://medium.com/@meshuggah22/functiongemma-i-fine-tuned-googles-270m-edge-model-and-tested-it-on-my-s23-4105d7f45d39?source=post_page---author_recirc--7c102fc22589----1---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4105d7f45d39&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Ffunctiongemma-i-fine-tuned-googles-270m-edge-model-and-tested-it-on-my-s23-4105d7f45d39&source=---author_recirc--7c102fc22589----1-----------------bookmark_preview----e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

![Image 14: HuggingFace Skills: Fine-Tune Any Open-Source LLM with One Line of English](https://miro.medium.com/v2/resize:fit:679/format:webp/1*MUeedz3VzD9Oqu4HCiqZ4g.png)

[![Image 15: Pawel](https://miro.medium.com/v2/resize:fill:20:20/1*axcXEgSlEMqpEtRExV2r2Q.jpeg)](https://medium.com/@meshuggah22?source=post_page---author_recirc--7c102fc22589----2---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[Pawel](https://medium.com/@meshuggah22?source=post_page---author_recirc--7c102fc22589----2---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[HuggingFace Skills: Fine-Tune Any Open-Source LLM with One Line of English -------------------------------------------------------------------------- ### What if fine-tuning a language model was as simple as sending a text message? HuggingFace just made it possible.](https://medium.com/@meshuggah22/huggingface-skills-fine-tune-any-open-source-llm-with-one-line-of-english-e25168b79a04?source=post_page---author_recirc--7c102fc22589----2---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

Dec 7, 2025

[212](https://medium.com/@meshuggah22/huggingface-skills-fine-tune-any-open-source-llm-with-one-line-of-english-e25168b79a04?source=post_page---author_recirc--7c102fc22589----2---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fe25168b79a04&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fhuggingface-skills-fine-tune-any-open-source-llm-with-one-line-of-english-e25168b79a04&source=---author_recirc--7c102fc22589----2-----------------bookmark_preview----e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

![Image 16: Hands-On with Bloom: Anthropic’s Open-Source Framework for Automated AI Behavioral Evaluation](https://miro.medium.com/v2/resize:fit:679/format:webp/1*I0rwc8KgvU3lLefwvFwbgA.png)

[![Image 17: Pawel](https://miro.medium.com/v2/resize:fill:20:20/1*axcXEgSlEMqpEtRExV2r2Q.jpeg)](https://medium.com/@meshuggah22?source=post_page---author_recirc--7c102fc22589----3---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[Pawel](https://medium.com/@meshuggah22?source=post_page---author_recirc--7c102fc22589----3---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[Hands-On with Bloom: Anthropic’s Open-Source Framework for Automated AI Behavioral Evaluation --------------------------------------------------------------------------------------------- ### Anthropic just open-sourced a very useful tool for your AI safety evaluation — Bloom. It’s an agentic framework that automatically…](https://medium.com/@meshuggah22/hands-on-with-bloom-anthropics-open-source-framework-for-automated-ai-behavioral-evaluation-0fb9c75c346a?source=post_page---author_recirc--7c102fc22589----3---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

Dec 22, 2025

[15](https://medium.com/@meshuggah22/hands-on-with-bloom-anthropics-open-source-framework-for-automated-ai-behavioral-evaluation-0fb9c75c346a?source=post_page---author_recirc--7c102fc22589----3---------------------e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F0fb9c75c346a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40meshuggah22%2Fhands-on-with-bloom-anthropics-open-source-framework-for-automated-ai-behavioral-evaluation-0fb9c75c346a&source=---author_recirc--7c102fc22589----3-----------------bookmark_preview----e8ffea7c_bb11_4e99_9ed8_7e59378e48ff--------------)

[See all from Pawel](https://medium.com/@meshuggah22?source=post_page---author_recirc--7c102fc22589---------------------------------------)

Recommended from Medium
-----------------------

![Image 18: Claude Code’s Creator, 100 PRs a Week — His Setup Will Surprise You](https://miro.medium.com/v2/resize:fit:679/format:webp/1*NzL9azc6cI21xVQeiuUheA.png)

[![Image 19: Vibe Coding](https://miro.medium.com/v2/resize:fill:20:20/1*nD0mORiSRPKPztpAByfNdw.png)](https://medium.com/vibe-coding?source=post_page---read_next_recirc--7c102fc22589----0---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

In

[Vibe Coding](https://medium.com/vibe-coding?source=post_page---read_next_recirc--7c102fc22589----0---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

by

[Alex Dunlop](https://medium.com/@alexjamesdunlop?source=post_page---read_next_recirc--7c102fc22589----0---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[Claude Code’s Creator, 100 PRs a Week — His Setup Will Surprise You ------------------------------------------------------------------- ### Simple principles most developers overlook completely](https://medium.com/vibe-coding/claude-codes-creator-100-prs-a-week-his-setup-will-surprise-you-7d6939c99f2b?source=post_page---read_next_recirc--7c102fc22589----0---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

Jan 15

[341 5](https://medium.com/vibe-coding/claude-codes-creator-100-prs-a-week-his-setup-will-surprise-you-7d6939c99f2b?source=post_page---read_next_recirc--7c102fc22589----0---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7d6939c99f2b&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fvibe-coding%2Fclaude-codes-creator-100-prs-a-week-his-setup-will-surprise-you-7d6939c99f2b&source=---read_next_recirc--7c102fc22589----0-----------------bookmark_preview----29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

![Image 20: Why Building AI Agents Is Mostly a Waste of Time](https://miro.medium.com/v2/resize:fit:679/format:webp/0*6w1dzyn44p2-bRS8)

[![Image 21: Data Science Collective](https://miro.medium.com/v2/resize:fill:20:20/1*0nV0Q-FBHj94Kggq00pG2Q.jpeg)](https://medium.com/data-science-collective?source=post_page---read_next_recirc--7c102fc22589----1---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

In

[Data Science Collective](https://medium.com/data-science-collective?source=post_page---read_next_recirc--7c102fc22589----1---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

by

[Shenggang Li](https://medium.com/@datalev?source=post_page---read_next_recirc--7c102fc22589----1---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[Why Building AI Agents Is Mostly a Waste of Time ------------------------------------------------ ### The Structural, Mathematical, and Economic Limits of RAG Pipelines](https://medium.com/data-science-collective/why-building-ai-agents-is-mostly-a-waste-of-time-55600b57e692?source=post_page---read_next_recirc--7c102fc22589----1---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

Jan 12

[1.2K 103](https://medium.com/data-science-collective/why-building-ai-agents-is-mostly-a-waste-of-time-55600b57e692?source=post_page---read_next_recirc--7c102fc22589----1---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F55600b57e692&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdata-science-collective%2Fwhy-building-ai-agents-is-mostly-a-waste-of-time-55600b57e692&source=---read_next_recirc--7c102fc22589----1-----------------bookmark_preview----29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

![Image 22: Claude Code Just Cut MCP Context Bloat by 46.9% — 51K Tokens Down to 8.5K With (New) Tool Search](https://miro.medium.com/v2/resize:fit:679/format:webp/1*1JKrivfT3hOtFHFuAQSWtw.png)

[![Image 23: Joe Njenga](https://miro.medium.com/v2/resize:fill:20:20/1*0Hoc7r7_ybnOvk1t8yR3_A.jpeg)](https://medium.com/@joe.njenga?source=post_page---read_next_recirc--7c102fc22589----0---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[Joe Njenga](https://medium.com/@joe.njenga?source=post_page---read_next_recirc--7c102fc22589----0---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[Claude Code Just Cut MCP Context Bloat by 46.9% — 51K Tokens Down to 8.5K With (New) Tool Search ------------------------------------------------------------------------------------------------ ### I watched my context window die before I could write a single prompt — 67,000 tokens gone, connecting 4 MCP servers. But now it’s fixed](https://medium.com/@joe.njenga/claude-code-just-cut-mcp-context-bloat-by-46-9-51k-tokens-down-to-8-5k-with-new-tool-search-ddf9e905f734?source=post_page---read_next_recirc--7c102fc22589----0---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

6d ago

[203 6](https://medium.com/@joe.njenga/claude-code-just-cut-mcp-context-bloat-by-46-9-51k-tokens-down-to-8-5k-with-new-tool-search-ddf9e905f734?source=post_page---read_next_recirc--7c102fc22589----0---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fddf9e905f734&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40joe.njenga%2Fclaude-code-just-cut-mcp-context-bloat-by-46-9-51k-tokens-down-to-8-5k-with-new-tool-search-ddf9e905f734&source=---read_next_recirc--7c102fc22589----0-----------------bookmark_preview----29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

![Image 24: Claude Cowork is a Game-Changer](https://miro.medium.com/v2/resize:fit:679/format:webp/1*Nvy6-bqu5BFlslcexJoZYQ.png)

[![Image 25: Marco Kotrotsos](https://miro.medium.com/v2/resize:fill:20:20/1*Js8KAMDJXq4BNemORhaX0w.jpeg)](https://medium.com/@kotrotsos?source=post_page---read_next_recirc--7c102fc22589----1---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[Marco Kotrotsos](https://medium.com/@kotrotsos?source=post_page---read_next_recirc--7c102fc22589----1---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[Claude Cowork is a Game-Changer ------------------------------- ### What Claude Code’s Consumer Sibling Means for the Future of Work](https://medium.com/@kotrotsos/claude-cowork-is-a-game-changer-ec4037ef0ba4?source=post_page---read_next_recirc--7c102fc22589----1---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

6d ago

[130 3](https://medium.com/@kotrotsos/claude-cowork-is-a-game-changer-ec4037ef0ba4?source=post_page---read_next_recirc--7c102fc22589----1---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fec4037ef0ba4&operation=register&redirect=https%3A%2F%2Fkotrotsos.medium.com%2Fclaude-cowork-is-a-game-changer-ec4037ef0ba4&source=---read_next_recirc--7c102fc22589----1-----------------bookmark_preview----29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

![Image 26: The Walls Are Closing In On Tesla](https://miro.medium.com/v2/resize:fit:679/format:webp/0*Nbcf3Y7PBvg3v4Aq)

[![Image 27: Will Lockett](https://miro.medium.com/v2/resize:fill:20:20/1*V0qWMQ8V5_NaF9yUoHAdyg.jpeg)](https://medium.com/@wlockett?source=post_page---read_next_recirc--7c102fc22589----2---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[Will Lockett](https://medium.com/@wlockett?source=post_page---read_next_recirc--7c102fc22589----2---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[The Walls Are Closing In On Tesla --------------------------------- ### Musk has destroyed every path forward.](https://medium.com/@wlockett/the-walls-are-closing-in-on-tesla-81285535029c?source=post_page---read_next_recirc--7c102fc22589----2---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

6d ago

[3.2K 76](https://medium.com/@wlockett/the-walls-are-closing-in-on-tesla-81285535029c?source=post_page---read_next_recirc--7c102fc22589----2---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F81285535029c&operation=register&redirect=https%3A%2F%2Fwlockett.medium.com%2Fthe-walls-are-closing-in-on-tesla-81285535029c&source=---read_next_recirc--7c102fc22589----2-----------------bookmark_preview----29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

![Image 28: End of Figma?](https://miro.medium.com/v2/resize:fit:679/format:webp/1*UVYGArVnLeqjybKc3Sfpcg.jpeg)

[![Image 29: Bootcamp](https://miro.medium.com/v2/resize:fill:20:20/1*_wDJs77bAPiwuAe9qOK5Zg.png)](https://medium.com/design-bootcamp?source=post_page---read_next_recirc--7c102fc22589----3---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

In

[Bootcamp](https://medium.com/design-bootcamp?source=post_page---read_next_recirc--7c102fc22589----3---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

by

[Punit Chawla](https://medium.com/@punitweb?source=post_page---read_next_recirc--7c102fc22589----3---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[Why Are Designers Leaving Figma? The Great Transition. ------------------------------------------------------ ### The Creative Industry Is Changing Rapidly & So Is Figma’s Future](https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745?source=post_page---read_next_recirc--7c102fc22589----3---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

Jan 11

[1.1K 33](https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745?source=post_page---read_next_recirc--7c102fc22589----3---------------------29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F1a63d8b03745&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdesign-bootcamp%2Fwhy-are-designers-leaving-figma-the-great-transition-1a63d8b03745&source=---read_next_recirc--7c102fc22589----3-----------------bookmark_preview----29ae3a00_20a9_42c6_93b3_44c9eb12887e--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--7c102fc22589---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----7c102fc22589---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----7c102fc22589---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----7c102fc22589---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----7c102fc22589---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----7c102fc22589---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----7c102fc22589---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----7c102fc22589---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----7c102fc22589---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----7c102fc22589---------------------------------------)
