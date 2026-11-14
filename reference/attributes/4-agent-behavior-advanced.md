# 4. Agent Behavior - Advanced

Back to the [attribute index](index.md).

## `project_attributes_scenario`


**Title:** Scenario [C]

**Description:**

```md
This setting selects which scenario set the Agent should use for your current business setup. Use
`Default Scenario` for standard, system-managed behavior.

**Best Practice:** Keep this on `Default Scenario` unless your account is explicitly configured for
a custom scenario workflow.

Behavior by value:

- **`Default Scenario`:** The Agent uses system-provided scenario mappings for your industry.
- **`Custom Scenario`:** The system expects a custom scenario configuration and uses that context
  for scenario-labeled logic.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This value is used as a label dimension for AKB/topic selection together with
`project_business_industry` in runtime paths such as task-instruction retrieval, task-object schema
retrieval, and intent-type-map template selection. It is also used when appending RAG topics so
appended content remains scoped to the same industry+scenario context.

**Fallbacks:** During initialization, industry setup usually defaults this attribute to
`Default Scenario`. If scenario-labeled intent-type-map templates are missing, the system falls back
to industry default intent-type-map templates.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Combined with this setting for label-scoped AKB retrieval.
- **Logic Interactions:**
  - Restaurant AKB initialization flow: when this setting is `Custom Scenario`, default restaurant
    workflow AKB topics are not auto-created.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `enum`

**Possible values:** `["Default Scenario", "Custom Scenario"]`

**Is hidden:** `true`

---

## `project_attributes_setting_additional_global_conversation_instruction`


**Title:** Conversation - Additional Global Conversation Instruction [C]

**Description:**

````md
Use this setting to add a high-priority global instruction that can override normal conversation
behavior.

**Best Practice:** Treat this as an emergency override. Keep it short (about 2-3 sentences), clear,
and temporary.

If this field is overloaded with long or conflicting instructions, the Agent can become unstable or
inconsistent.

**Examples:**

```txt
Always mention that quoted prices are estimates and may change.
Never ask for a full date of birth.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Read during runtime prompt compilation and appended near the response footer as a
self-instruction when non-empty.

**Fallbacks:** Default initialization sets this field to whitespace. Empty/whitespace effectively
means no additional global override.

**Dependencies:**

- **Primary Settings:**
  - Global prompt-compilation path: This is where the setting is consumed for response generation.
- **Logic Interactions:**
  - Runtime trims whitespace before use; blank content is treated as absent.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_additional_limitations_and_restrictions`


**Title:** Conversation - Additional Limitations and Restrictions [B]

**Description:**

````md
Use this setting to define extra boundaries for what the Agent should not handle directly in
conversation.

This is especially useful in chat, where phone transfer logic does not automatically apply but you
still want the same operational boundaries enforced.

**Best Practice:** Write short, actionable bullet points that describe request types the Agent must
relay or refuse to complete directly.

Example for `restaurant` industry:

```txt
- Confirm that their table reservation is secured;
- Notify that they will be late for an existing reservation;
- Participate in or book a table for a special event mentioned in the context;
- Order catering;
- Report a forgotten or lost item at the restaurant;
- Speak with customer service;
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into the explicit-constraints prompt block used by the supervisory
analysis layer. When present, the system adds an `# ADDITIONAL LIMITATIONS AND RESTRICTIONS` section
to constrain scenario execution.

**Fallbacks:** If empty, this block is omitted and no extra limitations are injected.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_enabled`: Enables a relay-to-team option that
    is appended alongside these limitations.
- **Logic Interactions:**
  - Conversation channel detection: phone sessions append a call-transferring reminder in the same
    limitations block.
  - `project_attributes_restaurant_order_url`: In restaurant initialization, when this advanced
    system configuration is populated, food-order limitations are adjusted automatically.
  - `project_attributes_restaurant_googlemaps_reservation_url`: In restaurant initialization, when
    this advanced system configuration is populated, reservation-related limitations are adjusted
    automatically.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_blocked_phone_numbers`


**Title:** Phone - Blocked Numbers [A]

**Description:**

````md
Use this list to block specific phone numbers from interacting with your voice Agent. Blocked
callers are disconnected automatically when they start a call.

**Best Practice:** Save numbers in full international format and keep the format consistent with how
your telephony integration sends caller IDs.

How this list is used:

- Numbers in this list are proactively blocked on call start.
- Numbers can also be added automatically when repeated spam sessions reach your configured spam
  threshold.

**Example:**

```json
["13334445556", "12223334455"]
```

**Format options (for each phone number in the list):**

- With plus: `+12223334444`
- Without plus: `12223334444`

Both formats are accepted, but include full country code for every entry.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** On voice-call start, each entry in this array is normalized (characters other
than digits and `#`/`*` are dropped, including a leading `+`) and the caller external ID is compared
against the normalized entries. If matched, it triggers a stop-call command for the active voice
integration.

**Fallbacks:** Initialized as an empty array. If empty, no proactive blocking is applied. During
spam-limit enforcement, missing/empty values are treated as an empty list before updates.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_spam_limit`: Reaching the configured threshold appends the user's
    phone number to this list.
  - `project_attributes_setting_voice_integration_service`: Determines which voice integration
    connector receives the stop-call command.
- **Logic Interactions:**
  - Caller identifier matching normalizes every list entry before comparison: digits and the
    `#`/`*` characters are kept, other characters (including a leading `+`) are dropped, so
    `+12223334444` and `12223334444` block the same caller. Spam-limit enforcement applies the
    same normalization to the caller's number and the stored entries before its already-blocked
    check.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_spam_limit`


**Title:** Phone - Spam Limit [A]

**Description:**

```md
This setting defines how many consecutive spam-classified sessions are allowed before a user's phone
number is automatically blocked.

**Best Practice:** Use a positive value to limit abuse while reducing false positives. Set `-1` only
if you want to fully disable automatic spam-based blocking.

Behavior by value:

- **`-1`:** Automatic blocking by spam threshold is disabled.
- **`0` or higher integer:** The system counts consecutive spam sessions and blocks when threshold
  is reached.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Evaluated at session end. If session type contains `spam`, the persona-level
