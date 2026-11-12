# Health check, and level A vs level B

How to review an agent's configuration, find what is wrong or contradictory, and turn an owner's
wish into the right kind of change. Newo's built-in configuration assistant (Vibe mode in the Newo
portal: "check my agent") runs the same kind of check; this page lets any coding assistant do it.
Rules marked (inferred) are not documented by Newo yet; confirm them before relying on them.
Scenario editing itself: [05-scenarios.md](05-scenarios.md).

## 0. Two levels of customization

| Level | What changes | Examples | Where |
|---|---|---|---|
| **A: values** | the value of a setting (attribute) | hours, prices, products, FAQ, greeting, transfer numbers, tone of voice, report recipients | attributes in groups 1–5 |
| **B: behavior (canvas)** | how the agent recognizes intents and runs the conversation | a new intent type ("wants a second opinion"), a new scenario ("reschedule"), a step-by-step procedure ("collect insurance details") | Workflow Builder canvas: introduction, intent types, scenarios, procedures |

How to decide:

1. **Search the attributes first.** Most requests are values. Even when the request is about behavior,
   the *destination and execution* of an action live in attributes: where to transfer, which SMS to
   send, where to book.
2. **Go to level B only for conversation logic:** recognizing a new kind of caller request, a new
   dialog path, a different order of steps.
3. **Mixed requests:** set the attributes first (destination, content), then change the canvas
   only if the trigger also has to change.
4. **The existing configuration is the source of truth.** Update the existing setting or card.
   Never build a parallel structure, and never put behavior into a text field that is meant for
   facts.
5. **Edit level B through the Workflow Builder (or Vibe mode), never through the API.** The
   canvas attribute and its compiled forms (`…_ami_*`, `…_itm_*`) are rebuilt on publish and on
   Newo updates. Cards you edited yourself are kept, while cards from the library are re-synced.
6. **Changing NAF code is not level C.** It is outside customization and allowed only in
   exceptional cases ([04-naf-change-policy.md](04-naf-change-policy.md)).

Note on naming: attribute titles carry difficulty tags `[A]` `[B]` `[C]`. These mean basic,
advanced and system *settings*, not the levels above. Do not confuse the two.

## 1. One field, one kind of content

The agent's prompt is built from sections:
- a header with the persona and speaking style;
- output format;
- `<BusinessContext>`: story, products, terms, FAQ;
- `<ExplicitConstraints>`;
- the working schedule;
- the intent map;
- scenarios and procedures.

Each attribute lands in **one** of these sections. Content in the wrong field lands in the wrong
section, and the model weighs it wrongly. Example: products inside the speaking style become
"how to talk", not "what we sell".

| Field | Put here | Do not put here |
|---|---|---|
| `project_business_story` | 1–2 paragraphs: what the business is, what makes it different | catalogs, prices, policies, tone instructions |
| `project_attributes_products_and_services` | catalog entries: name, `Description:`, optional `Price:`, `Payment link:` | marketing text; huge catalogs (→ [knowledge](06-knowledge.md)) |
| `…_products_and_services_not_offering` | hard exclusions | soft caveats |
| `project_attributes_faq` | conversational Q&A, `1. Question?` / `> Answer` | strict rules (→ terms) |
| `project_attributes_terms_and_conditions` | short rules: cancellation, late arrival, accessibility | Q&A, marketing; the literal value `null` |
| `project_attributes_current_specials` | dated promotions | permanent prices |
| `project_representative_agent_voice_speaking_style` / `…_chat_speaking_style` | pace, tone, manner only | business facts, products, languages, rules |
| `project_representative_agent_chat_formatting_style` | short do/don't rules about lists, markdown, emojis | tone or persona text |
| `…_voice_greeting_phrase` / `…_chat_greeting_phrase` | one sentence: business name, agent name, a question | intros, disclaimers (own field) |
| `…_providing_prices_explicit_constraint` | short pricing disclaimers | the prices themselves |
| `…_additional_limitations_and_restrictions` | requests the agent must relay or refuse | style text |
| `…_additional_global_conversation_instruction` | a temporary emergency override, 2–3 sentences | long instruction sets (the agent becomes unstable) |
| `…_transfer_call_criteria` | one transfer case per line | phone numbers |
| escalation phones, `…_transfer_call_phone_numbers` | staffed human lines, `+12223334444` | the public number if it forwards to the agent (loop); the AI phone number |
| knowledge base (`…_rag_knowledge_base_append_text`) or Knowledge Studio | long manuals, price lists, policies | — |

