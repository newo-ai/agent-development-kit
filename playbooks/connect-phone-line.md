# Playbook: connect the business phone line

Goal: callers who dial the business's existing number reach the agent (always, after hours, or
when nobody answers), and the agent can transfer calls back to people.

There are two ways. Ask the owner which phone system they use (a mobile or landline carrier, or a
business phone system such as RingCentral, Nextiva, 8x8, Zoom Phone, Dialpad, Genesys, or their
own PBX), then pick one:

| Way | When | Who changes what |
|---|---|---|
| **A. Call forwarding** to the agent's number | almost always; the simplest | the owner (or you, with their access) changes forwarding in their phone system; nothing changes in Newo |
| **B. The agent registers as a SIP extension** of the business phone system | the business wants the agent inside its PBX (internal transfers, its own caller ID) | both sides: an extension in the PBX, the SIP settings in Newo, and network access |

Do not change both at once. Every step below needs the owner's "yes"; changes to a phone line
affect real callers immediately.

## 1. Read the agent's phone setup

1. The agent's number: the read-only attribute for the agent's phone number (see
   [Finish the configuration](finish-configuration.md)), or `GET /api/v1/integrations`, the
   `newo_voice` integration, its connector `newo_voice_connector`, and the provider and number in
   its settings ([API reference](../reference/api.md#integrations-and-connectors)). Never show `sip_password` or
   keys.
2. Transfers back to people: `project_attributes_setting_transfer_call_enabled`, `..._phone_numbers`,
   `..._criteria`, `..._destination_format` (`full_number`, or `short_code` for internal
   extensions), and the escalation phone numbers for working and non-working hours. Read their
   descriptions in the [attribute reference](../reference/attributes/index.md).

## 2. Way A: call forwarding

Decide with the owner **when** calls go to the agent:
- always;
- after hours (a time-based rule in the phone system);
- when nobody answers within N seconds, or when busy ("conditional" or "no answer" forwarding).
  This is the usual start: people answer first, the agent catches the rest.

Then set it up where the line lives:
- **Mobile or landline carrier:** forwarding codes dialed from the business phone. In most GSM
  networks: `**61*<agent number>**<seconds>#` for "no answer" and `##61#` to cancel. US carriers
  differ (for example Verizon uses `*72` / `*73`; conditional forwarding only in its app or
  portal). Check the carrier's own help page.
- **Business phone systems (RingCentral, Nextiva, 8x8, Zoom Phone, Dialpad, Genesys, ...):**
  forwarding or an answering rule on the user, extension, queue or main number, in their admin
  portal. Many have an API, and some offer an MCP server. If you have the owner's admin access
  through such a tool, you may change the rule yourself after the owner confirms the exact rule;
  otherwise give the owner click-by-click steps for their admin portal.
- Use the agent's number in full international format (E.164, for example `+14155550123`).

Test:
1. Ask the owner to call the business number from another phone and let it ring.
2. Check that a new conversation appeared ([API reference](../reference/api.md#conversations)) and that the agent
   answered.
3. When calls are forwarded, the agent may see the business number instead of the caller's
   number on some systems. Check the caller number in the new conversation; if every caller looks
   like the same person, tell the owner and Newo support.

## 3. Way B: the agent as a SIP extension

Newo connects to the business phone system by **SIP registration** (username and password of an
extension), not by IP trunking.

On the business phone system (owner or their IT, or you with their admin access):
1. Create an extension (SIP user) for the agent.
2. Allow it to transfer calls to other extensions, and to call out in E.164 format if transfers
   to outside numbers are needed.
3. Route calls to it (ring group, queue, after-hours rule).
4. Collect: SIP server host and port, transport (UDP or TCP; say so if TLS is required), the
   extension's username, the caller ID, and whether the system only accepts known IP addresses.

On Newo:
1. The `newo_voice_connector` provider becomes Custom SIP with these values. **Do not ask the
   owner to paste the SIP password into the chat.** Ask Newo support to enter it, or the owner
   to enter it in the Newo portal (Integrations).
2. If the phone system accepts only known IP addresses, ask Newo support for Newo's addresses
   and to allow the business's server on Newo's side.
3. Transfers: set `..._destination_format` to `short_code` when transfers go to internal
   extensions.

Test: an inbound call through the PBX route, an outbound test if the agent calls out, and one
transfer to a person. If the agent does not receive calls, the registration may have failed; Newo
support can check it. There is no public API route that reads registration status, but the
agent's flow is told: Newo sends a `registration_changed` connector event with the arguments
`status` (`registered` or `failed`) and `provider`.

## 4. After it works

- Watch the first real calls ([Review conversations](review-conversations.md)).
- Write down for the owner what was changed in their phone system and how to undo it.
