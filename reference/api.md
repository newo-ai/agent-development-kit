# API reference

Base URL `https://app.newo.ai`. All bodies are JSON. Send `accept: application/json` and, after
the token step, `Authorization: Bearer <access_token>`.

Status of each request in this page:

- **checked**: called successfully with an account API key while this guide was written
  (November 2026).
- **from client code**: taken from the official Newo CLI source; not called while writing this
  guide. Expect it to work, but read the response carefully the first time.
- **from platform docs**: taken from Newo's Flow Designer V2 API description (November 2026);
  not called while writing this guide.

Rules from [the guide](../docs/assistant-guide.md) apply: ask the owner before every change, never DELETE.

**Flow Designer V2.** From 9 November 2026 accounts move to Flow Designer V2. In V2 the agent's
code (agents, flows, skills, libraries) is a set of **files in a project version**, and only a
whole version can be published. Check which designer the account uses first
([Which designer](#which-designer)). The old reference is kept in
[API reference, old designer (V1 archive)](api-v1.md) for accounts that are not migrated yet.

## Contents

1. [Authentication](#authentication)
2. [Which designer](#which-designer)
3. [Account and projects](#account-and-projects)
4. [Attributes (settings)](#attributes)
5. [Agents, flows and skills (V2 files)](#agents-flows-and-skills)
6. [Publish and activate](#publish)
7. [Conversations and transcripts](#conversations)
8. [Logs](#logs)
9. [Test chat (sandbox)](#sandbox)
10. [Integrations and connectors](#integrations-and-connectors)
11. [Webhooks](#webhooks)
12. [Knowledge base (AKB)](#akb)
13. [Known limits](#known-limits)

## Authentication

`POST /api/v1/auth/api-key/token` (checked). Header `x-api-key: <api_key>`, no body.

```bash
TOKEN=$(curl -s -X POST https://app.newo.ai/api/v1/auth/api-key/token \
  -H "x-api-key: $NEWO_API_KEY" -H "accept: application/json" \
  | python3 -c 'import sys,json; print(json.load(sys.stdin)["access_token"])')
H=(-H "Authorization: Bearer $TOKEN" -H "accept: application/json")
curl -s "${H[@]}" https://app.newo.ai/api/v1/customer/profile
```

Response (HTTP 201): `access_token`, `refresh_token`, `expires_in` (the string `"900"`: 15
minutes), `token_type`. When a request returns 401 or 403, request a new token with the API key
and retry once; you do not need the refresh token.

## Which designer

`GET /api/v1/customer/settings/name/projects_v2_enabled` (checked).

- `200` with `{"idn": "projects_v2_enabled", "value": "true"}`: the account uses **Flow
  Designer V2**. Use this page.
- `404`, or any other value: the account still uses the old designer (most accounts in November
  2026; migration goes account by account). Use [API reference, old designer (V1 archive)](api-v1.md) for projects, skills and
  publishing. Everything else on this page (attributes, conversations, logs, sandbox,
  integrations, webhooks, AKB) works the same for both.

Decide **only** by this setting. `GET /api/v3/designer/projects` can return projects for an
account that is not on V2 yet, and the old `/api/v1/designer/...` requests still answer on V2
accounts. On a V2 account, never change skills or publish through the old requests.

## Account and projects

| Request | Status | Returns |
|---|---|---|
| `GET /api/v1/customer/profile` | checked | `id`, `idn`, `organization_name`, `email`, `website`, `country`, `address`, `industry`, ...; business fields are often empty |
| `GET /api/v3/designer/projects` | checked | `{"items": [...]}`: projects with `id`, `idn`, `title`, `version`, `registry_idn`, `registry_item_version`, `is_auto_update_enabled` |
| `GET /api/v3/designer/projects/{project_id}` | from platform docs | one project |
| `GET /api/v3/designer/customer-links?project_idn=naf` | checked | which version the account runs: `items[0]` has either `project_version_id` (a **local** version) or `registry_idn` + `module_idn` + `module_version` (a release from a Newo registry) |
| `GET /api/v3/designer/project-versions?project_idn=naf` | checked | versions with `id`, `status` (`pending` = editable, `published` = read-only), `version_prefix`, `version_increment`, `has_customer_link` |
| `GET /api/v3/designer/registries` | from platform docs | registries (for version information only) |

`GET /api/v1/account` returns 403 with an account API key; use the profile instead.

The receptionist is the project with `idn` `naf`. Keep its `id`: most requests below need it.
**Two project ids.** On a V2 account the `naf` project has a V2 `id` (from
`/api/v3/designer/projects`; use it for attributes) and a different old `id` (from
`GET /api/v1/designer/projects`). `GET /api/v1/bff/agents/list?project_id=...` needs the **old**
id; with the V2 id it returns 404.

**Updates from Newo:** `is_auto_update_enabled` in `GET /api/v3/designer/projects` says whether
Newo updates the agent to new releases automatically; an update replaces changed skill code (see
[Improve and fix](../playbooks/improve-and-fix.md)). In the customer link, `module_version` is the
release the account runs; per the platform docs `null` means "always the latest release" and a
string pins one release.

## Attributes

### Read

| Request | Status | Notes |
|---|---|---|
| `GET /api/v1/bff/customer/attributes?include_hidden=true` | checked | `{"groups": [...], "attributes": [...]}`, 300 to 500 items, more than 1 MB |
| `GET /api/v1/bff/projects/{project_id}/attributes?query=&include_hidden=true` | checked | project attributes of one project, same shape |

Each attribute: `id`, `idn`, `value`, `title`, `description`, `group`, `is_hidden`,
`is_read_only`, `possible_values`, `value_type` (`string`, `enum`, `json`, `number`, `bool`, ...).

Values are always strings. Booleans are the strings `"True"` and `"False"`. JSON attributes hold
a JSON document serialized as a string. An empty setting is `""` or `" "`. `value_type` is a
hint, not a guarantee (a phone number of type `number` can hold `"+1..."`).

`is_read_only: true` marks settings managed by Newo (industry, the agent's phone number): do not
change them. Some values are secrets (keys, auth headers, tokens): do not display them, see the
rules in [the guide](../docs/assistant-guide.md).

The response is large. Fetch it once, save it to a local file, and filter by `idn` instead of
printing everything:

```bash
curl -s "${H[@]}" "https://app.newo.ai/api/v1/bff/customer/attributes?include_hidden=true" \
  > attrs.json
python3 -c '
import json, sys
attrs = {a["idn"]: a for a in json.load(open("attrs.json"))["attributes"]}
for idn in sys.argv[1:]:
    a = attrs.get(idn); print(idn, "=>", repr(a["value"]) if a else "(missing)")
' project_business_name project_business_working_hours project_business_time_zone
```

### Change

`PUT /api/v1/customer/attributes/{attribute_id}` (from client code) for a customer attribute,
`PUT /api/v1/designer/projects/{project_id}/attributes/{attribute_id}` (from client code) for a
project attribute.

**Always send the whole attribute**, not only the value. Read the current object, replace
`value`, send back these fields: `idn`, `value`, `title`, `description`, `group`, `is_hidden`,
`possible_values`, `value_type`. A body with only `{"value": ...}` erases the title,
description and allowed values.

```bash
python3 - <<'PY'
import json, os, urllib.request
token, idn, new_value = os.environ["TOKEN"], "project_business_working_hours", "..."
base = "https://app.newo.ai"
hdr = {"Authorization": f"Bearer {token}", "accept": "application/json",
       "content-type": "application/json"}
req = urllib.request.Request(f"{base}/api/v1/bff/customer/attributes?include_hidden=true",
                             headers=hdr)
attrs = {a["idn"]: a for a in json.load(urllib.request.urlopen(req))["attributes"]}
a = attrs[idn]
print("old value:", a["value"])
body = {k: a[k] for k in ("idn", "title", "description", "group", "is_hidden",
                          "possible_values", "value_type")}
body["value"] = new_value
req = urllib.request.Request(f"{base}/api/v1/customer/attributes/{a['id']}", method="PUT",
                             data=json.dumps(body).encode(), headers=hdr)
print(urllib.request.urlopen(req).status)
PY
```

For an `enum` attribute the new value must be one of `possible_values`. For a `json` attribute,
validate the JSON before sending. Read the value back after the change.

Attribute requests are the same in V1 and V2; in V2 use the project `id` from
`GET /api/v3/designer/projects`. **In V2, publishing a version overwrites project attributes**
(see [Publish and activate](#publish)). Before publishing, save the live attributes:
`GET /api/v1/designer/projects/{project_id}/export_attributes` (checked, with the V2 project id).

## Agents, flows and skills

In V2 there are no separate requests per agent, flow or skill. They are files of a project
version: `project.yaml` with `include` entries, agent and flow YAML files, and one code file per
skill (its `execution_path`).

| Request | Status | Returns |
|---|---|---|
| `GET /api/v1/bff/agents/list?project_id={old_project_id}` | checked | agents with their `flows` and `persona`; use it for the persona ids. Needs the old project id (see [Two project ids](#account-and-projects)) |
| `GET /api/v3/designer/project-versions/{version_id}/export` | from platform docs | the whole version as a ZIP |
| `POST /api/v3/designer/project-versions/{version_id}/export-url` | from platform docs | a signed URL to download the same ZIP |
| `POST /api/v3/designer/project-versions/{version_id}/session` | from platform docs | file access to the version in cloud storage: `api_base_url`, `bucket`, `prefix`, `access_token`, permissions (published versions: read only) |
| `GET /api/v3/designer/project-versions/{version_id}/state-fields?agent_idn=...&flow_idn=...` | from platform docs | flow state variables |
| `GET /api/v1/script/actions` | checked | the functions (actions) skill code can call, with arguments |

**Read the code:**
1. Find the version the account runs: `GET /api/v3/designer/customer-links?project_idn=naf`.
   For a registry link, the running version is the module's published version.
2. Download it (`export` or `export-url`) and unpack it locally.
3. Open `project.yaml`, follow `include` to the agents and flows, and open each skill's file at
   its `execution_path`. After a migration from V1, files are usually named
   `agents/<agent>/agent.generated.yaml` and `agents/<agent>/flows/<flow>/flow.generated.yaml`.

The `naf` project has agents such as `ConvoAgent` (the conversation logic, about 30 flows),
`GeneralManagerAgent` (setup, reports, knowledge), `TaskManager`, `EmailWorker`, `SmsWorker`,
`MultiLocationAgent`, `TestAgent`.

### Change a skill (last resort)

1. Create an editable copy of the running version:
   `POST /api/v3/designer/project-versions` with
   `{"project_idn": "naf", "source_project_version_id": "<running version id>"}` (from platform
   docs). It returns the new `id` (status `pending`).
2. Change files: either open a `session` on the new version and write the changed file, or
   change the unpacked ZIP and upload it as a new version
   (`POST /api/v3/designer/project-versions/import-url`, upload with `PUT`, then
   `POST /api/v3/designer/project-versions/import-url/complete` with
   `{"project_idn": "naf", "object_name": "...", "publish_after_import": false}`).
3. Save the live attributes, publish the version (next section), compare the attributes.

Changing code switches the agent from Newo's automatic updates to a local version: later Newo
releases will not reach it until someone moves it back. Read
[Improve and fix](../playbooks/improve-and-fix.md) before changing code.

According to its README, the Newo CLI from version 4.6.0 (`npm i -g newo`) supports V2:
`newo pull` downloads the version's files and `newo push` writes to a pending copy.

## Publish

`POST /api/v3/designer/project-versions/{version_id}/publish` (from platform docs, no body,
returns 204). It **publishes and activates** the whole version. There is no publish of one flow
or one skill.

Activation:
- switches the account to this version;
- creates missing agent personas and keeps existing ones;
- **replaces the project's live attributes with the attribute values stored in the version, and
  deletes project attributes that are not in the version.** Changes made earlier through the
  project attribute API are lost unless the version contains them. This concerns **project**
  attributes (`/api/v1/designer/projects/{project_id}/attributes`). Customer attributes
  (`/api/v1/customer/attributes`), where most business settings live, are not listed among the
  effects;
- starts the agent's initialization again (settings such as working hours, time zone, languages
  and scenarios are recompiled). Allow 2 to 5 minutes before testing.

Safe order:
1. `GET /api/v1/designer/projects/{project_id}/export_attributes` and save the file.
2. Publish.
3. Read the attributes again and compare with the saved file.
4. Restore lost values with `POST /api/v1/designer/projects/{project_id}/import_attributes`
   (it updates the given attributes and does not delete others). Ask the owner first.

To return to Newo's automatic updates, or to update to the latest release once:
`POST /api/v3/designer/customer-links` with
`{"project_idn": "naf", "link": {"type": "registry", "data": {"registry_idn": "<registry>", "module_idn": "naf", "module_version": null}}}`
(from platform docs). `null` follows every release; a version string pins one. This is also an
activation: the same attribute rules apply. Do it only when the owner agrees.

Errors come back in `message` and `reasons`; show them to the owner in plain words.

## Conversations

| Request | Status | Returns |
|---|---|---|
| `GET /api/v1/bff/conversations/user-personas?page=1&per=50` | checked | people who talked to the agent, most recent first: `id`, `name`, `last_session_id`, `session_is_active`, `last_act_time`, `last_act_text`, `act_count`, `actors`, `not_found` |
| `GET /api/v1/bff/conversations/user-personas/{persona_id}` | checked | one person |
| `GET /api/v1/chat/history?user_actor_id={actor_id}&page=1&per=100` | checked | messages of one actor, **newest first**: `id`, `type`, `datetime`, `is_agent`, `external_event_id`, `payload.text`, `payload.arguments` |

Each actor in `actors` has `id`, `integration_idn`, `connector_idn`, `external_id` and
`contact_information`. Channels:

- `newo_voice`: voice calls. `connector_idn` `newo_voice_connector` is the phone line,
  `newo_voice_connector_web` a call from the browser widget.
- `newo_chat`: website chat. `newo_sms` or `twilio_messenger`: text messages. Text messages the
  agent sends during a call also appear in the voice actor's history.
- `sandbox`: test chats.

How to read the list:

- Real callers are usually named `User`; the name tells you nothing. `act_count` counts every
  internal event (timers, HTTP calls), not messages, and can be in the thousands.
- Skip rows with `not_found: true` or name `<Persona Not Found>`, and internal names:
  `Assessor`, `ConvoAgent`, `vibe_...`, `Workflow builder actor ...`, `newo-cli-...`,
  `setup-test-...`.
- Newo's automated test calls look like real calls (`User`, `newo_voice`). They usually come in
  bursts of many calls within minutes with scripted questions; mention such bursts to the owner
  as probable test calls instead of reviewing them as customers.
- One actor's history holds all of that person's conversations, with no session id per message.
  Split it into conversations where two messages are more than two minutes apart. Page through
  with `page=2, 3, ...` while `metadata.total` is larger than what you read.

`GET /api/v1/bff/conversations/acts` returns 403 with an account API key; use the chat history.

## Logs

`GET /api/v1/analytics/logs` (checked). Query parameters:

| Parameter | Meaning |
|---|---|
| `from_datetime`, `to_datetime` | required in practice; UTC `YYYY-MM-DDTHH:MM:SS`. **Keep the window at 48 hours or less**: an unfiltered 72-hour request returned HTTP 500 (a filtered one may work); on a 500, split the period |
| `per` | page size |
| `cursor` | value of `metadata.next_cursor` from the previous page |
| `levels` | `info`, `warning`, `error` (comma-separated) |
| `log_types` | `system`, `operation`, `call` (comma-separated) |
| `project_idn`, `flow_idn`, `skill_idn` | filter by where the log came from |
| `user_actor_ids`, `user_persona_ids`, `agent_persona_ids` | filter by conversation participant |
| `external_event_id`, `runtime_context_id` | follow one event or one skill run |
| `message` | text filter |

Each item: `log_id`, `level`, `log_type`, `project_idn`, `message`, `datetime`, `data`. For
`call` logs, `data` holds `name` (the function called), `parameters`, `result`, `context`
(with `flow_idn`, `user_actor_id`), `source` (with `skill_idn`), `execution_time_ms`,
`runtime_context_id` and sometimes `prompt_script`. Items are large: use small pages
(`per=20`). `metadata.total` can be null; page with `cursor` until `next_cursor` is null.

Typical uses: `levels=error` over the night of a test launch; `user_actor_ids=<actor>` to see
what the agent did during one call. Errors are not always tagged with the caller
(`context.user_actor_id` can be null), so to find the errors of one call, also query
`levels=error` for the minutes of that call without the actor filter.

## Sandbox

A text conversation with the agent for testing, without a phone call (from client code, flow
used by the Newo CLI):

1. `GET /api/v1/integrations` (checked), find the integration with `idn` `sandbox`.
2. `GET /api/v1/integrations/{integration_id}/connectors` (checked), take a connector whose
   `status` is `running`. Most agents have `test_agent_sandbox` or `convo_agent_sandbox`.
3. `POST /api/v1/customer/personas` with `{"name": "setup-test-<random>", "title": "setup-test-<random>"}`
   returns the new persona `id`.
4. `POST /api/v1/customer/personas/{persona_id}/actors` with
   `{"name": "<same name>", "external_id": "<6 random hex characters>", "integration_idn": "sandbox", "connector_idn": "<connector_idn from step 2>", "time_zone_identifier": "<business time zone>"}`
   returns the actor `id`.
5. `POST /api/v1/chat/user/{actor_id}` with `{"text": "Hi, are you open on Sunday?", "arguments": []}`.
6. Poll `GET /api/v1/chat/history?user_actor_id={actor_id}&page=1&per=100` every second, up to
   60 seconds, until a message with `is_agent: true` newer than your message appears.
   Continue the conversation by repeating steps 5 and 6 with the same actor.

The sandbox tests what the agent says. It does not test the phone line, voice, transfers or SMS
delivery; for those, ask the owner to make a real test call.

## Integrations and connectors

| Request | Status | Returns |
|---|---|---|
| `GET /api/v1/integrations` | checked | integrations: `id`, `idn`, `title`, `description`, `is_disabled`, `connector_settings_descriptions` (which settings a connector takes) |
| `GET /api/v1/integrations/{integration_id}/connectors` | checked | connectors: `id`, `connector_idn`, `title`, `status` (`running`, ...), `settings` (`[{"idn", "value"}]`) |
| `GET /api/v1/integrations/{integration_id}/settings` | from client code | integration-level settings |
| `PATCH /api/v1/integrations/connectors/{connector_id}` | from client code | `{"title", "connector_idn"}` (both required); other fields (`status`, `settings`) are ignored, and there is no `PUT` route |
| `POST /api/v1/integrations/connectors/{connector_id}/settings` | from client code | `[{"idn", "value"}]` - change connector settings |
| `POST /api/v1/integrations/{integration_id}/connectors` | from client code | `{"title", "connector_idn", "integration_idn", "settings": [{"idn", "value"}]}` |

Connector objects can contain an `api_key` field, and settings such as `sip_password`. Never
show them to the owner or anyone else.
Change connector settings only when a playbook says so; the phone (`newo_voice`) connectors are
managed by Newo.

## Webhooks

| Request | Status | Returns |
|---|---|---|
| `GET /api/v1/webhooks` | checked | outgoing webhooks: `id`, `idn`, `description`, `connector_idn`, `url`, `command_idns` |
| `GET /api/v1/webhooks/incoming` | checked | incoming webhooks: `id`, `idn`, `url`, `connector_idn`, `event_idns`, `allowed_ips` |
| `POST /api/v1/webhooks` | from client code | `{"idn", "description": "", "url", "connector_idn", "command_idns": [...]}`; `idn`, `connector_idn`, `url` are required, and any command triggers it when `command_idns` is omitted |
| `POST /api/v1/webhooks/incoming` | from client code | `{"idn", "description": "", "connector_idn", "event_idns": [...] (at least one), "allowed_ips": [...], "response_payload": {...}}`; returns only the new `id`, and the `url` to give to the outside system comes from `GET /api/v1/webhooks/incoming` |

## AKB

The knowledge base belongs to the persona of the `GeneralManagerAgent` agent in `naf` (take
`persona.id` from the agents list).

| Request | Status | Returns |
|---|---|---|
| `GET /api/v1/akb/topics?persona_id={persona_id}&page=1&per=100&order_by=created_at` | checked | `items[].topic`: `topic_name`, `topic_summary`, `topic_facts`, `labels`, `source`, `confidence` |
| `POST /api/v1/akb/append-manual` | from client code | adds one article: `{"persona_id", "topic_name", "topic_summary", "topic_facts": [...], "confidence": 100, "source": "<who added it>", "labels": [...]}` |

Each item is `{"topic": {...}, "fuzzy_search_fields_score": ...}`. In responses, `labels` is a
string holding a list (`"['rag_context', ...]"`) and `topic_facts` is a JSON string; parse them
before use. When adding an article, send both as real JSON arrays. The topics endpoint has no
working text search; page through and filter locally. Copy the labels of existing topics (they
include `rag_context`).

If `project_attributes_setting_knowledge_source` is `akb_studio`, the agent does not use this
knowledge base; knowledge is managed in Newo Knowledge Studio. For ordinary owners, adding
knowledge through the attribute `project_attributes_rag_knowledge_base_append_text` is simpler
(see [Finish the configuration](../playbooks/finish-configuration.md)).

## Known limits

- Access tokens live 15 minutes.
- Logs: keep each request to 48 hours or less.
- `GET /api/v1/account` and `GET /api/v1/bff/conversations/acts` are not available to account
  API keys.
- The API key belongs to one account. Requests about other accounts fail.
- After a publish, allow about two minutes before testing.
- V2: only whole versions are published, and publishing replaces project attributes (see
  [Publish and activate](#publish)).
- Connector updates go through `PATCH /api/v1/integrations/connectors/{connector_id}` and only
  save `title` and `connector_idn`; anything else in the body is ignored, so an update can return
  success without saving it. Change `settings` with
  `POST /api/v1/integrations/connectors/{connector_id}/settings` and read the connector back
  after any change.
