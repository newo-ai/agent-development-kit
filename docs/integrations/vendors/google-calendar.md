# Google Calendar

## What it does for the agent

Books a meeting at the time the caller asks for, in voice or chat, and sends calendar invites to
the business manager and the caller.

## Before you start

- No Google account to connect: the article says Newo uses its own Google Calendar account to
  create the events and invites the manager. [http-rest.md](../http-rest.md#2-calendar-appointments)
  says the owner signs in to Google in the portal (`google_calendar` connector). **The two
  disagree (to confirm with the platform team).** Read the live state with `get_integrations`.
- The manager's email, `project_business_manager_email`. A Google address shows the event in
  that calendar automatically; any other address gets an emailed invite to add by hand.

## Partner does in Google

Nothing, per the article. Tell the assistant the manager's email for invites.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Check or set **Email to Manager - Email Address** (`project_business_manager_email`). This
   address organizes the events.
2. Set **Appointment - Calendar Event Integration**
   (`project_attributes_setting_calendar_event_integration`) to `google_integration`. Save, then
   **Apply** (or publish).
3. Workflows: the library intent `[L] Closing via Appointment` and the scenario "Appointment
   Setting via Calendar Invite". If the industry has no such scenario, create it from the
   article's template. Code phrase: "I will send the calendar invite right now."
4. Optional (Builder, **Show Hidden**): **Appointment - Google Calendar Meeting - Duration**
   (minutes), **- Setup Phrase**, **- Working Hours Validation - Enabled**.

## Test

1. Ask "Can we book a demo tomorrow at 10 AM?"
2. The agent asks for phone, email, full name, date and time.
3. The manager and the test caller each get an invite; the event is in the manager's Google
   Calendar.

## Needs Newo

None stated in the article.

## Limits and known issues

- **Cannot check free slots.** It books the time the caller asks for. Need availability? Use
  [Cal.com](cal-com.md) or [Calendly](calendly.md).

## Source

https://help.newo.ai/en/articles/13786202-google-calendar-integration, read 2026-11-25.
