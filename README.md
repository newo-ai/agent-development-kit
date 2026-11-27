# Newo Agent Development Kit (ADK)

Agent Development Kit for Partner AI Enablement: the shared knowledge base for **AI coding
assistants** (Claude Code, Codex, Cursor, Claude and ChatGPT in the browser). With it they build,
configure, test, debug and connect voice and chat agents on the **Newo platform** for partners and
business owners.

If you are a coding assistant: **start with [AGENTS.md](AGENTS.md)**. It tells you what to read for
the task you were given and the rules you must follow.

If you are a person: point your coding assistant at this repository (for example, "read
https://github.com/newo-ai/agent-development-kit and help me set up my Newo agent"). The assistant
does the technical work; you make the decisions.

## Set up

New to Newo? The ADK is a set of instructions for an AI assistant. You open it in the assistant,
connect the assistant to your Newo account, and the assistant does the work. You don't choose a
tool: the assistant follows this rule.

| | The assistant uses | For |
|---|---|---|
| **By default** | the **Newo Customer MCP server**, added as a custom connector; you sign in with your Newo account (OAuth), no key ([docs/02, section D](docs/02-access-and-tools.md#d-newo-customer-mcp-server)) | everything the MCP can do ([docs/02, "Which path"](docs/02-access-and-tools.md#which-path); each MCP row **to confirm** against the live tool list) |
| **Only when needed** | the **Newo CLI**, only when the assistant asks; you sign in with your Newo account (`newo login`). The assistant sets it up | saved `newo test` files and CI, export or backup of an agent, or a task the MCP has no tool for |
| **Neither** | the Workflow Builder, by hand | editing scenarios ([docs/05](docs/05-scenarios.md)) |

1. **Connect the Newo MCP first:** [SOP](docs/sop/connect-newo-mcp.md). In ChatGPT the assistant
   cannot open these pages while the server is on. If a step marked (to confirm) stalls on the
   MCP, the assistant switches to the CLI for that step (sign in with `newo login`; no API key).
2. **The CLI only when the assistant asks; you sign in with your Newo account:**
   [SOP: sign in to the CLI](docs/sop/sign-in-cli.md). Which task needs which tool:
   [docs/02, "Which path"](docs/02-access-and-tools.md#which-path).

In the Claude desktop app without Git: [quick start](docs/quick-start-desktop.md). Stuck at any
point? Tell your assistant "I'm stuck".

The rest of this section is for when the assistant sets up the CLI.

**Folder layout.** Keep this repository as it is, and do all agent work in `work/`, one folder per
agent:

```
agent-development-kit/          this repository; read it, do not edit it for one agent
└── work/                       your agents; Git ignores this folder
    ├── <agent-name>/           one agent = one folder
    │   ├── .env                this agent's account, from `newo customer switch`; no key
    │   ├── build-notes.md      delivery only: the build notes; "Account idn" says which account it is
    │   └── newo_customers/     what `newo pull` downloads
    └── <next-agent>/
```

`work/` has no history: make it its own Git repository or a synced folder if you want backups.
First add a `.gitignore` in `work/` with `.env`, `.env.*` and `.newo/`, and keep that repository
private. A synced folder (iCloud, Dropbox, OneDrive) also syncs the keys.

**One account per agent folder.** The person signs in once with `newo login` (their Newo
account, in the browser). In each agent's folder, `newo customer switch <idn>` saves that agent's
account in the folder's `.env`. Run every `newo` command from inside the agent's folder: the CLI
reads the `.env` of the folder you are in. A key in `.env` turns the browser login off: use one
only where the login is refused ([SOP: sign in to the CLI](docs/sop/sign-in-cli.md)), and never
through a chat.

Don't run `newo init` inside `work/`: create the agent's folder and run `newo customer switch`
there. The root
`.gitignore` already ignores `work/` and `.env`.

**Check the account before every change.** Run `newo profile` in the agent's folder. If the agent
has a `build-notes.md` (from the delivery process), compare `Customer IDN` with its `Account idn`;
if they differ, stop. Otherwise the assistant says the account's name and IDN back, and you say
"yes" once per session. On the MCP path, before any change the assistant names the customer and
its IDN from `get_customers`, and you say "yes" once per session **(to confirm)**.

**Setup check.** Run [docs/setup-check.md](docs/setup-check.md) on first setup and whenever
something stops working. The checks change nothing in the agent's setup. Check 4 leaves one
sandbox chat in the conversations. Some fixes change files on this computer; ask before each one.

## Map

Read top to bottom for a new agent; jump to the block you need for a single task.

**Understand**

| I need to... | Read |
|---|---|
| Deliver an agent for a customer, stage by stage: requirements, build, test, go-live, operation | [delivery/](delivery/README.md) |
| See the big picture: the problem, the harness, the feedback loop | [docs/00-how-the-ecosystem-works.md](docs/00-how-the-ecosystem-works.md) |
| Understand the platform in 10 minutes | [docs/01-platform-concepts.md](docs/01-platform-concepts.md) |
| Get access: API keys, the Newo Customer MCP server, the older plugin, Knowledge Studio | [docs/02-access-and-tools.md](docs/02-access-and-tools.md) |
| Work with a non-technical owner in a chat, step by step, with the rules | [docs/assistant-guide.md](docs/assistant-guide.md), [docs/humans/](docs/humans/README.md) |

**Create and configure**

| I need to... | Read |
|---|---|
| Create a new agent for an owner | [docs/assistant-guide.md, "Create the agent"](docs/assistant-guide.md#create-the-agent) |
| Finish the configuration of a new agent (business info, hours, greeting, transfers, knowledge, reports) | [playbooks/finish-configuration.md](playbooks/finish-configuration.md), then the [industry page](industries/README.md) |
| Configure or customize an agent (settings first) | [docs/03-configure-and-customize.md](docs/03-configure-and-customize.md) |
| Look up any setting (attribute): meaning, format, examples, dependencies | [reference/attributes/index.md](reference/attributes/index.md), industry settings in [reference/attributes/industries/](reference/attributes/industries/general.md) |
| Change scenarios (what the agent does for each caller intent) | [docs/05-scenarios.md](docs/05-scenarios.md) |
| Give the agent knowledge (settings, AKB, Knowledge Studio, search services) | [docs/06-knowledge.md](docs/06-knowledge.md) |
| Change connector settings (voice model, voice, speech recognizer) through the API | [docs/08-connector-settings.md](docs/08-connector-settings.md) |
| Decide whether to change framework (NAF) code | [docs/04-naf-change-policy.md](docs/04-naf-change-policy.md) |
| Industry specifics (restaurants, dental and medical, home services, ...) | [industries/](industries/README.md) |

**Integrate**

| I need to... | Read |
|---|---|
| Connect a calendar, CRM, booking system, webhooks, email/SMS, MCP servers | [playbooks/connect-external-systems.md](playbooks/connect-external-systems.md), [docs/integrations/](docs/integrations/README.md) |

**Launch**

| I need to... | Read |
|---|---|
| Put the agent to work: nights first, then the day (overflow or AI first) | [playbooks/night-launch.md](playbooks/night-launch.md), [docs/telephony/go-live.md](docs/telephony/go-live.md) |
| Keep the business's phone number, forward calls, connect SIP | [playbooks/connect-phone-line.md](playbooks/connect-phone-line.md), [docs/telephony/](docs/telephony/README.md) |
| Get a new phone number (any country) | [playbooks/get-phone-number.md](playbooks/get-phone-number.md), [docs/telephony/phone-numbers.md](docs/telephony/phone-numbers.md) |

**Test, review and debug**

| I need to... | Read |
|---|---|
| Test with text and with real voice calls | [docs/testing/](docs/testing/README.md) |
| Review real conversations and report to the owner | [playbooks/review-conversations.md](playbooks/review-conversations.md) |
| Check an agent's health; decide between a setting (level A) and a scenario change (level B) | [docs/07-health-check.md](docs/07-health-check.md) |
| Turn a problem into a fix and confirm it | [playbooks/improve-and-fix.md](playbooks/improve-and-fix.md) |
| Debug a bad conversation, a wrong answer, a failed booking | [docs/debugging/](docs/debugging/README.md) |
| Debug Knowledge Studio and knowledge search | [docs/debugging/search-debug.md](docs/debugging/search-debug.md), [docs/debugging/studio-troubleshooting.md](docs/debugging/studio-troubleshooting.md) |

**Reference and community**

| I need to... | Read |
|---|---|
| Every API request (Flow Designer V2), the old designer (V1) | [reference/api.md](reference/api.md), [reference/api-v1.md](reference/api-v1.md) |
| All playbooks in one list | [playbooks/](playbooks/README.md) |
| Run a delivery task as a skill (requirements, criteria, SOW, plan, UAT, go-live, customer emails, sign-off) | [skills/](skills/README.md) |
| Report a bug or request something from Newo | [docs/support/](docs/support/README.md) |
| Report a security problem, or a secret published by mistake | [SECURITY.md](SECURITY.md) |
| Learn from other assistants' cases, or share yours | [learnings/](learnings/README.md) |

## Related sources

- **Agent setup guide, API reference and attribute reference** are in this repository (moved here
  from knowledge.newo.ai on 13 November 2026):
  - [docs/assistant-guide.md](docs/assistant-guide.md): the step-by-step guide for an AI assistant
    working with an owner in a chat;
  - [playbooks/](playbooks/README.md): the task playbooks;
  - [reference/api.md](reference/api.md) and [reference/api-v1.md](reference/api-v1.md): the full
    API reference;
  - [reference/attributes/](reference/attributes/index.md): the reference of every setting
    ("attribute"), with the industry settings.
- **Newo CLI**: https://www.npmjs.com/package/newo (`npm i -g newo`). From a terminal you can:
  - pull and push agent code;
  - run sandbox chats and scripted chat tests;
  - read logs and transcripts.
- **Help center**: https://help.newo.ai

## Contributing

Coding assistants and people are welcome to propose fixes and new learnings. See
[CONTRIBUTING.md](CONTRIBUTING.md). Never commit secrets, API keys or anyone's personal data.

Maintained by Newo.ai. This is the first version of the repository (November 2026). Some parts
describe features that are still being rolled out. They are marked **(rolling out)** or
**(planned)**.
