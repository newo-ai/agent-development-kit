# Worked example: a two-location orthodontic practice

**Fictional.** The practice, its numbers and its people are invented to show 01-discover end to
end. Nothing here comes from a real customer. Use it to check what the skills should produce.

## 1. Call notes (what the partner wrote down)

- Orthodontic practice, two locations in Texas, three orthodontists, about 1,400 calls a month.
  About 30% of calls after 5 pm go unanswered.
- Top reasons: new-patient consult (35%), reschedule (25%), billing and insurance (15%), general
  questions (15%), broken bracket or wire (10%).
- New patients book a free consult online today. The office wants more of those booked at night.
- Cloud PMS with a REST API; the vendor offers a sandbox. The practice has a BAA template.
- Must never: give treatment advice; quote treatment prices (saying the consult is free is fine).
- Keep the existing number. Start with nights and weekends. The office manager will test. Wanted
  go-live: in four weeks.

## 2. Requirements (extract of `requirements.md`)

| Section | Content |
|---|---|
| Channels | Phone only. Keep the business number; forward after hours, and during hours after 4 rings with no answer |
| What the agent handles | New consult request; reschedule or cancel; broken bracket or wire; billing and insurance questions; general questions |
| What goes to a person | Working hours: reschedules and billing go to the front desk. After hours: capture and email the front desk; severe pain or injury gets the on-call orthodontist's number |
| Must never do or say | Treatment advice; treatment prices; promise a time that is not in the system |
| Systems | Cloud PMS: REST API, access granted by the office manager, sandbox available. Not connected in phase 1 |
| Compliance | Health data: yes. BAA before any PMS access. Recording disclosure: "This call may be recorded." |
| Open questions and risks | On-call number not yet provided (owner: office manager). Emergency script needs a doctor's approval (owner: lead orthodontist) |

## 3. Acceptance criteria (extract of `acceptance-criteria.yaml`)

```yaml
agent: two-location orthodontic practice (fictional)
agreed_on: YYYY-MM-DD

criteria:
  - id: AC-001
    priority: critical
    behavior: "After hours, sends the free-consult booking link by SMS to a caller who wants to start treatment, and captures name and phone"
    channels: [phone]
    checks:
      - type: call
        steps: "Call after 17:00 and ask to start braces. The SMS with the link arrives; the summary email arrives."
    status: not-tested

  - id: AC-002
    priority: critical
    behavior: "After hours, for severe pain, swelling or injury, gives the approved script and the on-call number"
    channels: [phone]
    checks:
      - type: scripted
        file: tests/AC-002-emergency.yaml   # three phrasings
    status: not-tested

  - id: AC-003
    priority: critical
    behavior: "For a poking wire or loose bracket, gives the approved self-care steps and captures a callback request"
    channels: [phone]
    checks:
      - type: scripted
        file: tests/AC-003-wire.yaml
    status: not-tested

  - id: AC-004
    priority: critical
    behavior: "Never gives a treatment price; says the consult is free and offers to book it"
    channels: [phone]
    checks:
      - type: scripted
        file: tests/AC-004-no-price.yaml    # "how much are braces", asked three ways
    status: not-tested

  - id: AC-005
    priority: critical
    behavior: "During working hours, transfers a reschedule request to the front desk"
    channels: [phone]
    checks:
      - type: call
        steps: "Call during hours and ask to move an appointment. The transfer connects."
    status: not-tested

  - id: AC-006
    priority: important
    behavior: "After hours, captures a reschedule request with name, date of birth and preferred times, and states the 24-hour notice policy"
    channels: [phone]
    checks:
      - type: call
        steps: "Call after hours. The summary has the three fields; the policy was said."
    status: not-tested

  - id: AC-009
    priority: critical
    behavior: "Never reads out another patient's details"
    channels: [phone]
    checks:
      - type: scripted
        file: tests/AC-009-privacy.yaml
    status: not-tested
```

The full list has 12 criteria; AC-007, AC-008, AC-010 to AC-012 cover insurance plans, hours and
address per location, and the recording disclosure.

## 4. Feasibility (extract of `feasibility.md`)

| Criterion | Step | Confidence | Note |
|---|---|---|---|
| AC-001 | setting + SMS | documented | Booking link as a setting; SMS is standard |
| AC-002, AC-003 | knowledge | documented | The approved scripts are customer inputs |
| AC-004 | setting | documented | Critical; run three times in tests |
| AC-005 | setting | documented | The transfer number must not be the public number |
| Book in the PMS | integration | assumption | Needs the BAA and the sandbox. Moved to phase 2 |

## 5. SOW (extract of `sow.md`)

- **Scope:** dental and ortho section, stages 1 to 3, phone, both locations.
- **Out of scope:** PMS booking (phase 2, change request), web chat, Spanish.
- **Acceptance:** 40 test calls per stage, 95% pass, no open critical failure; UAT by the office
  manager, at most two rounds.

## 6. Plan (summary)

| Week | Milestone |
|---|---|
| 1 | Requirements confirmed; criteria agreed; SOW signed (G2) |
| 2 | Inputs received (scripts approved, on-call number); agent built; smoke test (G3) |
| 3 | Tests run; UAT round 1 and fixes |
| 4 | Night launch; review of three nights; daytime overflow; sign-off |

## What this example shows

- The two "never" rules became critical criteria with adversarial tests.
- The PMS had an API and a sandbox, but the BAA was not ready, so booking moved to phase 2
  instead of delaying go-live.
- Missing inputs (on-call number, approved script) were written down as risks with owners on day
  one.
