# 4. Agent Behavior

Back to the [attribute index](index.md).

## `project_attributes_setting_calendar_event_integration`


**Title:** 4-04. Appointment - Calendar Event Integration [A] [IMPORTANT]

**Description:**

```md
Choose how the Agent should handle calendar event creation during appointment flows.

**Best Practice:** Enable only the integration your team actually uses in production and keep
related setup fields complete before going live.

Behavior by value:

- **`disabled`:** The Agent does not attempt calendar-event creation.
- **`calcom_integration`:** Appointment flow follows Cal.com integration logic.
- **`google_integration`:** The Agent can create calendar invites directly.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This setting controls which appointment-creation path is exposed in runtime
prompts. For Google integration, the system builds meeting payloads and includes both the user email
and `project_business_manager_email` as attendees. It also controls `create_meeting_tool`
registration and the meeting-action state visibility in runtime context. For Cal.com integration,
the appointment scenario follows booking-style availability and booking-submission steps instead of
the Google meeting-creation path.

**Fallbacks:** During initialization, this value can be taken from Agent Creator settings; many
industry defaults keep it disabled. If not configured to an active integration, event creation paths
stay inactive.

**Dependencies:**

- **Primary Settings:**
  - `project_business_manager_email`: Used as a required attendee in Google invite creation.
  - `project_attributes_setting_booking_enabled`: Required for Cal.com integration flows that rely
    on booking-style tool registration and booking action-state handling.
- **Logic Interactions:**
  - `project_attributes_setting_meeting_duration`: Used for Google meeting creation payload.
  - `project_attributes_setting_meeting_setup_phrase`: Alters accepted phrasing for
    `create_meeting_tool` triggering when Google integration is active.
  - `project_attributes_setting_test_mode`: Switches Google meeting handling between live calendar
    command execution and mock success event flow.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `enum`

**Possible values:** `["disabled", "calcom_integration", "google_integration"]`

---

## `project_attributes_setting_email_send_information_enabled`


**Title:** 4-05. Email to User During Session - Enabled [B] [IMPORTANT]

**Description:**

```md
Turn this on if the Agent is allowed to send emails to users during a live conversation.

**Pro-Tip:** Enable this only after you configure allowed email content and confirm your team is
comfortable with what can be sent automatically.

Behavior by value:

- **Enabled (`True`):** Email-send tools and email content guidance can be used during the session.
- **Disabled (`False`):** The Agent will not send user-facing emails during the session. If the user
  asks for email delivery, the Agent should explain that it cannot send the email and that it will
  pass the information to the manager.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This flag gates email-related prompt instructions and tool availability. It is
also used by send-message routing logic when deciding delivery channels. In voice prompts, the
disabled state adds an explicit fallback instruction to tell the user email cannot be sent and the
information will be passed to the manager instead.

**Fallbacks:** Common initialization keeps this field empty until industry defaults apply; industry
content setup then typically sets an explicit boolean.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_email_send_information_allowed_content`: Defines detailed allowed
    email content.
  - `project_attributes_setting_email_send_information_allowed_content_items`: Defines concise
    allowed item list for policy prompts.
- **Logic Interactions:**
  - `project_attributes_setting_sms_send_information_enabled`: Channel routing may prefer SMS first
    when both channels are available.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `bool`

---

## `project_attributes_setting_email_send_information_allowed_content`


**Title:** 4-06. Email to User During Session - Allowed Content [B] [IMPORTANT]

**Description:**

````md
Define the exact email content templates or rules the Agent is allowed to send.

**Best Practice:** Keep this content explicit and reusable (clear subject/body format, approved
placeholders, and approved tone).

**Examples:**

```txt
# Appointment Confirmation

Email subject:
---
[business_name] - Appointment Confirmation
---

Email body:
---
Dear [user_name],<br><br>

Thank you for choosing [business_name]!<br><br>

