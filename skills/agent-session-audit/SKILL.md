---
name: agent-session-audit
description: Weekly numbers for each of a partner's live agents from the Newo MCP - calls, leads, units used, and calls where the caller's goal wasn't reached - with a pointer to the Sessions page in the Newo portal for CSS, LSS and goal reached. Use when a partner asks "how are my agents doing", "weekly numbers", "weekly check", "how many calls did we get this week", "how many leads", "how many units did we use", "is the agent working", "which agent should I look at", "what happened on the calls this week". Not the configuration check (docs/07-health-check.md); for why calls failed, run review-agent.
---

# Weekly session audit

Stage: [05-operate](../../delivery/05-operate/README.md), "The review". Read only: this skill
changes nothing on the platform. It produces a table in the chat, and on request the "Numbers"
block of `work/<agent-name>/weekly-review.md` from
[the template](../../delivery/05-operate/templates/weekly-review.md).

Plain counts only. No scores, no status labels, no thresholds, no comparison with other weeks or
other partners. Quality scores (CSS, LSS) and goal reached are on the **Sessions** page in the
Newo portal: the partner reads them there; this skill does not compute them.

## Before you start

- **The Newo Customer MCP** is the tool ([README.md, "Set up"](../../README.md#set-up)). Don't ask
  which tool to use.
- **Which agents.** `get_customers` lists every account the partner's sign-in opens, one agent
  per account. Ask whether to cover all of them or the ones they name (for example "Northfield
  HVAC"), and say the names back.
- **Which week.** By default the last 7 full days, in UTC. Say the dates. A partner may ask for
  the business's time zone or another period.
- **Callers' data.** `list_sessions` returns summaries with callers' names and details. Count;
  never repeat a summary, a name or a number in the chat or a file.

## 1. Collect the calls

For each agent, `list_sessions` with `customer_idn`, `from_datetime` and `to_datetime`, `per`
up to 1000. Page on until you have `total` sessions; if a page says `truncated`, say the count is
incomplete.

- **Skip tests:** sessions with `is_test: true`, sandbox and Vibe connectors (`connector` names
  with `sandbox` or `vibe`). **Assumption:** `is_test` is not set on every test session; web
  widget calls on a test account showed `is_test: false`. Count the web call widget separately,
  so the partner can see what came from the website.
- **Channel:** from `channel` and `connector`, in plain words: phone, web call widget, chat,
  text message.

## 2. Count

| Number | How |
|---|---|
| Calls | sessions left after step 1, by channel |
| Leads | sessions with `is_lead: true` (or `list_sessions` with `is_lead: true`) |
| Units used | `get_customer_usage` with `start_at` and `end_at` of the same week: `totals.voice_units`, `totals.text_units`. Plan and balance fields can be empty; leave them out then |
| Goal not reached | sessions whose `actual_result` has at least one ❌ line |
| Null result | sessions with an empty `actual_result`. Counted in calls, not as goal not reached |

**Assumption, to confirm:** `actual_result` from the MCP is the same text as the call result in
the portal, and "at least one ❌" matches the portal's "goal not reached". A ❌ can also mark a
smaller step that failed in a call whose goal was met. Where the Sessions page and this count
differ, trust the portal and tell the partner.

**IVR and routing agents.** An agent that only routes calls has no quality checks. If the
partner says the agent is an IVR or routing agent (or its `sow.md` uses the IVR section), show
its calls only, with the note: "Quality checks aren't available for this agent." Never leave it
out: the partner sees its calls in the portal.

## 3. Report

One table, one row per agent:

| Agent | Calls (phone / web / chat / text) | Leads | Units used | Goal not reached | Null result | Note |
|---|---|---|---|---|---|---|

Then two or three sentences in plain counts: which agents had the most calls, the most
goal-not-reached calls, the most null results. No "good" or "bad", no targets.

End with:
- "CSS, LSS and goal reached for each call are on the Sessions page in the Newo portal."
- For the agent with the most goal-not-reached calls: "Want me to look at why? I'll group the
  failed calls by reason" ([review-agent](../review-agent/SKILL.md)).

Write the numbers into `weekly-review.md` only after a "yes".

## Never

- Change anything on the platform.
- Compute or estimate CSS, LSS or goal reached, or trends over weeks.
- Use status labels, thresholds or benchmarks across agents or partners.
- Copy summaries, dialogue, callers' names or numbers into the chat or a file.

## Next

[review-agent](../review-agent/SKILL.md) for one agent's failed calls.
