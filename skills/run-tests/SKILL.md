---
name: run-tests
description: Test the built agent against every acceptance criterion with chat tests, calls and checks in the other systems, fix what fails, and write test-report.md. Use after the build, or when a partner asks "test the agent", "run the tests", "is it ready for the customer".
---

# Test the agent

Stage: [03-test](../../delivery/03-test/README.md). Follow its steps; this skill adds how to run
them and how to judge a result. Produces `work/<agent-name>/tests/` (scenario files) and
`work/<agent-name>/test-report.md` from [the template](../../delivery/03-test/templates/test-report.md).

## Before you start

- Read `acceptance-criteria.yaml` and `build-notes.md`. If the build notes show critical
  health-check findings or a failed smoke test, say so and let the partner decide.
- **On the MCP path** (the default): the account check is the customer and its IDN from
  `get_customers`, said back once per session
  ([AGENTS.md, section 4](../../AGENTS.md#4-how-you-reach-the-platform)).
- **On the CLI path** (only for saved `newo test` files, CI, export or backup): work in the
  agent's folder, `work/<agent-name>/`, and run the [setup check](../../docs/setup-check.md) there
  (rules: [README.md, "Set up"](../../README.md#set-up)). Repeat `newo profile` before every change
  you make while fixing.
- Test data: for each criterion that books or changes something in another system, a test
  account, test mode that covers it, or the live-test procedure agreed in discovery. Otherwise
  test only what reads. Turning test mode on is a change: ask first, note it, and list it in the
  report to switch off before go-live.

## 1. Plan the checks

Write the checks the stage page describes (scripted chat test, call, other system, hard cases).
Show the plan; write the files after a "yes".

## 2. Run

- **Through the MCP** (the default): run each chat check as a practice chat through the MCP's
  sandbox connector **(to confirm: how a sandbox connector is named in `get_connectors`)**.
  - Start a new conversation for every run **(to confirm: how the MCP starts one)**.
  - Send each turn with `send_message`. Read the reply with `search_conversations`; if it is not
    there yet, look again for up to a minute before you mark the check "Not tested".
  - Check whether a tool ran: the conversation's events (`search_conversations`) and its logs
    (`search_logs`).
  - Run each critical check three times, each in a new conversation, as with `newo test`. Keep
    each run's `session_id` for the report.
  - Judge as in step 3, and note in the report that the check ran through the MCP. Keep each
    check's turns and expectations in `tests/` so the same checks can be run again after a fix.
- **Saved `newo test` files** (CLI; when the partner keeps them or runs CI):
  `newo test tests/<file>.yaml --json`. Read the JSON, not only the exit code: exit 1 covers a
  failed turn, a timeout, skipped turns and a setup error alike. Do not save the JSON in `work/`:
  it holds the conversation text.
- **Calls:** you cannot call. Give the person each call check's `steps`, ask when and from which
  number they called, then find that conversation among the newest ones with
  `search_conversations` and read its logs with `search_logs` **(to confirm: the filters for the
  newest conversations)**. On the CLI path: `newo session <session_id> --json` and
  `newo logs --session-id <id>`. Not `newo conversations`: it downloads the whole history. If
  more than one conversation matches, the check is not tested.
- **Assessor** only if the account already uses it
  ([voice tests](../../docs/testing/voice-tests.md#automated-voice-tests)).
- After a publish, wait 2 to 5 minutes before testing.

## 3. Judge what happened, not what was said

- **Pass:** what the criterion asks for happened. "I booked it for you" is not a booking. If
  the criterion has a `system` check, only the other system counts: the booking, the record, the
  SMS is there. Otherwise the run's logs must show the tool ran and succeeded
  (`newo logs --session-id <id>`; the tool is named in `build-notes.md`, "Covered by"). Logs
  arrive late: look again after a minute before you say the tool did not run.
- **Fail:** the agent answered, and the answer or the result is wrong.
- **Not tested:** a timeout, a skipped turn, an error of the test tool, no logs. Not a fail of the
  agent: run it again, but if the check books or sends something, first look whether the first
  run already did it, so it does not happen twice. If it repeats, look in the logs; an empty reply
  with no error often means a change was not published.
- Repeat calls from the same phone reuse the caller: wait about five minutes between them, or a
  result may carry over from the previous call.

Keep the `session_id` of every failure; never copy conversation text into a file.

## 4. Fix and re-run

Find the cause ([debugging](../../docs/debugging/README.md)) and fix it with the partner's "yes"
([improve and fix](../../playbooks/improve-and-fix.md), [02-build rules](../../delivery/02-build/README.md#rules)).
Then run all scripted tests again, the failed check on its own channel, and the call or system
checks the fix can affect (a transfer fix: every transfer).

## 5. Report

Write `test-report.md` and set `status` in `acceptance-criteria.yaml` (show both first). A
criterion passes only when all its checks pass. Fill the template's line "Ready for the customer's
acceptance test" with `yes` only when the stage's "Done when" holds. The partner decides.

## Next

[run-uat](../run-uat/SKILL.md).
