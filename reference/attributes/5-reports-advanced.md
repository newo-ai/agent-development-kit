# 5. Reports - Advanced

Back to the [attribute index](index.md).

## `project_attributes_private_custom_schema_inbound_call_report`


**Title:** Reports - Phone Inbound - Custom Schema [C]

**Description:**

````md
This advanced setting defines extra fields to extract from a conversation when the session ends. It
extends the default structured data written to your inbound session records.

**Pro-Tip:** Keep this schema focused on fields your team will actually review, and make each field
description explicit about what to store when data is missing (for example, `Not Provided`).

**How it works:**

- A predefined `template (schema)` tells the system what information to look for in the conversation
- If a detail is mentioned by the user, it is captured and stored
- If a detail is missing, the system sets it to `Not Provided` instead of leaving it blank
- All collected details are saved in session logs, making it easy to access and analyze later

**Example of schema used for data extraction:**

```json
{
  "type": "object",
  "properties": {
    "organization": {
      "type": "string",
      "description": "Set to the organization name provided by the user. If the user didn't mention an organization name, set it to \"Not Provided\"."
    },
    "job_title": {
      "type": "string",
      "description": "Job title provided by the user. If the user didn't mention a job title, set it to \"Not Provided\"."
    }
  },
  "required": ["organization", "job_title"]
}
```

**Example of what it captures:**

If a user shares their company name and job title during the conversation, the system records:

- Organization: "ABC Corp"
- Job Title: "Marketing Manager"

If they don't mention this information, the system saves:

- Organization: "Not Provided"
- Job Title: "Not Provided"

**Why it is useful**

- Saves important details automatically
- Ensures no critical information is missed
- Organizes data clearly for future use

This makes it easy to review past conversations and use the captured information for reports,
insights, or follow-ups.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During session-ended processing, this schema is read and used for structured
extraction from conversation history plus user context. The extracted object is included in
`customValues` for inbound-session record updates. The system also appends conversation-source data
to this custom payload before writing the record.

**Fallbacks:** Initialization creates this attribute as an empty placeholder. If empty, custom
extraction is skipped and the custom payload starts as `{}`. If no usable conversation transcript
exists, the end-session extraction pipeline is skipped, so this schema is not applied for that
session.

**Dependencies:**

- **Primary Settings:**
  - `project_business_time_zone`: Extraction context includes current datetime based on this time
    zone, which can affect schema fields requiring time-aware values.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_webhook_schema`: Separate extraction schema processed
    in the same session-ended pipeline for webhook payloads.
  - `project_attributes_setting_session_ended_webhook_url`: Controls outbound webhook sending; this
    custom schema still affects inbound-record custom values independently.
````

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_asr_recognition`


**Title:** ASR - Working Hours Recognition [A]

**Description:**

```md
Defines the recognition percentage used for ASR attribution during working hours when your
redirection mode is `non-overflow`. In practice, this acts as a normalization coefficient for how
much of the AI-handled outcome should be counted as uniquely attributable to the AI instead of the
standard business process.

**Pro-Tip:** Keep this value tied to real historical performance, not assumptions. Revisit it after
major changes in staffing, call routing, or response speed.

**Examples:**

- **`40`:** In working-hours `non-overflow` mode, 40% of relevant outcomes are treated as
  attributable recognition.
- **`100`:** In working-hours `non-overflow` mode, all relevant outcomes are treated as recognized.
- **Any value:** Ignored when conversation is outside working hours, or when working-hours mode is
  `overflow` (those paths force 100%, because the AI is handling traffic that was already missed or
  unavailable to the human team).

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** End-session event logic computes `asrRecognition` for the `session_ended` payload
using this branch:

- outside working hours -> `100`
- working hours + `project_attributes_setting_asr_redirection_type_working_hours = overflow` ->
  `100`
- working hours + `project_attributes_setting_asr_redirection_type_working_hours = non-overflow` ->
  this attribute value

**Fallbacks:** Common initialization creates this setting as empty, then in-scope industry setup
flows seed default value `40` when empty. If it stays empty in a working-hours `non-overflow` path,
outgoing ASR recognition data can be blank.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_asr_redirection_type_working_hours`: Determines whether this value
    is used or bypassed by forced `100`.
  - `project_business_industry`: Industry setup selects the default seed value during account setup.
- **Logic Interactions:**
  - `project_attributes_setting_asr_conversion_ratio`: Sent together in end-session ASR analytics
    payloads.
  - `project_attributes_setting_asr_average_lead_value`: Used alongside ASR metrics in downstream
    revenue analytics.
```

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_conversation_summary_instruction`


**Title:** Reports - Conversation Summary Guidelines [B]