<strong>Appointment Summary:</strong><br>
Appointment date: [preferred_date]<br>
Appointment time: [preferred_time]<br>

One of our team members will review your appointment request and confirm the details shortly.<br><br>

Warm regards,<br>
[[agent_name]]
---
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime email-send flows inject this field as the primary policy/context block
that constrains what the Agent may send.

**Fallbacks:** Common defaults initialize this as empty and industry-specific preparation fills it.
If this remains empty while email sending is enabled, policy guidance becomes under-specified.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_email_send_information_enabled`: Must be enabled for this content to
    be actionable.
  - `project_attributes_setting_email_send_information_allowed_content_items`: Companion concise
    list used by separate prompt constraints.
- **Logic Interactions:**
  - `project_business_name`: Commonly used placeholder in approved templates.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

---

## `project_attributes_setting_email_send_information_allowed_content_items`


**Title:** 4-07. Email to User During Session - Allowed Content Items [B] [IMPORTANT]

**Description:**

````md
Define a short, high-level whitelist of what the Agent may include in emails.

**Pro-Tip:** Use this field for concise policy items (what is allowed), and keep full writing
templates in the Allowed Content field.

**Examples:**

```txt
- Appointment confirmation summary
- Booking or purchase links
- Next-step instructions
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This field is injected into runtime explicit-constraint prompts as a compact
allow-list for email content decisions.

**Fallbacks:** Defaults initialize this as empty and industry initialization usually provides a
value. If empty with email enabled, constraint quality degrades.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_email_send_information_enabled`: Activates/deactivates email policy
    usage.
  - `project_attributes_setting_email_send_information_allowed_content`: Full content policy that
    complements this condensed list.
- **Logic Interactions:**
  - `project_attributes_setting_sms_send_information_allowed_content_items`: Teams often align both
    channel lists to keep policy consistency.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

---

## `project_attributes_setting_sms_send_information_enabled`


**Title:** 4-08. SMS to User During Session - Enabled [B] [IMPORTANT]

**Description:**

```md
Turn this on if the Agent is allowed to send SMS/text messages during the conversation.

**Best Practice:** Enable only after you define approved SMS content and confirm operational rules
for messaging customers.

Behavior by value:

- **Enabled (`True`):** SMS send tools and SMS content guidance are available.
- **Disabled (`False`):** SMS information-send tools and SMS policy guidance are disabled. If the
  user asks for SMS delivery, the Agent should explain that it cannot send an SMS and that it will
  pass the information to the manager.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This flag gates SMS-related prompt constraints and `send_sms_tool` exposure for
information-delivery behavior. It also affects default channel selection logic when no explicit send
type is provided. In voice prompts, the disabled state adds an explicit fallback instruction to tell
the user SMS cannot be sent and the information will be passed to the manager instead. This setting
does not globally disable every workflow-specific SMS dispatch path.

**Fallbacks:** Common defaults initialize this field for later industry setup; industry content
skills usually set a concrete boolean.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_sms_send_information_allowed_content`: Full approved SMS content
    rules.
  - `project_attributes_setting_sms_send_information_allowed_content_items`: Condensed allowed item
    list for policy prompts.
- **Logic Interactions:**
  - `project_attributes_setting_email_send_information_enabled`: If SMS is off, message routing may
    fall back to email when available.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `bool`

---

## `project_attributes_setting_sms_send_information_allowed_content`


**Title:** 4-09. SMS to User During Session - Allowed Content [B] [IMPORTANT]

**Description:**

````md
Define the exact SMS content the Agent is allowed to send during a session.

**Pro-Tip:** Keep messages short, operational, and channel-appropriate. Include only approved
wording for links, confirmations, and next actions.

**Examples:**

```txt
- Large group reservation acknowledgment and next steps.
- Link handoff message: "Please use this link to continue: https://example.com/path"
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime SMS send flows inject this as the main policy block for what can be sent.
The system can combine it with dynamic per-user context and booking-link context when available.

