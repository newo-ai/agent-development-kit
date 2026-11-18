# Good and weak acceptance criteria

A good criterion is one behavior a caller can observe, with a priority and a way to test it. Used
by [write-acceptance-criteria](../../../skills/write-acceptance-criteria/SKILL.md) and by people
reviewing its output.

## Rules

- One behavior per criterion.
- Observable from outside: what the caller hears, or what appears in another system.
- Says when (working hours, after hours) and on which channel.
- Includes what the agent must **not** do.
- Has at least one check: a scripted test, a phone call, or a check in the other system.
- 10 to 25 per agent. `critical` means the agent cannot go live while it fails.

## Pairs

| Weak | Good | Why the weak one fails |
|---|---|---|
| The agent handles bookings well | During working hours, books a cleaning in the next free slot | "Well" cannot be tested |
| The agent is friendly | Greets with the business name and the agent's name in the first sentence | Tone is subjective; the greeting is observable |
| The agent knows our prices | Quotes the new-patient exam price from the approved list; for any other treatment, offers a consultation | Says nothing about what it must not quote |
| Emergencies are handled | After hours, for severe pain or swelling, gives the approved script | No definition of emergency or of the action |
| Transfers work | When the caller asks for a person during working hours, transfers to the front desk with caller ID | Which transfer, when, and what proves it? |
| The agent integrates with the CRM | After a new-lead call, a contact with name, phone and reason appears in the CRM test account within 2 minutes | The integration is the means; the result is the criterion |
| No hallucinations | Asked about a service not on the list, says it is not offered and offers the closest alternative | Make it concrete and test it adversarially |
| Handles busy times | Answers 6 calls at once with no caller waiting more than 3 seconds | Needs a number |
| Supports Spanish | Completes a booking in Spanish when the caller speaks Spanish | Says what must work in the language |
| Books, confirms, sends an SMS and emails staff | Four criteria, one per behavior | One failure would hide the others |

## Priority

| Priority | Use when | Examples |
|---|---|---|
| critical | Failure harms a caller, the business or compliance, or directly loses revenue | Wrong booking, missed emergency, invented price, data disclosed, dropped caller |
| important | Failure is visible but has a workaround | Hours wrong for one holiday; a field missing from the summary |
| nice-to-have | Polish | Mentions the name of the parking garage |
