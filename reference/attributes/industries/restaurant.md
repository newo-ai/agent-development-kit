# Restaurant Industry Customer and Project Attributes Metadata

## Customer Attributes

### 1. Business

#### `project_attributes_restaurant_catering_email`

**Title:** 1-16. Email - Catering [A]

**Description:**

```md
The main email inbox for catering inquiries and event-related follow-up requests.

**Pro-Tip:** Use a shared inbox monitored by the events/catering team so requests do not depend on
one person being online.

**Examples:**

- `catering@yourrestaurant.com`
- `events@yourrestaurant.com`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Included in restaurant dynamic context variable packs for technical and email
aliases. Runtime email/SMS information delivery and task-shaping flows consume the technical-context
pack that contains this value.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_catering_email`. If that Agent Creator field is empty or unavailable,
setup falls back to `project_business_manager_email`. If both sources are empty, the field stays
empty until manually configured.

**Dependencies:**

- **Primary Settings:**
  - `project_business_manager_email`: Fallback first-init source used when the Agent Creator
    catering email is empty or unavailable.
- **Logic Interactions:**
  - `agent_creator_restaurant_catering_email`: First-init source used to prefill this attribute.
  - `project_business_industry`: Restaurant-specific technical variable assembly consumes this
    value.
```

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

#### `project_attributes_restaurant_googlemaps_reservation_url`

**Title:** 1-17. Link (URL) - Google Booking Reservation [A] [IMPORTANT]

**Description:**

````md
The "Reserve with Google" URL used by the Agent to check table availability and place bookings.

**Pro-Tip:** Paste a direct Google reservation link from your exact listing. If this URL is missing
or invalid, Google-based table booking cannot run.

**Examples:**

```txt
https://www.google.com/maps/reserve/v/dine/c/XXXXXXXXXXX
```

```txt
https://www.google.com/maps/reserve/dine?c=XXXXXXXXXXX&ihs=3
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** On initialization, the value can be prefilled from
`agent_creator_restaurant_googlemaps_reservation_url`. Runtime normalization logic validates and
rewrites accepted Google links into a canonical format and derives the internal reservation
identifier required by default availability/booking flows. Booking payload generation also injects
this URL directly as the `reserveTableURL`.

**Fallbacks:** If the field is empty, the system clears the derived Google reservation identifier
and reserve-table task context. If a non-empty link fails validation, those derived values are also
cleared and the original link remains unchanged until you replace it with a valid Google reservation
URL. In default availability/booking modes, runtime validation stops when the derived Google
reservation identifier is missing. Restaurant transfer/limitations criteria are adjusted based on
whether this field is empty, so leaving it blank avoids promising self-serve table-booking behavior.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_booking_check_availability_type`: For `default` mode, a valid Google
    reservation setup is required.
  - `project_attributes_setting_booking_type`: For `default` mode, a valid Google reservation setup
    is required for default booking execution.
  - `project_business_time_zone`: Included together with reservation URL in booking payload
    preparation.
- **Logic Interactions:**
  - `agent_creator_restaurant_googlemaps_reservation_url`: First-init source used to prefill this
    attribute.
  - `project_attributes_setting_transfer_call_criteria`: Auto-adjusted based on whether this URL is
    present.
  - `project_attributes_setting_additional_limitations_and_restrictions`: Auto-adjusted based on
    whether this URL is present.
````

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

#### `project_attributes_restaurant_large_group_reservation_email`

**Title:** 1-18. Email - Large Group Reservation [A]

**Description:**

```md
The email inbox for reservations that qualify as large-group requests and need manual team handling.

**Pro-Tip:** Use a mailbox monitored by your events/private-booking team so group requests are
triaged quickly.

**Examples:**

- `groups@yourrestaurant.com`
- `events@yourrestaurant.com`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Included in restaurant dynamic context variable packs for technical and email
aliases. Runtime handoff, notification, and information-delivery flows consume the technical-context
pack that contains this value.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_large_group_reservation_email`. If that Agent Creator field is empty or
unavailable, setup falls back to `project_business_manager_email`. If both sources are empty, the
field remains empty until manually configured.

**Dependencies:**

- **Primary Settings:**
  - `project_business_manager_email`: Fallback first-init source used when the Agent Creator
    large-group reservation email is empty or unavailable.
- **Logic Interactions:**
  - `agent_creator_restaurant_large_group_reservation_email`: First-init source used to prefill this
    attribute.
  - `project_attributes_restaurant_large_group_reservation_minimum_party_size`: Defines when a
    reservation is categorized as large-group in restaurant reservation branching logic.
```

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

#### `project_attributes_restaurant_order_email`

**Title:** 1-19. Email - Order [A]

**Description:**

```md
The email inbox used for food-order related requests that require manual follow-up.

**Pro-Tip:** Use a dedicated operational inbox for order handling, especially if your kitchen and
front-of-house teams are different.

**Examples:**

- `orders@yourrestaurant.com`
- `takeout@yourrestaurant.com`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Included in restaurant dynamic context variable packs for technical and email
aliases. Runtime information-delivery and handoff flows consume the technical-context pack that
contains this value.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_order_email`. If that Agent Creator field is empty or unavailable, setup
falls back to `project_business_manager_email`. If both sources are empty, this field stays empty
until manually configured.

**Dependencies:**

- **Primary Settings:**
  - `project_business_address`: Core location data paired with map references.
  - `project_business_public_phone`: Contact data often presented with map references.
- **Logic Interactions:**
  - `agent_creator_restaurant_order_email`: First-init source used to prefill this attribute.
  - `project_business_manager_email`: Fallback first-init source used when the Agent Creator order
    email is empty or unavailable.
