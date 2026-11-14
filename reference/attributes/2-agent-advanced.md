# 2. Agent - Advanced

Back to the [attribute index](index.md).

## `project_representative_agent_voice_phone_area_code`


**Title:** Voice - AI Phone - Area Code Primary [C]

**Description:**

```md
Primary area code preference for provisioning the Agent phone number.

**Pro-Tip:** Use a local area code your customers recognize, and always provide a fallback area
code.

**Examples:**

- **`408`:** Try to provision in this area first.
- **`650`:** Another valid primary choice based on local coverage goals.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used during first-time phone provisioning to request a number in the preferred
area. If unavailable, provisioning can continue with the fallback area code. It is also reused in
some industry setup flows when composing default served-area phrasing.

**Fallbacks:** Initialization reads this from `agent_creator_voice_channel_phone.area_code` when
available. During phone purchase, Agent Creator phone payload is used directly when present; this
attribute is used as the fallback area-code source for older accounts. If empty, provisioning may
proceed without area-code preference. During Agent Creator reinitialization, an existing value is
preserved as long as the requested country code is unchanged, so an area-code-only change does not
replace the already provisioned phone region; if the reinitialization request specifies a different
country code, the provisioned region is dropped and a new number is bought using the newly requested
region. This field is mainly relevant during account initialization.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_voice_phone_alpha2_code`: Country context required for area-code
    based number search.
  - `project_representative_agent_voice_phone_fallback_area_code`: Secondary area-code option when
    the primary area has no available numbers.
- **Logic Interactions:**
  - When the advanced system configuration
    `project_attributes_private_account_initialized_first_time` is `True`, first-time
    number-purchase flow is skipped.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_representative_agent_voice_phone_alpha2_code`


**Title:** Voice - AI Phone - ISO 3166-1 Alpha-2 Code [C]

**Description:**

```md
Two-letter ISO country code used for Agent phone-number provisioning (for example, `US`, `NL`).

**Pro-Tip:** Keep this value uppercase and valid ISO 3166-1 alpha-2 to avoid provisioning errors.

**Examples:**

- **`US`:** United States provisioning context.
- **`NL`:** Netherlands provisioning context.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Used as country context during first-time connector phone-number provisioning and
to derive the numeric default country dialing code used in user phone normalization/extraction.

**Fallbacks:** Initialization reads this from `agent_creator_voice_channel_phone.country_code` when
available. During phone purchase, Agent Creator phone payload is used directly when present; this
attribute is used as the fallback country source for older accounts. If missing, the system stores a
null-like placeholder and later country-code mapping may produce no numeric country code. During
Agent Creator reinitialization, an existing value is preserved only when the requested country code
matches the current one; if the reinitialization request specifies a different country code, the
provisioned region is dropped and a new number is bought in the new country.

**Dependencies:**

- **Primary Settings:**
  - When the advanced system configuration `project_representative_agent_voice_phone_country_code`
    is present, it is derived from this alpha-2 code via internal country-code mapping.
- **Logic Interactions:**
  - When the advanced system configuration `project_representative_agent_voice_phone_area_code` is
    provided, it is combined with this country context for number purchase requests.
  - When the advanced system configuration
    `project_representative_agent_voice_phone_fallback_area_code` is provided, it is treated as a
    secondary area preference within the same country context.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_representative_agent_voice_phone_fallback_area_code`


**Title:** Voice - AI Phone - Area Code Fallback [C]

**Description:**

```md
Backup area code used if the primary area code has no available phone numbers.

**Pro-Tip:** Choose a nearby region your business can still serve naturally.

**Examples:**

- **Primary `408`, fallback `650`:** Keep provisioning in the same metro area.
- **Primary unavailable:** System retries using fallback.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Sent as a fallback parameter in first-time phone purchase requests when the
primary area-code lookup fails.

**Fallbacks:** Initialization reads this from `agent_creator_voice_channel_phone.fallback_area_code`
when available. During phone purchase, Agent Creator phone payload is used directly when present;
this attribute is used as the fallback area-code source for older accounts. If both sources are
empty, number purchase runs without a fallback area-code preference. During Agent Creator
reinitialization, an existing value is preserved as long as the requested country code is unchanged;
if the reinitialization request specifies a different country code, the provisioned region is
dropped and a new number is bought using the newly requested region.

**Dependencies:**

- **Primary Settings:**
  - `project_representative_agent_voice_phone_area_code`: First-choice area before fallback is used.
  - `project_representative_agent_voice_phone_alpha2_code`: Country context for both primary and
    fallback area-code selection.
- **Logic Interactions:**
  - When the advanced system configuration
    `project_attributes_private_account_initialized_first_time` is `True`, first-time
    number-purchase flow is skipped.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_representative_agent_voice_phone_country_code`


**Title:** Voice - AI Phone - Country Code [C]

**Description:**

```md
Numeric country dialing code used as the default for phone formatting and parsing.

**Pro-Tip:** Store only digits (no `+` sign), because downstream phone parsing expects numeric
country code values.

**Examples:**