**Description:**

````md
Defines the instruction template used to generate end-session conversation summaries.

**Pro-Tip:** Write concise, outcome-focused guidance (length, tone, and key points) and avoid
conflicting requirements. Keep instructions practical so summaries remain consistent across
sessions.

**Examples:**

```txt
Summarize the given conversation between a customer and an AI Agent (digital employee). The summary should be concise and around 100 words.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected directly into the summary-generation prompt during session-ended metrics
collection. The generated summary is then reused across session-ended outputs, including
`session_ended` system events, inbound-record updates, and optional monitoring/disaster workflows.
The runtime prompt always adds an additional rule to keep very short conversations minimally
summarized.

**Fallbacks:** Initialization sets a default summary instruction if this field is empty. If the
session transcript is empty or has no real user turns, the summary-generation path is skipped and
session-ended handling uses a fallback no-conversation summary.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_hitl_monitoring_enabled`: When enabled, the generated summary is
    included in HITL monitoring payloads.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_enabled`: Report delivery settings are
    independent; summary generation still runs for core session-ended outputs.
  - `project_attributes_setting_send_report_during_conversation`: Mid-conversation report checks use
    separate logic and do not consume this summary template.
````

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_send_report_during_conversation`


**Title:** Reports - Send Report During Conversation - Enabled [C]

**Description:**

```md
This advanced setting controls whether report sending can be triggered before the conversation ends.

**Pro-Tip:** Keep this disabled unless you need urgent manager handoff notifications while the
session is still active. For reliable behavior, keep your report content and criteria settings up to
date.

**Examples:**

- **Enabled (`True`):** Mid-conversation report checks run and can send a report when the Agent
  explicitly promises to pass the user’s information right away.
- **Disabled (`False`):** Mid-conversation report checks are skipped; report sending remains in
  standard session-ended flow.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Read in the `broadcast_analyze_conversation` event path. When enabled, the system
evaluates the latest Agent reply for explicit immediate-handoff intent and only then calls report
delivery logic. Even in this path, report dispatch still depends on normal report configuration and
recipient-direction decisions.

**Fallbacks:** Defaults to `False` during initialization. Default preparation restores baseline
behavior. If enabled but the latest reply does not meet the immediate-handoff condition, no
mid-conversation report is sent.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_enabled`: Must be enabled for actual report
    delivery.
  - `project_attributes_setting_session_ended_report_content`: Defines report structures used when
    mid-conversation sending is triggered.
  - `project_attributes_setting_session_ended_report_criteria_template`: Determines recipients and
    delivery conditions.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_include_conversation_and_record_urls`: Affects
    whether email reports sent from this path include conversation/recording links.
```

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_report_include_conversation_and_record_urls`


**Title:** Reports - Session Ended Report - Records Links [A]

**Description:**

```md
Controls whether session report emails include links to the conversation page and call recordings.

**Pro-Tip:** Enable this for operations teams that review conversations in detail. Disable it when
you want leaner emails or stricter link-sharing policies.

**Examples:**

- **Enabled (`True`):** Email generation attempts to include a conversation URL and recording links
  when those links are available in the current environment.
- **Disabled (`False`):** Conversation and recording links are omitted from the report email body.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Applied while composing report email body text. When set to `False`, conversation
URL generation and recording-link rendering are skipped. When set to `True`, the system attempts to
build links from portal/session context and available call recordings.

**Fallbacks:** During first initialization, this is populated from Agent Creator settings when
available, otherwise defaults to enabled. Even when enabled, links are omitted when required
portal/session inputs or recording data are unavailable.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_enabled`: Link output is relevant only when
    report delivery is active.
- **Logic Interactions:**
  - `project_attributes_setting_hipaa_mode_enabled`: Suppresses recording-link output even when this
    setting is enabled.
  - `project_attributes_setting_session_ended_report_include_transcript`: Independent report-body
    section controlled separately from link output.
  - `project_attributes_setting_session_ended_report_include_utm_tags`: Independent report-body
    section controlled separately from link output.
```

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_report_type_email`


**Title:** Reports - Session Ended Report - Type - Email [C]

**Description:**

```md
This advanced setting decides how the Agent hands off session-ended report emails after a
conversation qualifies for email delivery. Use `default` for the standard built-in email path, or
use `custom` when your deployment needs another integration to receive the prepared report payload
instead.

**Pro-Tip:** Leave this on `default` unless you have a compatible custom integration that listens
for report-email events and knows how to process the generated recipients, subject, and HTML body.

**Examples:**

- **`default`:** The built-in email delivery path receives the prepared recipient, CC list, subject,
  and report body and sends the report through the standard system email workflow.
