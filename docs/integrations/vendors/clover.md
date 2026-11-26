# Clover

## What it does for the agent

Reads the menu or inventory, creates orders and cancels orders in Clover.

## Before you start

- A Clover account where you can create an app (plans: not stated, to confirm).

## Partner does in Clover

1. Sign in. **My Apps** → **Create new app**.
2. An **App name** (for example "NewoIntegration"), the **Countries**, **Next**.
3. **Payment app**, **Next**. Tick **Web**. **Create app**.
4. On **App Settings**, copy the **App ID** and **App Secret** and type them into
   `clover_app_id` and `clover_app_secret` in the Newo Builder. Not into the chat.
5. In the Builder, open the link in the `clover_oauth_code` description, sign in to Clover,
   authorize, and paste the code Clover shows into `clover_oauth_code`.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `CloverIntegration`, Title `CloverIntegration`, Registry `production`,
   Module `clover_integration`, Auto update on. **Force Update Project**.
2. After the partner's steps: **Publish All**. Then `clover_oauth_code` is empty and
   `clover_access_token`, `clover_refresh_token` are set (say "set", never show them).
3. Add the intents and scenarios from the article: Scenario 0 "Introduction", intent
   "[L] Create an Order", intent "[T] Cancellation", Scenario 2 "Create an Order", Scenario 6
   "Canceling Existing Order", Scenario 20 "Finish Conversation". Remove nothing, but make sure no
   other intent or scenario competes with them (ask the partner). Keep the code phrases word for
   word: "I'm submitting your order right now. Please give me a moment, and I'll get back to you
   shortly." and "I'm canceling your order right now." Editing cards:
   [SOP](../../sop/edit-a-scenario.md).

## Test

Orders are real. Agree a test order with the business.

1. Place a test order; check it in Clover.
2. Cancel it through the agent; check it is cancelled in Clover.

## Needs Newo

None stated in the article.

## Limits and known issues

Not stated in the article.

## Source

https://help.newo.ai/en/articles/13786217-clover-integration, read 2026-11-25.
