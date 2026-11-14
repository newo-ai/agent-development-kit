# Playbook: improve and fix

Goal: turn a problem the owner noticed, or one found in [Review conversations](review-conversations.md), into a
tested change. Most problems are fixed with settings. Code changes are rare and risky.

## 1. Find the cause

| Symptom | Usual cause | Where to fix |
|---|---|---|
| Wrong or invented fact (price, hours, service) | the fact is missing or wrong in the settings | Knowledge settings: products and services, FAQ, terms, knowledge base text |
| "We are closed" when open, or the reverse | working hours or time zone | `project_business_working_hours`, `project_business_time_zone`, then publish `naf` |
| Agent transfers too often or never | transfer criteria or numbers | `project_attributes_setting_transfer_call_criteria`, escalation phones, `project_attributes_setting_transfer_call_enabled` |
| Wrong language or switches language | language settings | primary, secondary and multilingual agent settings |
| Greeting too long or unclear | greeting setting | `project_representative_agent_voice_greeting_phrase` |
| Talks too much, wrong tone | speaking style | `project_representative_agent_voice_speaking_style` |
| Names prices it should not, or refuses to | price rule | `project_representative_agent_providing_prices_explicit_constraint` |
| Owner got no report | report settings | `project_attributes_setting_session_ended_report_enabled`, criteria, `project_business_manager_email` |
| Booking fails | booking settings or the outside booking system | see [Connect external systems](connect-external-systems.md); read logs with `levels=error` |
| Error in the logs inside a skill | a bug in the agent code or a setting the code reads | read the skill and the setting it uses; prefer fixing the setting |

To confirm a cause, read the logs of the conversation
(`GET /api/v1/analytics/logs` with `user_actor_ids` and a window of 48 hours or less, see
[API reference](../reference/api.md#logs)) and the full description of the setting in the
[attribute reference](../reference/attributes/index.md).

## 2. Change, test, confirm

1. Propose the change to the owner: setting, old value, new value, why. Wait for "yes".
2. Apply it ([API reference](../reference/api.md#change)) and read it back.
3. Publish `naf` if the setting is compiled at start (hours, time zone, languages, voice).
4. Reproduce the original problem in a sandbox chat with a new test persona, or ask the owner
   to call. A fix is done only when the same question now gets the right answer.
5. Tell the owner the result, with the old value at hand in case they want it back.

## 3. Changing skill code (last resort)

Change code only when no setting can fix the problem and the owner agrees after hearing the
risks:

- **Updates overwrite code changes.** The `naf` project is shared by all Newo customers and is
  updated from a registry. When the account follows Newo's updates (`is_auto_update_enabled: true` on
  the `naf` project, in `/api/v3/designer/projects` or, on the old designer,
  `/api/v1/designer/projects`), the next update
  replaces changed skills. In V2, publishing your own copy moves the account off Newo's updates
  until someone moves it back. Tell the owner, and suggest asking Newo support to make the fix
  for everyone.
- **A broken skill can break every call.** Change the smallest possible piece of code.

If the owner still wants it:

1. Find the skill. V2: download the running version and follow `project.yaml` to the skill's
   file ([API reference](../reference/api.md#agents-flows-and-skills)). Old designer: list agents, then the
   flow's skills ([API reference, old designer (V1 archive)](../reference/api-v1.md#agents-flows-and-skills)). Use logs (`skill_idn`,
   `flow_idn` of the failing step) to locate it.
2. Save the complete current code before changing anything (V2: keep the downloaded ZIP).
3. Learn the language: `runner_type` `nsl` or `guidance` (Jinja-like templates). Callable
   functions and their arguments: `GET /api/v1/script/actions`. Copy patterns from other
   skills in the same flow.
4. Show the owner the change as a before and after of the changed lines. Wait for "yes".
5. V2: create an editable copy of the running version, write the changed file, save the project
   attributes, publish the version and compare the attributes ([API reference](../reference/api.md#publish)). If
   the publish fails or calls break, activate the previous version again. Old designer:
   `PUT /api/v1/designer/flows/skills/{skill_id}` with the full skill object, then publish the
   flow; on errors put the old code back and publish again.
6. Wait two minutes and test.
