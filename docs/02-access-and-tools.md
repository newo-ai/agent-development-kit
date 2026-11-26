# Access and tools

How an AI assistant reaches a Newo account, and what to tell a person so they can give you access
safely.

## Which path

Do not ask the person to choose a tool. Pick it from this table, say which one you use, and go.

| Task | Use | Section |
|---|---|---|
| Find the account and its IDN (the account check) | the **Newo Customer MCP** (`get_customers`) **(to confirm)** | [D](#d-newo-customer-mcp-server) |
| Create a new agent from a website or Google Maps link | the MCP (`create_customer`, then `get_run`) **(to confirm)** | [D](#d-newo-customer-mcp-server) |
| Read conversations and logs | the MCP **(to confirm)** | [D](#d-newo-customer-mcp-server) |
| Read and change project files, versions; activate a version. Project files include NAF code: rule 6 and [04](04-naf-change-policy.md) apply | the MCP **(to confirm)** | [D](#d-newo-customer-mcp-server) |
| A practice chat with the agent (sandbox) | the MCP **(to confirm)** | [D](#d-newo-customer-mcp-server) |
| Read and change settings (attributes) | the MCP **(to confirm)** | [D](#d-newo-customer-mcp-server) |
| The knowledge base | the MCP **(to confirm)**; search debugging in Knowledge Studio | [D](#d-newo-customer-mcp-server), [C](#c-newo-knowledge-studio) |
| Connector settings | the MCP **(to confirm)** | [D](#d-newo-customer-mcp-server), [08](08-connector-settings.md) |
| Saved `newo test` files and CI | the **Newo CLI**; sign in with `newo login` | [A](#a-terminal-assistants) |
| Export or backup of an agent | the CLI; sign in with `newo login` | [A](#a-terminal-assistants) |
| Work without a sign-in (scripts, automation) | the CLI or the HTTP API with an API key; key sign-in is deprecated, use it only where `newo login` is refused | [A](#a-terminal-assistants) |
| An agent the older Newo plugin created in that same chat | the older **Newo plugin** | [B](#b-the-older-newo-plugin) |
| Phone numbers, porting, SIP allowlist | Newo only: [draft-support-request](../skills/draft-support-request/SKILL.md) | [support](support/README.md) |
| Edit a scenario card | neither: the person, by hand in the Workflow Builder ([SOP](sop/edit-a-scenario.md)) | [05](05-scenarios.md) |

MCP rows: checked against the live tool list on: **(to confirm)**. Until a date is here, treat each
MCP row as a plan, not a fact. Section [D](#d-newo-customer-mcp-server) lists what the server is
known to cover. After connecting, the server's own tool list is the source of truth: if a row's
tool is missing, say so and use the CLI for that task.

- The MCP is the default. Use the CLI only for saved `newo test` files, CI, export or backup, or
  when the MCP has no tool for the task. Then set it up for that task: the person signs in with
  their Newo account with `newo login` ([SOP: sign in to the CLI](sop/sign-in-cli.md)).
- If an MCP tool for a row fails, say so, try once more, then follow
  [get-unstuck](../skills/get-unstuck/SKILL.md).

## A. Terminal assistants

**Sign-in.** The person signs in to the CLI with their Newo account in the browser; no API key
(the person's steps: [SOP: sign in to the CLI](sop/sign-in-cli.md)):
- `newo login` opens the browser and keeps the session on this computer. EU accounts
  (app.eu.newo.ai): `NEWO_BASE_URL=https://app.eu.newo.ai newo login`, and the same
  `NEWO_BASE_URL` line in the folder's `.env` (from the CLI's `newo-setup` skill, 5.4.1).
- `newo auth status` says, offline, whether the person is signed in: exit 0 yes, exit 1 run
  `newo login` first.
- `newo customer switch <idn>`, run in the agent's folder, checks that the sign-in can open the
  account and saves it in that folder's `.env` (`NEWO_DEFAULT_CUSTOMER`). One agent, one folder,
  one account: see the [folder layout](../README.md#set-up).
- **A key in `.env` (or in the shell) turns the browser login off.** Signing in with a key is
  deprecated. Use one only where the browser login is refused: a viewer or contractor role, or an
  account with a signed BAA. The key steps are in the SOP; never ask for a key in a chat.

Then run the [setup check](setup-check.md).

**The API.** The HTTP API takes an API key (the key steps: [SOP](sop/sign-in-cli.md)).
- Base URL: `https://app.newo.ai`.
- Exchange the key for a 15-minute token:
  ```bash
  curl -s -X POST https://app.newo.ai/api/v1/auth/api-key/token \
    -H "x-api-key: $NEWO_API_KEY" -H "accept: application/json"
  ```
- Send `Authorization: Bearer <access_token>` with every request. On 401 or 403, get a new token
  and retry once.
- First call of every session, and again before every change: `GET /api/v1/customer/profile`.
  If the agent has a `build-notes.md`, check that its `idn` equals `Account idn` there; otherwise
  say the account's name and `idn` back and get a "yes" once per session.
- Full reference: [reference/api.md](../reference/api.md) (Flow Designer V2) and
  [reference/api-v1.md](../reference/api-v1.md) (old designer, V1).
- Connector settings: [08-connector-settings.md](08-connector-settings.md). The CLI's `newo push`
  does not change them.

**The CLI.** `npm i -g newo`, version 5.4.1 or later (needs Node.js 22.12 or later). Do not run
`newo init` inside `work/`: it writes its own assistant instructions and skills there, which
compete with the ADK's. Create the agent's folder and run `newo customer switch <idn>` there; the
root `.gitignore` already ignores `work/` and `.env`. The CLI reads the `.env` of the folder you
run it in, so run every command there.
Useful commands:
- `newo profile` — which account this folder opens; run it before every change.
- `newo pull` / `newo push` — download / upload the projects and the customer attributes (the
  agent's code and settings); works for Flow Designer V2.
- `newo sandbox` — test chat.
- `newo test <scenario.yaml>` — scripted chat tests.
- `newo logs --session-id <id>` — the logs of one conversation.
- `newo session <id> --json` — one conversation's transcript.
- `newo conversations` — every transcript of the account, with no limit: slow on a busy agent and
  full of callers' personal data. For one conversation use `newo session`.

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
  [agent setup guide, "Connect the Newo plugin"](assistant-guide.md#connect-the-newo-plugin).
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
- **Debugging with it:** the search-debug loop and the tool names are in
  [debugging/search-debug.md](debugging/search-debug.md#4-the-same-loop-through-the-knowledge-studio-mcp-server);
  Studio problems in [debugging/studio-troubleshooting.md](debugging/studio-troubleshooting.md).

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
- **Which clients work today:** ChatGPT and Claude (web, desktop, mobile), and Claude Code and
  Codex in the terminal. The terminal clients sign in through a local callback: the client is
  registered as a Native application with the callback `http://localhost:8765/callback`, and the
  connection commands below use port 8765. Terminal assistants that prefer a key can still use
  [A](#a-terminal-assistants).

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
  A member who is not an Owner sees **Add custom connector** greyed out, with the note "Ask an
  organization owner to add this for your team" (seen on 13 November 2026). Do not look for a way
  around it: ask the Owner.
- **In a chat:** **+** → **Connectors** → turn it on.
- Authorization settings cannot be edited later: remove the connector and add it again.

**Claude Code and Codex** (terminal clients; the local callback listens on port 8765):
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
