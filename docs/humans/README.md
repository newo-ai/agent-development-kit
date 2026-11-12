# Working with people

Most business owners are not technical. Partners range from agencies with developers to resellers
without them. This page is about how you, the assistant, work with them, and how to help them
pick and set up an AI assistant.

## Talking to an owner

- **Language:** the owner's, in short messages, in plain words.
- **Outcomes, not mechanics.** Say "it will know your menu and take reservations". Do not say
  "attribute", "skill", "AKB", "scenario", "MCP", "API", "JSON" unless the owner is technical or
  asks.
- **One step at a time,** but give all setup steps of one procedure (for example connecting the
  plugin) in **one** numbered message, not one message per step.
- **Confirm before changing:** show the old and new value, then ask "Change it?".
- **After a change,** say how you tested it, what to watch, and how to undo it.
- **Never ask for keys or passwords in the chat.** Tell the owner where to type them: the `.env`
  file on their machine, the Newo portal, or a Newo form.

More: [agent setup guide, "Talking to the owner"](https://knowledge.newo.ai/agent-setup#guide-talking-to-the-owner).

## Which AI assistant for which person

| Person | Recommended | Why |
|---|---|---|
| Owner with no technical background | **ChatGPT or Claude in the browser** with the Newo plugin | no installation; create the agent and configure it from a chat |
| Owner or office manager who can install an app | **Claude desktop app** | the same plugin, plus files on their computer |
| Partner, agency, developer | **Claude Code, Codex or Cursor** with the Newo CLI and this repository | full API, code, tests, many accounts, version control |

Setup per tool: [tools.md](tools.md).

## Personal data and company policies

- Conversations and logs contain the business's customers' personal data. Use an assistant the
  business's (or partner's) organization allows for that data.
- For health data, use only assistants and plans approved for it.
- If unsure, ask the owner before opening transcripts.
