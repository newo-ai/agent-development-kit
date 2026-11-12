# The Newo agent as an MCP client

The Newo platform can connect an account to **another system's MCP server**: a CRM, a booking
system, a practice or patient management system. The agent then calls that server's tools
during a conversation.

Do not confuse this with the MCP servers **you** (the coding assistant) connect to:
- the Newo plugin;
- Knowledge Studio;
- the Newo Customer MCP server.

Those are described in [02-access-and-tools.md](../02-access-and-tools.md). This page is about the
**agent** using an external MCP server while it talks to a caller.

## 1. Connect the MCP server to the account

In the Newo portal: Builder → Integrations → **MCP Integration Service** → Add connector. One
connector = one external MCP server.

| Setting | Value |
|---|---|
| Connector title and **idn** | the idn is how code refers to this server, for example `pms`. Format `[a-zA-Z_][a-zA-Z0-9_]*` |
| `url` | the MCP server's address from the vendor's documentation, for example `https://mcp.example.com/mcp` |
| `auth_type` | `none`, `headers` (key-value pairs), `jwt` (a bearer key) or `oauth2` |
| `oauth2_scopes` | for `oauth2`: optional list of scopes to request; default `[]` |

- **Keys and secrets are entered by the person in the portal.** Never through a chat.
- Newo also has a few **platform-wide MCP servers** (Available MCP) managed by Newo for shared
  integrations. They are not for customer-specific integrations: use a connector. A connector
  with the same idn as a platform-wide server takes precedence.

## 2. OAuth 2.0 authorization

With `auth_type = oauth2`, the business owner signs in to the other system once to give consent.
The flow runs through a command and three events.

### Start

The command `oauth2_start` on the connector. It does **not** return the link and does not wait;
the results arrive as events.

NSL:
```jinja
{{ SendCommand(integrationIdn="mcp", connectorIdn="pms", commandIdn="oauth2_start") }}
```

Python:
```python
import newo

def main():
    newo.commands.send(integration_idn="mcp", connector_idn="pms", command_idn="oauth2_start")
```

### Events

Handle them in the flow that started the authorization.

| Event | Arguments | What to do |
|---|---|---|
| `oauth2_link` | `authorization_url`, `expires_at` | Give the person the URL to open in a browser. They sign in to the other system and approve. |
| `oauth2_success` | none | The connector is ready. Its authorization status becomes `success`. |
| `oauth2_error` | `code`, `reason`, `error_type` | Tell the person what went wrong. Restart if it makes sense. |

Example `oauth2_link` arguments:
```json
[
  {"name": "authorization_url", "value": "https://auth.example.com/authorize?client_id=example&state=example"},
  {"name": "expires_at", "value": "2026-10-09T12:15:00+00:00"}
]
```

### Errors

| `code` | `error_type` | Typical cause |
|---|---|---|
| `400` | `bad_request` | missing authorization code or issuer mismatch in the callback; or the provider needs a pre-registered client (below) |
| `403` | `forbidden` | the person or the provider denied access |
| `409` | `conflict` | the connector is not an `oauth2` connector |
| `410` | `gone` | the person opened the link after it expired: start again |
| `502` | `bad_gateway` | discovery, client registration or code exchange failed at the provider |
| `504` | `gateway_timeout` | the provider did not answer in time |
| `500` | `server_error` | an unexpected error |

### Providers that need a pre-registered OAuth client

Newo registers itself with the provider automatically when the provider supports it. If the
provider supports neither dynamic client registration (DCR) nor client metadata documents (CIMD),
`oauth2_error` says so:

```json
[{"name": "code", "value": "400"}, {"name": "error_type", "value": "bad_request"},
 {"name": "reason", "value": "Authorization server supports neither CIMD nor DCR; configure client_id and client_secret from a pre-registered OAuth2 client"}]
```

Then:
1. The business (or its IT) registers an OAuth app in the other system and gets a client ID and
   client secret. The callback (redirect) address has the form
   `https://<newo environment>/api/v1/mcp/oauth2/callback`; the connector shows its Redirect URL,
   or ask Newo support for the exact one.
2. The person enters the client ID and secret in the connector's settings in the Newo portal:
   `oauth2_client_id` and `oauth2_client_secret`. **Not in a chat.**
3. Start `oauth2_start` again.