- **`custom`:** The built-in report logic still prepares the recipient, CC list, subject, body,
  transcript, and report type, but hands them off to a custom system event so another integration
  can process them.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This attribute is read during the session-ended email dispatch step, after report
logic has already decided that an email should be sent. When set to `default`, runtime emits
`email_worker_send_email`, the built-in system email event, with the prepared `email`, `cc`,
`subject`, and `body`. When set to `custom`, runtime emits `convoagent_send_custom_report_email`
instead and includes the prepared `email`, `cc`, `subject`, `body`, `transcript`, `userId`,
`reportType`, `reportData`, and `ignore_opt_out` fields. The `ignore_opt_out` field marks the report
as system-driven delivery so the downstream handler receives that flag with the payload. In the
in-scope external module coverage, a setup workflow forces this setting to `custom`, marks it
read-only, and routes the custom event into an outbound data-delivery integration.

**Fallbacks:** Common initialization sets this attribute to `default` only when it is empty, so
existing non-empty values are preserved. A module-specific setup workflow can override that value to
`custom` for deployments that require custom handling.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_enabled`: Must allow session-ended reports
    before any email dispatch path is reached.
  - `project_attributes_setting_session_ended_report_criteria_template`: Determines whether an email
    should be sent and which recipients/subject template are prepared before this setting chooses
    the handoff path.
  - `project_attributes_setting_session_ended_report_content`: Defines the report fields and content
    used to build the email body that either delivery path receives.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_include_transcript`: Changes whether the
    prepared email body includes the conversation transcript before it is handed to the selected
    delivery path.
  - `project_attributes_setting_session_ended_report_include_conversation_and_record_urls`: Changes
    whether conversation and recording links are included in the prepared email body.
  - `project_attributes_setting_hipaa_mode_enabled`: Can suppress transcript and recording details
    in the prepared email body before either dispatch path receives it.
```

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `enum`

**Possible values:** `["default", "custom"]`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_webhook_auth_header`


**Title:** Reports - Webhook - Authentication Header [C]

**Description:**

```md
Authorization value used for session-ended webhook requests. This is sent as the `Authorization`
HTTP header when your webhook endpoint is called.

**Pro-Tip:** Always include the scheme (`Bearer`, `Basic`, etc.) in this field and rotate secrets
regularly. Leave it empty only when your endpoint does not require authentication.

**Examples:**

- `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
- `Basic dXNlcm5hbWU6cGFzc3dvcmQ=`
- empty value for unauthenticated endpoints

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When `project_attributes_setting_session_ended_webhook_url` is configured, the
outbound request is sent with `Content-Type: application/json` and an `Authorization` header set to
this value exactly as stored.

**Fallbacks:** Initialization prepares this attribute as an empty placeholder. If it remains empty,
the webhook request can still be sent (when webhook URL is configured), but without authorization
credentials.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_webhook_url`: Webhook dispatch must be enabled for
    this header to be used.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_webhook_schema`: Defines optional schema-based payload
    extraction used for the webhook body. If this schema is empty, the request body falls back to
    `{}` while this header is still sent.
```

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_webhook_schema`


**Title:** Reports - Webhook - Schema [C]

**Description:**

````md
Defines the JSON schema used to build the payload for your session-ended webhook. The Agent uses
this schema to extract structured values from the conversation.

**Pro-Tip:** Keep the schema focused on business-critical fields and write clear field descriptions
that explain what to do when data is missing (for example, use a standard placeholder such as
`Not Provided`).

**How it works:**

- A predefined `template (schema)` tells the system what information to look for in the conversation
- If a detail is mentioned by the user, it is captured and stored
- If a detail is missing, the system sets it to `Not Provided` instead of leaving it blank
- All collected details are sent to `project_attributes_setting_session_ended_webhook_url`

**Example of schema used for data extraction:**

```json
{
  "type": "object",
  "properties": {
    "user_name": {
      "type": "string",
      "description": "Set to the name provided by the user. If the user didn't mention their name, set it to \"Not Provided\"."
    },
    "organization": {
      "type": "string",
      "description": "Set to the organization name provided by the user. If the user didn't mention an organization name, set it to \"Not Provided\"."
    },
    "job_title": {
      "type": "string",
      "description": "Job title provided by the user. If the user didn't mention a job title, set it to \"Not Provided\"."
    }
  },
  "required": ["user_name", "organization", "job_title"]
}
```

**Example of what it captures:**

If a user shares their company name and job title during the conversation, the system records:

- Name: "Alex Johnson"
- Organization: "ABC Corp"
- Job Title: "Marketing Manager"

If they don't mention part of the information, the system saves:

- Name: "Alex Johnson"
- Organization: "Not Provided"
- Job Title: "Not Provided"