**Pro-Tip:** If you need content pulled from the conversation or user context, use explicit
placeholders such as `[user's physical address]` instead of generic ones like `[address]`.

**Fallbacks:** Common defaults initialize as empty and industry initialization typically populates
it. If empty while SMS sending is enabled, guidance is weak and behavior becomes less predictable.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_sms_send_information_enabled`: Must be enabled for this policy to be
    applied.
  - `project_attributes_setting_sms_send_information_allowed_content_items`: Companion concise
    allow-list.
- **Logic Interactions:**
  - `project_attributes_setting_booking_enabled`: Booking-related link messages can appear when
    booking flows are active.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

---

## `project_attributes_setting_sms_send_information_allowed_content_items`


**Title:** 4-10. SMS to User During Session - Allowed Content Items [B] [IMPORTANT]

**Description:**

````md
Define a concise list of SMS content categories the Agent is allowed to send.

**Best Practice:** Keep this list short and explicit so policy prompts stay clear and deterministic.

**Examples:**

```txt
- Reservation update summary
- Approved booking link
- Email-collection instruction via SMS
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This field is inserted into explicit-constraint prompts for SMS behavior and helps
steer the Agent toward approved categories only.

**Fallbacks:** If left empty while SMS sending is enabled, policy constraints become less specific.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_sms_send_information_enabled`: Activates/deactivates SMS policy
    usage.
  - `project_attributes_setting_sms_send_information_allowed_content`: Full message policy paired
    with this compact list.
- **Logic Interactions:**
  - `project_attributes_setting_email_send_information_allowed_content_items`: Teams often align
    both channel policy lists.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

---

## `project_attributes_setting_sms_provider`


**Title:** 4-10-A. SMS Provider [C]

**Description:**

```md
Choose which SMS provider should be treated as the default path.

**Pro-Tip:** Keep this aligned with the base SMS connectors your agent actually uses.

Behavior by value:

- **`twilio_messenger`:** Uses the Twilio Messenger path.
- **`sms_service`:** Uses the dedicated SMS service connector path.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This enum is evaluated in the SMS worker to choose the base delivery path in both
command-send and actor/message-send flows. When there is a more specific session-based or pooled SMS
match, runtime can use that path instead. Caller-ID-pool setup also uses this value as the base SMS
provider. Pooled SMS lookups only accept routed bindings from that same provider; otherwise they
fall back to the base SMS provider selected here. The number `+12442442424` is a magic number that
is always treated as mock, allowing platform-level listeners, such as virtual SMS handlers, to route
it accordingly.

**Fallbacks:** Common defaults set `twilio_messenger`.

**Provisioning note:** Initial phone provisioning can override this value automatically based on the
provider returned by the phone-number service.

- Bought provider `twilio` -> set to `twilio_messenger`
- Any other bought provider -> set to `sms_service`

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_sms_send_information_enabled`: Controls message-mode behavior that
    can route into SMS sends.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `enum`

**Possible values:** `["twilio_messenger", "sms_service"]`

---

## `project_business_manager_email`


**Title:** 4-11. Email to Manager - Email Address [A] [IMPORTANT]

**Description:**

```md
Set the main manager/team email where the Agent should send escalations, leads, and operational
updates.

