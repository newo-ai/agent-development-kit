# SOW section 3B: dental and orthodontic practices

Paste into section 3B of [sow-core.md](sow-core.md). Industry setup:
[industries/appointments.md](../../../industries/appointments.md). Health data rules:
[docs/integrations/README.md](../../../docs/integrations/README.md#health-data).

## Cover additions

| Field | Detail |
|---|---|
| Practice type | [General / orthodontic / group / multi-specialty] |
| Practice management system (PMS) | [Name]. Needed for part B. |
| Online booking link | [URL]. Needed for stage 3. |
| BAA | [Signed / not yet]. Required before part B. |

## Stages

| Stage | Part | What the agent does | Criteria |
|---|---|---|---|
| 1 | A | Answers 24/7, identifies intent, answers hours, address, services, insurance accepted; routes | [ ] |
| 2 | A | Collects caller and appointment details; sends a summary to front desk, billing or manager | [ ] |
| 3 | A | New patients: sends the booking link by SMS and collects intake. Existing patients: transfers or captures | [ ] |
| 4 | B | Books new-patient appointments in the PMS at the right location, provider, type and slot | [ ] |
| 5 | B | Finds existing patients; books, reschedules and cancels for new and existing patients | [ ] |

New-patient booking comes first because it needs no patient-record matching.

## Session types

| Session | Working hours | After hours |
|---|---|---|
| New patient appointment | Book (stage 4+) or send link; intake | Same |
| Dental emergency (pain, swelling, broken tooth) | Same day per practice rules; message manager | Approved emergency script and on-call number; summary to manager |
| Existing patient: new service or follow-up | Transfer | Send link or capture |
| Reschedule or cancel | Transfer (native from stage 5) | Capture; state the notice policy |
| Billing or insurance | Transfer to billing | Capture to billing inbox; caller texts insurance card photos |
| Ortho: broken bracket, poking wire, aligner question | Transfer or same day per practice rule | Approved self-care steps; capture a callback |
| Vendor, lab, contractor | Capture and route | Same |
| General information | Answer from knowledge | Same |

## Customer inputs

- Hours per location, non-working days, same-day cutoff
- Booking link, transfer numbers, inboxes (front desk, billing, manager, vendors)
- Services, insurance plans accepted, any price the agent may quote
- Emergency script and ortho self-care steps approved by a doctor
- Part B: signed BAA, PMS authorization per location, providers, schedules, appointment types,
  operatories, booking rules, a test patient or sandbox

## Starter criteria

| Priority | Behavior |
|---|---|
| critical | Recognizes a dental emergency and follows the approved script |
| critical | Never gives a diagnosis or clinical advice beyond the approved script |
| important | Says whether a named insurance plan is accepted, from the approved list only |
| critical | Transfers to the front desk when a caller asks for a person in working hours |
| critical | After hours, captures name, date of birth, phone and reason, and sends the summary to the right inbox |
| critical | Sends the booking link by SMS to a new patient who asks for an appointment |
| critical | Books a new-patient exam in the PMS at the right location, provider, type and slot (part B) |
| critical | Verifies an existing patient before any change (part B) |
| critical | Never reads out another patient's information |
| important | States the cancellation notice policy when a caller cancels |

## Out of scope

- Clinical decisions, diagnosis or triage beyond the approved script
- PMS licensing or API fees; cleanup of PMS data
- Any system other than the single PMS named
- Locations opened after signature (change request)

## Compliance gate

No PMS authorization, test account or live data before the BAA is signed. Transcripts used for
review are redacted before they leave the customer's or partner's systems.

## Acceptance rule

At least [40] test calls per stage across working and after hours, including emergencies and
difficult callers. A stage goes forward at [95]% or better with no open critical failure.
Critical failures: an appointment written to the wrong patient, provider, location or slot; a
missed emergency; clinical advice given; another patient's data disclosed; a dropped caller with
no capture.
