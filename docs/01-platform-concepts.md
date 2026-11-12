# Platform concepts

What you need to know before your first request. Details:
[agent setup guide, "The agent in one page"](https://knowledge.newo.ai/agent-setup#guide-the-agent-in-one-page).

## The account

- One business (or one location) = one **account**, called a *customer*. It has an `idn` such as
  `C_NE_ABC12345`. Partners usually manage many accounts.
- An account holds **projects**. The AI receptionist is the project `naf` (**Newo Agent
  Framework**, NAF), shared by all Newo customers and updated by Newo. You may also see
  `assessor` (automated tests), `outbound`, `lead_nurturing` and projects built for one account.
- A project has **agents** (`ConvoAgent` talks to callers, `GeneralManagerAgent` does setup,
  reports and knowledge, workers send email and SMS). An agent has **flows**, and a flow has
  **skills**: the code, written in NSL or Guidance (Jinja-like templates).

## Settings: attributes

- **Attributes** are the settings: 300 to 500 per account. Customer attributes hold the business
  data and behavior switches; project attributes are few.
- Every attribute has an `idn`, a `value` (always a string), a `title`, a `description`, a `group`
  and a `value_type`.
- **The reference of every attribute**: https://knowledge.newo.ai/agent-setup/attributes/index.md.
  Read the description before you change one.
- `private` in a name does **not** mean secret. It marks developer settings.
- **Do not change** read-only settings, the groups `8. System`, `7. Customer Account` and
  `0. Agent Creator`, or custom groups built for one account.

## Channels: integrations and connectors

- **Integrations** are channel types: `newo_voice` (phone), `newo_chat` (web chat), `newo_sms`,
  `email`, `google_calendar`, `http`, `api`, `sandbox` (test chat), `mcp` (external MCP servers)
  and others.
- A **connector** is one configured instance of an integration. For example, the
  `newo_voice_connector` connector belongs to the phone integration; its provider is Twilio,
  Telnyx, Custom SIP or WebSocket.

## People and conversations

- Every caller or chat visitor is a **user persona** with one **actor** per channel. A
  conversation is a **session**.
- Transcripts are the actor's chat history. Logs record every skill run. See
  [debugging](debugging/README.md).

## Knowledge

- Short facts and texts live in **settings**.
- Longer material goes into the agent's knowledge base (**AKB**).
- Large knowledge (above about 100 to 200 articles) goes to **Newo Knowledge Studio**, an external
  search service.

See [06-knowledge.md](06-knowledge.md).

## Code versions: Flow Designer V1 and V2

Accounts are moving to Flow Designer V2 one by one (from November 2026).

- **Which version an account uses:** `GET /api/v1/customer/settings/name/projects_v2_enabled`. A
  value of `"true"` means V2; a 404 means V1. Decide only by this setting.
- **V2:** agent code is a set of **files in a project version**. Only a whole version can be
  published, and publishing replaces the project's own attributes with the values stored in the
  version.
- **Details:** [API reference, "Which designer"](https://knowledge.newo.ai/agent-setup#api-which-designer).

## Updates from Newo

- When automatic updates are on for `naf`, Newo releases reach the account by themselves, with
  fixes and new features. The flag is `is_auto_update_enabled` on the project.
- A local code change and automatic updates do not mix. See
  [04-naf-change-policy.md](04-naf-change-policy.md).
