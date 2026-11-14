# Playbook: review conversations

Goal: the owner learns what callers wanted, how the agent did, and what to improve, in a short
report. Transcripts contain callers' personal data: quote only what you need, and do not copy
them anywhere except back to the owner.

## 1. Collect the conversations

1. `GET /api/v1/bff/conversations/user-personas?page=1&per=50` (newest first). Keep personas
   whose `last_act_time` falls in the period the owner asked about. Page on while the last item
   is still inside the period.
2. Skip internal and test personas and recognize automated test calls as described in
   [API reference](../reference/api.md#conversations) (real callers are usually named `User`, so the name alone
   does not tell you who is real; sandbox actors are tests).
3. For each persona, read each actor's history:
   `GET /api/v1/chat/history?user_actor_id={actor_id}&page=1&per=100`. `integration_idn`
   and `connector_idn` tell the channel: phone, web voice widget, website chat, text message.
4. The history is newest first and mixes all conversations of that person. Order messages by
   `datetime` and split them into conversations where two messages are more than two minutes
   apart. `is_agent: true` is the agent; the text is `payload.text`.

## 2. Judge each conversation

For each conversation, write down:

- **What the caller wanted** in a few words.
- **Outcome**: answered, booked, message taken, transferred, caller hung up, unresolved.
- **Mistakes**: wrong or invented facts (compare with the settings and the website), missed
  questions, repeated questions, wrong language, talking too long, wrong open or closed
  status, a transfer that should or should not have happened.
- **Missing knowledge**: questions the agent could not answer because the information is not in
  the settings.

When a conversation looks wrong and the reason is not clear, read the logs of that actor:
`GET /api/v1/analytics/logs?from_datetime=...&to_datetime=...&user_actor_ids={actor_id}&per=50`
(48 hours at most) and look at what the agent looked up. Errors are not always tagged with the
caller, so also read `levels=error` for the minutes of the call without the actor filter.
Errors in the agent's own logic (not caused by a setting) are for Newo support: collect the
time, the error message and the skill name, and give them to the owner to forward.

## 3. Report to the owner

Keep it short:

1. Numbers: conversations, by channel, by outcome.
2. Two or three good examples in one line each.
3. Problems, most important first, each with one short quote and the cause you believe in
   (missing information, wrong setting, agent behavior).
4. Proposed fixes, each as a concrete setting change. Ask which ones to apply, then follow
   [Improve and fix](improve-and-fix.md).
