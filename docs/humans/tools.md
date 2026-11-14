# Setting up each AI assistant

Give the person the steps for their tool in one message.

## Claude Code, Codex, Cursor (terminal or IDE)

1. Install Node.js. Then: `npm i -g newo`.
2. Make a folder for the business (or one per partner), open a terminal there and run `newo init`.
   It writes instructions and skills for coding assistants, an empty `.env` and a `.gitignore`.
3. The person creates an API key in the Newo portal (Builder → Integrations → API Integration →
   new connector → copy the key) and pastes it into `.env` themselves. See
   [02-access-and-tools.md](../02-access-and-tools.md#a-terminal-assistants).
4. Open the assistant in that folder. Point it to this repository:
   > Read https://github.com/newo-ai/agent-development-kit (start with AGENTS.md) and help me with
   > my Newo agent.
5. Keep the folder in a private git repository if the partner manages many agents. Never commit
   `.env`.

## ChatGPT or Claude (browser, desktop, mobile)

The person connects the **Newo Customer MCP server** once and signs in with their Newo account. It
works for any agent that account can open. Give them the steps for their tool from
[02-access-and-tools.md, section D](../02-access-and-tools.md#d-newo-customer-mcp-server):
- the server URL `https://api.newo.ai/api/v1/customer-mcp`;
- authentication **OAuth** with Newo's client ID `g2t0mUwvyASY6OC9F76xvNBSFfZjSyfe`, secret empty;
- **ChatGPT:** Plugins → black **Add** button → **Add custom MCP server**;
- **Claude:** Customize → Connectors → **+ Add** → **Add custom connector**.

A work ChatGPT account may have custom MCP servers turned off by its administrator. Use a
personal account or Claude.

Then the first message names the agent's IDN and carries the rules from [AGENTS.md](../../AGENTS.md)
in short form. Do not rely on a link to this repository: in a chat with the Newo server turned on,
ChatGPT cannot open web pages (see
[section D](../02-access-and-tools.md#d-newo-customer-mcp-server)).

## What a browser assistant cannot do yet

- **Run voice tests.** Ask Newo for an Assessor run.
