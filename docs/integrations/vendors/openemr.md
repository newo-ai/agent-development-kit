# OpenEMR

**Health data.** Apply [Health data](../README.md#health-data) before you connect.

## What it does for the agent

Checks free slots for one provider and facility, books (finds or creates the patient) and
cancels, through the OpenEMR REST API.

## Before you start

- An OpenEMR instance with the REST API on, reachable over HTTPS from the internet.
- An OAuth2 client (Client ID and Secret) registered in OpenEMR.
- An OpenEMR user with API access to appointments and patients: user name, password, email.
- A staging instance or test data: every action is real.
- Versions: not stated (to confirm).

## Partner does in OpenEMR

1. Sign in as an administrator.
2. **Administration → System → API Clients**: register a new OAuth2 client. Note the Client ID
   and Client Secret.
3. Check the API user can manage appointments and patients.
4. Type the client and user details into the Newo Builder (next section). Not into the chat.

## Assistant does in Newo

Names from the help article; read the live list with `get_integrations` first. The article has no
project step (to confirm whether a project from a module is needed).

1. Set `openemr_base_url` (for example `https://emr.example.com`).
2. The partner types into the Builder (Attributes): `openemr_client_id`, `openemr_client_secret`,
   `openemr_username`, `openemr_password`, `openemr_email`.
3. Optional: `openemr_enable_slot_check`, `openemr_enable_booking`, `openemr_enable_cancellation`,
   `openemr_check_existing_client` (all default `True`), `openemr_show_for_days` (days ahead),
   `openemr_override_agent_attributes` (default `True`). `openemr_scope` is preset.
4. **Publish All**. The facility list (`openemr_facility`) fills; choose the facility, then the
   provider (`openemr_provider`). Changing facility needs **Publish All** again.

The agent asks for first and last name, date of birth, sex and phone number. Appointments are 15
minutes, titled "Office Visit".

## Test

1. `openemr_access_token` is set after publish (say "set", do not show it).
2. Facilities and providers are listed.
3. Ask "What slots are available on Monday?"
4. Book; it appears in the OpenEMR calendar.
5. Cancel; it is gone from OpenEMR.

## Needs Newo

None stated in the article.

## Limits and known issues

- One provider and one facility at a time.
- No reschedule: cancel and book again.
- Only appointments made after activation.

## Source

https://help.newo.ai/en/articles/14121850-openemr-integration, read 2026-11-25.