```

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

#### `project_attributes_restaurant_private_dining_email`

**Title:** 1-20. Email - Private Dining [A]

**Description:**

```md
The email inbox for private-dining inquiries, proposals, and event-booking follow-up.

**Pro-Tip:** Route this to whoever manages private-room inventory and event terms so responses stay
consistent.

**Examples:**

- `privatedining@yourrestaurant.com`
- `events@yourrestaurant.com`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Included in restaurant dynamic context variable packs for technical and email
aliases. Runtime handoff and information-generation flows consume the technical-context pack that
contains this value.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_private_dining_email`. If that Agent Creator field is empty or
unavailable, setup falls back to `project_business_manager_email`. If both sources are empty, this
field remains empty until set manually.

**Dependencies:**

- **Primary Settings:**
  - `project_business_manager_email`: Fallback first-init source used when the Agent Creator
    private-dining email is empty or unavailable.
- **Logic Interactions:**
  - `agent_creator_restaurant_private_dining_email`: First-init source used to prefill this
    attribute.
```

**Level:** `Customer`

**Group:** `1. Business`

**Value type:** `string`

### 1. Business - Advanced

#### `project_attributes_restaurant_googlemaps_url`

**Title:** Link (URL) - Google Maps [A]

**Description:**

````md
Use this field for your restaurant's public Google Maps listing URL so customers can quickly access
location and contact details.

**Pro-Tip:** Use a stable public listing link and keep it updated whenever your listing changes.

**Examples:**

```txt
https://maps.google.com/?cid=1234567890123456789
```

**Note:** This field is informational and separate from reservation-link configuration.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into restaurant business-context and technical-context variables so
prompt flows can reference map/listing links during runtime.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_googlemaps_url`. If empty, shared runtime context blocks do not contain a
usable Google Maps URL.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_opentable_url`: Reservation-oriented companion link surfaced in
    shared context blocks.
  - `project_attributes_restaurant_yelp_url`: Listing-oriented companion link surfaced in shared
    context blocks.
- **Logic Interactions:**
  - `agent_creator_restaurant_googlemaps_url`: First-init source used to prefill this attribute.
````

**Level:** `Customer`

**Group:** `1. Business - Advanced`

**Value type:** `string`

**Is hidden:** `true`

#### `project_attributes_restaurant_opentable_url`

**Title:** Link (URL) - OpenTable [A]

**Description:**

````md
Use this field for your restaurant's OpenTable page URL so the Agent can reference an external
reservation path when needed.

**Pro-Tip:** Use the final customer-facing OpenTable URL for the specific venue.

**Examples:**

```txt
https://www.opentable.com/r/example-restaurant
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into restaurant business-context and technical-context variables used by
runtime prompt flows that surface external booking/listing links.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_opentable_url`. If empty, shared runtime context blocks do not contain a
usable OpenTable URL.

**Dependencies:**

- **Primary Settings:**
  - `project_business_address`: Location context commonly paired with external reservation links.
  - `project_business_public_phone`: Contact fallback commonly provided alongside booking links.
- **Logic Interactions:**
  - `agent_creator_restaurant_opentable_url`: First-init source used to prefill this attribute.
  - `project_attributes_restaurant_googlemaps_url`: Companion listing link surfaced in shared
    context blocks.
  - `project_attributes_restaurant_yelp_url`: Companion listing link surfaced in shared context
    blocks.
````

**Level:** `Customer`

**Group:** `1. Business - Advanced`

**Value type:** `string`

**Is hidden:** `true`

#### `project_attributes_restaurant_yelp_url`

**Title:** Link (URL) - Yelp [A]

**Description:**

````md
Use this field for your public Yelp business page URL so the Agent can provide another external
listing source to users.

**Pro-Tip:** Keep the URL tied to the exact branch/location represented by this Agent.

**Examples:**

```txt
https://www.yelp.com/biz/example-restaurant-austin
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into restaurant business-context and technical-context variables used in
prompt flows that include third-party listing references.

**Fallbacks:** On first initialization, this can be copied from `agent_creator_restaurant_yelp_url`.
If empty, shared runtime context blocks do not contain a usable Yelp URL.

**Dependencies:**

- **Primary Settings:**
  - `project_business_address`: Helps align listing references with the configured business
    location.
  - `project_business_public_phone`: Commonly paired with third-party listing references.
- **Logic Interactions:**
  - `agent_creator_restaurant_yelp_url`: First-init source used to prefill this attribute.
  - `project_attributes_restaurant_googlemaps_url`: Companion listing link surfaced in shared
    context blocks.
  - `project_attributes_restaurant_opentable_url`: Companion booking/listing link surfaced in shared
    context blocks.
````

**Level:** `Customer`

**Group:** `1. Business - Advanced`

**Value type:** `string`

**Is hidden:** `true`

### 3. Knowledge Base

#### `project_attributes_restaurant_menu`

**Title:** 3-07. Restaurant Menu [A]

**Description:**

````md
This is your full restaurant menu content. It helps the Agent answer dish questions and provide more
accurate menu recommendations.

**Pro-Tip:** Keep each item structured (dish name, short description, category, and price). Clear
formatting improves downstream menu summarization and retrieval quality.

**Examples:**

```txt
- **Margherita Pizza**
Description: Classic Italian pizza with tomato sauce, fresh mozzarella, and basil.
Category: Main Course.
Price: $12.99.
- **New York Cheesecake**
Description: A creamy, rich cheesecake with a crunchy base.
Category: Desserts.
Price: $7.50.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This field is the source menu input for restaurant workflows. The system generates
a menu overview from it and appends menu content into AKB topics for retrieval workflows.

