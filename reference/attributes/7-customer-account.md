# 7. Customer Account

Back to the [attribute index](index.md).

## `customer_email`


**Title:** Customer Email [A]

**Description:**

```md
Primary account-owner email linked to this workspace.

**Pro-Tip:** Keep this as a monitored inbox you can access during onboarding, account recovery, and
support escalations.

**Examples:**

- `owner@yourbusiness.com`
- `operations@yourbusiness.com`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Initialized from customer contact data (`GetCustomerInfo().contact_email`) when
empty.

**Fallbacks:** If no contact email is available, initialization stores an empty value. If available,
setup can source it from current customer contact data.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required.
- **Logic Interactions:**
  - `project_business_manager_email`: First-time business-manager email setup can use this value as
    a fallback when Agent Creator manager business info is not provided.
```

**Level:** `Customer`

**Group:** `7. Customer Account`

**Value type:** `string`

**Is hidden:** `true`

---

## `customer_first_name`


**Title:** Customer First Name [A]

**Description:**

```md
First name of the primary account contact.

**Pro-Tip:** Keep this aligned with your active account owner/contact so support communications are
clear and properly addressed.

**Examples:**

- `Alex`
- `Jordan`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Current common initialization ensures this attribute exists during account setup.

**Fallbacks:** Common initialization creates this as an empty value when missing.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required.
- **Logic Interactions:**
  - No direct runtime logic reads were found across current in-scope runtime flows.
```

**Level:** `Customer`

**Group:** `7. Customer Account`

**Value type:** `string`

**Is hidden:** `true`

---

## `customer_last_name`


**Title:** Customer Last Name [A]

**Description:**

```md
Last name of the primary account contact.

**Pro-Tip:** Keep this updated for cleaner account records and support handoffs.

**Examples:**

- `Smith`
- `Garcia`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Current common initialization ensures this attribute exists during account setup.

**Fallbacks:** Common initialization creates this as an empty value when missing.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required.
- **Logic Interactions:**
  - No direct runtime logic reads were found across current in-scope runtime flows.
```

**Level:** `Customer`

**Group:** `7. Customer Account`

**Value type:** `string`

**Is hidden:** `true`

---

## `customer_phone`


**Title:** Customer Phone Number [A]

**Description:**

```md
Primary account-owner phone number linked to this workspace.

**Pro-Tip:** Store a full number with country code so support and onboarding teams can reach the
right contact quickly.

**Format options:**

- With plus: `+12223334444`
- Without plus: `12223334444`

Both formats are accepted, but make sure to include the full country code in all entries.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Initialized from customer contact data (`GetCustomerInfo().contact_phone`) when
empty.

**Fallbacks:** If no contact phone is available, initialization stores an empty value. If available,
setup can source it from current customer contact data.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required.
- **Logic Interactions:**
  - No direct runtime logic dependencies are currently applied in core NAF flows.
```

**Level:** `Customer`

**Group:** `7. Customer Account`

**Value type:** `string`

**Is hidden:** `true`

---