- **`1`:** Default dialing code for US/Canada contexts.
- **`31`:** Dialing code for Netherlands context.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Automatically derived from the alpha-2 country code and injected into explicit
constraints, transfer, reporting, user-information extraction, and phone-validation prompt schemas
as the default dialing context.

**Fallbacks:** If alpha-2 mapping is unavailable, this field is set to a null-like placeholder.
System mapping can repopulate it when a valid alpha-2 value is available. Agent Creator phone
payload can seed the alpha-2 source used by this mapping during first initialization. During Agent
Creator reinitialization, the existing phone-region attributes are preserved while the requested
country code is unchanged, so this value continues to follow the preserved alpha-2 source; if the
reinitialization request specifies a different country code, the region is re-derived from the new
request and a new number is bought accordingly.

**Dependencies:**

- **Primary Settings:**
  - When the advanced system configuration `project_representative_agent_voice_phone_alpha2_code` is
    present, it is used as the source for country-code mapping.
- **Logic Interactions:**
  - `project_attributes_setting_transfer_call_phone_numbers`: Transfer-phone parsing treats this as
    the default country code.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `number`

**Is hidden:** `true`

---

## `project_representative_agent_voice_stt_model_id`


**Title:** Voice - 4 - STT Model ID [C]

**Description:**

```md
Stores the speech-to-text model ID for the representative Agent voice configuration.

**Pro-Tip:** Leave this hidden field unchanged unless your setup process requires a specific STT
model ID.

**Examples:**

- **`nova-2`**
- **`nova-2-phonecall`**

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During common account setup, the system creates this hidden field and writes a
blank placeholder when no value is provided. This field does not currently change the Agent's active
voice behavior.

**Fallbacks:** If no value is provided during setup, the system stores a blank placeholder.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required for setup-time initialization of this field.
- **Logic Interactions:**
  - No active transcription or voice-processing logic currently depends on this field.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_representative_agent_voice_stt_provider_id`


**Title:** Voice - 3 - STT Provider ID [C]

**Description:**

```md
Stores the speech-to-text provider ID for the representative Agent voice configuration. This hidden
field does not currently affect the Agent's active voice behavior.

**Pro-Tip:** Leave this hidden field unchanged unless your setup process requires a specific STT
provider ID.

**Examples:**

- **`deepgram`**
- **`11labs`**

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During common account setup, the system creates this hidden field and writes a
blank placeholder when no value is provided. This field does not currently change the Agent's active
voice behavior.

**Fallbacks:** If no value is provided during setup, the system stores a blank placeholder.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required for setup-time initialization of this field.
- **Logic Interactions:**
  - No active transcription or voice-processing logic currently depends on this field.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_representative_agent_voice_transcriber_language`


**Title:** Voice - 5 - STT Transcriber Language [C]

**Description:**

```md
Stores the speech-to-text language code for the representative Agent voice configuration. This
hidden field does not currently affect the Agent's active voice behavior.

**Pro-Tip:** Leave this hidden field unchanged unless your setup process requires a specific STT
language code.

**Examples:**

- **`en-US`**
- **`es`**
- **`fr`**

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During common account setup, the system creates this hidden field and writes a
blank placeholder when no value is provided. This field does not currently change the Agent's active
voice behavior.

**Fallbacks:** If no value is provided during setup, the system stores a blank placeholder.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required for setup-time initialization of this field.
- **Logic Interactions:**
  - No active transcription or voice-processing logic currently depends on this field.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_representative_agent_voice_tts_model_id`


**Title:** Voice - 2 - TTS Model ID [C]

**Description:**

```md
Stores the text-to-speech model ID for the representative Agent voice configuration. This hidden
field does not currently affect the Agent's active voice behavior.

**Pro-Tip:** Leave this hidden field unchanged unless your setup process requires a specific TTS
model ID.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During common account setup, the system creates this hidden field and writes a
blank placeholder when no value is provided. This field does not currently change the Agent's active
voice behavior.

**Fallbacks:** If no value is provided during setup, the system stores a blank placeholder.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required for setup-time initialization of this field.
- **Logic Interactions:**
  - No active speech-generation or voice-processing logic currently depends on this field.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_representative_agent_voice_tts_provider_id`


**Title:** Voice - 1 - TTS Provider ID [C]

**Description:**

```md
Stores the text-to-speech provider ID for the representative Agent voice configuration. This hidden
field does not currently affect the Agent's active voice behavior.

**Pro-Tip:** Leave this hidden field unchanged unless your setup process requires a specific TTS
provider ID.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** During common account setup, the system creates this hidden field and writes a
blank placeholder when no value is provided. This field does not currently change the Agent's active
voice behavior.

**Fallbacks:** If no value is provided during setup, the system stores a blank placeholder.

**Dependencies:**

- **Primary Settings:**
  - No additional customer settings are required for setup-time initialization of this field.
- **Logic Interactions:**
  - No active speech-generation or voice-processing logic currently depends on this field.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `string`

**Is hidden:** `true`

---

## `project_attributes_setting_voice_integration_service`


**Title:** Voice - Integration Service [C] [IMPORTANT]

**Description:**

```md
Selects which voice-integration backend the Agent uses for call operations.

