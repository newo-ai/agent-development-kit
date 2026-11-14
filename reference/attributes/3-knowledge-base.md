# 3. Knowledge Base

Back to the [attribute index](index.md).

## `project_attributes_products_and_services`


**Title:** 3-01. Products & Services [A]

**Description:**

````md
This is the main catalog of what your business offers. Agents use it to answer questions, suggest
options, and decide whether a request can be handled.

**Pro-Tip:** Keep entries concise and structured (name, short description, optional price). For very
large catalogs, keep only high-level highlights here and move long reference material into Text
Memory or Website Memory.

**Examples:**

```txt
Deep Cleaning
Description: Full-home deep cleaning for kitchens, bathrooms, and high-touch surfaces.
Price: Starting at $220
```

```txt
Invisalign Consultation
Description: Initial orthodontic assessment with clear aligner candidacy review.
```

```txt
Solar Panel Installation
Description: Residential rooftop solar system setup and activation.
Payment link: https://example.com/pay/solar-install
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This field is processed into an internal runtime catalog that powers
service-availability checks and business-context instructions used by customer-facing flows.

**Fallbacks:** On initialization, the system attempts to prefill this from Agent Creator intake for
most industries. If both this field and the explicit not-offered list stay empty (or only
whitespace), the generated runtime catalog remains blank until you add values.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_products_and_services_not_offering`: Explicit exclusions are merged with
    this catalog.
  - `project_attributes_setting_products_and_services_structured_representation_enabled`: Advanced
    system configuration that switches between plain-text and structured parsing modes.
- **Logic Interactions:**
  - `project_business_industry`: Initialization behavior differs by industry during first setup.
  - `project_attributes_rag_knowledge_base_append_text`: Use this to append long, text-based
    knowledge without overloading turn-level context.
  - `project_attributes_rag_knowledge_base_append_websites`: Use this to append knowledge extracted
    from websites without overloading turn-level context.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

---

## `project_attributes_products_and_services_not_offering`


**Title:** 3-02. Unavailable Products & Services [A]

**Description:**

````md
This field lists offerings your business does not provide. It helps Agents avoid promising services
you cannot deliver.

**Best Practice:** Keep this list short and explicit. Add only hard exclusions that should trigger a
clear "we do not offer this" response.

**Examples:**

```txt
- Emergency surgery
- Same-day installation
- 24/7 on-site support
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** This value is merged with the main Products & Services catalog before runtime
service matching. It directly influences whether a requested service is treated as unavailable.

**Fallbacks:** The field is initialized as empty/whitespace. If left empty, no explicit exclusions
are applied.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_products_and_services`: Main catalog that this exclusion list modifies.
- **Logic Interactions:**
  - `project_attributes_setting_products_and_services_structured_representation_enabled`: Advanced
    system configuration that affects how offering and non-offering lists are normalized.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

---

## `project_attributes_current_specials`


**Title:** 3-03. Specials [A]

**Description:**

````md
Use this field for active promotions, discounts, and limited-time offers you want the Agent to
mention.

**Pro-Tip:** Include dates or conditions (for example, "weekdays only" or "expires March 31") so the
Agent can present offers accurately.

**Examples:**

```txt
Get 15% off your next booking through March 31.
```

```txt
Happy Hour: 4:00 PM-6:00 PM, Monday-Friday.
Buy one appetizer, get one 50% off.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into business-context prompts and pricing-reasoning flows so the Agent
can factor promotions into responses and cost explanations.

**Fallbacks:** Initialized as empty/whitespace. When empty, no promotional context is applied.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_calculation_context`: Pricing context consumed alongside specials in
    calculator flows.
  - `project_attributes_setting_calculation_rules`: Output/rules configuration used when pricing
    logic references promotions.
- **Logic Interactions:**
  - `project_attributes_current_specials_url`: Advanced system configuration stored for future
    URL-based specials ingestion; currently not auto-applied in runtime calculations.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

---

## `project_attributes_faq`


**Title:** 3-04. FAQ [A]

**Description:**

````md
Use this field for common customer questions and your preferred answers. It gives the Agent
ready-to-use responses for recurring requests.

