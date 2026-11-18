---
name: prepare-go-live
description: Walk the go-live checklist and plan a staged launch - nights first, review with the customer, then day mode - with every phone change in an agreed window. Use when UAT passed, or a partner says "go live", "launch at night", "switch on forwarding".
---

# Prepare the go-live

Stage: [04-launch](../../delivery/04-launch/README.md), steps 3 and 4. Produces
`work/<agent-name>/go-live-checklist.md` from
[the template](../../delivery/04-launch/templates/go-live-checklist.md); the launch schedule
lives in the checklist's "Agreed with the customer" section.

A phone change affects real callers at once. Nothing on the phone line changes without the
person's "yes" for that exact step and time ([AGENTS.md](../../AGENTS.md), rule 8).

## Steps

1. **Check UAT.** `uat-report.yaml` has a round with `passed: true`. If not, stop.
2. **Save the agent's settings** to a local file today, with `newo pull` (or the API): the copy
   to go back to (rule 3).
3. **Go through "Before real callers"** in the checklist, item by item. Read each value from the
   platform; do not tick from memory. Answer each item yes, no, or not visible. Some settings do
   not show in the portal: "not visible" is not "no"; read it through the API or the CLI before
   you tick it. Show what is not yet true.
4. **Agree the schedule** with the person:
   - the first night: date and forwarding window
     ([playbooks/night-launch.md](../../playbooks/night-launch.md));
   - who reviews the first two or three nights, and when;
   - the day mode afterwards: human first, AI second, or AI first
     ([docs/telephony/go-live.md](../../docs/telephony/go-live.md));
   - the undo step, in writing, for the customer.

   Write the agreed schedule into the checklist's "Agreed with the customer" section.
5. **Show the filled checklist and the schedule.** Wait for a "yes", then write the checklist to
   `work/<agent-name>/go-live-checklist.md`.
6. **Offer the night-launch notice** ([draft-customer-comms](../draft-customer-comms/SKILL.md),
   template 6).
7. **On the night:** go through "On the live line" with the person. Each test call is real.
8. **After the review:** move to day mode only when the customer agrees. Offer template 7.
9. **Mark the launch milestones** 13 to 15 in `project-plan.md` (night launch, review of the
   first nights, day mode) as each one completes.

## Done when

- Every checklist item is ticked or has a reason.
- The customer has the undo step in writing.
- The agent answers real callers in the agreed mode.

## Next

[collect-signoff](../collect-signoff/SKILL.md).