**Why it is useful**

- Sends important information for each session to the provided webhook
- Ensures no critical information is missed.
- Organizes data clearly for future use, easily filtered by "Not Provided" constant.
- Allows you to integrate with your CRM etc.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** At session end, the system reads this schema and performs structured extraction
from conversation history and user context. If the schema is not empty and not `{}`, extracted
values are serialized as the webhook request body.

**Fallbacks:** Initialization prepares this attribute as an empty placeholder. If empty (or set to
`{}`), extraction is skipped and the webhook body remains an empty JSON object (`{}`). If no usable
conversation transcript exists for the session, webhook dispatch is skipped entirely.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_webhook_url`: Destination endpoint that receives the
    payload generated from this schema.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_webhook_auth_header`: Optional authorization value
    sent with the same webhook request.
  - `project_attributes_private_custom_schema_inbound_call_report`: Separate advanced schema for
    report-table custom values; it does not replace this webhook payload schema.
````

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_webhook_url`


**Title:** Reports - Webhook - Link (URL) [C]

**Description:**

````md
This setting defines the endpoint URL that receives a webhook when a session ends.

If this attribute is empty, no webhook is sent.

If this attribute is set, the Agent sends a `POST` request with an `application/json` payload.

**Pro-Tip:** Use a stable HTTPS endpoint and design it to handle retries/idempotency. Keep this URL
aligned with your webhook schema and authentication settings.

The payload follows the schema defined in `project_attributes_setting_session_ended_webhook_schema`.

**Example of payload sent:**

```json
{
  "user_name": "Alex Johnson",
  "organization": "ABC Corp",
  "job_title": "Marketing Manager"
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During session-ended processing, this value is trimmed and checked. If non-empty,
the system sends an HTTP request with method `POST`, headers from
`project_attributes_setting_session_ended_webhook_auth_header`, and body built from
`project_attributes_setting_session_ended_webhook_schema` extraction output.

**Fallbacks:** Initialization prepares this attribute as an empty placeholder. If the trimmed value
is empty at runtime, outbound webhook dispatch is skipped.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_webhook_schema`: Defines the payload shape/content for
    this endpoint.
  - `project_attributes_setting_session_ended_webhook_auth_header`: Provides optional authorization
    credentials for the outbound request.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_enabled`: Independent from email/SMS
    session-ended report delivery; webhook dispatch is controlled by this URL field itself.
````

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_info_client_session_logs_table_link`


**Title:** Reports - Client Session Logs Table - Link (URL) [C]

**Description:**

```md
Stores the URL of your Client Session Logs table where teams review incoming sessions (calls and
chats).

**Pro-Tip:** Use a stable shared URL with controlled access so operations and support teams can open
the same source of truth during investigations.

**Examples:**

- `https://docs.google.com/spreadsheets/d/.../edit`
- `https://airtable.com/app.../tbl.../viw...`

If the link is missing, contact support at `support@newo.ai`.

If your session logs are stored in Google Sheets and access is blocked, follow the
[Google Sheet setup guide](https://docs.newo.ai/docs/google-sheet-setup).

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Stored as an operational reference link. In current NAF runtime flows, no direct
read of this attribute is used for core report dispatch or session-ended extraction logic.

**Fallbacks:** Initialization creates this attribute as an empty placeholder. If empty, operators
have no stored direct link to open from configuration.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required.
- **Logic Interactions:**
  - None in current runtime flows; this remains an operator-facing reference field.
```

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_technical_owners`


**Title:** Reports - Technical Owners [B] [IMPORTANT]

**Description:**

````md
Define the technical-owner email recipients for critical issue alerts detected during conversations.

**Pro-Tip:** Put your primary on-call mailbox first, then add backup recipients. Keep this list
current during staffing changes.

**Examples:**

```txt
oncall@yourcompany.com
engineering-manager@yourcompany.com
```

```txt
oncall@yourcompany.com, ops-lead@yourcompany.com
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When severe conversation failures are identified in end-session analysis, this
value is read and used to generate disaster-alert email routing: first recipient as the primary
target, remaining recipients as CC.

**Fallbacks:** Initialization creates this attribute as an empty placeholder. If empty (or
effectively `[]`), disaster-alert email sending is skipped even when a disaster condition is
detected.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required.
- **Logic Interactions:**
  - `project_attributes_setting_hitl_monitoring_enabled`: HITL monitoring is a separate alert path
    and does not replace technical-owner disaster emails.
  - `project_attributes_setting_session_ended_report_enabled`: Standard report delivery is
    independent from disaster-alert email routing.
````

**Level:** `Customer`

**Group:** `5. Reports - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---