**Fallbacks:** On first initialization, this can be copied from `agent_creator_restaurant_menu`. If
empty, menu overview generation and menu-based retrieval regeneration do not run during that refresh
cycle.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_menu_overview`: Advanced system configuration generated from this
    menu and consumed in restaurant business context.
  - `project_attributes_restaurant_menu_url`: Advanced system configuration that stores a menu link
    and is surfaced in shared restaurant context blocks.
- **Logic Interactions:**
  - `agent_creator_restaurant_menu`: First-init source used to prefill this attribute.
  - `project_attributes_restaurant_signature_dishes`: Used alongside the full menu for
    recommendation-style responses.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

#### `project_attributes_restaurant_regular_events_schedule`

**Title:** 3-08. Restaurant Regular Events - Schedule [A]

**Description:**

````md
Use this field for recurring event schedules (for example, live music nights, tasting events, or
weekly specials programming).

**Best Practice:** For each event, include name, a short description, recurrence pattern, time
window, and booking conditions.

**Examples:**

```txt
**Live Music:** Every Friday from 7:00 PM to 10:00 PM. Performances by local jazz musicians. Free entry.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into restaurant business-context prompts so the Agent can answer event
availability/schedule questions.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_regular_events_schedule`. If no recurring events are configured, the field
remains empty.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_regular_events_schedule_url`: Companion events-link setting
    surfaced alongside this schedule in shared restaurant context blocks.
- **Logic Interactions:**
  - `agent_creator_restaurant_regular_events_schedule`: First-init source used to prefill this
    attribute.
  - `project_attributes_terms_and_conditions`: Surfaced in the same shared restaurant context and
    commonly used to provide related event-policy details.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

#### `project_attributes_restaurant_signature_dishes`

**Title:** 3-09. Restaurant Signature Dishes [A]

**Description:**

````md
This field lists the restaurant's signature or best-known dishes. It helps the Agent quickly surface
your top recommendations.

**Best Practice:** Keep this focused and curated (for example, top 5-15 dishes) instead of copying
the entire menu. For each item, ideally include the dish name, a short description, and category.

**Examples:**

```txt
- **Tom Yum Kung** – Traditional Thai soup with shrimp, coconut milk, and aromatic spices.
- **Pasta Carbonara** – Classic Italian pasta with a sauce made from eggs, Pecorino cheese, and pancetta.
- **New York Cheesecake** – A creamy dessert made with rich cream cheese and a crunchy biscuit base.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into restaurant business-context prompts as a dedicated recommendation
section, separate from full-menu representation.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_signature_dishes`. If the source value is empty, this field remains
unconfigured and the signature-dishes section in shared restaurant context has no custom entries.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_menu_overview`: Advanced system configuration surfaced in the
    same shared restaurant context as this field to provide broader menu summary.
  - `project_attributes_restaurant_menu`: Source field used to generate
    `project_attributes_restaurant_menu_overview`, which is shown alongside signature dishes.
- **Logic Interactions:**
  - `agent_creator_restaurant_signature_dishes`: First-init source used to prefill this attribute.
  - `project_attributes_current_specials`: Surfaced in the same shared restaurant context as a
    separate promotions section.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

### 3. Knowledge Base - Advanced

#### `project_attributes_restaurant_menu_overview`

**Title:** Restaurant Menu Overview [C]

**Description:**

````md
Auto-generated summary of your restaurant menu used for faster menu-aware responses.

**Pro-Tip:** Update the full Restaurant Menu field when menu items change. This overview is
regenerated from that source.

**Examples:**

```txt
Top categories: Starters, Mains, Desserts.
Popular dishes: Tom Yum Kung, Pasta Carbonara, New York Cheesecake.
Service highlights: Vegetarian options available.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Generated from the full restaurant menu and injected into restaurant business
context for compact, high-signal menu guidance.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_menu_overview`. If the source restaurant menu is empty, overview
generation does not run and this field remains empty/placeholder. Regeneration is also skipped when
the menu content has not changed since the previous processed version.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_menu`: Source field used to build this overview.
- **Logic Interactions:**
  - `agent_creator_restaurant_menu_overview`: First-init source used to prefill this attribute
    before menu overview regeneration runs.
  - `project_attributes_restaurant_signature_dishes`: Complements overview answers with curated
    featured dishes.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base - Advanced`

**Value type:** `string`

**Is hidden:** `true`

#### `project_attributes_restaurant_menu_url`

**Title:** Link (URL) - Menu [B]

**Description:**

````md
Public URL where customers can view your restaurant menu online.

**Pro-Tip:** Keep this URL current, and continue maintaining the full Restaurant Menu field for best
retrieval quality.

**Examples:**

```txt
https://www.example.com/menu
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into restaurant business-context and technical-context variables as the
menu-link reference used by runtime prompt flows.

**Fallbacks:** On first initialization, this can be copied from `agent_creator_restaurant_menu_url`.
If empty, a placeholder is stored and no usable menu URL is provided.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_menu`: Full menu content source used for retrieval and overview
    generation in related restaurant menu logic.
- **Logic Interactions:**
  - `agent_creator_restaurant_menu_url`: First-init source used to prefill this attribute.
  - `project_attributes_restaurant_menu_overview`: Generated from full menu content; not currently
    auto-generated from this URL.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base - Advanced`

**Value type:** `string`

**Is hidden:** `true`

#### `project_attributes_restaurant_regular_events_schedule_url`

