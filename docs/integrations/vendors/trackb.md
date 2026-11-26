# TrackB (parcel tracking)

## What it does for the agent

A customer gives a TrackB tracking number in voice or chat; the agent reads back the live
delivery status exactly as TrackB gives it.

## Before you start

- A Newo account with Builder access and the agent. No TrackB credentials: the platform manages
  access.

## Partner does in TrackB

Nothing.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `trackb`, Title `trackb`, Registry `production`, Module
   `trackb_integration`, Auto update on. **Force Update Project**, then **Publish All**.
2. Optional, **12. TrackB Settings**: `trackb_setup_scenarios` (default `True`: adds the "Delivery
   Status Lookup" scenario and intent) and `trackb_override_agent_attributes` (default `True`).
3. Check the canvas has the "Delivery Status Lookup" scenario and intent. Missing? Check
   `trackb_setup_scenarios` is `True` and publish again.

## Test

"What's the status of my delivery? My tracking number is [a real test number]." The status
matches TrackB, with no added dates or promises.

## Needs Newo

None stated in the article.

## Limits and known issues

- One tracking number per turn.
- TrackB only; other carriers are not supported.
- On request only; no proactive notices.

## Source

https://help.newo.ai/en/articles/14178619-trackb-integration, read 2026-11-25.
