# Cal.com

## What it does for the agent

Checks free slots and books, cancels or reschedules meetings in Cal.com.

## Before you start

- A Cal.com account (free or paid) with the meeting type (event type) set up.

## Partner does in Cal.com

1. Create an API key, as Cal.com's API reference describes.
2. Type it into **CalCom API Token** (`calcom_api_token`) in the Newo Builder. Not into the chat.
3. Tell the assistant which meeting the agent books, and personal or team.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `calcom`, Title `calcom`, Registry `production`, Module
   `cal_com_integration`, Auto update on. **Force Update Project**.
2. After the token: **Publish All** and reload. `calcom_event_type` and `calcom_event_mode`
   appear. A new meeting in Cal.com may need another **Publish All** to show.
3. Set `calcom_event_type` (the meeting) and `calcom_event_mode` (**Personal** or **Team**).
4. Set **Booking - Enabled** (`project_attributes_setting_booking_enabled`) to `True`, and
   `project_attributes_setting_calendar_event_integration` to `calcom_integration`.
   **Publish All**.
5. Workflows: the intent `[L] New Patient Appointment` and "Scenario 2: Scheduling Appointment via
   Agent" from the article (a dental example: adapt the wording to the business, keep the code
   phrases). Make sure no other intent schedules appointments, or they clash.

## Test

Call or chat: "I'd like to schedule an appointment." The meeting appears in Cal.com. Cancel it
afterwards.

## Needs Newo

None stated in the article.

## Limits and known issues

Only one scheduling intent at a time. Nothing else stated.

## Source

https://help.newo.ai/en/articles/13786201-cal-com-integration, read 2026-11-25.
