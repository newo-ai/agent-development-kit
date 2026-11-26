# Housecall Pro

## What it does for the agent

Schedules and cancels jobs in Housecall Pro. Checks the service area by ZIP code, offers free
times, and assigns a technician.

## Before you start

- A Housecall Pro **MAX** subscription.
- A Housecall Pro API key (Housecall Pro's own help, "API overview", says where).

## Partner does in Housecall Pro

1. Create or copy the API key, following Housecall Pro's "API overview" article.
2. Type it into the Newo Builder (next section, step 2). Not into the chat.
3. Tell the assistant how technicians are assigned: one point of contact, by job type, or by ZIP
   code.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `hcp`, Title `hcp`, Module `hcp_integration`, Auto update on (Registry: not
   stated, to confirm). **Force Update Project**, then **Publish All**.
2. The partner types the **Housecall Pro API key** into the Builder (Attributes, search `hcp`,
   **Show Hidden**; its IDN is not stated in the article, to confirm).
3. Settings, with their defaults:
   - `hcp_auto_employee_type`: `poc` (default), `job_type` or `zip_code`.
   - `hcp_booking_duration`: 2 (hours). `hcp_show_for_days`: 5. `hcp_availability_offset`: 2.
   - `hcp_time_zone`: `America/Los_Angeles`; set the business's zone.
   - `hcp_check_existing_client`: `True` (finds the caller by phone).
   - `hcp_static_data_update_interval`: 86400 seconds. `hcp_base_url`: change only for a test
     environment.
   - Do not edit `hcp_company_employees`, `hcp_location_employees`, `hcp_company_info`,
     `hcp_job_types`: the platform fills them.
4. In **Intent Type Map - ITM (Business Onboarding Interview - BOI)**, replace "Cancellation" with
   `[T] Cancellation` (starts the scenario "Cancel Reservation"). **Publish All**.
5. In **Custom Agent Scenarios**, add "Scenario 1: Schedule an Appointment" and "Scenario 11:
   Cancel Reservation" with the text from the article. Keep the code phrases word for word,
   including "I'm submitting your booking right now. Please give me a moment, and I'll get back to
   you shortly." **Publish All**.
6. Booking settings (search `booking`, **Show Hidden**): **Booking - Cancellation - Enabled**
   `True`; **Booking - Cancellation - Type** `project`; **Booking - Check Availability - Enabled**
   `True`; **Booking - Check Availability - Type** `project`; **Booking - Type** `project`; and the
   three schemas (**Create Booking**, **Check Availability**, **Meta Fields**) from the article.
   **Publish All**.

## Test

Jobs are real. Use a test customer and cancel afterwards.

1. Call or chat and schedule a job; it appears in Housecall Pro.
2. Cancel it through the agent; Housecall Pro shows it cancelled.

## Needs Newo

None stated in the article.

## Limits and known issues

Needs the MAX plan. Nothing else stated.

## Source

https://help.newo.ai/en/articles/13786208-housecall-pro-integration, read 2026-11-25.