**Pro-Tip:** Keep this stable in production. Changing it affects command routing for transfer,
hang-up, and telephony-related actions.

**Examples:**

- **External integration value:** Uses external connector command routing.
- **Platform-native integration value:** Uses native connector command routing and advanced voice
  mode controls.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Determines which connector/integration receives voice commands (for example,
`stop_call`, `transfer_call`, and dialpad behavior). Conversation-start flows can auto-update this
value based on the active channel integration. It is also used when creating/selecting SMS-related
voice actors and when resolving the source of the Agent voice phone number during setup.

**Fallbacks:** Default initialization sets the platform-native voice integration value. Runtime
start skills may override it when a different integration channel is detected.

**Dependencies:**

- **Primary Settings:**
  - `project_attributes_setting_voice_integration_service_voice_mode`: Applied with the
    platform-native voice integration path.
  - `project_attributes_setting_voice_integration_service_bypass_phone_number`: Synced to connector
    emergency/bypass routing settings.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `enum`

**Possible values:** `["VAPI Integration", "Platform Voice Integration"]`

**Is hidden:** `true`

---

## `project_attributes_setting_voice_integration_service_voice_mode`


**Title:** Voice - Integration Service - Voice Mode [C] [IMPORTANT]

**Description:**

```md
Defines the operating mode for the platform-native voice integration.

**Pro-Tip:** Use `voice-to-voice` or `speech-to-speech` for direct real-time spoken interaction, or
`transcriber` when you need transcript-first behavior.

**Examples:**

- **`transcriber`:** Uses transcriber-oriented conversation-start flow.
- **`voice-to-voice`:** Uses voice-to-voice conversation-start handling and spoken interaction.
- **`speech-to-speech`:** Uses speech-to-speech conversation-start handling and spoken interaction.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Controls which conversation-start skills are activated for native voice channels
and gates multiple runtime behaviors in prompt, waiting, and follow-up flows. `voice-to-voice` and
`speech-to-speech` are handled as separate direct spoken-interaction modes.

**Fallbacks:** Default initialization sets `voice-to-voice`. Connector sync logic propagates this
value to native voice connectors.

**Dependencies:**

- **Primary Settings:**
  - When the advanced system configuration `project_attributes_setting_voice_integration_service` is
    set to the platform-native voice integration option, this mode controls native voice channel
    behavior.
  - `project_attributes_setting_voice_integration_service_voice_to_voice_provider`: Used when mode
    is `voice-to-voice`. `speech-to-speech` provider selection is managed in native voice connector
    settings rather than by this attribute.
- **Logic Interactions:**
  - Voice-to-voice provider and native tool-calling settings apply only to `voice-to-voice`; they do
    not configure `speech-to-speech` provider routing or native tools.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `enum`

**Possible values:** `["transcriber", "voice-to-voice", "speech-to-speech"]`

**Is hidden:** `true`

---

## `project_attributes_setting_voice_integration_service_voice_to_voice_provider`


**Title:** Voice - Integration Service - Voice To Voice Provider [C] [IMPORTANT]

**Description:**

```md
Selects the active provider for `voice-to-voice` operation in the platform-native voice path.

**Pro-Tip:** Keep provider choice aligned with your preferred voice catalog and reliability
requirements.

**Examples:**

- **`genai`:** Uses GenAI voice-to-voice provider path.
- **`grok`:** Uses Grok voice-to-voice provider path.
- **`openai`:** Uses OpenAI voice-to-voice provider path.

---

**⚙️ Technical & System Details (Advanced)**

**System Usage:** Synced to connector `v2v_mode` settings and used as the fallback provider source
when session-level provider state is not already set by connector context.

**Fallbacks:** Default initialization sets `genai`. Runtime can override provider per session using
connector fallback settings when enabled.

**Dependencies:**

- **Primary Settings:**
  - When the advanced system configuration
    `project_attributes_setting_voice_integration_service_voice_mode` is enabled with
    `voice-to-voice`, this provider setting is used for session-level provider resolution.
  - `speech-to-speech` provider selection is managed by native voice connector settings and is not
    controlled by this attribute.
  - When the advanced system configuration `project_attributes_setting_voice_integration_service` is
    enabled with the platform-native voice integration option, this provider setting applies to
    voice-to-voice native voice channels.
- **Logic Interactions:**
  - When the advanced system configuration
    `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_voice` is
    updated, connector-sync flows propagate it to the native connector GenAI voice setting.
  - When the advanced system configuration
    `project_attributes_setting_voice_integration_service_voice_to_voice_provider_grok_voice` is
    updated, connector-sync flows propagate it to the native connector Grok voice setting.
  - When the advanced system configuration
    `project_attributes_setting_voice_integration_service_voice_to_voice_provider_openai_voice` is
    updated, connector-sync flows propagate it to the native connector OpenAI voice setting.
```

**Level:** `Customer`

**Group:** `2. Agent - Advanced`

**Value type:** `enum`

**Possible values:** `["openai", "genai", "grok"]`

**Is hidden:** `true`

---
