# 5. Reports

Back to the [attribute index](index.md).

## `project_attributes_setting_asr_average_lead_value`


**Title:** 5-01. ASR - Average Lead Value [A]

**Description:**

```md
This is your baseline revenue value for potential-revenue reporting. The system uses it when it
cannot confidently calculate a specific deal value from the conversation and also as the default
potential revenue for non-lead sessions.

**Pro-Tip:** Set this to a realistic average closed deal value for your business, then review it
regularly as pricing or service mix changes.

**Examples:**

- For dental businesses, this is typically the average contract value for a new patient or case.
- For cleaning businesses, this is often the average service value across a typical customer
  relationship.
- Restaurant and hospitality setups use their industry bill settings for most revenue formulas, but
  this value still remains a fallback safeguard in some categories.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used in end-session metrics and events as the `defaultLeadValue`. Revenue
calculation flows also use it as the baseline fallback when formula output is invalid.

**Fallbacks:** Initialized as an empty setting in common defaults, then populated by
industry-specific setup skills when empty. At runtime, if extracted pricing data is missing or
invalid, revenue calculation falls back to this baseline first. In some industry-specific models,
bill-based calculations can still apply `zero_default` or `min_value` guardrails that reuse this
value after the formula runs.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines which initialization flow sets the default value and
    which revenue model is applied.
- **Logic Interactions:**
  - `project_attributes_catering_deposit`: Catering revenue formulas can replace lower calculated
    revenue with the configured deposit minimum.
  - `project_attributes_restaurant_bill_average_per_person_regular_reservation`: Restaurant revenue
    categories use industry bill attributes first and reuse this setting only as a fallback
    safeguard in some paths.
  - `project_attributes_hospitality_bill_average_per_person_per_day_regular_reservation`:
    Hospitality formulas use per-day values first and reuse this setting for fallback safeguards in
    some categories.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `number`

---

## `project_attributes_setting_asr_conversion_ratio`


**Title:** 5-02. ASR - Conversion Ratio [A]

**Description:**

```md
This is the expected conversion percentage for your conversations. It represents how many
conversations typically become paying outcomes.

**Pro-Tip:** Keep this value evidence-based (from real historical performance), not aspirational.
Update it after major campaign, pricing, or sales-process changes.

**Examples:**

- **Higher ratio:** External ASR analytics will treat the pipeline as more conversion-efficient.
- **Lower ratio:** External ASR analytics will treat outcomes more conservatively.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Sent in the `session_ended` system event as `asrConversationRatio` for downstream
ASR/reporting calculations.

**Fallbacks:** Common initialization leaves this empty; industry setup skills populate defaults when
empty. If it is still blank, the `session_ended` event carries the stored empty/placeholder value,
so downstream reporting should not rely on it until a real ratio is configured or seeded.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Controls which default conversion ratio is seeded at
    initialization.
- **Logic Interactions:**
  - `session_ended`: Downstream reporting receives this value as `asrConversationRatio`.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `number`

---

## `project_attributes_setting_asr_redirection_type_working_hours`


**Title:** 5-03. ASR - Redirection Type (Working Hours) [A]

**Description:**

```md
This setting controls how ASR recognition is interpreted for phone conversations during working
hours. It defines whether recognition is treated as full (`overflow`) or uses your configured
recognition percentage (`non-overflow`).

**Pro-Tip:** Use `overflow` when you want working-hours call handling counted as fully recognized.
Use `non-overflow` when you need stricter percentage-based ASR recognition.

**Examples:**

- **`overflow`:** Working-hours ASR recognition is forced to 100%.
- **`non-overflow`:** Working-hours ASR recognition uses your configured recognition percentage.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** End-session event logic sets `asrRecognition` to 100% outside working hours, and
during working hours either forces 100% (`overflow`) or reads
`project_attributes_setting_asr_recognition` (`non-overflow`). It is also used in post-setup logic
that selects a bypass/emergency transfer number. In `non-overflow`, setup prefers
`project_business_working_hour_escalation_phone` because sending bypass calls to the public number
is more likely to loop when that public number already forwards to the Agent. In `overflow`, setup
may still choose the public number when it is not the same literal number as the Agent's AI line.

**Fallbacks:** Common defaults initialize this as empty, then industry setup logic sets it to a
supported value (typically `overflow`) when needed.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_asr_recognition`: Used when this setting is `non-overflow`.
- **Logic Interactions:**
  - `project_attributes_setting_voice_integration_service_bypass_phone_number`: Auto-selection logic
    for bypass routing depends on this redirection mode.
  - `project_business_public_phone`: Considered as a bypass target in `overflow` mode, which is safe
    only when that public number does not auto-forward back to the Agent.
  - `project_business_working_hour_escalation_phone`: Used as the safer fallback target in
    non-overflow and anti-recursion checks.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `enum`

