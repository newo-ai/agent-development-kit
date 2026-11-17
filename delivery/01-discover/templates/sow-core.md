# Statement of work: AI agent for <customer>

Core template for every vertical. Paste the vertical section as section 3B:
[restaurant](sow-restaurant.md), [dental and ortho](sow-dental-ortho.md), [IVR](sow-ivr.md),
[support](sow-support.md). Replace every `[bracket]`. Keep this file in the partner's folder for
the project, never in this repository. No callers' personal data, API keys or passwords.

| Field | Detail |
|---|---|
| Effective date | [On countersignature] |
| Service provider | [Partner legal entity] (partner of record) |
| Platform | The Newo platform (voice, chat and SMS AI agents) |
| Customer | [Customer legal entity], contact [name, role] |
| Vertical | [Restaurant / Dental and ortho / IVR and call routing / Support / Other] |
| Locations in scope | [List. One Newo account per location is usual.] |
| Channels | [Phone / web chat / SMS / email] |
| Languages | [Per location] |
| Systems to connect | [Calendar, booking, PMS, POS, CRM, ticketing] or "none in this SOW" |
| Target go-live | [Date], nights first (section 6) |
| Linked files | `requirements.md`, `acceptance-criteria.yaml`, `project-plan.md` |

## 1. Summary and objectives

