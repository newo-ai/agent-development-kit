# Denticon

**Health data.** Apply [Health data](../README.md#health-data) before you connect.

## What it does for the agent

Books, cancels and looks up appointments in Denticon, and tells a caller about their upcoming
appointment.

## Before you start

- A Denticon account with OAuth 2.0 credentials: **Client ID**, **Client Secret** and a
  **Subscription Key** (`PDDS-Subscription-Key`).
- Where in Denticon these are created: not stated (to confirm).
- Plans and versions: not stated (to confirm).

## Partner does in Denticon

1. Get the Client ID, Client Secret and Subscription Key for the practice (the article does not
   describe the Denticon screens; work it out with the practice or Denticon).
2. Type them into the Newo Builder (next section, step 2). Not into the chat.
3. Tell the assistant which office the agent books for.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn and Title `DenticonIntegration`, Module `denticon_integration`, Auto update
   on (Registry: not stated in the article, to confirm). **Force Update Project**, **Publish All**.
2. The partner types into the Builder (Attributes): `denticon_client_id`,
   `denticon_client_secret`, `denticon_subscription_key`. Then **Publish All**.
3. In **12. Denticon Settings**, set **Denticon Office (Location)** (`denticon_location_id`) to the
   practice's office. **Publish All**.
4. Scenarios, from the library: **2: Scheduling Appointment via Agent** and the procedures for
   name, phone, services, preferred date and time, date of birth and email.
5. Custom scenarios, with the full text from the article: **Scenario 6: "Canceling Appointment via
   Agent"** and **Scenario 13: "Upcoming appointment information Scenario"**. Keep their code
   phrases word for word (for example "Give me a moment, I will cancel your booking right now.").
   Editing scenario cards: [SOP](../../sop/edit-a-scenario.md).
6. Intents: clone and update `[L] New Patient Appointment`; create `[T] Cancellation via Agent` and
   `[T] Upcoming appointment information`, each linked to its scenario. **Publish All**.

## Test

Bookings are real. Use a test patient.

1. Book a test appointment; it appears in Denticon for the chosen office.
2. Ask about the upcoming appointment; the agent finds it.
3. Cancel it; Denticon shows it cancelled.

## Needs Newo

None stated in the article.

## Limits and known issues

Not stated in the article.

## Source

https://help.newo.ai/en/articles/14019479-denticon-integration, read 2026-11-25.
