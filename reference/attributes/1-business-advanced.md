# 1. Business - Advanced

Back to the [attribute index](index.md).

## `project_business_locations`


**Title:** Business Locations [C] [IMPORTANT]

**Description:**

````md
Use this field to list all business locations when you operate in more than one place. It helps the
Agent identify which location the user is asking about.

**Pro-Tip:** Keep one location per block and include the same core details for each location (name,
address, phone, and any location-specific notes).

**Examples:**

```txt
Downtown Office
Address: 100 Main St, Austin, TX
Phone: +1 (512) 555-0100

North Office
Address: 2400 Cedar Ave, Austin, TX
Phone: +1 (512) 555-0199
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When multi-location mode is active, this field is transformed into internal
location records used for location-aware reasoning and location switching during conversations.
Booking-schema reconfiguration is handled by multi-location feature-flag transition logic, while
this field itself primarily supplies and refreshes location data.

**Fallbacks:** If empty, initialization stores a generic placeholder. When this value changes, the
system rebuilds internal location records.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_private_feature_flag_multi_location`: Advanced system configuration that
    enables multi-location parsing and runtime location switching.
- **Logic Interactions:**
  - `project_attributes_setting_booking_payload_schema_template`: Updated when multi-location mode
    toggles so schema handling stays consistent.
  - `project_attributes_setting_booking_meta_fields_schema_template`: Updated with multi-location
    mode changes.
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: Updated with
    multi-location mode changes.
  - `project_attributes_setting_booking_check_availability_validation_schema_template`: Updated with
    multi-location mode changes.
````

**Level:** `Customer`

**Group:** `1. Business - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_business_top_location_count`


**Title:** Number of Business Locations [A]

**Description:**

```md
Store the total number of locations in your business network. This is primarily informational
metadata for configuration and reporting.

**Pro-Tip:** Keep this value aligned with your location list so team members can quickly verify
multi-location setup consistency.

**Examples:**

- **`1`:** Single-location operation.
- **`2` or more:** Multi-location operation.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Stored as informational metadata for operational reference. In the current
implementation, it is not used as a direct input for conversation routing or multi-location runtime
logic.

**Fallbacks:** If empty, initialization stores a generic placeholder value.

**Dependencies:**

- **Primary Settings:**
  - None. This field is maintained manually and is not consumed by runtime routing logic.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_multi_location`: Multi-location runtime behavior is
    controlled by this advanced system configuration independently of this count field.
```

**Level:** `Customer`

**Group:** `1. Business - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_business_top_name`


**Title:** Parent Company Name [A]

**Description:**

````md
Use this field for the parent organization name when your business has multiple branches or brands.
It helps keep organization-level information explicit.

**Pro-Tip:** Use the legal or publicly recognized parent brand name to avoid ambiguity across
locations.

**Examples:**

```txt
Example Hospitality Group
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Stored as informational metadata for account context and operational reference. In
the current implementation, it is not used as a direct input for conversation routing or other
runtime automation.

**Fallbacks:** If empty, initialization stores a generic placeholder value.

**Dependencies:**

- **Primary Settings:**
  - None. This field is maintained manually for reference context.
- **Logic Interactions:**
  - None. This attribute is not used as an input to runtime automation in the current
    implementation.
````

**Level:** `Customer`

**Group:** `1. Business - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_business_top_url`


**Title:** Parent Company Name Website [A]

**Description:**

````md
Use this field for the parent organization's main website URL in multi-location setups. It provides
a canonical source for corporate-level reference.

**Pro-Tip:** Use a full URL with protocol (for example, `https://...`) so linked systems can parse
it reliably.

**Examples:**

