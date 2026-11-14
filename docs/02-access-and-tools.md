# Access and tools

How an AI assistant reaches a Newo account, and what to tell a person so they can give you access
safely.

## Which path

| The person uses | You reach Newo through | Section |
|---|---|---|
| Claude Code, Codex, Cursor or another assistant with a terminal | the Newo HTTP API or the Newo CLI, with the account's API key in an environment variable | [A](#a-terminal-assistants) |
| ChatGPT or Claude in the browser (or the Claude apps) | the **Newo Customer MCP server**: the person signs in with their Newo account | [D](#d-newo-customer-mcp-server) |
| ChatGPT or Claude, for an agent the older Newo plugin created in that same chat | the older **Newo plugin** (a custom MCP server without sign-in) | [B](#b-the-older-newo-plugin) |
| Any assistant, for knowledge only | **Newo Knowledge Studio** | [C](#c-newo-knowledge-studio) |

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
- Connector settings: [08-connector-settings.md](08-connector-settings.md). The CLI's `newo push`
  does not change them.

**The CLI.** `npm i -g newo`, then run `newo init` in an empty folder. It writes instructions and
skills for coding assistants, an empty `.env` and a `.gitignore`. Useful commands:
- `newo pull` / `newo push` — agent code; works for Flow Designer V2.
- `newo sandbox` — test chat.
- `newo test <scenario.yaml>` — scripted chat tests.
- `newo logs --session-id <id>` — the logs of one conversation.
- `newo conversations` — transcripts.

The CLI masks secrets in its output. Changing framework (NAF) code needs explicit confirmation
(`NEWO_UNRESTRICTED`, default off); see [04-naf-change-policy.md](04-naf-change-policy.md).

## B. The older Newo plugin

For browser assistants, use the Newo Customer MCP server ([D](#d-newo-customer-mcp-server)). This
older plugin stays for agents it created with `create_agent`, while you work in the same chat.

ChatGPT and Claude in the browser cannot call APIs by themselves. The **Newo plugin** is a custom
MCP server without sign-in that gives them tools.

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
- **Agents created another way** (in the Newo portal, Voice Creator or by a partner): use the Newo
  Customer MCP server (D). Never ask the owner to paste an API key into the chat.

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

## D. Newo Customer MCP server

An MCP server for customer accounts. The person signs in with their Newo account (OAuth), so no
API key or job id is needed. It reaches every account that Newo user can open, however the agent
was created. It covers:
- accounts and conversations;
- logs;
- project versions and files;
- activating a version.

After connecting, list the server's tools and their descriptions: they are the source of truth for
what it can do.

**Status (13 November 2026):** live in production.

| Setting | Value |
|---|---|
| Server URL | `https://api.newo.ai/api/v1/customer-mcp` |
| Authentication | OAuth, sign-in at `auth.newo.ai` |
| OAuth client ID | `g2t0mUwvyASY6OC9F76xvNBSFfZjSyfe` (public, not a secret) |
| Client secret | empty |
| Scopes | `openid offline_access` |

- Newo's sign-in does not support automatic client registration. In every client, choose the
  option to use your own OAuth client and enter the client ID above.
- **Which clients work today:** ChatGPT and Claude (web, desktop, mobile). The client ID does not
  yet accept a sign-in that returns to a local address (`localhost`), which Claude Code and Codex
  use. Their sign-in ends with "Callback URL mismatch". Until Newo adds this, terminal assistants
  use [A](#a-terminal-assistants).

**ChatGPT (web).**
1. Open https://chatgpt.com/plugins (or **Plugins** in the menu on the left).
2. Click the black **Add** button in the top right corner → **Add custom MCP server**. Not
   **Create plugin** and not **Upload plugin archive**. Newo is not in the plugin search.
3. Name: `Newo`. Connection: **Server URL**, the URL above. Authentication: **OAuth**.
4. **Advanced OAuth settings** → enter the client ID by hand, leave the secret empty, scopes
   `openid offline_access`. Keep everything else as ChatGPT filled it in.
5. Tick **I understand and want to continue** and create the server. It stays private to you and
   is not published to the store.
6. Click **Connect** and sign in on the Newo page with the Newo account of the agent.
7. In a chat, type `@` and pick Newo.

- If there is no **Add** button, the person is not signed in to ChatGPT.
- A **work** ChatGPT account often has custom MCP servers turned off by its administrator. Use a
  personal account or Claude.
- ChatGPT asks for confirmation before tools that are not marked read-only.
- **In a chat with a custom MCP server turned on, ChatGPT does not open web pages.** Its page fetch
  ends with `DisabledError`, also for this repository (seen on 13 November 2026; the same link
  opens in a chat without the server). Put the rules the assistant needs into the first message,
  or read the page in a separate chat and paste the text.
- The ChatGPT desktop and mobile apps are not documented by OpenAI for this yet.

**Claude (web, desktop, mobile).** The connector belongs to the account. Add it once on the web
and it works in every Claude app.
- **Personal plan:**
  1. Customize → Connectors → **+ Add** → **Add custom connector**.
  2. Name `Newo` and the URL above → **Continue** → Authentication: **Sign in now**.
  3. **Advanced** → OAuth client: **Use your own OAuth client** → the client ID → **Add** →
     **Connect**, then sign in on the Newo page.
  4. The Free plan allows one custom connector.
- **Team or Enterprise:** the Owner adds it in Organization settings → Connectors → **Add** →
  **Custom** → **Web**, the same way. Members then press **Connect** in Customize → Connectors.
- **In a chat:** **+** → **Connectors** → turn it on.
- Authorization settings cannot be edited later: remove the connector and add it again.

**Claude Code and Codex** (after Newo enables `localhost` sign-in; until then use A):
```bash
claude mcp add --transport http -s user --client-id g2t0mUwvyASY6OC9F76xvNBSFfZjSyfe --callback-port 8765 newo https://api.newo.ai/api/v1/customer-mcp
```
```bash
codex mcp add newo --url https://api.newo.ai/api/v1/customer-mcp --oauth-client-id g2t0mUwvyASY6OC9F76xvNBSFfZjSyfe
```

## Secrets: the short version

- Keys and passwords are typed by the person into `.env`, the Newo portal, or a Newo form. Never
  into a chat, an issue or a commit.
- Never display the value of a setting whose name contains `api_key`, `auth_header`, `token`,
  `password`, `secret` or `key`. Say "set" or "empty".
- If a key was exposed, tell the person; Newo support can replace it.
