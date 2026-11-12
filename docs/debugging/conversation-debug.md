# Debugging one conversation

## Find it

- **API:** `GET /api/v1/bff/conversations/user-personas?page=1&per=50` lists people who talked to
  the agent, most recent first, with their actors. Then
  `GET /api/v1/chat/history?user_actor_id=<actor>` returns the messages, newest first. See
  [API reference, Conversations](https://knowledge.newo.ai/agent-setup#api-conversations).
- **CLI:** `newo conversations`, or `newo conversations --session-id <uuid>` for one session's
  transcript.
- Real callers are often named `User`: the name tells you nothing. Use the time and the number.
- Skip internal personas: `Assessor`, `ConvoAgent`, `vibe_...`, `newo-cli-...`, `setup-test-...`.
  A burst of many calls within minutes with scripted questions is usually an automated test.
- One actor's history holds all of that person's conversations. Split them by gaps of more than
  two minutes.

## Read the logs

- **API:** `GET /api/v1/analytics/logs`, with the parameters in the table below.
- **CLI:** `newo logs --session-id <uuid>` returns the logs of one conversation. Also useful:
  `newo logs --level error,warning`.

| Parameter | Use |
|---|---|
| `from_datetime`, `to_datetime` | UTC; keep the window at 48 hours or less |
| `levels` | `info`, `warning`, `error` |
| `log_types` | `system`, `operation`, `call` |
| `user_actor_ids`, `user_persona_ids` | one participant |
| `external_event_id`, `runtime_context_id` | one event or one skill run |
| `project_idn`, `flow_idn`, `skill_idn` | where the log came from |

`call` logs show which function ran, with its parameters, result, time and source skill. Pages are
large: use `per=20` and page with `cursor`. Errors are not always tagged with the caller, so also
query `levels=error` for the minutes of the call without the actor filter.

## What to look for

| Symptom | Look at |
|---|---|
| A wrong fact | the setting that holds it; the knowledge search of that turn ([search-debug.md](search-debug.md)) |
| A wrong action (no transfer, an unwanted booking) | the tool or transfer decision in the logs; the criteria settings |
| A failed booking or CRM request | the HTTP or MCP call: request, status code, response, timing |
| A language switch | the caller's language detection, the agent's language settings, the turn where it switched |
| An SMS not received | whether the SMS was sent (logs), then the delivery status at the SMS provider |
| Silence, cut-off, echo, talking over the caller | voice settings and the phone line; one bad call vs a pattern |

## Report to the person

What happened, why (or the best hypothesis and how sure you are), what you changed, and how you
tested it. No raw logs with personal data: quote only what is needed.
