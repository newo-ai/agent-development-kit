# 1. Business

Back to the [attribute index](index.md).

## `project_business_name`


**Title:** 1-01-A. Business Name [A]

**Description:**

````md
The short, customer-recognized business name the Agent uses in greetings, SMS/email headers, and
signatures.

**Pro-Tip:** Keep it short (2-5 words), easy to say, and consistent with how customers recognize
you. For multi-location brands, include the specific location. If voice calls need better
pronunciation, also fill in the Business Phonetic Name.

**Examples:**

```txt
Example Tavern
```

```txt
Example Orthodontics - Downtown
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into Agent persona, VibeAgent configuration/coaching replies, voice
greetings, SMS/email templates, and calendar/meeting titles as the primary business label. When a
phonetic business name is provided, the system replaces this name inside voice greeting phrases to
improve pronunciation. If returning greeting phrases are not set, default voice greetings may be
generated using this name.

**Fallbacks:** On first initialization, the system attempts to populate this from Agent Creator
business info. If it remains empty, downstream templates may use a generic placeholder or omit the
name.

**Dependencies:**

- **Primary Settings:**
  - `project_business_name_phonetic`: Used to replace this name in voice greetings for accurate
    pronunciation.
- **Logic Interactions:**
  - `project_representative_agent_voice_greeting_phrase`: Phonetic replacement only works when this
    phrase includes the business name.
  - `project_representative_agent_voice_greeting_phrase_recent_returning`: If empty, default
    returning greetings may be generated using this name.
  - `project_representative_agent_voice_greeting_phrase_later_returning`: If empty, default
    returning greetings may be generated using this name.
  - `project_representative_agent_voice_disclaimer_phrase`: Prepended to the voice greeting phrase
    before delivery.
  - `project_representative_agent_chat_greeting_phrase`: Chat greeting content is separate; include
    the business name there if you want it spoken in chat.
  - `project_attributes_setting_email_sender_name`: If empty, it is auto-derived using the business
    name.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_name_phonetic`


**Title:** 1-01-B. Business Phonetic Name [B]

**Description:**

````md
The pronunciation form of your business name used during voice conversations. Set this when your
normal business name spelling is hard for voice models to pronounce correctly.

**Pro-Tip:** Use IPA notation and include only what needs pronunciation guidance. If only part of
the name is mispronounced, you can focus on that spoken form.

**Examples:**

```txt
/ˈmɛnloʊ ˈtævərn/
```

```txt
/ɪmɪdʒ ˌɔrθəˈdɑntɪks/
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Applied in voice-only runtime paths. The value is injected into pronunciation
constraints ("always pronounce X as Y"), used when generating default returning voice greetings, and
used to replace the regular business name inside voice greeting text and voice connector system
context.

**Fallbacks:** If empty or whitespace, no phonetic replacement is performed and voice flows keep the
regular business name. During default initialization this field is created as an empty placeholder.

**Dependencies:**

- **Primary Settings:**
  - `project_business_name`: Base name that is replaced with the phonetic form in voice text.
- **Logic Interactions:**
  - `project_representative_agent_voice_greeting_phrase`: Replacement works when this phrase
    contains the regular business name text.
  - `project_representative_agent_voice_greeting_phrase_recent_returning`: Auto-generated returning
    greetings may use the phonetic value as the spoken business name.
  - `project_representative_agent_voice_greeting_phrase_later_returning`: Auto-generated returning
    greetings may use the phonetic value as the spoken business name.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_address`


**Title:** 1-02. Business Address [A]

**Description:**

````md
The primary physical address the Agent should reference when users ask where your business is
located.

**Pro-Tip:** Use the full street address for the exact location this Agent supports. For
multi-location brands, enter only the branch tied to this Agent.

**Examples:**

```txt
220 University Ave, Palo Alto, CA 94301, United States
```

```txt
4th Floor, 151 W 30th St, New York, NY 10001, United States
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into industry business-context and technical-context prompts so the Agent
can provide location details consistently. It is also used in industry setup logic (for example,
Cleaning and Home Service) to compose default served-area text when that setting is missing.

**Fallbacks:** On first initialization, the system attempts to populate this from Agent Creator
business info. If empty later, downstream context keeps the address slot with a generic placeholder
value, and selected industry templates may generate generic served-area phrasing from available
location signals.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines which industry setup templates consume the address.
- **Logic Interactions:**
  - `project_attributes_products_and_services_served_area`: In some industries, this can be
    auto-composed from the business address when empty.
  - `project_representative_agent_voice_phone_area_code`: Used together with address when generating
    served-area fallback text in applicable industries.
  - `project_business_country`: Used alongside address in Agent-style inference prompts.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_country`