The same values can be set from code (`newo.connectors.set(integration_idn="mcp",
connector_idn="pms", field="oauth2_client_id", value=...)`). Never hard-code a secret in a skill:
the portal is the place for it.

## 3. See what the server offers

Read the vendor's documentation, then read the live catalog of tools from the agent's runtime.

NSL `GetMCPTools`, or `newo.mcp.get_tools` in Python:

```jinja
{% set tools = GetMCPTools(mcpIdn="pms", toolNames=["find_free_slots", "create_appointment"], query="slot") %}
```

```python
from dataclasses import asdict
import newo

def main():
    tools = newo.mcp.get_tools(mcp_idn="pms", tool_names=["find_free_slots"], query="slot")
    return [asdict(t) for t in tools]
```

Each tool comes back with `name`, `description`, `input_schema`, `output_schema` and
`annotations`. For example, `{"readOnlyHint": true}` marks a tool that only reads.

Rules:
- Without `toolNames`, you get every tool of the server. An empty list `[]` returns nothing.
- Names match exactly. An unknown name fails the whole call.
- `query` is a case-insensitive filter on names and descriptions.
- An unknown server, missing authorization or a failing server makes the action fail. It does
  not return a partial list.
- `GetMCPTools` only lists the tools; it does not call them.

## 4. Call it during the conversation

An MCP server is used from **skill code**: a structured generation that lists the server as a
tool. Newo does not plan a no-code `call_mcp` action in the conversation tools setting for now.
For a plain HTTP API, the no-code conversation tools
([http-rest.md](http-rest.md#4-conversation-tools-any-http-api-during-the-call)) remain an option.

NSL:
```jinja
{% set result = GenStructured(
    blocks=[{"role": "user", "content": "..."}],
    tools=[{"type": "mcp", "server_idn": "pms", "allowed_tools": ["find_free_slots"]}],
    toolChoice="auto") %}
```

Python:
```python
import newo
from newo.models import GenerationBlock, MCPTool

def main():
    result = newo.generation.generate_structured(
        blocks=[GenerationBlock(role="user", content="Find free slots tomorrow afternoon")],
        tools=[MCPTool(server_idn="pms", allowed_tools=["find_free_slots"])],
        tool_choice="auto",
    )
    return result.text
```

- **Always set `allowed_tools`** to exactly the tools this step needs. Omitting it, or `None`,
  allows every tool of the server. `[]` disables the server. Unknown names fail the call.
- Each server may appear once per call. MCP entries can be mixed with ordinary `function` tools
  and `web_search`.
- `toolChoice`:
  - `auto` (default): the model decides;
  - `required`: a tool must be used;
  - `none`: no tools at all.
- The older form `mcpIdns=["pms"]` (Python `mcp_idns`) still works, without tool filtering. Do not
  put the same idn in both forms.
- To narrow a large catalog, combine the two: `get_tools` with `query`, then
  `MCPTool(server_idn="pms", allowed_tools=[t.name for t in tools])`.

Because this is code, follow the ladder:
1. Write the skill in a **separate project** or your own flow, not inside NAF. If it must live in
   NAF, follow [04-naf-change-policy.md](../04-naf-change-policy.md).
2. Keep reading tools and writing tools in **separate** generation steps, so writing happens only
   after the caller confirms (section 5).

## 5. Two-step pattern: look up, then act after confirmation

1. **Look up** with a read-only tool. The agent says "let me check", calls the tool and tells the
   caller the result, for example free slots tomorrow afternoon for Dr. X.
2. **Confirm.** The agent repeats the exact details (who, what, when) and waits for a clear yes.
3. **Act** with a write tool, in its own step with `allowed_tools` set to that one tool. The agent
   calls it once, with an idempotency key if the server supports one, and confirms only what the
   server returned.
4. **Fail safely.** On a timeout or an error, the agent says so honestly and offers a callback, a
   message or a transfer to a person.

Worked example: [example-pms-appointments.md](example-pms-appointments.md).

## 6. Test and debug

- Use the vendor's sandbox or test account, authorized with `oauth2_start` like a real one.
- Check the catalog with `GetMCPTools` first: it fails clearly if the authorization is missing.
- Run a sandbox chat through both steps ([testing](../testing/README.md)).
- Read the logs of that conversation: the tool call, its arguments, the response, the time it
  took.
- Make a real test call. Voice adds latency: check that the "let me check" phrase covers the wait.
