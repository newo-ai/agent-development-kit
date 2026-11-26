# Kolla (bridge to on-premises dental PMS)

Kolla connects the agent to a practice management system installed on the practice's own
computer: Dentrix, OpenDental, Eaglesoft, Dolphin. The pages for those systems point here and add
one setting each.

**Health data.** Apply [Health data](../README.md#health-data) before you connect.

## What it does for the agent

- Checks free slots, books new and existing patients, cancels.
- Finds the patient by the caller's phone number.
- Tags bookings "(NP)" for a new patient and "(EP)" for an existing one. Newo can email the
  practice manager after a booking.

## Before you start

- A Kolla portal account (`app.getkolla.com`) and an active dental or orthodontic agent.
- The practice runs its PMS **on-premises**. Cloud editions cannot be reached (the article's
  example: the cloud edition of Dentrix).
- From the practice: its name, which PMS, the provider(s) and the operatory (room) to book into
  by default.
- WinOMS, OrthoTrac and DSN: lower confidence, confirm with Kolla before promising them.
- About 30 to 60 minutes for a first practice. Plans and versions: not stated (to confirm).

## Partner does in Kolla

1. Sign in to the Kolla portal. Check the connector for the practice's PMS is listed and
   enabled. Not listed? Ask the Kolla representative: invite links need a published connector.
2. **Linked Accounts** → **Create Invite Link**. Pick the connector for the PMS.
3. Enter a **unique consumer identifier** for the practice (you choose it; it must be unique in
   your Kolla account) and the practice name. The email is for reference only.
4. Generate the link and send it to the practice.
5. The practice's administrator opens the link **on the computer where the PMS is installed** and
   installs the Kolla connector.
6. When the record shows **Active** in **Linked Accounts**, note the **Consumer ID**.
7. **API Keys** → create a key for that linked account. Copy the token without spaces before or
   after: stray spaces are the most common cause of failed sign-in.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first.

1. Add a project: Idn `kolla_integration`, Title `kolla_integration`, Registry `production`,
   Module `kolla_integration`, Auto update on. **Force Update Project**, then **Publish All**.
   The `kolla_*` settings appear only after this.
2. The partner types into the Builder (Attributes, search `kolla`): `kolla_api_token`.
3. Set `kolla_consumer_id` (from step 6 above) and `kolla_connector_id` (`dentrix`,
   `opendental`, `eaglesoft` or `dolphin`).
4. **Force Update Project** again, then **Publish All**. Kolla reads the practice's system and
   fills the lists of providers and operatories.
5. With the practice, choose `kolla_default_provider` (**Kolla Provider**, required) and
   `kolla_default_operatory` (**Kolla Operatory**, required if the PMS tracks rooms).
6. Optional: `kolla_enable_provider_selection` (off by default: matches the service to a provider
   by specialty; keep off until every provider's specialties are set),
   `kolla_appointment_length` (default 30 minutes), `kolla_appointment_types`. Do not edit
   `kolla_operatories_list` and `kolla_providers_catalog`: the platform fills them.

## Test

Every action is live in the practice's schedule. Agree a test patient and test dates.

1. Check the default provider and operatory are set.
2. Ask for free slots; they match that provider's calendar in the PMS.
3. Book; the appointment appears in the PMS at once, tagged "(NP)".
4. Cancel; the PMS shows it.
5. Check in the conversation events that the scheduling tools ran.
6. Before launch: at least five good bookings across dates, providers and reasons for visit.

No slots but calls run cleanly? The provider or operatory choice is usually wrong.

## Needs Newo

None stated in the article. A connector missing in Kolla is for the Kolla representative.

## Limits and known issues

- No reschedule: cancel and book again.
- One location per linked account.
- Cloud-hosted PMS editions are not reachable.

## Source

https://help.newo.ai/en/articles/13786216-kolla-integration, read 2026-11-25.