**Title:** 1-02-A. Business Country [A]

**Description:**

````md
The main country information for the business location handled by this Agent. This helps the system
adapt language and regional behavior in voice and messaging flows.

**Pro-Tip:** If this Agent serves one location, provide one primary country. If operations truly
span multiple countries for this same Agent, list them in a clear comma-separated format.

**Examples:**

```txt
United States
```

```txt
United States, Canada
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Added to industry business-context and technical-context prompts and used in
Agent-style generation logic (with language/address signals) to infer voice style characteristics.

**Fallbacks:** On first initialization, the system attempts to populate this from Agent Creator
business info. If empty, country-specific style inference may be reduced.

**Dependencies:**

- **Primary Settings:**
  - `project_business_language_primary`: Used together with country for Agent-style reasoning.
- **Logic Interactions:**
  - `project_representative_agent_voice_speaking_style`: May be influenced by country-aware style
    generation.
  - `project_business_address`: Combined with country in style-generation input context.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_public_phone`


**Title:** 1-03. Business Phone (Public Phone) [A]

**Description:**

````md
The official customer-facing phone number the Agent should share when users ask how to reach your
business.

**Pro-Tip:** Enter the same number customers see on public channels (website, maps, social
profiles). For location-based businesses, use the number tied to this specific location.

**Examples:**

```txt
+14155551234
```

```txt
14155551234
```

```txt
+14155551234, +14155559876
```

Use full country codes in every number.

**Best Practice:** If this public number forwards inbound calls to the Agent's AI number, do not
reuse it as a transfer, escalation, or bypass destination. Otherwise the Agent can send the caller
back to this public number, your phone system forwards the call to the Agent again, and the call can
repeat in a loop.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Inserted into industry business-context and technical-context prompts as the main
contact number. It is also referenced in setup logic that determines a safe bypass/emergency phone
for voice routing behavior.

**Fallbacks:** On first initialization, the system attempts to populate this from Agent Creator
business info. If empty, downstream context keeps the public-phone slot with a generic placeholder
value, and voice bypass auto-fill may rely on escalation routing settings or remain unset.

**Routing Safety:** Call loops are usually caused by external phone forwarding. A common failure
pattern is: a caller dials `project_business_public_phone`, the business phone system forwards that
call to `project_representative_agent_voice_phone_number`, and later the Agent transfers or bypasses
the call back to this same public number. The telephony provider then routes the call back to the
Agent instead of a human.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_bypass_phone_number`: Used as the existing
    bypass value gate during auto-fill setup.
  - `project_attributes_setting_asr_redirection_type_working_hours`: Influences whether public phone
    can be used as a bypass target in overflow vs non-overflow routing.
- **Logic Interactions:**
  - `project_business_working_hour_escalation_phone`: Used as fallback bypass target when public
    phone is unsafe or unavailable.
  - `project_representative_agent_voice_phone_number`: Checked against public phone to avoid routing
    the call back to the Agent itself.
  - `project_business_industry`: Industry setup templates consume this value for user-facing contact
    context.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_story`


**Title:** 1-04. Business Description [A]

**Description:**

````md
A short business overview the Agent uses to explain what you do and what makes you different. This
should read like a clear customer-facing summary, not internal notes.

**Pro-Tip:** Keep it to 1-2 concise paragraphs with plain language. Mention your core services,
ideal customers, and one or two differentiators the Agent can reuse in conversations.

**Examples:**

```txt
Harbor Grill serves wood-fired seafood, fresh pasta and seasonal salads by the marina. Dine in
or order takeout. Our menu changes with the season and features local produce and catch of the day.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into industry-specific business-context prompts. These prompts guide
runtime behavior, including how the Agent frames service explanations and recommendations.

**Fallbacks:** On first initialization, the system attempts to populate this from Agent Creator
business info. If empty, the Agent relies more heavily on other business inputs (for example,
products/services, FAQ, and terms) and may provide less contextual descriptions.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines which industry prompt template consumes this business
    description.
- **Logic Interactions:**
  - `project_attributes_products_and_services`: Complements the business story with concrete
    offerings.
  - `project_attributes_faq`: Used alongside the business story for question answering context.
  - `project_attributes_terms_and_conditions`: Adds policy constraints that may shape how the story
    is presented in responses.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_website_url`


**Title:** 1-05. Business Website Link (URL) [A]

**Description:**

````md
The official website URL the Agent can share when users ask for more information.

**Pro-Tip:** Use a complete URL (including `https://`) for the exact location or branch this Agent
supports. Avoid short links when possible.

**Examples:**

```txt
https://www.yourrestaurant.com
```

