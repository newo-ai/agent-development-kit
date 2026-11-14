# 2. Agent

Back to the [attribute index](index.md).

## `project_representative_agent_name`


**Title:** 2-01. Agent Name [A]

**Description:**

````md
The public name your Agent uses when introducing itself in conversations and message signatures.

**Pro-Tip:** Use a short, natural name your customers can easily hear and remember across voice and
chat.

**Examples:**

```txt
Mia
```

```txt
Alex
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into dynamic Agent persona text, VibeAgent configuration/coaching
replies, greeting fallbacks, report context, and email signatures across conversation/report flows.
VibeAgent uses this name as the first-person outward identity when users configure and mentor the AI
Employee. This value is also synchronized to the chat connector `agent_name` setting, and is used as
input for automatic Agent gender inference when `project_representative_agent_gender` is empty.

**Fallbacks:** On first initialization, the system attempts to copy this value from
`agent_creator_agent_info_name`. If empty, downstream templates and connector-facing introductions
may produce generic or incomplete wording until set.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_title`: Combined with name to compose persona and signature
    context.
  - `project_representative_agent_gender`: If already set, name-based automatic gender inference is
    skipped.
- **Logic Interactions:**
  - `project_representative_agent_chat_greeting_phrase`: Industry setup templates often compose this
    greeting using the Agent name.
  - `project_representative_agent_voice_greeting_phrase`: Industry setup templates often compose
    this greeting using the Agent name.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_voice`:
    Default value may be chosen from inferred Agent gender when this voice setting is empty.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_openai_voice`:
    Default value may be chosen from inferred Agent gender when this voice setting is empty.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_grok_voice`:
    Default value may be chosen from inferred Agent gender when this voice setting is empty.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_title`


**Title:** 2-02. Agent Title [A]

**Description:**

````md
The Agent's role label (for example, AI Host or AI Sales Rep) shown in messages and signatures.

**Pro-Tip:** Choose a role that matches your workflow handoff boundaries so customers understand
what the Agent can do.

**Examples:**

```txt
AI Host
```

```txt
AI Sales Rep
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used in report/email signature blocks and transformed into a runtime job-title
phrase that is injected into Agent persona instructions and voice connector prompt context.

**Fallbacks:** On first initialization, the system attempts to copy this from
`agent_creator_agent_info_title`. If still empty, industry setup flows may inject an
industry-specific default title. If it remains empty after those steps, runtime persona/title
composition falls back to a generic representative role label.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Determines which industry setup flow may inject a default title.
- **Logic Interactions:**
  - `project_representative_agent_name`: Used together in persona/signature composition.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_primary_language`


**Title:** 2-03-A. Agent Primary Language [A]

**Description:**

````md
The Agent's preferred default language for conversation replies. It supplies the starting language
when the conversation has not established another allowed language.

**Pro-Tip:** Keep this set to the main language the Agent should use by default. For true
multilingual behavior, also enable Agent Multilingual.

**Examples:**

```txt
English
```

