# GoHighLevel

One page for the five GoHighLevel articles (integration, FAQ, settings reference, use cases,
workflow automation).

## What it does for the agent

- Books in a GoHighLevel calendar: picks the calendar, checks free slots, books, cancels.
- Finds and updates the contact; saves the conversation to the contact's notes; syncs the call
  status; moves the opportunity to a pipeline stage.
- GoHighLevel workflows can start an outbound call or a text from the agent.

## Before you start

- A GoHighLevel sub-account, a staff user linked to a calendar (**Settings** > **My Staff**), a
  calendar (**Settings** > **Calendars**), and a pipeline if stages should move
  (**Opportunities** > **Pipelines**).
- How the agent was made decides the sign-in: an agent installed from the GoHighLevel
  **Marketplace** uses OAuth (done automatically); any other agent uses a private integration
  token.
- Plans: not stated (to confirm).

## Partner does in GoHighLevel

**A. Marketplace (new agent).** **App Marketplace** → search "Newo.ai" → **Install**. The sidebar
then shows "Newo" and "Newo AI Voice Receptionist". The sign-in is done; go to C.

**B. Private integration token (existing Newo agent).**
1. **Settings** > **Private Integrations** → **Create new integration**, give it a name.
2. Turn on the scopes the article lists (contacts, conversations, calendars, businesses,
   locations, custom values and fields, opportunities, users, workflows; read and write where
   offered).
3. Copy the token and type it into the Newo Builder (`ghl_oauth_token`). Not into the chat.
4. **Settings** > **Business Profile**: copy the **Location ID** and tell the assistant.

**C. Calendar and pipeline.**
1. Add a staff user if needed, then **Settings** > **Calendars** > **Create Calendar**.
2. If stages should move: **Opportunities** > **Pipelines** → **Create Pipeline** with stage names
   (for example "New lead", "Appointment scheduled", "Not interested").
3. Tell the assistant the calendar and stage names **exactly** as written in GoHighLevel.

## Assistant does in Newo

Names from the help articles; read the live list with `get_integrations` first. Settings are
under **Attributes** > **GoHighLevel Settings**. **Publish All** after every change.

1. Not a Marketplace agent: add a project: Idn `gohighlevel`, Title `gohighlevel`, Module
   `ghl_integration` (Registry: not stated, to confirm). **Force Update Project**.
2. Sign-in: `ghl_auth_type` = `token` (path B) or `oauth` (Marketplace). With `token`, the partner
   has typed `ghl_oauth_token`; set `ghl_location_id` (**Show Hidden**). With `oauth` outside the
   Marketplace, the partner opens the link in `ghl_oauth_code`, approves, and pastes the code
   (single use). The article marks this OAuth path "in progress"; prefer the token.
3. Calendar choice, one mode only (`ghl_selection_type`):
   - `Single`: one calendar in `ghl_calendar`. The simplest and safest set-up.
   - `Name` or `Duration`: the agent picks a calendar using `ghl_selection_criteria`, which must
     return one plain-text calendar name (for example "Cleaning → Hygienist"). `Duration` needs
     one calendar per duration. These ignore `ghl_calendar`.
4. Other settings:
   - `ghl_check_availability_on_conversation_start`: offers times at the start. Only with
     `Single`.
   - `ghl_use_timezone_from_conversation`: shows slots in the caller's time zone (remote or
     international callers).
   - `ghl_enable_booking` (default `True`), `ghl_enable_cancellation`, `ghl_check_existing_client`.
   - `ghl_enable_client_history`: saves the transcript to the contact's notes ("Voice Agent
     Conversation Log").
   - `ghl_sync_conversation`: syncs the call status (completed, voicemail, busy, no-answer,
     failed, canceled) for GoHighLevel workflows.
   - `ghl_update_pipeline` and `ghl_pipeline_criteria`: rules from outcome to stage name, names
     matching GoHighLevel exactly.
5. Booking scenarios keep the code phrase "I'm submitting your booking right now. Please give me
   a moment, and I'll get back to you shortly." word for word.

**Outbound calls and texts from GoHighLevel workflows** (optional). In a GoHighLevel workflow, the
app "Newo.ai Voice AI Receptionist" offers **Make Outbound Call** and **Send text message**. The
fields: **NEWO.AI API KEY** (the partner stores the key as a GoHighLevel Custom Value such as
`newo_api_key` and references `{{custom_values.newo_api_key}}`), **CONTACT PHONE NUMBER**
(`{{contact.phone_raw}}`), **CONTACT NAME** (`{{contact.name}}`), **AGENT INSTRUCTION** ("Follow
[Scenario Name] scenario." plus details). A retry loop on "no-answer" needs a retry limit (3 to 5):
without one it never stops.

## Test

1. A test call or chat: slots are offered and the booking appears in the calendar.
2. In GoHighLevel: the contact (may lag), the conversation log if on, the call status, the
   pipeline stage.
3. In Newo, the session appears under **Sessions**.
4. A workflow: **Test Workflow** > **Select Contacts** > **Run Test** > **Execution Logs**.

## Needs Newo

None stated in the articles.

## Limits and known issues

- One calendar-selection mode at a time; `Name` and `Duration` do not combine.
- Calendar and stage names must match exactly (case, spaces, punctuation).
- Pre-loading availability does not work with `Name` or `Duration`.
- Nothing takes effect before **Publish All**.
- Saving the conversation history does not change how the agent behaves.

## Source

Read 2026-11-25:
- https://help.newo.ai/en/articles/13673964-gohighlevel-integration
- https://help.newo.ai/en/articles/13860268-gohighlevel-faq
- https://help.newo.ai/en/articles/13860269-gohighlevel-settings-reference
- https://help.newo.ai/en/articles/13860270-gohighlevel-use-cases-and-scenarios
- https://help.newo.ai/en/articles/13860271-gohighlevel-workflow-automation
