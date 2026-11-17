---
name: check-feasibility
description: Check each acceptance criterion against what the Newo platform can do, map it to the lowest step that delivers it (setting, knowledge, tool, scenario), and flag integrations without test accounts and requests only Newo can fulfil. Use before drafting a SOW, or when a partner asks "can the platform do this", "is this possible".
---

# Check feasibility

Stage: [01-discover](../../delivery/01-discover/README.md), step 5. Produces
`work/<agent-name>/feasibility.md` from
[the template](../../delivery/01-discover/templates/feasibility.md).

## Before you start

- Read `acceptance-criteria.yaml` and `requirements.md` in `work/<agent-name>/`.
- Read [the ladder](../../docs/03-configure-and-customize.md#the-ladder-always-try-the-lowest-step-first).
- If you can reach the account, read live settings instead of relying on memory. If this
  repository and the platform disagree, trust the platform ([AGENTS.md](../../AGENTS.md), rule 9).

## Steps

1. **For each criterion, pick the lowest step** that delivers it:
   1. a setting (attribute): [reference/attributes/index.md](../../reference/attributes/index.md);
   2. knowledge: [docs/06-knowledge.md](../../docs/06-knowledge.md);
   3. a tool or integration: [docs/integrations/](../../docs/integrations/README.md);
   4. a scenario change: [docs/05-scenarios.md](../../docs/05-scenarios.md).
   Write the step and the setting or document involved.
2. **Mark the confidence.** `verified` (you read the setting or ran the request), `documented`
   (this repository says so), or `assumption`.
3. **Integrations.** For each criterion that needs another system: access type, test account,
   and the fallback if the system fails (capture and forward, send a link, transfer).
4. **Newo-only requests.** A phone number in a given country, SIP allowlisting, anything in
   [operations requests](../../docs/support/README.md#operations-request). List them and draft the
   request; do not send it.
5. **Risks to schedule.** A scenario change, custom code or a missing test account each adds time.
   Mark them.
6. **Later phases.** Criteria that cannot be delivered now: propose moving them to a later phase,
   and say which file to change (`sow.md` section 8, the criterion's status).
7. **Show the table.** Wait for a "yes" before writing the file or drafting any request.

## Done when

- Every criterion has a step and a confidence label.
- Every integration has a fallback.
- Newo-only requests are listed with drafts.
- Nothing is promised that is only an assumption, unless the SOW says so.

## Never

- Change the shared framework (NAF) to make a criterion work. See
  [docs/04-naf-change-policy.md](../../docs/04-naf-change-policy.md).
- Send a support request without the person's approval.

## Next

[draft-sow](../draft-sow/SKILL.md).
