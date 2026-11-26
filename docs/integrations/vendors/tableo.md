# Tableo

## What it does for the agent

Guests check availability, pick a dining area, book, change or cancel a reservation, by phone or
chat.

## Before you start

- A Tableo restaurant account with admin access, and its API token.
- At least one dining area (for example "Main Dining", "Terrace") and availability set up.
- Builder publish rights.

## Partner does in Tableo

1. Get the API token from the Tableo admin panel (the exact menu is not stated, to confirm).
2. Type it into the Newo Builder (`tableo_api_token`) as given, without the word "Bearer" and
   without extra spaces. Not into the chat.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `tableo_integration`, Title `tableo_integration`, Registry `production`,
   Module `tableo_integration`, Auto update on. **Force Update Project**.
2. After the token (Attributes, search `tableo`, **Show Hidden**), check the switches (default
   `True`): `tableo_enable_availability_check`, `tableo_enable_booking`,
   `tableo_enable_booking_lookup`, `tableo_enable_cancellation`, `tableo_enable_reschedule`,
   `tableo_setup_scenarios`. `tableo_booking_lookup_days` (7, 1 to 30), `tableo_booking_window`
   (3, 1 to 30). `tableo_connector_name` defaults to `Tableo`.
3. **Publish All**. Publish again after any change.

## Test

Reservations are real. Use test dates.

1. "Do you have a table for 4 on Saturday at 7 PM?" Compare with Tableo.
2. Book; it is in Tableo.
3. Call from a number with a reservation; it is found.
4. Cancel or reschedule; check the status in Tableo.

## Needs Newo

None stated in the article.

## Limits and known issues

- One restaurant per project.
- Lookup covers only upcoming reservations within `tableo_booking_lookup_days`.
- Some Tableo errors come without detail. Phone numbers must be in the same format as in Tableo.

## Source

https://help.newo.ai/en/articles/15552867-tableo-integration, read 2026-11-25.
