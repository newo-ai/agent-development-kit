# General Industry Customer and Project Attributes Metadata

## Customer Attributes

### 1. Business - Advanced

#### `project_business_type`

**Description:**

````md
Define your business category in a short phrase so the Agent has clear domain context from the
start.

**Pro-Tip:** Keep this concise (2-8 words) and include specialization only when it changes how the
Agent should respond. For General industry accounts, use this field to explain the real-world
subject area behind the Agent, such as "dance studio", "nonprofit membership program", or "online
course provider". Avoid generic values like "Other" unless you add useful detail.

**Examples:**

```txt
Dance studio and private lessons
```

```txt
Online course subscriptions
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into business-context preparation for supported industries and into
session-success evaluation prompts to anchor business-domain reasoning. During setup,
industry-specific defaults can populate this value so the Agent can describe the business with the
right domain language.

For General industry accounts, this value is also injected into General introduction routing. In the
General introduction scenario, it tells the Agent what receptionist vocabulary, expected questions,
and caller flow to use. If it is empty, set to "Auto detect", set to "Other" without more detail, or
otherwise unrecognized, the Agent falls back to a generic small-business receptionist style.

**Fallbacks:** On first initialization, this can be copied from Agent Creator's business-industry
description. If that source is empty, initialization first stores a generic placeholder, then
applies the selected industry's default label when available. For General accounts, that
industry-specific fallback is the General default label.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines whether the General industry defaults and General
    introduction scenario are used.
- **Logic Interactions:**
  - `agent_creator_business_info_industry_description`: First-init source used to prefill this
    attribute when Agent Creator provides a custom business category.
  - `project_attributes_general_modality`: Controls the primary General workflow route while this
    field controls the domain language and style used within that route.
````

**Level:** `Customer`

**Is hidden:** `true`

### 4. Agent Behavior

#### `project_attributes_general_appointment_check_in_notes`

**Title:** 4-20. Appointment Setting - Check-in Notes [B]

**Description:**

````md
Define what the Agent should tell people after they complete booking, such as arrival timing,
parking details, or documents to bring.

**Pro-Tip:** Keep this focused on must-know next steps for the day of the appointment.

**Examples:**

```txt
Please arrive 10 minutes early for check-in. Bring a photo ID and any documents we asked you to complete before your visit.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into the general appointment-via-link scenario and shared after the user
confirms they finished booking.

**Fallbacks:** On first initialization, this can be copied from Agent Creator intake. If no value is
provided, it is initialized as empty. If left empty, the booking flow finishes without extra
post-booking notes.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_general_appointment_url`: Used in the same link-booking flow where these
    notes are delivered.
- **Logic Interactions:**
  - `agent_creator_general_appointment_check_in_notes`: First-init source used to prefill this
    attribute when provided by Agent Creator.
  - `project_attributes_general_appointment_scenario_link_guidance_instruction`: Used earlier in the
    same flow while the Agent helps the user complete the online form.
  - `project_attributes_general_modality`: The `booking` modality is the General workflow path that
    uses these post-booking notes.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_general_appointment_scenario_link_guidance_instruction`

**Title:** 4-21. Appointment Setting - Self-schedule Link (URL) - Guidance Instruction [B]

**Description:**

````md
Define the exact instructions the Agent should use while helping someone complete your online
appointment form.

**Best Practice:** Write this as short, step-by-step actions that match the wording and order on
your booking page.

**Examples:**

```txt
Open the booking link, choose the service you need, select a convenient date and time, enter your contact details, and submit the form to finish scheduling.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into the general link-booking scenario after the user confirms the
booking page is open and needs help completing it.

**Fallbacks:** On first initialization, this can be copied from Agent Creator intake. If no custom
instruction is provided, setup uses a neutral placeholder.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_general_appointment_url`: Guidance is actionable only when a booking link is
    available.