**Best Practice:** Write each item as a direct question with a concise answer. Include escalation
language when human follow-up is required.

**Examples:**

```txt
1. Can I reschedule my appointment?
> Yes. Please share your preferred new date/time and we will confirm availability.

2. Do you accept same-day bookings?
> We can sometimes accommodate same-day requests depending on open slots.

3. I need to file a complaint.
> I am sorry you had this experience. I can collect details and notify a manager immediately.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Included in industry business-context prompts so the Agent can answer high-volume
questions with consistent phrasing.

**Fallbacks:** On first initialization, this can be copied from Agent Creator intake. If it remains
empty, FAQ-specific guidance is simply omitted from context.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines which industry business-context template consumes this
    FAQ block.
- **Logic Interactions:**
  - `project_attributes_terms_and_conditions`: Often used together to separate FAQ responses from
    formal policy/rules content.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

---

## `project_attributes_terms_and_conditions`


**Title:** 3-05. Additional Details and Rules [B]

**Description:**

````md
Use this field for operational rules customers should know before booking or visiting (policies,
access rules, timing, and constraints).

**Pro-Tip:** Keep each rule short and unambiguous. Focus on policies that change customer decisions
or prevent scheduling friction.

**Examples:**

```txt
- Cancellation policy: 24-hour notice required to avoid fees.
- Late arrival policy: Reservations are held for 15 minutes.
- Pet policy: Service animals only.
- Accessibility: Wheelchair-accessible entrance and seating available.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Added to business-context instructions (industry-dependent) and used as policy
ground truth for customer-facing answers.

**Fallbacks:** During initialization, the system may prefill this from Agent Creator intake and/or
industry starter templates. If still empty, policy guidance is omitted until values are provided.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Controls which industry templates seed and consume this field.
- **Logic Interactions:**
  - `project_attributes_faq`: Use FAQ for conversational Q&A and this field for strict policy/rules
    so handoffs stay consistent.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

---

## `project_attributes_rag_knowledge_base_append_text`


**Title:** 3-06-A. RAG - Knowledge Base - Text [A]

**Description:**

````md
Use this field to append text-based knowledge to the Agent without replacing existing memory. It is
best for manuals, policies, scripts, and long-form reference content.

**Best Practice:** Add content in focused batches by topic, then wait for this field to clear before
submitting the next batch. For large payloads, keep each batch reasonably sized (about 100,000
characters or less) to reduce processing failures.

**Examples:**

```txt
# Refund Policy
Customers may request a refund within 30 days of purchase with proof of payment.

# Installation Timeline
Standard installations are completed within 5-7 business days after confirmation.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When the knowledge-base append processing cycle runs and this field contains new
non-empty content, the system converts the text into structured AKB-ready topics, creates new AKB
records labeled `rag_autogenerated_from_text`, writes an audit entry to the text log, and clears
this input field.

**Retrieval Behavior:** Text-appended topics are evaluated alongside website-appended topics by
relevance to the conversation. New text append requests create additional topics; to fully replace
older text-appended content, use the text reset setting before appending.

**Fallbacks:** Initialized as empty/whitespace. Empty input is ignored. If reset is requested, all
text-appended AKB topics are deleted and the reset switch auto-returns to `False`.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_rag_knowledge_base_append_text_log`: Receives append history entries for
    each successful request.
  - `project_attributes_rag_knowledge_base_append_text_reset`: Clears existing text-appended memory
    before new content is applied.
- **Logic Interactions:**
  - `project_attributes_rag_knowledge_base_append_websites`: Website append flow is independent and
    can run in parallel with text append memory.
  - `project_attributes_rag_knowledge_base_append_websites_reset`: Resets only website-appended
    memory and does not clear text-appended memory.
  - `project_business_industry`: Added as AKB label context for appended topics.
  - `project_attributes_scenario`: Added as AKB label context for appended topics.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

---

## `project_attributes_rag_knowledge_base_append_text_log`


**Title:** 3-06-B. RAG - Knowledge Base - Text - Log [A]

**Description:**