**Title:** Restaurant Regular Events - Schedule Link (URL) [B]

**Description:**

````md
Public URL where customers can view your recurring events schedule.

**Pro-Tip:** Include this link if events are updated frequently, and keep the text-based schedule
field aligned with major changes.

**Examples:**

```txt
https://www.example.com/events
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into restaurant business-context and technical-context variables so the
Agent can share event schedule links during conversations.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_regular_events_schedule_url`. If empty, the Agent has no usable events URL
to provide.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_regular_events_schedule`: Text schedule field used as main events
    knowledge context.
- **Logic Interactions:**
  - `agent_creator_restaurant_regular_events_schedule_url`: First-init source used to prefill this
    attribute.
  - `project_attributes_current_specials`: Injected into the same shared restaurant business-context
    block, so both events and specials are available in conversation context.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base - Advanced`

**Value type:** `string`

**Is hidden:** `true`

### 4. Agent Behavior

#### `project_attributes_restaurant_catering_questions`

**Title:** 4-20. Catering - Questions [B]

**Description:**

```md
Define the catering-specific questions the Agent should ask before routing or confirming next steps.

**Best Practice:** If catering is unavailable, state that explicitly in this field so the Agent does
not imply support.

**Examples:**

- "What is the event address? We service locations within 50 miles from [your city]."
- "Sorry, we do not provide catering services."

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into the restaurant "Make a Large Reservation" scenario as the
catering-specific question set. This branch is used when that scenario runs and the request is
handled as catering. In the default intent map, standalone catering intents can also be routed to a
direct "not offered" response path instead of this scenario.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_catering_questions`. If empty, setup uses a neutral placeholder.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_large_group_reservation_minimum_party_size`: For party-size
    reservation requests, this threshold helps route into the large-reservation scenario where this
    catering branch can be used.
- **Logic Interactions:**
  - `agent_creator_restaurant_catering_questions`: First-init source used to prefill this attribute.
  - `project_attributes_restaurant_private_dining_questions`: Used in the same scenario for
    private-dining branch logic.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_restaurant_large_group_reservation_minimum_party_size`

**Title:** 4-21. Large Group Reservation - Minimum Party Size [A] [IMPORTANT]

**Description:**

```md
Set the guest-count threshold where regular reservations switch to large-reservation handling.

**Best Practice:** Keep this exactly aligned with your booking platform/POS threshold. If this is
wrong, users may be sent down the wrong reservation path.

Behavior examples:

- **`7`:** 1-6 guests stay in regular flow; 7+ uses large-reservation flow.
- **`10`:** 1-9 guests stay in regular flow; 10+ uses large-reservation flow.

How to set it:

1. Check your booking platform/POS setting for maximum regular-party size.
2. Use that same number here as the large-group minimum.
3. If you rely on Google Booking and do not have POS access, open the Google Booking reservation
   link and note the highest guest count still allowed as a regular booking.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This value is injected into restaurant intent maps, ITM definitions, regular
reservation scenarios, and large reservation scenarios to control `<` vs `>=` branching. It is also
inserted into restaurant reservation-constraint text that updates
`project_attributes_setting_transfer_call_criteria` and
`project_attributes_setting_additional_limitations_and_restrictions`. In default restaurant
availability setup, it is embedded in
`project_attributes_setting_booking_check_availability_validation_schema_template` (the
`regularGroup` rule), then compiled into the availability schema consumed by check-availability
flows.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_large_group_reservation_minimum_party_size`. If empty, setup uses the
restaurant default threshold.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_large_group_reservation_questions`: Used when group size is
    at/above this threshold.
  - `project_attributes_setting_booking_check_availability_validation_schema_template`: Restaurant
    validation schema includes this threshold for regular-group classification.
- **Logic Interactions:**
  - `agent_creator_restaurant_large_group_reservation_minimum_party_size`: First-init source used to
    prefill this attribute.
  - `project_attributes_restaurant_regular_reservation_via_link_guidance_instruction`: Used in the
    below-threshold regular-link flow.
  - `project_attributes_setting_transfer_call_criteria`: Restaurant transfer criteria text includes
    this threshold for small-party booking constraints.
  - `project_attributes_setting_additional_limitations_and_restrictions`: Restaurant limitation text
    includes this threshold for small-party booking constraints.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `number`

#### `project_attributes_restaurant_large_group_reservation_questions`

**Title:** 4-22. Large Group Reservation - Questions [B]

**Description:**

````md
Define the additional questions the Agent should ask when a request qualifies as a large
reservation.

**Pro-Tip:** Ask only details needed by your team for manual follow-up and feasibility review.

**Examples:**

```txt
What is the occasion? Do you have any special accommodation requests?
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Inserted into the large-reservation scenario when the branch is identified as
large-party booking (not private dining or catering).

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_large_group_reservation_questions`. If empty, setup uses the restaurant
default optional question prompt.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_large_group_reservation_minimum_party_size`: Controls when this
    field is used.
- **Logic Interactions:**
  - `agent_creator_restaurant_large_group_reservation_questions`: First-init source used to prefill
    this attribute.
  - `project_attributes_restaurant_private_dining_questions`: Alternate branch in the same
    large-reservation scenario.
  - `project_attributes_restaurant_catering_questions`: Alternate branch in the same
    large-reservation scenario.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_restaurant_order_url`

**Title:** 4-23. Link (URL) - Order [A] [IMPORTANT]

**Description:**

```md
Set the URL where customers can place pickup/delivery food orders online.

**Best Practice:** Provide a valid direct ordering URL and verify it resolves correctly without
login barriers.

