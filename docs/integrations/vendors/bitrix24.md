# Bitrix24

## What it does for the agent

- Checks free slots, books, cancels and suggests times, as calendar events with a linked contact.
- Creates a deal at the end of a conversation, given to the employee with the fewest open deals.
- Creates leads from outside sources (such as Yelp), creates tasks, finds or creates contacts.

## Before you start

- A Bitrix24 account (cloud or on-premises).
- A Bitrix24 OAuth app with a **Client ID** and **Client Secret** (how to create it in Bitrix24:
  not stated in the article, to confirm).
- A calendar on the owner user (usually the admin, user ID 1).

## Partner does in Bitrix24

1. Create the OAuth app and keep its Client ID and Client Secret.
2. Type both into the Newo Builder (next section). Not into the chat.
3. Open the Bitrix24 authorization link from the Builder, sign in, approve the Newo app.
4. Copy the code from the address bar after the redirect and paste it into `bitrix_oauth_code`.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first. The article has no
project step (to confirm whether a project from a module is needed).

1. Set `bitrix_base_url` (for example `https://northfieldhvac.bitrix24.com`; on-premises works
   with its own address).
2. The partner types `bitrix_client_id`, `bitrix_client_secret` and, after authorizing,
   `bitrix_oauth_code`. **Publish All**: tokens, working hours and the tools are set up.
3. Optional (defaults): `bitrix_owner_id` (1), `bitrix_duration` (60), `bitrix_availability_days`
   (1), `bitrix_employee_position_name` (`cleaner`; set the job title that takes deals),
   `bitrix_create_deal_on_conversation_end` (`True`),
   `bitrix_check_availability_on_conversation_start` (`False`), `bitrix_enable_slot_check`,
   `bitrix_enable_booking`, `bitrix_enable_cancellation`, `bitrix_enable_task_creation`,
   `bitrix_enable_lead_creation` (all `True`).

## Test

Test records go into the live CRM. Use a test contact and remove the records afterwards.

Test each flow in a chat: availability, booking, cancellation, the deal at the end, a task.
Nothing happens? Check the credentials, the owner's calendar and the feature switches.

## Needs Newo

None stated in the article.

## Limits and known issues

- No reschedule: cancel and book again.
- One calendar only.

## Source

https://help.newo.ai/en/articles/14121843-bitrix24-integration, read 2026-11-25.
