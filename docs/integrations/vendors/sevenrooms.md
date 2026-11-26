# SevenRooms

## What it does for the agent

Checks table availability, books, finds, reschedules and cancels reservations, by phone or chat.

## Before you start

- A SevenRooms account with external integration access, **enabled by the SevenRooms
  representative** for the venue.
- From the representative: **Client ID**, **Client Secret** and **Venue ID**. Never make up
  substitutes.
- Bookable dates and times, including test dates. Builder publish rights.
- About 15 minutes once the credentials exist; SevenRooms may take longer to provide them.

## Partner does in SevenRooms

1. Ask the SevenRooms representative to enable external integration access for the venue and to
   send the Client ID, Client Secret and Venue ID.
2. Ask whether the venue is on US or EU production.
3. Type the three values into the Newo Builder (next section). Not into the chat.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `sevenrooms_integration`, Title `sevenrooms_integration`, Registry
   `production`, Module `sevenrooms_integration`, Auto update on. **Force Update Project**.
2. The partner types into **Module - SevenRooms**: `sevenrooms_client_id`,
   `sevenrooms_client_secret`, `sevenrooms_venue_id`. No token: the integration manages it.
3. `sevenrooms_base_url`: keep `https://api.sevenrooms.com/2_4` for US; use
   `https://api.eu.sevenrooms.com/2_4` only if SevenRooms confirms EU.
4. Check the project's business time zone matches the venue.
5. Switches (on by default; turn one off only if the restaurant does not want it):
   `sevenrooms_enable_availability`, `sevenrooms_enable_reservation`,
   `sevenrooms_enable_cancellation`, `sevenrooms_enable_reschedule`,
   `sevenrooms_enable_booking_lookup`. `sevenrooms_availability_search_radius_hours` (3).
   `sevenrooms_setup_scenarios` on for a new project. Leave the other `sevenrooms_*` settings.
6. **Publish All**. Check the canvas has "Regular Table Booking", "Cancellation via Agent" and
   "Restaurant Reservation Reschedule via Agent" with their scenarios. Their trigger phrases must
   not be edited (translating is allowed).

## Test

Reservations are real. Use test dates and cancel afterwards.

1. "Can I reserve a table for two tomorrow at 7 PM?" Compare the times with SevenRooms.
2. Book; it is in SevenRooms.
3. In a new chat, find the reservation by phone number.
4. Cancel it; check SevenRooms. Reschedule one; check the new date, time and party size.

## Needs Newo

None stated in the article. If cancelling fails, the article says to contact Newo support:
[draft-support-request](../../../skills/draft-support-request/SKILL.md).

## Limits and known issues

- One venue per project.
- Lookup depends on the phone number matching.
- Slots that need a card are not offered (no payments).
- Availability search stays within one day. Booking lookup off limits cancelling from another
  conversation.

## Source

https://help.newo.ai/en/articles/16163790-sevenrooms-integration, read 2026-11-25.
