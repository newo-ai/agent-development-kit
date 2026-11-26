---
name: write-acceptance-criteria
description: Turn confirmed requirements into 10 to 25 testable acceptance criteria in total (the kept baseline ones included) with stable ids, priorities and at least one check each, in acceptance-criteria.yaml. Use when requirements are confirmed, or when a partner says "write the acceptance criteria", "what will we test", or an agent was built without criteria.
---

# Write acceptance criteria

Stage: [01-discover](../../delivery/01-discover/README.md), steps 3 and 4. Produces
`work/<agent-name>/acceptance-criteria.yaml` from
[the template](../../delivery/01-discover/templates/acceptance-criteria.yaml). Stages 02 to 05 all
work from this file.

## Before you start

- Read `work/<agent-name>/requirements.md`. If it does not exist, offer to run
  [gather-requirements](../gather-requirements/SKILL.md) first.
- Read [good and weak criteria](../../delivery/01-discover/examples/good-vs-weak-criteria.md).
- If the file already exists and the customer agreed to it, **do not renumber**. Add new ids after
  the last one.

## Steps

1. **One criterion per behavior.** For each item in "What the agent handles", write what a caller
   can observe: what the agent says, or what appears in another system. Split working hours and
   after hours when they differ. Split channels when they differ.
2. **Cover the limits.** Add a criterion for every "must never" item and every "goes to a person"
   case. These are usually `critical`.
3. **Offer the baseline criteria** in
   [baseline-criteria.md](../../delivery/01-discover/templates/baseline-criteria.md): transfers in
   and outside transfer hours, unknown answers, a caller who will not leave details, ending the
   call, test calls, language, and the report. Show which apply; drop or reword the rest with the
   person. Add the ones kept after the agent's own criteria, with their "Correct if" and
   "Wrong if" in the check's steps.
4. **Set the priority.**
   - `critical`: failure harms a caller, the business or compliance, or loses revenue. The agent
     cannot go live while one fails.
   - `important`: visible, has a workaround.
   - `nice-to-have`: polish.
5. **Add at least one check to each.** `scripted` (a scenario file run with `newo test`, see
   [docs/testing/text-tests.md](../../docs/testing/text-tests.md)), `call` (steps for a real call and
   what must happen), or a check in the other system. If you cannot say how to test a criterion,
   rewrite it until you can.
6. **Check the list.**
   - 10 to 25 criteria in total, the kept baseline ones included: a customer can test that many in
     one UAT round. More means some are not distinct, or baseline ones that do not apply were
     kept; fewer usually means limits are missing.
   - No criterion uses "well", "friendly", "fast" or "correctly" without saying what that means.
   - No criterion holds two behaviors joined by "and". One behavior with its expected outcome
     ("takes a callback request and says someone will call back") is one criterion.
   - Every critical criterion has a check that can fail.
7. **Show the list** with ids, priorities and checks. Wait for a "yes" before writing.
8. **Write the file.** Set `agreed_on` only when the customer agrees. From then on the ids are fixed.

## Done when

- 100% of criteria have at least one check. This is the stage's measure.
- Every "must never" and every handoff is covered.
- Each baseline criterion is either in the file or dropped with the person's agreement.
- Ids run `AC-001`, `AC-002`, … with no gaps or duplicates.

## Next

Ask whether to continue with [check-feasibility](../check-feasibility/SKILL.md).

## Example

[Orthodontic practice](../../delivery/01-discover/examples/orthodontic-practice.md), step 3, and
[restaurant group](../../delivery/01-discover/examples/restaurant-group.md), step 3 (fictional).
