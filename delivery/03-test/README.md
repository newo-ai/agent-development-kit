# 03-test: prove it against the criteria

**Goal:** know, criterion by criterion, whether the agent is ready for the customer to test.

**Needs:** a built agent ([02-build](../02-build/README.md)) and `acceptance-criteria.yaml`.

**Done when:**
- every criterion has at least one check, and every check was run;
- every `critical` criterion passes;
- every failed `important` criterion is fixed, or the customer accepted it as a known limitation;
- `test-report.md` is written, and `status` is filled in for every criterion.

How the test tools work is in [docs/testing/](../../docs/testing/README.md). This page says what
to test and in which order.

## Steps

1. **Turn each criterion into checks.**
   - What the agent **says** (facts, rules, refusals, the booking dialog): a scripted chat test.
     One scenario file per criterion, named after it: `tests/AC-001-booking.yaml`. The format is
     in [text tests](../../docs/testing/text-tests.md#scripted-tests-newo-test).
   - What depends on the **call** (greeting, voice, language, transfers, after-hours behavior,
     how numbers and dates are spoken): a phone call. Write the steps and what must happen into
     the criterion's `checks`.
   - What happens in **another system** (a booking, a CRM record, an SMS, a report): check it
     there, not only in the conversation.
2. **Add the hard cases.** For each `critical` criterion, add at least one difficult version: the
   caller changes their mind, gives an incomplete answer, asks for a slot that is not free, or
   switches language.
3. **Run the scripted tests:** `newo test <file>` for each scenario. Prefer expectations on key
   facts and on what must never be said; exact wording changes between runs.
4. **Run a test more than once** before you trust it. The same question can pass once and fail
   the next time. Run each `critical` scripted test three times; a criterion passes when all
   three pass. (The number is a starting point, not a platform rule.)
5. **Make the phone calls** with the checklist in
   [voice tests](../../docs/testing/voice-tests.md#manual). Test one transfer in each direction
   you configured, at a time when someone answers.
6. **Fix and re-run.** Fix failures at the lowest step of the ladder
   ([02-build, "Rules"](../02-build/README.md#rules); the playbook is
   [improve and fix](../../playbooks/improve-and-fix.md)). After every fix, run **all** scripted
   tests again: a fix for one case can break another.
7. **Write the report:** [templates/test-report.md](templates/test-report.md). Set `status` for
   each criterion in `acceptance-criteria.yaml`.

Keep the scenario files. They are the regression tests for every later change
([05-operate](../05-operate/README.md)).

## What a chat test cannot show

The sandbox does not test the phone line, the voice, transfers, SMS delivery, silence or
interruptions. A criterion about any of these is not passed until a call showed it.

## Test data

- Use the other system's test account, or the agent's test mode
  ([voice tests, "Test mode"](../../docs/testing/voice-tests.md#test-mode)). Switch test mode
  **off** before go-live.
- Test conversations stay in the conversation list. Their names (`newo-cli-...`) tell them apart
  from real callers.
