# Kommo

## What it does for the agent

Finds or creates the contact by phone or email, finds or creates the lead, and moves it to a
pipeline stage after the conversation, following rules you write in plain words.

## Before you start

- A Kommo account where you can create an integration under **Settings**.
- Plans and roles: not stated (to confirm).

## Partner does in Kommo

1. **Settings** → **Create Integration** (top right).
2. **Redirect URL** `https://static.newo.ai/auth.html`; **Integration name** `Newo.ai`; a short
   description. **Save**.
3. **Keys and scopes** tab → **Generate secret key**.
4. Type into the Newo Builder (not into the chat): the secret key in `kommo_client_secret`, the
   **Integration ID** in `kommo_client_id`, the **Authorization code** in `kommo_oauth_code`
   (where Kommo shows the code: not stated in the article, to confirm).
5. Tell the assistant the Kommo subdomain (`northfieldhvac` for `northfieldhvac.kommo.com`) and
   the pipeline stage names, exactly as written in Kommo.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `KommoIntegration`, Title `KommoIntegration`, Registry `production`, Module
   `kommo_integration`, Auto update on. **Force Update Project**, **Publish All**.
2. After the partner's step 4, set `kommo_subdomain`. **Publish All**: the code is exchanged for
   tokens (`kommo_access_token`, `kommo_refresh_token`; say "set", never show them).
3. Optional: `kommo_pipeline_decision_rules`, one rule per stage, for example "Stage 'Initial
   Contact': Select this stage IF the user just asked general questions."

## Test

Call or chat as a test caller. A contact appears in Kommo, in the right pipeline stage.

## Needs Newo

None stated in the article.

## Limits and known issues

A rule that names a stage which does not exist can make the lead update fail. Stage names must
match exactly.

## Source

https://help.newo.ai/en/articles/13786215-kommo-integration, read 2026-11-25.
