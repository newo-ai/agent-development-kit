# SOW section 3B: support agents

Paste into section 3B of [sow-core.md](sow-core.md). For an agent that resolves defined support
requests itself and hands off the rest with full context.

## Cover additions

| Field | Detail |
|---|---|
| Support domain | [Product / service / IT / other] |
| Volume | Inbound calls [/month], chats [/month], outbound [/month, only if in scope] |
| Ticketing or CRM | [Name or none] |

## Workflow baseline

| # | Workflow | Customer-specific setting |
|---|---|---|
| 1 | Triage and routing: greet, identify the caller and reason, check the escalation map | [Required caller fields] |
| 2 | Single-turn questions from approved knowledge | [Topics and limits] |
| 3 | Multi-turn questions: one clarifying question at a time | [Topics needing clarification] |
| 4 | Troubleshooting: one step per turn, track what was tried, confirm the result | [Supported issues and procedures] |
| 5 | Guided procedure: walk the caller through a documented procedure | [Procedures] |
| 6 | Handoff: summarize, then transfer or relay a message | [Destinations, after-hours, callback] |
| 7 | Out of scope or unsafe: refuse, redirect or escalate | [Restrictions] |
| 8 | Knowledge gap: record it and give the agreed next step | [Where gaps are logged] |
| 9 | Proactive outbound follow-up (only if in scope) | [Triggers and outcomes] |

The agent does not invent facts, does not ask again for what it knows, and keeps the
troubleshooting context when it hands off.

## Escalation boundary (customer completes)

| Decision | Definition | Status |
|---|---|---|
| Resolved by the agent | [What it may resolve alone] | [Open / confirmed] |
| Always to a person | [Issue types or conditions] | [ ] |
| Caller asks for a person | [Transfer at once?] | [ ] |
| Critical or high severity | [Signals and action] | [ ] |
| After hours | [Transfer / message / callback] | [ ] |
| Knowledge gap | [Case / message / handoff] | [ ] |

## Handoff package

The person receiving the handoff gets: who called and how to reach them; the confirmed problem;
product or environment details; steps already tried and their results; any case or ticket id; why
the agent escalated.

## Customer inputs

- Top contact reasons with their share of volume
- Approved knowledge: FAQ, runbooks, policies, with an owner and refresh rule
- Escalation matrix and severity definitions
- Transfer destinations and after-hours coverage
- 20 to 50 redacted transcripts with their outcomes, for the test set
- Ticketing test queue and technical contact

## Starter criteria

| Priority | Behavior |
|---|---|
| critical | Routes each defined issue type to resolve or escalate as the boundary says |
| critical | Never escalates late on a critical-severity signal |
| important | Resolves a documented issue and confirms the result with the caller |
| critical | The person receiving a handoff gets the agreed context without asking the caller again |
| critical | When knowledge is missing, says so and gives the next step instead of guessing |
| important | When the ticketing system fails, uses the agreed fallback and never claims success |

## Out of scope

- Use cases not listed in this SOW
- Actions the customer has not authorized the agent to take alone
- Knowledge outside the approved set

## Acceptance rule

A labelled test set built from the customer's transcripts, covering each workflow, escalation and
knowledge gap. Minimum: every critical criterion passes; overall pass rate [ ]%. Critical
failures: a missed critical escalation, an invented answer, a false "resolved", a lost handoff.