```txt
https://downtown.yourclinic.com
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Added to industry business-context and technical-context prompts, used in scenario
generation templates as the canonical website placeholder, and referenced in industry messaging
templates that allow sending business links.

**Fallbacks:** On first initialization, the system attempts to populate this from Agent Creator
business info. During connector setup for existing accounts, this value may be used as a fallback
website source if the upstream Agent Creator website field is missing.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines which industry prompt/template flows consume website
    information.
- **Logic Interactions:**
  - `project_attributes_setting_sms_send_information_allowed_content`: Industry defaults may include
    this URL in link-sharing templates.
  - `project_attributes_setting_email_send_information_allowed_content`: Industry defaults may
    include this URL in link-sharing templates.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_working_hours`


**Title:** 1-06. Working Hours [A] [IMPORTANT]

**Description:**

````md
The operating schedule for this business location used for scheduling, availability checks, and
working-hours call behavior.

**Best Practice:** Use a consistent day-by-day format with explicit open/close windows and include
holiday handling notes whenever possible.

To ensure reliable behavior, follow this preferred format structure when describing your business
hours:

```txt
Working days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
Working hours:
1) Monday: open from 7AM to 10:30 AM and from 11AM to 2:30 PM and from 5PM to 10PM
2) Tuesday: open from 7AM to 10:30 AM and from 11AM to 2:30 PM and from 5PM to 10PM
3) Wednesday: open from 7AM to 10:30 AM and from 11AM to 2:30 PM and from 5PM to 10PM
4) Thursday: open from 7AM to 10:30 AM and from 11AM to 2:30 PM and from 5PM to 10PM
5) Friday: open from 7AM to 10:30 AM and from 11AM to 2:30 PM and from 5PM to 10PM
6) Saturday: open from 7AM to 10AM and from 11AM to 2PM and from 5PM to 10PM
7) Sunday: open from 7AM to 10AM and from 11AM to 2PM and from 5PM to 10PM
```

If you are creating an agent for a call center that serves locations with different operating hours,
contact support team for guidance on how to properly provide this information to the agent.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Parsed into structured schedule artifacts used by Convo flows to determine
open/closed status in the configured business time zone, build "we are open/closed" phrases, and
drive logic for call transfer behavior and booking/meeting availability checks. It is also used as
the raw working-schedule prompt context when derived schedule fields are unavailable.

**Fallbacks:** On first initialization, the system attempts to populate this from Agent Creator
business info. If empty, compiled schedule artifacts are cleared. When structured
working-hours-object cache is unavailable, runtime status checks fall back to LLM evaluation over
the derived working-schedule and calendar context. If all derived schedule text fields are empty,
shared schedule-context builders fall back to this raw text.

**Dependencies:**

- **Primary Settings:**
  - `project_business_time_zone`: Required to evaluate current-time status against this schedule.
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Enables
    working-hours gating logic for conversation behavior.
- **Logic Interactions:**
  - `project_attributes_setting_transfer_call_enabled`: Transfer behavior is evaluated alongside
    current working-hours status.
  - `project_business_working_hour_escalation_phone`: Used for transfer routing during working
    hours.
  - `project_business_non_working_hour_escalation_phone`: Used for transfer routing outside working
    hours.
  - `project_attributes_setting_booking_check_availability_working_hours_status`: Can enforce
    working-hours constraints for booking availability checks.
  - `project_attributes_setting_meeting_check_availability_working_hours_status`: Can enforce
    working-hours constraints for meeting scheduling checks.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_time_zone`


**Title:** 1-07. Business Time Zone [A] [IMPORTANT]

**Description:**

```md
The primary time zone for this business location. The Agent uses this as the reference for
time-based decisions and time stamps.

**Pro-Tip:** Pick the IANA/TZDB value for the location this Agent serves (for example,
`America/New_York`). If your call center spans multiple zones, use the main office time zone.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used broadly across Convo, Task, SMS, and reporting flows to compute local current
time, convert between UTC and local time, evaluate working-hours status, and build time-aware
booking/scheduling payloads.

**Fallbacks:** On first initialization, the system attempts to populate this from Agent Creator
business info. If it remains empty, common setup sets `America/Los_Angeles`. If an invalid value is
provided, the system attempts to normalize it to a valid `tzdata` item and falls back to
`America/Los_Angeles` when normalization is not possible. If Agent Creator provides a valid timezone
that is outside the supported list, the system attempts to map it to the closest supported
equivalent with matching business clock behavior. Runtime prefers the attribute metadata
`possible_values` list when it is already available and falls back to an internal copy of the list
during early initialization.

**Dependencies:**

- **Primary Settings:**
  - `project_business_working_hours`: Evaluated together with this time zone for open/closed
    determination.