- **Logic Interactions:**
  - `agent_creator_general_appointment_scenario_link_guidance_instruction`: First-init source used
    to prefill this attribute when provided by Agent Creator.
  - `project_attributes_general_appointment_check_in_notes`: Runs later in the same flow after the
    user confirms booking completion.
  - `project_attributes_general_modality`: The `booking` modality is the General workflow path that
    uses this form guidance.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_general_appointment_url`

**Title:** 4-22. Appointment Setting - Self-schedule Link (URL) [A] [IMPORTANT]

**Description:**

```md
Set the URL where people can self-schedule appointments online for your business. If you do not
offer online self-scheduling, leave this empty.

**Best Practice:** Use the final booking page URL instead of a homepage or contact page, and retest
it whenever your scheduling provider changes.

**Examples:**

- `https://yourbusiness.com/book`
- `https://booking.example.com/request-appointment`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Referenced directly by the general self-schedule appointment-via-link scenario
when the Agent shares the booking link with the user.

**Fallbacks:** On first initialization, this can be copied from Agent Creator intake. If no value is
provided, it is initialized as empty. If it stays empty, the link-booking scenario has no usable
self-scheduling URL to share.

**Dependencies:**

- **Primary Settings:**
  - None. This link is consumed directly by the General booking workflow.
- **Logic Interactions:**
  - `agent_creator_general_appointment_url`: First-init source used to prefill this attribute when
    provided by Agent Creator.
  - `project_attributes_general_modality`: The `booking` modality is the General workflow path that
    shares this link.
  - `project_attributes_general_appointment_scenario_link_guidance_instruction`: Guidance content
    used after this link is shared.
  - `project_attributes_general_appointment_check_in_notes`: Post-booking notes shown later in the
    same link-based flow.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_general_modality`

**Title:** 4-23. General Modality [A] [IMPORTANT]

**Description:**

```md
Choose the primary workflow style for a General industry Agent. This tells the Agent whether the
business mainly wants callers to book through a link, complete a purchase or signup through a link,
or leave details for follow-up.

**Best Practice:** Pick the mode that matches the main promise of the Agent. Use `followup` when the
business needs human review, custom quoting, or manual follow-up before a commitment is made.

**Examples:**

- **`booking`:** The Agent routes booking or scheduling requests to the General Booking via Link
  flow and guides the user through the configured booking page.
- **`transactional`:** The Agent routes purchase, order, payment, subscription, or signup requests
  to the General Purchase via Link flow and uses the business website or relevant checkout context.
- **`followup`:** The Agent gathers the caller's needs and contact details, then routes through User
  Inquiry so a team member can follow up.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Read by the General introduction scenario as the highest-priority routing rule for
matching requests. `booking` routes booking-style requests through **Booking via Link**,
`transactional` routes purchase/signup-style requests through **Purchase via Link**, and `followup`
routes the caller through **User Inquiry** so details can be relayed to the team. If the value is
missing, empty, or unrecognized, runtime treats it as `followup`.

**Fallbacks:** On first initialization, this can be copied from `agent_creator_general_modality`. If
Agent Creator does not provide a value, setup defaults it to `followup`.

**Dependencies:**

- **Primary Settings:**
  - `project_business_type`: Provides the business subject area and receptionist style that the
    selected modality should use.
  - `project_attributes_general_appointment_url`: Required for `booking` mode to share a real
    self-scheduling link.
  - `project_business_website_url`: Used by `transactional` mode as the default purchase, order, or
    signup link when a more specific checkout URL is not present in business context.
- **Logic Interactions:**
  - `agent_creator_general_modality`: First-init source used to prefill this attribute when Agent
    Creator provides a modality.
  - `project_attributes_general_appointment_scenario_link_guidance_instruction`: Used during
    `booking` mode after the booking link is opened.
  - `project_attributes_general_appointment_check_in_notes`: Used after successful booking
    completion in `booking` mode.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `enum`

**Possible values:** `["booking", "followup", "transactional"]`