**Examples:**

- `https://order.yourrestaurant.com/menu`
- `https://www.yourrestaurant.com/order`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Included in restaurant business/tech context and consumed by initialization logic
that validates/refines this URL format. Restaurant transfer and limitation criteria are also
auto-adjusted based on whether this URL exists.

**Fallbacks:** On first initialization, this can be prefilled from
`agent_creator_restaurant_order_url`. Invalid URLs are cleared during normalization. If empty,
order-related self-serve assumptions are removed from default criteria.

**Dependencies:**

- **Primary Settings:**
  - None. This attribute does not require another customer-facing setting before it can be
    initialized or used.
- **Logic Interactions:**
  - `agent_creator_restaurant_order_url`: First-init source for this field.
  - `project_attributes_setting_transfer_call_criteria`: Restaurant initialization adds/removes
    order-transfer criteria based on this URL.
  - `project_attributes_setting_additional_limitations_and_restrictions`: Restaurant initialization
    adds/removes order limitations based on this URL.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_restaurant_private_dining_questions`

**Title:** 4-24. Private Dining - Questions [B]

**Description:**

```md
Define the private-dining questions the Agent should ask before routing or follow-up.

**Best Practice:** If private dining is not offered, say so explicitly here to avoid false
expectations.

**Examples:**

- "What is the occasion? Do you have any special accommodation requests?"
- "Sorry, we do not provide private dining."

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Inserted into the large-reservation scenario when the request branch is private
dining.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_private_dining_questions`. If empty, setup uses a neutral placeholder.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_large_group_reservation_minimum_party_size`: One entry path into
    the large-reservation scenario is threshold-based (`>=` minimum party size), where this private-
    dining branch can be used. Private-dining intent routing can also enter the same
    large-reservation scenario, independent of party-size threshold checks.
- **Logic Interactions:**
  - `agent_creator_restaurant_private_dining_questions`: First-init source used to prefill this
    attribute.
  - `project_attributes_restaurant_large_group_reservation_questions`: Alternate branch in the same
    large-reservation scenario.
  - `project_attributes_restaurant_catering_questions`: Alternate branch in the same
    large-reservation scenario.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

#### `project_attributes_restaurant_regular_reservation_via_link_guidance_instruction`

**Title:** 4-25. Regular Reservation - Self-Reservation Link (URL) - Guidance Instruction [B]

**Description:**

````md
Define the spoken guidance the Agent should use when helping guests complete a reservation through
your booking link.

**Best Practice:** Write this in simple chronological steps that match your real booking form
screens.

**Examples:**

```txt
Open the link, specify your full name, the amount of guests, select time and date. Then, press
Submit.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Inserted into the "Make a Regular Table Booking via Link" scenario after link
delivery and confirmation that the guest opened the page. This guidance is specific to that scenario
variant. In default restaurant routing, regular reservations can also be directed to the "Make a
Regular Table Booking via Website Link" variant, which sends the booking link without using this
guidance field.

**Fallbacks:** On first initialization, this can be copied from
`agent_creator_restaurant_regular_reservation_via_link_guidance_instruction`. If empty, setup uses a
neutral placeholder.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_large_group_reservation_minimum_party_size`: Determines whether
    reservation remains in regular-link flow where this guidance is used.
- **Logic Interactions:**
  - `agent_creator_restaurant_regular_reservation_via_link_guidance_instruction`: First-init source
    used to prefill this attribute.
  - `project_attributes_restaurant_order_url`: Related URL capabilities can change
    transfer/limitation behavior in the same restaurant runtime setup.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior`

**Value type:** `string`

### 4. Agent Behavior - Advanced

#### `project_attributes_private_dynamic_restaurant_google_restaurant_id`

**Title:** Restaurant Google Booking ID [C] [IMPORTANT]

**Description:**

```md
This internal field stores the Google reservation restaurant ID used for default restaurant
availability checks and booking execution.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

The system typically derives this value from your Google reservation URL. If default Google booking
is not working, verify that the reservation URL is valid so this ID can be regenerated.

**Examples:**

- From `https://www.google.com/maps/reserve/v/dine/c/XXXXXXXXXXX`, the stored ID is `XXXXXXXXXXX`.
- Alternative supported Google reservation link formats are normalized and the same ID is extracted.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime processing reads
`project_attributes_restaurant_googlemaps_reservation_url`, validates supported Google reservation
URL formats, normalizes accepted links to canonical `/maps/reserve/v/dine/c/{id}`, and stores the
extracted `{id}` in this attribute. The value is then injected into default restaurant availability
payloads as `restaurantId`, used in default booking URL assembly, and included in reservation
task-context generation with seating options.

**Fallbacks:** If the reservation URL is empty, invalid, or cannot produce a valid ID, this
attribute is reset to empty and dependent reservation task-context data is cleared. If the source
URL did not change and both this ID and its task context are already populated, existing values are
reused without regeneration.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_googlemaps_reservation_url`: Source value parsed to derive this
    ID.
  - `project_attributes_setting_booking_check_availability_type`: In `default` mode, availability
    checks require a non-empty ID.
  - `project_attributes_setting_booking_type`: In `default` mode, booking execution requires a
    non-empty ID.
- **Logic Interactions:**
  - `project_attributes_private_dynamic_restaurant_google_restaurant_seating_options`: Combined with
    this ID when building reservation task context.
  - `project_attributes_task_context_w1s3_reserve_table_task`: Regenerated and cleared together with
    this ID.
  - `project_business_industry`: Restaurant runtime branches consume this attribute.
```

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

