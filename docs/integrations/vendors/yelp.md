# Yelp

## What it does for the agent

Answers reservation requests from new leads who come from the business's Yelp listing.

## Before you start

- The business's **Yelp Business ID** (Yelp's support explains where to find it).
- Plans: not stated (to confirm).

## Partner does in Yelp

1. Find the Yelp Business ID and tell the assistant (it is not a secret).

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `YelpReservation`, Title `YelpReservation`, Registry `production`, Module
   `yelp_reservation`, latest version, Auto update on. **Force Update Project**, **Publish All**.
2. **Integrations** > **Yelp Integration** > the `yelp_reservation` item > **Edit Settings**: enter
   the Yelp Business ID (the field's name is not stated, to confirm). **Save**.
3. **Run** the integration and wait for the status **Running**.

## Test

Not stated in the article. At least check the status is **Running** (to confirm how to send a
test lead).

## Needs Newo

None stated in the article.

## Limits and known issues

Not stated in the article.

## Source

https://help.newo.ai/en/articles/13786212-yelp-integration, read 2026-11-25.
