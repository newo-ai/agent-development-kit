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

## Claude in the browser or the Claude desktop app

1. Customize → Connectors → **+** → **Add custom connector**.
2. Paste the Newo plugin address (from Newo Voice Creator or Newo support). Choose no
   authentication.
3. In a chat, turn the connector on and describe the business. Or paste the first message Newo
   Voice Creator gives.

## ChatGPT in the browser

1. Plugins → black **Add** button → **Add custom MCP server** (third item).
2. Name: Newo. Server URL: the plugin address. Authentication: **No authentication**.
3. Tick the confirmation and click **Create as a plugin**.
4. In the chat, press **+** and turn on Newo.
5. Work in the **same** chat for that agent; it keeps the agent's access for 180 days.

A work ChatGPT account may have custom MCP servers turned off by its administrator. Use a
personal account or the Claude desktop app.

Pictures and exact wording:
[agent setup guide, "Connect the Newo plugin"](https://knowledge.newo.ai/agent-setup#guide-connect-the-newo-plugin).

## What the browser plugin cannot do yet

- **Connect an agent created outside the plugin.** Use a terminal assistant, or Knowledge Studio
  for knowledge.
- **Run voice tests.** Ask Newo for an Assessor run.

Both are planned with the Newo Customer MCP server.
