---
name: review-agent
description: Review one agent's failed calls from the Newo MCP - group them by reason (Spam or sales call, Caller declined or ended, Other / needs review, with Technical problem and Agent mistake counted as tags) - then read the real dialogue and logs behind the biggest reasons and say what to do next. Use when a partner asks "why are calls failing", "review this agent", "what went wrong this week", "look at the bad calls", "why didn't callers get what they wanted", "check Northfield HVAC's failed calls". Read only; fixes go to fix-issue.
---

# Review an agent's failed calls

Stage: [05-operate](../../delivery/05-operate/README.md), "The review". Read only. It produces a
grouped report in the chat, and on request the "Failed calls by reason" and "Issues" tables of
`work/<agent-name>/weekly-review.md`
([template](../../delivery/05-operate/templates/weekly-review.md)).

## Before you start

- **The Newo Customer MCP** is the tool. Find the agent with `get_customers` and say its name
  back.
- **The period.** The same week as [agent-session-audit](../agent-session-audit/SKILL.md) (by
  default the last 7 full days, UTC), or what the partner asks.
- **Callers' data.** Dialogue, summaries and logs hold callers' names, numbers and sometimes
  health data ([health data](../../docs/integrations/README.md#health-data)). Read what the task
  needs; describe patterns; never copy a name, a number or a transcript into the chat or a file.
  Session ids are fine in the partner's files.
- **IVR and routing agents** have no quality checks: say "Quality checks aren't available for
  this agent", give the call count, and stop.

## 1. Find the failed calls

`list_sessions` for the period (skip tests as in agent-session-audit, step 1). A **failed call**
has at least one ❌ line in `actual_result`. Count sessions with an empty `actual_result` as
**Null result**, apart from the failed calls.

**Assumption, to confirm:** `actual_result` from the MCP is the same text as the portal's call
result. If the partner sees a different result on the Sessions page, trust the portal.

The result text ends with tags after a `---` line, for example `⚠️Probably technical issue:
<reason>`, `✋Probably refused by the user.`, `✋Probably failed by the user.`. One call often
carries several.

## 2. Group them

**One group per call**, the first that matches:

1. **Spam or sales call.** The MCP returns a platform spam signal: `spam_detected` true, or
   `outcome_category` "Spam Session". These exist only on agent versions 4.16 and later, and the
   two don't always agree: treat either as a strong hint, say so, and say when they disagree.
   Without these fields (older agents), use the result text only when it clearly says spam,
   robocall or sales call.
2. **Caller declined or ended.** The tag `Probably refused by the user` or `Probably failed by
   the user`.
3. **Other / needs review.** Everything else, including ❌ lines with no tag.

**Two tags, counted next to the groups** (a call can have a group and both tags):

- **Technical problem.** `Probably technical issue: <reason>`, when the reason names something
  that broke: a check that never finished, a failed submission, an error in the logs. Not when
  the reason only says the caller hung up or the cause is unknown; count those apart as
  "technical tag without a cause".
- **Agent mistake.** Only when a ❌ line clearly says the agent got it wrong ("incorrectly
  stated that the restaurant was closed", "used the wrong code phrase"). A step the call never
  reached is not a mistake. When in doubt, no tag: the call stays in its group for review.

Never move a call into Agent mistake because nothing else fits.

## 3. Read the calls behind the top reasons

Take the two or three largest groups or tags (Other / needs review included). For each, read two
or three calls:

- `get_session` for the dialogue;
- `search_logs` with that `session_id`, `levels` `error` and `warning`, `per` 20. Logs of one
  session only; no wide time windows.

Ignore per-call quality flags in the logs (such as `quality_metrics`): this skill doesn't use
them. Write each pattern in your own words: what callers wanted, where it went wrong, what the
logs show. At most one short quote per pattern, with no names or numbers.

## 4. Report

| Group | Calls |
|---|---|
| Spam or sales call | |
| Caller declined or ended | |
| Other / needs review | |
| **Tags:** Technical problem / Agent mistake | / |
| Null result (not failed) | |

Then, for each top reason: the pattern, two or three session ids, and what comes next:

| Reason | Next |
|---|---|
| Agent mistake, missing or wrong fact | [fix-issue](../fix-issue/SKILL.md): a setting or knowledge |
| Technical problem | [fix-issue](../fix-issue/SKILL.md) drafts a support request with the session ids and log lines |
| Caller declined or ended | usually nothing; if the dialogue shows the agent drove callers away, say so and treat it as a mistake pattern |
| Spam or sales call | nothing to fix in the agent |
| Other / needs review | the partner looks at the listed sessions on the Sessions page |

Write the tables into `weekly-review.md` only after a "yes".

## Never

- Change anything on the platform.
- Compute CSS, LSS, goal reached, issue rates or trends.
- Copy dialogue, callers' names or numbers into a file, an issue or this repository.

## Next

[fix-issue](../fix-issue/SKILL.md) for one reason at a time.