**Best Practice:** Use a monitored shared mailbox (not one person's inbox) so handoffs and reports
are not missed.

**Examples:**

- `manager@yourbusiness.com`
- `frontdesk@yourbusiness.com`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used across reporting/handoff paths, as the manager attendee when calendar invites
are created, and as the reply-to address for outbound emails when those workflows enable reply
handling.

**Fallbacks:** On first initialization, the system can prefill this from Agent Creator manager
business info. If that source is empty, it falls back to `customer_email`. If still empty,
manager-directed notifications have no destination until configured, and reply-enabled outbound
emails are sent without an effective reply-to address.

**Dependencies:**

- **Primary Settings:**
  - `customer_email`: First-init source used to prefill this field.
- **Logic Interactions:**
  - The advanced system configuration `agent_creator_business_info_manager_email` is read as the
    preferred first-init source when provided by Agent Creator.
  - `project_attributes_setting_calendar_event_integration`: Google meeting creation uses this value
    as attendee.
  - Outbound email flows that request reply handling read this value, normalize it, and use it as
    `replyTo` only when it passes basic email-format validation.
  - Built-in session-ended report criteria commonly use this address as the default manager
    recipient when report delivery is active.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

---

## `project_attributes_setting_transfer_call_enabled`


**Title:** 4-12. Transfer Call to Manager - Enabled [B] [IMPORTANT]

**Description:**

```md
Controls whether the Agent is allowed to transfer live phone calls to a human co-worker.

**Best Practice:** Keep this enabled only when escalation numbers are fully configured for both
working-hours and non-working-hours behavior.

Behavior by value:

- **Enabled (`True`):** Transfer-call logic can run when transfer criteria and phone prerequisites
  are satisfied.
- **Disabled (`False`):** The Agent does not transfer calls. Relay fallback remains available only
  when session-ended reporting is enabled.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Enables transfer-call prompt constraints and transfer tool usage on phone
conversations.

**Fallbacks:** If enabled but required escalation numbers are missing for the current time context,
transfer is blocked and the Agent falls back to non-transfer behavior (typically relay messaging
when reporting is enabled).

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_destination_availability_check_enabled`: Controls
    whether scenario-specific transfer phone numbers configured in
    `project_attributes_setting_transfer_call_phone_numbers` are checked for after-hours
    availability.
  - `project_attributes_setting_transfer_call_criteria`: Defines which intents should trigger
    transfer suggestions.
  - `project_business_non_working_hour_escalation_phone`: Required for non-working-hours transfer
    attempts.
  - `project_business_working_hour_escalation_phone`: Working-hours baseline transfer target.
  - `project_attributes_setting_transfer_call_phone_numbers`: Advanced per-scenario phone routing.
- **Logic Interactions:**
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Changes how
    working-hours checks gate transfer eligibility.
  - `project_attributes_setting_session_ended_report_enabled`: Enables relay fallback behavior when
    transfer is unavailable.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `bool`

---

## `project_business_non_working_hour_escalation_phone`


**Title:** 4-13. Transfer Call to Manager - Phone # Non-Working Hours [A] [IMPORTANT]

**Description:**

```md
Set the escalation phone number the Agent should use outside working hours when a transfer is
needed.

**Best Practice:** Always include full country code, and do not put your public business number here
if that public number automatically forwards inbound calls to the Agent. Otherwise the Agent can
transfer the caller to this number and the phone system can send the call straight back to the
Agent.

Accepted formats:

- `+12223334444`
- `12223334444`
- `+12223334444#1234` (extension supported)

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used as the baseline non-working-hours transfer target when advanced per-scenario
mapping is not provided. It is also referenced in chat/phone explicit-constraint guidance when
off-hours manager-contact instructions are generated.

**Fallbacks:** If advanced transfer-number routing is empty and this field is also empty, an
outside-working-hours transfer is unavailable. What happens next depends on session-ended reporting:

- **Reporting enabled:** The Agent explains that it cannot transfer the call, offers to pass a
  message to the team, and asks the caller what they would like to convey.
- **Reporting disabled:** The Agent explains that it cannot transfer the call but does not offer to
  take or relay a message.

**Routing Safety:** A recursive call loop happens when this field is set to
`project_business_public_phone` or any other number that forwards to
`project_representative_agent_voice_phone_number`. The transfer flow sends the active call to this
escalation number, then the business telephony system routes it back to the Agent.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_enabled`: Must be enabled for this value to be used.
  - `project_attributes_setting_transfer_call_phone_numbers`: Optional advanced map for selecting a
    specific transfer destination.
- **Logic Interactions:**
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Determines
    whether non-working-hours branch logic is strictly enforced.
  - `project_attributes_setting_session_ended_report_enabled`: When enabled, allows the Agent to
    offer to take the caller's message for the team if an after-hours transfer cannot proceed.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

---

## `project_business_working_hour_escalation_phone`


**Title:** 4-14. Transfer Call to Manager - Phone # Working Hours [A] [IMPORTANT]

**Description:**

```md
Set the primary escalation phone number for transfer attempts during working hours.

**Pro-Tip:** Use a staffed line that can actually pick up live transfers. Do not enter your public
business number here if that public number automatically forwards inbound calls to the Agent.

Accepted formats:

- `+12223334444`
- `12223334444`
- `+12223334444#1234` (extension supported)

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used as the baseline working-hours transfer target when advanced per-scenario
mapping is not provided. It is also referenced in manager-contact guidance during working hours and
as an off-hours fallback contact in manager-chat guidance when the non-working-hours number is
empty. Built-in session-ended report criteria also commonly use this value as the default
working-hours SMS recipient.

**Fallbacks:** On first initialization, the system can prefill this from Agent Creator escalation
phone business info. Working-hours transfer remains possible if this field is empty only when
`project_attributes_setting_transfer_call_phone_numbers` provides a usable route; if both are empty,
transfer is blocked. During working-hours manager-contact guidance, there is no dedicated fallback
number if this field is blank.

**Routing Safety:** A recursive call loop happens when this field is set to
`project_business_public_phone` or any other number that forwards to
`project_representative_agent_voice_phone_number`. The transfer flow sends the active call to this
escalation number, then the business telephony system routes it back to the Agent.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_enabled`: Must be enabled for transfer routing.
  - `project_attributes_setting_transfer_call_phone_numbers`: Can satisfy working-hours routing when
    this field is empty.
- **Logic Interactions:**
  - The advanced system configuration `agent_creator_business_info_escalation_phone` is read as a
    first-init source when provided by Agent Creator.
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Controls how
    strictly working-hours status affects transfer eligibility.
  - `project_business_non_working_hour_escalation_phone`: When non-working-hours contact is empty,
    manager-chat guidance can fall back to this working-hours number with a call-during-hours note.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

---

## `project_attributes_setting_transfer_call_criteria`


**Title:** 4-15. Transfer Call to Manager - Call Criteria [B] [IMPORTANT]

**Description:**

````md
Define the situations where the Agent should suggest connecting the user to a human co-worker.

**Best Practice:** Write concrete intent lines (one case per line) so transfer decisions stay
predictable.

**Examples:**

```txt
- Re-confirm an existing appointment/reservation with a human team member.
- Report a lost item.
- Request customer service or manager support.
- Notify the team about being late for an existing reservation.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into transfer-call explicit constraints to define which intents should
trigger a manager-transfer suggestion. The same criteria list is also reused in relay-message
guidance when transfer is unavailable and reporting-based relay is enabled.

**Fallbacks:** If empty, no criteria-specific list is injected into transfer constraints, so
transfer guidance falls back to generic manager-transfer behavior. During initialization, industry
skills typically prefill defaults; in some industries, criteria rows are also dynamically added or
removed based on configured booking/order capabilities.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_transfer_call_enabled`: Must be enabled for criteria-driven
    transfers.
- **Logic Interactions:**
  - `project_attributes_setting_session_ended_report_enabled`: Criteria can also influence
    relay-message suggestions when transfer is unavailable.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

---

## `project_attributes_setting_transfer_call_phone_numbers`


**Title:** 4-16. Transfer Call to Manager - Advanced Phone Number Selection & Rules [B] [IMPORTANT]

**Description:**

````md
Use this field when you need different transfer numbers for different call scenarios.

**Pro-Tip:** Keep one baseline escalation number in the standard working-hours/non-working-hours
fields, then use this field only for advanced routing exceptions.

Example structure:

```txt
During working hours:
- Standard booking: +12223334444
- Group booking: +12223335555
- Emergency: +12223337777

Outside working hours:
- Standard booking: +12223334444
- Group booking: +12223335555
- Emergency: +12223337777
```

Accepted phone formats also support extensions, for example: `+12223334444#1234`.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime transfer flow evaluates this ruleset and selects one phone number (or a
clarification question) based on conversation intent and current working-hours state.

