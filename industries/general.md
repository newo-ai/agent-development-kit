# General setup playbook

For an AI assistant setting up a Newo agent for any business that has no playbook of its own
(dental, beauty, cleaning, catering, hospitality, home service, sales, support and others). Read
the main guide first ([docs/assistant-guide.md](../docs/assistant-guide.md); with the older plugin, `read_guide`, the guide itself); its rules always apply: ask the owner before
every change, keep old values, never delete, never ask for an API key. Talk to the owner in their
language, in short messages, about what the agent will know and do.

## The essential work (always, do it first)

Verify with the owner, one at a time, before anything else:

1. **Products and services** the business offers, and what it does not offer.
2. **Opening hours**, every day of the week, with breaks and upcoming holidays, and the time zone.
3. **Prices**, and whether the agent may say them on the phone.

These live in the settings named in the main guide's "Finish the configuration" playbook ([playbooks/finish-configuration.md](../playbooks/finish-configuration.md))
(`project_attributes_products_and_services`, `project_business_working_hours`,
`project_business_time_zone`, `project_representative_agent_providing_prices_explicit_constraint`).
Then continue with that playbook: greeting, transfers to a person, FAQ, policies, reports.

## Where the knowledge goes

Settings first. Use the knowledge base (AKB) only for what does not fit the settings; above about
100 to 200 articles, recommend Newo Knowledge Studio (see the main guide, "Where the agent's
knowledge goes": [assistant guide](../docs/assistant-guide.md#where-the-agents-knowledge-goes), [06-knowledge.md](../docs/06-knowledge.md)).

## Keep it simple

A standard setup needs only settings. Do not bring up scenarios, Vibe mode, the workflow builder,
custom skills or code unless the owner asks for something the standard setup cannot do.

## Industry settings

The industry's own settings (appointment types, service areas, booking links and similar) are in
`attributes/industries/<industry>.md` ([reference/attributes/industries/](../reference/attributes/industries/general.md)), listed in the main guide's "Industry playbooks" table ([assistant guide](../docs/assistant-guide.md#industry-playbooks), [README.md](README.md)). Open
that page when a task needs them.

Pages with more detail for some industries: [appointments.md](appointments.md) (dental, medical,
beauty, wellness), [home-services.md](home-services.md) (home services, cleaning).

## Typical next steps

- Keep the business number with forwarding after 2–3 rings: [telephony](../docs/telephony/README.md),
  [Connect the business phone line](../playbooks/connect-phone-line.md).
- Send every conversation to the business's CRM or email: [integrations](../docs/integrations/http-rest.md),
  [Connect external systems](../playbooks/connect-external-systems.md).
- Large documentation (support centers, insurers, banks, telecom): use Knowledge Studio
  ([knowledge](../docs/06-knowledge.md)).