```md
This is the running history of text batches you appended to memory. It acts as an audit trail and
easy recovery source.

**Best Practice:** Keep this log intact for traceability. If memory is reset, copy needed sections
from here back into the text append field.

**Note:** System logic appends entries automatically. You can still edit this field manually for
corrections.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Each successful text append writes a timestamped log block using the standard
separator/header format, with newest entries appended at the end.

**Fallbacks:** Initialized as empty/whitespace. If project timezone is missing, timestamps are
generated using UTC.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_rag_knowledge_base_append_text`: Source input whose successful appends are
    recorded here.
  - `project_business_time_zone`: Used to render human-readable log timestamps.
- **Logic Interactions:**
  - `project_attributes_rag_knowledge_base_append_text_reset`: Log remains available for recovery
    after text-memory resets.
  - `project_attributes_rag_knowledge_base_append_websites_log`: Uses the same append-log format and
    rolling cleanup strategy.

**Capacity Notes:** The log uses a rolling window of approximately 180,000 characters. When the
limit is reached, oldest full entries are dropped first.
```

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

---

## `project_attributes_rag_knowledge_base_append_text_reset`


**Title:** 3-06-C. RAG - Knowledge Base - Text - Reset [A]

**Description:**

```md
This switch clears text-appended memory so you can repopulate it cleanly.

**Best Practice:** Turn this on before replacing large or outdated text batches to avoid old and new
versions coexisting.

Behavior:

- **Enabled (`True`):** Deletes all AKB topics labeled `rag_autogenerated_from_text`, clears
  text-append staging, then auto-sets itself back to `False`.
- **Disabled (`False`):** No reset is performed.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Evaluated early in the text append pipeline. Reset is executed before processing
new text input in the same cycle.

**Fallbacks:** Default state is `False`. If set to `True`, auto-reset to `False` happens after reset
completion.

**Warning:** Reset removes active text-appended AKB memory and cannot be undone from runtime state.
Use the text log as your recovery source.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_rag_knowledge_base_append_text`: If new text is present, it is processed
    after reset completes.
  - `project_attributes_rag_knowledge_base_append_text_log`: Reset does not remove append history.
- **Logic Interactions:**
  - `project_attributes_rag_knowledge_base_append_websites_reset`: Independent reset path for
    website-appended memory.
```

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `bool`

---

## `project_attributes_rag_knowledge_base_append_websites`


**Title:** 3-06-D. RAG - Knowledge Base - Websites [A]

**Description:**

````md
Use this field to append knowledge from websites by providing URLs plus extraction instructions.
This is useful for live menus, policy pages, product pages, and other web-hosted content.

**Best Practice:** Point to specific pages (not broad homepages), include your objective, and submit
only the sources relevant to what the Agent should learn next.

**Examples:**

```txt
Website: https://example.com
Objective: Collect information about pricing and services offered
Keywords: pricing, services

Website: https://another-example.com
Objective: Gather details on customer testimonials and reviews
Keywords: testimonials, reviews
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When the append processing cycle detects new website instructions in this field,
the default scraper path sends asynchronous search and extract requests, then accumulates callback
content until the scraper sends its finalization callback. Only after every scraper request has
finished does the system transform the accumulated content into structured AKB-ready topics and
update AKB once with label `rag_autogenerated_from_websites`.

When `project_attributes_private_feature_flag_rag_append_websites_use_native_web_search_tool` is
`True`, the native path instead processes website blocks one at a time through the web-search tool.
After each successful website result, it immediately transforms that result into RAG topics and
updates AKB before retrieving the next website. Native processing does not wait for all submitted
website requests to finish before adding available content to AKB. Both paths log the request and
clear this field after processing.

The scraper path writes its normal request log entry at finalization, immediately before converting
the accumulated callback content. The native path writes one normal request log entry after its
website loop finishes, not one entry per website and not one entry per AKB update.

Only with the scraper path: If the website search/extraction service reports a failure, that failed
callback is not converted into AKB topics. The failed attempt is written to the website append log
with the failed website item. After a failed callback is logged, this field is cleared so the
request does not continue to appear pending.

**Retrieval Behavior:** Website-appended topics are evaluated alongside text-appended topics by
relevance. New website append requests create additional topics; to fully replace older
website-appended content, use the website reset setting before re-appending.

**Fallbacks:** Initialized as empty/whitespace. Empty input is ignored. The feature flag defaults to
`False`, so website requests use the asynchronous scraper. Set it to `True` to use the native
web-search tool one website at a time.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_private_feature_flag_rag_append_websites_use_native_web_search_tool`:
    Selects the web-search implementation instead of the scraper service.
  - `project_attributes_rag_knowledge_base_append_websites_log`: Stores the original website
    requests/instructions after successful processing.
  - `project_attributes_rag_knowledge_base_append_websites_reset`: Clears existing website-appended
    AKB memory before re-appending updated sources.