**Possible values:** `["overflow", "non-overflow"]`

---

## `project_attributes_setting_session_ended_report_enabled`


**Title:** 5-04. Reports - Session Ended Report - Enabled [B] [IMPORTANT]

**Description:**

```md
This is the master switch for end-of-session manager reports. When enabled, the system can send
report emails and/or SMS based on your report criteria and templates.

**Pro-Tip:** Keep this enabled if your team relies on human follow-up, missed-call recovery, or
escalation visibility.

**Examples:**

- **Enabled (`True`):** Session-ended report workflows can route messages to configured recipients.
- **Disabled (`False`):** No session-ended report delivery is attempted, even if content/criteria
  are configured.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Hard gate for report sending in report flow execution. Standard report execution
is skipped entirely when full session-end processing is disabled. This flag also affects fallback
communication logic (for example, whether the Agent offers to relay a message to a human co-worker
when transfer is unavailable or technical issues occur).

**Fallbacks:** During report preparation, autogenerated report criteria can initialize this to
enabled. If criteria cannot be generated, initialization can set it to disabled. Manual values are
respected when already present.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_content`: Defines what report payload is
    generated when delivery is enabled.
  - `project_attributes_setting_session_ended_report_criteria_template`: Defines when and where
    report delivery should occur.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_full_processing_enabled`: Must be enabled for the
    standard session-ended report handler to run.
  - `project_attributes_setting_transfer_call_enabled`: Combined with this flag for
    transfer-vs-relay fallback behavior in voice flows.
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Working-hours
    logic affects fallback messaging paths tied to report relay options.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `bool`

---

## `project_attributes_setting_session_ended_report_content`


**Title:** 5-05. Reports - Session Ended Report - Content [B] [IMPORTANT]

**Description:**

````md
This setting defines the report templates used after a conversation ends. It controls report types,
fields to extract, and how email subjects/SMS text are generated. Your criteria template decides
whether a report goes by email, SMS, or both; this setting defines what each of those reports says.

**Pro-Tip:** Keep report types aligned with your active intent naming and focus extracted fields on
what your team actually needs for action.

**Examples:**

```txt
## Report Type: **LARGE GROUP RESERVATION**

### Fields to be included in the report:
User name
User phone
Party size
Requested date
40-word summary

### Subject line format:
LARGE GROUP RESERVATION: [user name] [user phone] [6-word additional summary]

### SMS example:
LARGE GROUP RESERVATION: [user name] [user phone] [20-word additional summary] Truly, [agent name], [agent title]
```

Keep report type names aligned with your criteria template so the intended template is selected for
each session type.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Report-preparation flows normalize this template set against the current intent
catalog, then convert it into structured runtime report content consumed by report-sending logic. If
a report type is missing or stale, it can be automatically rebuilt/trimmed during preparation.

**Fallbacks:** If empty, industry-specific default report content is generated (except certain
minimal/default modes where report content may remain empty). If a specific report type is missing
from prepared content, the system uses a generic fallback template for that report type. Report
sending exits only when structured report content is empty or when routing logic decides nothing
should be sent.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_enabled`: Must allow report sending for this
    content to be used.
  - `project_attributes_setting_session_ended_report_criteria_template`: Determines recipient
    routing and timing for each report type.
- **Logic Interactions:**
  - `project_business_industry`: Selects default report content templates during initialization.
  - `project_attributes_setting_session_ended_report_additional_schema`: Extends output directions
    schema used by report decision logic.
  - `project_attributes_setting_session_ended_report_event_map`: Maps optional additional directions
    to follow-up system events.
````

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `string`

---

## `project_attributes_setting_session_ended_report_criteria_template`


**Title:** 5-06. Reports - Session Ended Report - Criteria [B] [IMPORTANT]

**Description:**

````md
This setting defines the routing rules for session-ended reports. It decides which report types send
SMS/email, when they send, and who receives them.

