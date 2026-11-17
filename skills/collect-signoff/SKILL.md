---
name: collect-signoff
description: Close the launch - record the customer's approval in the lightest form they will give (one reply to an email is enough), list known limitations, and set up who runs the agent afterwards, usually the partner for small, non-technical businesses. Use when the agent runs in the agreed mode, or a partner says "get sign-off", "close the launch", "hand over", "the customer is happy".
---

# Close the launch: approval and handover

Stage: [04-launch](../../delivery/04-launch/README.md), steps 5 and 6. Produces
`work/<agent-name>/customer-signoff.md` from
[the template](../../delivery/04-launch/templates/customer-signoff.md).

## Why record approval at all

The customer does not have to run anything. Approval is a short record that the agent does what
was agreed. It protects the partner: it closes the scope (anything new is a change request), marks
the launch as done for billing, and keeps the list of known limitations in writing. For a small
business, the partner writes everything and the customer only replies "approved".

## Pick the form with the partner

| Customer | Form | What the customer does |
|---|---|---|
| Small business, non-technical (most) | **Short form**: email | Replies "approved" to one email |
| Larger business, or the SOW asks for it | **Full form**: signed document | Signs `customer-signoff.md` (Word copy via [export-docx](../export-docx/SKILL.md)) |

## Steps

1. **Check the basis.** The last UAT round passed ([run-uat](../run-uat/SKILL.md)) and the go-live
   checklist is done. Do not ask for approval while a critical criterion fails.
2. **Fill `customer-signoff.md`** from the files: criteria tested and passed, UAT rounds, go-live
   mode, known limitations (including anything moved to a later phase).
3. **Set up "After go-live" for who really runs it.** For most small businesses the partner runs
   the agent: the partner reviews calls, makes changes and keeps the switch-off steps. The customer
   needs only two things: whom to call, and how to stop calls going to the agent in an emergency
   (one line, in plain words). If the customer manages it themselves, give them the full list.
4. **Draft the approval request** ([draft-customer-comms](../draft-customer-comms/SKILL.md),
   template 7). Short form: three or four lines with the known limitations and "reply 'approved'
   to confirm". Show it; the partner sends.
5. **Record the answer.** When the customer replies, write the date and the reply ("approved by
   email on YYYY-MM-DD") in the confirmation section. No signature is needed for the short form.
6. **Hand over** with template 8, written for the customer's real role.

## Done when

- The customer's approval is recorded (reply or signature) with a date.
- Known limitations are listed.
- The customer knows whom to call and how to stop the agent in an emergency.

## Next

[05-operate](../../delivery/05-operate/README.md): weekly reviews, usually run by the partner.