**Fallbacks:** If empty, the system uses baseline working-hours/non-working-hours escalation
numbers. If populated but routing is ambiguous, the transfer flow can return a clarification prompt
instead of a number. With working-hours checks enabled, a non-working-hours escalation number is
required for after-hours transfers, even when Transfer Call Phone Numbers contains a matching route.

**Dependencies:**

- **Primary Settings:**
  - `project_business_working_hour_escalation_phone`: Baseline working-hours fallback.
  - `project_business_non_working_hour_escalation_phone`: Baseline non-working-hours fallback when
    this field is empty.
  - `project_attributes_setting_transfer_call_enabled`: Must be enabled to use this routing map.
- **Logic Interactions:**
  - `project_attributes_setting_define_conversation_is_during_working_hours_enabled`: Affects
    whether after-hours eligibility rules are strictly enforced.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

---

## `project_attributes_setting_session_ended_sms_enabled`


**Title:** 4-17. Promotional SMS - Enabled [B]

**Description:**

```md
Controls whether the system should send a post-conversation SMS after a session ends.

**Best Practice:** Enable this only when you have approved final-message content and clear
consent/compliance handling for your use case.

Behavior by value:

- **Enabled (`True`):** Session-end SMS send logic runs when content and phone prerequisites are
  satisfied.
- **Disabled (`False`):** No automatic post-session SMS is sent.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Checked in end-session flow before triggering the `sms_worker_send_sms` system
event for post-session SMS delivery.

**Fallbacks:** Defaults to `False`. Even when enabled, sending is skipped if message content is
empty or no usable phone number is available. Sending is also skipped when no meaningful
conversation transcript exists, because the end-session flow exits before the SMS send step.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_sms_content`: Required message text.
- **Logic Interactions:**
  - Conversation/user phone data: If phone is unavailable, send is abandoned.
  - Conversation transcript availability: If transcript is empty, the flow returns before SMS send
    logic is executed.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `bool`

