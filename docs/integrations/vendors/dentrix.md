# Dentrix (through Kolla)

Dentrix connects through Kolla: a Kolla connector on the practice's computer reads the PMS. All
steps are on the [Kolla page](kolla.md); this page lists what is different.

**Health data.** Apply [Health data](../README.md#health-data) before you connect.

## What it does for the agent

Checks free slots, books new and existing patients, cancels, and finds the patient by the
caller's phone number, in the practice's Dentrix schedule.

## Before you start

- Dentrix Core and Dentrix Enterprise, **on-premises** only. The cloud edition cannot be reached through Kolla.
- Everything in [Kolla, "Before you start"](kolla.md#before-you-start).
- Plans and versions: not stated (to confirm).

## Partner does in Dentrix

Nothing in Dentrix itself beyond the on-premises check. The partner does the Kolla steps:
[Kolla, "Partner does in Kolla"](kolla.md#partner-does-in-kolla), choosing the Dentrix connector.
The practice's administrator installs the Kolla connector on the computer where Dentrix runs.

## Assistant does in Newo

As on the [Kolla page](kolla.md#assistant-does-in-newo), with `kolla_connector_id` = `dentrix`.
Read the live names with `get_integrations` first.

## Test

As on the [Kolla page](kolla.md#test): slots, a booking in Dentrix tagged "(NP)", a cancellation.

## Needs Newo

None stated in the article.

## Limits and known issues

- No reschedule: cancel and book again.
- Cloud-only editions are not reachable.

## Source

https://help.newo.ai/en/articles/15825116-dentrix-integration, read 2026-11-25.
