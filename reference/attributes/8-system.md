# 8. System

Back to the [attribute index](index.md).

## `project_attributes_private_dynamic_ami_template`


**Title:** AMI - Template [C]

**Description:**

```md
This attribute stores the system-generated AMI (Agent Main Instruction) template text. The system
uses this template as the source for producing the runtime AMI instruction.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Examples:**

- When workflow-builder content changes, this template is regenerated and recompiled.
- If no generated template exists yet, the value remains an empty placeholder until generation runs.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system builds this template from
`project_attributes_private_dynamic_workflow_builder_canvas` content and then compiles it into
`project_attributes_private_dynamic_ami_compiled` for runtime instruction consumption.

**Fallbacks:** During initialization, if the attribute is missing, the system seeds it with an empty
placeholder string until template generation updates it.

**Dependencies:**

- **Primary Settings:**
  - No direct customer-facing settings are required.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_workflow_builder_canvas`: Provides the source canvas content
    that is transformed into the AMI template.
  - `project_attributes_private_dynamic_ami_compiled`: Receives the compiled output generated from
    this template.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_ami_compiled`


**Title:** AMI - Compiled [C]

**Description:**

```md
This attribute stores the compiled AMI (Agent Main Instruction) text that the runtime actually uses
as the Agent's main instruction. The value is generated automatically from the AMI template during
instruction preparation workflows.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Examples:**

- After workflow-builder updates are applied, this compiled AMI is regenerated and becomes the
  active main instruction.
- If the template contains placeholders like `[[project_business_name]]`, the compiled AMI stores
  the final text after those placeholders are replaced with current Customer Attribute values.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system compiles `project_attributes_private_dynamic_ami_template` into this
attribute by resolving placeholder tokens in the format `[[attribute_idn]]` with current Customer
Attribute values. Conversation runtime uses this compiled text as the main instruction context, and
assessment workflows also read the same compiled instruction for evaluation runs.

Native voice mode (`project_attributes_private_feature_flag_v2v_native_tools`) builds introductory
and intent instructions from the current canvas; tool calls read that canvas again. This compiled
attribute continues to support base-mode, chat, and assessment workflows; native intent routing does
not rewrite it.

**Fallbacks:** During initialization, if this attribute is missing, the system seeds it with a
whitespace placeholder until the next compile cycle runs.

**Dependencies:**

- **Primary Settings:**
  - No direct customer-facing settings are required.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_ami_template`: Source template used to produce this compiled
    output.
  - `project_attributes_private_dynamic_workflow_builder_canvas`: Upstream workflow-builder content
    that drives template regeneration before this compiled value is produced.
  - Referenced Customer Attributes in `[[attribute_idn]]` placeholders: Their current values are
    injected into the compiled instruction text during compilation.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_caller_id_routing`


**Title:** Dynamic - Caller ID Routing [C]

**Description:**

```md
This advanced system configuration stores the compiled caller-ID defaults and override routing used
by voice and SMS runtime selection and pooled public-number lookup.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Update `project_attributes_setting_caller_id_pool` and let publish/setup rebuild
this routing table automatically.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Publish/setup compiles the editable caller-ID pool into a normalized routing with
two O(1) hash indexes. Runtime combines this compiled override table with the base default
connectors:

- `routes`: keyed by phone prefix for outbound voice and SMS selection.
- `phone_numbers`: keyed by pooled connector suffix for resolving the linked public phone number.
- `max_prefix_length`: the longest prefix currently present in `routes`, used to avoid checking
  impossible prefix lengths at runtime.

Each `routes[prefix]` entry can include `voice_connector_idn`, an optional `sms_binding`, and
`phone_number`. Session-start logic extracts the suffix from the active pooled connector idn and
uses `phone_numbers` to resolve the Agent's live public number without scanning all prefixes.
Follow-up SMS can also prefer the current session's paired connector before falling back to pure
prefix matching.

**Fallbacks:** If the editable pool is empty or malformed, publish/setup rewrites this attribute
back to an empty routing and runtime falls back to the default single connectors.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_caller_id_pool`: Source configuration compiled into this routing
    table.
  - `project_attributes_setting_sms_provider`: Selects which base SMS provider is used while setup
    compiles and stores the concrete per-route `sms_binding` used later by runtime.
- **Logic Interactions:**
  - `project_representative_agent_voice_phone_country_code`: Used while compiling prefix values when
    a pool item omits `country_code`.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_itm_template`


**Title:** ITM - Template [B]

**Description:**

```md
This attribute stores the system-generated ITM (Intention Type Map) template text built from the
workflow-builder intent definitions. The runtime uses this template as the source for generating the
compiled ITM used by downstream intent-processing logic.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Examples:**

- When intent-type entries are updated in the workflow builder, this template is regenerated from
  the latest intent titles and bodies.
- If the template includes placeholders like `[[project_business_name]]`, compilation resolves them
  with current Customer Attribute values before producing the compiled ITM.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system builds this template from the `intent_types` section of
`project_attributes_private_dynamic_workflow_builder_canvas`, then compiles it into
`project_attributes_private_dynamic_itm_compiled`. During downstream preparation, the template is
also compared with the current industry's canonical default template. An exact content match lets
the system use the corresponding predefined working-hours and non-working-hours maps without LLM
filtering; a changed custom template is filtered from the compiled ITM instead. The resulting maps
are consumed during conversation and report-intent analysis.

**Fallbacks:** During initialization, if this attribute is missing, the system seeds it with a
whitespace placeholder until template generation runs.

**Dependencies:**

- **Primary Settings:**
  - No direct customer-facing settings are required.
- **Logic Interactions:**
  - `project_business_industry`: Selects the canonical default template used for the exact-match
    comparison and the corresponding predefined working-hours variants.
  - `project_attributes_private_dynamic_workflow_builder_canvas`: Provides source intent-type
    content used to build this template.
  - `project_attributes_private_dynamic_itm_compiled`: Receives compiled output generated from this
    template.
  - `project_attributes_private_dynamic_itm_non_working_hours_compiled`: Derived downstream from the
    compiled ITM for non-working-hours intent routing.
  - `project_attributes_private_dynamic_itm_working_hours_compiled`: Derived downstream from the
    compiled ITM for working-hours intent routing.
  - Referenced Customer Attributes in `[[attribute_idn]]` placeholders: Their values are injected
    into compiled output during template compilation.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_itm_compiled`


**Title:** ITM - Compiled [C]

**Description:**

```md
This attribute stores the compiled ITM (Intention Type Map) that runtime workflows use as the base
intent map. The value is generated automatically from the ITM template and updated when workflow
instructions are rebuilt.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Examples:**

- After intent-type updates are saved, the system recompiles this ITM and refreshes downstream
  intent-map outputs.
- If the source template contains placeholders like `[[project_business_name]]`, this compiled ITM
  stores the resolved text after replacement with current Customer Attribute values.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system compiles `project_attributes_private_dynamic_itm_template` into this
attribute, then uses this compiled map as input for downstream ITM preparation. When this value
matches the last successfully prepared value and both derived maps still contain content, the system
reuses them. When the value changes or either derived map is missing, the system regenerates both
maps and refreshes stored intent entries. Assessment workflows also read this compiled ITM value.

Native voice mode (`project_attributes_private_feature_flag_v2v_native_tools`) builds introductory
and intent instructions from the current canvas; tool calls read that canvas again. This compiled
attribute continues to support base-mode, chat, and assessment workflows; native intent routing does
not rewrite it.

**Fallbacks:** During initialization, if this attribute is missing, the system seeds it with a
whitespace placeholder until compilation runs. If compilation produces no ITM content, downstream
preparation clears both working-hours variants instead of invoking LLM filtering.

**Dependencies:**

- **Primary Settings:**
  - No direct customer-facing settings are required.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_itm_template`: Source template compiled into this attribute.
  - `project_attributes_private_dynamic_last_prepared_itm_compiled`: Records this compiled ITM after
    the working-hours and non-working-hours maps are built. Both normal ITM preparation and
    actor-specific configuration preview compilation reuse those maps only while the recorded value
    still matches this attribute and both maps are available.
  - `project_attributes_private_dynamic_itm_non_working_hours_compiled`: Derived downstream from
    this compiled ITM for non-working-hours routing.
  - `project_attributes_private_dynamic_itm_working_hours_compiled`: Derived downstream from this
    compiled ITM for working-hours routing.
  - `project_attributes_private_dynamic_intents_list`: Refreshed from this compiled ITM when intent
    entries are rebuilt.
  - Referenced Customer Attributes in `[[attribute_idn]]` placeholders: Their values are injected
    into this compiled output during compilation.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_last_prepared_itm_compiled`


**Title:** ITM - Prepared Source [C]

**Description:**

```md
This attribute stores the compiled ITM (Intention Type Map) used during the latest preparation of
the working-hours and non-working-hours versions. It allows separate workflows to verify that a
saved pair belongs to the current ITM.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system compares this value with
`project_attributes_private_dynamic_itm_compiled` before reusing the persistent working-hours and
non-working-hours pair. Reuse also requires both prepared outputs to contain content. The value is
updated after ITM preparation and cleared when the preparation cache is reset.

**Fallbacks:** If this attribute is empty or differs from the current compiled ITM, the system does
not treat the persistent pair as prepared for that ITM and regenerates the required outputs.

**Dependencies:**

- **Primary Settings:**
  - No direct customer-facing settings are required.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_itm_compiled`: Supplies the ITM snapshot stored here after
    preparation.
  - `project_attributes_private_dynamic_itm_non_working_hours_compiled`: Must contain content before
    the saved pair can be reused.
  - `project_attributes_private_dynamic_itm_working_hours_compiled`: Must contain content before the
    saved pair can be reused.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_itm_non_working_hours_compiled`


**Title:** ITM - Non Working Hours - Compiled [C]

**Description:**

```md
This attribute stores the compiled ITM (Intention Type Map) used when runtime logic is operating in
non-working-hours mode. The value is generated automatically by ITM preparation workflows and is
updated when the base ITM changes.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Examples:**

- When the current ITM exactly matches the industry's canonical default, the system uses the
  predefined non-working-hours map without an LLM call.
- After a custom ITM changes, the system regenerates this value by filtering out
  working-hours-specific content from the base compiled ITM.
- If the base ITM and this prepared output are unchanged, the system reuses the existing value.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system populates this attribute for non-working-hours intent routing. It first
uses the compiled ITM cache to avoid rebuilding unchanged content when both prepared variants are
present. When a rebuild is required, an exact match between the current ITM template and the
industry's canonical default selects the predefined industry map. Otherwise, a non-empty custom
`project_attributes_private_dynamic_itm_compiled` is processed with LLM filtering that removes
working-hours-specific behavior. An actor-specific configuration preview also reuses the prepared
pair when its compiled ITM exactly matches the successfully prepared account ITM. If that preview
does not select intent types, it falls back to this persistent map without generating an override.
Any other non-empty selection receives an isolated LLM-generated map. These preview maps are stored
separately and do not overwrite this attribute. Runtime consumers use this map when working-hours
checks resolve to non-working-hours context, including conversation intent selection, session-ended
report pre-analysis, and assessment workflows.

Native voice mode (`project_attributes_private_feature_flag_v2v_native_tools`) builds introductory
and intent instructions from the current canvas; tool calls read that canvas again. This compiled
attribute continues to support base-mode, chat, and assessment workflows; native intent routing does
not rewrite it.

**Fallbacks:** During initialization, if this attribute is missing, the system seeds it with a
whitespace placeholder until ITM preparation runs. If the base compiled ITM is empty, preparation
clears this value. If a predefined map is unavailable for an unrecognized industry, the default path
also produces an empty value.

**Dependencies:**

- **Primary Settings:**
  - No direct customer-facing settings are required.
- **Logic Interactions:**
  - `project_business_industry`: Selects the canonical default template and predefined
    non-working-hours map used when the current template matches that default.
  - `project_attributes_private_dynamic_itm_compiled`: Base compiled ITM used for downstream
    non-working-hours filtering on update cycles.
  - `project_attributes_private_dynamic_itm_working_hours_compiled`: Paired output generated in the
    same ITM preparation cycle.
  - `project_attributes_private_dynamic_intents_list`: Rebuilt alongside these ITM variants during
    ITM preparation.
  - Referenced Customer Attributes in `[[attribute_idn]]` placeholders: Their values are injected
    during compile-in-place processing.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_itm_working_hours_compiled`


**Title:** ITM - Working Hours - Compiled [C]

**Description:**

```md
This attribute stores the compiled ITM (Intention Type Map) used when runtime logic is operating in
working-hours mode. The value is generated automatically by ITM preparation workflows and is updated
when the base ITM changes.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Examples:**

- When the current ITM exactly matches the industry's canonical default, the system uses the
  predefined working-hours map without an LLM call.
- After a custom ITM changes, the system regenerates this value by filtering out
  non-working-hours-specific content from the base compiled ITM.
- If the base ITM and this prepared output are unchanged, the system reuses the existing value.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system populates this attribute for working-hours intent routing. It first
uses the compiled ITM cache to avoid rebuilding unchanged content when both prepared variants are
present. When a rebuild is required, an exact match between the current ITM template and the
industry's canonical default selects the predefined industry map. Otherwise, a non-empty custom
`project_attributes_private_dynamic_itm_compiled` is processed with LLM filtering that removes
non-working-hours-specific behavior. An actor-specific configuration preview also reuses the
prepared pair when its compiled ITM exactly matches the successfully prepared account ITM. If that
preview does not select intent types, it falls back to this persistent map without generating an
override. Any other non-empty selection receives an isolated LLM-generated map. These preview maps
are stored separately and do not overwrite this attribute. Runtime consumers use this map when
working-hours checks resolve to working-hours context, including conversation intent selection,
session-ended report pre-analysis, and assessment workflows.

Native voice mode (`project_attributes_private_feature_flag_v2v_native_tools`) builds introductory
and intent instructions from the current canvas; tool calls read that canvas again. This compiled
attribute continues to support base-mode, chat, and assessment workflows; native intent routing does
not rewrite it.

**Fallbacks:** During initialization, if this attribute is missing, the system seeds it with a
whitespace placeholder until ITM preparation runs. If the base compiled ITM is empty, preparation
clears this value. If a predefined map is unavailable for an unrecognized industry, the default path
also produces an empty value.

**Dependencies:**

- **Primary Settings:**
  - No direct customer-facing settings are required.