---

## `project_attributes_setting_session_ended_sms_content`


**Title:** 4-18. Promotional SMS Content [B]

**Description:**

````md
Write the SMS text that should be sent automatically after the conversation ends.

**Pro-Tip:** Keep this concise, compliant, and action-oriented. If you include a link, ensure it is
valid and approved for customer messaging.

**Examples:**

```txt
Thank you for speaking with us today. We appreciate your time. Here is your next-step link: [your-link-here]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** End-session SMS logic reads this text and forwards it as `sms_text` in the
`sms_worker_send_sms` event when post-session SMS checks pass.

**Fallbacks:** If this field is empty (or whitespace), the post-session SMS send is skipped. This
content is also not used when session-ended SMS is disabled or when the end-session flow exits early
due to an empty transcript.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_session_ended_sms_enabled`: Must be enabled for this content to be
    used.
- **Logic Interactions:**
  - Conversation/user phone data: A valid phone is required at send time.
  - Conversation transcript availability: If transcript is empty, the flow returns before this
    content can be sent.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

---

## `project_attributes_setting_instant_callback_on_abort_enabled`


**Title:** 4-19. Phone - Instant Callback on Abort [A]

**Description:**

```md
Enable this if the Agent should automatically try one immediate callback after an apparent aborted
phone call.

**Best Practice:** Keep this on only if your call flows can safely handle retry callbacks and your
business policy allows automatic re-dial.

Behavior by value:

- **Enabled (`True`):** The system may place one automatic callback after connection-related abort
  conditions.
- **Disabled (`False`):** No automatic callback is attempted.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Evaluated during voice conversation-ended handling. If enabled and the session
channel is `phone`, the system runs callback-eligibility checks and, when eligible, triggers the
`make_call` command. A per-session state flag prevents more than one automatic callback in the same
session.

**Fallbacks:** Defaults to `False`. Callback is skipped for forwarded-call endings, when a callback
has already been executed in the same session, when call start time is unavailable, and when
heuristic/LLM inspection determines the call ended intentionally.

**Dependencies:**

- **Primary Settings:**
  - Voice-call end-event handling context: Callback logic is evaluated only in supported voice-call
    conversation-ended paths.
- **Logic Interactions:**
  - Conversation channel resolution: Automatic callback is limited to `phone` sessions (not
    `webcall`).
  - Call-end reason and session duration heuristics: Forwarded calls are excluded; very short calls
    are prioritized for callback.
  - LLM intentional-end inspection: Non-intentional endings are treated as callback candidates.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `bool`

---

## `project_attributes_setting_phone_dialpad_output_enabled`


**Title:** 4-19-A. Phone - Dialpad Output [B]

**Description:**

```md
This setting lets the Agent press phone keypad digits during a live phone conversation. Use it when
a scenario requires the Agent itself to navigate another phone system, such as choosing an IVR menu
option, entering a confirmation code, or sending an account/order number through DTMF.