- **Logic Interactions:**
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Enables
    working-hours gating that depends on time-zone-aware status checks.
  - `project_attributes_setting_booking_check_availability_working_hours_status`: Can enforce
    working-hours constraints for booking checks in this time zone.
  - `project_attributes_setting_meeting_check_availability_working_hours_status`: Can enforce
    working-hours constraints for meeting checks in this time zone.
  - `project_attributes_setting_booking_type`: Booking flows may inject this time zone into provider
    payloads.
```

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `enum`

**Possible values:**
`["Africa/Accra", "Africa/Addis_Ababa", "Africa/Algiers", "Africa/Cairo", "Africa/Casablanca", "Africa/Johannesburg", "Africa/Khartoum", "Africa/Lagos", "Africa/Nairobi", "Africa/Tripoli", "Africa/Tunis", "America/Anchorage", "America/Argentina/Buenos_Aires", "America/Asuncion", "America/Bogota", "America/Cancun", "America/Caracas", "America/Chicago", "America/Denver", "America/Edmonton", "America/Guatemala", "America/Guayaquil", "America/Halifax", "America/Havana", "America/Jamaica", "America/La_Paz", "America/Lima", "America/Los_Angeles", "America/Mexico_City", "America/Montevideo", "America/New_York", "America/Panama", "America/Phoenix", "America/Port-au-Prince", "America/Recife", "America/Santiago", "America/Santo_Domingo", "America/Sao_Paulo", "America/Tijuana", "America/Toronto", "America/Vancouver", "America/Winnipeg", "Asia/Almaty", "Asia/Amman", "Asia/Ashgabat", "Asia/Baghdad", "Asia/Baku", "Asia/Bangkok", "Asia/Beirut", "Asia/Bishkek", "Asia/Colombo", "Asia/Damascus", "Asia/Dhaka", "Asia/Dubai", "Asia/Dushanbe", "Asia/Ho_Chi_Minh", "Asia/Hong_Kong", "Asia/Jakarta", "Asia/Jerusalem", "Asia/Kabul", "Asia/Karachi", "Asia/Kathmandu", "Asia/Kolkata", "Asia/Kuala_Lumpur", "Asia/Manila", "Asia/Muscat", "Asia/Nicosia", "Asia/Novosibirsk", "Asia/Riyadh", "Asia/Seoul", "Asia/Shanghai", "Asia/Singapore", "Asia/Taipei", "Asia/Tashkent", "Asia/Tbilisi", "Asia/Tehran", "Asia/Tokyo", "Asia/Ulaanbaatar", "Asia/Vladivostok", "Asia/Yangon", "Asia/Yerevan", "Atlantic/Azores", "Atlantic/Reykjavik", "Atlantic/St_Helena", "Australia/Adelaide", "Australia/Brisbane", "Australia/Darwin", "Australia/Hobart", "Australia/Melbourne", "Australia/Perth", "Australia/Sydney", "Europe/Amsterdam", "Europe/Athens", "Europe/Belgrade", "Europe/Berlin", "Europe/Brussels", "Europe/Bucharest", "Europe/Budapest", "Europe/Chisinau", "Europe/Copenhagen", "Europe/Dublin", "Europe/Helsinki", "Europe/Istanbul", "Europe/Kyiv", "Europe/Lisbon", "Europe/London", "Europe/Luxembourg", "Europe/Madrid", "Europe/Malta", "Europe/Moscow", "Europe/Oslo", "Europe/Paris", "Europe/Prague", "Europe/Riga", "Europe/Rome", "Europe/Sofia", "Europe/Stockholm", "Europe/Tallinn", "Europe/Vienna", "Europe/Vilnius", "Europe/Warsaw", "Europe/Zurich", "Indian/Mauritius", "Pacific/Apia", "Pacific/Auckland", "Pacific/Fiji", "Pacific/Guam", "Pacific/Honolulu", "Pacific/Pago_Pago", "Pacific/Port_Moresby", "Pacific/Tahiti", "Pacific/Tongatapu"]`

---

## `project_attributes_payment_methods`


**Title:** 1-08. Payment Methods [A]

**Description:**

````md
The payment methods your business accepts from customers. The Agent uses this to answer
payment-related questions accurately.

**Pro-Tip:** List every accepted option clearly (cards, digital wallets, cash, financing, etc.) and
note important restrictions if they matter to customers.

**Examples:**

```txt
Visa, Mastercard, American Express, Apple Pay, Google Pay, cash.
```

```txt
Card only. No cash accepted.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into industry business-context prompts that guide how the Agent answers
questions about accepted payment options.

