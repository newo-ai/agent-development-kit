# docs/ — platform documentation hub

Earned its own file: score 10 (33 files, 7 subdirectories, 113 inbound links — the most
referenced directory). Topical platform docs; one-task procedures live in ../playbooks/, exact
formats in ../reference/.

## STRUCTURE

- `00-how-the-ecosystem-works.md` — why this repository exists, the shared framework (NAF)
- `01-platform-concepts.md` — accounts, attributes, connectors, conversations, V1/V2 designers
- `02-access-and-tools.md` — API key, CLI, plugin, Knowledge Studio, Customer MCP, secrets
- `03-configure-and-customize.md` — customization ladder, when a change takes effect
- `04-naf-change-policy.md` — exceptional framework changes: alternatives, consent, notice
- `05-scenarios.md` — Workflow Builder scenarios, system-managed compiled state
- `06-knowledge.md` — AKB, Knowledge Studio, search services, personal-data rules
- `07-health-check.md` — level A/B review procedure and reporting
- `08-connector-settings.md` — read, write and verify connector settings
- `assistant-guide.md` — long-form guide for working with an owner (top hub, ~27 inbound refs)
- `debugging/` — conversation logs, search answers, Studio troubleshooting, common issues
- `telephony/` — forwarding, go-live, phone numbers, transfers, WebSocket voice API
- `integrations/` — HTTP/REST and MCP procedures, PMS appointment example
- `testing/` — scripted text tests, voice tests
- `humans/` — how to talk to the owner
- `support/` — bug reports and operations requests
- `images/` — ChatGPT setup screenshots used by assistant-guide.md

## WHERE TO LOOK

| Task | Go to |
|---|---|
| API key, CLI install, MCP setup, secrets | [02-access-and-tools.md](02-access-and-tools.md) |
| Change a setting; when it takes effect | [03-configure-and-customize.md](03-configure-and-customize.md) |
| Knowledge base, search quality | [06-knowledge.md](06-knowledge.md), [debugging/search-debug.md](debugging/search-debug.md) |
| Check an agent's health | [07-health-check.md](07-health-check.md) |
| Connector or speech-recognizer settings | [08-connector-settings.md](08-connector-settings.md) |
| Phone numbers, forwarding, go-live | [telephony/](telephony/README.md) |
| Connect a CRM / booking / PMS | [integrations/](integrations/README.md) |
| Why a call went wrong | [debugging/](debugging/README.md) |
| Prove it works | [testing/](testing/README.md) |

## CONVENTIONS

- `00`–`08` is a topic list, not a reading order; the delivery lifecycle is numbered separately
  under ../delivery/.
- Hub pages link to detail pages instead of repeating them; keep it that way.
- Anchors are lowercase hyphenated slugs and other pages link to them
  (`#d-newo-customer-mcp-server`, `#scripted-tests-newo-test`) — rename headings carefully.

## ANTI-PATTERNS

- `PATCH` on connector settings reports success but silently ignores the settings — always
  `POST /api/v1/integrations/connectors/{id}/settings` ([08](08-connector-settings.md)).
- Level B fields: edit in Workflow Builder / Vibe mode, never through the API; never build a
  parallel structure next to the existing one ([07](07-health-check.md)).
- Never answer a settings question from memory — read the live value ([08](08-connector-settings.md)).
- No account details, personal data or secrets in public issues ([support/](support/README.md)).
- Create agents with `create_agent`; never send the owner to agent.newo.ai/creator
  ([assistant-guide.md](assistant-guide.md)).
