# Syrve

## What it does for the agent

Takes food delivery orders, checks order status, and keeps the menu in sync.

## Before you start

- A Syrve account with API access and an API key (`apiLogin`).
- At least one organization and terminal group, and a filled menu.
- Plans: not stated (to confirm).

## Partner does in Syrve

1. Sign in to the Syrve management console → API settings.
2. Copy the API key (`apiLogin`) and type it into the Newo Builder (`syrve_api_key`). Not into
   the chat.
3. Tell the assistant the API region (EU by default: `https://api-eu.syrve.live`).

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `syrve`, Title `syrve`, Registry `production`, Module `syrve_integration`,
   Auto update on. **Force Update Project**, **Publish All**.
2. After the partner's key (Attributes, search `syrve`, **Show Hidden**): `syrve_base_url` for
   the region; `syrve_delivery_menu_update_interval` (86400 seconds);
   `syrve_override_agent_attributes` (`True`). Do not edit `syrve_access_token`,
   `syrve_organization_id`, `syrve_terminal_group_id`, `syrve_delivery_menu`.
3. **Publish All**. `syrve_access_token` and `syrve_organization_id` are set. Empty? Check the key
   and publish again.

## Test

Orders are real (marked `voice-agent` in Syrve). Agree a test order with the restaurant.

1. `syrve_access_token` and `syrve_organization_id` are set.
2. Start a conversation; the menu (`syrve_delivery_menu`) is filled.
3. "I want to order a [menu item] to [address]." Check the order in Syrve.
4. "What's the status of my order?"

The agent needs first name, phone number (the customer must already exist in Syrve), delivery
address.

## Needs Newo

None stated in the article.

## Limits and known issues

- No modifiers, no table reservations, no payments, no order changes after creation.
- The first terminal group is used.
- An item not matched in the menu returns "product not found".

## Source

https://help.newo.ai/en/articles/14121854-syrve-integration, read 2026-11-25.
