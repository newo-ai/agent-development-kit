# 6. Support - Advanced

Back to the [attribute index](index.md).

## `project_attributes_setting_hitl_monitoring_enabled`


**Title:** HITL - Monitoring [C]

**Description:**

```md
Enables or disables HITL (Human-in-the-Loop) monitoring outputs for support and quality operations.

**Pro-Tip:** Start with this disabled in early setup, then enable once your team is ready to review
and triage monitoring signals consistently.

**Examples:**

- **Enabled (`True`):** Session-ended monitoring payloads are sent to HITL reporting endpoints.
  Magic-browser reservation workflows can also emit extra operational alerts for manual checks.
- **Disabled (`False`):** HITL-specific monitoring commands are not sent.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When enabled, end-session logic sends a `send_hitl_report` command through the API
webhook connector with conversation and performance fields (for example summary, success, potential
revenue, channel, and version metadata). Version metadata comes directly from the installed Project.
The payload schema includes an `asr` field, but in current end-session dispatch it is sent with the
default empty value unless explicitly provided by the caller. In reservation-related magic-browser
task handling, this flag also gates `send_slack_report` command dispatch for success/failure
operational notifications.

**Fallbacks:** Defaults to `False` during common initialization. If disabled, core session-ended
processing still runs, but HITL-specific command dispatch is skipped.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required.
- **Logic Interactions:**
  - `project_attributes_setting_magic_browser_alert_enabled`: Independent alert-email path that can
    operate alongside HITL monitoring.
  - `project_attributes_setting_session_ended_report_enabled`: Session report delivery remains
    separate from HITL monitoring dispatch.
```

**Level:** `Customer`

**Group:** `6. Support - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_setting_magic_browser_alert_enabled`


**Title:** HITL - Magic Browser Alerting [C]

**Description:**

```md
Controls whether alert emails are sent when magic-browser task execution fails after retry attempts.

**Pro-Tip:** Keep this enabled unless you already have an equivalent incident-alert channel, so
failed automated booking tasks are not missed.

**Examples:**

- **Enabled (`True`):** Failure alerts are emailed with task context for manual follow-up.
- **Disabled (`False`):** No magic-browser failure alert email is sent.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In magic-browser response handling, once retries are exhausted, this flag gates
sending `email_worker_send_email` alerts with an "ACTION REQUIRED" subject and diagnostic context
(business info, manager contacts, bot response, task context). The recipient is a runtime-fixed
internal operations mailbox (not a customer-configurable destination), so this setting controls
whether the alert is sent, not where it is routed.

**Fallbacks:** Defaults to `True` during common initialization. If disabled, failure handling
continues without alert-email dispatch.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required.
- **Logic Interactions:**
  - `project_attributes_setting_hitl_monitoring_enabled`: HITL monitoring/slack notifications are a
    separate path and may still fire when this email-alert path is disabled.
  - `project_business_manager_email`: Included in the generated alert content for escalation
    context.
  - `project_business_non_working_hour_escalation_phone`: Included in alert context for incident
    follow-up routing.
  - `project_business_working_hour_escalation_phone`: Included in alert context for incident
    follow-up routing.

**Roadmap Note:** This setting is planned for future renaming/expansion so alerting can cover
broader issue categories beyond magic-browser failures.
```

**Level:** `Customer`

**Group:** `6. Support - Advanced`

**Value type:** `bool`

**Is hidden:** `true`

---

## `project_attributes_support_log_document_link`


**Title:** Support Log Document Link (URL) [B]

**Description:**

```md
Stores the URL of your shared support-log document used to coordinate requests, issues, and delivery
status with your support team.

**Pro-Tip:** Use one canonical document per account, keep sections dated, and clearly mark owner and
status for each request.

If this attribute is empty, your support-log workspace link has not been set yet.

Suggested setup flow:

1. Open your template source folder (read-only), for example
   your template folder.
2. Choose the industry-relevant template.
3. Create a copy for your workspace.
4. Share it with your team and support stakeholders.
5. Paste the copied document URL into this attribute and save.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Stored as an operational reference link for support collaboration. In current
runtime paths across the core project and in-scope modules, this attribute is not directly consumed
by conversation, reporting, or booking execution logic.

**Fallbacks:** Common initialization pre-creates this field with a placeholder value so the support
log link slot always exists. If it remains unconfigured, it is treated as an operational reference
field only and does not change runtime behavior.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required.
- **Logic Interactions:**
  - No direct runtime logic interactions are currently applied.
```

**Level:** `Customer`

**Group:** `6. Support - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---
