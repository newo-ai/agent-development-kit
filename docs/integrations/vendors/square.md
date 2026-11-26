# Square (Square Appointments)

## What it does for the agent

Checks free appointment times, books and cancels through Square Appointments, and syncs the
service list at the start of every conversation.

## Before you start

- A Square account (free or paid) with owner or admin access, and Square Appointments on.
- A desktop browser: the Square Developer Dashboard does not work on a phone. Its **Production**
  tab needs a verified account.
- A test account or a location that takes no real customers: every booking is real.

## Partner does in Square

**Developer app** (`https://developer.squareup.com/apps`):
1. **+ New Application**, a name (for example "Newo AI Assistant"), accept the terms, **Next**.
2. Select **Build customer relationships**, **Manage a team**, **Manage a product catalog**,
   **Next**; then **Myself**, **Complete**.
3. **Credentials** → the **Production** tab (not Sandbox).
4. Type the **Application ID** (starts `sq0idp-`) into `square_client_id` and the **Personal
   Access Token** (starts `EAAA`) into `square_secret_id` in the Newo Builder. Not into the chat.

**Appointments** (Square Dashboard):
1. **... Add more** → **Bookings** → **Add** next to Appointments → **Start setup**.
2. **Settings → Account & Settings → My business → Locations**: time zone and regular hours.
3. **Staff → Team → Team members**: at least one team member.
4. **Items & services → Items → Service library**: services with price and duration, **Bookable
   by customers online** on, team members assigned.
5. **Staff → Scheduling → Availability**: working times per team member. Without these green
   blocks there are no slots.

**Authorize**: open the link in the `square_oauth_code` description in the Builder, sign in,
**Allow**. Copy the value after `code=` (up to the next `&`) from the address bar and paste it into
`square_oauth_code`. It works once.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first. The article has no
project step (to confirm whether a project from a module is needed).

1. After the partner's steps: **Publish All**. The code is exchanged for tokens and
   `square_locations` fills.
2. Choose the location in `square_locations` (one per instance). Publish again if needed.
3. Optional (default `True`): `square_enable_slot_check`, `square_enable_booking`,
   `square_enable_cancellation`. Leave `square_base_url` and `square_login_url` as they are.

## Test

1. After publish, `square_locations` is filled.
2. Start a conversation; the service list (`square_catalog`) is filled.
3. Ask "Any openings for [service] tomorrow?"; slots come back with a team member.
4. Book; it appears in Square Bookings. Cancel; it is gone.

## Needs Newo

None stated in the article.

## Limits and known issues

- No reschedule: cancel and book again. No payments.
- One location per instance.
- Services must be appointment services in the Service library.
- Booking needs the caller's phone number and first and last name.

## Source

https://help.newo.ai/en/articles/14121853-square-integration, read 2026-11-25.
