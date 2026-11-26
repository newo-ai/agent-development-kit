# Pipedrive

## What it does for the agent

Books meetings in the Pipedrive calendar and cancels them.

## Before you start

- A Pipedrive API key (Pipedrive's API reference says how to get it).
- Plans and roles: not stated (to confirm).

## Partner does in Pipedrive

1. Create or copy the API key, as Pipedrive's own guide describes.
2. Type it into the Newo Builder (next section). Not into the chat.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `pipedrive`, Title `pipedrive`, Module `pipedrive_integration`, Auto update
   on (Registry: not stated, to confirm). **Force Update Project**, **Publish All**.
2. The partner types into the Builder (Attributes, **Show Hidden**): `pipedrive_api_token`.
3. **Publish All**.

## Test

1. Book a time you know is free in the Pipedrive calendar; refresh Pipedrive and see it.
2. In the same conversation, cancel it; refresh and see it gone.

## Needs Newo

None stated in the article.

## Limits and known issues

Not stated in the article.

## Source

https://help.newo.ai/en/articles/13786211-pipedrive-integration, read 2026-11-25.
