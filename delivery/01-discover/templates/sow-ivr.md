# SOW section 3B: IVR replacement and call routing

Paste into section 3B of [sow-core.md](sow-core.md). For a business replacing a "press 1" phone
menu with an agent that understands the reason for the call and routes it. Transfers:
[docs/telephony/transfers.md](../../../docs/telephony/transfers.md).

## Cover additions

| Field | Detail |
|---|---|
| Current phone menu | [Attach the menu tree or describe it] |
| Phone system and carrier | [Cloud PBX / on-premise PBX / SIP trunk / carrier] |
| Destinations | [Number of departments and queues] |
| Volume | [Calls per month; peak hour] |
| Transfer method | [Warm / cold; SIP REFER; DTMF to an extension] |

## Stages

| Stage | What the agent does | Criteria |
|---|---|---|
| 1 | Greets, understands the reason in the caller's words, transfers to the right destination; a person is always reachable | [ ] |
| 2 | Answers the top [10] general questions itself; routes only what needs a person | [ ] |
| 3 | When a department is closed or busy: captures name, number and reason; sends it to the department's inbox or queue | [ ] |
| 4, elected | Looks up the caller in the CRM or ticketing system and routes by account, priority or open case | [ ] |

## Routing map

| Caller says (examples) | Reason | In hours | After hours | Passed on |
|---|---|---|---|---|
| "My bill is wrong", "payment" | Billing | [Extension / number] | [Capture to inbox] | [Name, account, reason] |
| "Not working", "outage" | Technical support | [ ] | [On-call number] | [ ] |
| "Buy", "pricing", "quote" | Sales | [ ] | [ ] | [ ] |
| A person's name | Directory | [Directory list] | [Message] | [ ] |
| Unclear after two questions | Fallback | [Operator] | [ ] | [ ] |

## Telephony checks before signing

- Confirm the carrier supports the transfer method for this setup before promising it. Some
  signals (for example DTMF to an extension) depend on the carrier; check native support before
  building custom logic.
- Confirm caller ID passes through on transfer.
- Agree what happens when a transfer fails: retry, another destination, or capture.
- Agree the cut-over window and the rollback (point the number back to the old menu).

## Starter criteria

| Priority | Behavior |
|---|---|
| critical | Routes each of the top [N] call reasons to the right destination in at least [95]% of test calls |
| critical | Transfers to a person when the caller asks, at any point |
| critical | When a transfer fails, captures the caller's details instead of dropping the call |
| important | Asks at most two clarifying questions before falling back to the operator |
| important | Answers hours and address without transferring |
| critical | Outside a department's hours, takes a message and sends it to that department |
| important | Routes a known account with an open case to the case owner's queue (stage 4) |

## Out of scope

- Changes to the customer's PBX beyond forwarding and transfer targets
- Outbound calling and contact-center workforce tools
- Payments by phone

## Acceptance rule

A labelled test set of at least [60] calls covering every route, phrased the way real callers
speak, including unclear and multi-reason calls. Routing accuracy at or above [95]% with no
critical failure. Critical failures: a dropped caller, a failed request for a person, a wrong
route for an urgent reason.