**Pro-Tip:** Use exact report/intent names from your workflow and keep recipient rules simple first,
then add advanced CC/SMS variations after baseline routing is stable.

**Examples:**

```txt
**Criteria for SMS Report:**
- **During working hours:**
  - If it is a Manager or Human Request, send an SMS to [[project_business_working_hour_escalation_phone]]

---

**Criteria for Email Report:**
- If it is a Manager or Human Request, send an email to [[project_business_manager_email]]
```

```txt
**Criteria for Email Report:**
- If it is a Manager or Human Request, send an email to [[project_business_manager_email]] and cc to [[project_business_top_owner_email]], ops-lead@example.com
```

```txt
**Criteria for SMS Report:**
- If it is a Manager or Human Request, send an SMS to [[project_business_working_hour_escalation_phone]] and +12223334445
```

Use `[[attribute_idn]]` placeholders to inject attribute values dynamically. Use plain text values
for fixed emails/phone numbers.

To change report fields or the email subject/SMS body templates, update the Session Ended Report
content setting separately.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Merged with additional criteria blocks, then compiled so placeholders resolve to
runtime values before report-direction logic executes. Report decision logic can use only recipients
defined in this criteria set. When multiple email addresses are returned, the first email is used as
the primary recipient and the remaining addresses are sent as CC. Every listed SMS number receives
the report message.

**Fallbacks:** If empty during setup, industry-specific default criteria may be generated. If no
usable criteria exists, the system can keep report delivery disabled.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_enabled`: During default criteria
    initialization, this is set to `True` when generated criteria is available and to `False` when
    no criteria template can be generated.
  - `project_attributes_setting_session_ended_report_content`: Must stay aligned with criteria
    report type names.
  - `project_business_manager_email`: Common default email recipient used by generated criteria.
  - `project_business_working_hour_escalation_phone`: Common default SMS recipient used by generated
    criteria.
- **Logic Interactions:**
  - `project_business_industry`: Determines which default criteria template is generated when this
    setting is empty.
  - `project_attributes_setting_session_ended_report_additional_criteria`: Appended to the base
    criteria before compilation.
  - `project_attributes_setting_session_ended_report_criteria_complete_template`: Advanced system
    configuration storing merged criteria before placeholder compilation.
  - `project_attributes_setting_session_ended_report_criteria_compiled`: Advanced system
    configuration consumed by report decision logic at runtime.
````

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `string`

---

## `project_attributes_setting_session_ended_report_include_transcript`


**Title:** 5-07. Reports - Session Ended Report - Transcript [B]

**Description:**

```md
This setting controls whether full conversation text is attached to session-ended report emails.

**Pro-Tip:** Keep this off if you only need summaries, or when you want smaller report payloads.

**Examples:**

- **Enabled (`True`):** Report emails include a prepared transcript section.
- **Disabled (`False`):** Report emails include summary/structured fields only.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Read while building email body text for session reports. If enabled, transcript
preparation runs and appends conversation text to the generated report.

**Fallbacks:** Defaults to `False` during initialization. Even when enabled, transcript inclusion is
suppressed when HIPAA mode is enabled.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_enabled`: Transcript is relevant only when
    report delivery is active.
- **Logic Interactions:**
  - `project_attributes_setting_hipaa_mode_enabled`: Overrides transcript inclusion to protect
    sensitive data handling.
  - `project_attributes_setting_session_ended_report_content`: Defines the rest of report structure
    that transcript output is appended to.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `bool`

---

## `project_attributes_setting_session_ended_report_include_utm_tags`


**Title:** 5-08. Reports - Session Ended Report - UTM Tags [B]

**Description:**

```md
This setting controls whether captured UTM campaign parameters are appended to session-ended report
emails.

**Pro-Tip:** Enable this for marketing-attribution workflows, especially for web/chat channels where
campaign tags are commonly available.

**Examples:**

- **Enabled (`True`):** UTM details are added when campaign parameters exist for the conversation.
- **Disabled (`False`):** No UTM section is appended to report emails.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Report email assembly reads this flag and, when enabled, formats persona URL
parameters into a UTM section for the outgoing report.

**Fallbacks:** Defaults to `False` during initialization. If enabled but the conversation has no URL
parameters, no UTM content is appended.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_enabled`: UTM output is used only in active
    report-delivery flows.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_content`: UTM section is appended to the report
    body assembled from this content template.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `bool`

---