[Partner] will configure and launch an AI agent on the Newo platform for [Customer]. The agent
will [main job in one sentence, for example "answer every call 24/7, book new-patient
appointments and route urgent requests to staff"].

Objectives, written so they can be measured after go-live:

- [Example: every after-hours caller gets an answer or a captured message]
- [Example: at least [__]% of new-appointment requests booked or sent a booking link without staff]
- [Example: staff receive a summary of every captured request within 5 minutes]

## 2. Delivery approach: go live early, add capabilities in stages

The agent goes live in its simplest useful form and gains capabilities stage by stage. Each stage
is a go-live point; the customer can stay on any stage while the next is built. The vertical
section lists the stages. When the vertical marks stages as part A and part B, part B acts
inside the system named on its cover (restaurant: the POS; dental: the PMS) and its customer
inputs list what part B needs, including sign-offs such as a BAA; part A is everything else.
Stages marked "elected" are optional upgrades the customer chooses.

| Stage | What the agent does | Value at go-live | Criteria |
|---|---|---|---|
| 1 | [Answers, identifies intent, answers general questions, routes] | [24/7 answering] | [AC-001 to AC-00x] |
| 2 | [Captures requests and forwards a summary] | [No lost requests] | [ ] |
| 3 | [Books or acts in a connected system] | [Self-service] | [ ] |

## 3. Scope

### 3A. Use cases

Every use case lists the acceptance criteria that prove it. A use case without criteria is not in
scope.

| Id | What the caller wants | Working hours | After hours | Criteria |
|---|---|---|---|---|
| UC-01 | [New appointment / reservation / order] | [Book / transfer] | [Book / send link / capture] | [AC-001, AC-002] |
| UC-02 | [Change or cancel] | [ ] | [ ] | [ ] |
| UC-03 | [General questions] | [Answer from knowledge] | [Same] | [ ] |
| UC-04 | [Speak to a person] | [Transfer to …] | [Message to …] | [ ] |

### 3B. Vertical section

[Paste every section of the vertical file: stages, session types, inputs, starter criteria,
exclusions, acceptance rule, and anything else it carries (routing map, telephony checks,
workflow baseline, escalation boundary, handoff package, compliance gate). Its cover additions
go into the cover table at the top, not here.]

## 4. Knowledge and content

| Source | Used for | Owner | Refresh |
|---|---|---|---|
| [Website pages] | [Hours, services, directions] | [Customer] | [On change] |
| [Price list, menu, FAQ] | [Answers] | [ ] | [ ] |

The agent answers only from approved content. It must never say: [list, for example prices for
treatments, allergen assurances, legal or medical advice].

## 5. Integrations (business level)

Technical details (endpoints, credentials, field mappings) go in a separate integration note,
never in this SOW.

| System | What the agent does in it | Access type | Who grants access | Test account | If the system fails |
|---|---|---|---|---|---|
| [System] | [Look up / create / update / notify] | [MCP server / REST API / web only] | [Owner / IT / vendor] | [Yes / no: risk] | [Capture and forward / send link / transfer] |

A missing test account is a risk and is listed in section 10. A test booking in a live system is
a real booking.

## 6. Telephony and go-live

- Number: [keep the business number and forward to the AI number / new number in [country] / SIP]
- Launch: nights first for [2 to 3] nights with a review, then [human first, AI second after
  [N] rings / AI first]
- Switch-off: [steps], given to the customer in writing at handover
- Every phone change happens in an agreed window, because it affects real callers at once

## 7. Handoff and escalation

| Situation | Working hours | After hours | Destination |
|---|---|---|---|
| Caller asks for a person | [Transfer] | [Message] | [Number / inbox] |
| Urgent or emergency | [ ] | [ ] | [ ] |
| Complaint | [ ] | [ ] | [ ] |

Transfer numbers are lines where a person answers, never the public business number or the AI
number. The handoff carries what the caller already said.

## 8. Out of scope

- Use cases, channels, languages, locations or systems not named in this SOW
- Data migration or cleanup in the customer's systems
- Third-party fees (carrier, SMS, vendor API access)
- Changes to the shared Newo framework; all work is configuration of this agent
- [Vertical exclusions]

## 9. Data and compliance

- Health data (PHI): [yes / no]. If yes, a BAA between the customer and the Newo platform
  ([health data rules](../../../docs/integrations/README.md#health-data)), plus a customer-partner
  BAA if the partner processes PHI, is signed before any system access or live system data.
- Personal data under GDPR, CCPA or similar: a data processing agreement where it applies.
- Call recording and consent wording: [confirmed by the customer].
- Credentials are shared through [secure method], never by email or chat.

## 10. Customer inputs

| Input | Needed for | Due | Status |
|---|---|---|---|
| Hours, holidays, locations | Stage 1 | [Date] | [ ] |
| Transfer numbers and inboxes | Stage 1 | [ ] | [ ] |
| Knowledge content | Stage 1 | [ ] | [ ] |
| System access and test account | Integration stage | [ ] | [ ] |
| UAT tester and time | Acceptance | [ ] | [ ] |

The agent is as accurate as these inputs. A correction after stale inputs is a configuration
change, not a defect.

## 11. Acceptance

- `acceptance-criteria.yaml` lists every behavior, its priority and its check. Ids stay fixed once
  agreed.
- Copy the starter criteria in section 3B into `acceptance-criteria.yaml` and adapt them; renumber
  to fit the agent's file.
- Before UAT, [Partner] runs [__] test calls and chats per stage, covering every use case in
  working and after hours.
- The customer tests each criterion and records pass or fail. Each round is one UAT attempt.
- [2] UAT rounds are included in this SOW; further rounds are a written change request (section
  13).
- A stage is accepted when every critical criterion passes, at least [95]% of all criteria pass,
  and the customer signs off.
- Acceptance is complete by [date].
- After sign-off, [Partner] monitors the agent for [__] business days. Defects in the agreed
  scope are fixed at no charge; anything else is a change request (section 13).
- Critical failures: [a wrong booking or order, a failed escalation, an invented price or policy,
  a safety assurance, a dropped caller with no capture].

Critical criteria for this agent: [AC-…, AC-…]

## 12. Timeline

| # | Milestone | Owner | Target |
|---|---|---|---|
| 1 | SOW signed, criteria agreed, plan in place (gate G2) | Both | [ ] |
| 2 | Customer inputs complete | Customer | [ ] |
| 3 | Agent ready for testing (gate G3) | [Partner] | [ ] |
| 4 | UAT round 1 | Customer | [ ] |
| 5 | Night launch | Both | [ ] |
| 6 | Day launch and sign-off | Both | [ ] |
| 7 | Handover | [Partner] | [ ] |

## 13. Change control

New use cases, systems, languages or locations are added by a written change request with an
updated criteria file and timeline.

## 14. Commercial terms

[PARTNER TO FILL: fees, billing, term, termination, liability, ownership of the configuration
and content.]

## 15. Sign-off

| Role | Name | Signature and date |
|---|---|---|
| Customer, business owner | [ ] | [ ] |
| Customer, technical owner | [ ] | [ ] |
| Delivery owner | [ ] | [ ] |

## Where each section comes from

| SOW section | Source |
|---|---|
| Cover, 1, 6 | `requirements.md`: The business, Channels, Acceptance |
| 3A, 7 | `requirements.md`: What the agent handles, What goes to a person |
| 4 | `requirements.md`: Facts the agent needs, What the agent must never do or say |
| 5 | `requirements.md`: Systems; `feasibility.md` |
| 8 | Vertical section; `feasibility.md` (later phases) |
| 9 | `requirements.md`: Compliance |
| 11 | `acceptance-criteria.yaml` |

Before sending the SOW to the customer: delete this table, the paste instructions, and every
repository link.
