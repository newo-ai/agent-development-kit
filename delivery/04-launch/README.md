# 04-launch: acceptance and go-live

**Goal:** the customer accepts the agent, and it starts answering real callers with the lowest
possible risk.

**Needs:** a test report that says "ready" ([03-test](../03-test/README.md)).

**Done when:**
- the customer tested the agent against the acceptance criteria and accepted it;
- the go-live checklist is complete;
- the agent answers real callers in the agreed mode, and the customer knows how to switch it off.

A phone change affects real callers at once. Agree on the time of every step with the person
([AGENTS.md](../../AGENTS.md), rule 8).

## Steps

1. **Acceptance test by the customer (UAT).**
   - Give the customer the list of criteria in plain words, and how to reach the agent: the AI
     phone number, the chat link.
   - The customer tests each criterion and says pass or fail. Do not test for them.
   - Record the round in [templates/uat-report.yaml](templates/uat-report.yaml): which criteria
     failed and why.
2. **Fix what failed, then repeat.** Fix, run all scripted tests again
   ([03-test](../03-test/README.md), step 6), and let the customer re-test the failed criteria.
   Each round is a new `uat_attempt`.
3. **Go through the go-live checklist:**
   [templates/go-live-checklist.md](templates/go-live-checklist.md).
4. **Go live in stages:** nights first, review two or three nights with the customer, then the
   day. The playbook is [docs/telephony/go-live.md](../../docs/telephony/go-live.md).
5. **Get the customer's sign-off:** [templates/customer-signoff.md](templates/customer-signoff.md).
6. **Hand over.** Tell the customer:
   - how to switch the forwarding off;
   - who reviews calls, and how often ([05-operate](../05-operate/README.md));
   - whom to contact when something is wrong.

## The UAT report

It answers two questions: did the agent pass on the first attempt, and if not, why not. The
root-cause categories show where the delivery process needs work: requirements that were unclear,
a build mistake, an integration, the platform.

- Keep it with the agent's files.
- You may share it with Newo (your Newo contact, or Newo support at https://help.newo.ai). It
  helps Newo improve the platform and this repository. Before you share it, remove customer names
  and anything personal: describe the business as "a dental clinic in Germany".
- A root cause in the `platform` category is also a bug report:
  [docs/support/](../../docs/support/README.md#bug-report).
- If the same root cause shows up in several deliveries, propose a learning
  ([learnings/](../../learnings/README.md)).
