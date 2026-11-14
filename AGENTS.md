# Instructions for AI coding assistants

You are helping a partner or a business owner build, configure, improve or connect an AI agent on
the Newo platform. Read this file first. It is short on purpose.

## 1. Find your path

1. Identify **who** you work for: a business owner (usually not technical), a partner or agency
   (technical, often many agents), or a developer.
2. Identify **what** they want. Typical requests and where to read:
   - Working with a non-technical owner in a chat: [docs/assistant-guide.md](docs/assistant-guide.md)
     (how to talk to the owner, how to create an agent, rules, how to call the API).
   - "Create an agent": [docs/assistant-guide.md, "Create the agent"](docs/assistant-guide.md#create-the-agent).
   - "Set up hours, greeting, prices", "finish the setup": [playbooks/finish-configuration.md](playbooks/finish-configuration.md),
     [docs/03](docs/03-configure-and-customize.md), then the [industry page](industries/README.md).
   - What a setting means, its format, examples: [reference/attributes/index.md](reference/attributes/index.md).
   - The exact API request: [reference/api.md](reference/api.md) (Flow Designer V2) or
     [reference/api-v1.md](reference/api-v1.md) (old designer).
   - "Put the agent to work", "forward calls at night", "forward after two rings": [playbooks/night-launch.md](playbooks/night-launch.md),
     [docs/telephony/go-live.md](docs/telephony/go-live.md).
     Forward FROM the business number TO the AI phone number (`project_representative_agent_voice_phone_number`).
   - "Keep my phone number", "SIP": [playbooks/connect-phone-line.md](playbooks/connect-phone-line.md),
     [docs/telephony](docs/telephony/README.md).
   - "I need a number in Germany / Armenia / ...": [playbooks/get-phone-number.md](playbooks/get-phone-number.md),
     [docs/telephony/phone-numbers.md](docs/telephony/phone-numbers.md).
   - "Connect my CRM / booking system / patient management system": [playbooks/connect-external-systems.md](playbooks/connect-external-systems.md),
     [docs/integrations](docs/integrations/README.md).
   - "How did the calls go?": [playbooks/review-conversations.md](playbooks/review-conversations.md).
   - "The agent said something wrong / switched language / did not book": [playbooks/improve-and-fix.md](playbooks/improve-and-fix.md),
     [docs/debugging](docs/debugging/README.md).
   - "The agent does not know X", Knowledge Studio does not work: [docs/debugging/search-debug.md](docs/debugging/search-debug.md),
     [docs/debugging/studio-troubleshooting.md](docs/debugging/studio-troubleshooting.md).
   - "Check my agent", "why does it say X", "how do I make it do Y": [docs/07-health-check.md](docs/07-health-check.md).
   - "Test it": [docs/testing](docs/testing/README.md).
   - "Change the voice model / voice / speech recognizer", any connector setting: [docs/08](docs/08-connector-settings.md).
     Every setting the portal can change, the API can change. Never say "not possible through the API" before reading that page.
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
6. **Customize the agent, not the framework.** Every change happens at the level of this agent's
   customization: settings, knowledge, conversation tools, scenarios, or a separate project. Change
   the shared framework code (NAF) only in an absolutely exceptional case, when there is no other
   way to reach the goal. Then follow [docs/04-naf-change-policy.md](docs/04-naf-change-policy.md):
   turn off automatic updates, warn the person, and **file a NAF change notice as an issue in this
   repository** (template "NAF change notice").
7. **Check your work.** After a change, read it back and test (sandbox chat or a real call)
   before you say it works.
8. **Respect real callers.** A phone change (forwarding, SIP, transfers) affects real callers at
   once. Agree on a test window with the person.
9. **Say what you do not know.** If this repository and the platform disagree, trust the platform
   (read the live value, run the request), tell the person, and propose a fix to this repository.

## 3. How you reach the platform

- **Terminal assistants** (Claude Code, Codex, Cursor): the Newo HTTP API with the account's API
  key, or the Newo CLI. See [docs/02-access-and-tools.md](docs/02-access-and-tools.md).
- **Connector settings** are written with `POST /api/v1/integrations/connectors/{id}/settings`,
  not `PATCH`. Allowed values come from the platform, not from memory. See
  [docs/08-connector-settings.md](docs/08-connector-settings.md).
- **Browser assistants** (ChatGPT, Claude): the **Newo Customer MCP server**. The person signs in
  with their Newo account; no key in the chat. Server URL, client ID and steps:
  [docs/02-access-and-tools.md, section D](docs/02-access-and-tools.md#d-newo-customer-mcp-server).

## 4. Before you finish

- Tell the person what changed, how to undo it and what to watch.
- If you found something other assistants should know (a pitfall, a working integration recipe),
  propose a learning: [learnings/README.md](learnings/README.md).
- If you found a platform bug, file it: [docs/support/README.md](docs/support/README.md).