- **Logic Interactions:**
  - `project_attributes_rag_knowledge_base_append_text`: Text append flow is independent and can be
    used alongside website append memory.
  - `project_attributes_rag_knowledge_base_append_text_reset`: Resets only text-appended memory.
  - `project_business_industry`: Added as AKB label context for appended topics.
  - `project_attributes_scenario`: Added as AKB label context for appended topics.
````

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

---

## `project_attributes_rag_knowledge_base_append_websites_log`


**Title:** 3-06-E. RAG - Knowledge Base - Websites - Log [A]

**Description:**

```md
This is the history of website append requests you submitted (URLs and objectives). It helps you
track what was requested and replay it when needed.

**Best Practice:** Treat this as your replay list. After a reset, copy selected entries back into
the website append field to rebuild web-based memory quickly.

**Note:** System logic appends entries automatically. You can edit this field manually for
corrections when needed.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** The native web-search path writes one normal timestamped entry containing the
original submitted request after it finishes processing all website blocks. It does not write a
separate entry for each website or each AKB update, and it does not write a failed-status entry when
an individual web-search call returns no content.

The scraper path writes one normal timestamped entry containing the original submitted request only
after its finalization callback has received all scraper results. A scraper failure writes a
separate failed-status entry with the error message and the original failed website item when
available (`Website`, `Objective`, and `Keywords`). Technical extract URLs are used only as a
fallback for older in-flight requests that do not carry item context.

**Fallbacks:** Initialized as empty/whitespace. If project timezone is missing, timestamps are
generated using UTC.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_rag_knowledge_base_append_websites`: Source requests that are logged here
    after successful append completion.
  - `project_business_time_zone`: Used for timestamp generation in log headers.
- **Logic Interactions:**
  - `project_attributes_rag_knowledge_base_append_websites_reset`: Log remains available for replay
    even after website memory resets.
  - `project_attributes_rag_knowledge_base_append_text_log`: Shares the same append-log delimiter
    format and rolling cleanup strategy.

**Capacity Notes:** The log uses a rolling window of approximately 180,000 characters. Oldest full
entries are removed first when space is needed.
```

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `string`

---

## `project_attributes_rag_knowledge_base_append_websites_reset`


**Title:** 3-06-F. RAG - Knowledge Base - Websites - Reset [A]

**Description:**

```md
This switch clears website-appended memory so you can re-import refreshed web content.

**Best Practice:** Enable reset before re-crawling heavily changed websites to prevent stale and
updated versions from mixing.

Behavior:

- **Enabled (`True`):** Deletes AKB topics labeled `rag_autogenerated_from_websites`, clears
  website-append staging, and auto-sets itself back to `False`.
- **Disabled (`False`):** No reset is performed.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Evaluated at the start of the website append pipeline. Reset executes before any
new website append request in the same run.

**Fallbacks:** Default state is `False`. If set to `True`, auto-reset to `False` occurs after reset
completion.

**Warning:** Reset removes active website-appended AKB memory and cannot be undone from runtime
state. Use the website log as your replay source.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_rag_knowledge_base_append_websites`: If new website instructions are present
    after reset, they are processed as a fresh append request.
  - `project_attributes_rag_knowledge_base_append_websites_log`: Reset does not erase request
    history.
- **Logic Interactions:**
  - `project_attributes_rag_knowledge_base_append_text_reset`: Independent reset path for
    text-appended memory.
```

**Level:** `Customer`

**Group:** `3. Knowledge Base`

**Value type:** `bool`

---