```txt
Spanish
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** With the advanced Agent Language Instructions V2 configuration enabled, prompts
that request the explicit primary-language line add `Your primary language is ...` regardless of
Agent Multilingual. Other prompt builds can intentionally omit that line. When runtime current
conversation language is not active, the core conversation instructions use this language for short
or ambiguous initial input; a clear, contextually relevant user phrase can establish another allowed
language. The core legacy instruction branch uses the same initial fallback, but earlier
food-ordering and outbound-call prompts follow the user's apparent language immediately and do not
read this Attribute.

Beyond shared conversation instructions, this value supplies the default language for generated chat
and voice greetings, outbound greeting and user-data preparation, voice-style guidance, and
assessment workflows when no explicit assessment language is requested. It also initializes and
backs up runtime current conversation language. Configuration health checks compare it with the
restricted-language list and report a critical conflict when both contain the same language.

**Fallbacks:** Normal initialization preserves an existing non-empty value. When this Attribute is
empty, representative setup fills it from `project_business_language_primary`, which is prepared
from the account-setup language or its configured default. Downstream consumers otherwise use the
stored value directly.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_multilingual`: Controls whether shared language instructions add
    broad multilingual behavior in the V2 branch. The primary language remains the default there,
    while capability-specific legacy prompts can ignore both settings.
  - `project_representative_agent_secondary_languages`: Adds explicitly allowed secondary languages
    in the V2 branch when Agent Multilingual is disabled.
  - `project_business_language_primary`: Normal initialization source when no Agent-specific primary
    language is set.
  - `project_business_language_restricted_list`: Restricted-language rules still apply even when a
    primary Agent language is configured, and the same language must not appear in both settings.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_agent_language_instructions_v2`: This advanced system
    configuration controls which prompt branch reads this Attribute and whether capability-specific
    legacy prompts bypass it.
  - `project_attributes_private_feature_flag_current_conversation_language`: This advanced system
    configuration enables runtime current-language initialization and fallback behavior.
    Current-language prompt wording also requires Agent Language Instructions V2.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `enum`

**Possible values:**
`["English", "Spanish", "French", "German", "Italian", "Portuguese", "Russian", "Chinese", "Japanese", "Korean", "Arabic", "Hindi", "Bengali", "Urdu", "Turkish", "Vietnamese", "Thai", "Indonesian", "Polish", "Dutch", "Hebrew", "Swedish", "Norwegian", "Danish", "Finnish", "Greek", "Czech", "Hungarian", "Slovak", "Ukrainian", "Romanian", "Bulgarian", "Serbian", "Croatian", "Slovenian", "Lithuanian", "Latvian", "Estonian", "Filipino", "Malay", "Khmer", "Lao", "Afrikaans", "Swahili", "Persian", "Punjabi", "Gujarati", "Marathi", "Tamil", "Telugu", "Kannada", "Malayalam", "Sinhalese", "Nepali", "Mongolian", "Amharic", "Azerbaijani", "Georgian", "Uzbek", "Basque", "Catalan", "Kazakh", "Armenian", "Assamese", "Belarusian", "Bosnian", "Burmese", "Cantonese", "Cebuano", "Galician", "Ganda", "Hausa", "Icelandic", "Igbo", "Irish", "Javanese", "Kurdish", "Kyrgyz", "Luo", "Macedonian", "Maltese", "Odia", "Pashto", "Sindhi", "Somali", "Tajik", "Welsh", "Wolof", "Xhosa", "Zulu"]`

---

## `project_representative_agent_secondary_languages`


**Title:** 2-03-B. Agent Secondary Languages [A]

**Description:**

````md
Languages the Agent is explicitly allowed to use in addition to Agent Primary Language. Use this
when the Agent should support a controlled set of languages instead of full multilingual behavior.

**Pro-Tip:** Keep this as an empty JSON list (`[]`) unless you want a strict allowlist. Agent
Secondary Languages take effect when Agent Multilingual is disabled.

**Examples:**

```json
["Spanish", "French"]
```

```json
[]
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Runtime consumers parse this value as a JSON array. With the advanced Agent
Language Instructions V2 configuration enabled, a non-empty list is added to shared
core-conversation, food-ordering, and outbound-call prompts only when Agent Multilingual is `False`.
Those prompts make the primary language the default, allow the listed secondary languages, and
prohibit languages outside that primary-plus-secondary allowlist. Without runtime current-language
state, a clear request or a coherent, contextually relevant phrase in an allowed language can
authorize a prompt-side switch; short, ambiguous, irrelevant, or likely speech-recognition noise
does not. When runtime current-language state is active, only an explicit request or a Language
Observer update changes the prompt language. Some capability prompts also anchor a language after
two consecutive turns. When Agent Multilingual is `True`, shared prompts ignore the secondary list
because broader non-restricted language support takes precedence.

When Agent Language Instructions V2 is not enabled, the shared legacy prompt branches do not read
this Attribute. Language Observer is separate from that prompt flag: when runtime current
conversation language is enabled, it can select a secondary language after the channel-specific
pre-generation gate when the utterance is classified as reliable, and it normally requires
confidence of at least `0.75`. An explicit switch request can bypass that confidence cutoff, but it
cannot bypass the reliability requirement or pre-generation gate. A language that is also restricted
is never eligible. Chat, phone, and webcall observations receive the latest user message and
conversation memory after `broadcast_analyze_conversation`.

**Fallbacks:** Common representative initialization preserves a non-empty value and otherwise sets
this to `[]`. During first initialization, it can copy
`agent_creator_agent_info_secondary_languages`; a missing, empty, or `N/A` setup value uses `[]`. A
non-empty value must be valid JSON because runtime consumers do not replace malformed JSON with the
empty-list fallback.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Default language used together with secondary
    languages in the allowlist.
  - `project_representative_agent_multilingual`: When enabled, broad multilingual behavior takes
    precedence and secondary languages are not injected.
  - `project_business_language_restricted_list`: Used in multilingual and restricted-only modes, but
    not injected into shared prompts when the primary-plus-secondary allowlist is active. Language
    Observer still rejects a listed secondary language if it is also restricted.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_agent_language_instructions_v2`: This advanced system
    configuration must be enabled for shared prompts to use the secondary-language allowlist. Legacy
    prompt branches ignore it.
  - `project_attributes_private_feature_flag_current_conversation_language`: This advanced system
    configuration enables observer use of secondary languages as runtime current conversation
    language candidates.
  - `agent_creator_agent_info_secondary_languages`: Optional first-initialization source.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `json`

---

## `project_representative_agent_multilingual`


**Title:** 2-03-C. Agent Multilingual [A]

**Description:**

```md
Determines whether the Agent receives broad permission to converse in any language that is not
restricted. Common setup enables this behavior by default so the Agent can serve multilingual users
without a configured secondary-language allowlist.

