# Eaglesoft (through Kolla)

Eaglesoft connects through Kolla: a Kolla connector on the practice's computer reads the PMS. All
steps are on the [Kolla page](kolla.md); this page lists what is different.

**Health data.** Apply [Health data](../README.md#health-data) before you connect.

## What it does for the agent

Checks free slots, books new and existing patients, cancels, and finds the patient by the
caller's phone number, in the practice's Eaglesoft schedule.

## Before you start

- Eaglesoft, **on-premises** only. A cloud-only PMS cannot be reached.
- Everything in [Kolla, "Before you start"](kolla.md#before-you-start).
- Plans and versions: not stated (to confirm).

## Partner does in Eaglesoft

Nothing in Eaglesoft itself beyond the on-premises check. The partner does the Kolla steps:
[Kolla, "Partner does in Kolla"](kolla.md#partner-does-in-kolla), choosing the Eaglesoft connector.
The practice's administrator installs the Kolla connector on the computer where Eaglesoft runs.

## Assistant does in Newo

As on the [Kolla page](kolla.md#assistant-does-in-newo), with `kolla_connector_id` = `eaglesoft`.
Read the live names with `get_integrations` first.

## Test

As on the [Kolla page](kolla.md#test): slots, a booking in Eaglesoft tagged "(NP)", a cancellation.

## Needs Newo

None stated in the article.

## Limits and known issues

- No reschedule: cancel and book again.
- Cloud-only editions are not reachable.

## Source

https://help.newo.ai/en/articles/15825118-eaglesoft-integration, read 2026-11-25.
