# Mozrest (bridge to restaurant reservation systems)

Mozrest connects the agent to more than 50 reservation systems, among them Reservours,
SevenRooms and Tableo. SevenRooms and Tableo also have their own direct integrations
([sevenrooms.md](sevenrooms.md), [tableo.md](tableo.md)): ask the partner which one the
restaurant uses.

## What it does for the agent

Checks table availability, books with full guest details (matching the guest's wish to an area),
and cancels.

## Before you start

- A Mozrest account with API access, and the restaurant set up in Mozrest with areas.
- **Mozrest connector credentials at platform level.** The article does not say who sets these
  (to confirm with the platform team; likely Newo).

## Partner does in Mozrest

1. Check the restaurant is connected in Mozrest, with its areas, and on which reservation system.
2. Tell the assistant the restaurant's identifier used by Mozrest.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `mozrest`, Title `mozrest`, Registry `production`, Module
   `mozrest_integration`, Auto update on. **Force Update Project**, **Publish All**.
2. Check or set: `project_business_time_zone` (an IANA name, for example `America/Chicago`),
   `project_business_name`, `project_attributes_private_dynamic_restaurant_google_restaurant_id`
   (required: nothing works without it).
3. Switches (default `True`): `mozrest_enable_slot_check`, `mozrest_enable_booking`,
   `mozrest_enable_cancellation`. **Publish All**.

The agent asks for first and last name, email, phone, date and time, party size, area.

## Test

These are real reservations.

1. "Do you have a table for 4 tomorrow at 7 PM?" Areas come back.
2. Book; it is in Mozrest. Cancel; it is gone.

## Needs Newo

The platform-level Mozrest connector credentials (to confirm). If `get_integrations` shows no
working Mozrest connector for the account, draft a request with
[draft-support-request](../../../skills/draft-support-request/SKILL.md).

## Limits and known issues

- No reschedule (cancel and book again), no waitlist.
- One restaurant per instance.

## Source

https://help.newo.ai/en/articles/14121848-mozrest-integration, read 2026-11-25.