## 2. The health check

Newo's Vibe mode already runs one ("check my agent"). It applies fixed rules, then
two model passes, and labels each finding by how to fix it:
- `settable` — level A;
- `canvas` — level B;
- `hand_off` — Newo support.

It changes nothing until the owner confirms. A coding assistant should follow the same order.

### Step 1. Read everything once
Save to a local file:
- all attributes, with secrets masked;
- the canvas items (introduction, intent types, scenarios, procedures) with library or custom
  flags;
- the industry, the designer version (V1/V2) and auto-update.

### Step 2. Critical: the agent breaks or loops

| Check | Rule |
|---|---|
| Call loop | an escalation or bypass number equals the public number that forwards to the agent, or the AI phone number |
| Transfer to nowhere | `…_transfer_call_enabled` = True, but the escalation phone for the current time and the exception numbers are all empty |
| Broken routing | an intent type routes to a scenario that does not exist in the canvas |
| Leftover template tokens | `{{…}}` or `<||…||>` in spoken text |
| Voice without greeting | voice is on and the greeting is empty |
| Booking without a target | booking or availability check enabled, but the URL or schema is empty |
| Language conflict | the primary language is in the restricted list |
| Test mode in production | `…_setting_test_mode` = True: bookings, SMS and email are mocked |

### Step 3. Wrong setup for the business

| Check | Rule |
|---|---|
| Industry | `project_business_industry` matches the business. `sales_industry` only for lead qualification and sales. A clinic on sales gets sales intents, sales reports and the "AI Sales Rep" persona. Industry is read-only: changing it means re-initialization with Newo support |
| Hours and time zone | `project_business_working_hours` in the documented day-by-day format (not `N/A`); `project_business_time_zone` is an IANA zone. Without hours, the agent cannot tell working hours from after-hours |
| Languages | the agent's primary language matches the callers. If callers use several languages: multilingual on, or secondary languages listed. No language words in speaking style |
| Calendar | `google_integration` ⇒ manager email set; `calcom_integration` ⇒ booking enabled |
| Industry essentials | the industry's own key fields are filled (dental: appointment URL, scheduling questions; sales: qualifying criteria, appointment URL; general: modality and URL). Empty ones fall back to neutral placeholders (inferred: the scenarios then run without real content) |
| Health data | medical or dental business ⇒ HIPAA mode considered (US); GDPR rules on reports (EU) |

### Step 4. Content quality (level A)

| Check | Look for |
|---|---|
| Misplaced content | facts in speaking style; rules in FAQ; prices in the price constraint; catalog in the story |
| Placeholders | `N/A`, `null`, `TBD`, `*(No … specified.)*`, generic lines such as "Services in dentistry" with no real services |
| Duplicates and contradictions | the same fact in two fields with different values (hours in FAQ vs working hours; prices in FAQ vs products); agent, business and greeting names that disagree |
| Thin essentials | products without real services or prices; address that is only a city; FAQ that repeats the story |
| Overlong fields | global instruction above about 3 sentences; huge text in style fields; catalogs above a screen → knowledge base or Knowledge Studio |
| Reports | report type names in content and criteria match; recipients defined |

### Step 5. Behavior (level B)
- Intent types and scenarios fit the business (no "Sale to a Client" for a clinic).
- Every intent routes to an existing scenario.
- Custom cards are few and named consistently.
- Library cards are not hand-edited without reason (edits detach them from Newo updates).

### Step 6. Report to the owner
Report in plain words, ordered by **Critical → Important → Nice to have**. For each finding:
- what is wrong;
- why it matters for callers;
- the proposed fix, with its level (A, B, or Newo support);
- old value and new value.

Apply nothing without the owner's "yes". After the fixes:
1. re-read the changed fields;
2. publish if the field is compiled (hours, products, locations, reports, booking schemas);
3. test with a new conversation;
4. run the health check again.

## 3. Turning an owner's wish into a change

1. Restate the wish as an outcome ("callers asking about implants get a consultation booked").
2. Search attributes for where that outcome is configured (level A). If it is there, change the
   value.
3. If the outcome needs the agent to recognize something new, or to follow new steps, plan a
   level-B change in the Workflow Builder. Set the attributes it needs first.
4. If neither is enough, tell the owner, and file a NAF change notice before touching framework
   code.
5. Test, report, and record the change.
