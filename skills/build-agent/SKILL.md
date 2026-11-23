---
name: build-agent
description: Build the agent from the agreed discovery files, change by change with the person's approval, until it passes the health check and a sandbox smoke test and is ready for testing. Use after the discovery gate passed, or when a partner asks "build the agent", "set up the agent from the SOW", "configure the agent for this customer", "is the agent ready for testing".
---

# Build the agent

Stage: [02-build](../../delivery/02-build/README.md), the whole stage. It ends at the gate "ready
for testing". This skill changes the live agent, so every change waits for a clear "yes".

## Talk to the partner in plain words

The partner knows the customer's business, not the inside of the platform. Say what the agent
will **know** and **do**; keep the technical names for `build-notes.md`.

| Say | Not |
|---|---|
| "The agent will say you are open Monday to Friday, 9 to 6, Berlin time" | "I'll set `project_business_working_hours` and `project_business_time_zone`" |
| "When a caller asks for a person, the agent will transfer them to +1 555 0100" | "I'll enable `…_transfer_call_enabled` and fill the escalation phone" |
| "The agent will look up free times in your booking system" | "I'll add a conversation tool" |
| "This changes how the conversation goes; it takes longer, and Newo updates will not change it for you" | "I'll edit the scenario" |

Use a technical name only when the partner asks for it or uses it first. Ask one question at a
time; collect the rest under "Open questions".

## Before you start

1. **The discovery gate passed.** Read in `work/<agent-name>/`: `requirements.md`,
   `acceptance-criteria.yaml`, `sow.md`, and `feasibility.md` if there is one. If the gate was not
   checked, offer to run [check-discovery-gate](../check-discovery-gate/SKILL.md) first. Without
   `acceptance-criteria.yaml` there is nothing to build against: say so and stop.