**Best Practice:** Leave this enabled for broad multilingual support. Disable it when the Agent must
use only its primary and configured secondary languages, and make sure the required secondary
languages are configured. Language availability does not make a single short or ambiguous phrase a
valid switch.

**Examples:**

- **Enabled (`True`):** The Agent can use any non-restricted language while keeping the active
  conversation language until a valid switch signal occurs. Agent Secondary Languages are ignored in
  this mode.
- **Disabled (`False`) with secondary languages configured:** The Agent is limited to its primary
  and secondary languages.
- **Disabled (`False`) without secondary languages configured:** Shared instructions do not add
  broad multilingual permission. The primary-language and applicable restricted-language guidance
  remain in effect.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When the advanced language-instructions V2 configuration is enabled, shared
language prompts for core conversations, reasoning, voice-to-voice and outbound calls, and food
ordering read this setting. Only the exact value `True` enables broad multilingual instructions.
Those instructions allow every non-restricted language without treating language availability as
evidence of a switch. The Agent keeps its active conversation language after isolated or ambiguous
input and switches only after an explicit request or stable evidence under the active language
policy.

When set to `False`, shared prompts do not add broad multilingual permission. If
`project_representative_agent_secondary_languages` contains values, the primary-plus-secondary
allowlist takes precedence. Otherwise, the primary-language line remains available to prompts that
request it, and configured restricted-language guidance still applies. When set to `True`, secondary
languages are intentionally ignored because broader multilingual behavior takes precedence.

When the advanced system configuration
`project_attributes_private_feature_flag_current_conversation_language` is enabled, Language
Observer also reads this setting. It may switch the runtime current conversation language to a
language outside the primary and secondary lists only with very high confidence or an explicit user
request, and it never switches to a restricted language. Chat, phone, and webcall channels are
observed after `broadcast_analyze_conversation`, where conversation memory is available. In chat,
short messages are gated. After a language is confirmed, observer generation runs only when the
latest message has at least 12 words and at least four turns have elapsed since the previous
observer run; an explicit request does not bypass this pre-generation gate.

**Fallbacks:** Common account setup initializes an empty value to `True` and preserves any existing
explicit value. Runtime consumers enable this setting only for the exact value `True`; an empty or
other value follows the disabled branch. When the advanced system configuration
`project_attributes_private_feature_flag_agent_language_instructions_v2` is disabled, legacy shared
prompts use broad multilingual instructions independently of this setting, so this Attribute does
not narrow those legacy prompts.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Supplies the default language and the optional
    primary-language prompt line.
  - `project_representative_agent_secondary_languages`: Becomes the allowed-language list alongside
    the primary language when multilingual mode is disabled and secondary languages are configured.
  - `project_business_language_restricted_list`: Excludes configured languages in multilingual and
    restricted-only prompt modes. The primary-plus-secondary allowlist takes precedence in shared
    prompts, while Language Observer still rejects restricted candidates when it is enabled.
- **Logic Interactions:**
  - `project_attributes_private_feature_flag_agent_language_instructions_v2`: This advanced system
    configuration enables the shared instruction branch in which this Attribute controls broad
    multilingual behavior. Its legacy branch assumes broad multilingual capability independently.
  - `project_attributes_private_feature_flag_current_conversation_language`: This advanced system
    configuration enables Language Observer to use this Attribute when deciding whether a language
    outside the primary and secondary lists is eligible for a runtime switch.
```

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `bool`

**Possible values:** `["True", "False"]`

---

## `project_representative_agent_voice_speaking_style`


**Title:** 2-04-A. Agent Tone of Voice / Speaking Style for Voice Channels [A]

**Description:**

````md
Defines voice-channel speaking behavior (pace, tone, and optional accent guidance).

**Pro-Tip:** Keep this style voice-specific and actionable (pace, warmth, clarity). Avoid embedding
language settings here.

By default, we recommend using the following style:

```txt
Friendly professional, super welcoming. Speak energetic and fast.
From the second turn onward, naturally include "uhh", "umm", or "hmm" in roughly every third response.
```

If you'd like to add a specific accent - for example, Australian - you can specify it like this:

```txt
Friendly professional, super welcoming. Speak energetic and fast.
From the second turn onward, naturally include "uhh", "umm", or "hmm" in roughly every third response.

You speak with Australian accent.
```

Why specify style in different attributes for chat and voice? Because in some cases you might want
your agent to speak in voice calls by providing specific intonation, speed, or accent. It's not
necessary to specify these details for chat interactions.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Applied in voice prompt headers and synchronized into voice integration connector
initial system instructions for v2v runtime behavior.

**Fallbacks:** If empty, initialization derives a default voice style using business
location/language context. Existing non-empty values are preserved.

**Dependencies:**

- **Primary Settings:**
  - `project_business_country`: Used by style-generation logic when deriving defaults.
  - `project_business_address`: Used by style-generation logic when deriving defaults.
  - `project_business_language_primary`: Used by style-generation logic when deriving defaults.
- **Logic Interactions:**
  - `project_attributes_setting_voice_integration_service_voice_mode`: Voice style is consumed by
    voice runtime prompts when voice mode is enabled.

**Deprecated Guidance:** Do not encode language requirements in this style field; use business
language attributes instead.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_chat_speaking_style`


