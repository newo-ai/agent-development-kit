# Connector settings: how to change them through the API

Assistants often decide that a connector setting "cannot be changed through the API". The usual
reasons are a request to the wrong endpoint that answers `200` but changes nothing, or a list of
models taken from memory instead of from the platform. **Every setting you can change in the
portal can also be changed through the API.** This page shows how.

Example task: switch the voice agent to Grok 3.0 and turn off the separate speech recognizer
("User STT Provider" = `None`).

## 1. Read the allowed values from the platform, not from memory

New models appear on the platform before any assistant knows about them. Read the list:

```
GET /api/v1/integrations
```

Find the integration (`idn` = `newo_voice` for phone and web calls). Its
`connector_settings_descriptions` lists every setting with `idn`, `title`, `group`,
`possible_values` and `default_value`.

Examples (read on 2026-11-12):

| Portal label (group) | `idn` | `possible_values` |
|---|---|---|
| Model (Voice to Voice: Grok) | `grok_v2v_model` | `grok-voice-think-fast-1.0`, `grok-voice-think-fast-2.0`, `grok-voice-think-fast-3.0` |
| Voice (Voice to Voice: Grok) | `grok_v2v_voice` | `ara`, `leo`, `eve`, ... (28 voices) |
| User STT Provider (Voice To Voice) | `v2v_mode_user_stt` | `openai_transcriber`, `deepgram`, `google`, `tencent`, `elevenlabs`, `None` |

`None` is a real value, written as the string `"None"`. It means "no separate recognizer": the
voice model hears the caller itself.

If `possible_values_only` is `true`, send exactly one of the listed strings.

## 2. Find the connector and read its current settings

```
GET /api/v1/integrations/{integration_id}/connectors
GET /api/v1/integrations/connectors/{connector_id}/settings
```

A voice agent usually has **two** voice connectors: `newo_voice_connector` (phone) and
`newo_voice_connector_web` (calls in the browser). Change both, unless the person asks for only
one. **Save the old values** before the change (rule 3 in [AGENTS.md](../AGENTS.md)).

## 3. Write the settings

```
POST /api/v1/integrations/connectors/{connector_id}/settings
Content-Type: application/json

[
  {"idn": "grok_v2v_model", "value": "grok-voice-think-fast-3.0"},
  {"idn": "v2v_mode_user_stt", "value": "None"}
]
```

- The body is a JSON **array** of `{"idn", "value"}` pairs. Values are strings, including
  `"True"`, `"False"` and `"None"`.
- This is the request the portal's own **Edit Settings** form sends (seen in the portal code on
  2026-11-12). The form sends every setting of the connector. Sending the full list read in
  step 2, with your values changed, is the safest form.
- **Do not use** `PATCH /api/v1/integrations/connectors/{connector_id}` for settings. It changes
  only the connector's title and idn (`connector_idn`); a connector's status (running or stopped)
  is changed only by the `run` and `stop` requests (section 4). Settings sent to PATCH are
  ignored even though the answer is `200`.
- `PUT /api/v1/integrations/connectors/{connector_id}` answers `405 Method Not Allowed`
  (2026-11-12).
- The voice model itself (Gemini, Grok or OpenAI) is chosen by `v2v_mode`. On a NAF agent, change
  it through the setting `project_attributes_setting_voice_integration_service_voice_to_voice_provider`
  (values `genai`, `grok`, `openai`) and publish, not on the connector; see section 5.

## 4. Check the result

1. Read `GET /api/v1/integrations/connectors/{connector_id}/settings` again. The new values must
   be there. A `200` answer to the write is not proof.
2. Make a test call (see [testing/voice-tests.md](testing/voice-tests.md)). A different model or
   recognizer can change language handling, interruptions and the end of the call.
3. If the call still behaves the old way, check that the connector is `running`. Stop it and run
   it again: `POST /api/v1/integrations/connectors/{connector_id}/stop`, then `.../run`.
   (Assumption: not needed in most cases. Report it in a learning if it was.)

Tell the person how to undo: the same request with the old values.

## 5. Settings that NAF writes back

On a NAF agent, some connector settings are **copies of agent settings**. NAF writes them again
when the account is set up and when certain settings change. If you change only the connector,
NAF can later put the old value back. Change the agent setting instead:

