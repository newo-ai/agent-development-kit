# Voice tests

## Manual

- **Browser call:** agents created through the Newo plugin get a link to talk to the agent in the
  browser (`agent_status` returns it). It is good for quick checks without a phone.
- **Phone call** to the agent's number or to the business number, if forwarding or SIP is set up.
  This is the only test of the real phone path.

A useful checklist for each call:
1. The greeting is correct, and the language matches the caller.
2. The key facts are right: hours, prices, address.
3. Numbers, dates, times and names are spoken clearly.
4. The agent waits well: no talking over the caller; no long silence while it looks something up.
5. A transfer reaches a person; a booking appears in the real system.
6. A follow-up SMS or email arrives, if configured.
7. The conversation appears in the transcripts, and the logs have no errors.

After the call, read its transcript and logs ([debugging](../debugging/README.md)).

## Test mode

`project_attributes_setting_test_mode` and the test phone number settings let the agent treat
calls from listed numbers as tests, where the integration supports it. Read the descriptions in
the [attribute reference](../../reference/attributes/index.md) before using
them, and switch test mode off when done.

## Automated voice tests

**Assessor** runs automated tests: simulated callers follow a written scenario, and each call is
judged. The customer or partner sets it up on their own account; Newo does not run it for them.
It is not documented publicly yet, so only some customers know about it, usually because Newo
told them. The `assessor` project you may see on an account belongs to it. First find out which
case you are in:

- **The person already uses Assessor on this account**: run the scenarios through it, then read
  the transcripts and logs of the calls it made.
- **They do not**: do not plan the project around it and do not promise it to the customer. Test
  voice with the steps below.

If you are not sure, ask the person; do not guess from the `assessor` project alone.

Without Assessor, test voice with:
- the manual calls above, with the checklist;
- `newo test` scenarios for everything that does not need a call
  ([text tests](text-tests.md#scripted-tests-newo-test));
- the night launch below, and a review of every call.

Write voice scenarios the same way as chat tests: who the caller is, what they want, what must
happen (a booking, a transfer, a correct answer) and what must not. The same scenarios work in Assessor
where the account uses it.

## Night launch: the real-caller test

Before full launch, forward the business line to the agent for a few hours outside business
hours, then review every call. Playbook:
[Launch at night](../../playbooks/night-launch.md).
