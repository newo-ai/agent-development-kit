# 3. Knowledge Base - Advanced

Back to the [attribute index](index.md).

## `project_business_average_prices`


**Title:** Average Prices [A]

**Description:**

````md
Legacy field for storing approximate average price ranges for your services.

**Pro-Tip:** Keep this as a high-level range only. Put active pricing logic in your pricing rules
and service catalog fields.

**Examples:**

```txt
Our prices range from $100 to $500, though they may be higher depending on your specific requests.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This field is retained mainly for setup compatibility and metadata continuity.
Current runtime prompt flows do not actively consume it for pricing decisions.

**Fallbacks:** On first initialization, this can be copied from Agent Creator intake. If empty, it
remains a generic placeholder.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_products_and_services`: Primary source for active customer-facing offering
    and pricing context.
  - `project_attributes_setting_calculation_context`: Main pricing context used by calculation
    flows.
- **Logic Interactions:**
  - `project_attributes_setting_calculation_rules`: Active pricing behavior is defined here rather
    than by this legacy field.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_current_specials_url`


**Title:** Specials - Link (URL) [B]

**Description:**

````md
Optional URL for a webpage that lists your current specials and promotions.

**Pro-Tip:** Keep key offers in the main Specials field as well, because URL-only ingestion is not
automatic yet.

**Examples:**

```txt
https://www.example.com/specials
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Stored as advanced reference metadata. It is not currently auto-fetched into the
active Specials content pipeline.

**Fallbacks:** Initialization sets an empty placeholder when missing.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_current_specials`: Active promotions field used by runtime prompts.
- **Logic Interactions:**
  - No additional customer settings are required.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_products_and_services_served_area`


**Title:** Products & Services - Area Served [A]

**Description:**

````md
Describe the general geographic area where your products or services are available.

**Pro-Tip:** Be explicit about radius, cities, or regions so service-availability checks remain
predictable.

**Example 1:**

```txt
We deliver within a 50-mile radius from 335 University Ave, Palo Alto, CA, 94301.
```

**Example 2:**

```txt
We provide services in these cities:
- Palo Alto, CA
- Mountain View, CA
- Los Altos, CA
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used in service-area validation flows when ZIP-code validation is not available or
when the user provides location text (city/region) instead of a ZIP code. This field is also
injected into industry business-context prompts.

**Fallbacks:** Default is empty. Cleaning and Home Service setup flows can auto-seed this field from
business address and agent phone area code. If user location is unclear, area-check logic defaults
to treating the location as served.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_products_and_services_served_zip_codes`: If ZIP list is empty, area-based
    validation becomes the primary fallback.
  - `project_attributes_setting_products_and_services_background_check_location_enabled`: Advanced
    system configuration that controls background ZIP-check tooling behavior.
- **Logic Interactions:**
  - `project_business_address`: Used to seed default served-area phrasing in selected industries.
  - `project_representative_agent_voice_phone_area_code`: Used with business address for default
    served-area phrasing in selected industries.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_products_and_services_served_zip_codes`


**Title:** Products & Services - ZIP Codes Served [B]

**Description:**

````md
JSON array of ZIP/postal patterns used to validate where service is available.

**Pro-Tip:** Keep entries normalized and test new patterns carefully. For large ZIP lists, use
background location-check mode for better runtime performance.

The Agent can validate availability using exact ZIP values, numeric ranges, or wildcard prefixes.

ZIP codes can be specified as an explicit list, using intervals (ranges), or using wildcard
patterns.

**Matching Rules:**

- **Normalization:** Matching is case-insensitive and ignores spaces (e.g., "sw1a 1aa" matches
  "SW1A1AA").
- **Intervals:** Ranges (e.g., "94000-94999") are supported **only for numeric ZIP codes**.
  Alphanumeric ranges (e.g., UK/Canada postal codes) are not supported via intervals; please use
  patterns or explicit lists for them.
- **Patterns:** Use `*` as a wildcard (e.g., "SW1\*").

**Example:**

```json
["94020", "94201", "94301-94309", "950**", "SW1A*"]
```

Benefits:

- Clearly defines service areas
- Ensures accurate availability checks
- Easily updated to reflect changes in service areas

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Consumed by ZIP-check flows for location validation. Matching supports exact ZIP
values, numeric ranges (`start-end`), and trailing wildcard prefixes (`*`). If this field is empty,
the system falls back to area-description checks.

**Fallbacks:** Default initialization value is `[]`. If the value is empty or not formatted as a
JSON array string (missing surrounding `[` and `]`), ZIP-check logic falls back to permissive
handling and treats the user as within service area. Otherwise, the value is parsed as JSON for ZIP
matching rules.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_products_and_services_served_area`: Used when ZIP list is empty or when
    location checks rely on city/region text.
  - `project_attributes_setting_products_and_services_background_check_location_enabled`: Advanced
    system configuration that enables ZIP double-check tooling paths.
- **Logic Interactions:**
  - `project_attributes_setting_products_and_services_background_check_location_enabled`: When set
    to `False`, ZIP coverage can be surfaced directly in contextual prompt sections.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---
