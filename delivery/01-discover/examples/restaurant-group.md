# Worked example: a two-location restaurant group

**Fictional.** An invented family-owned Italian restaurant group, used to show 01-discover.
Nothing here comes from a real customer.

## 1. Call notes

- Two locations in one city; dinner seven days, brunch on weekends. About 2,200 calls a month. On
  Friday and Saturday from 17:00 to 20:00 the host stand misses many calls.
- Top reasons: reservations (55%), hours and directions (15%), takeout orders (15%), private
  events (8%), other (7%).
- Reserve with Google is live with no payment step. The reservation platform has no API access
  agreed yet.
- Takeout goes through the POS; the owner does not want phone ordering yet.
- Parties over 8 go to the events manager. No allergen assurances, ever.
- Guests call in English and Spanish. Keep the number; overflow after 3 rings during service.

## 2. Requirements (extract)

| Section | Content |
|---|---|
| What the agent handles | New reservations up to 8 guests; hours, directions, parking; menu questions; takeout requests (capture and transfer); events (capture) |
| What goes to a person | During service: complaints and changes to existing reservations go to the host stand. Parties over 8 and catering go to the events inbox |
| Must never do or say | Allergen safety assurances; guaranteed tables for walk-ins; prices not on the menu |
| Systems | Reserve with Google (stage 3). Reservation platform: later change request. POS: not in scope |

## 3. Acceptance criteria (extract)

```yaml
criteria:
  - id: AC-001
    priority: critical
    behavior: "Books a reservation for 2 to 8 guests through Reserve with Google with the right location, date, time and party size, and confirms by SMS"
    channels: [phone]
    checks:
      - type: call
        steps: "Ask for 4 guests on Saturday at 19:30 at the second location. The booking appears in the Google Business Profile; the SMS arrives."
    status: not-tested

  - id: AC-002
    priority: critical
    behavior: "For 9 or more guests, does not book; captures date, headcount and occasion and sends them to the events inbox"
    channels: [phone]
    checks:
      - type: scripted
        file: tests/AC-002-large-party.yaml   # 9, 12 and 20 guests
    status: not-tested

  - id: AC-003
    priority: critical
    behavior: "For any allergen question, says staff will confirm and offers a transfer or callback; never says a dish is safe"
    channels: [phone]
    checks:
      - type: scripted
        file: tests/AC-003-allergen.yaml
    status: not-tested

  - id: AC-004
    priority: critical
    behavior: "Switches to Spanish when the caller speaks Spanish, and completes a booking in Spanish"
    channels: [phone]
    checks:
      - type: call
        steps: "Call and speak Spanish from the first sentence. The booking completes; the SMS is in Spanish."
    status: not-tested

  - id: AC-006
    priority: important
    behavior: "Answers 6 calls at once without any caller waiting more than 3 seconds"
    channels: [phone]
    checks:
      - type: call
        steps: "Six testers call within the same minute."
    status: not-tested
```

## 4. SOW (extract)

- **Scope:** restaurant section, stages 1 to 3, both locations, English and Spanish.
- **Out of scope:** reservation platform integration (stages 4 and 5), part B ordering, delivery
  marketplaces.
- **Acceptance:** 50 test calls per stage in two rounds, 95% pass, no open critical failure.

## What this example shows

- The agent books from day one with no integration, so the platform integration became an
  upgrade, not a blocker.
- The party-size threshold and the allergen rule became critical criteria with exact tests.
- "Handles busy nights" became a criterion with a number.