**Fallbacks:** On first initialization, the system attempts to populate this from Agent Creator
business info. Common setup does not define a separate business-level fallback for this attribute
beyond that import step. Industry business-context builders still read this field through the shared
customer-attribute helper when assembling the active business context.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines which industry context templates consume this value.
- **Logic Interactions:**
  - `project_attributes_products_and_services`: Industry business-context builders place payment
    methods alongside the business's service catalog and service-coverage context.
  - `project_attributes_current_specials`: Included in the same industry business-context blocks
    that also list payment methods.
  - `project_attributes_terms_and_conditions`: In industries that include policy or house-rule
    context, payment methods are injected in the same business-context builder.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_top_owner_name`


**Title:** 1-09. Billing Manager Full Name [A]

**Description:**

```md
The full name used in greetings inside internal booking and session-report emails. It personalizes
internal notifications for your team.

**Pro-Tip:** Use the real person responsible for booking/report follow-up. This keeps internal
notifications more actionable and professional.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used as the salutation name in internal booking-notification and session-report
emails generated by Convo flows.

**Fallbacks:** Common setup seeds this field with a blank placeholder. If no usable name is set at
runtime, email salutations fall back to a generic recipient label (for example, "manager").

**Dependencies:**

- **Primary Settings:**
  - `project_business_manager_email`: Internal booking notifications are delivered to this email
    address, while this name is used in the email greeting.
  - `project_attributes_setting_session_ended_report_enabled`: Enables report emails that also use
    this salutation.
- **Logic Interactions:**
  - `project_attributes_setting_booking_success_notification_on_email_enabled`: When enabled,
    booking success emails include this name in the greeting.
  - `project_attributes_setting_booking_fallback_processing_type`: If set to custom fallback
    handling, built-in booking failure emails (and this salutation) are bypassed.
  - `project_business_industry`: For `restaurant_industry`, built-in booking failure emails are
    bypassed in favor of restaurant-specific handling.
  - `project_representative_agent_name`: Included in the same email body signature block.
  - `project_representative_agent_title`: Included in the same email body signature block.
  - `project_business_name`: Included in the same email body signature block.
```

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_top_owner_phone`


**Title:** 1-10. Billing Manager Phone Number [A]

**Description:**

````md
Direct phone number of the billing or operations contact. Use this for internal escalation and
reporting workflows where a human contact number is needed.

**Pro-Tip:** Enter the full international number with country code. If this person has multiple
numbers, use the one monitored most consistently.

**Examples:**

```txt
+14155551234
```

```txt
14155551234
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Stored as an administrative contact field. Built-in booking/report automations do
not automatically send SMS to this attribute unless your custom routing rules explicitly reference
it.

**Fallbacks:** Initialized as an empty placeholder by default. If empty, built-in workflows continue
to use configured manager/escalation channels.

**Dependencies:**

- **Primary Settings:**
  - `project_business_manager_email`: Remains the primary built-in recipient for internal booking
    email notifications.
  - `project_business_working_hour_escalation_phone`: Default report-routing SMS escalation channel
    when criteria require an escalation phone number.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_criteria_template`: Can reference
    `[[project_business_top_owner_phone]]` in custom SMS/report routing criteria.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_top_owner_email`


**Title:** 1-11. Billing Manager Email [A]

**Description:**

````md
Email address of the billing or operations contact. Use this when you want report or escalation
messages to include an additional internal recipient.

**Pro-Tip:** Use a monitored inbox (person or team alias). Avoid personal inboxes that are not
checked during business operations.

**Examples:**

```txt
ops-manager@yourbusiness.com
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Available as a template-injection attribute for custom report-routing logic (for
example, adding CC recipients in session-ended report criteria templates).

**Fallbacks:** Initialized as an empty placeholder by default. If unset, report/booking emails still
use primary configured recipient fields.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_enabled`: Controls whether session-ended report
    emails are sent at all.
  - `project_business_manager_email`: Used as the primary report target in built-in report flows.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_criteria_template`: Can include
    `[[project_business_top_owner_email]]` as a dynamic CC target in custom criteria.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_attributes_setting_common_phone_numbers`


**Title:** 1-12. Common (Shared) Phone Numbers [A]

**Description:**

````md
List of common business phone numbers that may be used by multiple people (for example, a reception
desk or front-office line). Use this to prevent the Agent from treating all calls/messages from that
number as one person.

**Pro-Tip:** Add only numbers that can be used by multiple people. Keep numbers in full
international format with country code to avoid matching issues.

**Examples:**

```json
["+13334445556", "+12223334455"]
```

Accepted number format per item:

- With plus: `+12223334444`
- Without plus: `12223334444`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Synced into voice-integration connector `shared_phone_numbers` settings. For phone
calls, these numbers are treated as common lines (not person-specific lines), which helps avoid
binding multiple humans to one persistent phone-based profile. Incoming SMS replies from these
numbers are filtered from normal SMS-reply processing paths. In booking retry flows, non-phone
external IDs (for example UUID-like IDs assigned to common lines) are ignored when deriving fallback
phone numbers.

**Fallbacks:** Defaults to `[]` on initialization. If a single integer is accidentally stored,
update logic normalizes it into a JSON list.

**Dependencies:** No active runtime attribute dependencies currently.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `json`

---

## `project_attributes_info_crm`


**Title:** 1-13. CRM [A]

**Description:**

```md
Name of the CRM platform your business uses. This gives operators and support teams quick context
about your back-office stack.

