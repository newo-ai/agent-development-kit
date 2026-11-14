# Playbook: finish the configuration

Goal: every setting a caller can notice is correct and complete, and the owner has heard the
agent at least once. Follow the rules in [the guide](../docs/assistant-guide.md): ask before each change, keep
old values, never delete.

## 1. Read the current state

1. `GET /api/v1/customer/profile` and check the `idn`.
2. Check the designer ([API reference](../reference/api.md#which-designer)). V2:
   `GET /api/v3/designer/projects` and `GET /api/v3/designer/customer-links?project_idn=naf`;
   note the `naf` project's `id`, the running version and whether it follows Newo's updates.
   Old designer: `GET /api/v1/designer/projects`; note `id`, `version` and
   `is_auto_update_enabled`.
3. Read all customer attributes once and save them to a file (see [API reference](../reference/api.md#attributes)).
4. Build a short checklist from the attributes below: value present or missing, and anything
   that looks wrong (a placeholder, another business's name, a time zone that does not match the
   address).

## 2. Settings to check, in this order

Open the linked group page when you need the exact format of a value. The owner should confirm
every change.

**Business** ([1-business.md](../reference/attributes/1-business.md))

| Setting | What to check |
|---|---|
| `project_business_name` | exact public name |
| `project_business_address`, `project_business_country` | full address |
| `project_business_public_phone` | the number customers already know (the business line) |
| `project_business_website_url` | main website |
| `project_business_story` | 3 to 8 sentences about the business, what makes it different |
| `project_business_working_hours` | every day, with breaks; use the day-by-day format from the attribute description |
| `project_business_time_zone` | IANA name matching the address, for example `America/Los_Angeles` |
| `project_attributes_payment_methods` | what customers can pay with |

Do not change `project_business_industry` (marked DON'T CHANGE).

**Agent** ([2-agent.md](../reference/attributes/2-agent.md))

| Setting | What to check |
|---|---|
| `project_representative_agent_name`, `project_representative_agent_title` | the name and role the agent introduces itself with |
| `project_representative_agent_voice_greeting_phrase` | first sentence on the phone: short, names the business, invites the caller to speak |
| `project_representative_agent_voice_disclaimer_phrase` | recording or AI notice, if the owner wants or the law requires one |
| `project_representative_agent_primary_language`, `..._secondary_languages`, `..._multilingual` | languages callers use |
| `project_representative_agent_voice_speaking_style` | tone on the phone |
| `project_representative_agent_providing_prices_explicit_constraint` | whether and how the agent may name prices |

`project_representative_agent_voice_phone_number` is the agent's own number and is managed by
Newo: read it, never change it.

**Knowledge** ([3-knowledge-base.md](../reference/attributes/3-knowledge-base.md))

| Setting | What to check |
|---|---|
| `project_attributes_products_and_services` | the main catalog: services or menu, durations, prices if allowed |
| `project_attributes_products_and_services_not_offering` | what the business does not do |
| `project_attributes_faq` | the 10 to 20 questions callers ask most, with the owner's answers |
| `project_attributes_current_specials` | current offers, or empty |
| `project_attributes_terms_and_conditions` | policies: cancellations, deposits, parking, age limits |
| `project_attributes_rag_knowledge_base_append_text` | long documents (price lists, policies) to add to the knowledge base; read its description first, it appends instead of replacing |
| `project_attributes_rag_knowledge_base_append_websites` | web pages to import, with what to extract |

Ask the owner for anything missing, or read their website and propose text for them to approve.
Write in the language callers use.

**Transfers to a person** ([4-agent-behavior.md](../reference/attributes/4-agent-behavior.md))

| Setting | What to check |
|---|---|
| `project_attributes_setting_transfer_call_enabled` | `"True"` only if the numbers below are set |
| `project_business_working_hour_escalation_phone` | who answers transfers during business hours |
| `project_business_non_working_hour_escalation_phone` | who answers outside business hours, or empty |
| `project_attributes_setting_transfer_call_criteria` | when the agent should offer a person |
| `project_business_manager_email` | where the agent sends leads and escalations |

**Reports** ([5-reports.md](../reference/attributes/5-reports.md))

| Setting | What to check |
|---|---|
| `project_attributes_setting_session_ended_report_enabled` | `"True"` so the owner gets a summary after conversations |
| `project_attributes_setting_session_ended_report_content` | the report types and fields; they must fit this business (a dental office needs no "catering order" report) |
| `project_attributes_setting_session_ended_report_criteria_template` | who receives which report type, by email or SMS; every type named here must exist in the content setting |
| `project_attributes_setting_session_ended_report_include_transcript` | whether the email includes the full transcript |
| `project_attributes_setting_session_ended_full_processing_enabled` | reports need the full end-of-conversation processing; check that it is `"True"` |

The report settings are filled from an industry template when the agent is created. If they
mention things this business does not do, propose rewriting both content and criteria for its
real cases, using the formats in [5-reports.md](../reference/attributes/5-reports.md).

Booking, calendar, email and SMS to callers are covered in
[Connect external systems](connect-external-systems.md). Industry-specific settings (menus, appointment types,
service areas) are listed in [attributes/industries/](../reference/attributes/industries/general.md);
open the page for the business's industry.

## 3. Apply the changes

1. Show the owner one list: setting, old value, new value. Get a "yes" (they may approve all at
   once or one by one).
2. Change each attribute with a full-object PUT ([API reference](../reference/api.md#change)).
3. Read each value back.
4. If you changed working hours, time zone, languages or voice settings, publish the `naf`
   project ([API reference](../reference/api.md#publish)) and wait 2 to 5 minutes.

## 4. Test

1. Run a sandbox chat ([API reference](../reference/api.md#sandbox)) with 3 to 5 questions that use the changed
   settings: "Are you open on Sunday?", "How much is ...?", "Can I talk to a person?".
   Creating the sandbox test user is itself a change: tell the owner and ask once. If the owner
   does not want it, skip to step 2.
2. Ask the owner to call the agent's number, listen to the greeting and ask the same questions.
   Then read that call's transcript ([Review conversations](review-conversations.md)) and tell the owner what
   you saw.
3. Report what worked and what did not. Fix and repeat.

When the owner is happy, offer the night launch ([Launch at night](night-launch.md)).
