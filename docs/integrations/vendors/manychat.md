# ManyChat (WhatsApp, Instagram, Facebook, TikTok, Telegram)

One page for the three ManyChat articles: the channel connection, WhatsApp messages instead of
SMS, and WhatsApp reports.

## What it does for the agent

- **Channels:** the agent answers messages from Instagram, Facebook, WhatsApp, TikTok and
  Telegram through one ManyChat account.
- **WhatsApp instead of SMS (optional):** the agent's notices (an order link, a booking
  confirmation) go by WhatsApp from the business's WhatsApp Business number. Useful where SMS is
  strictly regulated or WhatsApp is preferred (Spain and Europe, the UAE, many Asian markets).
- **WhatsApp reports (optional):** after each conversation, a summary goes by WhatsApp to the
  right person, by intent and working hours.

## Before you start

- ManyChat **Pro** or higher, with the social channels already connected in ManyChat.
- For WhatsApp: a WhatsApp Business number connected in ManyChat. Meta Business Verification can
  take days.

## Partner does in ManyChat

**Channels:**
1. Open the Newo.ai ManyChat template (link in the article) → **Install** → choose the business's
   ManyChat account → **Install Now**.
2. **Automation** > **My Automations** > the Newo folder: the Default Reply flows are there.
3. **Settings** > **API** → **Generate Your API Key**. Type it into the Newo Builder
   (`project_attributes_setting_manychat_api_token`). Not into the chat.
4. **Settings** > **Channels**: for each platform, set **Default Reply** to the matching Newo.ai
   template (for example "Default Reply Telegram V.2").
5. In each platform's template, the first "When..." step → **When this happens** → "every time".

**WhatsApp instead of SMS:**
1. Install the Newo.ai WhatsApp Information Template (link in the article) on the same account.
2. **Settings** > **Channels** > **WhatsApp** > **Message Templates** → "Initial greeting": a short
   message (for example "Please confirm receipt of the messages.") and a reply button ("Ok").
   **Save**. The first WhatsApp message must use this approved template.

## Assistant does in Newo

Names from the help articles; read the live list with `get_integrations` first.

**Channels:**
1. Add a project: Idn `manychat`, Title `manychat`, Registry `production_newo`, Module
   `manychat`, Auto update on. **Force Update Project**.
2. After the partner's API key: **Publish All**.
3. **Integrations**: the ManyChat connectors under "API Integration" show **Running**.

**WhatsApp instead of SMS:** set `project_attributes_setting_manychat_use_whatsapp_to_send_information`
to `true` (**Show Hidden**). **Publish All**. Keep the old value: turning it off again does not
bring SMS back on its own, the partner reverts the instructions by hand.

**WhatsApp reports:**
1. Needs `project_attributes_setting_manychat_use_whatsapp_to_send_information` `true` and
   `project_attributes_setting_session_ended_report_enabled` `True` (this one also controls email
   and SMS reports).
2. Write `project_attributes_setting_manychat_whatsapp_report_criteria_template`, in the article's
   format: "During working hours" and "Outside working hours", each with rules like "If it is
   <Intent Type> send a WhatsApp message to [[project_business_working_hour_escalation_phone]]".
   Intent names must match the Workflows page exactly. Default: no reports.
3. The report text comes from `project_attributes_setting_session_ended_report_content`.
   **Publish All**.

## Test

1. Send a test message on each connected channel; the agent replies. No reply? Repeat the steps.
2. WhatsApp instead of SMS: a notice arrives on WhatsApp and the test phone can tap "Ok".
3. Reports: a test conversation that matches an intent, then end it; the report reaches the
   number the template routes to.

## Needs Newo

None stated in the articles.

## Limits and known issues

- WhatsApp instead of SMS is set up by hand per business and cannot yet fully replace SMS at
  scale. It cannot tell whether a caller has WhatsApp.
- Turning it off does not restore SMS.

## Source

Read 2026-11-25:
- https://help.newo.ai/en/articles/13786205-manychat-integration-whatsapp-telegram-instagram-facebook-tiktok
- https://help.newo.ai/en/articles/13786206-manychat-integration-whatsapp-messaging-as-sms-alternative
- https://help.newo.ai/en/articles/13860272-configure-whatsapp-reports-for-manychat