2. **Health data.** If the business handles health data, the agreement the SOW requires is in
   place before you read conversations or connect a system
   ([health data](../../docs/integrations/README.md#health-data)).
3. **The setup check passes.** Run [docs/setup-check.md](../../docs/setup-check.md) in the
   agent's folder: CLI, key, account, sandbox. The key stays in `.env`, never in the chat. Say
   the account's name and `idn` back to the partner.
4. **One folder per agent.** `work/<agent-name>/` holds this agent's `.env` (one key), its
   `build-notes.md`, the `newo pull` files and the copy of the settings
   ([folder layout](../../README.md#set-up)). Run `newo` only there. Several keys in one `.env` is
   not recommended. Never swap the key inside a folder: the CLI keeps using the old account's
   sign-in for a while. If the account check shows the wrong account, stop. Delete only the
   sign-in file, `.newo/<account idn>/tokens.json` (or `.newo/tokens.json`), and check again.
   Never delete the whole `.newo/`: it also holds what `newo push` needs to match your files to
   the platform.
5. **The agent exists.** If not, create it first:
   [assistant guide, "Create the agent"](../../docs/assistant-guide.md#create-the-agent).
6. **Designer version.** `GET /api/v1/customer/settings/name/projects_v2_enabled`. On V2 never
   use the old V1 requests ([reference/api.md](../../reference/api.md#which-designer)).

## 1. Read everything once and keep a copy

- Save everything [health check, step 1](../../docs/07-health-check.md#step-1-read-everything-once)
  lists (settings with secrets masked, canvas items, industry, designer version, automatic
  updates) to a dated folder in the partner's folder, for example `baseline-YYYY-MM-DD/`. The
  CLI's `newo pull` helps, but a later pull overwrites its files: copy them into the dated folder
  and never pull over it. Save the connector settings too
  ([docs/08](../../docs/08-connector-settings.md)); `newo pull` does not include them. This copy is
  how you put any value back.
- Read the [industry page](../../industries/README.md). If the agent's industry does not match the
  business, stop and tell the partner: the industry is changed only with Newo support.
- Copy [the build-notes template](../../delivery/02-build/templates/build-notes.md) to
  `work/<agent-name>/build-notes.md` (ask first) and fill in "The agent".

## 2. Plan where each criterion goes

For each criterion in `acceptance-criteria.yaml`, and each fact in `requirements.md` the agent
needs, choose **the lowest step of the ladder** that can do it
([docs/03](../../docs/03-configure-and-customize.md#the-ladder-always-try-the-lowest-step-first)):
a setting ([attribute reference](../../reference/attributes/index.md): search the index, do not
read whole files), knowledge, a conversation tool, a scenario change, and only then a separate
project or framework code. Voice, speech recognition and language model are connector settings
([docs/08](../../docs/08-connector-settings.md)).

Write the plan into the table "How each criterion is covered" in `build-notes.md`; the smoke
column stays empty for now. A request is a symptom, not a design: when the partner asks for a
specific fix ("add this sentence to the prompt"), find where the problem is solved properly before
you copy their wording anywhere.

Check the plan against the SOW and show the partner the result in plain words:

- every use case in `sow.md` has a place in the plan;
- every `critical` criterion is covered by something this account can do today;
- nothing out of scope is added;
- what still needs an answer, a test account, or Newo support.

The partner approves the plan before the first change. An answer nobody gave goes to "Open
questions", never into a setting as a guess.

## 3. Build, one change at a time

Follow the steps and rules of [02-build](../../delivery/02-build/README.md): settings, knowledge,
systems (read-only tools first), the phone side without forwarding real callers, scenarios last
([adjust-scenarios](../adjust-scenarios/SKILL.md)).

For every change:

1. Show the old value and the new value in plain words. Wait for "yes".
2. Check the account again, the same way the change will be made: `newo profile` from the same
   folder before a CLI change; `GET /api/v1/customer/profile` with the same token before an API
   change. One check does not prove the other. Compare the IDN with `Account idn` in
   `build-notes.md`; if they differ, stop. Before a change callers will notice (publish, test
   mode, phone, transfers), say the account's name back to the partner. If the `.env` holds keys
   for several accounts (not recommended), a command without `--customer <idn>` goes to the
   default account: pass the same `--customer` to `newo profile` as to the change.
3. Make the change. For a setting, send the whole attribute, not only the value
   ([docs/03](../../docs/03-configure-and-customize.md#changing-an-attribute)).
4. Read it back.
5. Write into `build-notes.md` what changed and why. The old value stays in the dated copy.

In addition to the 02-build rules:

- **A publish is its own change.** Publish only when the setting needs it
  ([when a change takes effect](../../docs/03-configure-and-customize.md#when-a-change-takes-effect)).
  Tell the partner first that it switches on the whole version and restarts the agent for 2 to 5
  minutes, wait for "yes", then follow the [safe order](../../reference/api.md#publish): save the
  project's attributes, publish, compare, restore.
- **Test mode is a change too.** Turning it on or off needs a "yes" and a line in
  `build-notes.md`. It stops real bookings, SMS and email only where the integration supports it
  ([integrations](../../docs/integrations/README.md)).
- **Before a smoke test that books or changes something in another system,** have one of: the
  system's test account; confirmation that test mode covers that action on that channel; or the
  live-test procedure agreed in discovery (for example, a real booking cancelled after each round).
  Otherwise test only what reads.
- **`newo push` only adds knowledge articles.** Pushing an edited downloaded knowledge file adds
  all its articles again. Leave downloaded knowledge files unedited unless you mean to add
  articles.
- **Put experiments back.** A change made only to find something out is put back right after,
  even if the test failed. A planned change that fails stays until the cause is found, or is put
  back with the partner's "yes".
- **Three strikes.** If the same step fails three times the same way, stop and show the partner
  the exact error.

## 4. Health check

Run [the health check](../../docs/07-health-check.md#2-the-health-check) and fix every critical
finding (each fix goes through step 3). Write the date and what is left into `build-notes.md`.
Report the rest to the partner as Critical, Important, Nice to have.

## 5. Smoke test in a sandbox chat

For each `critical` criterion a chat can show, have one short conversation
([text tests](../../docs/testing/text-tests.md): `newo sandbox`, or the API).

- Start a **new** conversation after every change. After a publish wait 2 to 5 minutes: the first
  conversation may still run the old version.
- A different answer on an identical rerun within about five minutes may be left over from the
  previous conversation, not caused by your change.
- Each run leaves a test conversation in the list. Tell the partner; it is not deleted.
- Write pass, fail or "needs a call" into the smoke column. Keep the conversation's `session_id`;
  never copy the conversation text into a file.
- On a fail, find the cause (`newo logs --session-id <id>`), fix it through step 3, and repeat the
  smoke test for that criterion.

This is a smoke test, not the full test; that is [03-test](../../delivery/03-test/README.md).

## 6. Ready for testing?

Show the gate as a table:

| # | Check | Pass when |
|---|---|---|
| 1 | Coverage | Every criterion has a row in `build-notes.md` that names what covers it |
| 2 | Live values match | Hours, prices, transfer numbers and out-of-scope items, read back from the platform, match `requirements.md` and `sow.md` |
| 3 | Health check | No critical findings left |
| 4 | Smoke test | Every `critical` criterion a chat can show passed once; the others say "needs a call" |
| 5 | Test mode | Its state is in `build-notes.md`, and the partner chose it for 03-test |
| 6 | Build notes | Up to date: changes beyond settings, integrations, known limitations |
| 7 | Open questions | Each has an owner, or the partner accepts it |
| 8 | Clean files | No callers' personal data, keys or passwords in any file |

End with one line: "Ready for testing" or "Not ready: N items". The partner decides; never mark
the gate passed on your own. Tell them what changed and how to undo it (the dated copy).

## Next

[03-test](../../delivery/03-test/README.md).
