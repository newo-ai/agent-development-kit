# The Newo agent as an MCP client

The Newo platform can connect an account to **another system's MCP server**: a CRM, a booking
system, a practice or patient management system. The agent then calls that server's tools
during a conversation.

Do not confuse this with the MCP servers **you** (the coding assistant) connect to:
- the Newo plugin;
- Knowledge Studio;
- the planned Newo Customer MCP server.

Those are described in [02-access-and-tools.md](../02-access-and-tools.md). This page is about the
**agent** using an external MCP server while it talks to a caller.

## 1. Connect the MCP server to the account

In the Newo portal: Builder → Integrations → **MCP Integration Service** → Add connector.

| Field | Value |
|---|---|
| Connector title and **idn** | the idn is how code refers to this server, for example `pms` |
| URL | the MCP server's address from the vendor's documentation |
| Authorization | `headers` (key-value pairs), `jwt` (a bearer key) or `oauth2` |

- **OAuth 2.0:**
  1. The person starts the authorization from the connector and signs in to the other system to
     give consent.
  2. The connector status changes from `auth_required` to `success`.
  3. If the vendor supports neither dynamic client registration nor client metadata documents,
     the vendor gives a client ID and secret for the connector.
- **Keys and secrets are entered by the person in the portal.** Never through a chat.
- Newo also has a few **platform-wide MCP servers** managed by Newo. They are not for
  customer-specific integrations: use a connector.

## 2. See what the server offers

Before you design the conversation, read the vendor's documentation of the MCP server's tools:
- names;
- input schemas;
- which tools only read and which change data.

Plan to use only the tools the conversation needs.

## 3. Call it during the conversation (rolling out)

Today an MCP connector is used from **skill code**. The skill runs a structured generation and
lists the connector:

```jinja
{% set result = GenStructured(
    blocks=[{"role": "user", "content": "..."}],
    tools=[{"type": "mcp", "server_idn": "pms", "allowed_tools": ["find_free_slots"]}],
    toolChoice="required") %}
```

- `allowed_tools` limits the call to the tools you name. **Always set it**, so the agent cannot
  reach tools it does not need (for example deleting records).
- The older form `mcpIdns=["pms"]` also works. Do not use the same idn in both forms.

Because this is code, follow the ladder:
1. Write the skill in a **separate project** or in your own flow, not inside NAF. If it must live
   in NAF, follow [04-naf-change-policy.md](../04-naf-change-policy.md).
2. If the system also has a plain HTTP API, the no-code conversation tools
   ([http-rest.md](http-rest.md#4-conversation-tools-any-http-api-during-the-call)) may be enough.

**(Planned)** A no-code action that calls an MCP tool from the conversation tools setting, in the
same way as `send_webhook`. This page will be updated when it ships.

## 4. Two-step pattern: look up, then act after confirmation

1. **Look up** (read-only tool): the agent says "let me check", calls the read tool, and tells
   the caller the result. For example, free slots tomorrow afternoon for Dr. X.
2. **Confirm:** the agent repeats the exact details (who, what, when) and waits for a clear yes.
3. **Act** (write tool): the agent calls the booking tool once, with an idempotency key if the
   server supports one. It confirms only what the server returned.
4. **Fail safely:** on a timeout or an error, say so honestly, and offer a callback, a message or
   a transfer to a person.

Worked example: [example-pms-appointments.md](example-pms-appointments.md).

## 5. Test and debug

- Use the vendor's sandbox or test account.
- Run a sandbox chat through both steps ([testing](../testing/README.md)).
- Read the logs of that conversation: the tool call, its arguments, the response, the time it
  took.
- Then make a real test call. Voice adds latency: check that the "let me check" phrase covers the
  wait.
