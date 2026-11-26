# Altegio

## What it does for the agent

Checks free slots by service, staff and date; books through Altegio's online booking; cancels and
reschedules appointments the agent made; finds existing appointments by phone number.

## Before you start

- An Altegio account with services and staff set up.
- A **Partner Token** and **Application ID** from the Altegio marketplace / Developer Hub.
- A **User Token**, only for finding existing appointments and rescheduling.
- Builder access with publish rights.

## Partner does in Altegio

1. Get the Partner Token and Application ID (and the User Token if needed) from Altegio. The exact
   screens are not stated in the article (to confirm with Altegio).
2. Type them into the Newo Builder (next section). Not into the chat.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `altegio_integration`, Title `altegio_integration`, Registry `production`,
   Module `AltegioIntegration`, Auto update on. **Force Update Project**.
2. The partner types `altegio_partner_token`, `altegio_application_id` and, if needed,
   `altegio_user_token` (Attributes or **Settings** > **Module - AltegioIntegration**, **Show
   Hidden**).
3. Choose `altegio_location_id` from the list (it fills after the first two).
4. Optional (default `True`): `altegio_availability_enabled`, `altegio_booking_enabled`,
   `altegio_cancellation_enabled`, `altegio_reschedule_enabled`,
   `altegio_existing_appointments_enabled`, `altegio_setup_scenarios`;
   `altegio_existing_appointments_search_days` (365).
5. **Publish All**: the `altegio_connector` starts, services and staff load, and the scenarios are
   added.

## Test

Bookings are real. Use a test client.

1. Ask about a service; real slots for the right staff member come back.
2. Book; it appears in Altegio.
3. With the User Token: call from a number with an appointment; it is found. Move it.
4. Cancel an appointment the agent made; it is gone.

## Needs Newo

None stated in the article.

## Limits and known issues

- Cancel and reschedule only for appointments the agent created.
- Lookup and reschedule need a valid User Token. One location per project.

## Source

https://help.newo.ai/en/articles/15825114-altegio-integration, read 2026-11-25.
