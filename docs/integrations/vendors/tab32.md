# Tab32

**Health data.** Apply [Health data](../README.md#health-data) before you connect.

## What it does for the agent

- Checks free slots by date, time and location; books (creates the patient if none is found);
  cancels by booking id.
- Finds the patient by phone number and name. Converts times to the clinic's time zone.
- With several locations, matches the caller's description to an office.

## Before you start

- A Tab32 account with API access and its **PDDS-Subscription-Key**.
- Plans and versions: not stated (to confirm).

## Partner does in Tab32

1. Sign in to Tab32 and open the API management section.
2. Generate or find the `PDDS-Subscription-Key` and copy it.
3. Type it into the Newo Builder (next section). Not into the chat.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first. The article has no
project step (to confirm whether a project from a module is needed).

1. The partner types into the Builder (Attributes): **Tab32 API Key** (`tab32_api_key`).
2. Optional: `tab32_base_url` (default `https://openapi.tab32.com/api`), `tab32_multilocation`
   (default `True`; `False` uses one preselected location), `tab32_slot_duration` (15, 30, 45 or 60;
   default 30), `tab32_enable_booking`, `tab32_enable_cancellation`, `tab32_enable_slot_check`,
   `tab32_check_existing_client`, `tab32_enable_client_history`.
3. **Publish All**. The platform checks the key and loads the clinic locations
   (`tab32_offices`). Check `location_time_zone`.

## Test

Bookings are real. Use a test patient.

1. After publish, the logs show the locations were loaded.
2. Ask "What slots are available on Monday?"
3. Book; it appears in the Tab32 dashboard.
4. Cancel; the status changes in Tab32.

## Needs Newo

None stated in the article.

## Limits and known issues

- No reschedule: cancel and book again.
- Only appointments made after activation; no history import.
- One Tab32 key per integration; several accounts need several instances.

## Source

https://help.newo.ai/en/articles/14121852-tab32-integration, read 2026-11-25.