#### `project_attributes_private_dynamic_restaurant_google_restaurant_seating_options`

**Title:** Restaurant Google Booking Seating Options [C]

**Description:**

````md
This internal field stores seating area options (for example indoor, patio, or bar) discovered from
Google reservation availability results.

**Note:** This is a system-managed internal attribute. Its value is generated and updated
automatically and can be overwritten by runtime workflows. Do not edit this attribute manually.

The Agent uses this value to keep reservation task context aligned with currently known seating
locations.

**Examples:**

```json
["Main Dining", "Patio", "Bar"]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During restaurant availability-result processing, runtime reads location labels
from received slots and updates this attribute as JSON. If the field is empty (or `[]`), it is
initialized from current locations. If it already contains data, new unique locations are appended
to the existing JSON array. The final value is also embedded into reservation task context together
with the Google restaurant ID.

**Fallbacks:** Initialization sets this field to an empty placeholder value when unset. If
availability handling does not run, the value remains unchanged. When there are no returned
availability slots, seating-option refresh is skipped for that response.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Seating-option updates run only in restaurant-industry availability
    branches.
- **Logic Interactions:**
  - `project_attributes_task_context_w1s3_reserve_table_task`: Regenerated with this seating-options
    JSON.
  - `project_attributes_private_dynamic_restaurant_google_restaurant_id`: Included alongside seating
    options in the same task context.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `json`

**Is hidden:** `true`

#### `project_attributes_task_context_w1s3_reserve_table_task`

**Title:** Restaurant Reserve Table Task Context [C]

**Description:**

````md
This internal context field stores reservation details used by the booking worker during the
"Reserve Table" execution step.

**Pro-Tip:** Do not edit this value manually. If booking context appears outdated, refresh
reservation setup and run a new availability check so the system can rebuild it.

**Examples:**

```txt
**Google Restaurant ID:** *XXXXXXXXXXX*. **Seating options:** *[
  "Main Dining",
  "Patio"
]*
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime composes and updates this string context for task
`w1s3_reserve_table_task`. During booking execution, the worker resolves
`project_attributes_task_context_{task_idn}` into `TASK_CONTEXT`, so this attribute becomes the
context block used when selecting seating/time-slot options and completing reservation actions.

**Fallbacks:** If reservation URL processing determines the Google booking setup is empty or
invalid, this attribute is cleared. If the reservation URL is unchanged and valid context already
exists, regeneration is skipped. After successful restaurant availability responses, the value is
refreshed with the latest seating context.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_restaurant_googlemaps_reservation_url`: Source setting that controls whether
    reservation task context can be generated or must be cleared.
- **Logic Interactions:**
  - `project_business_industry`: Restaurant-specific availability-processing branches refresh this
    context.
````

**Level:** `Customer`

**Group:** `4. Agent Behavior - Advanced`

**Value type:** `string`

**Is hidden:** `true`

### 5. Reports

#### `project_attributes_restaurant_bill_average_order`

**Title:** 5-09. ASR - Average Bill Amount For Food Order [A]

**Description:**

```md
Estimated average revenue from a single food order. This is used to value order-type conversations
in restaurant ASR reporting.

**Pro-Tip:** Use your recent POS average ticket for order channels (not dine-in table averages) and
review it monthly.

**Examples:**

- Higher value increases potential revenue reported for order conversations.
- Lower value makes order revenue analytics more conservative.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** In the restaurant revenue model, this value is used as `fixed_potential_revenue`
for the `order` category.

**Fallbacks:** Initialized to a restaurant default when empty. Runtime model assembly also applies a
numeric fallback if this attribute is blank.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: This field is consumed only in restaurant-specific revenue model
    logic.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `number`

#### `project_attributes_restaurant_bill_average_per_person_catering`

**Title:** 5-10. ASR - Average Bill Amount For Catering Per Person [A]

**Description:**

```md
Expected per-guest catering spend benchmark used in restaurant ASR revenue configuration.

**Pro-Tip:** Set this from real catering invoices per person and review it together with your
regular-reservation per-person value, because current runtime logic uses that value for the active
catering per-person constant.

**Examples:**

- `45`
- `60`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During restaurant revenue-model preparation, runtime reads this value into the
catering configuration context. In the current default implementation, the active catering formula
constant `average_bill_per_person` is sourced from
`project_attributes_restaurant_bill_average_per_person_regular_reservation`, so this field is
currently loaded but not applied to final per-person catering calculations.

**Fallbacks:** Initialized to a restaurant default when empty. Runtime loading falls back to
`project_attributes_restaurant_bill_average_per_person_regular_reservation` when this field is
blank.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: This field applies to restaurant revenue model configuration.
- **Logic Interactions:**
  - `project_attributes_restaurant_bill_average_per_person_regular_reservation`: Used as fallback
    source when this value is empty and currently used as the active catering per-person constant.
  - `project_attributes_restaurant_bill_minimum_large_group_reservation`: Currently used as the
    `min_value` floor in the catering category of the default restaurant revenue model.

**Notes:** In the current default restaurant revenue model implementation, the catering formula uses
the regular-reservation per-person value at runtime.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `number`

#### `project_attributes_restaurant_bill_average_per_person_large_group_reservation`

**Title:** 5-11. ASR - Average Bill Amount For Large Group Reservation Per Person [A]

**Description:**

```md
Expected spend per guest for large-party reservations.

**Pro-Tip:** Base this on actual large-party checks, not standard table averages, since group
ordering patterns are often different.

**Examples:**

