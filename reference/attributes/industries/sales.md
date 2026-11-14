# Sales Industry Customer and Project Attributes Metadata

## Customer Attributes

### 4. Agent Behavior

#### `project_attributes_sales_after_appointment_notes`

**Title:** 4-20. After Appointment Notes [B]

**Description:**

````md
Define the follow-up notes the Agent should share after the user confirms appointment booking.

**Pro-Tip:** Keep this concise and operational (what happens next, how to reschedule, and any
preparation reminders).

**Examples:**

```txt
Feel free to call me if you would need to reschedule the appointment.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into sales appointment scenarios and delivered after successful booking
completion paths.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_sales_after_appointment_notes`. If empty, setup uses a neutral placeholder.

**Dependencies:**

- **Primary Settings:**
  - None. This attribute does not require another customer-facing setting before it can be
    initialized or used.
- **Logic Interactions:**
  - `agent_creator_sales_after_appointment_notes`: First-init source used to prefill this attribute.
  - `project_attributes_setting_calendar_event_integration`: Calendar-based appointment scenario
    also uses these notes in the success branch.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_sales_appointment_via_link_guidance_instruction`

**Title:** 4-21. Appointment Setting - Self-schedule Link (URL) - Guidance Instruction [B]

**Description:**

```md
Define the exact guidance the Agent should read while helping users complete self-scheduling through
the sales appointment link.

**Best Practice:** Write this as sequential, form-specific steps that match what users see on the
page.

**Examples:**

- "Open the link, complete your contact details, choose date/time, and submit the form."

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Inserted into the sales "Appointment Setting via Link" scenario at the step where
the user opens the link and needs guidance.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_sales_appointment_via_link_guidance_instruction`. If empty, setup uses a neutral
placeholder.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_sales_appointment_url`: Expected companion setting for this flow; the agent
    shares the appointment link before applying this guidance.
- **Logic Interactions:**
  - `agent_creator_sales_appointment_via_link_guidance_instruction`: First-init source used to
    prefill this attribute.
  - `project_attributes_sales_after_appointment_notes`: Used later in the same booking flow after
    completion.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_sales_appointment_url`

**Title:** 4-22. Appointment Setting - Self-schedule Link (URL) [A] [IMPORTANT]

**Description:**

```md
Set the URL where users can self-schedule a sales appointment.

**Best Practice:** Use a direct scheduling URL and verify it opens to the exact booking form. If
online booking is not available, leave this field empty.

**Examples:**

- `https://calendar.yourcompany.com/book`
- `https://yourcompany.com/schedule-demo`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Stored in sales business context and sales technical variables so the appointment
link is available to runtime messaging and appointment-link guidance flows.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_sales_appointment_url`. If it stays empty, link-sharing flows have no booking URL to
send.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_sales_appointment_via_link_guidance_instruction`: Instructions used after
    this link is shared in the self-scheduling flow.
- **Logic Interactions:**
  - `agent_creator_sales_appointment_url`: First-init source used to prefill this attribute.
  - `project_attributes_sales_after_appointment_notes`: Used later in the same link-based booking
    journey after the user completes self-scheduling.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_sales_pre_sale_questions`

**Title:** 4-23. Pre-Sale Notes [B]

**Description:**

````md
Define the consultation questions/prompts the Agent should use during the pre-sale stage.

**Pro-Tip:** Keep these focused on pain points, current setup, urgency, and readiness to act.

**Examples:**

```txt
- Have you ever tried any other AI Employee solutions?
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected directly into the "Pre-Sale Consultation" sales scenario.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_sales_additional_questions`. If empty, setup uses a neutral placeholder.

**Dependencies:**

- **Primary Settings:**
  - None. This attribute does not require another customer-facing setting before it can be
    initialized or used.
- **Logic Interactions:**
  - `agent_creator_sales_additional_questions`: First-init source used to prefill this attribute.
  - None. Qualification settings are evaluated in separate sales scenarios and are not read as part
    of this field's runtime evaluation.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_sales_qualifying_criteria`

**Title:** 4-24. Qualification Criteria [B]

**Description:**

````md
Define the rules the Agent should use to decide whether a lead is qualified for the sales path.

**Best Practice:** Write clear pass/fail rules that map directly to your qualification questions.

**Examples:**

```txt
- If the User is not a founder, the User does NOT qualify.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Evaluated in the "Lead Qualification" scenario after the Agent collects qualifying
answers.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_sales_qualifying_criteria`. If empty, setup uses a neutral placeholder.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_sales_qualifying_questions`: Criteria should be evaluated against answers to
    these questions.
  - `project_attributes_sales_qualifying_criteria_fallback_action`: Used when criteria are not met
    or user refuses required criteria.
- **Logic Interactions:**
  - `agent_creator_sales_qualifying_criteria`: First-init source used to prefill this attribute.
  - None. This field is evaluated within the lead-qualification scenario without direct runtime
    reads from additional sales attributes.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_sales_qualifying_criteria_fallback_action`

**Title:** 4-25. Action On Qualification Failure [B]

**Description:**

````md
Define what the Agent should do when a lead does not pass qualification.

**Pro-Tip:** Make this action explicit and operational (relay, handoff, polite close, or alternate
route).

**Examples:**

```txt
The agent starts the scenario: **Relaying Message to the Manager**.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Triggered by the lead-qualification scenario whenever criteria are unmet or
refused.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_sales_qualifying_criteria_fallback_action`. If empty, setup uses a neutral
placeholder that effectively disables fallback routing.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_sales_qualifying_criteria`: Determines when fallback action is triggered.
- **Logic Interactions:**
  - `agent_creator_sales_qualifying_criteria_fallback_action`: First-init source used to prefill
    this attribute.
  - `project_attributes_sales_qualifying_questions`: Supplies the answer set used before fallback
    decision.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_sales_qualifying_questions`

**Title:** 4-26. Qualification Questions [B]

**Description:**

````md
Define the question set the Agent should ask during lead qualification.

**Best Practice:** Ask one question per message and ensure every question ties directly to a
qualification criterion.

**Examples:**

```txt
- Do you want to increase your sales with us?
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used in the "Lead Qualification" scenario where the Agent asks qualifying
questions one-by-one before applying criteria.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_sales_qualifying_questions`. If empty, setup uses a neutral placeholder.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_sales_qualifying_criteria`: Applied to answers from these questions.
  - `project_attributes_sales_qualifying_criteria_fallback_action`: Executed when criteria are not
    satisfied.
- **Logic Interactions:**
  - `agent_creator_sales_qualifying_questions`: First-init source used to prefill this attribute.
  - None. This field is consumed directly in the lead-qualification scenario and does not require
    direct runtime reads from additional sales attributes.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`