**Pro-Tip:** Enter the real CRM product name (and optionally the workspace/account context) to make
future integrations and support tasks easier.

**Examples:**

- **HubSpot:** Helps document that contacts and pipeline stages are managed in HubSpot.
- **Salesforce:** Indicates enterprise CRM usage for lead and case workflows.
- **GoHighLevel:** Clarifies that automation and CRM records are managed in GHL.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Currently treated as informational metadata and not used as a decision variable in
core runtime conversation logic.

**Fallbacks:** Initialized as an empty placeholder by default.

**Dependencies:** No active runtime attribute dependencies currently.
```

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

---

## `project_business_expected_number_of_calls_month_location`


**Title:** 1-14. Estimated Monthly Calls [A]

**Description:**

```md
Estimated monthly inbound call volume for the location this Agent supports. Use this as a planning
signal for capacity and operational expectations.

**Pro-Tip:** Provide a realistic monthly average (not peak-day volume). If the Agent handles only
after-hours or overflow traffic, estimate the total location volume, not just overflow calls. For
call-center deployments, enter the average total monthly call volume for the full center.

**Examples:**

- **100-300/month:** Typical low-volume location.
- **1,000+/month:** Higher-volume operation that may need stricter process tuning.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Currently treated as planning metadata; it does not directly change core Agent
runtime logic.

**Fallbacks:** Initialized as an empty placeholder by default.

**Dependencies:** No active runtime attribute dependencies currently.
```

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `number`

---

## `project_business_industry`


**Title:** 1-15. Industry (DON'T CHANGE) [A] [IMPORTANT]

**Description:**

```md
The core business domain used to configure this Agent during setup. It controls which
industry-specific templates, defaults, and logic paths are applied.

**Pro-Tip:** Choose the closest supported industry at initial setup and keep it unchanged after go
live. Use `general_industry` as the fallback when no closer supported vertical exists. Use
`sales_industry` only when the Agent is primarily expected to qualify leads and move buyers toward a
sales appointment, demo, product link, or purchase.

Behavior examples:

- **`restaurant_industry`:** Enables restaurant-oriented reservation and availability behavior.
- **`dental_industry`:** Enables dental appointment and patient-support specific defaults.
- **`general_industry`:** Best for unsupported or mixed verticals that need broad receptionist
  routing, such as answering questions, sending users to a booking or purchase link, or collecting
  details for follow-up.
- **`sales_industry`:** Best for sales-led businesses where the Agent should consult on offerings,
  qualify leads, share sales resources, and route buyers toward a demo, sales appointment, or
  product link.

**Important:** Do not change this value after the Agent is created. Changing industry on an existing
account can desynchronize defaults, templates, and runtime assumptions. If a change is required,
contact support and re-run a controlled setup process.

Supported industries:

- `beauty_industry`
- `catering_industry`
- `cleaning_industry`
- `dental_industry`
- `general_industry`
- `home_service_industry`
- `hospitality_industry`
- `restaurant_industry`
- `sales_industry`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Drives industry branching across setup and post-setup flows, including
industry-specific attribute initialization, scenario preparation, reporting defaults, and
booking/availability behavior across multiple Agents. General industry setup prepares flexible
receptionist-style routing for booking links, purchase links, and human follow-up. Sales industry
setup prepares sales-specific lead qualification, consultation, demo/appointment, product-link, and
sales reporting paths.

**Fallbacks:** On first initialization, the system attempts to populate this from Agent Creator
business info. If that source is empty, common setup defaults this field to `general_industry`. If
the value is invalid, industry-dependent defaults may not be applied correctly.

**Dependencies:**

- **Primary Settings:**
  - `project_business_type`: Default value is derived from the selected industry during setup.
