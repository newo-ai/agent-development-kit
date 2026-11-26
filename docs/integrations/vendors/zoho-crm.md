# Zoho CRM

## What it does for the agent

Books in the Zoho CRM Events calendar: checks free slots, books, cancels. Finds or creates the
contact, creates leads and deals, and adds conversation notes.

## Before you start

- A Zoho CRM account with admin rights.
- Its data centre: `.com`, `.eu`, `.in` or `.au`.
- Plans: not stated (to confirm).

## Partner does in Zoho CRM

1. Open the Zoho authorization link from the Newo Builder (next section, step 2).
2. Sign in and approve the scopes the Newo app asks for.
3. Copy the code from the address bar after the redirect and paste it into `zoho_oauth_code` in
   the Builder. The code works once and expires fast: paste it at once.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first. The article has no
project step (to confirm whether a project from a module is needed).

1. Set `zoho_region` (`com`, `eu`, `in`, `au`; default `com`).
2. The partner does the Zoho steps above. **Publish All**.
3. Check `zoho_access_token` is set (say "set", do not show it). Empty? Authorize again, publish
   again.
4. Optional: `zoho_timezone`, `zoho_duration` (default 30), `zoho_availability_days`,
   `zoho_enable_slot_check`, `zoho_enable_booking`, `zoho_enable_cancellation` (default `True`),
   `zoho_update_pipeline` (default `False`) with `zoho_pipeline_criteria`,
   `zoho_check_existing_client` (default `True`), `zoho_check_availability_on_conversation_start`
   (default `False`). `zoho_user_id` fills itself.

## Test

Every write is live in the CRM. Use a test contact.

1. Ask "What slots are available this week?"
2. Book; check **Activities** > **Events**. Cancel; it is gone.
3. After the conversation: a lead (new caller), a note on the contact (returning caller), a deal
   (if `zoho_update_pipeline` is on).

## Needs Newo

None stated in the article.

## Limits and known issues

- No reschedule: cancel and book again.
- One Zoho account and user per integration. No import of old CRM data.
- Contacts are found by phone number.
- After changing credentials, **Publish All**.

## Source

https://help.newo.ai/en/articles/13786210-zoho-crm-integration, read 2026-11-25.
