# 6. Support

Back to the [attribute index](index.md).

## `project_attributes_private_sa_version`


**Title:** 6-01. SuperAgent Version [B]

**Description:**

```md
Stores the installed Agent framework version for external support and analytics systems.

**Pro-Tip:** Treat this as a system-managed value. Do not edit it manually unless requested by the
technical team during controlled troubleshooting.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Publication writes the installed Project's `version` name as is, prefixes and
suffixes included (`4.16.0-fork`, `v4.16.0`), when that name contains an `x.y.z`. For a name without
one, such as a fork named `fork_naf`, it writes the previous version name from the publish event as
is if that name contains an `x.y.z`, and otherwise leaves the value unchanged. It is a compatibility
copy for external systems. The framework reads its current version from the Project itself for
migration targets, the `modules` payload in `session_ended` events, and the `superagentVersion`
field in human-in-the-loop (HITL) report requests. Changing this Attribute does not change those
outputs or the migration target.

**Fallbacks:** Industry defaults contain a blank placeholder until a publication supplies a version
with an `x.y.z` in its name.

**Dependencies:**

- **Primary Settings:**
  - None. The installed Project version supplies this value.
- **Logic Interactions:**
  - None. The framework writes this Attribute for external consumers and does not read it.
```

**Level:** `Customer`

**Group:** `6. Support`

**Value type:** `string`

**Is read-only:** `true`

---

## `project_attributes_free_notes`


**Title:** 6-02. Free Notes [A]

**Description:**

```md
This is a shared workspace note field for your business team and support team. Use it to keep
operational notes, action items, troubleshooting context, and handoff details in one place.

**Pro-Tip:** Keep notes short, dated, and action-oriented so anyone reviewing the account can
quickly understand context.

**Examples:**

- Meeting outcomes and follow-up tasks.
- Change requests and implementation priorities.
- Temporary support-side observations and known caveats.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Not used as a primary instruction source for Convo runtime behavior. It functions
as support-oriented account context storage.

**Fallbacks:** Initialized as an empty placeholder when missing.

**Dependencies:**

- **Logic Interactions:**
  - None in current runtime flows; this remains an operator-facing notes field.
```

**Level:** `Customer`

**Group:** `6. Support`

**Value type:** `string`

---

## `project_attributes_chat_link_demo`


**Title:** 6-01. Chat - Demo Link (URL) [B]

**Description:**

```md
Link to the Chat widget (demo mode).

**Note:** Attribute is being set by `Agent Creator` during the account creation process. Does not
have any functionality after the account is created.
```

**Level:** `Project`

**Group:** `6. Support`

**Value type:** `string`

---
