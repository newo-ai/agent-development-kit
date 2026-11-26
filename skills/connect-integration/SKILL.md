---
name: connect-integration
description: Connect a named system that has a Newo integration (a calendar, CRM, dental or medical practice system, hotel PMS, POS or reservation system, ManyChat, Telegram, TrackB) to a Newo agent. The assistant does the Newo side through the Newo MCP, walks the partner through the vendor's side one step at a time, tests, and drafts a support request only when Newo must act. Use when a partner says "connect Housecall Pro", "integrate with Dentrix", "hook up Square", "set up GoHighLevel", or names any system listed in docs/integrations/vendors/README.md.
---

# Connect a named integration

Stage: [02-build](../../delivery/02-build/README.md), or any time later. Produces a working
integration that passed its test, or a drafted request to Newo. Note the change in
`build-notes.md` when the agent has one.

The steps for each system are on its vendor page:
[docs/integrations/vendors/README.md](../../docs/integrations/vendors/README.md). The system has no
page there? It has no Newo integration: use the generic mechanisms in
[docs/integrations/README.md](../../docs/integrations/README.md#pick-the-mechanism).

## 1. Find the system

1. Look up the system the partner names in the vendor index. Match loosely ("HCP" is Housecall
   Pro, "GHL" is GoHighLevel, "Open Dental" is OpenDental).
2. Ask only if two rows match (for example "Dentrix" when the practice may run the cloud
   edition, or a restaurant that could connect directly or through Mozrest).
3. Read the vendor page in full before you say anything about plans, steps or limits.

## 2. Confirm the account

Run `get_customers`, say the account's name and IDN back, and get one "yes" per session
([AGENTS.md, section 4](../../AGENTS.md#4-how-you-reach-the-platform)). Read `build-notes.md`
first if it exists and compare its `Account idn`.

## 3. Read the live Newo side

1. Call `get_integrations` and find the integration for this system. Use the setting names it
   returns. If they differ from the vendor page, follow the platform, tell the partner, and mark
   the difference for a fix to this repository
   ([rule 9](../../AGENTS.md#3-rules-always)).
2. Read the agent's current values of the settings the page names, and keep them so they can be
   put back. Show a secret setting as "set" or "empty", never its value.
3. Check what the page says must exist first: a plan in the vendor, an admin user, a test or
   sandbox account in the vendor. Missing? Stop and tell the partner what to get.
4. **Health data.** For a dental, medical or other patient system (the PMS rows in the index),
   apply [Health data](../../docs/integrations/README.md#health-data) before anything else:
   compliance agreed with the owner and Newo, identity checks in the conversation, and no health
   data in chats, logs or files.

## 4. Do the Newo side

Most integrations are a project added to the agent from a module, then settings, then
**Publish All**. For each change:

1. Show it in plain words: what changes, the old value, the new value. Wait for a clear "yes".
2. Make it through the MCP. If the MCP cannot make that change (for example, adding a project
   from a module **(to confirm with the platform team: which MCP tool adds a project)**), give
   the partner the exact steps from the vendor page to do it in the Builder, one at a time.
3. Read the value back after the change.

Keys, tokens, secrets and one-time codes are typed by the partner into the Newo Builder or the
vendor's own screens. Never ask for them in the chat. If the partner pastes one anyway, do not
repeat it, and ask them to replace it in the vendor ([rule 4](../../AGENTS.md#3-rules-always)).

Never delete a project, connector, setting or scenario. To remove one, the partner asks Newo
support ([rule 2](../../AGENTS.md#3-rules-always)).

## 5. Walk the partner through the vendor's side

Follow "Partner does in <vendor>" on the page, one step at a time:

1. Give one step, with the exact menu names from the page.
2. Wait until the partner says it is done, or says what they see instead.
3. Then the next step. Where the page has a Newo step in between (for example, pasting the code
   the vendor shows), say where in the Builder it goes.

A step the page does not describe ("the exact menu path is not stated") is a step to work out
with the partner from the vendor's own help; say so, do not invent menu names.

## 6. Test

1. **Test mode first** ([rule 10](../../AGENTS.md#3-rules-always)): read
   `project_attributes_setting_test_mode`, explain it, and ask whether the account already takes
   real calls or chats. Most integrations write real bookings, orders and records.
2. Prefer the vendor's test or sandbox account, or a test location, staff member or calendar.
3. A practice chat: send the vendor page's test phrases with `send_message`, read the reply and
   the conversation's events with `search_conversations`. Check that the tool ran, not only what
   the agent said.
4. The check on the vendor page: for example, the test booking appears in the vendor's calendar,
   then the cancellation removes it.
5. For anything critical (booking, cancelling, ordering), run the test three times
   ([run-tests](../run-tests/SKILL.md)).
6. Clean up: cancel test bookings and orders in the vendor, with a "yes" for each.

## 7. When only Newo can help

Draft a request with [draft-support-request](../draft-support-request/SKILL.md), to
`partner-support@newo.ai`, when:

- the page's "Needs Newo" section applies, or the integration is missing from
  `get_integrations` for this account;
- a step needs something enabled on the account, or a change the MCP and the Builder both refuse;
- the same step failed twice the same way.

Fill it with the system, the step, what you saw and when (UTC). No keys, no callers' data.
Show it and hand it to the partner; never send it.

## 8. Wrap up

Tell the partner what changed (old and new values), how to undo it, what to watch in the first
real conversations, and which test bookings were cancelled. Found a mistake on the vendor page?
Propose a fix with [github-workflow](../github-workflow/SKILL.md).

## Done when

- The integration passed its test (step 6) and test data was cleaned up, or
- the partner has a drafted request to Newo (step 7) and knows where to send it.
