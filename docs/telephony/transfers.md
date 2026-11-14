# Transfers to people

The agent can transfer a call to a person: a manager, the front desk, a department.

## Settings

| Setting | Purpose |
|---|---|
| `project_attributes_setting_transfer_call_enabled` | turns transfers on |
| `project_attributes_setting_transfer_call_phone_numbers` | where to transfer |
| `project_attributes_setting_transfer_call_criteria` | when to transfer (in plain words) |
| `project_attributes_setting_transfer_call_destination_format` | `full_number`, or `short_code` for internal extensions of a PBX |
| `project_business_working_hour_escalation_phone`, `project_business_non_working_hour_escalation_phone` | escalation numbers by working hours |
| `project_attributes_setting_custom_transfer_call_enabled` | a custom transfer handled by your own logic (advanced) |

Read the full descriptions in the
[attribute reference](../../reference/attributes/index.md) before changing
them.

## How a transfer works

- **Twilio or Telnyx number:** the call goes to the transfer number over the phone network.
- **SIP:** the transfer uses SIP REFER. The business's PBX must allow the agent's extension to
  transfer, and to dial out in E.164 format for outside numbers.
- **WebSocket voice API:** Newo calls your webhook, then sends a `transfer` frame. See
  [websocket-voice-api.md](websocket-voice-api.md#7-call-transfer).

## Rules

- **Billing:** transfers may stay off until billing is set up on the account. International
  transfers are off by default.
- **Test** one transfer in each direction you configured, during a time when someone answers.
- If transfers happen too early or too late, adjust the criteria text before anything else.
