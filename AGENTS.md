# Instructions for AI coding assistants

You are helping a partner or a business owner build, configure, improve or connect an AI agent on
the Newo platform. Read this file first. It is short on purpose.

## 1. Find your path

1. Identify **who** you work for: a business owner (usually not technical), a partner or agency
   (technical, often many agents), or a developer.
2. Identify **what** they want. Typical requests and where to read:
   - "Create an agent", "set up hours, greeting, prices": [docs/03](docs/03-configure-and-customize.md),
     then the [industry page](industries/README.md).
   - "Keep my phone number", "forward calls after two rings", "SIP": [docs/telephony](docs/telephony/README.md).
   - "I need a number in Germany / Armenia / ...": [docs/telephony/phone-numbers.md](docs/telephony/phone-numbers.md).
   - "Connect my CRM / booking system / patient management system": [docs/integrations](docs/integrations/README.md).
   - "The agent said something wrong / switched language / did not book": [docs/debugging](docs/debugging/README.md).
   - "Test it": [docs/testing](docs/testing/README.md).
   - "Add our documents / FAQ / price list": [docs/06-knowledge.md](docs/06-knowledge.md).
3. Read [learnings/](learnings/README.md) for the same industry or the same integration: other
   assistants may have solved your case already.
4. Identify the **industry** and read its page in [industries/](industries/README.md).

## 2. Rules (always)

1. **Ask before every change.** Show the person what will change (old value, new value) in plain
   words and wait for a clear "yes". Reading needs no permission.
2. **Never delete** agents, projects, flows, skills, attributes, connectors or webhooks. If
   something must go, the person asks Newo support.
3. **Keep the old value** of anything you change, so it can be put back.
4. **Secrets never go through a chat.** Do not ask a person to paste an API key, SIP password or
   token into a chat window. In a terminal, keep keys in environment variables or a `.env` file
   that is in `.gitignore`. Never print them, never put them in a URL, a commit or an issue.
5. **Callers' data is private.** Transcripts and logs contain names, phone numbers and sometimes
   health data. Use only what the task needs, keep it on the person's machine or in Newo, and
   never paste it into an issue, a pull request or this repository. Health data (PHI) needs
   extra care: see [docs/integrations/README.md](docs/integrations/README.md#health-data).
6. **Settings before code.** Almost everything is a setting (attribute). Change the shared
   framework code (NAF) only when no setting can do it, and then follow
   [docs/04-naf-change-policy.md](docs/04-naf-change-policy.md): turn off automatic updates,
   warn the person, and file a NAF change notice.
7. **Check your work.** After a change, read it back and test (sandbox chat or a real call)
   before you say it works.
8. **Respect real callers.** A phone change (forwarding, SIP, transfers) affects real callers at
   once. Agree on a test window with the person.
9. **Say what you do not know.** If this repository and the platform disagree, trust the platform
   (read the live value, run the request), tell the person, and propose a fix to this repository.

## 3. How you reach the platform

- **Terminal assistants** (Claude Code, Codex, Cursor): the Newo HTTP API with the account's API
  key, or the Newo CLI. See [docs/02-access-and-tools.md](docs/02-access-and-tools.md).
- **Browser assistants** (ChatGPT, claude.ai): the Newo plugin (a custom MCP server). See the same
  page.

## 4. Before you finish

- Tell the person what changed, how to undo it and what to watch.
- If you found something other assistants should know (a pitfall, a working integration recipe),
  propose a learning: [learnings/README.md](learnings/README.md).
- If you found a platform bug, file it: [docs/support/README.md](docs/support/README.md).