- **Logic Interactions:**
  - `project_attributes_products_and_services`: Initialization behavior differs for restaurant vs
    non-restaurant setup paths.
  - `project_attributes_setting_session_ended_report_criteria_template`: Default report-routing
    criteria are selected by industry.
  - `project_attributes_setting_session_ended_report_enabled`: Auto-enabled/disabled based on
    industry-specific report criteria generation.
  - `project_attributes_setting_session_ended_report_content`: Default report content templates are
    selected by industry.
```

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `enum`

**Is read-only:** `true`

**Possible values:**
`["beauty_industry", "catering_industry", "cleaning_industry", "dental_industry", "general_industry", "home_service_industry", "hospitality_industry", "restaurant_industry", "sales_industry"]`

---

## `project_business_language_primary`


**Title:** 1-16. Language - Primary [B]

**Description:**

```md
Primary language of the business. The system uses this language for business-facing generated
content such as reports, manager notifications, and email/SMS report fields.

**Note:** This setting no longer controls the Agent's live conversation reply language. To set the
Agent's preferred default speaking language, use Agent Primary Language
(`project_representative_agent_primary_language`).

**Pro-Tip:** Set this to the language your business uses internally for manager-facing summaries,
reports, and business-facing generated text.

Behavior examples:

- **Reports and manager notifications:** Generated report summaries, manager emails, and manager SMS
  messages use this language.
- **Report field extraction:** Report custom fields and generated SMS/email report content can be
  forced into this language.
- **Setup defaults:** During first initialization, this value is copied into Agent Primary Language.
  After that, Agent-facing greeting/disclaimer language is controlled by Agent Primary Language, not
  this business language setting.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used as a business-language setting across report generation, report custom-field
extraction, manager notification generation, VibeAgent configuration/health-check surfaces, and
first-initialization copy into Agent Primary Language.

**Fallbacks:** On initialization, the system first tries to read this from Agent Creator business
language input. If unavailable, common setup defaults it to `English`. Live Agent language
preference can be managed separately.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Controls the Agent's preferred default live
    conversation language. This business language does not replace that setting.
- **Logic Interactions:**
  - `project_business_country`: Used together with primary language when generating voice style and
    inferring accent context.
```

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `enum`

**Possible values:**
`["English", "Spanish", "French", "German", "Italian", "Portuguese", "Russian", "Chinese", "Japanese", "Korean", "Arabic", "Hindi", "Bengali", "Urdu", "Turkish", "Vietnamese", "Thai", "Indonesian", "Polish", "Dutch", "Hebrew", "Swedish", "Norwegian", "Danish", "Finnish", "Greek", "Czech", "Hungarian", "Slovak", "Ukrainian", "Romanian", "Bulgarian", "Serbian", "Croatian", "Slovenian", "Lithuanian", "Latvian", "Estonian", "Filipino", "Malay", "Khmer", "Lao", "Afrikaans", "Swahili", "Persian", "Punjabi", "Gujarati", "Marathi", "Tamil", "Telugu", "Kannada", "Malayalam", "Sinhalese", "Nepali", "Mongolian", "Amharic", "Azerbaijani", "Georgian", "Uzbek", "Basque", "Catalan", "Kazakh", "Armenian", "Assamese", "Belarusian", "Bosnian", "Burmese", "Cantonese", "Cebuano", "Galician", "Ganda", "Hausa", "Icelandic", "Igbo", "Irish", "Javanese", "Kurdish", "Kyrgyz", "Luo", "Macedonian", "Maltese", "Odia", "Pashto", "Sindhi", "Somali", "Tajik", "Welsh", "Wolof", "Xhosa", "Zulu"]`

---

## `project_business_language_restricted_list`


**Title:** 1-17. Language - Restricted Languages [B]

**Description:**

````md
Specify languages the Agent must avoid using in replies or automatic language switching. The same
list also prevents those languages from being selected as the runtime conversation language or the
user's stored preferred language.

**Pro-Tip:** Enter only the languages you want blocked, using a JSON array of language names. Keep
the list empty (`[]`) if there are no language restrictions, and never include the Agent's primary
language in this list.

**Examples:**

```json
["Russian", "Chinese"]
```

```json
[]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime consumers parse this value as a JSON array. With the advanced Agent
Language Instructions V2 configuration enabled, shared core-conversation, food-ordering, and
outbound-call prompts apply the list according to the active language mode:

- With Agent Multilingual enabled, every language except the restricted languages is allowed.
- With Agent Multilingual disabled and no secondary-language allowlist, the prompts prohibit the
  restricted languages while applying the current language-stability rules.
- With Agent Multilingual disabled and a non-empty secondary-language allowlist, shared prompts use
  the primary-plus-secondary allowlist instead of injecting this list. Language Observer still
  rejects any candidate language that is also restricted.

