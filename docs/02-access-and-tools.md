# Access and tools

How an AI assistant reaches a Newo account, and what to tell a person so they can give you access
safely.

## Which path

| The person uses | You reach Newo through | Section |
|---|---|---|
| Claude Code, Codex, Cursor or another assistant with a terminal | the Newo HTTP API or the Newo CLI, with the account's API key in an environment variable | [A](#a-terminal-assistants) |
| ChatGPT or Claude in the browser | the **Newo plugin** (a custom MCP server) | [B](#b-browser-assistants-the-newo-plugin) |
| Any assistant, for knowledge only | **Newo Knowledge Studio** | [C](#c-newo-knowledge-studio) |
| Any MCP client, with sign-in through a Newo account | **Newo Customer MCP server** **(planned)** | [D](#d-newo-customer-mcp-server-planned) |

## A. Terminal assistants

**The API key.** The owner (or a partner with access) creates it once:
1. Sign in at https://app.newo.ai, choose the account, open **Builder**.
2. Go to **Integrations**, find **API Integration**, and create a connector with any name, for
   example `newo-cli`. Save it.
3. Open the connector again and copy the key. It appears only after saving.

The person puts the key into a `.env` file in the project folder **themselves**, for example
`NEWO_API_KEY=...`, and `.env` must be in `.gitignore`. Never ask them to paste the key into a chat.

**The API.**
- Base URL: `https://app.newo.ai`.
- Exchange the key for a 15-minute token:
  ```bash
  curl -s -X POST https://app.newo.ai/api/v1/auth/api-key/token \
    -H "x-api-key: $NEWO_API_KEY" -H "accept: application/json"
  ```
- Send `Authorization: Bearer <access_token>` with every request. On 401 or 403, get a new token
  and retry once.
- First call of every session: `GET /api/v1/customer/profile`. Check that its `idn` is the account
  the person means.
- Full reference: https://knowledge.newo.ai/agent-setup#api.

**The CLI.** `npm i -g newo`, then run `newo init` in an empty folder. It writes instructions and
skills for coding assistants, an empty `.env` and a `.gitignore`. Useful commands:
- `newo pull` / `newo push` — agent code; works for Flow Designer V2.
- `newo sandbox` — test chat.
- `newo test <scenario.yaml>` — scripted chat tests.
- `newo logs --session-id <id>` — the logs of one conversation.
- `newo conversations` — transcripts.

The CLI masks secrets in its output. Changing framework (NAF) code needs explicit confirmation
(`NEWO_UNRESTRICTED`, default off); see [04-naf-change-policy.md](04-naf-change-policy.md).

## B. Browser assistants: the Newo plugin

ChatGPT and Claude in the browser cannot call APIs by themselves. The **Newo plugin** is a custom
MCP server that gives them tools.

| Tool | What it does |
|---|---|
| `create_agent` | creates a new agent from the business's website |
| `agent_status` | creation progress, the phone number, a link to talk to the agent in the browser |
| `newo_request` | any Newo API request for that agent |
| `read_guide` | reads the agent setup guide and the documents it names |
| `studio_connect`, `studio_tools`, `studio_call` | Knowledge Studio **(rolling out)** |

**How it connects.**
- The plugin address comes in the prompt that Newo Voice Creator gives the owner, or from Newo
  support. It ends in `/mcp`.
- **ChatGPT:** Plugins → black **Add** button → **Add custom MCP server** (the third item). Paste
  the address, set authentication to **No authentication**, tick the confirmation, then
  **Create as a plugin**. Back in the chat, turn on Newo with **+**. Step-by-step with pictures:
  [agent setup guide, "Connect the Newo plugin"](https://knowledge.newo.ai/agent-setup#guide-connect-the-newo-plugin).
- **Claude:** Customize → Connectors → **+** → **Add custom connector**, the same address, no
  authentication.
- A **work** ChatGPT account often has custom MCP servers turned off by its administrator. Use a
  personal account or the Claude desktop app.

**How access works today.**
- The plugin gets access to an agent **that it created itself** (`create_agent`). The access is
  tied to a *job id* that stays in that chat's history. **It lasts 180 days.**
- To keep working on that agent, continue **in the same chat**. In a new chat the assistant does
  not know the job id. If it calls `create_agent` again, the owner gets a second, new agent.
- **Agents created another way** (in the Newo portal, Voice Creator or by a partner) cannot be
  connected to a browser chat yet. Never ask the owner to paste an API key into the chat. Options
  until sign-in arrives (see D):
  - use a terminal assistant (A);
  - connect the agent to Knowledge Studio for knowledge work (C);
  - make setting changes in the Newo portal.

## C. Newo Knowledge Studio

- **What it is:** an external knowledge base and search service for Newo agents and other voice
  and chat platforms. It is at https://app.knowledge.newo.ai and you sign in with Google.
- **Connect an existing Newo agent:** https://app.knowledge.newo.ai/connect-newo-agent (add
  `?idn=<customer_idn>` to prefill). The owner types the agent's API key into that form only; the
  key goes straight to Newo and is never shown again.
- **MCP server:** Knowledge Studio has its own MCP server, `https://app.knowledge.newo.ai/mcp`,
  with tools for:
  - sources;
  - articles;
  - search;
  - search request logs;
  - autotests;
  - versions and publishing.

  Access is granted inside Studio. The exact steps change while the feature is rolling out: follow
  the instructions Studio shows, or ask Newo support.

## D. Newo Customer MCP server (planned)

Newo is building an MCP server for customer accounts with sign-in through a Newo account (OAuth),
so no API key or job id is needed. The planned tools cover:
- accounts and conversations;
- logs;
- project versions and files;
- activating a version.

Until it is published, use A, B or C. This page will be updated when it ships.

## Secrets: the short version

- Keys and passwords are typed by the person into `.env`, the Newo portal, or a Newo form. Never
  into a chat, an issue or a commit.
- Never display the value of a setting whose name contains `api_key`, `auth_header`, `token`,
  `password`, `secret` or `key`. Say "set" or "empty".
- If a key was exposed, tell the person; Newo support can replace it.