**Title:** 2-04-B. Agent Tone of Voice for Chat Channels [A]

**Description:**

````md
Defines the Agent's chat tone and communication personality.

**Pro-Tip:** Focus on behavior and tone (for example, concise vs. warm), not language selection.
Language should be controlled by business language attributes.

By default, we recommend using the following style:

```txt
Friendly professional, super welcoming.
```

If you'd like to add a specific behavior for chat channel, you can also mention it here:

```txt
Friendly professional, super welcoming. After each user's answer to your questions, use
affirmations like "Got it!", "Understood!", and "Thanks for the info!".
```

> Note: For `voice-to-voice` and `speech-to-speech` sessions, please use the
> `Agent Tone of Voice / Speaking Style for Voice Channels [A]`
> (`project_representative_agent_voice_speaking_style`) attribute. This chat style setting is used
> for text channels and other messaging/greeting prompts outside those voice modes.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Applied in the main style instruction whenever the session is not in
`voice-to-voice` or `speech-to-speech` mode. It is also reused by outbound greeting-generation
prompts (including call and SMS greetings).

**Fallbacks:** If empty, initialization applies a generic default chat-style instruction.

**Dependencies:**

- **Primary Settings:**
  - `project_business_language_primary`: Primary language routing is handled separately from style.
- **Logic Interactions:**
  - `project_representative_agent_chat_formatting_style`: Style and formatting constraints are
    applied together for chat.

**Deprecated Guidance:** Do not encode language requirements in this style field; use business
language attributes instead.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_chat_formatting_style`


**Title:** 2-04-C. Agent Chat Formatting Style [A]

**Description:**

````md
Controls formatting rules for chat responses (lists, markdown, emojis, and structure).

**Pro-Tip:** Keep these rules short and explicit. Prefer clear "do/don't" instructions to avoid
conflicting output behavior.

**Examples:**

```txt
- Do not use any lists (numbered or bulleted) when communicating information.
- Do not use markdown formatting.
- Do not use hashtags.
- Do not use emojis.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Inserted directly into the `<OutputFormat>` prompt section for chat channels and
therefore applied on every chat response.

**Fallbacks:** If empty, initialization sets a default anti-list/anti-markdown style template to
keep chat output consistent.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_chat_speaking_style`: Tone and formatting are applied together in
    chat prompt construction.
- **Logic Interactions:**
  - `project_representative_agent_gender`: Gender instructions are appended in output-format prompt
    generation for gendered languages.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_voice`


**Title:** 2-05-A. Voice - Integration Service - Voice To Voice Provider - GenAI - Voice [A]

**Description:**

```md
Selects which GenAI v2v voice profile your Agent uses in supported voice integrations.

**Pro-Tip:** Pick the final voice after validating pronunciation quality for your business names and
domain-specific terms in real call examples. Preview the available voice demos here:
[Google Chirp 3: HD voices](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd#voice_options).

**Examples:**

- **Female Despina - Smooth:** Common default for neutral/female profile setups.
- **Male Iapetus - Clear:** Common default for male profile setups.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Mapped to provider-specific short voice IDs and synchronized to connector setting
`genai_v2v_voice` in voice integration connector update flow.

**Fallbacks:** If empty, initialization applies a gender-based default voice selection.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_gender`: Used to pick default GenAI voice when empty.
- **Logic Interactions:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider`: Determines which
    v2v provider path is active.
  - `project_attributes_setting_voice_integration_service_voice_mode`: Voice mode governs whether
    connector voice settings are runtime-relevant.
```

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `enum`

**Possible values:**
`["Female Achernar - Soft", "Female Aoede - Breezy", "Female Autonoe - Bright", "Female Callirrhoe - Easy-going", "Female Despina - Smooth", "Female Erinome - Clear", "Female Gacrux - Mature", "Female Kore - Firm", "Female Laomedeia - Upbeat", "Female Leda - Youthful", "Female Pulcherrima - Forward", "Female Sulafat - Warm", "Female Vindemiatrix - Gentle", "Female Zephyr - Bright", "Male Achird - Friendly", "Male Algenib - Gravelly", "Male Algieba - Smooth", "Male Alnilam - Firm", "Male Charon - Informative", "Male Enceladus - Breathy", "Male Fenrir - Excitable", "Male Iapetus - Clear", "Male Orus - Firm", "Male Puck - Upbeat", "Male Rasalgethi - Informative", "Male Sadachbia - Lively", "Male Sadaltager - Knowledgeable", "Male Schedar - Even", "Male Umbriel - Easy-going", "Male Zubenelgenubi - Casual"]`

