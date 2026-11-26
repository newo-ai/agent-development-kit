# PosHUB

## What it does for the agent

Customers place, check and cancel orders by voice, SMS or chat, from a menu kept in sync.

## Before you start

- A PosHUB account with external API access, admin or reseller credentials, and access to the
  PosHUB Developer Portal.
- At least one published menu in a PosHUB location. Builder publish rights.
- 15 to 45 minutes. **The order of the steps matters.**

## Partner does in PosHUB

1. In the Newo Builder, type the PosHUB admin credentials (next section, step 2). Not into the
   chat.
2. After the first publish, copy the webhook URLs from the Builder settings.
3. PosHUB Developer Portal: create an application in the **Marketplace** category; paste the Newo
   webhook URLs into its webhook fields.
4. Type its **Client ID** and **Client Secret** into the Builder. Tell the assistant the
   **Reseller ID** from the PosHUB dashboard address.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first. The article does
not give the setting names for the credentials (to confirm).

1. Add a project: Idn `poshub`, Title `poshub`, Registry `production`, Module
   `poshub_integration`, Auto update on. **Force Update Project**.
2. First publish: after the admin credentials, **Publish All**. This creates the webhook URLs.
3. Final publish: after the Client ID, Client Secret and Reseller ID, **Publish All**. Choose the
   location, **Publish All** again.
4. Keep the trigger phrases unchanged and untranslated, for example "I will place your order
   right now and come back with the confirmation."

## Test

Orders are real. Agree a test order with the restaurant.

1. The location is chosen.
2. Ask about a menu item; only synced items are offered.
3. Place an order and see it in PosHUB. Ask for its status. Cancel it and check PosHUB's answer.

## Needs Newo

None stated in the article. If sign-in fails, PosHUB support may need to enable the password
grant.

## Limits and known issues

- One location per project. Payment is handled by PosHUB.
- Cancelling depends on PosHUB's rules for the order's state.
- Menu refreshes on the first publish, when a menu is published in PosHUB, and every 6 hours.
- The agent ignores orders? A trigger phrase was changed: restore it and publish.

## Source

https://help.newo.ai/en/articles/15552864-poshub-integration, read 2026-11-25.