**Best Practice:** Enable only for phone workflows that have been tested end-to-end. Turn this
setting on only when the scenario explicitly needs Agent-sent keypad output, then write the scenario
step so the Agent says both the digits and the dialpad action in the same spoken response. The
trigger should be an action statement from the Agent, not an instruction for the User to press
digits.

**Scenario authoring guidance:** Add a step that tells the Agent exactly when to send the digits and
what to say before sending them. The latest Agent message must contain the keypad intent and the
digits to send. Use clear wording such as:

- "I am pressing dial pad option 4 now."
- "Give me a moment, I will enter six three two one on the dial pad."
- "I will send confirmation code nine zero one two through the keypad."
- "I will enter star nine pound on the keypad."

Do not use this setting for steps where the User should type digits on their own phone keypad. For
that workflow, the scenario should ask the User to use the dial pad and wait for their input instead
of having the Agent send digits.

Behavior by value:

- **Enabled (`True`):** The Agent can attempt dialpad output when the phone conversation and
  scenario wording clearly indicate that the Agent is about to send digits.
- **Disabled (`False`):** Dialpad output path is blocked.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In phone-channel analysis, runtime exposes the `send_dtmf_output_tool` when this
setting is enabled and the configured voice provider supports outbound dialpad commands. The tool is
triggered only when the latest Agent message clearly says the Agent is going to enter, press, key
in, or send a number through the dial pad or keypad. The message must include the digits in the same
latest response; digits can be spoken as words, and `star`/`pound` are converted to `*`/`#`. If
approved, the system extracts the compact digit string and sends the `dial_digits` command to the
voice connector.

**Fallbacks:** Initialized to `False` in common defaults. If channel/provider prerequisites are not
met, runtime exits without sending dialpad output even when enabled. If the latest Agent message
does not contain both an explicit dialpad/keypad sending intent and the digits to send, the system
asks for clarification instead of sending digits.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service`: Dialpad command path is available only
    when the configured voice provider supports outbound dialpad commands.
- **Logic Interactions:**
  - `send_dtmf_output_tool`: The tool event path that extracts the digits from the latest Agent
    message and sends them via DTMF.
  - `commandIdn="dial_digits"`: Execution command used to emit keypad digits.
  - User keypad input waiting: A separate dialpad-input path is used when the Agent asks the User to
    type digits on their own phone keypad. This setting is for Agent-sent output, not User-entered
    input.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `bool`

**Is hidden:** `false`

---