- Higher value raises potential revenue for large reservation conversations.
- Lower value reduces projected revenue for those conversations.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used as the per-person constant in the `large_reservation` restaurant revenue
formula.

**Fallbacks:** Initialized with a restaurant default when empty. Runtime loading falls back to
`project_attributes_restaurant_bill_average_per_person_regular_reservation` if blank.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: This field is consumed in restaurant-specific revenue formulas.
- **Logic Interactions:**
  - `project_attributes_restaurant_bill_average_per_person_regular_reservation`: Fallback source for
    missing value.
  - `project_attributes_restaurant_bill_minimum_large_group_reservation`: Minimum floor applied to
    large reservation potential revenue.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `number`

#### `project_attributes_restaurant_bill_average_per_person_private_dining`

**Title:** 5-12. ASR - Average Bill Amount For Private Dining Per Person [A]

**Description:**

```md
Expected per-guest private-dining spend benchmark used in restaurant ASR revenue configuration.

**Pro-Tip:** Set this from real private-dining checks per person and review it together with your
private-dining minimum-revenue settings.

**Examples:**

- `50`
- `75`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During restaurant revenue-model preparation, runtime reads this value into the
private-dining configuration context. In the current default `private_dining` model, the
`average_bill_per_person` constant is resolved from the regular-reservation per-person value
(`project_attributes_restaurant_bill_average_per_person_regular_reservation`), so this field is
loaded for preparation but is not currently applied as the final private-dining per-person
constant.

**Fallbacks:** Initialized to a restaurant default when empty. Runtime loading falls back to
`project_attributes_restaurant_bill_average_per_person_regular_reservation` when blank, but the
current default `private_dining` model already resolves `average_bill_per_person` from that
regular-reservation value instead of this field.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Controls whether restaurant revenue logic is used.
- **Logic Interactions:**
  - `project_attributes_restaurant_bill_average_per_person_regular_reservation`: Fallback source for
    missing value while this field is being loaded into the private-dining context.
  - `project_attributes_restaurant_bill_minimum_large_group_reservation`: Currently used as the
    `min_value` floor in the private-dining category of the default restaurant revenue model.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `number`

#### `project_attributes_restaurant_bill_average_per_person_regular_reservation`

**Title:** 5-13. ASR - Average Bill Amount For Regular Reservation Per Person [A]

**Description:**

```md
Expected spend per guest for standard table reservations.

**Pro-Tip:** Treat this as your baseline dine-in per-person value. Keep it aligned with current menu
pricing and typical party behavior.

**Examples:**

- Higher value increases estimated revenue for regular reservation conversations.
- Lower value reduces estimated revenue and may understate opportunity value.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used directly as the per-person constant in `regular_table_booking` revenue
calculations. In the current default restaurant revenue model implementation, this value is also the
active per-person constant used in `catering`. The default `private_dining` model also resolves this
numeric value into its final `average_bill_per_person` constant.

**Fallbacks:** Initialized to a restaurant default when empty. Runtime formula loading also applies
this as the fallback source for other per-person restaurant attributes while their model constants
are being prepared.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines activation of restaurant revenue model logic.
- **Logic Interactions:**
  - `project_attributes_restaurant_bill_average_per_person_catering`: In current default runtime
    logic, catering calculations resolve through this value as the active per-person constant.
  - `project_attributes_restaurant_bill_average_per_person_large_group_reservation`: Falls back to
    this value when empty.
  - `project_attributes_restaurant_bill_average_per_person_private_dining`: Blank private-dining
    input falls back to this value during loading, but the current default `private_dining` model
    resolves this value, not the private-dining field, into the final per-person constant.
  - `project_attributes_setting_asr_average_lead_value`: Used as `zero_default` floor in regular
    reservation revenue outcomes.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `number`

#### `project_attributes_restaurant_bill_minimum_catering`

**Title:** 5-14. ASR - Minimum Bill Amount For Catering [A]

**Description:**

```md
Configured minimum catering revenue threshold stored for restaurant ASR setup.

**Pro-Tip:** Keep this aligned with your catering policy targets, and review it together with
`project_attributes_restaurant_bill_minimum_large_group_reservation`, because current default
runtime applies that floor to catering calculations.

**Examples:**

- `900`
- `1200`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Loaded into restaurant revenue-model configuration as the catering minimum
setting. In the current default runtime implementation, the active catering `min_value` is sourced
from `project_attributes_restaurant_bill_minimum_large_group_reservation`.

**Fallbacks:** Initialized to a restaurant default when empty. Runtime model loading applies a
numeric fallback if blank.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: This setting belongs to restaurant revenue logic.
- **Logic Interactions:**
  - `project_attributes_restaurant_bill_average_per_person_catering`: Related catering per-person
    configuration loaded in the same revenue-model setup.
  - `project_attributes_restaurant_bill_minimum_large_group_reservation`: Current default runtime
    model uses the large-group minimum as the active floor for the catering category.

**Notes:** In the current default restaurant revenue model implementation, this attribute is loaded
but not applied as the active catering `min_value`.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `number`

#### `project_attributes_restaurant_bill_minimum_large_group_reservation`

**Title:** 5-15. ASR - Minimum Bill Amount For Large Group Reservation [A]

**Description:**

```md
Minimum revenue floor for large-party reservation opportunities.

**Pro-Tip:** Choose a floor that matches your real minimums for staffing, room usage, or group
service overhead.

**Examples:**

- Higher minimum raises projected value for low-spend large-party inquiries.
- Lower minimum keeps projections closer to strict per-person multiplication.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Applied as `min_value` in the `large_reservation` revenue category.

