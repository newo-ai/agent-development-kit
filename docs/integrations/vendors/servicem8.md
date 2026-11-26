# ServiceM8

## What it does for the agent

Checks free times, books field-service jobs (creates the customer), reschedules, cancels, looks
up job status, and takes quote requests. Multi-site requests go to a human dispatcher.

## Before you start

- A ServiceM8 account with staff and job categories (**Settings** > **Job Categories**).
- Builder access with publish rights.

## Partner does in ServiceM8

1. **Settings** > **Developer** > **API Keys**: create a key.
2. Copy it exactly, with no spaces before or after.
3. Type it into the Newo Builder (next section, step 2). Not into the chat.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `servicem8`, Title `servicem8`, Registry `production`, Module
   `sm8_integration`, Auto update on. **Force Update Project**.
2. The partner types into the Builder (Attributes, **Show Hidden**): `servicem8_api_key`.
3. **Publish All**. The platform checks the key and fills the staff and job category lists.
4. Set `servicem8_default_staff_uuid` (required) and, if wanted,
   `servicem8_default_category_uuid`. Optional: `servicem8_activity_duration_minutes` (default
   60). **Publish All** again.
5. Keep the trigger phrases unchanged, for example "Give me a moment, I will book your service job
   right now."

## Test

Jobs are real. Use a test customer.

1. Offered times match the default staff member's schedule.
2. Book; the job and the new customer appear in ServiceM8.
3. Reschedule; the job moves.
4. Cancel; the job is marked **Unsuccessful**.
5. Look the job up; the details are read back correctly.

## Needs Newo

None stated in the article.

## Limits and known issues

- One staff member per project; the caller cannot pick one.
- One job per call; one ServiceM8 account per project.
- The agent takes no payments.

## Source

https://help.newo.ai/en/articles/15825115-servicem8-integration, read 2026-11-25.
