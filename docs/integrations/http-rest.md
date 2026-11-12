# HTTP and REST integrations (no code)

All of these are settings. Read each setting's full description in the
[attribute reference](https://knowledge.newo.ai/agent-setup/attributes/index.md) before you change
it, ask the person before each change, and test.

## 1. After every conversation: session-ended webhook

After a conversation ends, the agent POSTs a structured result to a URL: a CRM endpoint, a
Zapier or Make webhook, or the owner's server.

| Setting | Purpose |
|---|---|
| `project_attributes_setting_session_ended_webhook_url` | where to send |
| `project_attributes_setting_session_ended_webhook_schema` | which fields to send |
| `project_attributes_setting_session_ended_webhook_auth_header` | the authorization header the receiver expects; entered by the person, never shown |

Test: a sandbox chat or a test call. Then check that the record arrived.

## 2. Calendar appointments

`project_attributes_setting_calendar_event_integration`: `disabled`, `calcom_integration` or
`google_integration`. Connecting a Google account needs the owner to sign in to Google in the
Newo portal. If the `google_calendar` connector is missing or not `running`, the owner connects
it in the portal.

## 3. Booking settings

`project_attributes_setting_booking_*` let the agent check availability and create bookings
through a booking system's HTTP API: URLs, method, headers, request and validation schemas,
confirmation phrases, notifications.

`project_attributes_setting_booking_type` selects the path:

| Value | Path |
|---|---|
| `default` | built-in logic |
| `endpoint` | an HTTP request to your URL |
| `project` | a system event handled by a separate project |
| `custom` | reserved for custom setups |
| `intercom` | an internal event branch |

Industry pages describe ready-made options. Test with test mode on, read the logs with
`levels=error`, and switch test mode off only when the owner approves.

## 4. Conversation tools: any HTTP API during the call

`project_attributes_settings_platform_tools` (JSON) adds tools the agent can use **during** a
conversation.

**Each tool has:**
- `conditions` — when the tool fires. For example, the agent has just said it will check
  availability.
- `useConversationHistory`.
- `action`:
  - `send_webhook` — an HTTP request. Its `query`, `body` and `headers` are schemas the platform
    fills from the conversation;
  - `send_event`.
- `after_actions` (for webhooks) — what happens with a non-empty response:
  - `set_prompt_section` — put the response into the conversation;
  - `send_urgent_message` — say it now;
  - `set_persona_attribute`.

Optional: `conflictPolicy.tag`. When several tools with the same tag fire, only one runs.

Built-in tools (availability check, booking, cancellation and others) use the same structure.
A custom tool with the same key overrides the built-in one.

**Example: check free tables, then book after the caller confirms.** Illustrative values: take the
real URLs and fields from the booking system's API documentation.

```json
{
  "tools": {
    "check_tables_tool": {
      "description": "Checks free tables in the reservation system.",
      "conditions": {
        "agentPromised": {
          "type": "boolean",
          "description": "The agent's latest message says it is checking table availability now."
        }
      },
      "useConversationHistory": true,
      "action": {
        "type": "send_webhook",
        "options": {
          "method": "GET",
          "url": "https://booking.example.com/api/availability",
          "query": {
            "type": "object",
            "properties": {
              "date": {"type": "string", "description": "Date in YYYY-MM-DD"},
              "time": {"type": "string", "description": "Time in HH:MM, 24-hour"},
              "party_size": {"type": "integer"}
            }
          }
        }
      },
      "after_actions": [{"type": "send_urgent_message"}]
    }
  }
}
```

The booking tool follows the same shape, with `POST`, a body schema and a second condition: the
caller explicitly confirmed date, time, party size and name.

Rules:
- Start with one reading tool.
- Validate the JSON before you save it: invalid JSON disables the tools.
- Test in the sandbox, then with a call.
- Check the logs for the request and the response.

Full reference: `project_attributes_settings_platform_tools` in the
[attribute reference](https://knowledge.newo.ai/agent-setup/attributes/4-agent-behavior-advanced.md).

## 5. Email and SMS to callers

| Setting | Purpose |
|---|---|
| `project_attributes_setting_email_send_information_enabled` | allow emails to the caller |
| `project_attributes_setting_sms_send_information_enabled` | allow text messages to the caller |
| `..._allowed_content`, `..._items` | what an email or text may contain |

Text messages are subject to consent and anti-spam rules in many countries; in the US, for
example, A2P 10DLC registration and opt-out handling apply. Make sure the owner knows before
turning them on.