---

## `project_attributes_setting_voice_integration_service_voice_to_voice_provider_openai_voice`


**Title:** 2-05-B. Voice - Integration Service - Voice To Voice Provider - OpenAI - Voice [A]

**Description:**

```md
Selects which OpenAI v2v voice profile your Agent uses in supported voice integrations.

**Pro-Tip:** Validate this choice with your greeting/disclaimer phrases and frequent call intents to
avoid mismatched tone. Preview the available voices here: [OpenAI.fm](https://www.openai.fm/).

**Examples:**

- **Neutral - Alloy:** Common default for `auto` gender profile.
- **Female - Sage / Male - Cedar:** Common defaults for explicit gender profiles.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Mapped to provider-specific lowercase IDs (for example `sage`, `cedar`) and
synchronized to connector setting `openai_v2v_voice`.

**Fallbacks:** If empty, initialization applies a gender-based default OpenAI voice selection.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_gender`: Used to pick default OpenAI voice when empty.
- **Logic Interactions:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider`: Determines
    whether OpenAI voice setting is active at runtime.
  - `project_attributes_setting_voice_integration_service_voice_mode`: Voice mode governs whether
    connector voice settings are runtime-relevant.
```

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `enum`

**Possible values:**
`["Neutral - Alloy", "Male - Ash", "Male - Ballad", "Male - Cedar", "Female - Coral", "Male - Echo", "Female - Marin", "Female - Sage", "Female - Shimmer", "Male - Verse"]`

---

## `project_attributes_setting_voice_integration_service_voice_to_voice_provider_grok_voice`


**Title:** 2-05-C. Voice - Integration Service - Voice To Voice Provider - Grok - Voice [A]

**Description:**

```md
Selects which Grok v2v voice profile your Agent uses in supported voice integrations.

**Pro-Tip:** Test the final choice with your greeting, disclaimer, and business-name pronunciation
before switching your live provider to Grok.

**Examples:**

- **Female Ara - Warm:** Common default for female profile setups.
- **Neutral Sal - Smooth:** Common default for neutral profile setups.
- **Male Rex - Confident:** Common default for male profile setups.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Mapped to provider-specific lowercase IDs (for example `eve`, `rex`) and
synchronized to connector setting `grok_v2v_voice`.

**Fallbacks:** If empty, initialization applies a gender-based default Grok voice selection.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_gender`: Used to pick default Grok voice when empty.
- **Logic Interactions:**
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider`: Determines
    whether Grok voice setting is active at runtime.
  - `project_attributes_setting_voice_integration_service_voice_mode`: Voice mode governs whether
    connector voice settings are runtime-relevant.
```

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `enum`

**Possible values:**
`["Female Eve - Upbeat", "Female Ara - Warm", "Male Rex - Confident", "Neutral Sal - Smooth", "Male Leo - Authoritative"]`

---

## `project_representative_agent_voice_phone_number`


