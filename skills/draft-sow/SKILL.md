---
name: draft-sow
description: Draft a statement of work for a Newo agent, using the core SOW template plus the vertical section (restaurant, dental and ortho, IVR, support). Works from requirements.md and acceptance-criteria.yaml when they exist, or straight from call notes, an email or a website when the partner goes directly to the SOW. Use when a partner says "write the SOW", "prepare the statement of work", "scope document", "send them a proposal".
---

# Draft the SOW

Stage: [01-discover](../../delivery/01-discover/README.md), step 6. Produces
`work/<agent-name>/sow.md`, and a `.docx` copy on request.

## Two ways in

Partners often go straight to the SOW. That is fine. What matters is that the SOW ends up with
**testable acceptance criteria**, because testing, UAT and sign-off are measured against them.
In our delivery experience, missing criteria are the most common cause of rework.

| What exists in `work/<agent-name>/` | Path |
|---|---|
| `requirements.md` and `acceptance-criteria.yaml` | **Full path**: go to "Steps" |
| Only `requirements.md` | **Draft the criteria** from it (fast-path steps 2 to 5, marked as draft), then "Steps" |
| Neither, or only notes, an email or a website | **Fast path**: do "Fast path" first, then "Steps" |

## Fast path: SOW first

Do not send the partner to other skills. Collect what is needed inside this skill:

1. **Ask for whatever they have**: call notes, an email thread, the website, the intake form. If
   they have nothing, ask the five questions that matter most, one message:
   - the top reasons people call, and what "done" looks like for each;
   - what must go to a person, and to whom;
   - what the agent must never say or promise;
   - which systems it must use, and whether a test account exists;
   - the go-live date and who will test.
2. **Draft the scope and criteria together.** From the answers, write the use cases (section 3A)
   and the acceptance criteria (section 11) directly. Follow the rules in
   [good and weak criteria](../../delivery/01-discover/examples/good-vs-weak-criteria.md): one
   observable behavior each, a priority, a check. Include every "never" and every handoff.
3. **Mark them as draft.** Add the line "Draft criteria, to be confirmed by the customer before
   signature" to section 11, and remove it when the customer confirms. Unknowns go to section 10
   (Customer inputs) or requirements.md's "Open questions and risks", never into the SOW as
   guesses.
4. **Show the use cases and criteria** from steps 2 and 3. Wait for a "yes" before writing.
5. **Write the two files the later stages need**: a short
   `requirements.md` (only the sections you have answers for, the rest under "Open questions and
   risks") and `acceptance-criteria.yaml` with the same ids as section 11. Set "Confirmed by the
   customer: no" and leave `agreed_on` empty until the customer confirms. Without them, testing
   and UAT have nothing to read.
6. Continue with "Steps" below, skipping what is already done.

## Steps

1. **Ask which vertical section applies**, and whether the partner or Newo delivers:
   [restaurant](../../delivery/01-discover/templates/sow-restaurant.md),
   [dental and ortho](../../delivery/01-discover/templates/sow-dental-ortho.md),
   [IVR and call routing](../../delivery/01-discover/templates/sow-ivr.md),
   [support](../../delivery/01-discover/templates/sow-support.md), or none (core template alone).
2. **Start the draft in chat** from
   [sow-core.md](../../delivery/01-discover/templates/sow-core.md): paste the vertical section in
   place of section 3B. No file is written before the "yes" at the show step.
3. **Fill the cover and section 1** from `requirements.md`: the business, locations, channels,
   languages, systems, target go-live. Write the objectives so they can be measured.
4. **Fill section 2 (stages)** from the vertical section. Keep only the stages in scope.
5. **Fill section 3A (use cases).** Every use case lists how the agent handles it, who gets the
   report, and the criteria ids that prove it. Attach `call-flow.md`; if it does not exist, draft
   it from [call-flow.md](../../delivery/01-discover/templates/call-flow.md) with the same rows.
6. **Fill sections 4 to 7** (knowledge, integrations, telephony, handoff). Integrations stay at
   the business level: no endpoints, keys or field mappings.
7. **Section 8 (out of scope).** Start from the vertical section's list. Add anything
   `feasibility.md` moved to a later phase.
8. **Section 9 (compliance).** If health data is involved, the BAA comes before any system access.
9. **Fill sections 10 and 12.** Section 10 (customer inputs) from the vertical section's Customer
   inputs and the tester and go-live date in `requirements.md`'s "Acceptance". Section 12
   (timeline) from `project-plan.md` when it exists; until then, list it as unfilled at the show
   step.
10. **Section 11 (acceptance).** Every critical criterion by id; the vertical's acceptance rule
    (for example its test-call count, pass threshold and critical failures). Say how acceptance
    is given: by the customer's reply to one email is enough (see
    [collect-signoff](../collect-signoff/SKILL.md)).
11. **Commercial terms** (section 14) stay `[PARTNER TO FILL]`. Never add prices.
12. **Show the draft.** List anything you could not fill and every criterion still marked draft.
    Wait for a "yes" before writing.
13. **Write the file** to `work/<agent-name>/sow.md`. If `sow.md` already exists, keep a copy of
    the old version first ([AGENTS.md](../../AGENTS.md), rule 3) and change only what the person
    approved.
14. **Offer a Word copy** with [export-docx](../export-docx/SKILL.md).

## Done when

- Every critical criterion appears in sections 3A and 11, with the same ids as
  `acceptance-criteria.yaml`.
- Section 8 lists what is out of scope.
- Commercial terms are a placeholder.
- No personal data, keys, passwords or internal Newo details.
- On the fast path: draft criteria are marked as draft, and `requirements.md` and
  `acceptance-criteria.yaml` exist.

## Next

Ask whether to continue with [check-feasibility](../check-feasibility/SKILL.md) (if not done) or
[plan-project](../plan-project/SKILL.md). Before signature, the customer confirms the criteria;
[check-discovery-gate](../check-discovery-gate/SKILL.md) checks everything is in place.