- **Logic Interactions:**
  - `project_business_industry`: Selects the canonical default template and predefined working-hours
    map used when the current template matches that default.
  - `project_attributes_private_dynamic_itm_compiled`: Base compiled ITM used for downstream
    working-hours filtering on update cycles.
  - `project_attributes_private_dynamic_itm_non_working_hours_compiled`: Paired output generated in
    the same ITM preparation cycle.
  - `project_attributes_private_dynamic_intents_list`: Rebuilt alongside these ITM variants during
    ITM preparation.
  - Referenced Customer Attributes in `[[attribute_idn]]` placeholders: Their values are injected
    during compile-in-place processing.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_report_additional_criteria`


**Title:** Reports - Session Ended Report - Additional Criteria [C]

**Description:**

````md
This advanced system configuration stores extra report-routing criteria blocks that are merged into
your main session-ended report rules. It lets the platform add new report directions without
replacing your base criteria.

**Note:** This hidden field is system-managed and normally populated automatically. Do not edit it
manually.

**Pro-Tip:** Keep each custom report title stable over time. The system turns that title into a key
and uses it to connect criteria, schema, and event routing.

Example value:

```json
{
  "vip_escalation": "**Criteria for VIP Escalation:**\n- If it is a Manager or Human Request send to [manager email]"
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system stores this value as a JSON object keyed by normalized report-title
keys. During report preparation, each criteria string is appended to the base
`project_attributes_setting_session_ended_report_criteria_template` and persisted into the advanced
system configuration `project_attributes_setting_session_ended_report_criteria_complete_template`
before compilation.

**Fallbacks:** Default value is `{}`. If empty (or `{}`), no additional criteria blocks are
appended, and report routing uses only the base criteria template.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_criteria_template`: Base criteria text that
    receives appended additional criteria sections.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_additional_schema`: Uses the same normalized
    keys so each additional criteria block has a matching structured output schema.
  - `project_attributes_setting_session_ended_report_event_map`: Uses the same normalized keys to
    map each additional direction to its outbound routing event.
  - `project_attributes_setting_session_ended_report_criteria_complete_template`: Advanced system
    configuration storing merged base and additional criteria text.
  - `project_attributes_setting_session_ended_report_criteria_compiled`: Advanced system
    configuration generated from the merged template and consumed by report-decision logic.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_report_additional_schema`


**Title:** Reports - Session Ended Report - Additional Schema [C]

**Description:**

````md
This advanced system configuration stores structured JSON schema blocks for extra report directions
in session-ended reports. It defines what data should be produced when those additional directions
are evaluated.

**Note:** This hidden field is system-managed and normally populated automatically. Do not edit it
manually.

**Pro-Tip:** Keep schema fields small and explicit. If you add a custom direction, make sure its key
matches the corresponding additional criteria entry.

Example value:

```json
{
  "vip_escalation": {
    "type": "object",
    "properties": {
      "should_be_sent": {
        "type": "boolean"
      },
      "destination": {
        "type": "string"
      },
      "reason": {
        "type": "string"
      }
    }
  }
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system stores a JSON object keyed by normalized report-title keys. When an
additional direction is registered, the platform prepends a `should_be_sent` boolean into that
direction schema, then caches it here. During report-direction generation, this schema is injected
as `additional_directions` so structured payloads are generated for each custom direction.

**Fallbacks:** Default value is `{}`. If empty (or `{}`), no additional direction schema is injected
and no additional-direction payloads are generated.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_criteria_compiled`: Advanced system
    configuration with compiled routing rules that run together with additional-direction schema.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_additional_criteria`: Must share the same
    normalized keys so schema and criteria stay aligned.
  - `project_attributes_setting_session_ended_report_event_map`: Uses the same keys to map generated
    additional-direction payloads to system events.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_report_criteria_complete_template`


**Title:** Reports - Session Ended Report - Criteria - Complete Template [C]

**Description:**

````md
This advanced system configuration stores the merged session-ended report criteria before
placeholder compilation. It combines your main criteria template with any additional criteria
blocks.

**Pro-Tip:** Treat this as read-only. Update your main criteria setting (and optional additional
criteria) instead of editing this merged value directly.

Example merged output:

```txt
**Criteria for SMS Report:**
- During working hours, send SMS to [working-hours escalation phone]

---
**Criteria for VIP Escalation:**
- If it is a Manager or Human Request send an email to [manager email]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During report preparation, the system starts with
`project_attributes_setting_session_ended_report_criteria_template` and appends every entry from
`project_attributes_setting_session_ended_report_additional_criteria`, separated by `---`. The
merged text is saved here, then compiled into the advanced system configuration
`project_attributes_setting_session_ended_report_criteria_compiled` so placeholders like
`[[attribute_idn]]` resolve before runtime report decisions.

**Fallbacks:** Initialized with an empty placeholder string. If no additional criteria exist, this
value mirrors the base criteria template. If both are empty, compiled routing criteria can remain
empty.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_criteria_template`: Base source criteria.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_additional_criteria`: Optional appended
    criteria blocks.
  - `project_attributes_setting_session_ended_report_criteria_compiled`: Advanced system
    configuration compiled from this merged template and used by report-direction logic.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_report_criteria_compiled`


**Title:** Reports - Session Ended Report - Criteria - Compiled [C]

**Description:**

````md
This advanced system configuration stores the compiled session-ended report criteria used during
runtime report routing. It is generated automatically and should be treated as read-only.

**Pro-Tip:** Update your base report criteria and additional criteria instead of editing this
compiled output directly.

Example compiled value:

```txt
**Criteria for SMS Report:**
- During working hours:
  - If it is a Manager or Human Request send an SMS to [working-hours escalation phone]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During report preparation, the system compiles
`project_attributes_setting_session_ended_report_criteria_complete_template` into this value so
placeholders like `[[attribute_idn]]` are resolved to current runtime values. Report-direction logic
consumes this compiled criteria text to decide whether SMS/email/additional directions should be
sent. For additional directions that are selected for sending, destination event routing is resolved
through `project_attributes_setting_session_ended_report_event_map`.

**Fallbacks:** Initialized as an empty string placeholder during setup. If merged criteria is empty,
compiled criteria can remain empty until source criteria is prepared.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_criteria_complete_template`: Source template
    that is compiled into this runtime routing value.
  - `project_attributes_setting_session_ended_report_enabled`: Must allow report sending for this
    criteria to be used in delivery flow.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_criteria_template`: Base criteria source
    upstream of merge+compile.
  - `project_attributes_setting_session_ended_report_additional_criteria`: Optional criteria blocks
    merged before compilation.
  - `project_attributes_setting_session_ended_report_event_map`: Maps selected additional-direction
    keys to outbound event IDNs used during delivery.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_session_ended_report_event_map`


**Title:** Reports - Session Ended Report - Event Map [C]

**Description:**

````md
This advanced system configuration maps additional report-direction keys to system event IDNs. It
enables custom follow-up events when an additional report direction is marked for sending.

**Note:** This hidden field is system-managed and normally populated automatically. Do not edit it
manually.

**Pro-Tip:** Keep custom report titles stable. Direction keys are derived from titles, so renaming
titles can break existing event mappings.

Example value:

```json
{
  "vip_escalation": "crm_create_ticket",
  "high_value_lead": "sales_notify_pipeline"
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When additional report criteria is registered, the system normalizes
`report_title` into a key and stores `{key: event_idn}` in this map. During session-ended report
delivery, each additional direction with `should_be_sent = true` resolves its event IDN from this
map and dispatches a system event with the direction payload.

**Fallbacks:** Initialized as `{}`. If empty, or if a direction key has no matching mapped event
IDN, additional-direction event routing cannot be resolved for that direction.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_additional_criteria`: Defines additional
    direction keys that must match this mapping.
  - `project_attributes_setting_session_ended_report_additional_schema`: Defines structured payload
    shape for each mapped direction key.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_criteria_compiled`: Core criteria evaluation
    runs alongside additional-direction handling that can trigger mapped events.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_shadow_metrics_enabled`


**Title:** Assessment - Shadow Metrics - Enabled [C]

**Description:**

```md
Controls whether the Agent performs an additional shadow assessment after completing the standard
session assessment. Enable it to compare revised assessment criteria without replacing the standard
assessment result.

**Pro-Tip:** Keep this setting disabled unless you are actively evaluating the revised metrics.
Enabling it adds one LLM call to each session that reaches assessment, increasing processing time
and cost.

**Examples:**

- **Enabled (`True`):** The Agent completes the standard assessment, then performs an additional
  shadow assessment and emits a comparison event.
- **Disabled (`False`):** The Agent performs only the standard assessment.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system completes the standard analysis and scoring first. When this setting is
exactly `True`, it then makes one additional LLM call using a revised schema and scores that
response with the same assessment rules while suppressing fallback-report emission.

The revised schema narrows `user_refused` to explicit declines or a hang-up during an active attempt
to complete the scenario. It also expands `mentioned_issues` to cover SMS non-receipt, silence or an
unresponsive Agent, mispronunciation, and repetition, and expands `business_issues` to cover
unavailable slots, unavailable services or products, service-area restrictions, business-hours
restrictions, and pricing or eligibility mismatches.

After shadow scoring, the system emits the `convoagent_shadow_metrics` event with both standard and
shadow opportunity and Agent success metrics, the revised issue classifications, and a shadow schema
version. The standard assessment remains the source of the result passed to session completion:
shadow values do not overwrite its opportunity status, Agent success code, success factor, reporting
status, actual result, or expected result. The downstream `session_ended` event therefore receives
the standard assessment values.

**Fallbacks:** Initialization sets an empty value to `False` without overwriting an existing value.
At runtime, only the exact value `True` enables shadow processing. `False`, an empty value, or any
other value skips the shadow assessment and comparison event.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `false`

---

## `project_attributes_private_dynamic_booking_check_availability_payload_schema_compiled`


**Title:** Booking - Check Availability - Schema Compiled [C]

**Description:**

````md
This advanced system configuration stores the compiled schema used to generate and validate
check-availability request payloads. It is built automatically from booking check-availability
settings and should be treated as read-only.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Pro-Tip:** Edit your check-availability payload and validation templates, then republish so the
platform rebuilds this compiled schema.

Example compiled shape:

```json
{
  "payload": {
    "...": "..."
  },
  "validation": {
    "...": "..."
  },
  "validationRecap": {
    "valid": true,
    "explanation": ""
  },
  "additionalValidation": {
    "requestedDate": "2026-03-10",
    "requiredFieldsMissing": false
  }
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The platform combines
`project_attributes_setting_booking_check_availability_payload_schema_template` with
`project_attributes_setting_booking_check_availability_validation_schema_template` (or a default
validation schema when validation is empty), adds recap/additional-validation fields, then compiles
placeholders into this runtime JSON schema. Availability flows load this compiled schema before
extracting payloads and validating required fields.

**Fallbacks:** Initialized as an empty string placeholder. If
`project_attributes_setting_booking_check_availability_payload_schema_template` is empty, this
compiled schema can remain empty and availability flows stop with configuration errors. If
`project_attributes_setting_booking_check_availability_validation_schema_template` is empty, a
default validation schema is injected during schema build.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: Main source
    payload schema for availability requests.
  - `project_attributes_setting_booking_check_availability_validation_schema_template`: Optional
    validation schema merged into the compiled object.
- **Logic Interactions:**
  - `project_attributes_setting_booking_check_availability_max_days_in_advance`: Referenced by
    generated additional-validation rules.
  - `project_attributes_setting_time_format`: Used when building time-format instructions in
    additional-validation rules.
  - `project_attributes_private_feature_flag_multi_location`: When enabled, the compiled schema can
    be generated per location key and runtime selects current or `default`.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_booking_schema_compiled`


**Title:** Dynamic - Booking Schema Compiled [C]

**Description:**

````md
This advanced system configuration stores the compiled schema used to generate booking
create-request payloads. It is auto-generated from booking schema settings and should be treated as
read-only.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Pro-Tip:** Keep booking payload and meta-fields templates aligned. Republish after edits so this
compiled schema is rebuilt before live booking requests.

Example compiled shape:

```json
{
  "payload": {
    "...": "..."
  },
  "metaFields": {
    "...": "..."
  }
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The platform combines `project_attributes_setting_booking_payload_schema_template`
with `project_attributes_setting_booking_meta_fields_schema_template` (or a default meta-fields
object when empty), then compiles placeholders into this runtime booking schema. Booking flows load
this compiled schema to extract request objects and can append additional runtime validation blocks
before submission.

**Fallbacks:** Initialized as an empty string placeholder. If
`project_attributes_setting_booking_payload_schema_template` is empty, this compiled schema can
remain empty and booking flows stop with configuration errors. If
`project_attributes_setting_booking_meta_fields_schema_template` is empty, a default no-meta-fields
object is injected.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_payload_schema_template`: Main source payload schema for
    booking submissions.
  - `project_attributes_setting_booking_meta_fields_schema_template`: Optional meta-fields schema
    merged into the compiled booking object.
- **Logic Interactions:**
  - `project_attributes_setting_booking_type`: Runtime booking flow branches by booking type after
    validating this schema exists.
  - `project_attributes_setting_booking_url`: Required for default booking mode after schema checks
    pass.
  - `project_attributes_private_feature_flag_multi_location`: When enabled, the compiled schema can
    be generated per location key and runtime selects current or `default`.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_account_initialized_first_time`


**Title:** Account - Initialized First Time [C]

**Description:**

```md
This advanced system configuration marks whether full production account setup has already
completed. It prevents production first-time initialization steps from running repeatedly.

**Best Practice:** Do not set this flag manually. Let setup and publish lifecycle logic control it
so onboarding, callbacks, and version-upgrade routines execute in the correct order.

**Examples:**

- **`False`:** Full production setup has not completed yet. The system can copy onboarding values
  into empty settings, run first-time production callbacks, and allow production connector/bootstrap
  tasks when the full setup path runs.
- **`True`:** Full production setup is completed. Production first-setup-only writes are skipped,
  and normal publish/update behavior is applied.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During the full publish/import lifecycle, a missing value is initialized (with
legacy version handling for older deployments), first-setup operations run while value is `False`,
then it is set to `True` before post-setup work completes. When Agent Creator disables full
initialization, publish handling runs the shortened skip-initialization setup before it sends the
Agent Creator callback, preparing only the minimal connector/webhook state needed for the callback.
The shortened path does not mark this production setup flag as `True`; repeat skip setup is
controlled by separate General Manager flow state. Update flows use this flag to avoid production
first-setup behavior and to run version-specific upgrade routines only for already initialized
accounts.

**Fallbacks:** If missing, initialization sets it to `False` for first-time setup (or treats some
legacy upgrades as already initialized using previous-version metadata).

**Dependencies:**

- **Primary Settings:**
  - None. This flag is controlled by initialization lifecycle logic.
- **Logic Interactions:**
  - The advanced system configuration `agent_creator_setting_should_be_initialized` controls whether
    publish handling uses a shortened setup path instead of the full production import/post-setup
    path.
  - `project_representative_agent_voice_phone_number`: Onboarding callback payloads can include the
    provisioned voice number after setup prepares phone/connector state.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_data_injection_is_timer_running`


**Title:** Data Injection - Timer Is Running [C]

**Description:**

```md
This advanced system configuration shows whether a data-injection refresh timer is already active.
It helps prevent duplicate timer scheduling for external data fetches.

**Best Practice:** Treat this as read-only and control data injection from the main data-injection
toggle setting.

Behavior by value:

- **`True`:** A refresh timer is already in progress, so normal preparation flow does not start a
  second timer.
- **`False`:** No active timer marker is present, so data-injection flow can start a new fetch cycle
  and schedule the next refresh.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When data injection starts, runtime sets this flag to `True` and schedules a
single `data_injection_timer` event using the configured interval. This prevents repeated
conversation turns from creating duplicate timers. When data injection is disabled, runtime clears
retrieved data and resets this flag to `False` on the next flow pass.

**Fallbacks:** Initialized to `False` during common setup.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_data_injection_is_enabled`: Advanced system configuration that
    enables/disables the fetch loop using this timer marker.
  - `project_attributes_setting_data_injection_update_period`: Advanced system configuration used as
    the timer interval when scheduling the next fetch.
- **Logic Interactions:**
  - `project_attributes_private_data_injection_retrieved_data`: Cleared together with this flag when
    data-injection path is stopped.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_data_injection_payload`


**Title:** Data Injection - Payload [C]

**Description:**

````md
This advanced system configuration stores the JSON payload sent to the external data-injection
webhook on each fetch cycle. It defines what request data is passed to your external source.

**Best Practice:** Keep this payload stable and schema-consistent with your webhook contract. Use
small, explicit fields that your endpoint expects.

Example value:

```json
{
  "customer_id": "abc_123",
  "source": "runtime_sync",
  "requested_scope": "business_updates"
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During each fetch cycle, runtime reads this JSON and sends it through the
`data_injection` webhook command. Retrieved response content is later stored in injected-data
context for downstream reasoning.

**Fallbacks:** Initialized during common setup with a generic default JSON payload object. If this
payload is empty or schema-mismatched, runtime still sends it as-is in the `data_injection` webhook
request without local validation.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_data_injection_is_enabled`: Advanced system configuration that
    controls whether payload dispatch occurs.
- **Logic Interactions:**
  - `project_attributes_private_data_injection_retrieved_data`: Stores the response data generated
    from requests sent with this payload.
  - `project_attributes_setting_data_injection_update_period`: Governs how often this payload is
    resent in periodic fetch cycles.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_data_injection_retrieved_data`


**Title:** Data Injection - Retrieved Data [C]

**Description:**

````md
This advanced system configuration stores the latest fetched external data that can be injected into
Agent context during conversations. It is the runtime data cache for data injection.

**Best Practice:** Treat this as system-managed output. Tune summary and token-limit settings rather
than editing cached text directly.

Example value:

```txt
Inventory update: Product A low stock, Product B backordered.
Promo status: Weekend campaign active until Sunday 23:59.
Support notice: Callback queue delay is approximately 20 minutes.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When new data arrives from the webhook, runtime optionally summarizes it (based on
summary settings) and stores the result here. Thought/context assembly then appends this value into
`<AdditionalBusinessContext>` when data injection is enabled and content is non-empty.

Published native voice mode returns the current value through `get_business_information` only when
data injection is enabled. It does not depend on automatic thoughts to deliver this context.

**Fallbacks:** Initialized as a blank placeholder value. If the stored value is blank, injected
external context is omitted. When data injection is disabled, runtime clears this value back to a
blank placeholder.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_data_injection_is_enabled`: Advanced system configuration that
    controls whether this cached data is actively fetched and injected.
  - `project_attributes_setting_data_injection_needs_summary`: Advanced system configuration
    deciding whether fetched data is summarized before storage.
- **Logic Interactions:**
  - `project_attributes_setting_data_injection_max_summary_tokens`: Applies when summary mode is
    enabled and caps summary output size.
  - `project_attributes_static_additional_business_context`: Can be combined with this fetched data
    in the same additional business context block.
  - `project_attributes_private_data_injection_is_timer_running`: Reset together when data injection
    is stopped.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_agent_persona`


**Title:** Dynamic - Agent Persona [C]

**Description:**

````md
This advanced system configuration stores the Agent's runtime persona statement used in core prompt
instructions. It keeps identity wording consistent across conversation channels.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Update agent identity fields (name/title) and business identity fields in their
main settings, then let the platform regenerate this persona automatically.

Example value:

```txt
Your name is Ava. You are a professional conversational agent (internal identifier: ConvoAgent). Your job title is an AI Host at Blue Harbor Bistro.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During dynamic-attribute preparation, runtime composes this value from
`project_representative_agent_name`, `project_representative_agent_title`, and
`project_business_name`. The same builder also computes a companion runtime job-title phrase used in
voice-mode instruction headers and voice connector prompt sync. This persona string is injected into
the main conversation prompt and voice connector initial-system-instruction sync.

**Fallbacks:** If `project_representative_agent_title` is empty, builder logic uses a generic
representative phrase for title wording. If name/business fields are incomplete, the resulting
persona text can be sparse.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_name`: Source for Agent identity wording.
  - `project_representative_agent_title`: Source for job-title wording used in persona.
  - `project_business_name`: Source for business identity wording in persona text.
- **Logic Interactions:**
  - `project_representative_agent_chat_speaking_style`: Applied alongside persona in chat-mode main
    instruction.
  - `project_representative_agent_voice_speaking_style`: Applied alongside persona in voice-mode
    instructions and connector prompts.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_agent_title`


**Title:** Dynamic - Agent Title [C]

**Description:**

```md
This advanced system configuration stores the runtime job-title phrase for the Agent (including the
article, such as "a" or "an"). It is generated automatically from the representative title setting.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep the representative title as a clean role phrase (for example, "AI Host" or
"Sales Rep") so generated identity instructions sound natural.

**Examples:**

- **Representative title set to `AI Host`:** Runtime title becomes `an AI Host`
- **Representative title set to `Support Specialist`:** Runtime title becomes `a Support Specialist`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Dynamic-persona builder reads `project_representative_agent_title`, chooses an
article using first-letter vowel logic, and writes the composed phrase into this attribute. Runtime
uses this value in voice-focused instruction headers and connector initial-system-instruction sync.

**Fallbacks:** If `project_representative_agent_title` is empty, builder logic falls back to a
generic representative phrase.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_title`: Source title used to compose this runtime phrase.
- **Logic Interactions:**
  - `project_attributes_setting_voice_integration_service_voice_mode`: Voice-to-voice prompt header
    path explicitly uses this runtime title phrasing.
  - `project_representative_agent_voice_speaking_style`: Applied together with this title wording in
    voice-mode instruction blocks.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_business_context`


**Title:** Dynamic - Business Context [C]

**Description:**

````md
This advanced system configuration stores the compiled business-context block that the Agent uses as
its primary business knowledge context during conversations.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep core business profile, offerings, and contact information up to date in
their source settings. This context is regenerated from those values.

Example structure:

```txt
# Base information
- Business type: ...
- Business name: ...

# Business description
...

# Contact information
...

# Products and services
...
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Common dynamic setup first initializes this attribute to a placeholder, then
industry-specific builders regenerate the full context block based on the active
`project_business_industry`. Generated content is injected into `<BusinessContext>` in the main
conversation prompt and is also reused in voice connector instruction sync (with optional phonetic
business-name substitution for voice output).

Published native voice mode retrieves this value through `get_business_information` on demand
instead of embedding it in the native system prompt. The value itself is generated as before.

**Fallbacks:** If industry-specific context build is not executed, this value can remain a
whitespace placeholder. When source business fields are empty, generated context can be
partial/sparse.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Selects which industry context template is used to build this
    value.
  - `project_business_type`: Base business profile field included in context.
  - `project_business_name`: Base business identity field included in context.
  - `project_business_story`: Base business description field included in context.
  - `project_business_country`: Contact section source field.
  - `project_business_address`: Contact section source field.
  - `project_business_public_phone`: Contact section source field.
  - `project_business_website_url`: Contact section source field.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_products_and_services`: Dynamic offerings block that is
    injected into industry-specific business-context builders before this context is regenerated.
  - `project_attributes_current_specials`: Included in dynamic business context sections.
  - `project_attributes_terms_and_conditions`: Included in dynamic business context sections.
  - `project_attributes_faq`: Included in dynamic business context sections.
  - `project_attributes_payment_methods`: Included in dynamic business context sections.
  - `project_attributes_products_and_services_served_area`: Included in service-coverage section.
  - `project_attributes_products_and_services_served_zip_codes`: Included conditionally by coverage
    logic.
  - `project_attributes_setting_products_and_services_background_check_location_enabled`: Controls
    whether served zip codes are emitted in generated context.
  - `project_business_name_phonetic`: Used for voice-context substitution during connector prompt
    sync.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_booking_schema_template`


**Title:** Dynamic - Booking Schema Template [C]

**Description:**

````md
This advanced system configuration stores the prepared booking-request schema template before
runtime placeholder compilation. It combines booking payload fields with meta-fields into one schema
structure.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep payload and meta-fields templates aligned and valid JSON. After updates,
republish so the prepared template and compiled runtime schema are rebuilt.

Example prepared shape:

```json
{
  "payload": {
    "...": "..."
  },
  "metaFields": {
    "...": "..."
  }
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Builder logic composes this template from
`project_attributes_setting_booking_payload_schema_template` and
`project_attributes_setting_booking_meta_fields_schema_template`. In multi-location mode, it can
produce per-location keyed schema variants before compilation.

**Fallbacks:** Initialized as a whitespace placeholder. If booking payload template is empty, this
value can remain unbuilt and downstream booking schema compilation/runtime validation may fail. If
meta-fields template is empty, builder logic injects a generic no-meta-fields fallback object.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_payload_schema_template`: Primary source for booking request
    payload structure.
  - `project_attributes_setting_booking_meta_fields_schema_template`: Source for optional booking
    meta-fields.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_multi_location`: Enables per-location keyed schema
    construction path.
  - `project_attributes_setting_booking_payload_schema_template`: In per-location mode, payload
    schema keys are used as the location keys for generated template variants.
  - `project_attributes_setting_booking_type`: Booking flow branch that later validates presence of
    compiled booking schema derived from this template.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_booking_check_availability_schema_template`


**Title:** Dynamic - Booking Check Availability Schema Template [C]

**Description:**

````md
This advanced system configuration stores the prepared check-availability schema template before
runtime placeholder compilation. It combines availability payload rules, validation rules, and
helper validation sections into one schema object.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep availability payload and validation templates synchronized, then republish
so the prepared template and compiled availability schema refresh together.

Example prepared shape:

```json
{
  "payload": {
    "...": "..."
  },
  "validation": {
    "...": "..."
  },
  "validationRecap": {
    "...": "..."
  },
  "additionalValidation": {
    "...": "..."
  }
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Builder logic composes this template from
`project_attributes_setting_booking_check_availability_payload_schema_template` and
`project_attributes_setting_booking_check_availability_validation_schema_template`, then appends
`validationRecap` and `additionalValidation` sections. In multi-location mode, it can produce
per-location keyed template variants before compilation.

**Fallbacks:** Initialized as a whitespace placeholder. If availability payload template is empty,
this value can remain unbuilt and availability-validation flows can stop with configuration errors.
If validation template is empty, builder logic injects a default validation object.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: Primary source
    for availability request payload structure.
  - `project_attributes_setting_booking_check_availability_validation_schema_template`: Optional
    source for availability validation rules.
- **Logic Interactions:**
  - `project_attributes_setting_booking_check_availability_max_days_in_advance`: Referenced by
    generated additional-validation rules.
  - `project_attributes_setting_time_format`: Used when generating time-format instructions in
    additional-validation sections.
  - `project_attributes_private_feature_flag_multi_location`: Enables per-location keyed template
    construction path.
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: In per-location
    mode, payload schema keys are used as the location keys for generated template variants.
  - `project_attributes_setting_booking_check_availability_type`: Availability flow branch that
    later validates presence of compiled availability schema derived from this template.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_business_locations_indexes`


**Title:** Dynamic (LLM or non-LLM-based) - Business Locations Indexes [C]

**Description:**

````md
This advanced system configuration stores the normalized list of business location indexes used by
multi-location routing. It turns free-form location entries into stable location keys.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Update locations in the main business locations setting and let the platform
regenerate indexes automatically. Keep location names clear so generated keys remain meaningful.

Example value:

```json
["default", "downtown_office", "north_branch"]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Location processing logic parses `project_business_locations` and generates a JSON
array of semantic unique indexes (ASCII lowercase + underscore), with the first location forced to
`default`. These indexes are used by multi-location runtime to resolve and switch the active
location during conversation handling.

**Fallbacks:** If business locations input is empty, this value is reset to a whitespace
placeholder. When locations change, the index list is regenerated from the updated source.

**Dependencies:**

- **Primary Settings:**
  - `project_business_locations`: Source list used to generate normalized location indexes.
  - `project_attributes_private_feature_flag_multi_location`: Enables runtime flows that consume
    generated location indexes.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_business_locations_object`: Runtime location selection reads
    this map together with indexes; if object data is empty, location-switch evaluation exits.
  - `project_attributes_setting_booking_payload_schema_template`: Multi-location feature updates can
    reinitialize booking payload templates alongside location-derived attributes.
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: Multi-location
    feature updates can reinitialize availability payload templates alongside location-derived
    attributes.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_business_locations_object`


**Title:** Dynamic (LLM or non-LLM-based) - Business Locations Object [C]

**Description:**

````md
This advanced system configuration stores a generated map of location indexes to human-readable
location descriptions for multi-location routing.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Maintain clear location names in your main locations setting and let the platform
regenerate this map automatically.

Example value:

```json
{
  "default": "Main downtown location",
  "north_branch": "North branch near Central Park"
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Location-processing logic converts the source locations list into an index list
and this companion description map. Multi-location runtime analysis reads this map as contextual
location descriptions when deciding which location should become active for the current user
session.

**Fallbacks:** If the source locations field is empty, this value is reset to a whitespace
placeholder. When locations are changed, the map is regenerated from the updated source.

**Dependencies:**

- **Primary Settings:**
  - `project_business_locations`: Source list used to generate location descriptions and keys.
  - `project_attributes_private_feature_flag_multi_location`: Enables runtime location-switching
    behavior that consumes generated location data.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_business_locations_indexes`: Runtime location-selection
    logic reads this index list together with the description map; if indexes are empty, switching
    evaluation exits.
  - `project_attributes_setting_booking_payload_schema_template`: Multi-location feature updates can
    reinitialize booking payload templates alongside this generated location data.
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: Multi-location
    feature updates can reinitialize availability payload templates alongside this generated
    location data.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_email_signature`


**Title:** Dynamic - Email Signature (Compiled) [C]

**Description:**

````md
This is the ready-to-send email signature block, generated from the editable signature template
setting.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

Example value:

```txt
Yours truly,
Alex Johnson | Front Desk Manager
Example Tavern
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** At setup/publish, the platform compiles the paired editable signature-template
setting by substituting each `[[attribute_idn]]` placeholder with the current value of that
attribute, and stores the ready-to-send result here. When the advanced system configuration
`project_attributes_private_feature_flag_email_universal_template` is enabled, outgoing emails read
this value and pass it to the signature area of the message footer with its original line breaks
preserved. The delivery template renders those line breaks for each output format. When that
configuration is disabled, outgoing emails use their own separate built-in structured signature
instead and never read this value.

**Fallbacks:** If the source template is empty, this value is regenerated as empty at the next
compile. If this value is empty at send time on the template-based delivery path, the signature area
of the message is left blank; it is not backfilled with a default signature.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_email_signature_template`: Editable source template this value is
    compiled from.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_email_universal_template`: Determines whether outgoing
    emails read this compiled value as their signature.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

**Is read-only:** `true`

---

## `project_attributes_private_dynamic_email_variables`


**Title:** Dynamic - Email Variables [C]

**Description:**

````md
This advanced system configuration stores industry-specific email aliases in a compact key-value
text block that is regenerated automatically by industry setup flows.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep source manager/department email settings current, and let industry setup
flows rebuild these aliases.

Example value:

```txt
manager_email: manager@example.com
order_email: orders@example.com
private_dining_email: events@example.com
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Common dynamic setup first clears this value, then industry-specific preparation
skills repopulate it with relevant aliases (for example manager email only, or manager plus
specialized reservation/order emails depending on industry).

**Fallbacks:** If industry-specific preparation is not executed, this value can remain a whitespace
placeholder. Missing source email fields are resolved through default-value helper logic used by the
builders.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Selects which email-variable builder populates this value.
  - `project_business_manager_email`: Common baseline source for manager-level email alias.
- **Logic Interactions:**
  - `project_attributes_hospitality_large_group_reservation_email`: Hospitality-specific alias
    source.
  - `project_attributes_restaurant_catering_email`: Restaurant-specific alias source.
  - `project_attributes_restaurant_large_group_reservation_email`: Restaurant-specific alias source.
  - `project_attributes_restaurant_order_email`: Restaurant-specific alias source.
  - `project_attributes_restaurant_private_dining_email`: Restaurant-specific alias source.
  - `project_attributes_catering_catering_email`: Catering-specific alias source.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_first_customer_call_events_must_be_sent`


**Title:** Dynamic - First Customer Call Events Must Be Sent [C]

**Description:**

```md
This advanced system marker controls whether setup tooling is notified when the next eligible
customer voice conversation starts and finishes. Phone calls and webcalls are eligible. Ordinary
setup and reinitialization open this first-call callback window, which closes when the
conversation-ending callback is queued.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Examples:**

- **`False`:** Customer phone calls and webcalls do not send first-call started or finished
  callbacks. The system keeps this value after the first eligible voice conversation finishes so
  later conversations do not repeat the callbacks.
- **`True`:** The next eligible customer phone call or webcall start sends the first-call started
  callback. When that voice conversation ends, the system sends the first-call finished callback and
  resets this marker to `False`.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Ordinary setup and reinitialization set this marker to `True`, so each setup type
opens the callback window for the next eligible customer phone call or webcall. When that voice
conversation starts, runtime emits the system event `agent_creator_first_customer_call_started`,
which tells setup tooling the conversation started. The callback handler sends the external actor
event `first_customer_call_started` with the Agent phone number, user phone number,
`conversation_channel`, and customer ID. The `conversation_channel` value is `phone` or `webcall`,
so the receiver can distinguish whether `user_phone_number` is a phone number or the
platform-generated UUID for a webcall. Runtime adds a missing leading `+` only to phone-call
identifiers and preserves webcall UUIDs unchanged. Runtime intentionally keeps the marker enabled
after the start callback so the matching finished callback can still be sent. When an eligible
customer phone call or webcall ends while this marker is `True`, runtime emits
`agent_creator_first_customer_call_finished`, which tells setup tooling the voice conversation
finished. The callback handler sends the external actor event `first_customer_call_finished` with
the same core payload fields. After enqueueing the finished callback, runtime resets this marker to
`False`, so later voice conversations do not send either first-call callback unless lifecycle logic
enables the marker again.

**Fallbacks:** Missing, empty, or `False` values suppress both first-call callbacks. A `True` value
only dispatches callbacks for customer phone or webcall conversation start and end events.

**Dependencies:**

- **Primary Settings:**
  - None. Runtime lifecycle logic owns this marker.
- **Logic Interactions:**
  - `project_representative_agent_voice_phone_number`: Included in the callback payload as the Agent
    phone number.
  - `agent_creator_actor_id`: Determines which setup-assistant actor receives the callback event.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_intents_list`


**Title:** Dynamic - Intents List [C]

**Description:**

````md
This advanced system configuration stores the current intent-name catalog extracted from the active
intent type map.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Update your intent map/scenario configuration in source settings, then let ITM
preparation rebuild this list automatically.

Example value:

```json
["Manager or Human Request", "Large Reservation", "Cancellation"]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** ITM preparation extracts intent names from intent-map heading blocks and stores
them as a JSON-formatted string array in this attribute. Runtime uses this list as enum constraints
for intent-detection schemas and report-content schema generation, and to keep report templates
aligned with active intent coverage.

**Fallbacks:** Initialized as a whitespace placeholder during common setup. If ITM is unchanged but
this list is empty, ITM preparation repopulates it. If intent-map structure is malformed, extracted
intent coverage can be incomplete.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_private_dynamic_itm_compiled`: Source intent-map content parsed to build
    this intent-name list.
  - `project_business_industry`: Selects default intent-type templates used when workflow
    instructions and ITM are regenerated, which can change extracted intent names.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_content`: Report-content maintenance uses this
    list to add/remove report blocks by active intents.
  - `project_attributes_private_dynamic_session_ended_report_content_json`: Report-content JSON
    regeneration uses this list as enum coverage for `report_type` values.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_latest_executed_migration`


**Title:** Migrations - Latest Executed Migration [C]

**Description:**

```md
This attribute records the most recent completed NAF migration. It lets interrupted upgrades resume
from the next migration instead of restarting the entire migration sequence.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Examples:**

- During clean account initialization, an empty value is set to the final ordered migration
  applicable to the installed NAF `x.y.z` version.
- During the first checkpoint-aware update of an existing account, the checkpoint is initialized to
  the final migration applicable to the account's previous NAF version before newer migrations run.
- If a later migration fails, the value remains on the last completed migration so the next retry
  starts from the failed migration.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The migration runtime compares this checkpoint with the last ordered migration
included in the installed NAF version. Project publication runs pending migrations synchronously.
Conversation-start recovery sends `generalmanageragent_run_migrations` through the global queue so
retries are serialized. After each migration finishes, the runtime immediately advances this
checkpoint. When event-driven recovery advances it, the runtime requests a NAF project publication
to complete initialization work that depends on migrated data. A valid migration request emits
`generalmanageragent_run_migrations_success` after reaching or confirming the installed version's
target. Migration implementations must be safe to retry because an interruption after migration side
effects but before checkpoint persistence can replay the current migration.

**Fallbacks:** An empty checkpoint is interpreted using account initialization state. Clean accounts
store the final ordered migration applicable to the installed NAF `x.y.z` version without replaying
historical migrations. Existing accounts use the publish event's previous version as their baseline
when supplied, including when it equals the current version. Without a previous version, they use
the installed Project version and assume historical migrations are complete. This also applies to
conversation recovery without publish context. If the selected baseline cannot map to the ordered
migration list, execution stops without advancing the checkpoint. Non-empty values are never
replaced by initialization fallback; an unrecognized checkpoint also stops migration execution for
investigation. If the checkpoint already matches or is later than the installed version's target, no
migration runs.

**Dependencies:**

- **Primary Settings:**
  - None. The installed NAF project version determines the target migration.
- **Logic Interactions:**
  - `project_attributes_private_account_initialized_first_time`: Synchronous publish-time migration
    execution and previous-version bootstrap apply to accounts that completed first-time
    initialization; clean accounts initialize directly to the installed target.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_phone_variables`


**Title:** Dynamic - Phone Variables [C]

**Description:**

````md
This advanced system configuration stores a generated phone-variable map used by internal phone
selection logic and prompt templates.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep your escalation phone numbers current so transfer and automation logic can
resolve the right number without extra clarification.

Example value:

```txt
working_hour_escalation_phone: +14155550101
non_working_hour_escalation_phone: +14155550999
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Common setup initializes this value, and industry preparation rebuilds it as a
key-value block used by runtime phone-resolution logic. It is consumed as fallback context when
transfer-call number selection is ambiguous and when rule-based SMS tasks extract target numbers.

**Fallbacks:** If preparation has not populated this field, it can remain a whitespace placeholder.
In that case, transfer-number selection omits the fallback instructions and context block. Missing
source phone fields are resolved through default-value helper logic used during variable
composition, so downstream resolution may return no usable number.

**Dependencies:**

- **Primary Settings:**
  - `project_business_working_hour_escalation_phone`: Primary source for escalation routing during
    working hours.
  - `project_business_non_working_hour_escalation_phone`: Primary source for escalation routing
    outside working hours.
- **Logic Interactions:**
  - `project_attributes_setting_transfer_call_enabled`: Transfer-call flows consume this map only
    when transfer behavior is enabled.
  - `project_attributes_setting_transfer_call_phone_numbers`: Criteria-based transfer routing can
    fall back to values from this map when direct criteria resolution is inconclusive.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_products_and_services`


**Title:** Dynamic (LLM or non-LLM-based) - Products & Services [C]

**Description:**

````md
This advanced system configuration stores the runtime-ready products/services context that the Agent
uses for decision-making and prompt injection.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep your offered and not-offered service lists explicit, and use structured mode
only when the source content is clean enough to be parsed into reliable JSON.

**Examples:**

```json
{
  "products_and_services_offering": [
    {
      "name": "Teeth Cleaning",
      "category": "Dental Service",
      "description": "Standard preventive cleaning appointment.",
      "payment_link": "null",
      "price": [
        {
          "price": "$120",
          "condition": "regular price"
        }
      ]
    }
  ],
  "products_and_services_not_offering": [
    {
      "name": "Emergency Surgery",
      "category": "Dental Service",
      "explanation": "null"
    }
  ]
}
```

```txt
- Offering (available / provided):
General cleaning
Deep cleaning

- Not offering (not available / not provided):
After-hours emergency services
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Preparation logic builds this value from your services source fields. In
structured mode, it validates and converts content into a schema-constrained JSON object; in
non-structured mode, it stores a combined plain-text block. Runtime then injects this value into
business-context/technical variable compositions and service-availability checks during
conversation.

**Fallbacks:** If both source service fields are empty, this value is reset to a whitespace
placeholder. If source fields and structured-mode state are unchanged and the current value is
already populated, regeneration is skipped.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_products_and_services`: Main source of offered services/products.
  - `project_attributes_products_and_services_not_offering`: Main source of excluded or unavailable
    services/products.
  - `project_attributes_setting_products_and_services_structured_representation_enabled`: Controls
    structured JSON vs plain-text representation mode.
- **Logic Interactions:**
  - `project_business_industry`: Selects industry-specific context templates that consume this
    prepared value.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_prompt_calendar`


**Title:** Dynamic (LLM-based) - Prompt Calendar [C]

**Description:**

````md
This advanced system configuration stores a rolling, human-readable calendar used by the Agent when
reasoning about dates in conversations.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep your business time zone accurate and leave calendar injection enabled so
date interpretation stays aligned with local business time.

Example value:

```txt
today Wednesday 25th of February 2026, 2026-02-25
tomorrow Thursday 26th of February 2026, 2026-02-26
this Friday 27th of February 2026, 2026-02-27
next Monday 2nd of March 2026, 2026-03-02
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Data-injection preparation refreshes this calendar in the configured business time
zone and stores a multi-day timeline with relative markers (for example today/tomorrow/this/next).
Prompt-building, scheduling, availability checks, and working-hours reasoning consume this calendar
as shared date context. Assessment workflows also consume this calendar as date-reference context
when evaluating conversation quality outputs.

Published native voice mode reads this value through `get_calendar` on demand instead of including
it in the native system prompt. The existing calendar-generation schedule is unchanged; when no
calendar is available, the tool asks for an exact date rather than inventing one.

**Fallbacks:** Initialized as a whitespace placeholder during setup. Calendar refresh is skipped
when the system marker indicates the stored calendar is already current for the business day;
otherwise it is regenerated and persisted again. If calendar injection is disabled, this context is
omitted from calendar-injection prompt blocks.

**Dependencies:**

- **Primary Settings:**
  - `project_business_time_zone`: Defines the time zone used to generate calendar dates and day
    labels.
  - `project_attributes_setting_calendar_injection_is_enabled`: Enables/disables calendar generation
    and injection behavior.
- **Logic Interactions:**
  - `project_business_working_hours`: Working-hours evaluation logic uses this calendar together
    with schedule-derived context to interpret date-related requests.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_prompt_calendar_created_at`


**Title:** Dynamic - Prompt Calendar Creation Date [C]

**Description:**

````md
This advanced system configuration stores the business-day marker for the current generated calendar
context.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep this field read-only and let the platform update it automatically whenever
calendar context is regenerated.

Example value:

```txt
2026-02-25, Wednesday
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Calendar-preparation logic compares the current business-day marker against this
stored value. If they differ (or this field is empty), the system regenerates calendar context and
writes a new marker to indicate freshness for the current day.

**Fallbacks:** Initialized as a whitespace placeholder during setup. A blank or stale marker forces
calendar regeneration; a matching marker skips regeneration for that day.

**Dependencies:**

- **Primary Settings:**
  - `project_business_time_zone`: Defines the date/day format used for freshness checks.
  - `project_attributes_setting_calendar_injection_is_enabled`: Controls whether calendar-refresh
    logic runs and updates this marker.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_prompt_calendar`: This marker controls whether the prompt
    calendar is regenerated or reused for the current business day.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_rag_knowledge_base_append_text_structured`


**Title:** Dynamic (LLM-based) - RAG - Knowledge Base - Text - Structured [C]

**Description:**

````md
This advanced system configuration stores structured Markdown generated from text added to your RAG
append source.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Add knowledge in the text append source field, then let the platform convert and
ingest it automatically instead of editing this intermediate output manually.

Example value:

```md
# Product Warranty Policy

## Explains warranty coverage and claim steps.

## Warranty; Returns; Support

Customers can return damaged items within 30 days with proof of purchase. <<<RAG_TOPIC_SEPARATOR>>>
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When new text is detected in the append-text source, RAG processing converts that
input into structured Markdown topic blocks and stores the result here. Topic-creation logic then
consumes this content, creates AKB topics, and clears this field after successful processing.

**Fallbacks:** Initialized as a whitespace placeholder during setup. If the reset control is
triggered, generated topics for this append channel are cleared and this field is reset to an empty
string before any new ingest run. After successful processing, topic-creation logic also clears this
field to an empty string. If empty, no topic-creation step is executed.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_rag_knowledge_base_append_text`: Source text that is transformed into this
    structured representation.
  - `project_attributes_rag_knowledge_base_append_text_reset`: Clears existing generated text-append
    topics and resets intermediate processing state.
- **Logic Interactions:**
  - `project_attributes_rag_knowledge_base_append_text_log`: Updated with raw append requests during
    ingestion for audit/history tracking.
  - `project_business_industry`: Applied as a label dimension when AKB topics are created from this
    structured content.
  - `project_attributes_scenario`: Applied as a label dimension when AKB topics are created from
    this structured content.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_rag_knowledge_base_append_websites_text`


**Title:** Dynamic (LLM-based) - RAG - Knowledge Base - Websites - Text [C]

**Description:**

````md
This advanced system configuration temporarily stores raw text gathered from website append requests
before it is converted into structured RAG topics.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep website append input focused and specific so extracted content is easier to
transform into clean knowledge topics.

Example value:

```txt
Pricing page: Annual plan includes onboarding, support, and API access.
FAQ: Business hours are Monday-Friday, 9 AM to 6 PM local time.
Returns page: Refund requests are accepted within 14 days.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Website-ingestion workflows append scraped text chunks into this field while
results are streamed back. Once the final chunk arrives, the pipeline converts accumulated raw text
to structured Markdown for topic creation, then clears this field. If this field is populated
manually, the same conversion path is applied on the next ingest cycle.

**Fallbacks:** Initialized as a whitespace placeholder during setup. Reset operations clear this
buffer to an empty string before new ingestion, and successful website-processing runs clear it the
same way after conversion. Failed website search/extraction callbacks are handled before this buffer
is extended, so error text is not stored as knowledge. If no website text is accumulated, no
downstream conversion or topic creation is triggered from website input.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_rag_knowledge_base_append_websites`: Source URLs/instructions that trigger
    website scraping and populate this buffer.
  - `project_attributes_rag_knowledge_base_append_websites_reset`: Clears existing website-append
    generated topics and resets this website-text buffer.
- **Logic Interactions:**
  - `project_attributes_rag_knowledge_base_append_websites_log`: Updated with website append
    requests for audit/history tracking.
  - `project_business_industry`: Applied as a label dimension when website-derived AKB topics are
    created.
  - `project_attributes_scenario`: Applied as a label dimension when website-derived AKB topics are
    created.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_rag_knowledge_base_append_websites_text_structured`


**Title:** Dynamic (LLM-based) - RAG - Knowledge Base - Websites - Text - Structured [C]

**Description:**

````md
This advanced system configuration stores structured Markdown generated from website-ingested text
before it is committed into AKB topics.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Use website append input for source URLs and let the platform complete
extraction, structuring, and topic creation automatically.

Example value:

```md
# Refund Policy / Returns Window

## Summarizes refund eligibility and deadlines.

## Refunds; Returns; Policy

Refund requests are accepted within 14 days when the product is unused. <<<RAG_TOPIC_SEPARATOR>>>
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Website append workflows convert accumulated raw website text into structured
topic blocks and store them here. AKB topic-creation logic then consumes this content, creates
topics with append-specific labels/source IDs, and clears this field after processing.

**Fallbacks:** Initialized as a whitespace placeholder during setup. Reset operations clear this
field to an empty string before new website-ingestion runs, and successful topic creation clears it
the same way after processing. If this field is empty, AKB topic creation from website-append
content is skipped.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_rag_knowledge_base_append_websites`: Source URLs/instructions that drive
    website extraction and downstream structuring.
  - `project_attributes_rag_knowledge_base_append_websites_reset`: Clears website-append generated
    topics and resets structured ingestion state.
- **Logic Interactions:**
  - `project_attributes_rag_knowledge_base_append_websites_log`: Receives append request history
    used for tracking website-ingestion operations.
  - `project_business_industry`: Applied as a label dimension when topics are created from this
    structured content.
  - `project_attributes_scenario`: Applied as a label dimension when topics are created from this
    structured content.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_schedule_non_working_days`


**Title:** Dynamic (LLM-based) - Schedule - Non-Working Days [C]

**Description:**

````md
This advanced system configuration stores the business days that are treated as non-working in
runtime schedule context.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep your main working-hours setting explicit about closed days so date and
availability answers stay accurate.

Example value:

```txt
Sunday
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Schedule-preparation logic parses business working-hours input and derives a
normalized non-working-days string for prompt context. Runtime working-hours checks, schedule
rendering, and availability reasoning consume this value together with working days/hours data.
Shared working-schedule prompt builders include this value when present and otherwise rely on the
other derived schedule fields or the raw business working-hours source.

**Fallbacks:** If business working-hours input is empty, this value is reset to a whitespace
placeholder. If parsed output indicates no non-working days, this field is also normalized to a
whitespace placeholder. Regeneration is skipped when source schedule data is unchanged and both
derived working days and working hours fields are already populated. If all derived schedule text
fields are empty, runtime schedule-context builders fall back to `project_business_working_hours`.

**Dependencies:**

- **Primary Settings:**
  - `project_business_working_hours`: Source schedule text parsed to derive non-working days.
- **Logic Interactions:**
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Controls
    whether conversation-level working-hours status logic actively uses generated schedule context.
  - `project_business_time_zone`: Determines day/time interpretation when runtime checks consume
    this derived schedule data.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_schedule_working_days`


**Title:** Dynamic (LLM-based) - Schedule - Working Days [C]

**Description:**

````md
This advanced system configuration stores the normalized list of business working days used in
runtime schedule reasoning.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep your primary working-hours schedule consistent and up to date so working-day
logic, booking checks, and schedule responses stay aligned.

Example value:

```txt
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Schedule-preparation logic parses business working-hours input and writes this
working-days summary for prompt context. Runtime schedule blocks, working-hours status evaluation,
and availability flows consume this value as the day-level anchor for open/closed reasoning. Shared
working-schedule prompt builders use this value when derived schedule context is available.

**Fallbacks:** If business working-hours input is empty, this field is set to a whitespace
placeholder. Regeneration is skipped when source schedule data is unchanged and both derived working
days and working hours fields are already populated. If all derived schedule text fields are empty,
runtime schedule-context builders fall back to `project_business_working_hours`.

**Dependencies:**

- **Primary Settings:**
  - `project_business_working_hours`: Source schedule text parsed to derive working days.
- **Logic Interactions:**
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Controls
    whether conversation-level working-hours status logic actively uses generated schedule context.
  - `project_business_time_zone`: Determines day/time interpretation when runtime checks consume
    this derived schedule data.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_schedule_working_days_hours_exceptions`


**Title:** Dynamic (LLM-based) - Schedule - Exceptions [C]

**Description:**

````md
This advanced system configuration stores schedule exceptions that adjust or clarify normal
working-day/working-hour behavior.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep exception details explicit in your main working-hours source, especially for
holidays or special dates, so runtime schedule responses stay trustworthy.

Example value:

```txt
Thanksgiving Day: closed.
Christmas Eve: open from 9:00 AM to 2:00 PM.
All other holidays follow the normal schedule.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Schedule-preparation logic extracts exception notes from the business
working-hours source and stores them as supplemental context. Prompted working-hours reasoning and
availability responses include this text when present. Shared working-schedule prompt builders add
this value only when it is populated.

**Fallbacks:** If source schedule data is empty, this field is reset to a whitespace placeholder. If
the parser resolves exceptions as absent (`null`-equivalent), this field is also normalized to a
whitespace placeholder. Regeneration is skipped when source schedule data is unchanged and both
derived working days and working hours fields are already populated. If all derived schedule text
fields are empty, runtime schedule-context builders fall back to `project_business_working_hours`.

**Dependencies:**

- **Primary Settings:**
  - `project_business_working_hours`: Source schedule text parsed to derive exception notes.
- **Logic Interactions:**
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Controls
    whether conversation-level working-hours status logic actively uses generated schedule context.
  - `project_business_time_zone`: Determines day/time interpretation when exception-aware schedule
    context is consumed.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_schedule_working_hours`


**Title:** Dynamic (LLM-based) - Schedule - Working Hours [C]

**Description:**

````md
This advanced system configuration stores a normalized summary of business working-hour ranges used
across runtime availability logic.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep opening and closing intervals clear in your main working-hours source,
especially if you have split shifts or late-night hours.

Example value:

```txt
Monday: 9:00 AM-6:00 PM
Tuesday: 9:00 AM-6:00 PM
Wednesday: 9:00 AM-6:00 PM
Thursday: 9:00 AM-8:00 PM
Friday: 9:00 AM-8:00 PM
Saturday: 10:00 AM-4:00 PM
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Schedule-preparation logic parses the business working-hours source and writes
this working-hours summary for prompt context. Scheduling and availability flows consume this value
as the hour-range reference in working-schedule context. Shared working-schedule prompt builders use
this value when derived schedule context is available. Working-hours status checks primarily use the
structured schedule object and fall back to this summary when object data is unavailable.

**Fallbacks:** If source schedule data is empty, this field is reset to a whitespace placeholder.
Regeneration is skipped when source schedule data is unchanged and both derived working days and
working hours fields are already populated. If all derived schedule text fields are empty, runtime
schedule-context builders fall back to `project_business_working_hours`.

**Dependencies:**

- **Primary Settings:**
  - `project_business_working_hours`: Source schedule text parsed to derive working-hour ranges.
- **Logic Interactions:**
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Controls
    whether conversation-level working-hours status logic actively uses generated schedule context.
  - `project_business_time_zone`: Determines day/time interpretation when runtime checks consume
    working-hour ranges.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_schedule_compiled`


**Title:** Dynamic - Schedule - Compiled [C]

**Description:**

```md
Structured JSON schedule produced by the WHE producer skill. Format: {"regular": {mon/tue/.../sun:
[{open, close}]}, "exceptions": [{date, intervals, reason}]}

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The WHE (Working Hours Engine) producer skill parses business working hours text
into a deterministic JSON structure. The decision-point skill
`session_get_working_hours_status.nslg` (CAMainFlow) consumes this attribute via the canonical
`working_schedule_utils.working_schedule_session_is_open()` helper and caches the resulting BOOL
status (`"true"` / `"false"`) into the `working_hours_status` persona attribute — without LLM
involvement. Assessor workflows also read this compiled schedule for deterministic working-hours
classification.

**Fallbacks:** If this attribute is empty or cannot be evaluated, conversation workflows can use
model-based status inference, assessment workflows default to working hours, and outbound tasks keep
their requested execution time. The producer writes a whitespace placeholder when source schedule
data is empty. Exception dates are parsed directly from the source `project_business_working_hours`
text — no separate exceptions input is required.

**Lifecycle:** Setup workflows generate this value and reuse it while the source working-hours text
and calendar year remain unchanged. Updates to the source take effect the next time setup runs.

**Dependencies:**

- **Primary Settings:**
  - `project_business_working_hours`: Source schedule text parsed by the producer (includes
    exception dates inline if present).
  - `project_business_time_zone`: Timezone used by the producer to resolve year-less exception dates
    and by consumers for local time calculations.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_tech_variables`


**Title:** Dynamic - Tech Variables [C]

**Description:**

````md
This advanced system configuration stores a technical context block used by automation and
information-delivery prompts.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep core business contact fields, links, and manager/escalation channels
accurate so message templates can resolve placeholders reliably.

Example value:

```txt
- agent_name: Alex
- business_name: North Dental
- country: United States
- public_phone: +14155550123

**Links:**
- website_url: https://northdental.example
- appointment_url: https://northdental.example/book

**Emails:**
- manager_email: manager@northdental.example
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Common preparation initializes this field, then industry-specific dynamic builders
repopulate it with structured contact, link, email, and service-context variables. Runtime SMS/email
information flows and SMS-task generation use it as additional context for placeholder filling and
task-object composition.

**Fallbacks:** If industry-specific preparation is not executed, this field can remain a whitespace
placeholder. Missing source fields are resolved through default-value helper logic during variable
composition, so unresolved values may stay generic or empty in downstream prompts.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Selects which industry-specific variable template populates this
    field.
  - `project_representative_agent_name`: Common source for Agent-name variable injection.
  - `project_business_name`: Common source for business-name variable injection.
  - `project_business_public_phone`: Common source for phone variable injection.
  - `project_business_manager_email`: Common source for manager-email variable injection.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_products_and_services`: Direct intermediary service-context
    payload injected by industry-specific tech-variable builders.
  - `project_attributes_products_and_services`: Upstream source used to build
    `project_attributes_private_dynamic_products_and_services`.
  - `project_attributes_products_and_services_not_offering`: Upstream excluded-service source used
    to build `project_attributes_private_dynamic_products_and_services`.
  - `project_attributes_setting_sms_send_information_enabled`: When SMS information delivery is
    enabled, runtime generation consumes this technical context.
  - `project_attributes_setting_email_send_information_enabled`: When email information delivery is
    enabled, runtime generation consumes this technical context.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_v2v_native_config`


**Title:** Dynamic - Voice - Accepted Native Configuration [C]

**Description:**

```md
Stores the successfully applied native voice configuration used by new calls.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Enabled values contain `enabled`, `voice_mode`, `canvas`, `tools`, `description`
and `introduction`, plus `prompt_context` containing the persona, title, speaking style, additional
global instruction and voicemail instruction. Attribute placeholders in canvas text are resolved
before acceptance and marked with `text_resolved`. Runtime intent compilation does not reread those
instruction attributes. Publishing validates the candidate, verifies connector application, then
replaces this value. An empty connector-application result is treated as failed preparation: the
preceding value is retained and successful initialization is not announced. Failed or superseded
preparation keeps the preceding value. Inbound startup captures it per call; outbound captures it at
dialing and passes it into startup. Active native calls retain that configuration through later
publishes or disabling. User information and business facts can still be retrieved through tools.
Legacy tool metadata remains separate.

**Fallbacks:** Initialized to `{"enabled": false}`. An absent, blank or non-enabled configuration
selects legacy mode, including when outbound is deployed before the attribute is created.

**Dependencies:**

- `project_attributes_private_feature_flag_v2v_native_tools`: Requests the next published mode.
- `project_attributes_private_dynamic_workflow_builder_canvas`: Supplies the authored candidate.
- `project_attributes_private_dynamic_v2v_native_connector_snapshot`: Stores the restore baseline.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_v2v_native_connector_snapshot`


**Title:** Dynamic - Voice - Native Connector Restore Baseline [C]

**Description:**

```md
Remembers connector settings and legacy tool metadata for restoring an account after native voice is
disabled.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Stores `connectors` keyed by connector ID and `attributes` containing the three
legacy published tool values. Each connector entry preserves its tool schema and four initial
instructions before the first native write, including empty values. Repeated native publishes keep
the baseline and add newly encountered base, web and pool connectors.

A skip-init disable restores these saved values without synchronizing unrelated settings. Full
initialization also performs ordinary connector sync once using current account attributes. Missing
connectors are skipped. The baseline is cleared only after successful disabling; failed application
or restoration retains it for retry. Existing pilot accounts without a baseline are outside this
future-toggle restore contract.

**Fallbacks:** Initialized to `{}`. A nonempty baseline requires native cleanup even if the
requested flag is off and no enabled configuration was accepted, covering interrupted application.

**Dependencies:**

- `project_attributes_private_dynamic_v2v_native_config`: Identifies the accepted native mode.
- `project_attributes_private_feature_flag_v2v_native_tools`: Requests application or restoration.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_v2v_native_mentions_cache`


**Title:** Dynamic - Voice - Canvas Mentions Cache [C]

**Description:**

```md
Remembers successfully reconciled custom canvas items so unchanged publishes can skip dependency
reconciliation calls to the language model. Library mentions are maintained by developers.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Stores `inputs` (the authored canvas and library catalog) separately from `items`
(custom-item reconciliation results). Items with `is_from_library: true` keep their corrected
developer-maintained mentions; missing or false flags identify custom items. Changes to the authored
canvas or library invalidate the cache. Matching inputs rehydrate generated mentions in a separate
native candidate without rewriting the saved canvas. Comparison uses parsed JSON, so formatting and
object-key order do not matter. Tool configuration is rebuilt and validated on every enabled
publish. Calls read their startup configuration. Disabling native mode preserves the cache.

**Fallbacks:** Initialized to `{}`. A missing or different cache reconciles custom items only. A
library-only canvas skips reconciliation even without a cache. Failed or superseded preparation does
not update the cache.

**Dependencies:**

- **Logic Interactions:**
  - `project_attributes_private_dynamic_workflow_builder_canvas`: Supplies custom items for
    comparison.
  - `project_attributes_private_dynamic_workflow_builder_canvas_library`: Supplies the dependency
    catalog used to invalidate cached results.
  - `project_attributes_private_feature_flag_v2v_native_tools`: Requests publish-time
    reconciliation.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_variables`


**Title:** Dynamic - General Variables [C]

**Description:**

````md
This advanced system configuration stores a compact general-variable context used in report-routing
and report-template reasoning.

**Best Practice:** Keep business working hours and industry-specific reservation/catering
constraints up to date so report templates can be filled with accurate operational context.

Example value:

```txt
Monday-Friday: 9:00 AM-6:00 PM

Reservation variables:
- restaurant.large_group_reservation_minimum_party_size: 8
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Common preparation initializes this field, and industry-specific dynamic builders
overwrite it with schedule context plus optional domain variables (for example reservation minimums
or catering lead-time constraints). Session-ended report direction logic uses this context when
deciding destinations and filling report templates.

**Fallbacks:** If industry-specific preparation has not populated this field, it can remain a
whitespace placeholder. Missing optional source fields are omitted or resolved as empty/default
values in the generated variable block.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Selects which industry-specific variable template populates this
    field.
  - `project_business_working_hours`: Common schedule source included in this variable context.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_content`: Report-direction generation uses this
    variable context while composing template-driven outputs.
  - `project_attributes_setting_session_ended_report_criteria_template`: Routing criteria evaluation
    uses this variable context as supplemental prompt data.
  - `project_attributes_hospitality_large_group_reservation_minimum_party_size`: Hospitality
    reservation constraint source for industry variable composition.
  - `project_attributes_restaurant_large_group_reservation_minimum_party_size`: Restaurant
    reservation constraint source for industry variable composition.
  - `project_attributes_catering_order_minimum_days_in_advance`: Catering lead-time source for
    industry variable composition.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_voice_greeting_phrase`


**Title:** Dynamic - Voice - Greeting Phrase [C]

**Description:**

````md
This advanced system configuration stores the ready-to-use voice greeting phrase used in live voice
greeting scenarios.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep your voice disclaimer and voice greeting text polished, and set a phonetic
business name when pronunciation needs tuning.

Example value:

```txt
This call may be recorded. Thank you for calling North Dental. How can I help you today?
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Setup-time preparation composes this phrase by combining disclaimer text and base
voice greeting text, with phonetic-name substitution when applicable. Runtime inbound voice greeting
flows and greeting command paths for `voice-to-voice` and `speech-to-speech` consume this value when
no persona-specific greeting override is already set.

**Fallbacks:** If a phonetic business name is not provided, composition keeps the regular business
name phrasing. If a persona-level greeting phrase is already present for the session, runtime
greeting logic prioritizes that persona value over this customer-level fallback.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_voice_greeting_phrase`: Base voice greeting text used in
    composition.
  - `project_representative_agent_voice_disclaimer_phrase`: Disclaimer prefix prepended to the
    composed greeting.
  - `project_business_name_phonetic`: Optional phonetic replacement source for business-name
    pronunciation.
- **Logic Interactions:**
  - `project_business_name`: Source token replaced by phonetic business-name value when a phonetic
    variant is provided.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_session_ended_report_content_json`


**Title:** Dynamic (LLM-based) - Reports - Session Ended Report Content JSON [C]

**Description:**

````md
This advanced system configuration stores structured JSON report templates used to send
session-ended reports. It is auto-generated from your report content configuration and should be
treated as read-only.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Pro-Tip:** Make changes in the session-ended report content setting, then let the platform
regenerate this JSON automatically.

Example value:

```json
{
  "reports": [
    {
      "report_type": "MANAGER OR HUMAN REQUEST",
      "fields": ["User name", "User phone", "20-word summary"],
      "sms_template": "MANAGER OR HUMAN REQUEST: [user name] [user phone] [20-word summary]",
      "subject_template": "MANAGER OR HUMAN REQUEST: [user name] [user phone] [6-word additional summary]"
    }
  ]
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Report-preparation logic builds this JSON from
`project_attributes_setting_session_ended_report_content`. It is regenerated when empty, when report
content changes, or when report/intent coverage is rebuilt during preparation. Report-send logic
consumes this JSON to select report templates, extract fields, and generate SMS/email content.

**Fallbacks:** Initialized as a whitespace placeholder and then generated from configured report
content or industry defaults during preparation. If this JSON is truly empty when report sending is
attempted, report delivery is skipped.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_report_content`: Source template text transformed into
    this structured JSON.
  - `project_attributes_setting_session_ended_report_enabled`: Must allow report sending for this
    JSON to be consumed.
- **Logic Interactions:**
  - `project_business_industry`: Selects default report content templates when custom content is
    empty during setup.
  - `project_attributes_private_dynamic_intents_list`: Defines the allowed report-type set used when
    generating and validating this JSON structure.
  - `project_attributes_setting_session_ended_report_criteria_template`: Report type names should
    stay aligned with routing criteria.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_feature_flag_multi_location`


**Title:** Agent - Multi-Location Feature [C] [IMPORTANT]

**Description:**

```md
This advanced system configuration enables multi-location behavior for routing and booking logic.
When enabled, the Agent can detect which business location the user is talking about and apply
location-specific booking context.

**Best Practice:** Enable this only after your locations list and booking schema settings are ready
for per-location handling.

Behavior by value:

- **Enabled (`True`)**: Conversation logic tracks active location context and booking schema
  settings are handled in location-keyed form.
- **Disabled (`False`)**: The system uses single-location behavior and keeps only the `default`
  branch when converting from multi-location schema structures.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Setup/preparation monitors this flag and business locations, rebuilds location
metadata when needed, and rebuilds booking schema settings between single-location and
multi-location formats when the flag changes. Runtime location-analysis logic executes only when
this flag is enabled. Integration booking workflows also use this flag to switch between
single-value location settings and per-location mapped settings keyed by the active location. Some
integration setup workflows auto-enable this flag when business locations are configured.

**Fallbacks:** Default is `False` during common setup. If enabled while location definitions are
empty/incomplete, location switching can not operate reliably. Switching from `True` to `False`
keeps only the `default` location values for converted booking schemas, which can discard
location-specific data.

**Dependencies:**

- **Primary Settings:**
  - `project_business_locations`: Source location list used to build runtime location context.
  - `project_attributes_setting_booking_check_availability_payload_schema_template`: Converted
    between single-location and location-keyed forms when this flag changes.
  - `project_attributes_setting_booking_check_availability_validation_schema_template`: Converted
    between single-location and location-keyed forms when this flag changes.
  - `project_attributes_setting_booking_payload_schema_template`: Converted between single-location
    and location-keyed forms when this flag changes.
  - `project_attributes_setting_booking_meta_fields_schema_template`: Converted between
    single-location and location-keyed forms when this flag changes.
- **Logic Interactions:**
  - `project_attributes_setting_booking_check_availability_enabled`: Availability checks consume the
    active location-aware schema mode.
  - `project_attributes_setting_booking_enabled`: Booking flows consume the active location-aware
    schema mode.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_feature_flag_agent_language_instructions_v2`


**Title:** Feature Flag - Agent Language Instructions V2 [C]

**Description:**

```md
This advanced system configuration controls the newer Agent language-instruction block.

**Best Practice:** Keep this enabled for the current language behavior. Turn it off only as a
rollback switch if the Agent needs to use the previous language instructions while code remains
deployed.

Behavior by value:

- **Enabled (`True`)**: Shared language instructions include Agent Primary Language, secondary
  language allowlists, multilingual mode behavior, language anchoring/stability rules, Current
  conversation language prompt wording when that feature is enabled, and updated code-phrase /
  operational-phrase language rules.
- **Disabled (`False`)**: Core conversation prompts use the earlier broad-multilingual policy while
  retaining primary-language fallback, language stability, and the restricted-language list. Earlier
  food-ordering and outbound-call prompts instead match the user's apparent language immediately and
  apply only the restricted-language list. All legacy prompt branches ignore Agent Secondary
  Languages, Agent Multilingual, and Current conversation language prompt wording.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Prompt builders check
`project_attributes_private_feature_flag_agent_language_instructions_v2`, and only the exact value
`True` enables the newer instruction text. The flag affects core replies, fast and urgent replies,
code-phrases, conversation analysis, transfer constraints, voice-to-voice prompt updates,
food-ordering, and outbound-call language instructions. The newer branch reads Agent Primary
Language, Agent Secondary Languages, Agent Multilingual, and restricted languages, then applies
language anchoring and stability rules. Current conversation language wording is added only when
that advanced feature is also enabled and a runtime user is available.

The legacy core branch keeps an established conversation language, uses Agent Primary Language for
ambiguous initial input, and requires a clear switch signal. Legacy food-ordering and outbound-call
branches instead follow the user's apparent language immediately and return before reading primary,
secondary, or multilingual settings. This feature flag changes prompt wording only: it does not
delete stored runtime language state and does not stop current-language initialization or Language
Observer by itself.

**Fallbacks:** Default is `True` during common setup so existing rollout behavior stays active. Only
exact `True` enables the newer branch; `False`, a blank value, or any other value selects the legacy
prompt behavior.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Injected as an explicit primary-language line
    when requested by the newer instruction block. It is also the ambiguous-input fallback in the
    core legacy branch, but capability-specific legacy prompts can bypass it.
  - `project_representative_agent_secondary_languages`: Used only by the newer instruction block.
  - `project_representative_agent_multilingual`: Used by the newer instruction block for broad
    multilingual behavior.
  - `project_business_language_restricted_list`: Used by both legacy and newer instruction blocks.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_current_conversation_language`: This advanced system
    configuration adds runtime current-language prompt wording only when both feature flags are
    enabled. Its initialization and observer workflow do not depend on this V2 flag.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_feature_flag_current_conversation_language`


**Title:** Feature Flag - Current Conversation Language [C]

**Description:**

```md
This advanced system configuration enables the runtime current-conversation-language feature.

**Best Practice:** Keep this disabled until the Agent is ready to use the Language Observer and
runtime language state for replies, urgent messages, code-phrases, thoughts, and Voice prompts.

Behavior by value:

- **Enabled (`True`)**: New conversations initialize `current_conversation_language` from Agent
  Primary Language. The Language Observer can update that runtime language after
  `broadcast_analyze_conversation` for chat, phone, and webcall channels. When the newer Agent
  Language Instructions V2 configuration is also enabled, shared language instructions, urgent
  messages, code-phrases, thoughts, and user-scoped Voice prompt updates use Current conversation
  language. Connector initial prompts and other global-event prompt builds do not inject Current
  conversation language because they do not have a runtime user.
- **Disabled (`False`)**: The Language Observer does not run, runtime current-language attributes
  are not initialized or updated by this feature, and prompt language behavior follows the active V2
  or legacy instruction branch without Current conversation language wording.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime consumers check
`project_attributes_private_feature_flag_current_conversation_language`, and only the exact value
`True` is treated as enabled. At conversation start, the system initializes
`current_conversation_language` from Agent Primary Language and records its source, status, observer
turn counter, and audit state. Language Observer then receives the latest user message and
conversation memory after `broadcast_analyze_conversation`.

Before language detection runs, channel-specific gates reduce reactions to short or frequent
messages:

- In chat, every message needs at least four words and 16 characters. Before a language is
  confirmed, detection runs when the message has at least ten words or three turns have elapsed.
  After confirmation, it requires at least 12 words and four elapsed turns.
- In phone and webcall conversations, every message needs at least three words and 12 characters;
  after confirmation, it also needs at least five words.

After those gates, restricted or otherwise disallowed languages are rejected. A switch normally
requires confidence of at least `0.55` for the primary language, `0.75` for a configured secondary
language, or `0.92` for another language allowed by Agent Multilingual. An explicit switch request
can bypass these confidence cutoffs but cannot bypass the pre-generation gates or the requirement
that the utterance be classified as reliable. Observer results update the stored audit record. A
reliable observation of the current language with confidence of at least `0.75` can confirm the
language without switching; another allowed candidate can be marked tentative if a switch is not
accepted. An accepted switch records the new language, a confirmed status, and its observer source.

Current-language prompt wording has an additional gate: Agent Language Instructions V2 must also be
enabled. User-scoped prompt builders then read the stored language only when a runtime `user_id` is
available. Global-event prompt builds without a runtime user do not read stored current-language
state or inject Current conversation language wording; they use the active prompt branch's normal
primary/default language handling. Initialization and Language Observer continue to operate when
this flag is enabled even if Agent Language Instructions V2 is disabled.

**Fallbacks:** Default is `False` during common setup. If disabled after being enabled, existing
persona language state may remain stored but is ignored by the feature-gated prompt and observer
paths.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Initial and fallback language when the feature
    is enabled.
  - `project_representative_agent_secondary_languages`: Allowed secondary languages used by the
    Language Observer when the feature is enabled.
  - `project_representative_agent_multilingual`: Allows observer switching outside primary and
    secondary languages when the feature is enabled.
  - `project_business_language_restricted_list`: Prevents restricted languages from becoming the
    current conversation language.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_agent_language_instructions_v2`: This advanced system
    configuration must also be enabled before Current conversation language is injected into reply,
    urgent-message, thoughts, transfer, or Voice prompts. It does not gate initialization or
    Language Observer.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_feature_flag_booking_use_new_availability_formatted_response_processor`


**Title:** Feature Flag - Booking - Use New Availability Formatted Response Processor [C]

**Description:**

```md
This advanced system configuration selects which formatted-response availability processor is used
at runtime.

**Best Practice:** Turn this on only when your availability endpoint returns payloads compatible
with the newer formatted-response structure.

Behavior by value:

- **Enabled (`True`)**: Uses the newer formatted-response availability processor.
- **Disabled (`False`)**: Uses the legacy formatted-response availability processor.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Availability-receive flows check this flag when processing type is
`formatted_response` and route output parsing through either the new or legacy formatted-response
handler in system/project/default availability paths. Intercom-specific availability result handling
also uses this flag to choose between the new and legacy formatted-response processors.

**Fallbacks:** Default is `False` during common setup. In system/project/default availability paths,
if processing type is not `formatted_response`, this flag has no effect. If enabled against an
incompatible payload shape, availability interpretation can degrade and lead to missing/incorrect
slot context.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_processing_type`: Controls whether this
    feature-flag switch is applied in system/project/default availability paths.
  - `project_attributes_setting_booking_check_availability_type`: Determines which availability
    channel path applies the new-vs-legacy formatted-response processor decision.
- **Logic Interactions:**
  - `project_attributes_setting_time_format`: Parsed slot responses are later communicated using
    this configured time format.
  - `project_business_industry`: Restaurant-specific post-processing can run after
    formatted-response parsing.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_feature_flag_thoughts_genai_native_tools`


**Title:** Feature Flag - Thoughts - GenAI Native Tools [C]

**Description:**

```md
This advanced system configuration moves supported Voice GenAI voice-to-voice sessions from the
legacy "thoughts" pipeline to native provider tools.

**Best Practice:** Enable this only when the Agent is configured for Voice voice-to-voice with the
`genai` provider and you are ready for turn analysis to be handled through the injected native tool
instead of the legacy thoughts flow.

Behavior by value:

- **Enabled (`True`)**: Connector sync adds the `current_steps_analysis` native GenAI tool to the
  runtime tool set and skips the legacy thoughts-generation step for matching phone conversations.
- **Disabled (`False`)**: Connector sync excludes the native thoughts tool from the runtime tool
  set. Operator-authored GenAI tools still follow the normal GenAI tools toggle.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The standard feature-flag reader resolves this from
`project_attributes_private_feature_flag_thoughts_genai_native_tools`, and only the exact value
`True` is treated as enabled. During Voice connector sync, the system composes a runtime tool set
from the operator-authored GenAI tools plus the `current_steps_analysis` tool when this flag is
enabled. If the normal GenAI tools toggle is disabled but this flag is enabled, the runtime tool set
contains only `current_steps_analysis`. If both are enabled, the runtime tool set contains both the
operator-authored tools and `current_steps_analysis`. When disabled again, connector sync recomputes
the runtime tool set from the operator-authored tools only, or clears `genai_v2v_tools` to `[]` when
no runtime tools remain enabled.

When the advanced system configuration `project_attributes_private_feature_flag_v2v_native_tools`
has been successfully published, native voice sessions use on-demand context and intent tools
instead. Their toolbox excludes `current_steps_analysis`, even when this older thoughts flag is
enabled. The stored value of this flag is preserved and takes effect again for new calls after
native voice mode is disabled and published. Calls already running retain their selected mode.

**Fallbacks:** Default is `False` during common setup. If the voice channel is not Voice, the
conversation is not phone/v2v, the provider is not `genai`, or the connector does not expose
`genai_v2v_tools`, the observable effect is reduced or absent. Any value other than exact `True` is
treated as disabled.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_mode`: Must be `voice-to-voice` for
    the thoughts-skip runtime path to activate.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider`: Must be `genai`
    for the thoughts-skip runtime path to activate.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions`:
    Provides the operator-authored GenAI tools merged into the runtime tool set when the normal
    GenAI tools toggle is enabled.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`:
    Controls whether operator-authored GenAI tools participate in the runtime tool set.
- **Logic Interactions:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_description`:
    Provides operator-authored guidance merged into the runtime toolbox description when the normal
    GenAI tools toggle is enabled.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_feature_flag_email_universal_template`


**Title:** Feature Flag - Email - Universal SendGrid Template [C]

**Description:**

```md
This advanced system configuration selects the email-delivery pipeline used by the EmailWorker for
all outgoing emails (agent messages, session reports, booking notifications, disaster reports, and
internal dev alerts).

**Best Practice:** Enable this only once the universal SendGrid Dynamic Template and the backend
tenant resolution (from / logo / template id / API key) are deployed. Keep it disabled to retain the
legacy webhook delivery while rolling out.

Behavior by value:

- **Enabled (`True`)**: `SendEmailSkill` packages the email as a flat `body.fields` list and sends
  it through the SendGrid Dynamic Template via the `send_template_email` command on the
  `email_connector`.
- **Disabled (`False`)**: `SendEmailSkill` uses the legacy path: it appends the footer to the raw
  HTML body and sends it through the webhook `send_email` command.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The standard feature-flag reader resolves this from
`project_attributes_private_feature_flag_email_universal_template`, and only the exact value `True`
is treated as enabled. When enabled, `SendEmailSkill` builds template parameters from `params_json`
(the per-type builders' `body.fields`), injects header / footer / signature / audience metadata plus
the compiled signature, and dispatches `send_template_email` (provider `sendgrid`). When disabled,
it composes `arguments.body ~ _getFooterSkill(...)` and dispatches the legacy `send_email` webhook
command with `senderName` and `replyTo`.

**Fallbacks:** Default is `False` during common setup. Any value other than the exact value `True`
(including an unset attribute on an existing project) is treated as disabled, so existing projects
keep the legacy delivery until the flag is explicitly enabled.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_email_sender_name`: Supplies the `From` display name on both paths.
  - `project_attributes_private_dynamic_email_signature`: Compiled signature injected as the footer
    on the universal (`True`) path.
- **Logic Interactions:**
  - The universal path requires the SendGrid `email_connector`; the legacy path requires the webhook
    `send_email` connector. Both must be provisioned for the flag to be switchable at runtime.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_feature_flag_thoughts_step_state_tracing`


**Title:** Feature Flag - Thoughts - Step State Tracing [C]

**Description:**

```md
This advanced system configuration controls whether the Agent's internal conversation analysis
explicitly traces scenario-step progress before selecting its next directives. It is disabled by
default, so the Agent uses the legacy thoughts analysis unless an administrator enables tracing.

**Best Practice:** Keep this disabled for baseline behavior. Enable it in a controlled rollout when
you want to evaluate evidence-based step progression, repeated-question handling, and
wait-for-result gate tracking.

Behavior by value:

- **Enabled (`True`)**: Thoughts analysis must reconstruct the active scenario's step states,
  distinguish advancing from stalled progress, classify wait-for-result gates, and select a runway
  of up to four sequential valid directives.
- **Disabled (`False`)**: Thoughts analysis uses the legacy field-collection and directive format
  without mandatory step-state, progress, or gate sections.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The system checks this flag immediately before standard conversation-thoughts
generation. Thoughts generation can exit before this check when thoughts are deactivated for the
conversation, waiting mode is active, or a supported native voice-to-voice tool handles the analysis
instead. When checked, only exact `True` selects the step-state-tracing analysis; every other value
selects the legacy analysis.

The traced path marks scenario steps and result-dependent gates as `PENDING` or `DONE`, requires
direct evidence before marking completion, counts repeated asks to identify stalled progress, and
starts its directive runway at the first pending step. Steps after a pending gate can appear only as
conditional guidance and cannot be executed until the required result exists. The traced instruction
set lists the first pending step plus four later steps in step-state output and limits the
actionable directive runway to four sequential steps. Branch cases do not count toward that
four-step runway. Both analysis paths use the same conversation context and downstream thoughts
storage and delivery pipeline.

**Fallbacks:** Initialization sets an empty value to `False` and preserves an existing non-empty
value. The runtime reader enables tracing only for the exact value `True`; a missing, blank, or any
other value uses the legacy thoughts analysis.

**Dependencies:**

- **Logic Interactions:**
  - `project_attributes_private_feature_flag_thoughts_genai_native_tools`: This advanced system
    configuration routes supported phone-based GenAI voice-to-voice sessions to native analysis and
    bypasses standard thoughts generation when its required voice mode and provider are active.
  - `project_attributes_setting_voice_integration_service_voice_mode`: This advanced Voice
    configuration must select `voice-to-voice` for the native-analysis bypass.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider`: This advanced
    Voice configuration must select `genai` for the native-analysis bypass.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_feature_flag_v2v_native_tools`


**Title:** Feature Flag - Voice - Native Context and Intent Tools [C]

**Description:**

```md
This advanced configuration enables voice conversations to request context and scenario instructions
through native tools when needed. It reduces repeated system-prompt updates during a call.

**Best Practice:** Enable this for a pilot account and publish after changing the flag, canvas, or
custom tools. Check initialization logs for preparation errors before starting new test calls.

Behavior by value:

- **Enabled (`True`):** Publishing reconciles changed custom canvas items and prepares the native
  voice configuration. Successful preparation applies to new inbound, outbound, and web voice calls.
- **Disabled (`False`):** Successful publishing restores the base voice path. A skip-init publish
  restores saved connector values; a full initialization also synchronizes current account settings.
  Chat and non-voice conversations continue using their existing instruction path in either mode.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This flag requests a mode change; new calls use the last successfully applied
configuration, so editing the flag alone has no effect. Native preparation uses a separate candidate
canvas, completing its library dependencies without adding items to the saved canvas. Custom-item
reconciliation caches authored inputs separately from generated mentions and invalidates when the
canvas or dependency catalog changes. Library-only canvases skip language-model reconciliation.
Developers maintain one corrected library mentions graph for both modes. Tool schemas and guidance
are rebuilt and validated on every enabled publish. The developer-managed canvas is assumed to have
a valid structure and unique, non-empty entity IDs; native preparation does not validate these. The
model receives the current entity and all active-canvas dependencies with their IDs. Only
custom-item mentions in the candidate are replaced; the reconciler does not rewrite saved content.
Missing or ambiguous references prevent accepting the new configuration. Inline-only intents may
have no dependencies.

The runtime enables six managed tools: `define_intent`, `switch_intent`, `get_user_information`,
`get_current_time_and_working_hours`, `get_calendar`, and `get_business_information`. Intent ID
enums are built from the current canvas during publish. Enabled custom tools are merged without
changing their saved settings; managed definitions win name collisions. The older
`current_steps_analysis` tool is excluded while native mode is active. Automatic thoughts skip
native sessions. Each observer cycle selects knowledge-base articles and sends new ones as turn
context, regardless of the advanced system configuration
`project_attributes_private_feature_flag_v2v_prompt_mutation_optimization`;
`get_business_information` returns business facts only.

Each call captures the successfully applied resolved canvas, tools, guidance and prompt settings at
startup and retains them until it ends, including through later publishes or toggles. Scenario
attribute placeholders are resolved during preparation and are not reread by active calls. Outbound
dialing captures the same configuration for its initial instruction and startup. Current user
information, working hours, calendar and business information may still be retrieved through tools.
Intent switches return scenario and procedure dependencies through the tool response, including
nested references with cycle protection. They do not rebuild the system prompt. Initial setup and
explicit per-conversation instruction-selection changes may update the prompt. Existing action
execution and result delivery continue separately.

The compact native prompt omits global language-selection rules, OutputFormat, ExplicitConstraints,
and the long CurrentTaskAnalysis footer. Prior-interaction summaries, call metadata, custom prompt
sections, and SMS/email sendable-content lists are also omitted in this initial version. Authored
scenario instructions are preserved.

**Publish and restore:** The first native application saves five native-owned connector fields (tool
schema and four initial instructions) and the legacy tool metadata. Repeated native publishes retain
that baseline and add newly encountered connectors. Skip-init publishes modify only these five
fields. Full initialization synchronizes ordinary connector settings once before native overrides.
Disabling with skip-init restores the saved values; disabling with full initialization also
synchronizes current account attributes. The baseline is cleared after successful disabling.
Accounts that have never enabled the feature keep the immediate legacy publish-completion path.

**Fallbacks:** Defaults to `False`; only exact `True` requests preparation. An absent accepted
configuration means legacy mode, including when outbound is deployed before NAF. Invalid or
superseded preparation retains the previous accepted configuration and emits no successful
initialization-completion event. An empty connector-application result also retains the previous
accepted configuration and logs a preparation failure so publishing can be retried. Verified
connector-write failures attempt to restore the preceding native-owned values and retain the
baseline for retry. Malformed JSON or platform Action failures can abort the workflow; inspect logs
and publish again. Existing native pilot accounts without a saved baseline require separate
migration; this lifecycle covers future toggles.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_mode`: Requires a supported
    `voice-to-voice` or `speech-to-speech` conversation over the voice integration.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_workflow_builder_canvas`: Source of entities and mentions.
  - `project_attributes_private_dynamic_v2v_native_config`: Successfully applied configuration
    captured by inbound and outbound call startup.
  - `project_attributes_private_dynamic_v2v_native_connector_snapshot`: Saved values for disabling.
  - `project_attributes_private_feature_flag_thoughts_genai_native_tools`: Preserved but superseded
    for native voice sessions.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`:
    Controls participation of saved custom tools; managed tools remain enabled independently.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_feature_flag_v2v_prompt_mutation_optimization`


**Title:** Feature Flag - V2V Prompt Mutation Optimization [C]

**Description:**

```md
This advanced system configuration controls a coordinated set of Voice-to-Voice prompt-mutation
optimizations. The optimizations are enabled by default, and this flag provides one emergency
rollback switch for restoring the legacy session-level system prompt behavior in non-native voice
sessions. Native voice sessions continue receiving knowledge-base articles as turn context in either
setting.

**Best Practice:** Keep this enabled. Set it to `False` only as an emergency rollback if Voice
response quality, availability/RAG handling, or session behavior regresses.

Behavior by value:

- **Enabled (`True`)**: OpenAI and Grok Voice sessions keep changing current-call conversation
  history and current-task analysis out of the system prompt. All V2V providers receive the previous
  call as static `<PreviousConversation>` context when it is available. V2V sessions also keep RAG
  and waiting-mode instructions out of the system prompt; these are delivered as turn context
  instead. An identical compiled prompt does not trigger another session update.
- **Disabled (`False`)**: Non-native Voice sessions preserve the legacy system-prompt composition
  and update behavior. OpenAI and Grok receive conversation history and current-task analysis in the
  system prompt, RAG remains session-prompt content, waiting mode updates the session footer, and
  every requested session update is sent. Native voice sessions still receive newly selected
  knowledge-base articles as turn context on each observer cycle.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This flag affects Voice sessions using voice-to-voice or speech-to-speech mode.
When enabled, selected RAG article deltas, waiting-mode instructions are sent through turn-level
context messages. Their corresponding dynamic content is kept out of session prompt compilation, and
entering or timing out of waiting mode does not update the V2V system prompt. For returning callers,
history from before the latest completed call is included as static `<PreviousConversation>` context
for GenAI, OpenAI, and Grok; it does not grow during the active call. The runtime also compares each
newly compiled prompt with the last prompt sent for that user session and skips the update command
when they are identical. It does not disable ordinary urgent-message commands or the thoughts
pipeline. Native voice sessions prepare RAG on every observer cycle and send selected article deltas
through `set_turn_message` (a turn-context message command) regardless of this flag's value; their
`get_business_information` tool returns business facts only.

**Fallbacks:** Common initialization sets an empty value to `True`. An explicit `False` value is
preserved and restores legacy V2V behavior for non-native sessions; at runtime, only `True` enables
the flag-controlled optimizations. Native RAG turn-context delivery remains active with `False`.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_mode`: The optimization applies only
    to voice-to-voice and speech-to-speech sessions.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider`: Determines the
    active V2V provider and its turn-context role behavior.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_v2v_native_tools`: This advanced system configuration
    requests native voice mode on publish. Active native sessions deliver RAG as turn context
    independently of the prompt-mutation optimization flag.
  - `project_attributes_setting_booking_check_availability_enabled`: Availability context is
    relevant only when availability checking is enabled.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_set_turn_message_context_type`:
    Controls the role used for GenAI turn-context messages.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_feature_flag_rag_append_websites_use_native_web_search_tool`


**Title:** Feature Flag - RAG Append - Use Web Search [C]

**Description:**

```md
This internal customer feature flag selects the implementation used to append website content to RAG
knowledge.

**Enabled (`True`) - Native web search**

Selects the direct web-search tool instead of the scraper project for website retrieval.

Advantages:

- The existing input format supports custom `Crawl depth` for each submitted website.
- The scraper project and its external HTTP request lifecycle are bypassed.

Limitations and risks:

- Requests run sequentially. A later website is not retrieved until the current website has been
  retrieved.
- This is a best-effort path. It has no per-website retry, callback failure record, or automatic
  fallback to the scraper. If web search returns no content or fails, the user needs to request web
  extraction again or try scraper approach by setting the feature flag to `False`.

Observed behavior varies by website and objective:

- Native web search is usually cleaner and more focused on the requested objective, with less
  navigation, boilerplate, and repeated content. It can be stronger for dedicated services, pricing,
  financing, insurance, or treatment pages.
- The scraper can be more complete for menus, online ordering, product catalogs, family packages,
  and other pages where broad coverage of individual items matters.

**Disabled (`False`) - Asynchronous scraper project**

The scraper project parses the request, creates search queries per website, sends asynchronous
search and extract requests, and returns content through callbacks.

Advantages:

- Callback failures are recorded and retry/error handling is available in the scraper workflow.
- The scraper receives up to 20 search results per parsed website and deduplicates extracted URLs.
- It is better suited when operational visibility into scraping failures is required.

Limitations and risks:

- This mode depends on the external scraper service and callback delivery.
- It can return more broad or repeated page content than the native web-search path.

---

**Technical & System Details (Advanced)**

**System Usage:** The website append flow checks this attribute and treats only the exact value
`True` as enabled. The enabled path keeps the existing input format, separates multiple website
blocks, and makes one direct web-search extraction call per website. Native calls are sequential and
have no callback, retry queue, failed-website log entry, or scraper fallback.

**Fallbacks:** Default is `False` during common setup. Blank values and values other than exact
`True` use the scraper service. The native path does not retry or record individual web-search
failures.

**Dependencies:**

- `project_attributes_rag_knowledge_base_append_websites`: Provides the website blocks to ingest.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_llm_generated_scenarios`


**Title:** Dynamic - Workflow Builder - LLM-Generated Scenarios [C]

**Description:**

````md
This attribute stores reusable scenario bodies produced by LLM-based generation as a JSON object.
Each key identifies a generated scenario body, allowing industry workflows to store and reuse their
own generated content.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

Example structure:

```json
{
  "generated_scenario_body_idn": "Generated scenario body",
  "another_generated_scenario_body_idn": "Another generated scenario body"
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Scenario-building workflows read generated content from this shared store by key.
They can invoke the relevant generator when a requested body is missing, store the resulting content
here, and reuse it during later library builds. The object can contain generated scenario bodies for
any supported industry or workflow.

For generated sales consultation and partner-registration content, direct dependency mentions are
derived from the named calendar-booking, closing, phone, and email instructions in the saved body.
This keeps on-demand instruction retrieval aligned when the generated body is reused.

**Fallbacks:** Common initialization creates an empty JSON object. When a requested key is missing
or blank, the consuming workflow can invoke its configured generator and then read the generated
body from the updated object.

**Dependencies:**

- **Primary Settings:**
  - No direct customer-facing settings are required.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_workflow_builder_canvas_library`: Receives the stored
    scenario bodies when generation workflows include them as reusable library items.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_workflow_builder_canvas`


**Title:** Dynamic - Workflow Builder - Canvas [C]

**Description:**

````md
This advanced system configuration stores the current Workflow Builder canvas state used to
represent your intent/scenario/procedure structure.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Treat this as system-managed JSON and update it through Workflow Builder actions
instead of manual edits.

Example value:

```json
{
  "title": "Workflow Builder",
  "types": [
    {
      "idn": "intent_types",
      "items": []
    },
    {
      "idn": "scenarios",
      "items": []
    }
  ]
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Workflow-builder initialization sends this JSON to the builder UI, while
save/delete actions mutate it incrementally. Instruction-preparation logic uses this canvas to
derive ITM/AMI templates and trigger downstream instruction/ITM rebuild events. Report-intent
analysis logic also reads canvas intent/scenario definitions. Some module-specific follow-up flows
can edit the stored canvas after builder rebuild and then trigger instruction recompilation so
runtime instructions stay aligned.

Fresh default construction completes referenced scenarios and procedures recursively from the single
corrected library mentions graph in both modes. Library refresh updates selected library items while
preserving the customer's selections; deleted dependencies are not restored. Ordinary instruction
compilation uses selected item titles and bodies and strips mentions metadata.

When `project_attributes_private_feature_flag_v2v_native_tools` is enabled, publishing creates a
separate native candidate with completed library dependencies. Only custom-item mentions in that
candidate are reconciled by a language model; library mentions remain authoritative. The cache
compares authored canvas and catalog inputs, keeping generated results separately. Saved canvas IDs,
titles, bodies, selections and custom mentions are not changed by native preparation. Missing or
ambiguous dependencies reject the candidate. Successful calls use the accepted candidate captured at
startup.

**Fallbacks:** Initialized as a blank placeholder during common setup. If empty during instruction
preparation, the system generates a default canvas based on industry templates.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Selects default canvas content when initialization/rebuild is done
    from library templates.
- **Logic Interactions:**
  - `gm_prepare_instructions`: Event-driven rebuild path that initializes or refreshes this canvas.
  - `gm_build_instructions`: Event-driven path that compiles instructions from current canvas state.
  - `gm_prepare_itm`: Triggered after canvas-derived ITM templates are prepared.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_workflow_builder_canvas_backup`


**Title:** Dynamic - Workflow Builder - Canvas Backup [C]

**Description:**

````md
This advanced system configuration preserves the original Workflow Builder canvas before an
automated canvas upgrade changes it.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Keep this snapshot unchanged so it remains available if an automated canvas
change needs to be inspected or reversed.

Example value:

```json
{
  "title": "Workflow Builder",
  "types": [
    {
      "idn": "scenarios",
      "items": []
    }
  ]
}
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** At the start of the language-switch customization migration, the system copies the
complete existing canvas JSON into this attribute before parsing the canvas or asking the language
model to classify quoted text. The migration then reviews only custom Introduction, Scenario, and
Procedure items. An existing non-empty backup is preserved so a retried migration cannot replace the
original snapshot.

The classifier is instructed to select complete direct User-facing wording and leave quotes
containing Agent instructions unchanged. A second LLM pass reviews every extracted candidate under
the same rules before any canvas replacement, including when the first pass selects none.
Corrections must reference an existing candidate and include its complete candidate marker as
evidence, which binds the correction to that exact quoted occurrence. Whitespace and quote-style
differences are ignored during citation validation. Suggested wording remains excluded even when the
action is required, while examples inside a required spoken phrase do not make that phrase optional.
Invalid, duplicate, and redundant corrections are ignored.

**Fallbacks:** It remains empty when there is no existing canvas to preserve or the migration has
not run. If the migration finds no extracted candidate, the snapshot is still retained. A malformed
classifier response is treated as an empty selection, while a malformed review response leaves the
classifier selection unchanged. If neither pass produces a valid selection, the stored canvas
remains unchanged. Model review does not guarantee correct classification and cannot recover phrases
missed during deterministic extraction.

**Dependencies:**

- **Primary Settings:**
  - No direct customer-facing settings are required.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_workflow_builder_canvas`: Provides the original canvas JSON
    stored in the backup.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_workflow_builder_canvas_library`


**Title:** Dynamic - Workflow Builder - Canvas Library [C]

**Description:**

````md
This advanced system configuration stores the compiled library of reusable Workflow Builder
components shown in the canvas editor.

It combines default system templates with your custom library entries so reusable blocks can be
selected consistently.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Treat this as system-managed JSON and update library items through builder
actions/events instead of manual edits.

Example structure:

```json
[
  {
    "idn": "introduction",
    "title": "Introduction",
    "color": "#45556C",
    "items": []
  },
  {
    "idn": "intent_types",
    "title": "Intent Types",
    "color": "#E60076",
    "items": []
  }
]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Instruction-preparation routines rebuild this compiled library from industry
defaults plus custom entries. Workflow Builder initialization publishes the current compiled library
to the `workflow_builder` connector via `update_library`. Canvas refresh and procedure-mapping logic
read this compiled library to keep library-based items aligned with current definitions.

**Fallbacks:** Initialized as blank/whitespace in common setup. If custom library data is empty, the
system auto-seeds empty custom containers and still builds a full default library by industry.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Selects default template items that seed the compiled library.
- **Logic Interactions:**
  - `gm_prepare_instructions`: Rebuilds the library before canvas/instruction preparation.
  - `gm_canvas_add_library_item`: Adds or updates custom entries, then recompiles the library.
  - `gm_canvas_delete_library_item`: Removes custom entries, then recompiles the library.
  - `gm_workflow_builder_library_built`: Emitted after library compilation for downstream handling.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_workflow_builder_canvas_library_custom`


**Title:** Dynamic - Workflow Builder - Canvas Library - Custom [C]

**Description:**

````md
This advanced system configuration stores the custom library layer for Workflow Builder components.

It contains user- or integration-created items that are merged into the compiled library used by the
builder UI.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

**Best Practice:** Use library add/delete operations (UI or system events) instead of manual JSON
editing so merge and rebuild logic runs correctly.

Example structure:

```json
[
  {
    "idn": "introduction",
    "items": []
  },
  {
    "idn": "procedures",
    "items": []
  }
]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Library-item save actions mutate this JSON by type (`introduction`,
`intent_types`, `scenarios`, `procedures`), then rebuild the compiled library, refresh
library-backed canvas items, and rebuild instructions. Delete actions remove items from this custom
JSON and rebuild the compiled library, but they do not refresh canvas items or rebuild instructions
in the same controller path.

**Fallbacks:** Initialized as blank/whitespace in common setup. On first library preparation with an
empty value, the system auto-creates the four standard type containers with empty `items`.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines which default templates this custom layer is merged
    with.
- **Logic Interactions:**
  - `gm_prepare_instructions`: Rebuild path that prepares library/canvas state before instruction
    compilation.
  - `gm_canvas_add_library_item`: Inserts or updates custom entries (including batch variant).
  - `gm_canvas_delete_library_item`: Removes custom entries by type and item ID (including batch
    variant).
  - `gm_build_instructions`: Rebuild path that consumes post-merge library/canvas state.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_external_reply_type`


**Title:** Conversation - External Reply Type Handling [C]

**Description:**

```md
This advanced setting controls whether the built-in external reply handler stays active.

Use it to choose between the standard external reply path and your own custom outbound delivery
flow.

Behavior by value:

- **`default`:** The built-in external reply handler stays active.
- **`custom`:** The built-in external reply handler exits immediately so a custom flow can take
  over.

**Best Practice:** Keep `default` unless you already have a complete custom outbound delivery
pipeline and monitoring in place.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** External reply generation can emit the `send_external_reply` system event. When
this setting is `default`, the built-in handler reads the conversation source from persona data and
sends supported ManyChat replies. When this setting is `custom`, the handler returns without
dispatching a built-in reply.

**Fallbacks:** Common settings initialization sets the default value to `default`. If the source
resolves to ManyChat but `project_attributes_setting_manychat_api_token` is empty, the ManyChat
sender logs the issue and skips the request. Unknown external sources are also logged and skipped.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_manychat_api_token`: Required for built-in ManyChat outbound
    dispatch.
- **Logic Interactions:**
  - `send_external_reply`: System event that triggers external reply handling.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `enum`

**Possible values:** `["default", "custom"]`

**Is hidden:** `true`

---

## `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions`


**Title:** Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) [C]

**Description:**

````md
This advanced setting stores the JSON function (tool) definitions for GenAI voice-to-voice
integrations.

It defines the callable tool names and parameter schemas that can be synchronized to supported
voice-to-voice connectors.

**Best Practice:** Keep this as a valid JSON array and update it together with the tool description
attribute so runtime tool contracts and prompt instructions stay aligned. Leave it as `[]` when you
do not need shared global voice tools.

**Examples:**

```json
[
  {
    "name": "send_full_name",
    "description": "Send full name",
    "parameters": {
      "properties": {
        "first_name": {
          "type": "STRING",
          "description": "First name"
        },
        "last_name": {
          "type": "STRING",
          "description": "Last name"
        }
      },
      "required": ["first_name", "last_name"],
      "type": "OBJECT"
    }
  },
  {
    "name": "send_phone_number",
    "description": "Send phone number",
    "parameters": {
      "properties": {
        "phone_number": {
          "type": "STRING",
          "description": "Phone number"
        }
      },
      "required": ["phone_number"],
      "type": "OBJECT"
    }
  },
  {
    "name": "send_email",
    "description": "Send email",
    "parameters": {
      "properties": {
        "email": {
          "type": "STRING",
          "description": "Email"
        }
      },
      "required": ["email"],
      "type": "OBJECT"
    }
  },
  {
    "name": "send_appointment_type",
    "description": "Send appointment type",
    "parameters": {
      "properties": {
        "appointment_type": {
          "type": "STRING",
          "description": "Email"
        }
      },
      "required": ["appointment_type"],
      "type": "OBJECT"
    }
  },
  {
    "name": "send_date_and_time",
    "description": "Send date and time",
    "parameters": {
      "properties": {
        "date_and_time": {
          "type": "STRING",
          "description": "Date and time"
        }
      },
      "required": ["date_and_time"],
      "type": "OBJECT"
    }
  },
  {
    "name": "send_number_of_people",
    "description": "Send number of people",
    "parameters": {
      "properties": {
        "number_of_people": {
          "type": "STRING",
          "description": "Number of people"
        }
      },
      "required": ["number_of_people"],
      "type": "OBJECT"
    }
  },
  {
    "name": "send_date_of_birth",
    "description": "Send date of birth",
    "parameters": {
      "properties": {
        "date_of_birth": {
          "type": "STRING",
          "description": "Date of birth"
        }
      },
      "required": ["date_of_birth"],
      "type": "OBJECT"
    }
  },
  {
    "name": "send_company_name",
    "description": "Send company name",
    "parameters": {
      "properties": {
        "company_name": {
          "type": "STRING",
          "description": "Company name"
        }
      },
      "required": ["company_name"],
      "type": "OBJECT"
    }
  },
  {
    "name": "send_website_link",
    "description": "Send website link",
    "parameters": {
      "properties": {
        "website_link": {
          "type": "STRING",
          "description": "Website link"
        }
      },
      "required": ["website_link"],
      "type": "OBJECT"
    }
  }
]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This JSON is the operator-authored source list for voice GenAI tools. During Voice
connector synchronization, the system copies it into a runtime-composed tool set only when the
tools-enabled toggle is `True`; native thoughts tooling can add an additional system-managed tool to
that runtime set without mutating this JSON.

With successfully published `project_attributes_private_feature_flag_v2v_native_tools`, enabled
operator-authored tools and guidance are merged into the native toolbox. The six managed tools take
precedence on name collisions, and `current_steps_analysis` is excluded. The system does not rewrite
these operator-authored settings. A skip-init disable restores saved connector values; a full-init
disable recomposes ordinary tools from current account settings. Native voice mode uses the
successfully applied toolbox captured for each supported voice call.

**Fallbacks:** Common settings initialization leaves this attribute as an empty array (`[]`).

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`:
    Enables/disables whether this operator-authored JSON participates in the runtime tool set.
- **Logic Interactions:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_description`:
    Human-readable tool guidance should match this JSON contract.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_voice_integration_service_voice_to_voice_provider_genai_functions`


**Title:** Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) Runtime
[C]

**Description:**

```md
This system-managed attribute stores the effective voice GenAI tool schema used by runtime and
connector sync.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

Behavior by value:

- **Empty array (`[]`):** No voice GenAI tools are currently active in the runtime tool set.
- **One or more tool schemas:** Connector sync writes these schemas to `genai_v2v_tools` when the
  runtime tools-enabled value is active.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Voice connector sync composes this JSON from
`project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions` when
`project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`
is `True`. When the advanced system configuration
`project_attributes_private_feature_flag_thoughts_genai_native_tools` is enabled, connector sync
also adds the `current_steps_analysis` native tool. If the operator-authored tools are disabled and
the feature flag is enabled, this value contains only that native tool.

Native tool schemas are stored separately in `project_attributes_private_dynamic_v2v_native_config`.
Native application does not overwrite this legacy value. A skip-init disable restores its saved
baseline; a full-init disable recomputes it through ordinary connector sync using the current
account settings.

**Fallbacks:** Common setup initializes this value to an empty array (`[]`). Connector sync rewrites
it to the latest composed value whenever connector setting `genai_v2v_tools` is available.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions`:
    Provides the operator-authored base schemas.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`:
    Controls whether the operator-authored base schemas participate in this composed runtime value.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_thoughts_genai_native_tools`: Adds the native
    `current_steps_analysis` schema to this composed value when enabled.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `json`

**Is hidden:** `true`

---

## `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_description`


**Title:** Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools)
Description [C]

**Description:**

````md
This advanced setting stores the operator-authored text instructions that explain how voice-to-voice
tools should be used.

It gives the Agent a human-readable toolbox guide that complements the structured JSON tool schema.

**Best Practice:** Keep each instruction mapped to the exact tool name in your JSON schema so the
Agent’s reasoning instructions and callable tool definitions remain consistent. Leave this blank
when you do not need operator-authored global tool instructions. The toolbox section header and
system-managed native thoughts guidance are composed separately at runtime, so do not add them here
manually.

**Examples:**

```txt
- Send full name as soon as the User is providing it verbally using the function (tool) called `send_full_name`.
- Send phone number as soon as the User is providing it verbally using the function (tool) called `send_phone_number`.
- Send email as soon as the User is providing it verbally using the function (tool) called `send_email`.
- Send appointment type as soon as the User is providing it verbally using the function (tool) called `send_appointment_type`.
- Send date and time as soon as the User is providing it verbally using the function (tool) called `send_date_and_time`.
- Send number of people as soon as the User is providing it verbally using the function (tool) called `send_number_of_people`.
- Send date of birth as soon as the User is providing it verbally using the function (tool) called `send_date_of_birth`.
- Send company name as soon as the User is providing it verbally using the function (tool) called `send_company_name`.
- Send website as soon as the User is providing it verbally using the function (tool) called `send_website_link`.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This text is the operator-authored source for voice GenAI toolbox guidance.
Connector sync copies it into a runtime-composed toolbox description only when the tools-enabled
toggle is `True`; native thoughts tooling can add additional system-managed guidance to that runtime
description without mutating this text. Conversation prompt-building reads the composed value for
GenAI `voice-to-voice` sessions; `speech-to-speech` uses its separate native voice connector path
and does not use this voice-to-voice toolbox prompt path.

With successfully published `project_attributes_private_feature_flag_v2v_native_tools`, enabled
operator-authored tools and guidance are merged into the native toolbox. The six managed tools take
precedence on name collisions, and `current_steps_analysis` is excluded. The system does not rewrite
these operator-authored settings. A skip-init disable restores saved connector values; a full-init
disable recomposes ordinary tools from current account settings. Native voice mode uses the
successfully applied toolbox captured for each supported voice call.

**Fallbacks:** Common settings initialization keeps this operator-authored source blank.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions`:
    Structured schema this text should describe.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`:
    Controls whether this operator-authored guidance participates in the runtime toolbox
    description.
````

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_voice_integration_service_voice_to_voice_provider_genai_functions_description`


**Title:** Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) Runtime
Description [C]

**Description:**

```md
This system-managed attribute stores the effective voice GenAI toolbox instructions used at runtime.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

Behavior by value:

- **Empty value:** No toolbox guidance is currently active in the runtime prompt.
- **Text present:** Runtime prompt-building injects this composed toolbox guidance when the runtime
  tools-enabled value is active.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Voice connector sync starts this composed text with the toolbox section header,
then appends
`project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_description`
when
`project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`
is `True`. When the advanced system configuration
`project_attributes_private_feature_flag_thoughts_genai_native_tools` is enabled, connector sync
also appends the `current_steps_analysis` native-tool guidance.

Legacy voice and Thoughts prompts read this published value, preserving custom whitespace and
connector availability behavior. Unpublished authored-setting changes do not alter their toolbox
guidance. Native guidance is stored separately in
`project_attributes_private_dynamic_v2v_native_config` and captured per call. A skip-init disable
restores the saved legacy value; a full-init disable recomputes it through ordinary connector sync.

**Fallbacks:** Common setup initializes this value with the toolbox section header:
`**GLOBAL FUNCTIONS / TOOLS APPLICABLE TO ALL SCENARIOS / PROCEDURES:**`. Connector sync rewrites it
to the latest composed value whenever connector setting `genai_v2v_tools` is available.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_description`:
    Provides the operator-authored base guidance.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`:
    Controls whether the operator-authored base guidance participates in this composed runtime
    value.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_thoughts_genai_native_tools`: Adds the native
    `current_steps_analysis` guidance to this composed value when enabled.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`


**Title:** Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) Enabled
[C]

**Description:**

```md
This advanced toggle enables or disables operator-authored GenAI function (tool) usage for
`voice-to-voice` sessions.

Use it to control whether the system includes your configured GenAI tools in the runtime voice tool
set. System-managed native tools can still be activated by their own feature flags.

Behavior by value:

- **Enabled (`True`):** Operator-authored tool schemas/instructions participate in the runtime voice
  tool set.
- **Disabled (`False`):** Operator-authored tool schemas/instructions are excluded from the runtime
  voice tool set. System-managed native tools may still make the runtime tool set active.

**Best Practice:** Turn this on only after tool schemas and corresponding runtime handling are fully
validated for your voice-to-voice flow.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This flag controls whether the operator-authored GenAI tools and descriptions are
copied into runtime-composed tool settings during connector sync. Prompt assembly and connector
`genai_v2v_tools` use those runtime-composed settings, which may also include system-managed native
tools from feature flags. The conversation toolbox path is used only for GenAI `voice-to-voice`
sessions; `speech-to-speech` uses its separate native voice connector path and does not use this
voice-to-voice toolbox prompt path.

With successfully published `project_attributes_private_feature_flag_v2v_native_tools`, enabled
operator-authored tools and guidance are merged into the native toolbox. The six managed tools take
precedence on name collisions, and `current_steps_analysis` is excluded. The system does not rewrite
these operator-authored settings. A skip-init disable restores saved connector values; a full-init
disable recomposes ordinary tools from current account settings. Native voice mode uses the
successfully applied toolbox captured for each supported voice call.

**Fallbacks:** Default is `False` in common settings.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions`:
    Operator-authored structured tool contract included in the runtime tool set only when enabled.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_description`:
    Operator-authored toolbox guidance included in the runtime toolbox description only when
    enabled.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_private_dynamic_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`


**Title:** Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) Runtime
Enabled [C]

**Description:**

```md
This system-managed attribute stores whether any voice GenAI tools are active in the runtime tool
set.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

Behavior by value:

- **Enabled (`True`):** Connector sync has prepared an active tool set in `genai_v2v_tools`.
- **Disabled (`False`):** Connector sync has cleared `genai_v2v_tools` to `[]`.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Voice connector sync sets this value to `True` when either
`project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`
is `True` or the advanced system configuration
`project_attributes_private_feature_flag_thoughts_genai_native_tools` is enabled. It is set to
`False` in base mode when both operator-authored GenAI tools and native thoughts tooling are
inactive. Legacy voice and Thoughts prompts use this published value for toolbox availability,
including the original connector-availability checks. Native application does not force this legacy
value to `True`; native tools are described in the separate accepted configuration. A skip-init
disable restores the saved baseline, while a full-init disable recomputes it through ordinary
connector sync. Active native calls retain their startup configuration until they end.

**Fallbacks:** Common setup initializes this value to `False`. Connector sync rewrites it to the
latest composed value whenever connector setting `genai_v2v_tools` is available.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled`:
    Enables operator-authored GenAI tools in the composed runtime value.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_thoughts_genai_native_tools`: Enables the native
    `current_steps_analysis` tool in the composed runtime value.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_set_turn_message_context_type`


**Title:** Voice - Integration Service - Voice To Voice Provider - GenAI - Set Turn Message Context
Type [C]

**Description:**

```md
This advanced setting controls which message role is used when context is injected into GenAI
`voice-to-voice` turns.

Use it to define whether injected context is sent as `user` or `assistant` role in
`set_turn_message` context updates.

Behavior by value:

- **`user`:** Context is injected using the user role for GenAI voice context turns.
- **`assistant`:** Context is injected using the assistant role for GenAI voice context turns.

**Best Practice:** Keep this aligned with your GenAI prompt strategy and test with live voice calls
before changing globally.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** GenAI context-injection paths read this attribute before sending a
`set_turn_message` command with `turnComplete=False`. The same role decision is used both by direct
voice-context updates and by the `convoagent_send_context` event path.

**Fallbacks:** Common settings initialization sets the default value to `user`. If the current
voice-to-voice provider is not `genai`, context injection falls back to the `assistant` role instead
of reading this attribute.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_set_turn_message_type`:
    Companion advanced configuration for command-role routing in the same GenAI voice-to-voice flow.
- **Logic Interactions:**
  - `convoagent_send_context`: Event-driven context injection path that uses this role decision.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `enum`

**Possible values:** `["assistant", "user"]`

**Is hidden:** `true`

---

## `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_set_turn_message_type`


**Title:** Voice - Integration Service - Voice To Voice Provider - GenAI - Set Turn Message Type [C]

**Description:**

```md
This advanced setting controls which message role is used when command instructions are sent to
GenAI `voice-to-voice` sessions.

It determines how command turns are delivered in `set_turn_message` calls for the GenAI provider.

Behavior by value:

- **`user`:** Sends command turns through the user-role command path.
- **`assistant`:** Sends command turns through the assistant-role command path.

**Best Practice:** Keep `user` unless you have validated that assistant-role command turns improve
your provider behavior in production-like voice sessions.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** GenAI command-dispatch logic checks this attribute and routes to user-role or
assistant-role command senders accordingly. Both senders deliver the same command text through
`set_turn_message`, while the assistant-role path marks the turn complete.

**Fallbacks:** Common settings initialization sets the default value to `user`. This role selector
is consulted only when the current voice-to-voice provider resolves to `genai`.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_set_turn_message_context_type`:
    Companion advanced configuration for context-role routing in the same GenAI voice-to-voice flow.
- **Logic Interactions:**
  - `set_turn_message`: Voice command used to deliver the final command turn to the active GenAI
    connector.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `enum`

**Possible values:** `["user", "assistant"]`

**Is hidden:** `true`

## Project Attributes

---

## `project_attributes_setting_init_attributes_metadata_enabled`


**Title:** Project - Init - Setting-Up Attributes Metadata - Enabled [C]

**Description:**

```md
This advanced setting controls whether core Attribute metadata is rewritten during a manual publish.
Attribute metadata defines the titles, descriptions, value types, groups, and visibility rules shown
in the Attributes UI.

**Best Practice:** Leave this setting disabled during normal operation. When core Attribute metadata
must be refreshed, an advanced user can enable it in the Attribute-management UI and then run a
manual publish. The system returns the setting to `False` during post-setup.

**Examples:**

- **Enabled (`True`) before a manual core Project publish:** The publish rewrites core Attribute
  metadata, and post-setup resets this setting to `False`.
- **Disabled (`False`) before a manual core Project publish:** The publish skips the resource-heavy
  core metadata writes.
- **Non-manual core Project initialization:** Metadata setup can run when this setting is `False`
  once the initialization path reaches the metadata phase.
- **Module initialization:** Module-specific metadata setup runs independently and does not consult
  this setting.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Core metadata setup receives the `triggered_by` argument from
`project_publish_finish`, the event that starts Project initialization and identifies why it ran.
For a manual publish, metadata writes run only when this setting is `True`. For a non-manual
trigger, such as account creation, automatic update, or reinitialization, this setting does not
block core metadata setup once initialization reaches that phase. Module-specific metadata setup
neither reads nor initializes this setting. Core post-setup resets the setting to `False` after the
metadata phase, whether guarded metadata writes ran or were skipped.

**Fallbacks:** Core Project initialization sets this setting to `True` when it does not yet have a
value, allowing initial setup to populate core Attribute metadata. Module initialization does not
create or use this fallback.

**Dependencies:**

- **Logic Interactions:**
  - `project_publish_finish`: Provides the publish trigger context used to distinguish manual
    publishes from non-manual initialization paths.
```

**Level:** `Project`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_init_on_auto_update_enabled`


**Title:** Project - Init - Initialization Process On Auto-Update - Enabled [C]

**Description:**

```md
This setting controls whether the initialization process will take place during automatic updates.

Typically, this should be set to `True` to ensure that all necessary initialization steps are
performed during updates.

Value is being set to `False` when new version released which does not require initialization
process to be run.
```

**Level:** `Project`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_rag_append_website_search_request_url`


**Title:** Project - RAG Append - Website Search Request URL [C]

**Description:**

```md
Internal endpoint used by the website-search request service that powers the General Manager's RAG
website append flow.

Keep the default value unless support or engineering explicitly instructs you to change it.
```

**Level:** `Project`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_vibe_knowledge_base_search_url`


**Title:** Project - Vibe Agent - Knowledge Base Search URL [C]

**Description:**

```md
Internal endpoint used by `VibeAgent` when the `search_knowledge_base` action queries the platform
knowledge base.

Keep the default value unless support or engineering explicitly instructs you to change it.
```

**Level:** `Project`

**Group:** `8. System`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_vibe_loop_max_depth`


**Title:** Project - Vibe Agent - Loop Max Depth [C]

**Description:**

```md
Maximum number of internal `VibeAgent` loop iterations allowed for one user request before the agent
is restricted to `reply`, so it must summarize the information found, the actions already applied,
and the next best steps.

Values above `199` are capped to `199`.

Keep the default value unless support or engineering explicitly instructs you to change it.
```

**Level:** `Project`

**Group:** `8. System`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_attributes_setting_vibe_main_reasoning_effort`


**Title:** Project - Vibe Agent - Main Reasoning Effort [C]

**Description:**

```md
Controls how much reasoning the configuration Agent uses when deciding the next action in its main
work loop. Higher effort can improve difficult planning decisions, but it also increases response
latency and token cost.

**Pro-Tip:** Keep `medium` as the balanced default. Use `minimal` or `low` only when latency and
cost matter more than planning depth, and raise the value only after representative evaluations show
a meaningful quality improvement.

**Examples:**

- **`none`:** Minimizes reasoning for the fastest, lowest-cost decisions; this is not recommended
  for normal multi-step configuration work.
- **`minimal`:** Uses the smallest nonzero reasoning level for simple decisions where some
  deliberate reasoning is still useful.
- **`low`:** Favors speed and cost efficiency for simpler decisions.
- **`medium`:** Balances planning quality, latency, and cost for typical requests.
- **`high` or `xhigh`:** Allocates more reasoning to unusually difficult planning tasks and can
  substantially increase latency and cost.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** On every main-loop iteration, the configured `reasoning_effort` value is passed to
the LLM call that selects the next action and its parameters. The platform translates this ordinal
effort level into the provider-specific reasoning control.

**Fallbacks:** New projects initialize this setting to `medium`. If the value is empty or is not one
of the supported enum values, the runtime also uses `medium`.
```

**Level:** `Project`

**Group:** `8. System`

**Value type:** `enum`

**Possible values:** `["none", "minimal", "low", "medium", "high", "xhigh"]`

**Is hidden:** `true`

---

## `project_attributes_setting_vibe_project_init_timeout_seconds`


**Title:** Project - Vibe Agent - Project Initialization Timeout [C]

**Description:**

```md
Maximum time, in seconds, that the configuration Agent waits for a newly installed module to report
that initialization finished.

**Pro-Tip:** Keep enough time for integrations that perform external setup during initialization.
Short values can produce an unconfirmed result even when initialization completes later.

**Examples:**

- A completion signal received before the timeout confirms that the module initialized.
- When the timeout expires first, the Agent refreshes installation state and reports that the
  project should have published but initialization remains unconfirmed.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** After `PublishProject` is requested, the Agent waits for the matching
`project_init_finish` lifecycle event. The event confirms that the installed Project completed its
initialization path. A timeout triggers catalog discovery but does not by itself mean initialization
failed; an installed Project record confirms only that the Project exists.

**Fallbacks:** Empty, non-numeric, zero, and negative values use the built-in five-minute timeout.
```

**Level:** `Project`

**Group:** `8. System`

**Value type:** `number`

**Is hidden:** `true`

---
