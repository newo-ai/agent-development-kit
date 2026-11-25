---
name: gather-requirements
description: Turn discovery call notes, a call transcript, the business's website and the agent's current settings into a filled requirements.md with open questions and risks. Use when a partner starts a new agent, says "start discovery", "we had a call with the customer", "fill in the requirements", or pastes call notes.
---

# Gather requirements

Stage: [01-discover](../../delivery/01-discover/README.md), steps 1 and 2. Produces
`work/<agent-name>/requirements.md` from
[the template](../../delivery/01-discover/templates/requirements.md).

## Before you start

- Ask for the agent name and the industry. Read the industry page in
  [industries/](../../industries/README.md).
- Ask what the person has: call notes, a transcript, an intake form, the website, an existing
  agent. If there was no call yet, offer the
  [intake email](../../delivery/01-discover/templates/intake-email.md) and the
  [discovery call guide](../../delivery/01-discover/question-banks/discovery-call-guide.md).
- Read the question bank for the vertical:
  [dental and ortho](../../delivery/01-discover/question-banks/dental-ortho.md),
  [restaurant](../../delivery/01-discover/question-banks/restaurant.md),
  [IVR and support](../../delivery/01-discover/question-banks/ivr-support.md).
- A transcript contains callers' or staff's personal data. Read it where it is. Do not copy names,
  phone numbers, emails or health details into any file you write.

## Steps

1. **Read what exists.** If the agent was already created from the website, read its current
   settings first (see [docs/02-access-and-tools.md](../../docs/02-access-and-tools.md)). Much of
   the business information may already be there.
2. **Map the notes to the template.** Fill each section of `requirements.md` from the notes. Use the
   person's words for what callers want. Where the notes do not answer a question, leave the field
   empty and add the question to "Open questions and risks". Never fill a gap with a guess. Mark a
   statement the business makes about itself that you cannot check ("we answer every call within a
   minute") as the customer's claim. List numbers that contradict each other under "Open questions
   and risks" and ask the customer which is right.
3. **List what the agent handles.** One numbered item per caller intent: what the caller wants, how
   the agent handles it (puts them through, takes details and passes them on, answers itself, or
   books or orders itself), what "done" looks like, and who gets the report. Mark which ones differ
   after hours.
4. **List what goes to a person** and what the agent must never do or say. These become critical
   acceptance criteria later, so be specific: "never quote a price for implants", not "be careful
   with prices". Ask for the hours someone actually answers a transfer, which are often shorter
   than the opening hours, and what happens when nobody answers.
5. **Check every system.** For each system named, record the answers from
   [integrations, "Ask first"](../../docs/integrations/README.md#ask-first): MCP server, REST API or
   web only; who grants access; whether a test account exists. A missing test account is a risk.
6. **Check compliance.** Health data? Then read
   [the health data rules](../../docs/integrations/README.md#health-data) and add "BAA signed
   before any system access" to the risks. Recording and consent rules for the country.
7. **Write the red flags** into "Open questions and risks", each with an owner:
   - a system the agent must write to, with no test account;
   - an escalation number that is the public business number or the AI number;
   - a go-live date before the customer's tester is available;
   - health data with no BAA;
   - anything only Newo can do (a number in a given country, SIP allowlisting:
     [operations request](../../docs/support/README.md#operations-request)).
8. **Draft the call flow for the customer** from
   [call-flow.md](../../delivery/01-discover/templates/call-flow.md): one row per reason people
   call, in plain words, no platform terms. It is how a non-technical owner checks the agent.
9. **Show the draft.** Show the filled sections, the call flow and the open questions. Wait for a
   "yes" before writing the files.
10. **Write the files** to `work/<agent-name>/requirements.md` and `work/<agent-name>/call-flow.md`,
    and offer a short confirmation email for the customer with the call flow attached
    ([draft-customer-comms](../draft-customer-comms/SKILL.md), template 2).

## Done when

- Every section is filled or its gap is listed under "Open questions and risks".
- Every system has its access type, owner and test-account answer.
- Every red flag has an owner.
- Every case in "What the agent handles" has one of the four ways and a report recipient, and
  appears in `call-flow.md`.
- The file contains no personal data, keys or passwords.

## Next

[write-acceptance-criteria](../write-acceptance-criteria/SKILL.md), once the customer confirms the
requirements. When they do, set "Confirmed by the customer: yes" in `requirements.md`.

## Example

[A two-location orthodontic practice](../../delivery/01-discover/examples/orthodontic-practice.md),
steps 1 and 2 (fictional).
