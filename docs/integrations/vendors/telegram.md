# Telegram

Direct Telegram bot. Telegram also works through [ManyChat](manychat.md).

## What it does for the agent

Customers message a Telegram bot and the agent answers in real time.

## Before you start

- A Telegram account and an existing agent.

## Partner does in Telegram

1. Search "BotFather" in Telegram → **Start** → send `/newbot`.
2. A display name (for example "Northfield HVAC").
3. A user name: 5 to 32 characters, ending in "bot", letters, digits and underscores only, not
   starting with a digit, without "telegram", not taken.
4. BotFather replies with the bot's HTTP API token. Type it into the Newo Builder (next section).
   Not into the chat. The bot is at `t.me/<bot user name>`.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Builder → **Integrations** → **+** on **Telegram Integration**. Title and Idn
   `telegram_connector` (whether the MCP can create a connector: to confirm; if not, the partner
   does this step).
2. The partner types the token into **Telegram API Token** and saves.
3. Check the connector status is **Running**.

## Test

Open the bot and press **Start**: the agent greets within seconds. Send a message; it replies.
No greeting? Check the **Running** status and the token.

## Needs Newo

None stated in the article.

## Limits and known issues

Not stated in the article.

## Source

https://help.newo.ai/en/articles/13851264-telegram-integration, read 2026-11-25.