`spam_counter` is incremented. When threshold is reached, the system sends a system log, then
text-messages the caller (`sms_worker_send_sms`: "You have been blocked from contacting us due to
repeated spam calls. If you believe this is a mistake, please contact us via email."), then
appends the caller's detected phone number to `project_attributes_setting_blocked_phone_numbers`,
and resets the counter. Non-spam sessions reset the counter to zero.

**Fallbacks:** Initialized with a default numeric threshold during account setup. Automatic blocking
is skipped for temporal personas and for sessions where a usable phone number is unavailable.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_blocked_phone_numbers`: Target list updated when threshold is
    reached.
- **Logic Interactions:**
  - `project_attributes_setting_check_spam_or_voicemail`: Influences spam/voicemail classification
    inputs that ultimately affect session-type spam labeling.
  - Session semaphore `sessionType`: Spam counter logic activates only when this classification
    includes `spam`.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_cancellation_enabled`


**Title:** Booking - Cancellation - Enabled [B]

**Description:**

```md
This setting turns direct booking cancellation on or off for the Agent. When enabled, the Agent can
execute cancellation flows instead of only sending management links.

**Best Practice:** Enable this only after your cancellation method and booking data mapping are
fully configured.

Behavior by value:

- **Enabled (`True`):** Direct cancellation can be offered (depending on cancellation type and
  booking tool setup).
- **Disabled (`False`):** The Agent falls back to manage-link based cancellation assistance.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In tool-definition logic, this flag controls whether cancellation is handled by
`cancel_booking_tool` (direct cancellation path) or by `send_manage_booking_url_tool` (manage-link
path). In booking validation logic, disabled/default cancellation paths require `manage_booking_url`
on booking records.

**Fallbacks:** In most industry initialization paths, this setting is defaulted to `False`. If empty
or not explicitly `True`, direct cancellation tool exposure is skipped.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_enabled`: Booking tooling must be enabled before any
    cancellation-related tools are exposed.
  - `project_attributes_setting_booking_cancellation_type`: Defines whether cancellation runs
    through `default`, `endpoint`, or `project` handling.
  - `project_attributes_setting_booking_cancellation_url`: Required for `endpoint` cancellation
    flows.
- **Logic Interactions:**
  - Booking records must contain identifiable booking metadata (including booking ID) for direct
    cancellation execution.
  - For manage-link flows, booking records need `manage_booking_url` to be treated as valid for user
    cancellation handling.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_cancellation_type`


**Title:** Booking - Cancellation - Type [C]

**Description:**

```md
This setting controls which cancellation execution path the Agent uses for existing bookings. It
defines whether the Agent sends a manage link or performs direct cancellation.

**Best Practice:** Keep `default` until your direct-cancellation integration is fully configured and
tested end-to-end.

Behavior by value:

- **`default`:** Uses manage-link based flow. The Agent sends an SMS with a booking-management URL
  from the booking record.
- **`endpoint`:** Uses direct cancellation through an HTTP endpoint.
- **`project`:** Uses project-side cancellation handling through a system event.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Tool exposure logic combines this value with
`project_attributes_setting_booking_cancellation_enabled`:

- `endpoint`/`project` enables `cancel_booking_tool`.
- `default` uses `send_manage_booking_url_tool`.

In cancellation execution:

- `endpoint` sends an HTTP `DELETE` request (through `http_connector`) to the configured
  cancellation URL after injecting `booking_id`.
- `project` emits `convo_agent_cancel_booking` with selected booking payload.

Search/validation logic also uses this setting to decide whether only bookings with
`manage_booking_url` are considered valid (`default`) or all future bookings are considered.

**Fallbacks:** Initialized to `default` during common setup. If this value is unsupported while
direct cancellation is enabled, expected cancellation tools may not be exposed.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking tools so cancellation tooling can appear.
  - `project_attributes_setting_booking_cancellation_enabled`: This advanced system configuration is
    the master on/off switch for direct cancellation behavior.
  - `project_attributes_setting_booking_cancellation_url`: Required when this advanced system
    configuration uses `endpoint`.
- **Logic Interactions:**
  - Booking metadata (`manage_booking_url`, booking ID): Determines whether a booking can be managed
    via link (`default`) or canceled directly (`endpoint`/`project`).
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `enum`

**Possible values:** `["default", "endpoint", "project"]`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_cancellation_url`


**Title:** Booking - Cancellation - URL [B]

**Description:**

````md
This is the endpoint template used for direct booking cancellation requests. The Agent replaces
`{booking_id}` in this URL with the selected booking ID.

**Best Practice:** Use a stable HTTPS endpoint and keep the `{booking_id}` placeholder exactly in
the URL path/query position expected by your API.

**Examples:**

```txt
https://example.com/bookings/{booking_id}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used only when the advanced system configuration
`project_attributes_setting_booking_cancellation_type` is set to `endpoint`. The cancellation flow
builds `cancellation_url = url.replace("{booking_id}", booking_id)` and sends an HTTP `DELETE`
request to that URL.

**Fallbacks:** Initialized as empty. If blank or malformed when `endpoint` mode is active, HTTP
cancellation requests fail at runtime.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_cancellation_type`: When this advanced system configuration
    is `endpoint`, this URL is consumed by runtime cancellation logic.
  - `project_attributes_setting_booking_cancellation_enabled`: This advanced system configuration
    must enable direct cancellation.
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking toolset availability.
- **Logic Interactions:**
  - Booking ID extraction/selection: A valid booking ID is required for placeholder replacement.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_enabled`


**Title:** Booking - Check Availability - Enabled [B]

**Description:**

```md
This setting enables or disables availability lookup before booking confirmation. When enabled, the
Agent can actively check available slots for a requested date/time.

**Best Practice:** Enable this only after your availability request setup (type, schema, and
endpoint or project handler) is configured and tested.

Behavior by value:

- **Enabled (`True`):** The Agent can trigger availability checks and include availability context
  in prompts.
- **Disabled (`False`):** Availability checks are not offered by the runtime tool-selection path.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When `True`, runtime tool definitions include `check_availability_tool`, and
prompt builders inject an `<AvailabilityForTheUserRequestedDateTime>` section used by the
Agent/supervisor context. Tool invocation routes into the availability-check runtime flow via
`check_availability_tool`.

**Fallbacks:** Common setup initializes this field as empty (treated as disabled because checks use
exact string match to `True`). Industry setup then applies defaults (for example, enabled by default
for restaurant/hospitality and disabled in several other industries).

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_type`: This advanced system configuration
    defines which availability-check execution branch runs.
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: This advanced
    system configuration is required to construct valid availability requests in non-default
    branches.
  - `project_attributes_setting_booking_check_availability_url`: This advanced system configuration
    is required for HTTP-based availability checks.
- **Logic Interactions:**
  - Availability status/result persona fields are injected into prompt context when this setting is
    enabled.
  - Validation flow can notify/log configuration issues if required availability attributes are
    missing.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_processing_type`


**Title:** Booking - Check Availability - Processing Type [C]

**Description:**

````md
This setting controls how the Agent interprets the availability response after a check request is
sent.

**Best Practice:** Use `formatted_response` when your integration can return a predictable
structured payload. Use `use_llm` only when response format is unstable.

Behavior by value:

- **`use_llm`:** The Agent parses raw response content with LLM-based post-processing.
- **`formatted_response`:** The Agent processes structured response fields directly.
- **`custom`:** Default post-processing is skipped so custom project-side handling can take over.

If your integration returns formatted availability data, keep responses compatible with the schema
below.

Schema:

```json
{
  "type": "object",
  "title": "Availability Response Schema",
  "additionalProperties": true,
  "description": "Universal schema for availability across all industries",
  "required": ["availability"],
  "properties": {
    "range": {
      "type": "string",
      "description": "Human-readable time range (e.g., 'from 01:00 PM to 03:00 PM'). Optional for date-grouped responses. Example: `from 01:00 PM to 03:00 PM`"
    },
    "resourceType": {
      "type": "string",
      "description": "Type of resource being scheduled (optional, inferred if not provided). Examples: location, doctor."
    },
    "availability": {
      "type": "array",
      "description": "List of resources with their available time slots",
      "items": {
        "type": "object",
        "required": ["availableTimeSlots"],
        "properties": {
          "location": {
            "type": "string",
            "description": "DEPRECATED: Use 'resource' instead. Kept for backwards compatibility. Can also represent a date (YYYY-MM-DD) for date-grouped availability."
          },
          "resource": {
            "type": "string",
            "description": "Name/identifier of the resource (e.g., 'Dr. Smith', 'Patio', 'Team A', '2025-11-08')"
          },
          "availableTimeSlots": {
            "type": "array",
            "description": "List of available time slots in hh:mm AM/PM format. Examples: 09:00 AM, 05:00 PM",
            "items": {
              "type": "string"
            }
          }
        }
      }
    },
    "targetAction": {
      "type": "string",
      "description": "Optional action identifier for workflow routing. Example: check_availability"
    }
  }
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Availability response handlers branch on this setting:

- `use_llm`: response is interpreted through LLM-based post-processing.
- `formatted_response`: structured response processors are used (legacy/new, based on feature flag).
- `custom`: default post-processing is skipped and custom project-side handling is expected.

For `formatted_response`, output handling can switch to the new parser when advanced system
configuration
`project_attributes_private_feature_flag_booking_use_new_availability_formatted_response_processor`
is active.

**Fallbacks:** Initialized to `formatted_response` during common setup. Unknown values do not match
any processing branch and can result in no default availability post-processing.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_type`: This advanced system configuration
    determines source/channel of availability response before this processing mode is applied.
- **Logic Interactions:**
  - In `result_success`/`result_error` handlers, availability processing runs only when
    `targetAction` resolves to `check_availability`; the dedicated `receive_available_slots` system
    event uses its own event-scoped processing path.
  - `custom` mode assumes external/custom logic will complete user-facing handling.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `enum`

**Possible values:** `["use_llm", "formatted_response", "custom"]`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_payload_schema_template`


**Title:** Booking - Check Availability - Schema [C]

**Description:**

````md
This setting defines the payload schema used to build availability-check requests from conversation
context.

**Best Practice:** Keep required fields minimal and explicit. Ensure field descriptions are strict
so payload generation remains deterministic.

Request-method behavior:

- For `GET`, the runtime builds `queryParams` from this schema and appends them to the configured
  availability URL.
- For `POST`, the runtime sends request body payload built from this schema.

This attribute supports "templating" - within the text of this attribute, values from other
attributes can be inserted. Special "placeholders" in the format [[attribute_name]] are used for
this purpose.

**Example for restaurants:**

```json
{
  "type": "object",
  "properties": {
    "date": {
      "type": "string",
      "description": "User's preferred date for the reservation in format YYYY-MM-DD. Example: 2024-09-28"
    },
    "time": {
      "type": "string",
      "description": "User's preferred time for the reservation in format HH:MM (24 hours). Example: 20:00. If not provided, default to 19:00",
      "default": "19:00"
    },
    "dateTime": {
      "type": "string",
      "description": "User's preferred date and time for the reservation in format YYYY-MM-DD HH:MM. Combine `date` and `time` properties in the format. Example: 2024-09-28 20:00"
    },
    "partySize": {
      "type": "string",
      "description": "Only one number, the number of people for the reservation, if a range is provided, is set to maximum. Example: 6"
    },
    "timeZone": {
      "type": "string",
      "enum": ["[[project_business_time_zone]]"]
    },
    "restaurantId": {
      "type": "string",
      "enum": ["[[project_attributes_private_dynamic_restaurant_google_restaurant_id]]"]
    },
    "timeFormat": {
      "type": "string",
      "enum": ["12"]
    }
  },
  "required": ["date", "time", "dateTime", "partySize", "timeZone", "restaurantId", "timeFormat"]
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During metadata preparation, this template is merged with availability validation
schema and transformed into a runtime generation schema. At request time, the checking-availability
flow uses that runtime schema to generate `payload` (and `queryParams` for GET mode) before sending
availability requests.

**Fallbacks:** Initialized as empty during common setup. If empty at runtime, availability
validation fails and the system logs a configuration warning instead of sending a request.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_request_http_method`: This advanced
    system configuration controls whether this schema drives GET query parameters or POST request
    body.
  - `project_attributes_setting_booking_check_availability_validation_schema_template`: This
    advanced system configuration is combined with this schema to create the final
    availability-generation schema.
  - `project_attributes_setting_booking_check_availability_max_days_in_advance`: This advanced
    system configuration is referenced by built-in additional validation in generated schema logic.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_multi_location`: When the advanced system configuration
    is enabled, this template can be converted into location-keyed JSON structure.
  - Re-publishing regenerates runtime schema artifacts from this template.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_request_headers`


**Title:** Booking - Check Availability - Request Headers [C]

**Description:**

````md
This setting defines HTTP headers attached to availability-check API requests. Provide headers as a
JSON object where each key is a header name and each value is a header value.

**Best Practice:** Include only required headers (for example API key/auth and content type), and
avoid embedding short-lived tokens unless your update process refreshes them reliably.

**Example:**

```json
{ "X-API-KEY": "<REPLACE_WITH_API_KEY>", "Content-Type": "application/json" }
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In HTTP availability mode, this object is passed directly to `send_request` calls
for both GET and POST request branches.

**Fallbacks:** Initialized to `{}` during common setup. Runtime does not enforce header schema; if
required auth headers are missing/invalid, availability API requests fail at the integration layer.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_type`: This advanced system configuration
    defines when headers are relevant for HTTP-based availability paths (and not consumed by
    project/intercom branches).
  - `project_attributes_setting_booking_check_availability_request_http_method`: This advanced
    system configuration uses the same header object for both GET and POST request branches.
  - `project_attributes_setting_booking_check_availability_url`: This advanced system configuration
    defines the target endpoint receiving these headers.
- **Logic Interactions:**
  - Restaurant default availability flow may use magic-browser path (feature-flag dependent), where
    these HTTP headers are not used.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_request_http_method`


**Title:** Booking - Check Availability - Request HTTP Method [C]

**Description:**

```md
This setting defines which HTTP method the Agent uses when calling your availability endpoint.

**Best Practice:** Use `POST` unless your provider explicitly requires `GET`.

Behavior by value:

- **`GET`:** The Agent builds query parameters from the availability payload schema and appends them
  to the availability URL.
- **`POST`:** The Agent sends the generated availability payload in the request body.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used by availability request routing and schema-building logic. For GET mode,
runtime adds a `queryParams` field into the generation schema and sends `send_request` with
URL+query string. For POST mode, runtime sends `send_request` with `body`.

**Fallbacks:** Initialized to `POST` during common setup. In request logic, any value other than
`GET` follows the POST branch.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_type`: This advanced system configuration
    must route through HTTP availability branch for this method to be used.
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: This advanced
    system configuration defines the generated query params/body structure.
  - `project_attributes_setting_booking_check_availability_url`: This advanced system configuration
    is the endpoint target for both GET and POST.
  - `project_attributes_setting_booking_check_availability_request_headers`: This advanced system
    configuration supplies headers for both method branches.
- **Logic Interactions:**
  - Availability request is sent only after validation/reconfirmation gates pass.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `enum`

**Possible values:** `["GET", "POST"]`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_validation_schema_template`


**Title:** Booking - Check Availability - Validation Schema [C]

**Description:**

````md
This setting defines validation rules that the Agent applies before sending an availability-check
request.

**Best Practice:** Use clear boolean validation fields with descriptions that explain the condition
to verify and how the Agent should interpret failures.

If validation fails, the Agent does not continue with the request and instead asks the user to
correct missing/invalid details.

**Example for restaurants:**

```json
{
  "type": "object",
  "properties": {
    "regularGroup": {
      "type": "boolean",
      "description": "Set to true if **persons < [[project_attributes_restaurant_large_group_reservation_minimum_party_size]]**."
    }
  },
  "required": ["regularGroup"]
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During schema preparation, this template is combined with the availability payload
schema to build a runtime generation schema for checking availability. Request flow then evaluates
`validationRecap` and `additionalValidation` from generated output to decide whether to proceed,
reconfirm data, or stop and guide the user, while `validation` remains part of the generated schema
object.

**Fallbacks:** Initialized as empty in common setup. When this value is empty or `{}`, schema
preparation uses a default permissive validation schema so request generation can still proceed.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: This advanced
    system configuration is required because validation is merged with payload schema.
  - `project_attributes_setting_booking_check_availability_max_days_in_advance`: This advanced
    system configuration is enforced by built-in additional validation checks in generated schema
    logic.
  - `project_attributes_setting_booking_check_availability_working_hours_status`: This advanced
    system configuration can add working-hours gate checks before request dispatch.
- **Logic Interactions:**
  - Multi-location feature can convert this template into location-keyed JSON structure.
  - Publishing regenerates runtime validation artifacts from this template.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_type`


**Title:** Booking - Check Availability - Type [C]

**Description:**

```md
This setting defines which integration path the Agent uses to check availability. Choose the type
that matches where your availability data is sourced.

**Best Practice:** Keep this aligned with your actual integration setup. Mismatched type and
endpoint configuration will cause failed checks.

Behavior by value:

- **`default`:** Uses built-in provider-specific default route for supported industries.
- **`endpoint`:** Uses HTTP endpoint requests for availability checks.
- **`intercom`:** Uses Intercom actor-event request path.
- **`project`:** Uses project-side system event flow for availability checks.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Branches in availability request and receive/error handlers:

- `default`:
  - restaurant can use built-in provider path (`get_restaurant_availability`) when corresponding
    feature path is active.
  - hospitality default route uses dedicated event path (`check_availability_hospitality`).
- `endpoint`: uses HTTP `send_request` branch with configured method/headers/url.
- `intercom`: sends `send_actor_event` (`get_booking_windows`) through Intercom.
- `project`: sends system event `get_available_slots`.

Result/error processing also branches by this setting and always filters by
`targetAction=check_availability`.

**Fallbacks:** Initialized to `default` during common setup. If required prerequisites for selected
type are missing (for example provider-specific default requirements or HTTP URL), validation blocks
the request and logs configuration guidance.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_enabled`: This advanced system
    configuration must allow availability checks before type-specific routing is used.
  - `project_attributes_setting_booking_check_availability_processing_type`: This advanced system
    configuration defines how responses are interpreted after type-specific request execution.
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: This advanced
    system configuration is used to generate request payload for non-provider-default branches.
  - `project_attributes_setting_booking_check_availability_url`: This advanced system configuration
    is required for HTTP endpoint branch.
  - `project_attributes_setting_booking_check_availability_request_http_method`: This advanced
    system configuration controls HTTP method in endpoint/default HTTP fallback branches.
- **Logic Interactions:**
  - For `intercom`, data-injection flow prepares/maintains Intercom actor context used by
    availability requests.
  - For industry-specific default routes, additional business prerequisites are validated before
    dispatch.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `enum`

**Possible values:** `["default", "endpoint", "intercom", "project"]`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_url`


**Title:** Booking - Check Availability - Link (URL) [B]

**Description:**

```md
This setting defines the endpoint or business URL used during availability checks. Use it when your
availability flow depends on a specific external URL.

**Best Practice:** Use a stable HTTPS URL and verify that it matches the selected availability-check
type and request method.

Examples of use:

- API endpoint for availability checks (HTTP branch).
- Business listing URL for provider-specific availability lookup (industry-specific default branch).

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In HTTP request branches, runtime sends availability requests to this URL (`GET`
with query params or `POST` with body). URL validation is enforced for branches that route directly
through HTTP.

In hospitality default-provider flow, worker logic may use this URL as `businessUrl` hint to improve
business matching.

In restaurant `default` mode, provider-specific routing can proceed without URL validation. If that
provider path is not used, request flow falls back to HTTP dispatch and this URL is used there.

**Fallbacks:** Initialized as empty in common setup. If HTTP dispatch is used while this field is
empty, availability checks fail and error handling reports a request problem. In hospitality default
mode, when empty, matching can still proceed using `project_business_name` only.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_type`: This advanced system configuration
    determines whether this URL is required (for example HTTP branch) or optional/not used in other
    branches.
  - `project_attributes_setting_booking_check_availability_request_http_method`: This advanced
    system configuration defines how this URL is called in HTTP branch (`GET`/`POST`).
  - `project_attributes_setting_booking_check_availability_request_headers`: This advanced system
    configuration supplies headers for HTTP requests sent to this URL.
- **Logic Interactions:**
  - Industry/provider-specific default branches can short-circuit URL requirement checks.
  - Restaurant default mode may bypass URL usage on provider path, then use this URL in HTTP
    fallback path.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_window`


**Title:** Booking - Check Availability - Window [C]

**Description:**

```md
This setting defines a configurable availability-check window value used by schema-driven booking
flows.

**Best Practice:** Keep this value aligned with your provider limits (for example search horizon or
window constraints expected by your booking backend).

Behavior notes:

- This value takes effect only when your availability payload schema references it.
- If your schema does not reference this setting, changing it has no runtime impact.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Common initialization sets this value to `12`. The restaurant default availability
payload schema references it via template placeholder, so compiled request payload can include
`bookingWindow`.

External module flows may also read this value directly for interval calculations.

**Fallbacks:** If omitted from payload schema templates, runtime availability requests proceed
without using this value.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: This advanced
    system configuration must reference the placeholder for this value to be included in payload.
  - `project_attributes_setting_booking_check_availability_type`: This advanced system configuration
    determines which branch consumes the generated payload.
- **Logic Interactions:**
  - When your active availability schema includes
    `[[project_attributes_setting_booking_check_availability_window]]`, this value is inserted into
    the generated request payload.
  - If that placeholder is not used, this value does not affect schema-generated payload fields.
  - Some project-specific booking integrations can read this value directly as a time-window for
    date-range calculations, even when the payload schema does not include the placeholder.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_working_hours_status`


**Title:** Booking - Check Availability - Working Hours Validation - Enabled [C]

**Description:**

```md
This setting controls whether the Agent validates requested slot time against business working hours
before sending an availability request.

**Best Practice:** Keep this enabled if your business must strictly avoid off-hours booking checks.

Behavior by value:

- **Enabled (`True`):** Agent blocks out-of-hours requests and asks user for a different day/time
  before calling availability source.
- **Disabled (`False`):** Agent skips this gate and proceeds directly to availability request flow.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Availability request flow checks this flag before dispatching requests. If
enabled, it evaluates working-status using requested day/time extracted from additional validation
output. For `non_working_day` or `non_working_hours`, it sends urgent guidance and exits without
sending request.

**Fallbacks:** Initialized to `True` during common setup. Working-status resolver falls back to LLM
evaluation only when the runtime working-hours object is empty. If that object is available, status
is evaluated directly from the structured schedule data.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: This advanced
    system configuration feeds the compiled availability schema that includes
    `additionalValidation.requestedDayOfWeek` and `additionalValidation.requestedTimeFormatted`,
    which are consumed by this gate.
  - `project_attributes_setting_booking_check_availability_type`: This advanced system configuration
    selects the downstream availability request path; when this gate is enabled and fails, request
    dispatch is short-circuited before that type-specific path runs.
  - `project_business_working_hours`: Base schedule source used to build runtime working-hours
    structures consumed by status checks.
- **Logic Interactions:**
  - If disabled, requests can proceed for any requested slot (subject to downstream provider
    response).
  - Resolver uses LLM fallback only when structured schedule data is empty at runtime.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_email`


**Title:** Booking - Email [C]

**Description:**

```md
This setting defines the base email used in booking payload generation. The Agent derives
booking-specific email values from this base address.

**Best Practice:** Use a dedicated booking mailbox on your own domain (for example a monitored
shared inbox or catch-all), so provider-side booking requests remain traceable.

Example value:

- `bookings@yourbusiness.com`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In the currently exported runtime, restaurant booking execution paths validate
this base email format, then generate a booking-specific address by combining local part + user
phone + domain. This is used in both default restaurant create-booking approaches (new path and
legacy path).

On retry, a random postfix is appended to avoid duplicate-email rejections in provider flows.

**Fallbacks:** If this field is empty or invalid, runtime falls back to a generic default email
format and still derives booking-specific addresses from phone data.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking flow paths where generated email is used.
  - `project_attributes_setting_booking_type`: This advanced system configuration determines whether
    restaurant/default create-booking branches are active and therefore consume this derived email.
- **Logic Interactions:**
  - User phone number is used to personalize the booking-specific email variant when available. If
    phone data is unavailable, runtime can still build an email using the base local-part/domain
    pattern.
  - Retry handling adds random postfix to reduce provider duplicate detection.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_enabled`


**Title:** Booking - Enabled [B]

**Description:**

```md
This setting turns booking capabilities on or off for the Agent. When enabled, the Agent can start
booking actions and booking-management interactions.

**Best Practice:** Enable only after booking type, endpoint/integration settings, and payload
schemas are configured.

Behavior by value:

- **Enabled (`True`):** Booking tools and booking action-state context are available.
- **Disabled (`False`):** Booking tools are not exposed in the runtime tool-selection path.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Tool-definition logic adds booking tools only when this flag is `True` (for
example `create_booking_tool`, `search_booking_tool`, and related cancellation or manage-link
tools). Prompt builders also include booking action-state blocks only when enabled.

**Fallbacks:** Common setup initializes this field as empty (treated as disabled unless explicitly
set to `True`). Industry setup typically applies default value per vertical.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_type`: This advanced system configuration defines which
    booking execution branch runs once booking is enabled.
  - `project_attributes_setting_booking_fallback_processing_type`: This advanced system
    configuration affects failed-booking behavior for enabled booking flows.
  - `project_attributes_setting_booking_check_availability_enabled`: Often paired with booking flows
    when availability-first behavior is required.
- **Logic Interactions:**
  - Booking events are triggered only when booking tools are exposed and selected by runtime.
  - Booking state text is injected into prompt context only when this flag is enabled.
  - In default restaurant mode, this flag enables booking capabilities, while advanced system
    configuration
    `project_attributes_private_feature_flag_booking_use_new_restaurant_create_booking_approach`
    still determines whether the new or old booking approach runs.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_fallback_processing_type`


**Title:** Booking - Fallback Processing Type [C]

**Description:**

```md
This setting controls what the Agent does when a booking attempt fails.

**Best Practice:** Use `default` unless you have a project-side fallback workflow that consumes the
custom fallback event reliably.

Behavior by value:

- **`default`:** Keeps built-in fallback behavior. In default restaurant booking, this allows
  runtime to retry through the old (legacy) restaurant approach when a booking attempt in the new
  approach fails.
- **`custom`:** Sends `process_booking_fallback_custom` system event with payload metadata and skips
  built-in fallback branch.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Evaluated when booking result is negative/error. `custom` mode emits
`process_booking_fallback_custom` and returns immediately. `default` continues into built-in
fallback branch. In restaurant/default booking, that built-in branch can switch execution to the
legacy restaurant flow after unsuccessful booking responses.

**Fallbacks:** Initialized to `default` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking flow for fallback processing to be relevant.
  - `project_attributes_setting_booking_type`: This advanced system configuration influences where
    errors/results originate before fallback handling is applied.
- **Logic Interactions:**
  - `project_business_industry`: Built-in default fallback behavior differs by industry-specific
    booking paths.
  - `project_attributes_private_feature_flag_booking_use_new_restaurant_create_booking_approach`:
    When this advanced system configuration is enabled, failed default restaurant bookings can be
    retried through the legacy approach when fallback mode is `default`.
  - Custom mode requires external workflow/listener for `process_booking_fallback_custom` event.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `enum`

**Possible values:** `["default", "custom"]`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_check_availability_max_days_in_advance`


**Title:** Booking - Max Days in Advance [C]

**Description:**

```md
This setting limits how far into the future the Agent can process booking-availability checks. It
helps enforce your business booking window policy.

**Best Practice:** Match this value to the real booking window enforced by your booking provider and
internal operations (for example, staffing and inventory planning).

Behavior by value:

- **Lower value:** The Agent will reject farther-future date requests earlier and ask for another
  date.
- **Higher value:** The Agent accepts a wider future range before sending availability checks.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During availability request preparation, a value greater than zero enables a
deterministic, code-side booking-window check. When the availability payload includes
`additionalValidation.isWithinBookingWindow`, runtime compares the requested ISO date
(`YYYY-MM-DD`) with today's date in the project time zone advanced by this many days; if the
requested date is past the window end, runtime sends an urgent user message and stops before
dispatching the availability request. An empty or zero value applies no booking-window limit at
all.

**Fallbacks:** Initialized to `30` in common default settings.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_enabled`: This advanced system
    configuration must be enabled for availability-window validation to be executed.
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: This advanced
    system configuration feeds the compiled availability schema, which includes
    `additionalValidation.isWithinBookingWindow` when the tool enables the advance-days check. With
    a positive booking window, runtime decides the window verdict in code; the model-filled
    `isWithinBookingWindow` value is consulted only when the requested date is not an ISO
    `YYYY-MM-DD` date or the project time zone does not match a named `Area/City` zone.
  - `project_business_time_zone`: The code-side booking-window comparison computes today's date
    in this time zone.
- **Logic Interactions:**
  - `project_attributes_setting_booking_check_availability_working_hours_status`: Working-hours
    validation runs as a separate gate in the same availability flow.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_phrase_template_on_booking_submitting`


**Title:** Booking - Phrase Template on Submitting [B]

**Description:**

```md
This setting defines the message the Agent can send right after a booking request is submitted and
before final confirmation is received.

**Best Practice:** Keep this phrase short and neutral (for example, "Your request is being
processed"), and avoid wording that implies confirmed success.

Example value:

- `Your booking request is being processed.`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During booking submission handling, runtime reads this value and, when non-empty,
sends it to the user as an urgent instruction message in schema-based booking submission branches
(including the new default restaurant approach).

**Fallbacks:** Common default is empty. Many industry initializers set a non-empty default phrase.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking flow paths where submitting phrase can be emitted.
  - `project_attributes_setting_booking_type`: This advanced system configuration determines which
    booking dispatch branch runs before this phrase step.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_booking_use_new_restaurant_create_booking_approach`:
    When this advanced system configuration is disabled, default restaurant booking runs through the
    legacy approach with its own built-in submission messaging, so this phrase template may not be
    used.
  - If empty, no submitting phrase is sent and flow proceeds without this extra user-facing message.
  - `project_attributes_setting_booking_phrase_template_on_booking_success`: Success phrase is a
    separate post-confirmation step and should not duplicate "request submitted" wording.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_phrase_template_on_booking_success`


**Title:** Booking - Phrase Template on Successful Booking [B]

**Description:**

```md
This setting defines the optional confirmation message the Agent sends after a successful booking
response.

**Best Practice:** Use this for concise success confirmation only. Keep operational specifics (for
example, links or follow-up actions) in dedicated notification settings if needed.

Example value:

- `Meanwhile, your booking has been successfully confirmed.`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** After booking result is processed as successful, runtime reads this value and, if
non-empty, sends it as an urgent user instruction message in booking branches that emit standard
booking-success responses (including the new default restaurant approach).

**Fallbacks:** Common default is empty. Industry initializers often provide a default success
phrase.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking flow for success messaging to become relevant.
  - `project_attributes_setting_booking_type`: This advanced system configuration controls upstream
    booking execution that can produce a success result.
- **Logic Interactions:**
  - Emitted only on successful booking outcomes.
  - In default restaurant legacy flow, confirmation handling can follow separate task/SMS behavior
    and may complete without using this phrase template.
  - If empty, no success phrase is sent even when booking succeeds.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_payload_schema_template`


**Title:** Booking - Create Booking - Schema [C]

**Description:**

````md
This setting defines the JSON payload schema the Agent uses to build booking requests. It controls
which booking fields are extracted from conversation context before submission.

**Best Practice:** Keep required fields strict and minimal, and write explicit field descriptions so
payload generation is deterministic and easier to validate.

This attribute supports "templating" - within the text of this attribute, values from other
attributes can be inserted. Special "placeholders" in the format [[attribute_name]] are used for
this purpose.

**Example for restaurants:**

```json
{
  "type": "object",
  "properties": {
    "dateTime": {
      "type": "string",
      "description": "Date and time of the reservation (YYYY-MM-DD HH:MM). Example: 2024-02-15 14:00"
    },
    "timeFormatted": {
      "type": "string",
      "description": "Time of the reservation in 12 hour format (hh:mm A). Example: 02:00 PM"
    },
    "partySize": {
      "type": "integer",
      "description": "Number of people for the reservation"
    },
    "firstName": {
      "type": "string",
      "description": "Guest first name."
    },
    "lastName": {
      "type": "string",
      "description": "Guest last name. If not provided, set the same as firstName."
    },
    "phoneNumber": {
      "type": "string",
      "description": "Customer's phone number in E.164 format"
    },
    "place": {
      "type": "string",
      "description": "Location or area within the restaurant (e.g., Patio). Set to one of the seating options."
    }
  },
  "required": [
    "dateTime",
    "timeFormatted",
    "partySize",
    "firstName",
    "lastName",
    "phoneNumber",
    "place"
  ]
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Booking-schema preparation combines this payload schema with the booking
meta-fields schema to produce the runtime booking-generation schema used by schema-based booking
branches. In those branches, the Agent uses the generated schema to produce booking `payload` data
from conversation context.

For default restaurant booking, runtime supports two create-booking approaches:

- **New approach (primary when advanced system configuration
  `project_attributes_private_feature_flag_booking_use_new_restaurant_create_booking_approach` is
  enabled):** Uses this schema-driven payload generation flow.
- **Old approach (primary when that advanced system configuration is disabled):** Uses a separate
  restaurant task-format schema path instead of this payload schema.
- **Legacy fallback behavior:** Even when the new approach is primary, failed booking attempts can
  be retried through the old approach when
  `project_attributes_setting_booking_fallback_processing_type` stays `default`.

**Fallbacks:** Common setup initializes this attribute as empty. If schema-based booking path is
required and booking schema is missing, runtime blocks that schema-based dispatch and logs
configuration guidance. In default restaurant booking, runtime can still proceed through the old
approach when its prerequisites are configured (for example, required restaurant provider/task
format data). If meta-fields schema is empty, system applies a minimal default meta-fields schema so
the combined schema can still be built.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_meta_fields_schema_template`: This advanced system
    configuration is merged with this payload schema to form the booking-generation schema.
  - `project_attributes_setting_booking_type`: This advanced system configuration defines which
    booking execution branch consumes the generated payload.
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking flow paths where generated payload is used.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_booking_use_new_restaurant_create_booking_approach`:
    This advanced system configuration controls whether default restaurant booking uses this
    schema-driven approach as the primary path or routes primarily through the old approach.
  - `project_attributes_setting_booking_fallback_processing_type`: When set to `default`, failed
    default-restaurant booking attempts in the new approach can fallback to the old approach.
  - Publishing regenerates compiled booking schema artifacts from this template.
  - Multi-location mode converts this attribute into location-keyed JSON and selects the active
    location schema at runtime.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_request_headers`


**Title:** Booking - Request Headers [C]

**Description:**

````md
This setting defines HTTP headers attached to booking API requests. Provide headers as a JSON object
where each key is a header name and each value is a header value.

**Best Practice:** Include only headers required by your endpoint (for example auth/API key and
content type), and keep token rotation strategy in sync with this configuration.

**Example:**

```json
{ "X-API-KEY": "<REPLACE_WITH_API_KEY>", "Content-Type": "application/json" }
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In HTTP booking branch, this object is passed directly to `send_request` as
request headers when submitting `book_slot` requests.

**Fallbacks:** Initialized to `{}` during common setup. Runtime does not validate required header
presence, so missing/invalid headers fail at endpoint/integration level.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_type`: This advanced system configuration determines whether
    HTTP request branch is used (where these headers apply).
  - `project_attributes_setting_booking_url`: This advanced system configuration defines the
    endpoint that receives requests with these headers.
  - `project_attributes_setting_booking_payload_schema_template`: This advanced system configuration
    defines request body payload sent together with these headers.
- **Logic Interactions:**
  - Intercom/project booking branches do not consume these headers.
  - In default restaurant booking, both the new and old approaches use provider/task integrations
    instead of HTTP request headers from this setting.
  - In test mode, HTTP booking dispatch is skipped, so these headers are not sent.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_meta_fields_schema_template`


**Title:** Booking - Meta Fields Schema [C]

**Description:**

````md
This setting defines the schema for booking meta fields generated alongside booking payload data.
For current flows, `smsBodyText` is the primary supported field.

**Best Practice:** Keep meta fields optional and purpose-specific. Use `smsBodyText` only when you
need controlled booking-related SMS wording from generated booking details.

**Example for restaurants:**

```json
{
  "type": "object",
  "properties": {
    "smsBodyText": {
      "type": "string",
      "description": "Generate the SMS with booking confirmation using the following template: [[project_business_name]] booking confirmation. Congratulations! Your booking for [number of people] on [date] at [time] has been successfully submitted."
    }
  },
  "required": ["smsBodyText"]
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Schema preparation merges this template with booking payload schema into the
runtime booking-generation schema. Booking flows then generate `metaFields` together with `payload`
from conversation context in schema-based booking branches (including the new default restaurant
approach).

When `smsBodyText` is present, booking flows can use it for booking-related SMS messaging (for
example success-notification SMS composition).

When default restaurant booking runs through the old legacy approach (either as the primary path or
as fallback), booking request construction uses a separate task-format path and does not rely on
this meta-fields schema for core payload generation.

**Fallbacks:** Common setup initializes this value as empty. If empty or `{}`, schema preparation
uses a minimal default meta-fields schema, so booking generation still proceeds without custom
meta-field output.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_payload_schema_template`: This advanced system configuration
    is required because meta fields are merged with booking payload schema.
  - `project_attributes_setting_booking_success_notification_on_sms_enabled`: This advanced system
    configuration controls whether generated SMS text is actually sent in success-notification path.
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking flow paths where generated meta fields are consumed.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_booking_use_new_restaurant_create_booking_approach`:
    This advanced system configuration controls whether default restaurant booking primarily uses
    schema-generated `metaFields` (new approach) or legacy task-format payloads (old approach).
  - Publishing regenerates booking-generation artifacts from this template.
  - Multi-location mode can convert this template into location-keyed JSON structure.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_success_notification_on_email_enabled`


**Title:** Booking - Email Notification On Successful Booking [B]

**Description:**

```md
This setting controls whether the Agent sends an internal email notification after a booking is
successfully confirmed.

**Best Practice:** Enable this when your team needs a manager-side confirmation trail for completed
bookings.

Behavior by value:

- **Enabled (`True`):** Sends a success notification email to the manager email address.
- **Disabled (`False`):** No manager success email is sent.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** After a successful booking result, runtime sends `email_worker_send_email` to
`project_business_manager_email` with content built from booking payload details in branches that
emit standard booking-success responses (including the new default restaurant approach).

**Fallbacks:** Initialized to `False` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_business_manager_email`: Target recipient for success emails.
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking flow for success notifications to become relevant.
  - `project_attributes_setting_booking_type`: This advanced system configuration determines which
    booking branch produces the success response that triggers this notification.
- **Logic Interactions:**
  - This flag affects only success notifications; failed-booking manager email handling follows
    separate fallback logic.
  - In default restaurant legacy flow, booking completion can happen through separate worker/task
    handling and may not trigger this success-email step.
  - Runs independently from user-facing success phrase settings.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_success_notification_on_sms_enabled`


**Title:** Booking - SMS Notification On Successful Booking [B]

**Description:**

```md
This setting controls whether the Agent sends booking-success SMS confirmation to the user.

**Best Practice:** Keep this enabled when your booking flow should confirm success directly to the
user over messaging channels.

Behavior by value:

- **Enabled (`True`):** Agent attempts to send a user-facing success SMS message.
- **Disabled (`False`):** No success SMS notification is sent.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** On successful booking, runtime composes SMS text from booking
`metaFields.smsBodyText` plus optional `manage_booking_url` and sends it via
`convoagent_send_notification_message` in branches that emit standard booking-success responses
(including the new default restaurant approach).

**Fallbacks:** Initialized to `True` during common setup. If generated SMS text is empty, message is
not sent even when enabled.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_meta_fields_schema_template`: This advanced system
    configuration can generate `smsBodyText` used in success SMS body.
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking flow for success SMS handling to become relevant.
  - `project_attributes_setting_booking_type`: This advanced system configuration determines the
    booking branch that produces success output (including optional manage URL).
- **Logic Interactions:**
  - If `manage_booking_url` exists in booking result, it is appended to SMS text.
  - In default restaurant legacy flow, user SMS/confirmation handling can follow separate
    worker/task logic instead of this success-notification branch.
  - SMS send is independent from manager email success notification flag.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_type`


**Title:** Booking - Type [C]

**Description:**

```md
This setting defines which integration path the Agent uses to submit booking requests and process
booking results.

**Best Practice:** Match this value to your real booking backend wiring, and verify required
settings for the selected path (schema, URL, integration actor/event context).

Behavior by value:

- **`default`:** Uses built-in default booking logic. For restaurant booking, this includes two
  approaches: new approach and old legacy approach (used either as primary path or fallback,
  depending on advanced configuration).
- **`endpoint`:** Uses HTTP request branch to submit booking payload to configured booking URL.
- **`intercom`:** Uses Intercom actor-event booking branch.
- **`custom`:** Reserved for advanced custom setups.
- **`project`:** Uses project-side system event (`book_slot`) for booking execution.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Booking submission, booking result handling, and booking pre-validation branch
behavior by this setting:

- `intercom` -> sends actor event and expects intercom-style result payload.
- `project` -> sends `book_slot` system event and expects wrapped project result payload.
- `default` -> for restaurant booking, can run the new approach (schema-based/provider-integrated)
  or the old legacy task-based approach; for non-restaurant/default contexts, proceeds through the
  shared HTTP-style booking request path.
- `endpoint` -> follows HTTP `send_request` booking branch.
- `custom` -> currently follows endpoint-style HTTP branch in core runtime unless extended by
  project-side custom logic.

In default restaurant booking, advanced configuration
`project_attributes_private_feature_flag_booking_use_new_restaurant_create_booking_approach` selects
which approach is primary. With
`project_attributes_setting_booking_fallback_processing_type=default`, failed new-approach booking
attempts can fallback to the old approach.

Data-injection runtime also uses this setting to decide whether Intercom actor context must be
created/maintained.

**Fallbacks:** Initialized to `default` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_payload_schema_template`: Required for schema-based booking
    payload generation (including `intercom`, `project`, `endpoint`, current `custom`, and the new
    default-restaurant approach). In default-restaurant legacy-capable path, runtime can execute via
    separate restaurant prerequisites.
  - `project_attributes_setting_booking_url`: Required for HTTP-style branches (`endpoint`, and
    non-intercom/project paths including current `custom` handling).
  - `project_attributes_setting_booking_request_headers`: Applied in HTTP booking branch.
  - `project_attributes_setting_booking_enabled`: This advanced system configuration must enable
    booking tools/flows before type-specific routing is used.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_booking_use_new_restaurant_create_booking_approach`:
    Controls whether `default` restaurant booking primarily uses the new or old approach.
  - `project_attributes_setting_booking_fallback_processing_type`: In restaurant/default mode,
    controls whether failed booking attempts can fallback to legacy handling or are delegated to
    custom fallback eventing.
  - Restaurant default branch has additional prerequisites (for example restaurant provider IDs).
  - Validation blocks booking dispatch when required type-specific prerequisites are missing.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `enum`

**Possible values:** `["default", "endpoint", "intercom", "custom", "project"]`

**Is hidden:** `true`

---

## `project_attributes_setting_booking_url`


**Title:** Booking - Link (URL) [B]

**Description:**

```md
This setting defines the endpoint URL used to submit booking requests in HTTP-based booking flows.

**Best Practice:** Use a stable HTTPS endpoint that accepts your configured booking payload and
headers, and keep this URL aligned with your selected booking type.

**Examples:**

- REST API endpoint for booking creation.
- Integration webhook endpoint that accepts booking payloads.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In core booking runtime, pre-validation checks this value before dispatch in
branches that require HTTP submission. In those URL-based branches, runtime reads this attribute and
sends `send_request` (`targetAction="book_slot"`) with POST body payload and configured request
headers.

In default restaurant booking, both approaches (new and old) can run through provider/task
integrations without using this URL.

**Fallbacks:** Initialized as empty during common setup. In core booking runtime, if a URL-dependent
branch is active and this value is empty, booking request dispatch is blocked and runtime logs
configuration guidance.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_type`: This advanced system configuration determines whether
    the active booking path uses URL-based HTTP submission or a non-URL booking path.
  - `project_attributes_setting_booking_request_headers`: This advanced system configuration is sent
    together with requests to this URL.
  - `project_attributes_setting_booking_payload_schema_template`: This advanced system configuration
    defines booking payload submitted to this URL.
- **Logic Interactions:**
  - Restaurant default branch can bypass direct URL requirement in both the new and old approaches.
  - In test mode, HTTP booking dispatch is skipped even if URL is configured.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_calculation_context`


**Title:** Calculation Context [B]

**Description:**

````md
This setting stores the pricing context the Agent uses when calculating estimates for products and
services.

**Best Practice:** Keep pricing entries explicit and easy to parse (service name, package options,
special bundles) so calculations stay consistent.

To enable reliable calculation behavior:

1. Put complete pricing data in this field (see **Pricing Example**).
2. Ensure your advanced tools configuration includes trigger configuration for `calculation_tool`
   (see **Enabling Tool Example**).
3. Define output and reasoning constraints in Calculation Rules.

**Pricing Example:** Products and services pricing.

```
**Laser hair removal upper legs**
- 1 session: 10$
- 5 sessions: 40$
**Laser hair removal full legs**
- 1 session: 12$
- 5 sessions: 50$

**Active special offers**
- Laser hair removal full legs 8 sessions: 80$
```

**Enabling Tool Example:**

The trigger configuration has to be filled as follows:

```json
{
  "tools": {
    "calculation_tool": {
      "description": "The agent calculates the price and informs the user about it.",
      "conditions": {
        "agentPromised": {
          "type": "boolean",
          "description": "The agent clearly states that they are going to calculate the price right now. So their <LatestConvoAgentAnswer> should contain something like: \"I will calculate the price for you...\", \"Let me calculate the estimate...\", \"Give me a moment, I will calculate...\", etc. Statements of capability (e.g., \"I can calculate\", \"I could estimate\") or conditional offers are NOT firm intentions and must be ignored."
        }
      },
      "useConversationHistory": false
    }
  }
}
```

`conditions` is an object containing one or more conditions, conversation must match to execute
calculation.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Calculation runtime reads this attribute as `<Pricing>` context and combines it
with specials and conversation transcript before generating calculation output.

**Fallbacks:** Initialized as empty during common setup. Runtime does not hard-validate non-empty
pricing context; empty values can still trigger tool flow but lead to low-quality or ambiguous
estimates.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_calculation_rules`: This advanced system configuration provides
    output-format and reasoning constraints for calculation generation.
  - `project_attributes_current_specials`: Promotions/special offers are injected alongside pricing
    context.
  - `project_attributes_settings_platform_tools`: Must expose `calculation_tool` to allow runtime
    triggering of calculation flow.
- **Logic Interactions:**
  - Trigger routing depends on tool-caller conditions in
    `project_attributes_settings_platform_tools`.
  - Calculation output is sent to user via urgent-message event.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_calculation_rules`


**Title:** Calculation Rules [B]

**Description:**

````md
This setting defines the calculation and response rules the Agent must follow when producing price
estimates.

**Best Practice:** Use short, explicit directives (for example, how to apply offers, summarize
totals, and format the final answer) to reduce inconsistent calculation behavior.

**Examples:**

```
- Respond with a summary price of all products user has mentioned.
- Pay attention for any special offers.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Calculation runtime injects this attribute as the `Output Format` instruction
block for generation.

**Fallbacks:** Initialized as empty during common setup. If empty, calculation flow still runs but
without explicit output/rule constraints.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_calculation_context`: Main pricing data source interpreted under
    these rules.
  - `project_attributes_current_specials`: Offer context that rules can require to prioritize.
  - `project_attributes_settings_platform_tools`: Must expose `calculation_tool` for these rules to
    be applied in runtime calculation flow.
- **Logic Interactions:**
  - Conflicting or vague rules can degrade deterministic pricing output.
  - Rules affect generation style and decision logic but do not enforce hard arithmetic validation.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_calendar_injection_is_enabled`


**Title:** Calendar Injection [C]

**Description:**

```md
This setting controls whether the system refreshes generated calendar context and injects it into
one gated prompt path for date reasoning. When enabled, that path gets an up-to-date calendar block
that improves date interpretation.

**Best Practice:** Keep this enabled unless you intentionally manage date context another way. If
you disable it, verify that your date-sensitive flows still behave as expected.

Behavior by value:

- **Enabled (`True`):** The system refreshes generated calendar context during the background
  preparation cycle and injects calendar context in the gated prompt path.
- **Disabled (`False`):** The gated prompt path skips calendar injection and the background
  generation step does not refresh calendar context, but previously stored calendar data can still
  appear in other prompt/runtime paths.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This advanced system configuration is checked in two key places: a background
preparation path that regenerates calendar context, and a prompt section that conditionally injects
`<ConvoAgentCalendar>`. Separately, the main base prompt can still include the stored prompt
calendar directly, so this setting controls refresh behavior and one gated injection path rather
than every calendar reference in runtime.

**Fallbacks:** Initialized to `True` in common setup. Runtime Flows use different empty-value
defaults (`True` in background refresh path, `False` in the gated prompt section), so explicit
configuration is recommended. Disabling this setting does not globally remove calendar context from
all runtime consumers; previously generated calendar data can still be referenced by other
date-reasoning paths.

**Dependencies:**

- **Primary Settings:**
  - `project_business_time_zone`: Calendar generation uses this timezone for day/week boundaries and
    labels.
- **Logic Interactions:**
  - `project_attributes_setting_data_injection_is_enabled`: The same background preparation cycle
    also handles data injection, but calendar refresh logic runs before the data-injection on/off
    gate.
  - Date-sensitive flows that consume stored calendar context (for example availability checks,
    meeting setup, and structured extraction tasks) may still reference calendar data even when this
    setting is disabled, if calendar data was generated earlier.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_chat_split_messages`


**Title:** Chat - Split Long Messages [C]

**Description:**

```md
This setting controls whether the Agent splits certain chat replies into two messages for better
readability.

**Best Practice:** Keep this enabled for chat-first experiences where a short follow-up question
after an explanation improves response clarity.

Behavior by value:

- **Enabled (`True`):** For qualifying chat replies, Agent sends explanatory part first and the
  trailing question as a second message.
- **Disabled (`False`):** Agent sends standard single-message replies.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In chat channel, reply generation switches to a send-one-by-one path when enabled.
That path splits output only when response ends with a question and contains multiple sentences;
otherwise it sends one message.

Broadcast conversation analysis applies compatible split logic to normalize latest-agent-answer
format before memory-based analysis.

**Fallbacks:** Initialized to `True` during common setup.

**Dependencies:**

- **Primary Settings:**
  - Conversation channel routing: This setting is applied only for chat-channel flows.
- **Logic Interactions:**
  - Voice/webcall channels do not use this split path.
  - Split path adds a short delay between message parts for natural pacing.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_check_spam_or_voicemail`


**Title:** Check Spam or Voicemail [C]

**Description:**

```md
This setting controls whether the Agent actively classifies ongoing voice conversations as spam or
voicemail.

**Best Practice:** Enable this when you need automated call-handling safeguards and spam filtering
in voice channels.

Behavior by value:

- **Enabled (`True`):** Agent runs spam/voicemail classification and can trigger handling actions.
- **Disabled (`False`):** Inbound spam checks are skipped, while outbound voicemail checks may still
  run.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Voice transcription events invoke spam/voicemail classification. Classification
can return `True`, `False`, or `Skip` with specific skip reasons, such as a screening system or busy
announcement. On positive inbound detection, the Agent receives an urgent spam-handling instruction
before the call is stopped. On positive outbound detection, the Agent follows the voicemail guidance
already included in its outbound prompt, the `convoagent_voicemail_detected` event reports the
result, and the call is stopped after a fixed delay.

**Fallbacks:** Initialized to `False` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service`: This advanced system configuration
    determines which voice connector receives the stop-call command after detection.
- **Logic Interactions:**
  - `project_attributes_setting_spam_limit`: This advanced system configuration independently
    governs repeated sessions labeled as spam at session end; it does not control classification.
  - `outbound_session`: When this session attribute is `True`, detection can run even when this
    setting is `False`.
  - `voicemail_checked`: When this session attribute is `True`, repeated analysis is skipped.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_connect_with_the_manager_in_case_of_unhandled_issues`


**Title:** Conversation - Escalate Unresolved Issues To The Manager [C]

**Description:**

```md
This setting controls whether the Agent adds manager-escalation guidance when availability checks
cannot find suitable slots.

**Best Practice:** Enable this only if your transfer/escalation policy is configured and your team
expects manager handoff suggestions in no-availability situations.

Behavior by value:

- **Enabled (`True`):** Agent may include manager-assistance guidance in no-availability replies.
- **Disabled (`False`):** No manager-escalation guidance is added in those replies.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In formatted availability-response handling (including legacy/new response
processors and hospitality worker response path), when no slots are available, runtime can append an
extra escalation phrase that suggests manager assistance.

This is guidance logic only; it does not directly execute transfer actions by itself.

**Fallbacks:** Initialized to `True` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_enabled`: This advanced system configuration must be
    enabled for manager-connection guidance to be considered.
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: This advanced
    system configuration gates working-hours-aware escalation phrasing.
- **Logic Interactions:**
  - Working-hours status influences whether guidance suggests calling during business hours versus
    direct manager connection suggestion.
  - Applied primarily in no-availability result branches.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_conversation_session_timeout_finished_chat`


**Title:** Conversation - Session Timeout on Finished Chat [C] [IMPORTANT]

**Description:**

```md
This setting defines inactivity timeout (in seconds) for **finished chat** conversations. After this
timeout, session end is triggered automatically.

**Best Practice:** Keep this relatively short for chat to avoid stale context carrying over to later
messages, and keep it at `580` seconds or lower.

Behavior by value:

- **Lower timeout:** Session closes faster after conversation conclusion.
- **Higher timeout:** Session stays open longer before auto-end.

When timeout occurs:

- Agent loses visibility of previous conversation history.
- Agent sends report if session-ended reporting is enabled.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Session-extension runtime resolves timeout by conversation state and channel. If
conversation is concluded and channel is chat, this value is used to set the `session_timer` timer
(`eventIdn="end_session"`).

**Fallbacks:** Initialized to `60` during common setup. If empty at runtime, timer logic falls back
to `300`.

**Limits:** Keep this setting at `580` seconds or lower to stay aligned with current session-timeout
compatibility handling.

**Dependencies:**

- **Primary Settings:**
  - Conversation concluded state: This timeout applies only after conversation is marked concluded.
  - `project_attributes_setting_session_ended_report_enabled`: Controls whether report is sent when
    timeout ends the session.
- **Logic Interactions:**
  - If `extend_session` event is invoked with explicit `timeout` argument, that explicit value
    overrides this setting.
  - Voice/webcall channels use the finished-voice timeout setting instead.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_conversation_session_timeout_finished_voice`


**Title:** Conversation - Session Timeout on Finished Voice [C] [IMPORTANT]

**Description:**

```md
This setting defines inactivity timeout (in seconds) for **finished voice/webcall** conversations.
After this timeout, session end is triggered automatically.

**Best Practice:** Keep this long enough for natural post-call delays, and keep it at `580` seconds
or lower.

Behavior by value:

- **Lower timeout:** Session closes faster after call conclusion.
- **Higher timeout:** Session remains active longer before auto-end.

When timeout occurs:

- Agent loses visibility of previous conversation history.
- Agent sends report if session-ended reporting is enabled.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Session-extension runtime resolves timeout by conversation state and channel. If
conversation is concluded and channel is phone/webcall, this value is used to set the
`session_timer` timer (`eventIdn="end_session"`).

**Fallbacks:** Initialized to `60` during common setup. If empty at runtime, timer logic falls back
to `300`.

**Limits:** Keep this setting at `580` seconds or lower to stay aligned with current session-timeout
compatibility handling.

**Dependencies:**

- **Primary Settings:**
  - Conversation concluded state: This timeout applies only after conversation is marked concluded.
  - `project_attributes_setting_session_ended_report_enabled`: Controls whether report is sent when
    timeout ends the session.
- **Logic Interactions:**
  - If `extend_session` event is invoked with explicit `timeout` argument, that explicit value
    overrides this setting.
  - Chat channel uses the finished-chat timeout setting instead.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_conversation_session_timeout_unfinished_chat`


**Title:** Conversation - Session Timeout on Unfinished Chat [C] [IMPORTANT]

**Description:**

```md
This setting defines inactivity timeout (in seconds) for **unfinished chat** conversations. After
this timeout, session end is triggered automatically even when the conversation is not marked as
concluded.

**Best Practice:** Use a larger value than finished-chat timeout to give users enough time to resume
an active thread without losing context, but keep it at `580` seconds or lower.

Behavior by value:

- **Lower timeout:** Unfinished chat sessions close faster during inactivity.
- **Higher timeout:** Unfinished chat sessions remain open longer before auto-end.

When timeout occurs:

- Agent loses visibility of previous conversation history.
- Agent sends report if session-ended reporting is enabled.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Session-extension runtime resolves timeout by conversation state and channel. If
conversation is not concluded and channel is chat, this value is used to set the `session_timer`
timer (`eventIdn="end_session"`).

**Fallbacks:** Initialized to `580` during common setup. If empty at runtime, timer logic falls back
to `300`.

**Limits:** Keep this setting at `580` seconds or lower to stay aligned with current session-timeout
compatibility handling.

**Dependencies:**

- **Primary Settings:**
  - Conversation concluded state: This timeout applies only when conversation is still unfinished.
  - `project_attributes_setting_session_ended_report_enabled`: Controls whether report is sent when
    timeout ends the session.
- **Logic Interactions:**
  - If `extend_session` event is invoked with explicit `timeout` argument, that explicit value
    overrides this setting.
  - Voice/webcall channels use the unfinished-voice timeout setting instead.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_conversation_session_timeout_unfinished_voice`


**Title:** Conversation - Session Timeout on Unfinished Voice [C] [IMPORTANT]

**Description:**

```md
This setting defines inactivity timeout (in seconds) for **unfinished voice/webcall** conversations.
After this timeout, session end is triggered automatically even when the conversation is not marked
as concluded.

**Best Practice:** Set this high enough to cover realistic pauses in live calls, but keep it at
`580` seconds or lower.

Behavior by value:

- **Lower timeout:** Unfinished voice sessions close faster during inactivity.
- **Higher timeout:** Unfinished voice sessions remain active longer before auto-end.

When timeout occurs:

- Agent loses visibility of previous conversation history.
- Agent sends report if session-ended reporting is enabled.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Session-extension runtime resolves timeout by conversation state and channel. If
conversation is not concluded and channel is phone/webcall, this value is used to set the
`session_timer` timer (`eventIdn="end_session"`).

**Fallbacks:** Initialized to `300` during common setup. If empty at runtime, timer logic falls back
to `300`.

**Limits:** Keep this setting at `580` seconds or lower to stay aligned with current session-timeout
compatibility handling.

**Dependencies:**

- **Primary Settings:**
  - Conversation concluded state: This timeout applies only when conversation is still unfinished.
  - `project_attributes_setting_session_ended_report_enabled`: Controls whether report is sent when
    timeout ends the session.
- **Logic Interactions:**
  - If `extend_session` event is invoked with explicit `timeout` argument, that explicit value
    overrides this setting.
  - Chat channel uses the unfinished-chat timeout setting instead.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_conversation_sources_map`


**Title:** Conversation - Sources Map [C]

**Description:**

````md
This setting maps connector IDs to normalized source labels used in conversational context. It helps
the Agent adapt behavior based on where the conversation originated.

**Best Practice:** Use short, stable labels (for example `facebook`, `website_chat`, `tiktok`) and
keep mapping keys aligned with actual connector IDs.

Once mapped, `conversation.source` is added to conversation meta so your instructions can branch by
source. For example:

```text
### **Step X.X:** Decide how to proceed, based on `conversation.source`:
- If conversation.source is "facebook", tell the user that a manager will reach out to them via Facebook Messenger shortly.
- If conversation.source is "website_chat", ask the user to provide their phone number for follow-up.
```

Example mapping:

```json
{
  "manychat_facebook_connector": "facebook",
  "manychat_tiktok_connector": "tiktok",
  "website_chat": "website"
}
```

To obtain connector IDNs, use the Integrations page.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime first checks persona `conversation_source` and immediately reuses it when
a non-empty value is already cached. If no cached value exists, runtime reads current `connectorIdn`
from triggered activity, looks up mapped value in this JSON, stores the result in persona
`conversation_source`, and returns it. If no mapping exists for connector (or map is empty), runtime
falls back to conversation channel label.

**Fallbacks:** Initialized to `{}` during common setup. Empty map means source defaults to channel
value.

**Dependencies:**

- **Primary Settings:**
  - Connector IDs used as mapping keys must match the IDs of active integrations.
- **Logic Interactions:**
  - Resolved source is cached in persona state and reused in later prompt/meta generation.
  - Cached `conversation_source` is also included in end-session custom values for downstream
    reporting/integration consumers.
  - Source-specific instructions can branch on `conversation.source` in your prompt logic.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_data_injection_is_enabled`


**Title:** Data Injection [C]

**Description:**

```md
This setting controls whether the Agent periodically fetches external data and injects it into
runtime context.

**Best Practice:** Enable this only after webhook endpoint, payload configuration, and update period
are set and validated.

Behavior by value:

- **Enabled (`True`):** Agent fetches external data and can include it in additional business
  context.
- **Disabled (`False`):** Data-injection fetch loop is stopped and injected external context is
  cleared.

Setup overview:

1. Go to `Integrations`.
2. Open API `webhook` connector settings.
3. Configure webhook URL and required request handling.
4. Confirm payload/update settings for periodic fetch.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When enabled, runtime can trigger `data_injection` webhook requests and schedule
repeated fetches via `data_injection_timer`. Retrieved data is then available for
`<AdditionalBusinessContext>` injection. When disabled, runtime stops this path and resets internal
injected-data/timer state markers.

**Fallbacks:** Initialized to `False` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_data_injection_update_period`: Defines interval for repeated fetch
    scheduling.
  - `project_attributes_setting_data_injection_needs_summary`: Controls whether fetched data is
    summarized before being stored/injected.
  - `project_attributes_static_additional_business_context`: Can coexist with injected data in the
    same additional-context block.
- **Logic Interactions:**
  - If enabled but fetched data is empty, external injected context is omitted until data appears.
  - If disabled, static additional business context can still be injected independently.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_data_injection_max_summary_tokens`


**Title:** Data Injection - Max Summary Tokens [C]

**Description:**

```md
This setting defines the token cap used when summarizing fetched external data.

**Best Practice:** Use the smallest value that still preserves critical facts from your external
source data.

Behavior by value:

- **Lower value:** Stronger compression, lower token usage, higher risk of losing detail.
- **Higher value:** Richer summary/detail retention, higher token usage.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Applied in data summarization runtime as token limit for generated summary output.
The summarization instruction aims to keep original content when short enough and summarize when it
exceeds this threshold.

**Fallbacks:** Initialized to `1000` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_data_injection_needs_summary`: This limit is applied only when
    summary mode is enabled.
  - `project_attributes_setting_data_injection_is_enabled`: Summarization is relevant only when
    data-injection flow is active and external data is retrieved.
- **Logic Interactions:**
  - Very low limits can degrade downstream decision quality by over-compressing context.
  - High limits may reduce summarization benefit and increase token cost.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_data_injection_needs_summary`


**Title:** Data Injection - Needs Summary [C]

**Description:**

```md
This setting controls whether fetched external data is summarized before context injection.

**Best Practice:** Enable this for large/noisy external payloads to keep runtime context concise.

Behavior by value:

- **Enabled (`True`):** Retrieved data is summarized before storage/injection.
- **Disabled (`False`):** Retrieved data is stored/injected as received.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** On data retrieval, runtime checks this flag; when enabled, it runs summarization
before saving injected data context. When disabled, raw retrieved content is saved directly.

**Fallbacks:** Initialized to `False` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_data_injection_max_summary_tokens`: Defines summary size limit when
    this setting is enabled.
  - `project_attributes_setting_data_injection_is_enabled`: Data retrieval/injection must be active
    for this setting to have effect.
- **Logic Interactions:**
  - Applied only when external data payload is non-empty.
  - Summarization changes what is injected into additional business context for downstream
    reasoning.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_data_injection_update_period`


**Title:** Data Injection - Update Period [C]

**Description:**

```md
This setting defines how often external data is refreshed (in seconds) for data injection. It
controls the interval between automatic fetch cycles.

**Best Practice:** Start with a moderate interval and reduce only when your external data changes
frequently and requires near-real-time updates.

Behavior by value:

- **Lower interval:** More frequent refreshes, higher external-request load.
- **Higher interval:** Less frequent refreshes, lower external-request load.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** After each fetch cycle, runtime schedules the next `data_injection_timer` interval
using this value. Fetch cycles can continue automatically via timer events.

**Fallbacks:** Initialized to `14400` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_data_injection_is_enabled`: Refresh scheduling is relevant only when
    data injection is enabled.
- **Logic Interactions:**
  - Interval changes are applied when the next timer cycle is scheduled.
  - Very short intervals can increase webhook/API traffic and operational cost.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_define_conversation_is_during_working_hours_enabled`


**Title:** Conversation - Define Working Hours Status [C]

**Description:**

```md
This setting controls whether the Agent uses working-hours status in live conversation decision
paths.

**Best Practice:** Keep this enabled if your call-transfer, escalation, or availability policies
depend on open/closed business state.

Behavior by value:

- **Enabled (`True`):** Agent computes and reuses open/closed status (`business.currently_open`) for
  conversation-time instructions and branching.
- **Disabled (`False`):** Conversation-time logic stops gating these branches by open/closed status
  and uses non-status-specific fallback behavior.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In conversation runtime, working-hours status is evaluated and reused for
transfer-call rules, availability fallback guidance, manager-escalation phrasing, and related
explicit constraints.

When schedule structures are unavailable, runtime can fall back to model-based status inference.

**Fallbacks:** Initialized to `True` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_business_working_hours`: Main schedule source used to derive working-hours status.
  - `project_business_time_zone`: Time-zone basis for current-time status evaluation.
  - `project_attributes_setting_transfer_call_enabled`: Transfer behavior can depend on computed
    working-hours status.
- **Logic Interactions:**
  - Status is cached in conversation persona state and reused across flow decisions.
  - If disabled, conversation-time logic paths no longer gate behavior by open/closed status.
  - End-session/reporting paths can still derive working-hours status independently for reporting
    and analytics logic.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_outbound_tasks_working_hours_status`


**Title:** Outbound Tasks - Working Hours Enforcement - Enabled [C]

**Description:**

```md
This setting controls whether outbound call and outbound SMS tasks may be handed off only during
business working hours.

**Best Practice:** Enable this if your team wants TaskManager to delay outbound contact attempts
until the next open business window instead of dispatching them immediately.

Behavior by value:

- **Enabled (`True`):** TaskManager checks the effective execution moment for outbound `make_call`
  and `send_sms` tasks. If `asap`, `execute_in`, or `execute_at` resolve outside business hours, it
  rewrites the task to the next available working-hours slot before sending it to workers.
- **Disabled (`False`):** TaskManager keeps existing outbound timing unchanged, even if the task is
  scheduled outside business hours.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This flag is evaluated in TaskManager when `external_request`,
`task_manager_schedule_tasks`, or a prebuilt `task_manager_execute_task` request is received for
outbound task types. Runtime first resolves the base execution moment from `execute_in`,
`execute_at`, or immediate `asap` delivery. If this setting is enabled and the resulting outbound
execution moment falls outside business hours, TaskManager replaces it with the next future open
slot derived from the business schedule and then schedules the worker handoff for that rewritten
time.

The gate applies before TaskManager emits the internal `task_manager_dispatch_task` worker handoff.
After a task is handed off, worker-side queues, retries, and follow-up timers continue with their
own logic and are not re-checked by this setting.

**Fallbacks:** Initialized to `False` during common setup. If business time zone or structured
working-hours data is unavailable at runtime, TaskManager leaves outbound timing unchanged.

**Dependencies:**

- **Primary Settings:**
  - `project_business_working_hours`: Source schedule used to determine whether outbound execution
    falls inside or outside business hours.
  - `project_business_time_zone`: Time-zone basis used to evaluate the current time, `execute_at`,
    and derived future execution moments against the business schedule.
- **Logic Interactions:**
  - Applies only to outbound `make_call` and `send_sms` tasks; non-outbound tasks keep their normal
    execution timing.
  - When enabled, `execute_in` can be converted into a later `execute_at` if the calculated target
    lands outside business hours.
  - When enabled, `execute_at` is preserved if it already lands inside business hours and rewritten
    only when it falls outside the allowed schedule.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_caller_id_pool`


**Title:** Voice/SMS - Caller ID Pool [C]

**Description:**

````md
Defines a shared caller-ID pool that voice and SMS runtime can use when a channel needs to choose a
region-specific public number and connector instead of always falling back to one default number.

Use this when you want phone and SMS interactions to route through the intended regional phone
number for a user's country and local prefix, or to stay on the same phone number the user already
called or is currently talking to.

**Note:** Purchasing phone numbers through this attribute is currently supported only with Twilio.
Purchasing numbers from any other provider is temporarily unavailable because that provisioning path
has not yet been implemented.

**How to use:**

- Do not create the `Default` item manually. Publish/setup keeps it in sync with the base line
  automatically.
- Create one item per region or phone-number group you want to serve from a dedicated pooled number.
- `country_code` should be the dialing country code without `+`. Example: `1` for the US/Canada,
  `44` for the UK.
- `area_codes` should list the user prefixes that must route to this pooled connector. Runtime
  matches only `country_code + area_code`, so if a user number should match `817`, then `817` must
  be present in `area_codes`.
- `connector_suffix` is just a short technical suffix used to build the pooled connector names. Use
  something simple like `tx`, `quo`, `ldn`.
- `label` is only a human-friendly note so your team can recognize the entry later.
- `fallback_area_code` is used only while buying a phone number as a backup area code when the
  primary area code is unavailable. It does not add an extra runtime routing prefix by itself.

**If you are missing some information:**

- If you do not know `connector_suffix`, you can leave it empty and setup will derive it from the
  first `area_codes` item, or from `fallback_area_code` if there are no area codes.
- If you do not know `country_alpha2_code`, you can usually leave it empty. Setup will use the
  project's main voice phone country for provisioning.
- If you do not already have a pooled `phone_number`, you can leave it empty. Setup can buy and link
  a number automatically.
- If a pool item already contains `phone_number`, treat it as saved setup output, not as a manual
  relinking field. Setup can keep or rewrite it when a real linked pooled number is available.

If provisioning should happen in a country different from the project's main AI phone region, add
optional `country_alpha2_code` (for example `US`, `GB`, `NL`). If omitted, publish/setup uses
`project_representative_agent_voice_phone_alpha2_code` as the provisioning country.

If you omit `connector_suffix`, publish/setup derives it automatically from the first item in
`area_codes`, or from `fallback_area_code` when no area codes are present. If all three are empty,
that pool item is skipped and no connectors are created for it.

`phone_number` is not a manual routing key. During publish/setup the system rewrites it with the
actually linked pooled phone number when one is available. If a pool item contains a raw
`phone_number` string but the platform does not know the corresponding `phoneNumberId`, setup does
not relink that number from the attribute alone.

**Examples:**

```json
[
  {
    "label": "Texas",
    "connector_suffix": "tx",
    "country_code": "1",
    "area_codes": ["214", "469", "972"],
    "fallback_area_code": "817"
  }
]
```

```json
[
  {
    "label": "London",
    "connector_suffix": "ldn",
    "country_code": "44",
    "country_alpha2_code": "GB",
    "area_codes": ["20"],
    "phone_number": "+442079460958"
  }
]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Publish/setup reads this pool and, when it is non-empty, creates missing pooled
connectors, buys/links phone numbers, and normalizes the stored pool entries. Provisioning uses
`country_alpha2_code` when it is present; otherwise it falls back to
`project_representative_agent_voice_phone_alpha2_code`. While buying a number, setup can pass both
the primary `area_codes[0]` and optional `fallback_area_code` to the provider. Runtime keeps the
base connectors (`newo_voice_connector`, `sms_connector`, or `newo_sms_connector`) as the default
path. During an active voice/SMS session, follow-up SMS first tries to stay on the connector that
already owns the live public number. If there is no active session-specific match, runtime
normalizes the destination phone number, evaluates each configured `country_code + area_code`
combination from `area_codes`, and selects the longest matching override. `fallback_area_code`,
`label`, and the saved `phone_number` are not routing keys. For suffix-based entries, runtime
derives connector IDs automatically:

- Voice: `newo_voice_connector_<connector_suffix>`
- SMS: `<base sms connector idn>_<connector_suffix>`

The stored `phone_number` field is best treated as normalized setup output, not as the source of
truth for relinking an existing platform phone number.

**Fallbacks:** If this attribute is empty, malformed, or contains no usable entries, runtime keeps
using the built-in default connectors only.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_sms_provider`: Selects the base SMS provider used during caller-ID
    pool provisioning. Then the concrete per-route SMS integration/connector binding is stored in
    `project_attributes_private_dynamic_caller_id_routing`, and runtime SMS delivery / actor
    creation uses that stored binding rather than recomputing it from this setting alone.
  - `project_representative_agent_voice_phone_country_code`: Default dialing country code used by
    runtime matching when a pool item omits `country_code`.
  - `project_representative_agent_voice_phone_alpha2_code`: Default provisioning country used when a
    pool item omits `country_alpha2_code`.
- **Logic Interactions:**
  - Pooled voice connectors inherit the same voice prompt/settings sync that normally targets
    `newo_voice_connector`. Synchronization includes the default phone and web connectors plus every
    distinct pooled connector, without a fixed limit on the number of pool entries. The connector
    suffix comes from `connector_suffix`, the first non-empty `area_codes` value, or
    `fallback_area_code`, in that order. Missing connectors are skipped.
  - Conversation/event wiring accepts additional `newo_voice`, `twilio_messenger`, and `newo_sms`
    connectors so replies on pooled numbers continue through the standard ConvoAgent flows.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_email_sender_name`


**Title:** Email - Sender Name [A]

**Description:**

```md
This setting defines the sender display name shown on outgoing emails.

**Best Practice:** Use a clear business-aligned sender name so users can easily recognize automated
messages.

Example values:

- `Your Company Name | DoNotReply`
- `Appointments Team | DoNotReply`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Email delivery runtime reads this value and passes it as `senderName` in outgoing
email requests.

**Fallbacks:** Common setup initializes this field from business name using a DoNotReply postfix. If
empty at send time, runtime falls back to a generic sender name.

**Dependencies:**

- **Primary Settings:**
  - `project_business_name`: Used during initialization to construct default sender naming.
- **Logic Interactions:**
  - Affects email sender display only; it does not change recipient targeting or opt-out checks.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_email_signature_template`


**Title:** Email - Signature Template [B]

**Description:**

````md
This setting defines the signature block appended to the bottom of outgoing emails.

**Pro-Tip:** Use `[[attribute_idn]]` placeholders (for example the business name, or the Agent's
representative name and title) to keep the signature personalized automatically as those values
change, or write fixed plain text instead. Line breaks are preserved.

Example:

```txt
Best regards,
[[project_representative_agent_name]]
[[project_business_name]]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** At setup/publish, the platform compiles this template by substituting each
`[[attribute_idn]]` placeholder with the current value of that attribute, producing a ready-to-use
signature block stored separately. When the advanced system configuration
`project_attributes_private_feature_flag_email_universal_template` is enabled, outgoing emails read
that compiled block and render it in the signature area of the message footer. When that
configuration is disabled, outgoing emails use their own built-in structured signature (Agent name,
title, and business name) and do not read this setting at all.

**Fallbacks:** If left empty, the system fills in a generic default signature using the Agent's
representative name, title, and business name. If the compiled result is empty at send time, the
signature area of the message is simply left blank on the template-based delivery path.

**Dependencies:**

- **Logic Interactions:**
  - `project_attributes_private_feature_flag_email_universal_template`: Determines whether outgoing
    emails read the compiled result of this template as their signature, or fall back to a separate
    built-in structured signature instead.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `false`

---

## `project_attributes_setting_evaluate_ongoing_conversation_quality`


**Title:** Conversation - Evaluate Ongoing Conversation Quality [C]

**Description:**

```md
This setting controls whether the Agent continuously checks conversation quality during active
dialogue and applies recovery guidance when quality drops.

**Best Practice:** Enable this for production voice channels where background noise, poor
connection, or misunderstanding is common.

Behavior by value:

- **Enabled (`True`):** Agent evaluates quality and applies escalation guidance for low-quality
  conversations.
- **Disabled (`False`):** No quality-based escalation guidance is triggered.

When low quality is detected, runtime guidance follows this order:

- Attempt transfer if transfer is enabled and working-hours logic allows it.
- Otherwise, suggest callback or manager relay (if manager-relay mode is enabled).
- Otherwise, fall back to callback guidance.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime performs structured quality scoring on ongoing conversation history. If
the score is low, it emits `urgent_message` guidance and applies channel-aware escalation behavior.

**Fallbacks:** Initialized to `False` in common defaults. Low-quality escalation is suppressed after
the first successful trigger in the same conversation to avoid repeated interruptions.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_enabled`: Allows transfer-first handling when quality
    is poor and transfer is available.
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Working-hours
    evaluation influences whether transfer-first guidance can be used.
  - `project_attributes_setting_session_ended_report_enabled`: Enables manager-relay fallback when
    transfer is not available.
- **Logic Interactions:**
  - Phone channel can use transfer-first behavior; non-phone channels skip transfer and use fallback
    guidance.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_follow_up_timer_chat_interval_base`


**Title:** Conversation - Follow-Up Timer - Chat - Interval - Base [C]

**Description:**

```md
This setting defines the base chat follow-up delay (in seconds) after the Agent sends a reply. For
standard chat replies, it also affects how much extra delay is added for longer answers.

**Best Practice:** Start with `120` and tune based on user response behavior. Use `-1` when you want
attribute-driven chat follow-up scheduling disabled.

Behavior by value:

- **`-1`:** Attribute-driven chat interval logic returns disabled value and follow-up timer updates
  using that value are turned off.
- **`0` or positive number:** Follow-up timer is scheduled; larger values wait longer before
  follow-up and also increase the reply-length-based extension for standard chat replies.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In standard reply handling, runtime treats this as a base value and computes a
final delay from base interval plus response-length scaling before sending
`convoagent_update_followup`. Higher values therefore increase both the fixed base delay and the
extra delay added for longer chat replies. In chat tool-call follow-up updates, runtime uses this
value directly as the scheduling interval.

**Fallbacks:** Initialized to `120` in common defaults.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_follow_up_timer_voice_interval_user_speech_ended`: Voice/webcall
    channels use that advanced configuration instead of this chat base.
- **Logic Interactions:**
  - `convoagent_update_followup`: Receives the computed or direct interval and updates follow-up
    scheduling.
  - Some specialized flows can send explicit fixed intervals to `convoagent_update_followup`
    independently of this setting.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_follow_up_timer_voice_interval_agent_speech_ended`


**Title:** Conversation - Follow-Up Timer - Voice - Interval - Agent Speech Ended [C]

**Description:**

```md
This setting defines the voice follow-up delay (in seconds) after the Agent finishes speaking.

**Best Practice:** Keep this short enough to recover stalled calls quickly, but long enough to avoid
interrupting normal user pause time.

Behavior by value:

- **`-1`:** Disables this follow-up timer path.
- **`0` or positive number:** Schedules follow-up after agent speech ends; larger values wait
  longer.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime passes this value directly to `convoagent_update_followup` for
`agent_speech_ended` updates. Voice/webcall tool-call flows can also use this value when resetting
follow-up timing after tool execution.

**Fallbacks:** Initialized to `20` in common defaults.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_follow_up_timer_voice_interval_agent_speech_started`: Advanced
    voice-to-voice tool-call handling can use speech-started interval behavior in separate paths.
- **Logic Interactions:**
  - `project_attributes_setting_follow_up_timer_voice_interval_user_speech_ended`: Separate
    post-reply timing logic uses that base interval for dynamic voice delay calculations.
  - `convoagent_update_followup`: Scheduler event that applies this interval value.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_follow_up_timer_voice_interval_agent_speech_started`


**Title:** Conversation - Follow-Up Timer - Voice - Interval - Agent Speech Started [C]

**Description:**

```md
This setting defines the voice follow-up delay (in seconds) that starts when the Agent begins
speaking.

**Best Practice:** Keep this longer than your average opening phrase duration to avoid premature
follow-up prompts while the Agent is still actively guiding the conversation.

Behavior by value:

- **`-1`:** Disables this follow-up timer path.
- **`0` or positive number:** Schedules follow-up from agent-speech-started timing points.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime reads this value for `agent_speech_started` follow-up scheduling via
`convoagent_update_followup`. In advanced voice-to-voice tool-call handling, this interval is also
used when resetting follow-up after a tool call.

**Fallbacks:** Common setup initializes this to `70` when the attribute is empty. If this value is
empty at runtime, the follow-up scheduler applies a channel-specific default interval (`25` for
phone/webcall, `75` for non-voice channels).

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`:
    Advanced function-call follow-up reset paths use this interval when enabled.
- **Logic Interactions:**
  - `convoagent_update_followup`: Scheduler event that applies this interval.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_follow_up_timer_voice_interval_conversation_started_inbound`


**Title:** Conversation - Follow-Up Timer - Voice - Interval - Conversation Started - Inbound [C]

**Description:**

```md
This setting defines the voice follow-up delay (in seconds) right after an inbound conversation
starts.

This inbound timer is separate from the outbound timer so you can tune incoming-call silence
handling differently from proactive outreach calls.

**Best Practice:** Keep this short enough to recover quickly when the user goes silent at call
start, but long enough to avoid interrupting normal hello/opening pauses.

Behavior by value:

- **`-1`:** Disables this inbound conversation-started timer path.
- **`0` or positive number:** Schedules follow-up from inbound conversation-start events.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During conversation-start follow-up handling, runtime emits
`convoagent_update_followup` with `reason="conversation started"` using this value when the session
is not marked as outbound.

**Fallbacks:** Common setup initializes this to `12` when the attribute is empty. If this value is
empty at runtime, the follow-up scheduler applies a channel-specific default interval (`25` for
phone/webcall, `75` for non-voice channels).

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_mode`: This timer path is applied
    when advanced voice mode is `voice-to-voice` or `speech-to-speech`.
- **Logic Interactions:**
  - `convoagent_update_followup`: Scheduler event that applies the initial inbound follow-up delay.
  - `project_attributes_setting_follow_up_timer_voice_interval_conversation_started_outbound`: When
    session is marked outbound, start follow-up timing uses the outbound setting instead of this
    one.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_follow_up_timer_voice_interval_conversation_started_outbound`


**Title:** Conversation - Follow-Up Timer - Voice - Interval - Conversation Started - Outbound [C]

**Description:**

```md
This setting defines the voice follow-up delay (in seconds) right after an outbound conversation
starts.

This outbound timer is separate from the inbound timer so proactive outreach can use a different
start-of-call pacing strategy.

**Best Practice:** Keep this short for proactive outreach flows so stalled outbound calls recover
quickly after the opening message.

Behavior by value:

- **`-1`:** Disables this outbound conversation-started timer path.
- **`0` or positive number:** Schedules follow-up from outbound conversation-start events.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During outbound greeting/conversation-start follow-up handling, runtime emits
`convoagent_update_followup` with `reason="conversation started"` using this value when the session
is marked as outbound.

**Fallbacks:** Common setup initializes this to `12` when the attribute is empty. If this value is
empty at runtime, the follow-up scheduler applies a channel-specific default interval (`25` for
phone/webcall, `75` for non-voice channels).

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_mode`: In advanced `voice-to-voice`
    or `speech-to-speech` mode, conversation-start follow-up handling for outbound sessions reads
    this value.
  - `project_attributes_setting_follow_up_timer_voice_interval_conversation_started_inbound`:
    Companion advanced configuration for inbound conversation-start timing.
- **Logic Interactions:**
  - `convoagent_update_followup`: Scheduler event that applies the initial outbound follow-up delay.
  - `project_attributes_setting_follow_up_timer_voice_interval_conversation_started_inbound`: When
    session is not marked outbound, start follow-up timing uses the inbound setting instead of this
    one.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_follow_up_timer_voice_interval_user_speech_ended`


**Title:** Conversation - Follow-Up Timer - Voice - Interval - User Speech Ended [C]

**Description:**

```md
This setting defines the voice follow-up delay (in seconds) after the user finishes speaking.

**Best Practice:** Use this as your primary voice silence baseline. Shorter values make the Agent
more proactive; longer values reduce interruption risk.

Behavior by value:

- **`-1`:** Disables this timer path where disable semantics are honored.
- **`0` or positive number:** Schedules follow-up after user-speech-ended events.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime applies this value to `convoagent_update_followup` with
`reason="user_speech_ended"` when conversation state allows it. In voice/webcall dynamic interval
calculation, this value is also used as the base interval for reply-length scaling.

**Fallbacks:** Common setup initializes this to `20` when the attribute is empty. If this value is
empty at runtime, the follow-up scheduler applies a channel-specific default interval (`25` for
phone/webcall, `75` for non-voice channels).

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_follow_up_timer_chat_interval_base`: Non-voice channels use the chat
    base interval instead of this voice baseline.
- **Logic Interactions:**
  - `project_attributes_setting_follow_up_timer_voice_interval_user_speech_started`: User-started
    timer and interrupt-state handling can defer or skip this update path.
  - `convoagent_update_followup`: Scheduler event that applies this interval.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_follow_up_timer_voice_interval_user_speech_started`


**Title:** Conversation - Follow-Up Timer - Voice - Interval - User Speech Started [C]

**Description:**

```md
This setting defines the voice follow-up delay (in seconds) that starts when the user begins
speaking.

**Best Practice:** Keep this long enough to avoid reacting to short noise bursts or brief speech
fragments during active turn-taking.

Behavior by value:

- **`-1`:** Disables this timer path where disable semantics are honored.
- **`0` or positive number:** Schedules follow-up after user-speech-started events.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime applies this value to `convoagent_update_followup` with
`reason="user_speech_started"` in user-turn tracking paths. When the Agent is currently speaking,
runtime records interruption state and skips immediate timer scheduling.

**Fallbacks:** Common setup initializes this to `70` when the attribute is empty. If this value is
empty at runtime, the follow-up scheduler applies a channel-specific default interval (`25` for
phone/webcall, `75` for non-voice channels).

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_follow_up_timer_voice_interval_user_speech_ended`: Companion
    advanced configuration for post-user-turn silence handling.
- **Logic Interactions:**
  - Follow-up counter is reset when this path runs, so repeated silence prompting starts from the
    initial attempt.
  - `convoagent_update_followup`: Scheduler event that applies this interval.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_initial_thoughts`


**Title:** Conversation - Initial Thoughts [C]

**Description:**

````md
This setting defines the initial internal conversation context the Agent uses at the start of a new
session.

**Best Practice:** Keep this short and operational, focused on immediate next-step guidance rather
than business policy details.

**Examples:**

```txt
Just greeted the User. Next - understand inquiry and follow instructions.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** At new-session initialization, runtime copies this value into the Agent's
conversation-thought state. That state is then injected into prompt assembly where thought injection
is enabled and can be updated as the conversation evolves.

**Fallbacks:** Initialized in common defaults to a generic session-start thought.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_reset_persona_attributes`: This setting does not
    disable new-session thought seeding, but it changes how much persona/profile context is carried
    into the next session around that seeded thought.
- **Logic Interactions:**
  - The seeded thought is a starting point; runtime thought-generation logic may overwrite it in
    later turns.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_meeting_check_availability_working_hours_status`


**Title:** Appointment - Google Calendar Meeting - Working Hours Validation - Enabled [B]

**Description:**

```md
This setting controls whether the Agent validates requested Google meeting times against business
working hours before creating a meeting.

**Best Practice:** Keep this enabled to avoid creating meetings on non-working days or outside
working-hour windows.

Behavior by value:

- **Enabled (`True`):** Agent checks requested day/time and asks the user for a different slot if it
  falls outside working schedule.
- **Disabled (`False`):** Agent skips working-hours validation for meeting creation requests.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During Google meeting scheduling, runtime evaluates requested slot status and
blocks creation for `non_working_day` or `non_working_hours`, sending corrective guidance to collect
another time.

**Fallbacks:** Initialized to `True` in common defaults.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_calendar_event_integration`: This setting is relevant when calendar
    integration is configured for Google meeting creation.
  - `project_business_working_hours`: Source schedule used for working-hours validation.
  - `project_business_time_zone`: Time-zone basis for day/time interpretation.
- **Logic Interactions:**
  - If compiled schedule data is unavailable, runtime can use model-based fallback status
    evaluation.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_meeting_duration`


**Title:** Appointment - Google Calendar Meeting - Duration [B]

**Description:**

```md
This setting defines the meeting duration (in minutes) for Agent-created Google calendar events.

**Best Practice:** Use a duration that matches your real appointment format (for example, 30, 45, or
60 minutes) and keep it consistent with user-facing scheduling promises.

Behavior by value:

- **Positive number:** Used as event duration for created meetings.
- **`0` or negative values:** Passed through as configured and may produce invalid or unexpected
  calendar behavior depending on integration-side validation.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime reads this value and passes it as `eventDurationMinutes` in calendar
`create_event` requests used for Google meeting creation, including both normal conversation-driven
meeting setup and external task-driven meeting execution.

**Fallbacks:** Initialized to `60` in common defaults.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_calendar_event_integration`: Enables the primary conversation
    meeting-creation path where this duration is applied to Google calendar events.
- **Logic Interactions:**
  - `project_attributes_setting_test_mode`: In test mode, the live calendar command is skipped in
    conversation-driven meeting setup, and a mocked success event is emitted while preserving the
    configured duration in the generated meeting payload context.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_meeting_setup_phrase`


**Title:** Appointment - Google Calendar Meeting - Setup Phrase [B]

**Description:**

````md
This setting defines an additional phrase pattern the Agent can use to confirm it is about to create
a meeting.

**Best Practice:** Keep this phrase short and explicit (for example, "I will set up an appointment
request.") so meeting-tool triggering remains reliable.

**Examples:**

```txt
I will set up an appointment request.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime incorporates this text into `create_meeting_tool` promise-detection rules.
If populated, the phrase is treated as an accepted variant for recognizing that the Agent has
committed to immediate meeting creation.

**Fallbacks:** Initialized in common defaults to a generic meeting-setup phrase. If empty, runtime
uses built-in default phrase examples for tool detection.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_calendar_event_integration`: `create_meeting_tool` registration and
    this phrase extension are applied when Google calendar integration is active.
- **Logic Interactions:**
  - This setting affects meeting-tool trigger matching only; it does not alter the final meeting
    payload fields.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_settings_platform_tools`


**Title:** Conversation - Tools [C]

**Description:**

````md
This attribute specifies the `tools` that are available for the Agent to use during the
conversation. You can either override existing tools or add new ones.

**Best Practice:** Start with one narrowly scoped tool, validate its trigger behavior, and only then
add more tools or conflict groups.

**Examples:**

- Override an existing built-in tool by reusing the same tool key under `tools`.
- Add a new tool key to extend Agent behavior for a custom webhook or event workflow.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime merges built-in tools with this attribute’s JSON (`tools` object). If a
custom tool key matches a built-in tool key, the custom definition overrides the built-in one.
`conditions` and `useConversationHistory` are required per tool. `action` is optional; if omitted,
runtime defaults to `send_event`. For `send_webhook`, `after_actions` execute in order only when the
webhook returns a non-empty response body. Top-level webhook schema properties marked with
`runtime_value` are populated directly from runtime context instead of conversation content.

**Fallbacks:** If this attribute is empty, runtime uses built-in tools only. Common defaults
initialize this attribute either as blank (`" "`) or with industry-provided starter JSON.

**Dependencies:**

- **Primary Settings:**
  - Built-in tool availability can still depend on other feature settings (for example booking,
    meeting, SMS, email, and transfer-related settings), even when custom tools are configured here.
- **Logic Interactions:**
  - `generalmanageragent_update_platform_tools`: Runtime modules can append or override tools
    through this update event.
  - `conflictPolicy.tag`: If multiple selected tools share the same tag, runtime reranks and
    executes only one tool per tag.

**Detailed Configuration Reference:**

**Important:** This feature is under development. Use with caution, and expect interface changes in
future releases.

In addition, each tool may define a `conflictPolicy` to resolve collisions when multiple tools are
selected for execution at the same time.

**The following actions are supported:**

# Actions

## 1) `send_event`

Fire a named system event. **After actions:** _Not supported_ for this action.

**Options**

- `type`: `"send_event"` (not required, `type` defaults to it)

> Use when you just need to notify the system and handle the event completely on your own.

---

## 2) `send_webhook`

Make an HTTP request to an external endpoint. **After actions:** _Supported_ (you may chain one or
more after actions below, in order). After actions run only when the webhook returns a non-empty
response body.

**Options**

- `type`: `"send_webhook"` (required)
- `options.method`: HTTP method. One of `"GET" | "POST" | "PUT" | "PATCH" | "DELETE"`. Default:
  `"GET"`.
- `options.url`: Target URL. **Required.**
- `options.query`: Fields to place in the URL query string. _(Object schema describing fields to
  fill.)_
- `options.headers`: HTTP headers to send. _(Object schema describing fields to fill.)_
- `options.body`: JSON body to send. _(Object schema describing fields to fill.)_
- `runtime_value`: Optional keyword on a top-level property in `options.query`, `options.headers`,
  or `options.body`. The supported values are `session_id` and `customer_idn`. The property name
  remains the name sent in the query, header, or body.

> Tip: Provide only the fields you actually need in `query`, `headers`, and `body`.

Runtime-sourced properties are not generated from the conversation. For example, this schema sends
the current session identifier as `session_id` and the current Customer identifier as
`customer_idn`:

```json
{
  "type": "object",
  "properties": {
    "session_id": {
      "type": "string",
      "runtime_value": "session_id"
    },
    "customer_idn": {
      "type": "string",
      "runtime_value": "customer_idn"
    }
  },
  "required": ["session_id", "customer_idn"]
}
```

---

# After actions

## A) `send_urgent_message`

### Supported actions: [`send_webhook`]

Immediately sends a high-priority message to the user.

**Options**

- `prefix` _(string, optional)_: Text placed on a line above the message content.
- `uninterruptible` _(boolean, optional)_: Controls whether the urgent message is interruptible.
  Default is `true`. Set `false` to allow interruption.
- `call_analyze_conversation_skill` _(boolean, optional)_: Request follow-up analysis. Default:
  `false`.
- `call_manage_task_skill` _(boolean, optional)_: Request task handling. Default: `false`.

---

## B) `set_persona_attribute`

### Supported actions: [`send_webhook`]

Writes a value into the user’s persona/profile.

**Options**

- `attribute_name` _(string, required)_: The profile field to set.
- `llm_process_instruction` _(string, optional)_: A short instruction telling the AI how to
  transform the latest input into the value to store (e.g., “If data is successfully collected,
  generate True, else False.”). If empty, input is used as-is with no post-processing.

---

## C) `set_prompt_section`

### Supported actions: [`send_webhook`]

Stores text into a named custom section of the user’s prompt (for future turns).

**Options**

- `section_name` _(string, required)_: The prompt section to write to. Example: "section_name":
  "FullNameValidationProcess".
- `llm_process_instruction` _(string, optional)_: A short instruction telling the AI how to
  transform the latest input into the section value (e.g., “If validated, output the full name;
  otherwise output ‘False’.”). If empty, input is used as-is with no post-processing.

---

# Conflict resolution

## `conflictPolicy`

`conflictPolicy` is an optional object on the tool definition level. It can be omitted or empty (no
effect), or it can contain a single tag key:

- `conflictPolicy.tag` _(string, required)_: A grouping key used to prevent multiple tools from the
  same group from executing in the same selection.

If more than one tool with the same `conflictPolicy.tag` is selected for execution, they will be
reranked by the LLM and **only ONE tool for that tag will be executed**. This is guaranteed.

---

# Notes

- **Conditions**: You decide when a tool triggers by defining booleans like `emailProvided`,
  `phoneNumberProvided`, etc.
- **useConversationHistory (required)**: `true/false` - whether the tool can use prior conversation
  context to auto-fill fields. When `false`, only the latest Agent message is considered.
- **Order of after actions** matters: they run top to bottom.
- **Conflict resolution**: Use `conflictPolicy.tag` to ensure only one tool from a mutually
  exclusive group (e.g., multiple SMS-related tools) can execute at a time.
- **Cross-module updates**: Runtime modules can update this attribute by emitting
  `generalmanageragent_update_platform_tools`.

Example of overriding existing tool - `calculation_tool` and adding new `report_phone_number_tool`:

```json
{
  "tools": {
    "report_phone_number_tool": {
      "conditions": {
        "phoneNumberProvided": {
          "type": "boolean",
          "description": "The user just provided their phone number"
        }
      },
      "action": {
        "type": "send_webhook",
        "options": {
          "method": "GET",
          "query": {
            "type": "object",
            "properties": {
              "phone_number": {
                "type": "string",
                "description": "User's provided phone number"
              }
            }
          },
          "headers": {
            "type": "object",
            "properties": {
              "Content-Type": {
                "type": "string",
                "enum": ["application/json"]
              }
            }
          },
          "url": "https://hook.us1.make.com/somewebhookup"
        }
      },
      "after_actions": [
        {
          "type": "send_urgent_message"
        }
      ],
      "useConversationHistory": true
    },
    "calculation_tool": {
      "description": "The agent calculates the price and informs the user about it.",
      "conditions": {
        "agentPromised": {
          "type": "boolean",
          "description": "The agent clearly states that they are going to calculate the price right now. So their <LatestConvoAgentAnswer> should contain something like: \"I will calculate the price for you...\", \"Let me calculate the estimate...\", \"Give me a moment, I will calculate...\", etc. Statements of capability (e.g., \"I can calculate\", \"I could estimate\") or conditional offers are NOT firm intentions and must be ignored."
        }
      },
      "useConversationHistory": false
    }
  }
}
```

Example of adding new tool - `custom_tool`:

```json
{
  "tools": {
    "custom_tool": {
      "conditions": {
        "userAskedForCustomTool": {
          "type": "boolean",
          "description": "The agent promised to use a custom tool in their last message (enclosed in <LatestConvoAgentAnswer>) and use previously provided data in the conversation (enclosed in <Conversation>)."
        }
      },
      "useConversationHistory": true
    }
  }
}
```

Example of using `conflictPolicy` to avoid executing multiple tools from the same group:

```json
{
  "tools": {
    "send_sms_tool": {
      "description": "This tool sends an SMS to the User",
      "conflictPolicy": {
        "tag": "sms"
      },
      "conditions": {
        "agentPromised": {
          "type": "boolean",
          "description": "The agent clearly states that they are going to send an SMS. So their <LatestConvoAgentAnswer> should contain the explicit keywords \"SMS\" or \"text message\", e.g.: \"I will send you an SMS / text message shortly...\", \"Give me a moment, I will send you an SMS / text message...\", \"I will send an SMS / text message with the appointment request details.\", \"I'm sending a text message / SMS...\", \"Let me try sending it (considering SMS or text message) again...\", \"I will resend an SMS / text message...\", etc."
        }
      },
      "useConversationHistory": false
    },
    "send_manage_booking_url_tool": {
      "description": "This tool sends an SMS URL to the user with the link to manage their previously made booking.",
      "conflictPolicy": {
        "tag": "sms"
      },
      "conditions": {
        "agentPromised": {
          "type": "boolean",
          "description": "The agent clearly states that they are going to send a link for the user to manage their booking."
        },
        "bookingExist": {
          "type": "boolean",
          "description": "During the conversation the agent actually checked existing user's bookings and found the exact one, so the exact booking to send url for is known"
        }
      },
      "useConversationHistory": true
    }
  }
}
```

In the example above, both tools share the same `conflictPolicy.tag` (`"sms"`). If both tools are
selected for execution, they will be reranked and **only one** of them will be executed.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_products_and_services_background_check_location_enabled`


**Title:** Products & Services - Check Location In the Background [B]

**Description:**

```md
This setting controls whether the Agent uses a background tool to double-check whether a user ZIP
code is served.

**Best Practice:** Enable this when service-area coverage is large/complex or when inline ZIP checks
cause response-quality issues.

Behavior by value:

- **Enabled (`True`):** Runtime can register and use background ZIP verification tooling.
- **Disabled (`False`):** ZIP coverage is handled by standard prompt/context logic without that
  background tool path.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When enabled, runtime adds `check_zip_code_served_tool` to tool selection so ZIP
coverage can be validated asynchronously from the immediate assistant reply.

**Fallbacks:** Initialized to `False` in common defaults.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_products_and_services_served_zip_codes`: Main data source used for ZIP
    coverage validation.
- **Logic Interactions:**
  - `project_attributes_products_and_services_served_area`: Used in standard area-based reasoning
    when background ZIP-check mode is not active.
  - Multiple industry business-context builders include served ZIP coverage explicitly when this
    setting is `False`.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_products_and_services_background_check_availability_enabled`


**Title:** Products & Services - Check Availability In the Background [B]

**Description:**

```md
This setting controls whether the Agent uses a background tool to verify if a requested product or
service is actually offered.

**Best Practice:** Enable this when your catalog is broad or frequently updated and inline reasoning
alone is not reliable.

Behavior by value:

- **Enabled (`True`):** Runtime can register and use background product/service availability
  verification tooling.
- **Disabled (`False`):** Product/service availability is handled without this background tool path.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When enabled, runtime adds `check_product_or_service_availability` to tool
selection. This tool is intended for offering/coverage checks (using compiled catalog context), not
appointment-slot time availability.

**Fallbacks:** Initialized to `False` in common defaults.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_products_and_services`: Primary source for offered products/services used in
    availability decisions.
  - `project_attributes_products_and_services_not_offering`: Source for explicitly excluded
    products/services used when availability context is compiled.
- **Logic Interactions:**
  - `project_attributes_setting_products_and_services_structured_representation_enabled`: Controls
    how catalog data is compiled before background availability checks run.
  - `project_attributes_setting_booking_check_availability_enabled`: Slot-availability tooling can
    run in parallel domains; conflict policy uses shared `availability` grouping to avoid
    conflicting tool execution.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_products_and_services_structured_representation_enabled`


**Title:** Products & Services - Structured Representation [C]

**Description:**

```md
This setting controls whether Products and Services are compiled into a structured format before
runtime use.

**Best Practice:** Enable this when your catalog is large or complex and you need more reliable
service/product matching behavior.

Behavior by value:

- **Enabled (`True`):** Runtime builds structured JSON-style product/service representation.
- **Disabled (`False`):** Runtime keeps a non-structured text representation of
  offering/not-offering items.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During attribute-preparation cycles, runtime compiles products/services data
according to this mode and reuses the compiled result across prompt/context assembly and
product/service validation paths.

**Fallbacks:** Initialized to `False` in common defaults. If both source product/service fields are
empty, compiled output is cleared. If source values and mode are unchanged, recompilation is
skipped.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_products_and_services`: Main source for offered products/services.
  - `project_attributes_products_and_services_not_offering`: Main source for explicitly excluded
    products/services.
- **Logic Interactions:**
  - Compiled representation quality affects downstream service-offering checks and related prompt
    guidance.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_test_mode`


**Title:** Testing - Test Mode [C] [IMPORTANT]

**Description:**

```md
This setting switches booking/meeting scheduling flows into test behavior to reduce external side
effects.

**Best Practice:** Keep this `False` in production. Enable only for controlled validation of booking
and calendar logic. If you regularly test from fixed caller numbers, configure the dedicated test
phone-number list instead of toggling this globally.

Behavior by value:

- **Enabled (`True`):** Runtime suppresses selected external scheduling actions and uses simulated
  success paths/events.
- **Disabled (`False`):** Runtime sends real scheduling/task actions according to configured booking
  and calendar integrations unless the session phone number is listed in the advanced test-number
  override.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In scheduling flows, `test_mode=True` suppresses selected outbound actions such as
`book_restaurant_slot` and `create_event`, and injects mock success events like `result_success` and
`create_event_success_mock`. Task-routing logic also switches to simulated worker-message behavior.
Email and SMS worker flows also divert to mock events instead of sending live notifications, and
call-transfer execution is replaced with the end-conversation path. The first resolved result is
stored on the user persona as canonical `session_test_mode` (`True` or `False`) and remains fixed
until session cleanup. An integration can set that persona attribute before the checker runs; a
canonical externally supplied value takes precedence over this setting. Session-ended events expose
the operational status as `sessionTestMode`, and queued email/SMS work receives a snapshot so
cleanup cannot change its behavior.

**Fallbacks:** Initialized to `False` in common defaults. While a phone session has no
`last_convo_actor_id`, phone-number resolution remains uncached and is retried by later checks.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_type`: Determines which booking execution path is bypassed
    or simulated in test mode.
  - `project_attributes_setting_calendar_event_integration`: Google meeting creation uses mock
    success flow instead of real calendar command in test mode.
  - `project_attributes_setting_test_mode_phone_numbers`: Forces test-mode behavior for sessions
    whose active phone-call actor uses Voice Connector (phone) and whose `externalId` matches a
    configured test number.
  - `project_attributes_setting_test_mode_phone_numbers_static`: Adds project-scoped phone-number
    overrides that are merged with the customer list before session test-mode matching.
- **Logic Interactions:**
  - Booking result handlers include test-mode parsing for mocked booking responses.
  - Conversation-side status/persona updates still run, so test sessions can resemble real
    end-to-end flow behavior.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_test_mode_phone_numbers`


**Title:** Testing - Test Mode Phone Numbers [C] [IMPORTANT]

**Description:**

````md
Account-scoped JSON list of phone-call numbers that should always run in test mode, even when the
main test-mode switch is turned off.

**Best Practice:** Use this for account-specific QA or demo phone numbers. Keep each number in full
international format with country code so matching stays predictable.

**Examples:**

```json
["+15550001111", "+15550002222"]
```

Accepted number format per item:

- With plus: `+15550001111`
- Without plus: `15550001111`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime checks this list alongside `project_attributes_setting_test_mode` and the
project-scoped `project_attributes_setting_test_mode_phone_numbers_static` list. During the session
test-mode check, both arrays are merged and deduplicated after phone normalization that trims
whitespace and removes a leading `+`. The override is evaluated only for standard phone-call
sessions where the active conversation actor uses Voice Connector (phone). In that case, runtime
compares the actor `externalId` against the merged number list; on match, the session is treated as
test mode and follows the same mocked scheduling, messaging, and transfer-safe behavior as when the
main test-mode switch is enabled globally. Chat, SMS, webcall, and other non-phone session types do
not use this override. Once `last_convo_actor_id` is available, either match result is stored as
canonical `session_test_mode` and remains unchanged until session cleanup. If the actor is not yet
available, the checker returns non-test behavior without caching and retries later. Integrations can
mark non-phone sessions explicitly by setting `session_test_mode`; Assessor does this for both chat
and phone sessions.

**Fallbacks:** Defaults to `[]`. Empty list means no phone-number-based override is active.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_test_mode`: Global test-mode switch; this attribute acts as a
    session-scoped override on top of it.
  - `project_attributes_setting_test_mode_phone_numbers_static`: Project-scoped list merged with
    this account-specific list before matching.
- **Logic Interactions:**
  - `project_attributes_setting_common_phone_numbers`: Uses similar phone-number formatting
    expectations, but common/shared-number handling and test-mode overrides are evaluated
    independently.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_timezone_reasoning_enabled`


**Title:** Conversation - Time Zone Reasoning - Enabled [C]

**Description:**

```md
This setting controls whether the Agent performs an additional timezone-conversion correction pass
when timezone questions are raised.

**Best Practice:** Enable this when your conversations frequently involve cross-timezone
coordination and scheduling.

Behavior by value:

- **Enabled (`True`):** Timezone correction pass can run and issue corrective guidance when mismatch
  is detected.
- **Disabled (`False`):** Additional timezone correction pass is skipped.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When active and triggered by timezone-check tooling, runtime evaluates recent
conversation context against business timezone and sends corrective `urgent_message` output only
when a mismatch is detected.

**Fallbacks:** Common defaults initialize this field as empty; industry setup usually assigns an
explicit value (commonly `False`, with Sales commonly setting `True`).

**Dependencies:**

- **Primary Settings:**
  - `project_business_time_zone`: Reference timezone used for correction reasoning.
- **Logic Interactions:**
  - `project_attributes_settings_platform_tools`: Timezone correction typically depends on a
    configured `check_timezone_tool` trigger path.
  - `urgent_message`: Event used to deliver correction text when an error is found.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_time_format`


**Title:** Time Format [C]

**Description:**

```md
This setting defines how the Agent formats time values in availability-check payloads and
availability response guidance.

**Best Practice:** Match this format to your users' regional expectation and keep it consistent
across all scheduling-related messages.

Behavior by value:

- **`12-hour format (hh:mm A)`:** Availability logic expects/presents times in 12-hour AM/PM style.
- **`24-hour format (HH:mm)`:** Availability logic expects/presents times in 24-hour style.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime injects this format into booking/availability schemas and instructions,
and uses it when composing user-facing guidance about available slots and requested times.

**Fallbacks:** Initialized to `12-hour format (hh:mm A)` in common defaults.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_enabled`: Time-format guidance is
    especially relevant when availability checks are active.
- **Logic Interactions:**
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: Generated
    booking payload expectations reference this time format.
  - `project_attributes_setting_booking_check_availability_max_days_in_advance`: Date/time
    validation logic uses formatted requested time alongside booking-window checks.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `enum`

**Possible values:** `["12-hour format (hh:mm A)", "24-hour format (HH:mm)"]`

**Is hidden:** `true`

---

## `project_attributes_setting_transfer_call_confirmation_phrase`


**Title:** Transfer Call to Manager - Confirmation Phrase [B]

**Description:**

````md
This setting defines the exact confirmation question the Agent asks before attempting call transfer.

**Best Practice:** Use a clear yes/no confirmation phrase so user intent is explicit before transfer
is triggered.

**Examples:**

```txt
Would you like me to connect you with a co-worker now?
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime injects this phrase into transfer-call explicit constraints for voice
conversations, guiding the Agent to ask this confirmation question before transfer. Transfer
execution is then evaluated through `transfer_call_tool` and proceeds only when transfer is enabled
and a valid transfer target number can be resolved for the current call context.

**Fallbacks:** Common defaults initialize this field as empty; industry transfer setup commonly
pre-fills a standard confirmation phrase.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_enabled`: Confirmation phrasing is relevant only when
    transfer behavior is enabled.
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Working-hours
    gating influences when transfer-confirmation logic is applicable.
- **Logic Interactions:**
  - `project_attributes_setting_transfer_call_phone_numbers`: Available transfer targets affect
    whether confirmation-based transfer path can be used.
  - `project_business_working_hour_escalation_phone`: Used with transfer rules to determine
    transfer-path availability.
  - `project_business_non_working_hour_escalation_phone`: Used with transfer rules for off-hours
    transfer-path availability.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_transfer_call_custom_statement`


**Title:** Transfer Call to Manager - Custom Statement [B]

**Description:**

````md
This setting defines an optional custom phrase the Agent uses instead of the default when promising
to transfer a call.

**Best Practice:** Use this when your business requires specific transfer wording.

**Examples:**

```txt
I will transfer you to our main line where you can leave a voicemail...
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** On phone-channel conversations with transfer enabled, runtime appends this phrase
to the default `transfer_call_tool` intent-detection condition (`agentPromised`) so transfer
promises phrased in your custom wording are recognized. Runtime injects this value into the Agent's
explicit constraints as the only transfer code phrase when it is configured.

**Fallbacks:** If this setting is empty, the Agent uses the standard transfer phrase.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_enabled`: The custom phrase is used only when transfer
    tooling is enabled.
- **Logic Interactions:**
  - `project_attributes_settings_platform_tools`: Custom tool JSON is merged after default tool
    definitions are built. Overriding `transfer_call_tool` can replace custom phrase detection, but
    does not remove the phrase from explicit constraints.
  - `transfer_call_tool`: Trigger matching expands to include this custom phrase variant.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_transfer_call_destination_availability_check_enabled`


**Title:** Transfer Call to Manager - Destination Availability Check [C]

**Description:**

```md
Controls whether a scenario-specific transfer phone number selected from Transfer Call Phone Numbers
is checked for availability outside working hours, based on the availability specified in that
setting.

- **`True`:** Check whether the selected destination is available outside working hours. This is the
  default.
- **`False`:** Select a destination without checking its after-hours availability.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Applies only when selecting from
`project_attributes_setting_transfer_call_phone_numbers`. When disabled, working-hours status is
omitted from selection, the selected destination is not checked for after-hours availability, and
phone-variable fallback context is not included.

**Fallbacks:** An empty value is treated as `True`. When advanced routing is empty, the standard
working-hours or non-working-hours escalation number is used.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_enabled`: Must be enabled.
  - `project_attributes_setting_transfer_call_phone_numbers`: Provides the scenario-specific
    transfer phone numbers and their after-hours availability.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_transfer_call_destination_format`


**Title:** Transfer Call to Manager - Phone Number Format [C]

**Description:**

```md
Controls the format of phone numbers listed in Transfer Call Phone Numbers. It is used when the
Agent chooses a number from that list.

**Best Practice:** Use `full_number` for standard phone numbers. Use `short_code` only when the
receiving phone system supports short or internal transfer codes.

- **`full_number`:** Require a complete phone number with a country code. This is the default.
- **`short_code`:** Allow a short or internal number without a country code.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Controls the phone-number format instruction used when the Agent selects a
destination from `project_attributes_setting_transfer_call_phone_numbers`. It does not affect the
standard working-hours or non-working-hours escalation number.

**Fallbacks:** An empty value is treated as `full_number`.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_phone_numbers`: Provides the scenario-specific
    transfer phone numbers whose format is controlled by this setting.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `enum`

**Possible values:** `["full_number", "short_code"]`

**Is hidden:** `true`

---

## `project_attributes_setting_custom_transfer_call_enabled`


**Title:** Voice - Transfer Call - Custom Transfer Call Enabled [C]

**Description:**

```md
Controls whether supported voice call transfers are executed by a custom handler instead of the
standard transfer command.

**Best Practice:** Enable this only when a custom transfer handler is configured. Otherwise, the
call transfer will not be executed.

- **`True`:** Delegate the complete call transfer to the custom handler.
- **`False`:** Execute the standard voice transfer command. This is the default.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** For supported native voice transfers, the Agent emits the `custom_transfer_call`
system event with the selected destination, conversation context, and transfer timeout. The standard
`transfer_call` command is skipped, so the event subscriber is responsible for executing the
transfer.

**Fallbacks:** An empty value is treated as `False`.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_enabled`: Call transfer must be enabled.
- **Logic Interactions:**
  - `project_attributes_setting_voice_integration_service`: Custom handling applies to the native
    voice transfer path and does not replace VAPI transfer execution.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_number_of_past_interactions_to_observe`


**Title:** Conversation - Number of Past Interactions to Observe [C]

**Description:**

```md
This setting controls how many past interaction entries are included as memory context for the
Agent.

**Best Practice:** Use a low-to-moderate value (for example, `3` to `5`) to balance continuity and
prompt size.

Behavior by value:

- **`0`:** Past-interaction block is disabled (`No past interactions` context is used).
- **Positive number:** Runtime includes the latest N interaction entries (up to available history).
- **Empty or non-numeric input:** Runtime normalizes/falls back to default behavior.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime reads this value in memory-building paths and slices recent entries from
the persona interaction-history array before injecting formatted past-interaction context.

**Fallbacks:** Initialized to `3` in common defaults. At runtime, non-numeric characters are
removed; if result is empty, value defaults to `3`. Missing or malformed interaction history falls
back to `No past interactions`.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_reset_persona_attributes`: Session reset policy can
    reduce retained historical context available for this setting.
- **Logic Interactions:**
  - Persona `interaction_history` is the source data this setting slices.
  - Past-interaction formatting is shared across multiple memory/prompt assembly paths.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_on_conversation_ended_enabled`


**Title:** Conversation - End Session on Conversation End [C]

**Description:**

```md
Controls whether ending a phone or webcall conversation immediately starts lightweight session
finalization.

- **`True`:** Start lightweight session finalization when the conversation ends.
- **`False`:** Do not start session finalization from the conversation-end event. This is the
  default.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When enabled and full session-end processing is disabled, supported voice and
webcall conversation-end events emit `end_session`.

**Fallbacks:** An empty value is treated as `False`.

**Dependencies:**

- **Logic Interactions:**
  - `project_attributes_setting_session_ended_full_processing_enabled`: Must be `False`; full
    processing continues to use the existing report and assessment pipeline.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_full_processing_enabled`


**Title:** Conversation - Session Ended - Full Processing Enabled [C] [IMPORTANT]

**Description:**

```md
Controls whether session end runs full analysis, reporting, and finalization.

**Best Practice:** Keep this enabled unless voice or webcall sessions need lightweight cleanup.

- **`True`:** Run full session-end processing. This is the default.
- **`False`:** Skip analysis and reporting. Supported voice and webcall sessions reset session data
  and emit `session_ended` directly.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When an `end_session` event is received, `True` runs the existing report,
assessment, and finalization pipeline. `False` skips analysis and reporting, resets session data,
and emits `session_ended`.

**Fallbacks:** Defaults to `True`.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_reset_persona_attributes`: Controls the depth of
    lightweight cleanup.
  - `project_attributes_setting_session_ended_report_enabled`: Sends reports only when full
    processing is enabled.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_on_conversation_ended_enabled`: Can trigger
    lightweight finalization immediately when this setting is `False`.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_reset_persona_attributes`


**Title:** Conversation - Session Ended - Reset Persona Attributes [C]

**Description:**

```md
This setting controls how much user/persona context is preserved between sessions.

**Best Practice:** Keep `False` when continuity across sessions is important. Use `True` for
stricter session isolation.

Behavior by value:

- **`True`:** Runtime performs deeper persona cleanup at session end and resets more persisted user
  profile fields for the next session.
- **`False`:** Runtime keeps additional persona/profile continuity and stores session memory updates
  for future context.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Session-end cleanup always resets core runtime fields, but this setting controls
whether extended profile fields (for example booking/contact-related data) are also cleared. It also
controls whether end-session memory summarization is persisted via
`convoagent_update_user_memories`, and whether return-session greeting phrases are regenerated for
the next session. When full session-end processing is disabled, lightweight finalization applies the
same cleanup policy without running the memory-summarization path.

**Fallbacks:** Initialized to `False` in common defaults.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_number_of_past_interactions_to_observe`: Past-interaction context is
    more useful when session memory updates are preserved (`False` mode).
  - `project_attributes_setting_initial_thoughts`: New-session thought seeding still occurs, but
    user-profile continuity differs based on this setting.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_full_processing_enabled`: When disabled, supported
    voice and webcall channels still apply this reset policy during lightweight cleanup.
  - `convoagent_update_user_memories`: Emitted when session-memory carryover is allowed.
  - `greeting_phrase` / `new_session_greeting_phrase`: In strict reset mode (`True`), runtime clears
    stored return-session greeting phrases at session end, so the next session falls back to the
    default first-session greeting instead of reusing a returning-user phrase. In continuity mode
    (`False`), runtime preserves and rotates these greeting phrases for future return visits.
  - New-session startup logic resets/normalizes user display name behavior differently when strict
    reset mode is enabled.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_waiting_mode_fallback_instruction`


**Title:** Conversation - Waiting Mode - Fallback Instruction [C]

**Description:**

````md
This setting defines the message guidance the Agent uses when waiting mode times out before an
external result arrives.

**Best Practice:** Keep the instruction short, apologetic, and action-oriented so users get a clear
next step when a third-party response is delayed.

**Examples:**

```txt
Suggest to the user that you will relay the information to the manager, and they will reach out as soon as they are available.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** On `waiting_mode_fallback` trigger, runtime builds a fallback instruction by
prepending the base instruction from
`project_attributes_setting_waiting_mode_fallback_base_instruction` to this setting value, then
sends the response through the active channel path.

**Fallbacks:** Initialized in common defaults to a generic manager-relay fallback phrase.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_waiting_mode_timeout`: Defines when this fallback instruction is
    activated.
  - `project_attributes_setting_waiting_mode_fallback_base_instruction`: Base instruction placed
    before this setting value; if it is empty at runtime, a built-in generic apology is used
    instead.
- **Logic Interactions:**
  - `waiting_mode_fallback`: Timer event that triggers fallback delivery.
  - `project_attributes_setting_voice_integration_service_voice_mode`: `voice-to-voice` and
    `speech-to-speech` modes use the direct voice context/command path for fallback delivery; other
    channels use the normal reply path.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_waiting_mode_timeout`


**Title:** Conversation - Waiting Mode - Timeout [C]

**Description:**

```md
This setting defines how many seconds waiting mode stays active before fallback behavior is
triggered.

**Best Practice:** Set this slightly above your typical third-party response time so normal
responses arrive before fallback is used.

Behavior by value:

- **Positive number:** Runtime schedules waiting fallback timer for the configured interval.
- **Empty value:** Runtime falls back to default waiting timeout behavior.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When waiting mode is activated, runtime pauses the follow-up (`DisableFollowUp`)
and sends `set_timer` with `timerName="waiting_mode_fallback"` and
`eventIdn="waiting_mode_fallback"` using this interval. At the timeout the paused follow-up is
resumed, and on phone and webcall channels it is re-armed with
`project_attributes_setting_follow_up_timer_voice_interval_agent_speech_ended`, since no fallback
message follows when an earlier message already ended the waiting mode. Only a follow-up paused by
the waiting mode (follow-up state `disabled_auto`) is re-armed; one disabled manually (for example
by a live operator or an SMS reply) stays disabled.

**Fallbacks:** Initialized to `60` in common defaults. Runtime also falls back to `60` when this
field is empty at activation time.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_waiting_mode_fallback_instruction`: Defines the message behavior
    once this timeout is reached.
- **Logic Interactions:**
  - `convoagent_activate_waiting_mode`: Entry point that starts waiting-mode timer scheduling.
  - Follow-up timers are disabled while waiting mode is activated to prevent competing prompts.
  - `convoagent_update_followup`: System event that re-arms a waiting-mode-paused follow-up on
    phone and webcall channels after the fallback fires (`reason="waiting_mode_fallback"`).
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_test_mode_phone_numbers_static`


**Title:** Project - Testing - Test Mode Phone Numbers Static [C] [IMPORTANT]

**Description:**

````md
Project-scoped JSON list of phone-call numbers that should always run in test mode for this project,
even when the main test-mode switch is turned off.

**Best Practice:** Use this for QA or demo phone numbers that should apply across every account
using this project. Keep each number in full international format with country code so matching
stays predictable.

**Examples:**

```json
["+15550003333", "+15550004444"]
```

Accepted number format per item:

- With plus: `+15550003333`
- Without plus: `15550004444`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime reads this project-scoped list together with the customer-scoped
`project_attributes_setting_test_mode_phone_numbers` list. During the session test-mode check, both
arrays are merged and deduplicated after phone normalization that trims whitespace and removes a
leading `+`. The override is evaluated only for standard phone-call sessions where the active
conversation actor uses Voice Connector (phone). If the current actor `externalId` matches any
merged number, the session is treated as test mode and follows the same mocked scheduling,
messaging, and transfer-safe behavior as when `project_attributes_setting_test_mode=True`. Chat,
SMS, webcall, and other non-phone session types do not use this override. Once `last_convo_actor_id`
is available, either match result is stored as canonical `session_test_mode` and remains unchanged
until session cleanup; a missing actor leaves the status uncached so later checks can retry.
Integrations can explicitly set the canonical persona attribute for non-phone sessions, as Assessor
does for chat and phone runs.

**Fallbacks:** Defaults to the preseeded assessor voice-number list shown above. If you replace this
value with `[]`, this project adds no static phone-number-based override.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_test_mode`: Global test-mode switch; this list adds project-wide
    phone-number overrides on top of it.
  - `project_attributes_setting_test_mode_phone_numbers`: Customer-scoped list merged with this
    project-scoped list before matching.
- **Logic Interactions:**
  - `project_attributes_setting_common_phone_numbers`: Uses similar phone-number formatting
    expectations, but common/shared-number handling and test-mode overrides are evaluated
    independently.
````

**Level:** `Project`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

---
