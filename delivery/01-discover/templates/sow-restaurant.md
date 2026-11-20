# SOW section 3B: restaurants and hospitality

Paste into section 3B of [sow-core.md](sow-core.md). Industry setup: [industries/restaurant.md](../../../industries/restaurant.md).

## Cover additions

| Field | Detail |
|---|---|
| Venue type | [Full-service / fast-casual / fine dining / bar / multi-concept group] |
| Reserve with Google | [Live, no payment step / not live]. Needed for stage 3. |
| Reservation platform | [Name or none]. Needed for stages 4 and 5. |
| POS | [Name or none]. Needed for part B. |
| Peak concurrency | [Calls at the same time during rush, per location] |

## Stages

| Stage | Part | What the agent does | Criteria |
|---|---|---|---|
| 1 | A | Answers 24/7, identifies intent, answers hours, location, parking, dress code, menu highlights; routes to host stand or manager | [ ] |
| 2 | A | Captures reservation requests (party size, date, time, occasion, seating) and sends a summary to the host stand | [ ] |
| 3 | A | Books new reservations through Reserve with Google. Sends the reservation link when a deposit is needed or the widget cannot book. Transfers or captures changes, large parties and catering | [ ] |
| 4 | A, elected | Books new reservations in the reservation platform against live availability, deposits and booking rules | [ ] |
| 5 | A, elected | Finds existing guests and reservations; books, changes and cancels | [ ] |
| 6 | B, elected | Takes simple takeout orders from the live POS menu; returns order id and pickup time | [ ] |
| 7 | B, elected | Full ordering: dayparts, modifiers, combos, prepayment, transfer above the complexity limit | [ ] |

The agent books from stage 3 with no integration. Stages 4 and 5 upgrade how it books.

## Session types

| Session | Default handling |
|---|---|
| New reservation | Book (widget or platform); send link if a deposit is required; confirm by SMS |
| Large party or private dining | Above [N] guests: do not book. Capture date, headcount, occasion, budget; route to events |
| Change or cancel | Service hours: change natively (stage 5) or transfer. Otherwise capture, state the policy, message the manager |
| Waitlist and walk-in | Quote the wait per house rules. Never guarantee a table |
| Takeout order | Part A: capture and transfer. Part B: take the order |
| Menu and dietary | Answer from the menu. Allergen questions go to staff; never an allergen assurance |
| Catering and events | Capture and route to events. No pricing unless configured |
| Complaint, lost item, billing | Service hours: transfer to manager. Otherwise capture with a callback promise |
| Vendor, press, solicitation | Capture and route by caller type |

## Customer inputs

- Service periods, closures and holidays per location
- Google Business Profile access with the booking widget live and no payment step
- Reservation link (fallback)
- Host stand and manager numbers; inboxes for events, back office, marketing
- Menu and prices the agent may quote, and what it must never state
- House policies: large-party threshold, cancellation and no-show window, deposits, corkage, dress
  code, late-arrival grace
- Stages 4 and 5: platform authorization, floor plan, sections, turn times, pacing, blackout dates
- Part B: POS authorization, modifiers and rules, dayparts, prep times, payment, complexity limit

## Starter criteria

| Priority | Behavior |
|---|---|
| critical | Answers in the configured language and switches when the caller switches |
| important | Gives the right hours for today, including holiday closures |
| critical | Transfers to the host stand when a caller asks for a person during service |
| critical | Never invents a menu item, price or policy |
| critical | Books a reservation through the widget with the right date, time and party size |
| critical | Above the party-size threshold, does not book; captures and routes to events |
| critical | Sends the reservation link when a deposit is required |
| critical | Sends every allergen question to staff, with no assurance |
| important | Handles [N] calls at once at peak with no caller waiting |

## Out of scope

- Setting up the Google Business Profile or the booking widget itself
- Deposits or card on file through the widget path
- Card numbers spoken to the agent; prepayment, if elected, uses the customer's payment
  provider (method to confirm with Newo before signing)
- Delivery dispatch and marketplaces
- Loyalty, gift cards, CRM and marketing tools; outbound campaigns
- Allergen, dietary or food-safety assurances

## Acceptance rule

At least 50 test calls and chats per stage in two rounds: normal callers, then difficult ones
(interruptions, noise, accents, changes of mind, requests exactly at a threshold). A stage goes
forward at 95% or better with no open critical failure. Critical failures: a reservation or order
written wrong; a failed manager escalation; an invented item, price or policy; an allergen
assurance; a dropped caller with no capture. Monitoring after each stage: [5] business days.
