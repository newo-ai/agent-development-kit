# SOP: connect the Newo MCP

The Newo MCP lets your AI assistant work on your Newo agents. You sign in with your Newo account.
You need no API key. You do this once per AI app.

## What you need

- ChatGPT or Claude (web, desktop or mobile), or Claude Code or Codex in a terminal.
- A Newo account that can open the agent.

## Steps

1. **Add the connector.** Follow the steps for your app in
   [docs/02, section D](../02-access-and-tools.md#d-newo-customer-mcp-server). The settings you
   enter (the server URL and the OAuth client ID) are in the table there.
2. **Sign in** on the Newo page that opens, with the Newo account of the agent.
3. **Turn it on in a chat.** ChatGPT: type `@` and pick Newo. Claude: **+** → **Connectors** →
   turn on Newo.

## Check it worked

Ask your assistant: "List my Newo businesses". It names each business and its IDN. Say which one
is yours. If yours is not there:

- **Claude Team or Enterprise:** "Add custom connector" is greyed out. Your organization's Owner
  adds it once; then you press **Connect**.
- **A work ChatGPT account** may block custom MCP servers. Use a personal account or Claude.
- **ChatGPT cannot open web pages** while the Newo server is on in that chat. Paste what the
  assistant needs into the chat.
- Anything else: tell your assistant "I'm stuck".

## Next

Tell your assistant what you want to do with the agent.

Stuck? Tell your assistant "I'm stuck".
