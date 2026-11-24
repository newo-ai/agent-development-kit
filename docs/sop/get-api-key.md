# SOP: get an API key

Do this **only when your assistant asks for a key**. Most work needs only the Newo MCP
([connect it](connect-newo-mcp.md)). A key is for the few tasks that need the Newo CLI, such as
saved test files or a backup of the agent
([which path](../02-access-and-tools.md#which-path)).

One agent, one key. Never paste the key into a chat: anyone who reads the chat can use it.

## 1. Create the key in Newo

1. Sign in at https://app.newo.ai, choose the account and open **Builder**.
2. Go to **Integrations** and open **API Integration**.
3. Create a connector. Its IDN must be all lowercase, with no spaces: use `_` instead of a space,
   for example `newo_cli`. Save it.
4. Open the connector again and copy the key. It appears only after saving.

## 2. Give it to the assistant without the chat

- **Claude desktop app:** the assistant opens a field for the key above the prompt. The first
  time, Claude asks whether to turn on the mods written in this session: choose **Turn them on**
  **(to confirm)**. Paste the key into the field and press Enter. The key goes straight into a
  file, the assistant never sees it, and you get a message with the account's name.
- **Any other app, or if the field does not load:** the assistant opens the key file
  (`work/<agent-name>/.env`) in a text editor. Paste the key after `NEWO_API_KEY=` and save.

## If the key was exposed

You pasted it into a chat, an email or a file someone else can read: tell your assistant. Newo
support can replace the key.

## Next

Tell your assistant "the key is in". It runs the [setup check](../setup-check.md) and tells you
the account's name. Check that it is the right business.
