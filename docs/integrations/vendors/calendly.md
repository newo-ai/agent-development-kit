# Calendly

## What it does for the agent

Checks free slots, books and cancels meetings in Calendly.

## Before you start

- Calendly **Professional** plan or higher.
- An event type with the location **Phone Call** (Calendly calls the invitee).

## Partner does in Calendly

1. Calendly Developer Portal (`https://developer.calendly.com`): register a new web application.
2. Redirect URI `https://static.newo.ai/auth.html`. Turn on all scopes for scheduling, user
   management, security and webhooks. Save.
3. Type the **Client ID** and **Client Secret** into `calendly_client_id` and
   `calendly_client_secret` in the Newo Builder. Not into the chat.
4. Open the event type for the agent; set its location to **Phone Call**.
5. After the assistant's first publish: in the Builder, **12. Calendly Settings** →
   `calendly_oauth_code` → **open Calendly authorization page**. Approve, then **Copy Code** on the
   Newo **Access Granted** page and paste it into `calendly_oauth_code`. **Save** on that card.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `calendly`, Title `calendly`, Registry `production`, Module
   `calendly_integration`, Auto update on. **Force Update Project**.
2. After the client ID and secret: **Publish All**.
3. After the code: **Publish All**, reload. `calendly_oauth_code` must now be empty (the code was
   exchanged). Not empty? It expired: repeat the partner's step 5.
4. Choose `calendly_event_type_uri`. Set **Booking - Enabled**
   (`project_attributes_setting_booking_enabled`) to `True` and
   `project_attributes_setting_calendar_event_integration` to `calendly_integration`.
   **Publish All**.
5. Optional (**Show Hidden**): **Calendly - Slot Window Duration** (days; default 5, max 7),
   **Calendly - Slot Duration** (minutes; default 30), and switches for availability, booking and
   cancellation (their names are not stated, to confirm).
6. Workflows: as for [Cal.com](cal-com.md#assistant-does-in-newo), step 5 (the Calendly scenario
   asks for the phone number with country code and has no date of birth).

## Test

Call or chat: "I'd like to schedule an appointment." The agent offers slots; the meeting appears
in Calendly. Cancel it afterwards.

## Needs Newo

None stated in the article.

## Limits and known issues

- Looks at most 7 days ahead.
- The authorization code works once.
- `calendly_integration` is not in the list of values in
  [http-rest.md](../http-rest.md#2-calendar-appointments) (to confirm with the platform team).

## Source

https://help.newo.ai/en/articles/14178615-calendly-integration, read 2026-11-25.
