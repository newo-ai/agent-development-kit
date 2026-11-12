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

## Map

| I need to... | Read |
|---|---|
| See the big picture: the problem, the harness, the feedback loop | [docs/00-how-the-ecosystem-works.md](docs/00-how-the-ecosystem-works.md) |
| Understand the platform in 10 minutes | [docs/01-platform-concepts.md](docs/01-platform-concepts.md) |
| Get access: API keys, the browser plugin, Knowledge Studio | [docs/02-access-and-tools.md](docs/02-access-and-tools.md) |
| Configure or customize an agent (settings first) | [docs/03-configure-and-customize.md](docs/03-configure-and-customize.md) |
| Decide whether to change framework (NAF) code | [docs/04-naf-change-policy.md](docs/04-naf-change-policy.md) |
| Change scenarios (what the agent does for each caller intent) | [docs/05-scenarios.md](docs/05-scenarios.md) |
| Give the agent knowledge (settings, AKB, Knowledge Studio) | [docs/06-knowledge.md](docs/06-knowledge.md) |
| Put the agent to work: nights first, then the day (overflow or AI first) | [docs/telephony/go-live.md](docs/telephony/go-live.md) |
| Keep the business's phone number, forward calls, connect SIP | [docs/telephony/](docs/telephony/README.md) |
| Get a new phone number (any country) | [docs/telephony/phone-numbers.md](docs/telephony/phone-numbers.md) |
| Connect a CRM, a booking system or a patient management system | [docs/integrations/](docs/integrations/README.md) |
| Test with text and with real voice calls | [docs/testing/](docs/testing/README.md) |
| Debug a bad conversation, a wrong answer, a failed booking | [docs/debugging/](docs/debugging/README.md) |
| Help a non-technical owner work with an AI assistant | [docs/humans/](docs/humans/README.md) |
| Report a bug or request something from Newo | [docs/support/](docs/support/README.md) |
| Industry specifics (restaurants, dental and medical, home services, ...) | [industries/](industries/README.md) |
| Learn from other assistants' cases, or share yours | [learnings/](learnings/README.md) |

## Related sources

- **Agent setup guide**: https://knowledge.newo.ai/agent-setup, also as one Markdown file:
  https://knowledge.newo.ai/agent-setup/llms.txt.
  - The step-by-step guide for an AI assistant working with an owner in a chat.
  - The full API reference.
  - The reference of every setting ("attribute").

  This repository links to the guide instead of copying it.
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
