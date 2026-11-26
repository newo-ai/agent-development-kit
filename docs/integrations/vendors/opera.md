# Oracle Opera (hotels)

Hotel room reservations only. Restaurant bookings use other integrations, for example
[Mozrest](mozrest.md).

## What it does for the agent

Checks room availability by dates, guests and rooms; books (returns a reservation id); cancels;
changes dates. Can add booking and cancellation scenarios on publish.

## Before you start

From Oracle Opera: API access, an OAuth2 Client ID and Secret, an App Key, the Enterprise ID, the
Hotel ID, the API base URL and the OAuth scope. Where in Opera these come from: not stated (to
confirm). Plans and versions: not stated (to confirm).

## Partner does in Opera

1. Get the credentials above for the hotel from its Opera administrator or Oracle.
2. Type the secret ones into the Newo Builder (next section). Not into the chat.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first. The article has no
project step (to confirm whether a project from a module is needed).

1. Set `opera_base_url`, `opera_enterprise_id`, `opera_hotel_id`, `opera_scope`.
2. The partner types into the Builder (Attributes): `opera_app_key`, `opera_client_id`,
   `opera_client_secret`.
3. Optional: `opera_enable_slot_check`, `opera_enable_booking`, `opera_enable_cancellation`
   (default `True`), `opera_static_data_update_interval` (seconds). `opera_setup_scenarios`
   (default `True`) must be set before the **first** publish: it adds the scenarios then.
4. **Publish All**. `opera_access_token` is set when sign-in worked. Empty? Check the credentials
   and publish again.

## Test

Every reservation is live in the hotel's PMS. Use test dates and cancel afterwards.

1. `opera_access_token` is set.
2. Ask for rooms on given dates; offers come back with rates.
3. Book; a reservation id comes back and the booking is in Opera.
4. Cancel by reservation id; Opera shows it cancelled.
5. Change the dates; Opera shows the new ones.

## Needs Newo

None stated in the article.

## Limits and known issues

Hotel rooms only. Nothing else stated.

## Source

https://help.newo.ai/en/articles/14121851-opera-integration, read 2026-11-25.