| Connector setting (`newo_voice`) | Change this agent setting instead |
|---|---|
| `voice_mode` | `project_attributes_setting_voice_integration_service_voice_mode` |
| `v2v_mode` (Gemini / Grok / OpenAI) | `project_attributes_setting_voice_integration_service_voice_to_voice_provider` |
| `genai_v2v_voice`, `grok_v2v_voice`, `openai_v2v_voice` | `..._voice_to_voice_provider_genai_voice` / `_grok_voice` / `_openai_voice` |
| `emergency_phone_number` | `project_attributes_setting_voice_integration_service_bypass_phone_number` |
| `shared_phone_numbers` | `project_attributes_setting_common_phone_numbers` |
| `*_initial_system_instruction`, `genai_v2v_tools` | built by NAF from the agent; do not edit by hand |

| Connector setting (`newo_chat`) | Change this agent setting instead |
|---|---|
| `greeting_phrase` | `project_representative_agent_chat_greeting_phrase` |
| `agent_name` | `project_representative_agent_name` |

Settings that are **not** in these tables, for example `grok_v2v_model`, `genai_v2v_model` and
`v2v_mode_user_stt`, are not copied from agent settings. Set them on the connector (section 3).

Two more things can change a connector setting:
- **Defaults on creation.** When NAF creates a voice connector, it writes its defaults (for example
  `v2v_mode_user_stt` = `elevenlabs`). Existing connectors are not touched.
- **One-time migrations.** A NAF update can change a value once. Example: NAF 4.7.1 replaced
  `v2v_mode_user_stt` = `None` with `elevenlabs` on every account. Later publishes do not repeat it.
  The reason was the voice model of that time: Gemini 2.5 native audio recognized callers poorly,
  so a separate recognizer (ElevenLabs) was safer. This does not apply to newer models; see
  [section 7](#7-which-speech-recognizer-to-use).

Source: NAF skills `_updateConnectorSettingsNewoVoiceSkill`, `_updateConnectorSettingsNewoChatSkill`,
`prepare_connectors_newo_voice`, `_migration_4_7_1_v2v_11labs_transcription` (read 2026-11-12).

## 6. Other places where assistants give up too early

| What looks impossible | What works |
|---|---|
| "This model or voice does not exist" | Read `possible_values` (section 1). Never answer from memory. |
| A settings write answers `200`, but nothing changed | Wrong endpoint. Connector settings: section 3. Integration settings: `POST /api/v1/integrations/{integration_id}/settings` with the same array body. |
| `newo push` does not change connector settings | The CLI sends `PUT` to the connector (answers `405`). Use the API request in section 3. |
| A new connector does not work | It may be stopped. `POST /api/v1/integrations/connectors/{connector_id}/run`, then check that its status is `running`. |
| The value went back after Publish | NAF writes it from an agent setting (section 5). Change the agent setting. |
| "Only Newo support can change this" | Check first. In the portal, a person can change almost every connector setting in Builder → Integrations → the connector → **Edit Settings**; the same change works through section 3. Real exceptions: deleting things (ask the person to contact support) and read-only settings. |

## 7. Which speech recognizer to use

"User STT Provider" (`v2v_mode_user_stt`) decides who turns the caller's speech into text:
the voice model itself (`None`, native recognition) or a separate service (`elevenlabs`,
`deepgram`, `google` and others).

| Voice model (`v2v_mode` + model setting) | Recommended `v2v_mode_user_stt` |
|---|---|
| Grok (`grok_v2v_model`, for example `grok-voice-think-fast-3.0`) | **`None`** (native) |
| Gemini 3.8 (`genai_v2v_model` = `gemini-3.8-live` or newer) | **`None`** (native) |
| Gemini 2.5 native audio and older Gemini models | `elevenlabs` (the NAF default) |

Why: native recognition in Gemini 2.5 native audio was poor, which is why NAF 4.7.1 moved every
agent to ElevenLabs. Grok and Gemini 3.8 recognize speech well natively, and the native path is
recommended for them (source: the Newo voice team, 2026-11-12).

When you switch an agent to Grok or Gemini 3.8, also set `None` on both voice connectors, and
make a test call in the agent's main language (see section 4).

If something here is wrong or a request behaves differently, trust the platform, tell the person,
and propose a correction ([CONTRIBUTING.md](../CONTRIBUTING.md)).
