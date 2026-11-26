---
name: fix-issue
description: Propose one fix for one problem found in an agent's calls - a setting, a knowledge change, or a draft support request to Newo - apply it through the Newo MCP only after the partner's explicit "yes", keep the old value, never delete, then check a few new calls. Script and scenario changes go to the Workflow Builder by hand or to Newo support. Use when a partner says "fix this", "the agent keeps saying X", "the agent gave the wrong price", "change the agent so it...", "apply the fix", "send this to Newo", "write it up for support".
---

# Fix one issue

Stage: [05-operate](../../delivery/05-operate/README.md), "Fixing an issue". This skill can change
a live agent: every change reaches real callers at once and waits for a clear "yes". One change
at a time.

## Before you start

1. **The account.** Name the customer and its IDN from `get_customers` and get a "yes" once per
   session ([setup check, check 3](../../docs/setup-check.md#3-the-right-account)). With a
   `build-notes.md`, compare with its `Account idn`; if they differ, stop.
2. **Test mode.** Read `project_attributes_setting_test_mode` with `get_customer_attribute`.
   Explain it in plain words and follow rule 10 in [AGENTS.md](../../AGENTS.md): on an account
   with real callers, never switch it on.
3. **The problem.** From [review-agent](../review-agent/SKILL.md), or the partner's own words.
   One problem, with at least one session that shows it.

## 1. Confirm the cause

Read one session that shows the problem (`get_session`) and its logs (`search_logs` with that
`session_id`, `levels` `error` and `warning`). Check
[common issues](../../docs/debugging/common-issues.md) and the
[improve-and-fix table](../../playbooks/improve-and-fix.md#1-find-the-cause). Say the cause in
one sentence. **Not sure of the cause:** don't guess a change; go to step 2, "Support request".

## 2. Choose the lowest level

The ladder in [docs/03](../../docs/03-configure-and-customize.md#the-ladder-always-try-the-lowest-step-first):

| Level | How | Who applies it |
|---|---|---|
| **Setting** (hours, prices, FAQ, greeting, transfers) | `search_customer_attributes`, then `get_customer_attribute` for the full current value. Meaning and format: [attribute reference](../../reference/attributes/index.md) (search the index, never read whole files) | this skill, `set_customer_attribute_value` |
| **Knowledge** | a new topic: `create_knowledge_base_topic` ([docs/06](../../docs/06-knowledge.md)). When the knowledge source is `akb_studio`, changes go through Knowledge Studio instead | this skill (new topic) or the partner |
| **Scenario** (how the conversation runs) | the exact text to type in the Workflow Builder, as in [adjust-scenarios](../adjust-scenarios/SKILL.md) | the partner, by hand |
| **Script, skill code, NAF, platform bug** | a support request | Newo support |

**Assumption:** the MCP has no tool to edit an existing knowledge topic, and replacing one means a
delete. Give the partner the new text to change it in the portal.

**Support request.** Fill the [bug report](../../docs/support/README.md#bug-report): account
IDN, channel, time (UTC), session ids, expected, what happened, the relevant log lines without
personal data, how often, impact. It goes to Newo support or as an email draft in the partner's
mailbox; never send it yourself. Never in a public issue.

## 3. Show the change and wait for "yes"

In plain words, then the details:

- what the agent will do differently ("Callers asking for Sunday hours will hear you're
  closed");
- the setting idn, the **old value** and the **new value**;
- where the old value is saved: `work/<agent-name>/changes/YYYY-MM-DD-<setting>.txt`, and a row
  in "Changes made" of `weekly-review.md`;
- whether it needs a publish (below), and that it reaches real callers at once. Agree on a quiet
  hour if the partner wants one.

Wait for a clear "yes" for this exact change. Save the old value first, then apply.

## 4. Apply and read back

`set_customer_attribute_value`, then `get_customer_attribute`: the stored value must be the new
one, byte for byte. If not, say so and put the old value back (after a "yes").

**Publish.** Settings compiled at start (working hours, time zone, languages, voice) need a
publish of `naf` ([docs/03, "When a change takes effect"](../../docs/03-configure-and-customize.md#when-a-change-takes-effect)).
**Assumption, to confirm:** whether a change through the MCP reaches the agent without one. This
skill does not publish. If the old behavior is still there after 5 minutes, ask Newo support.

## 5. Check new calls

- **Something a chat can show:** a new sandbox chat (`send_message` to a sandbox connector, then
  `search_conversations` for the reply). Booking or ordering in the sandbox follows the test-mode
  rule.
- **Phone behavior:** `list_sessions` from the time of the change. Read the result of the next
  three to five real calls of the same kind (`session_type`), and the dialogue of one. Calls take
  time to come in: if there are none yet, say so and offer to check later.

Report: what changed, what the new calls show, how to undo it (the saved old value), what to
watch. A fix that holds becomes a scripted test if a chat can show it
([05-operate, step 3](../../delivery/05-operate/README.md#fixing-an-issue)).

## Never

- Call any `delete_*` tool, or delete anything another way.
- Write, publish or activate project versions (`write_project_version_files`,
  `publish_project_version`, `activate_project_version`): no script or NAF code.
- Make more than one change before checking the last one.
- Change anything without the account check and a "yes" for that exact change.
- Switch test mode on for an account with real callers.

## Next

Back to [review-agent](../review-agent/SKILL.md) for the next reason, or
[agent-session-audit](../agent-session-audit/SKILL.md) next week.
