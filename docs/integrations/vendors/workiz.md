# Workiz

## What it does for the agent

Schedules and cancels service jobs in Workiz.

## Before you start

- An active Workiz account with at least one team member who can be dispatched.
- The Workiz API Key and API Secret.

## Partner does in Workiz

1. **Settings** > **Integrations** > **API**: copy the API Key and API Secret.
2. Type them into the Newo Builder (next section, step 2). Not into the chat.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `workiz`, Title `workiz`, Registry `production`, Module
   `workiz_integration`, Auto update on. **Force Update Project**, **Publish All**.
2. The partner types into the Builder (Attributes, search `workiz`, **Show Hidden**):
   `workiz_api_key`, `workiz_api_secret`. **Publish All**: the team and the job types
   (`workiz_job_types`, do not edit) load.
3. Booking settings (search `booking`, **Show Hidden**): **Booking - Cancellation - Enabled**
   `True`, **Booking - Cancellation - Type** `project`, **Booking - Type** `project`.
   **Publish All**.
4. In **Intent Type Map - ITM (Business Onboarding Interview - BOI)**, replace "Cancellation" with
   the article's text (starts the scenario "Cancel Reservation"). **Publish All**.
5. In **Custom Agent Scenarios**, add "Scenario 1: Schedule a Service Job" and "Scenario 11: Cancel
   Reservation" from the article. Keep "I'm submitting your booking right now. Please give me a
   moment, and I'll get back to you shortly." word for word: without it no booking is made.
   **Publish All**.

## Test

Jobs are real. Use a test customer.

1. Schedule a job; it appears in Workiz with the customer and a technician.
2. Cancel it; check the job status in Workiz.

## Needs Newo

None stated in the article.

## Limits and known issues

No availability check, no reschedule, no payments.

## Source

https://help.newo.ai/en/articles/14178613-workiz-integration, read 2026-11-25.
