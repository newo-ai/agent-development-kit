---
name: plan-project
description: Build a dated project plan back from the go-live date, plus the partner's own action checklist - Newo support requests (phone numbers, porting, SIP allowlisting, outbound calling), vendor access, BAA, forwarding - each with when it was sent, the ETA and the milestone it blocks. Use when the customer wants dates, or a partner says "make a project plan", "when can we go live", "timeline", "what do I need to request".
---

# Plan the project

Stage: [01-discover](../../delivery/01-discover/README.md). Optional for the customer, but the
partner checklist is worth doing on every project: in our delivery experience, most delays come
from requests sent late.
Produces `work/<agent-name>/project-plan.md` from
[the template](../../delivery/01-discover/templates/project-plan.md).

## Before you start

- Read `sow.md` (stages, systems, inputs), `requirements.md` (go-live wish, tester) and
  `feasibility.md` (Newo-only requests, missing test accounts) if they exist.
- Ask for the go-live date and whether it is fixed (an event, a season) or a wish.

## Steps

1. **Build the partner checklist first.** Go through the "Partner checklist" table in the
   template and keep every row that applies to this agent. For each, find it in the files:
   - **Newo support requests** (only Newo can do them; use the
     [operations request](../../docs/support/README.md#operations-request) format): a phone number
     in a country, porting a number, SIP or RTP IP allowlisting. Plan Assessor runs only if Newo has set Assessor up for this account
     ([voice tests](../../docs/testing/voice-tests.md#automated-voice-tests)). If the agent
     makes outbound calls or sends SMS, ask Newo whether outbound needs enabling on the account.
   - **Platform set-up the partner does**: the test agent, connectors, knowledge.
   - **Vendor and customer access**: API credentials or MCP access per system, a test account,
     the BAA for health data, the Google Business Profile, carrier or PBX changes for forwarding.
2. **Draft every request** that is not sent yet (the operations request text, the email to the
   vendor or customer). Show the drafts. Do not send anything; the partner sends.
3. **Record status for each row**: sent on (date), ETA (the date Newo, the vendor or the customer
   gave; leave "asked" until one is given, never estimate it), owner, and the milestone it blocks.
4. **Copy the milestones** from the template. Work back from go-live. The launch is staged:
   nights first, a review, then the day ([docs/telephony/go-live.md](../../docs/telephony/go-live.md)).
5. **Tie the checklist to the plan.** A milestone cannot start before the requests it depends on
   have an ETA earlier than its start. Where an ETA is later, or missing, mark the milestone at
   risk and say so.
6. **Mark the gates.** G2: SOW signed with criteria, plan and test approach in place. G3: the agent
   passes its smoke test on every channel and is ready for testing.
7. **Leave time for UAT**: at least one round plus a retest of failed items, checked against the
   customer's (or the partner's, see [run-uat](../run-uat/SKILL.md)) tester availability.
8. **Phone changes** get an agreed window ([AGENTS.md](../../AGENTS.md), rule 8).
9. **Show the plan and the checklist.** Wait for a "yes" before writing or sharing.

## Keep it current

Run this skill again whenever an ETA arrives or slips: "update the plan, Newo says the number
will be ready on the 4th". Update the row, then re-check which milestones are at risk.

## Done when

- Every applicable checklist row has an owner, a sent date or "not sent", and an ETA or "asked".
- Every milestone has an owner and a date, and the ones waiting on a late request are marked.
- G2 and G3 are marked.
- The plan and all drafts contain no keys, passwords or callers' personal data.

## Next

Ask whether to continue with [check-discovery-gate](../check-discovery-gate/SKILL.md).