**Fallbacks:** Restaurant initialization commonly sets this value directly. Runtime revenue-model
assembly also applies a numeric fallback when blank.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Enables restaurant-specific revenue computation branches.
- **Logic Interactions:**
  - `project_attributes_restaurant_bill_average_per_person_large_group_reservation`: Combined with
    this minimum to calculate large-reservation potential revenue.
  - `project_attributes_restaurant_bill_minimum_catering`: Catering minimum settings are related,
    but current default runtime behavior also reuses this large-group minimum for catering.
  - `project_attributes_restaurant_bill_minimum_private_dining`: Private-dining minimum settings are
    related, but current default runtime behavior also reuses this large-group minimum for private
    dining.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `number`

#### `project_attributes_restaurant_bill_minimum_private_dining`

**Title:** 5-16. ASR - Minimum Bill Amount For Private Dining [A]

**Description:**

```md
Configured minimum private-dining revenue threshold stored for restaurant ASR setup.

**Pro-Tip:** Keep this aligned with your private-dining policy targets, and review it together with
`project_attributes_restaurant_bill_minimum_large_group_reservation`, because current default
runtime applies that floor to private-dining calculations.

**Examples:**

- `1000`
- `1500`

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Loaded into restaurant revenue-model configuration as the private-dining minimum
setting. In the current default runtime implementation, the active private-dining `min_value` is
sourced from `project_attributes_restaurant_bill_minimum_large_group_reservation`.

**Fallbacks:** Initialized to a restaurant default when empty. Runtime loading applies a numeric
fallback if blank.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Restricts usage to restaurant-specific revenue model flows.
- **Logic Interactions:**
  - `project_attributes_restaurant_bill_average_per_person_private_dining`: Related private-dining
    per-person configuration loaded in the same revenue-model setup.
  - `project_attributes_restaurant_bill_minimum_large_group_reservation`: Current default runtime
    model applies large-group minimum as the active private-dining floor.

**Notes:** In the current default restaurant revenue model implementation, this attribute is loaded
but not applied as the active private-dining `min_value`.
```

**Level:** `Customer`

**Group:** `5. Reports`

**Value type:** `number`

### 8. System

#### `project_attributes_private_feature_flag_booking_use_new_restaurant_availability_check_approach`

**Title:** Feature Flag - Booking - Use New Restaurant Availability Check Approach [C]

**Description:**

```md
This setting controls which default restaurant availability-check route is attempted first.

**Best Practice:** Keep this enabled unless you intentionally need the legacy availability-check
routing.

Behavior by value:

- **Enabled (`True`):** For restaurant sessions in default availability mode, runtime sends
  availability requests through the new restaurant availability command route.
- **Disabled (`False`):** Runtime skips that new route and continues with standard availability
  request routing.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This flag is evaluated only when `project_business_industry` is
`restaurant_industry` and `project_attributes_setting_booking_check_availability_type` is `default`.
The flag check is strict: only exact value `"True"` activates the new route. When active,
availability requests are sent through the new restaurant command path for
`targetAction="check_availability"`.

**Fallbacks:** Restaurant initialization sets this flag to `True` when empty. If the value is not
exactly `"True"` (including empty), runtime treats the flag as inactive and falls through to the
standard availability routing path based on configured availability type.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Limits this behavior to restaurant availability flow.
  - `project_attributes_setting_booking_check_availability_type`: New route is considered only when
    value is `default`.
- **Logic Interactions:**
  - `project_attributes_setting_booking_check_availability_url`: Used by standard HTTP routing when
    new route is inactive.
  - `project_attributes_setting_booking_check_availability_request_http_method`: Controls HTTP
    method for standard request routing.
  - `project_attributes_setting_booking_check_availability_request_headers`: Supplies HTTP headers
    for standard request routing.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`

#### `project_attributes_private_feature_flag_booking_use_new_restaurant_create_booking_approach`

**Title:** Feature Flag - Booking - Use New Restaurant Create Booking Approach [C]

**Description:**

```md
This setting controls which default restaurant create-booking approach is used first.

**Best Practice:** Keep this enabled unless you intentionally rely on the older restaurant booking
workflow.

Behavior by value:

- **Enabled (`True`):** New restaurant create-booking approach is primary.
- **Disabled (`False`):** Old legacy restaurant create-booking approach is primary.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Applies to restaurant create-booking flow selection when
`project_attributes_setting_booking_type` is `default`. The flag check is strict: only exact value
`"True"` activates the new default restaurant create-booking route. When inactive, runtime uses the
old legacy restaurant booking route.

Even when enabled, failed booking attempts can still fallback to the old legacy approach when
`project_attributes_setting_booking_fallback_processing_type` is `default`.

**Fallbacks:** Restaurant initialization sets this flag to `True` by default. If the value is not
exactly `"True"` (including empty), runtime treats the flag as inactive.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: This flag behavior is relevant to restaurant booking flow logic.
  - `project_attributes_setting_booking_type`: This behavior applies when booking type is `default`
    in restaurant flow.
  - `project_attributes_setting_booking_fallback_processing_type`: Controls whether failed primary
    attempts continue into built-in fallback handling.
- **Logic Interactions:**
  - `project_attributes_setting_booking_payload_schema_template`: New approach relies on
    schema-based booking payload generation.
  - `project_attributes_restaurant_googlemaps_reservation_url`: New default restaurant
    create-booking payload includes this reservation URL.
  - `project_business_time_zone`: New default restaurant create-booking payload includes this
    timezone value.
```

**Level:** `Customer`

**Group:** `8. System`

**Value type:** `bool`

**Is hidden:** `true`
