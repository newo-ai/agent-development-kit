# Industries

The agent's industry is `project_business_industry`. Each industry has its own default scenarios and
settings.

Read the setup playbook for the business right after the
[assistant guide](../docs/assistant-guide.md), then the extra page for the industry if there is one.
Open the industry attribute reference only when a task needs a setting's exact format.

| Industry (`project_business_industry`) | Setup playbook | Extra page | Attribute reference |
|---|---|---|---|
| Restaurant | [restaurant.md](restaurant.md) | – | [restaurant](../reference/attributes/industries/restaurant.md) |
| Catering | [general.md](general.md) | [restaurant.md](restaurant.md#orders-and-catering) | [catering](../reference/attributes/industries/catering.md) |
| Dental | [general.md](general.md) | [appointments.md](appointments.md) | [dental](../reference/attributes/industries/dental.md) |
| Beauty | [general.md](general.md) | [appointments.md](appointments.md) | [beauty](../reference/attributes/industries/beauty.md) |
| Cleaning | [general.md](general.md) | [home-services.md](home-services.md) | [cleaning](../reference/attributes/industries/cleaning.md) |
| Home service | [general.md](general.md) | [home-services.md](home-services.md) | [home service](../reference/attributes/industries/home_service.md) |
| Hospitality | [general.md](general.md) | – | [hospitality](../reference/attributes/industries/hospitality.md) |
| Sales | [general.md](general.md) | – | [sales](../reference/attributes/industries/sales.md) |
| Support, General or anything else | [general.md](general.md) | – | [general](../reference/attributes/industries/general.md) |

When there is no attribute page for the industry, use [general](../reference/attributes/industries/general.md).
All other settings, for every industry: [attribute index](../reference/attributes/index.md).

The extra pages add what the playbooks do not cover: integrations that are common in the industry,
pitfalls, and links to [learnings](../learnings/README.md) for that industry.
