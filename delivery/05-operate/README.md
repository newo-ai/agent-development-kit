# 05-operate: keep it healthy

**Goal:** the agent keeps doing what was agreed. Problems are found from real calls, fixed at the
right level, and do not come back.

**Needs:** a live agent, its `acceptance-criteria.yaml` and its test scenarios.

**In good shape when:**
- calls are reviewed on a schedule the customer agreed to;
- every issue has a cause, a fix and a test;
- the scripted tests pass after every change.

## The review

Review every call of the first nights ([go-live, stage 2](../../docs/telephony/go-live.md#stage-2-review-two-or-three-nights)),
then weekly, and again after every change of mode.

1. **Read the conversations** of the period: the playbook
   [review conversations](../../playbooks/review-conversations.md), with the details in
   [conversation-debug.md](../../docs/debugging/conversation-debug.md). Skip test conversations.
2. **Sort them:** what callers wanted, what went well, what went wrong. Check each problem
   against the acceptance criteria: a broken criterion, or a new case nobody planned for?
3. **Write the review:** [templates/weekly-review.md](templates/weekly-review.md). Describe
   patterns; do not copy transcripts or callers' details into it.
4. **Tell the customer** in plain words: how many calls, what callers wanted, what you propose
   to change.

## Fixing an issue

1. **Find the cause** with the playbook [improve and fix](../../playbooks/improve-and-fix.md) and
   [the debugging method](../../docs/debugging/README.md): one
   conversation, its logs, then classify. Check [common issues](../../docs/debugging/common-issues.md)
   first.
2. **Fix at the lowest step of the ladder**
   ([docs/03-configure-and-customize.md](../../docs/03-configure-and-customize.md)), after the
   person's "yes". One change at a time, old value kept.
3. **Add a test for it.** If a chat can show the problem, add a scenario file for the case. This
   is how an issue stays fixed.
4. **Run all scripted tests,** then confirm with a new conversation or a call.
5. **A new case becomes a new criterion.** Add it to `acceptance-criteria.yaml` once the customer
   agreed.
6. **A platform bug** goes to Newo: [docs/support/](../../docs/support/README.md#bug-report).

A change to a live agent reaches real callers. Make it in a quiet hour, and watch the first calls
after it.

## After a Newo update

With automatic updates on, Newo releases reach the agent by themselves. When the customer reports
a change in behavior, or after a release you know about:
- run the scripted tests;
- run the health check ([docs/07-health-check.md](../../docs/07-health-check.md)).

## What is not available yet

Health scores and quality metrics from Newo that a partner can read for their own agents are
**(planned)**. Until then, the review above is the measure: calls reviewed, issues found, issues
that came back.

## Share what you learned

A pitfall or a recipe that other assistants should know: [learnings/](../../learnings/README.md).
