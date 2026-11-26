# Odoo

## What it does for the agent

- Recognizes the caller by phone number.
- Appointments: free slots, book, reschedule, cancel, look up.
- Orders: status, add a note, start a return, price quotes (Sales module).
- Service requests as CRM leads: create, update, check, cancel (CRM module).

## Before you start

- Odoo with external API access: a Custom plan on Odoo.com, or self-hosted Community or
  Enterprise.
- Admin access, and a dedicated API user with rights to Calendar, Sales Orders and CRM Leads.

## Partner does in Odoo

1. **Settings** > **Users** → the API user → **Security** tab → **Add API Key**.
2. Confirm the password, set a duration, **Generate**. Copy the key at once: it is shown once.
3. Type the key into the Newo Builder (next section). Not into the chat.
4. Tell the assistant the instance address without a trailing slash (for example
   `https://northfieldhvac.odoo.com`) and the API user's email.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `odoo_integration`, Title `odoo_integration`, Registry `production`, Module
   `odoo_integration`, Auto update on. **Force Update Project**.
2. Set `odoo_base_url` and `odoo_username`. The partner types `odoo_api_key` (Attributes, search
   `odoo`, **Show Hidden**).
3. **Publish All**: eight scenarios are added. Their trigger phrases must not be edited,
   translated or shortened.

## Test

Every write is live. Use a test contact.

1. Call from the test contact's number; the agent greets them by name.
2. Book, reschedule, cancel; check the Odoo calendar each time.
3. Orders: status, a note, a return. Service requests: create one and see it in CRM.

## Needs Newo

None stated in the article.

## Limits and known issues

- One Odoo database per project. Order data is read on demand; no order webhooks.
- Only the API user's currency.
- "Account not found": the phone number in Odoo is in another format.
- After a new key: paste it into `odoo_api_key` and **Publish All**.

## Source

https://help.newo.ai/en/articles/15552857-odoo-integration, read 2026-11-25.