When Agent Language Instructions V2 is not enabled, the core conversation prompt still uses language
anchoring and the primary-language fallback. Earlier food-ordering and outbound-call prompts instead
follow the user's apparent language immediately, so an isolated phrase can trigger a language change
or restricted-language response in those capability-specific legacy prompts.

This list also adds a restriction to urgent-message generation, prevents restricted languages from
being saved as the user's preferred language, and constrains any language-switch procedure included
in an active conversation scenario. Configuration health checks report a critical conflict when the
Agent's primary language also appears in this list.

**Fallbacks:** Common business initialization sets this attribute to an empty JSON list (`[]`) when
no restrictions are provided. An empty list disables the restriction logic. A non-empty value must
be valid JSON; runtime prompt consumers do not replace malformed JSON with the empty-list fallback.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Must not also be restricted; configuration
    health checks treat that conflict as critical.
  - `project_representative_agent_multilingual`: Controls whether broad multilingual behavior is
    enabled. Restricted languages apply in multilingual mode and in non-multilingual mode when no
    secondary-language allowlist is active.
  - `project_representative_agent_secondary_languages`: When filled together with Agent Primary
    Language and Agent Multilingual is disabled, the Agent uses only the primary and secondary
    languages instead of the restricted-language list.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_agent_language_instructions_v2`: This advanced system
    configuration selects the current stable-language rules or the capability-specific legacy prompt
    behavior described above.
  - `project_attributes_private_feature_flag_current_conversation_language`: This advanced system
    configuration enables Language Observer and current-language prompt wording; restricted
    languages remain ineligible for observer selection.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `json`

---

## `project_attributes_known_employees`


**Title:** 1-18. Known Employees [A]

**Description:**

````md
List names of team members callers may explicitly ask for, such as managers, receptionists,
salespeople, doctors, technicians, or other named colleagues. This helps the Agent recognize
requests like "Can I speak with Sarah?" as a human-handoff request instead of treating the name as a
general question.

**Pro-Tip:** Use clear comma-separated names and include commonly used short forms, titles, or
role-based names that callers naturally say.

**Important Note:** If you add a person, role, or team here and callers may ask to be connected to
them, also fill the advanced Transfer Call to Manager - Advanced Phone Number Selection & Rules
(`project_attributes_setting_transfer_call_phone_numbers`) setting during the same setup pass.
Otherwise the Agent may recognize the request for that employee but still not know which phone
number to transfer the call to.

**Examples:**

```txt
Tom, Sarah, Claire, Dr. Patel, Mike, front desk, sales team
```

When adding employees here, pair this field with transfer-number routing:

```txt
Known Employees:
Sarah, Dr. Patel, front desk

Transfer Call to Manager - Advanced Phone Number Selection & Rules:
- Sarah: +12223334444
- Dr. Patel: +12223335555
- front desk: +12223336666
```

This tells the Agent both who callers might ask for and where to transfer the phone call when that
specific person, role, or team is requested.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into industry intent-type instructions where the "Manager or Human
Request" class already exists. This extends that class with named colleagues, so requests for
specific team members are handled alongside generic human or manager asks. The attribute helps the
Agent decide that the caller wants a colleague; it does not by itself provide a destination phone
number. In industries that include this class, the resulting handoff behavior is typically
transfer-first during working hours and relay-first outside working hours.

**Fallbacks:** If empty during initialization, the system sets a placeholder value indicating no
employees were specified.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Selects which industry intent map is used. Every industry intent
    map defines a manager/human request class that references this attribute; only the two generic
    non-industry templates (`default_itm_wh` / `default_itm_nwh`) omit that class.
  - `project_business_working_hours`: Provides the business schedule used for working-hours-aware
    transfer-vs-relay behavior when working-hours evaluation is enabled.
  - `project_business_working_hour_escalation_phone`: Baseline transfer target during working-hours
    handoff when transfer-call routing is available.
- **Logic Interactions:**
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Controls
    whether runtime working-hours status is actively evaluated for transfer-vs-relay routing.
  - `project_attributes_setting_transfer_call_enabled`: If disabled, manager/human requests use
    relay-style handling instead of call transfer.
  - `project_attributes_setting_transfer_call_phone_numbers`: Strongly recommended whenever this
    attribute names employees, roles, or teams that should have their own transfer destination. If
    configured, these routing-specific numbers tell the transfer flow which phone number to use when
    the caller asks for a particular worker or situation, and can override escalation-phone defaults
    for transfer execution.
  - `project_business_non_working_hour_escalation_phone`: Affects general off-hours transfer
    availability in transfer-call logic, but non-working-hours manager/human intent behavior is
    typically relay-first in default industry maps.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

**Is hidden:** `false`

---