**Title:** 2-06. Agent Phone Number (AI Phone) (DON'T CHANGE) [A]

**Description:**

```md
System-managed AI phone number assigned to this Agent for voice channels.

**Pro-Tip:** Treat this as read-only in normal setup. If it appears missing, resolve connector/phone
provisioning instead of manually editing this field.

**Examples:**

- `14155550123`
- `null` (when provisioning data is unavailable)

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Resolved from the active voice integration phone source during
representative-agent default preparation, then consumed by user-information extraction and
phone-channel fallback procedures (for example, email gathering). First-time phone purchase writes
the provisioned number here before linking it to voice and SMS connectors. When an existing voice
connector already owns an AI phone number, setup synchronizes that connector number back to this
attribute instead of buying another number. Agent Creator setup can restrict first-time phone
purchase to specific provider IDs and a provider-side phone group before the number is bought.
During Agent Creator reinitialization, the existing number is preserved as long as the requested
country code is unchanged; if the reinitialization request specifies a different country code, the
previously provisioned number is dropped and a new number is bought in the new country. It may be
refreshed later during phone-attachment synchronization.

**Fallbacks:** If phone-source lookup returns empty or unavailable, the system stores `null` as a
placeholder until a valid number is synchronized. During Agent Creator-driven provisioning, number
purchase is skipped when the account is already marked initialized or when required phone-purchase
inputs/connectors are unavailable. If the Agent Creator provider list is empty or not a JSON array,
or the group filter is empty, purchase continues without those restrictions.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service`: Determines which connector source is
    used to resolve the number.
- **Logic Interactions:**
  - `project_representative_agent_voice_phone_alpha2_code`: Used with this number in phone parsing
    logic.
  - `project_representative_agent_voice_phone_country_code`: Used with this number in phone parsing
    logic.
  - `project_attributes_setting_voice_integration_service_bypass_phone_number`: Compared during
    bypass/autofill logic to avoid direct self-routing to the Agent's AI line. If a different public
    number forwards to this AI line outside SuperAgent, that forwarding can still create the same
    loop.
  - `agent_creator_supported_phone_providers`: Optional Agent Creator first-init source. When it
    contains a JSON array of provider IDs, phone purchase is limited to those providers.
  - `agent_creator_supported_phone_group`: Optional Agent Creator first-init source. When provided,
    phone purchase is limited to that provider-side phone group.
```

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `number`

**Is read-only:** `true`

---

## `project_representative_agent_voice_disclaimer_phrase`


**Title:** 2-07-A. Voice - Disclaimer Phrase [A]

**Description:**

````md
Short phrase spoken before the main voice greeting (for example, compliance or recording notice).

**Pro-Tip:** Keep this concise and policy-aligned. Long disclaimers increase call friction and can
degrade greeting flow.

**Examples:**

```txt
If it's an emergency, please call 9-1-1.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Prepended to the inbound voice greeting during runtime greeting assembly and
passed as context during greeting-generation flows.

**Fallbacks:** On first initialization, the system first uses the Agent Creator voice disclaimer
when provided. If that source is empty, initialization applies a default recording/compliance
disclaimer localized with Agent Primary Language.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Used to localize the default disclaimer when
    this disclaimer is empty and no Agent Creator voice disclaimer was provided.
- **Logic Interactions:**
  - The advanced system configuration `agent_creator_voice_channel_disclaimer_phrase` is read as the
    preferred first-init source when provided by Agent Creator.
  - `project_representative_agent_voice_greeting_phrase`: Concatenated with disclaimer for dynamic
    greeting preparation.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_voice_greeting_phrase`


**Title:** 2-07-B. Voice - Greeting Phrase - Inbound [A] [IMPORTANT]

**Description:**

````md
Primary voice greeting for inbound calls.

**Pro-Tip:** Include business name and Agent name in one concise sentence so callers immediately
understand they reached the right place.

**Examples:**

```txt
Thank you for calling Example Hotel! I'm Mia, how may I assist you today?
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used as the base source for dynamic voice greeting construction and as a fallback
in returning-caller greeting generation when specialized returning greetings are empty.

**Fallbacks:** On first initialization, the system first uses the Agent Creator voice greeting when
provided. If that source is empty, common initialization creates an empty placeholder, then industry
representative-agent setup usually auto-fills a localized default if still empty.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Industry setup uses this for localized default
    greeting generation.
- **Logic Interactions:**
  - The advanced system configuration `agent_creator_voice_channel_greeting_phrase` is read as the
    preferred first-init source when provided by Agent Creator.
  - `project_representative_agent_voice_disclaimer_phrase`: Prepended during dynamic voice greeting
    composition.
  - `project_business_name_phonetic`: When set, phonetic replacement may be applied in prepared
    greeting phrase.
  - `project_representative_agent_voice_greeting_phrase_recent_returning`: Used before this default
    when available.
  - `project_representative_agent_voice_greeting_phrase_later_returning`: Used before this default
    when available.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_voice_greeting_phrase_recent_returning`


**Title:** 2-07-C. Voice - Greeting Phrase - Recent Returning Customer [A]

**Description:**

```md
Optional specialized greeting for very recent returning callers (same-session callbacks).

**Pro-Tip:** Keep this shorter than your first-time greeting and acknowledge continuity.

**Examples:**

- **Set:** Use your custom recent-return greeting.
- **Empty:** System generates or falls back to generic "welcome back" style behavior.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used as the first-choice recent-return greeting example during returning-caller
greeting generation.

**Fallbacks:** If empty, greeting generation falls back to built-in "welcome back" style templates
based on available user/business context.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Used as fallback target language when
    generating the final recent-return greeting.
  - `project_business_name_phonetic`: Used in fallback template phrasing when available.
  - `project_business_name`: Fallback business-name source when phonetic value is not set.
- **Logic Interactions:**
  - `project_representative_agent_voice_disclaimer_phrase`: Disclaimer context is applied during
    generated greeting preparation.
```

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_voice_greeting_phrase_recent_returning_after_transfer`


**Title:** 2-07-D. Voice - Greeting Phrase - Recent Returning Customer After Call Transfer [A]

**Description:**

````md
Optional source phrase for a caller who returns after the Agent forwarded the call but before the
current session is finalized.

**Pro-Tip:** Keep this very short and reference the transfer context—avoid full re-introductions and
redundant information.

**Examples:**

```txt
Welcome back. It looks like the transfer did not connect. How can I continue helping?
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When a phone call ends with the `assistant-forwarded-call` reason, this value
becomes the source for the recent-return greeting. Greeting generation combines it with the voice
disclaimer, translates it into the preferred conversation language or Agent Primary Language,
applies configured phonetic business-name replacement, and stores the result for a return before the
session ends. Configuration health checks audit this value as spoken text.

**Fallbacks:** If this value is empty, the system uses a built-in transfer-aware source phrase and
personalizes it with the caller's name when available.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Supplies the target language when the recent
    conversation does not establish one.
  - `project_representative_agent_voice_disclaimer_phrase`: Combined with the selected source phrase
    during greeting generation.
- **Logic Interactions:**
  - The advanced system configuration
    `project_attributes_setting_session_ended_reset_persona_attributes`: When enabled, generation is
    skipped at call end and stored returning greetings are cleared at session end.
  - `project_business_name` and `project_business_name_phonetic`: After generation, exact business
    name occurrences can be replaced with the configured phonetic form.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_voice_greeting_phrase_later_returning`


**Title:** 2-07-E. Voice - Greeting Phrase - Returning Customer [A]

**Description:**

```md
Optional specialized greeting for returning callers after a time gap (not immediate callback).

**Pro-Tip:** Mention business and Agent context briefly so long-gap callers can re-orient quickly.

**Examples:**

- **Set:** Use your custom later-return greeting.
- **Empty:** System falls back to inbound greeting or generated "welcome back" phrasing.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used as the preferred later-return greeting source for new sessions with returning
callers.

**Fallbacks:** If empty, runtime uses inbound greeting patterns or generated fallback text that may
include business and Agent name.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_voice_greeting_phrase`: Fallback source when later-return greeting
    is empty.
- **Logic Interactions:**
  - `project_representative_agent_name`: Used in generated later-return fallback phrasing.
  - `project_business_name`: Used in generated later-return fallback phrasing.
  - `project_representative_agent_voice_disclaimer_phrase`: Disclaimer context is applied during
    generated greeting preparation.
```

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_voice_greeting_phrase_later_returning_after_transfer`


**Title:** 2-07-F. Voice - Greeting Phrase - Later Returning Customer After Call Transfer [A]

**Description:**

````md
Optional greeting used when a caller returns to the Agent after a time gap following a transfer (for
example, callers who call back later rather than an immediate callback).

**Pro-Tip:** Briefly re-orient the caller and mention context or business name; offer a quick recap
option rather than replaying the entire prior interaction.

**Examples:**

```txt
Welcome back. I can continue helping after your earlier transfer.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** When a phone call ends with the `assistant-forwarded-call` reason, this value
becomes the source for the later-return greeting. Greeting generation combines it with the voice
disclaimer, translates it into the preferred conversation language or Agent Primary Language,
applies configured phonetic business-name replacement, and stores the result for use after the
current session ends. Configuration health checks audit this value as spoken text.

**Fallbacks:** If this value is empty, the system uses
`project_representative_agent_voice_greeting_phrase_later_returning`. If that is also empty, a
caller whose display name is the default `User` value uses
`project_representative_agent_voice_greeting_phrase`; every other display-name value uses a built-in
template composed from the business and Agent names.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_voice_greeting_phrase_later_returning`: First fallback source when
    this transfer-specific phrase is empty.
  - `project_representative_agent_voice_greeting_phrase`: Fallback source when the caller's name is
    unavailable and the standard later-return phrase is empty.
  - `project_representative_agent_primary_language`: Supplies the target language when the recent
    conversation does not establish one.
  - `project_representative_agent_voice_disclaimer_phrase`: Combined with the selected source phrase
    during greeting generation.
- **Logic Interactions:**
  - `project_representative_agent_name`: Used in the built-in fallback when the caller's name is
    known.
  - `project_business_name` and `project_business_name_phonetic`: Used by the named-caller fallback;
    exact business-name occurrences can also be replaced with the configured phonetic form after
    generation.
  - The advanced system configuration
    `project_attributes_setting_session_ended_reset_persona_attributes`: When enabled, generation is
    skipped at call end and stored returning greetings are cleared at session end.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_chat_greeting_phrase`


**Title:** 2-08. Chat - Greeting Phrase [A]

**Description:**

````md
Primary first message for chat channels where the Agent is expected to greet first.

**Pro-Tip:** Use one clear welcome + intent prompt. Avoid overlong intros that delay user action.

**Examples:**

```txt
I'm Becky. Would you like to reserve a table, or can I assist you with something else?
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used as the chat-channel proactive greeting source in integrations where greeting
is enabled, and synchronized to native chat-connector greeting settings during setup/update flows.

**Fallbacks:** On first initialization, the system first uses the Agent Creator chat greeting when
provided. If that source is empty, common initialization sets an empty placeholder; industry
representative-agent setup usually populates a localized default if still empty.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_primary_language`: Used during localized default greeting
    generation.
- **Logic Interactions:**
  - The advanced system configuration `agent_creator_chat_channel_greeting_phrase` is read as the
    preferred first-init source when provided by Agent Creator.
  - `project_representative_agent_name`: Often injected into default greeting templates.
  - `project_business_name`: Often injected into default greeting templates.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_gender`


**Title:** 2-09. Agent Gender [A]

**Description:**

```md
Controls grammatical self-reference style in gendered languages and influences default voice profile
selection.

**Pro-Tip:** Use `auto` unless you need explicit feminine/masculine first-person morphology in
supported languages.

**Examples:**

- **`auto`:** Prefer neutral constructions where possible.
- **`female`:** Apply feminine first-person forms in gendered-language responses.
- **`male`:** Apply masculine first-person forms in gendered-language responses.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Consumed by output-format prompt builders to inject grammatical-gender
instructions and used during initialization to pick default GenAI/OpenAI voice options.

**Fallbacks:** On first initialization, the system first uses the Agent Creator gender value when
provided. If that source is empty, initialization infers a value from
`project_representative_agent_name`.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_name`: Input signal for automatic gender inference.
- **Logic Interactions:**
  - The advanced system configuration `agent_creator_agent_info_gender` is read as the preferred
    first-init source when provided by Agent Creator.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_voice`:
    receives gender-based defaults when empty.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider_openai_voice`:
    receives gender-based defaults when empty.
```

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `enum`

**Possible values:** `["auto", "female", "male"]`

---

## `project_attributes_setting_voice_integration_service_bypass_phone_number`


**Title:** 2-10. Bypass Phone Number [A]

**Description:**

```md
Phone number used as emergency/bypass forwarding destination for voice integrations.

**Pro-Tip:** Use a monitored human-handled number that does not automatically redirect to the Agent.
Do not set this to the Agent's own AI number, and do not reuse your public business number if that
public number forwards inbound calls to the Agent.

**Examples:**

- **Set to working-hours escalation number handled by staff:** normal human fallback routing.
- **Set to separate manager/mobile line:** safe direct bypass destination.
- **Set to public office number that auto-forwards to the Agent:** creates a call loop and should be
  avoided.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Synchronized to connector `emergency_phone_number` setting in voice integration
connector update flow.

**Fallbacks:** If empty, post-setup logic attempts to auto-fill from escalation/public phones using
ASR redirection rules. In `non-overflow`, it prefers the working-hours escalation phone. In
`overflow`, it may use the public phone when that value is not identical to the Agent's AI number.

**Routing Safety:** A loop happens when this bypass number points to the same public business line
the caller used originally, and that public line is configured outside SuperAgent to forward calls
to `project_representative_agent_voice_phone_number`. The connector bypasses the call to that public
line, then the telephony provider forwards it back to the Agent instead of a human.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_asr_redirection_type_working_hours`: Governs bypass auto-fill
    strategy (`non-overflow` vs `overflow`).
  - `project_business_working_hour_escalation_phone`: Preferred bypass fallback in safe routing
    paths.
  - `project_business_public_phone`: Alternate bypass fallback when safe.
- **Logic Interactions:**
  - `project_representative_agent_voice_phone_number`: Compared to candidate bypass numbers to avoid
    direct self-routing. This check does not detect every carrier- or PBX-level forward from a
    separate public number back to the Agent.
```

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_voicemail_detection_behavior_instruction`


**Title:** 2-11. Voice - Voicemail Detection Behavior Instruction [A]

**Description:**

````md
Instruction for outbound-call behavior when voicemail or answering systems are detected.

**Pro-Tip:** Keep the instruction short and explicitly include a goodbye phrase so the call can end
cleanly after message delivery.

**Examples:**

```txt
Leave a brief message including the business name and phone number and say goodbye.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Included in outbound phone prompts before the call begins so the Agent knows what
to say when it encounters voicemail or an answering system. The voicemail detector classifies the
conversation separately and does not inject this instruction after detection.

**Fallbacks:** If empty, initialization sets a default voicemail behavior instruction that includes
a clear goodbye requirement.

**Dependencies:**

- **Primary Settings:**
  - None.
- **Logic Interactions:**
  - `project_attributes_setting_check_spam_or_voicemail`: This advanced system configuration
    independently classifies outbound voicemail and can stop the call after detection; it does not
    control whether this instruction is included in the outbound prompt.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---

## `project_representative_agent_providing_prices_explicit_constraint`


**Title:** 2-12. Explicit Constraint - Providing Prices [A]

**Description:**

````md
Explicit instruction block that controls how the Agent communicates pricing.

**Pro-Tip:** Use short, mandatory wording for disclaimers and approval boundaries (for example, when
only a manager can confirm final prices).

**Examples:**

```txt
- Always mention that actual prices might differ whenever you provide prices.
```

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Injected into pricing-related explicit constraints for both main conversation
responses and internal reasoning/evaluation flows.

**Fallbacks:** Default common initialization sets an empty value. Some industry setup flows set
first-init defaults with pricing-disclaimer language when the field is empty.

**Dependencies:**

- **Primary Settings:**
  - `project_business_industry`: Some industries inject opinionated default constraints during
    setup.
- **Logic Interactions:**
  - `project_attributes_setting_additional_limitations_and_restrictions`: Works alongside broader
    business constraints in prompt assembly.
````

**Level:** `Customer`

**Group:** `2. Agent`

**Value type:** `string`

---