```txt
https://www.yourhotelgroup.com
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Stored as informational metadata for account context and operational reference. In
the current implementation, it is not used as a direct input for routing or other runtime
automation.

**Fallbacks:** If empty, initialization stores a generic placeholder value.

**Dependencies:**

- **Primary Settings:**
  - None. This field is maintained manually for reference context.
- **Logic Interactions:**
  - None. This attribute is not used as an input to runtime automation in the current
    implementation.
````

**Level:** `Customer`

**Group:** `1. Business - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_business_type`


**Title:** Business Type [A]

**Description:**

````md
Define your business category in a short phrase so the Agent has clear domain context from the
start.

**Pro-Tip:** Keep this concise (2-8 words) and include specialization only when it changes how the
Agent should respond.

**Examples:**

```txt
Dental clinic and orthodontics
```

```txt
Residential cleaning services
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into business-context preparation for supported industries and into
session-success evaluation prompts to anchor business-domain reasoning. During setup,
industry-specific defaults can populate this value so the Agent can describe the business with the
right domain language.

**Fallbacks:** On first initialization, this can be copied from Agent Creator's business-industry
description. If that source is empty, initialization first stores a generic placeholder, then
applies the selected industry's default label when available.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines which industry-specific default label is applied when
    this field is empty.
- **Logic Interactions:**
  - `agent_creator_business_info_industry_description`: First-init source used to prefill this
    attribute when Agent Creator provides a custom business category.
````

**Level:** `Customer`

**Group:** `1. Business - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_hipaa_mode_enabled`


**Title:** HIPAA Mode [A]

**Description:**

```md
Enables stricter privacy handling in session-ended reports for conversations that may include
protected health information.

**Pro-Tip:** Turn this on only when your report workflow is ready for extra redaction. This mode
redacts report content and suppresses transcript/recording sections in email reports. Review your
report-delivery settings separately before rollout if your policy requires stricter handling.

**Examples:**

- **Enabled (`True`):** Report-generation logic applies stronger anonymization rules and removes
  transcript/recording sections from email report body generation.
- **Disabled (`False`):** Standard report behavior is used according to your report settings.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Default initialization sets this field to `False`. When enabled, report generation
flows inject additional HIPAA redaction instructions (for names and PII) while preparing report
directions, and generated email report bodies suppress transcript and recording sections.

**Fallbacks:** Common setup initializes this to `False` when the attribute is empty.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_include_conversation_and_record_urls`: Even
    when this is enabled, HIPAA mode suppresses recording-link output in email reports.
  - `project_attributes_setting_session_ended_report_include_transcript`: Even when this is enabled,
    HIPAA mode suppresses transcript insertion in email reports.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_criteria_compiled`: HIPAA redaction
    instructions are applied while generating destinations and report content from this criteria.
  - `project_attributes_setting_session_ended_report_enabled`: HIPAA mode affects report
    formatting/redaction only when report sending is enabled.
```

**Level:** `Customer`

**Group:** `1. Business - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

> **Industry variance:** In the Beauty and Dental industries this attribute is registered as a
> visible `1. Business` item titled `1-16. HIPAA Mode [A]` instead of the advanced hidden placement
> shown here; the other industry registries keep the placement shown here.

---

## `project_attributes_static_additional_business_context`


**Title:** Business Context - Additional [B]

**Description:**

````md
Use this field for extra business details that do not fit cleanly into other attributes. It helps
the Agent answer nuanced questions with better context.

**Pro-Tip:** Add stable operational details (policies, amenities, constraints, special handling)
instead of one-off promotions.

**Examples:**

```txt
Same-day emergency appointments are available Monday-Friday after 6 PM.
Parking is free for the first 2 hours with validation.
For accessibility requests, we can provide wheelchair-friendly entrance guidance.
For large groups, at least 24 hours notice is preferred.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into additional-business-context prompt sections used during runtime
reasoning. When data-injection features are enabled, this content is combined with injected
operational data to form richer context.

In published native voice mode, this content is returned by `get_business_information` when
requested, together with enabled injected business data and relevant knowledge-base articles. It is
not added to the native system prompt.

**Fallbacks:** If left blank, common initialization stores a whitespace placeholder rather than
meaningful text. When both static and injected context are unavailable, some prompt builders omit
the additional-business-context block entirely, while the base prompt path falls back to
`No additional business context.`

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_data_injection_is_enabled`: Controls whether injected business data
    can be merged with this static context.
- **Logic Interactions:**
  - None. This field can be used standalone even when no additional context sources are enabled.
````

**Level:** `Customer`

**Group:** `1. Business - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---
