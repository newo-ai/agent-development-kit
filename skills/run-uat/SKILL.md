---
name: run-uat
description: Run the customer's acceptance test (UAT) - turn acceptance criteria into a plain-language checklist for the customer, record each round in uat-report.yaml, and classify the cause of every failure. Use when the test report says ready, or a partner says "start UAT", "the customer tested it", "record the UAT results".
---

# Run the acceptance test (UAT)

Stage: [04-launch](../../delivery/04-launch/README.md), steps 1 and 2. Produces
`work/<agent-name>/uat-report.yaml` from
[the template](../../delivery/04-launch/templates/uat-report.yaml).

## Before you start

- Read `test-report.md`. If it does not say "Ready for the customer's acceptance test: yes", stop
  and go back to [03-test](../../delivery/03-test/README.md).
- Read `acceptance-criteria.yaml`.

## Steps

1. **Make the customer's checklist.** One line per criterion, in plain words, with what to do and
   what should happen. Critical ones first. Add how to reach the agent: the AI phone number, the
   chat link. Show it; wait for a "yes".
2. **Agree who tests.** Best: the customer tests, because they know their callers. Many small
   businesses will not. Then use the partner-led option: the partner runs the checklist, and the
   customer listens to a short live demo or to recordings of the critical criteria and says yes
   or no. Record who tested in the round. Either way the customer decides pass or fail on the
   critical criteria. Offer the invitation email
   ([draft-customer-comms](../draft-customer-comms/SKILL.md), template 4) or the demo invite.
3. **Record the round.** When results come back, add a round to `uat-report.yaml`:
   `uat_attempt`, date, `tested_by`, total, failed ids, and `passed` (true only when no critical criterion
   failed and the customer accepts).
4. **Classify each failure** with the template's categories: `requirements`, `build`, `test`,
   `integration`, `telephony`, `platform`, `other`. One sentence of description and the fix.
   A `platform` cause is also a bug report ([docs/support/](../../docs/support/README.md#bug-report)).
5. **Fix and retest.** After fixes, run all scripted tests again
   ([03-test](../../delivery/03-test/README.md)), then ask the customer to retest only the failed
   criteria. That is a new `uat_attempt`.
6. **Show the report** before writing it.

## Done when

- The round records who tested: customer, or partner with the customer reviewing.
- The last round has `passed: true`.
- Every failure in every round has a category and a fix.

## Share with Newo

The UAT report helps Newo improve the platform and this repository. Before sharing, replace the
agent name with a description ("a dental clinic in Germany") and remove anything personal.

## Next

[prepare-go-live](../prepare-go-live/SKILL.md).
