# Configure and customize an agent

## The ladder: always try the lowest step first

| Step | What | Who can do it | Survives Newo updates |
|---|---|---|---|
| 1 | **Settings (attributes)**: business info, hours, prices, greeting, transfers, FAQ, policies, reports, languages, voice | anyone, through the API, the plugin or the portal | yes |
| 2 | **Knowledge**: knowledge-base articles or Knowledge Studio | anyone | yes |
| 3 | **Conversation tools** (`project_attributes_settings_platform_tools`): look something up or act in another system during a conversation, with no code | technical users | yes |
| 4 | **Scenarios** in the Workflow Builder | technical users, in the portal | yes for cards you edited yourself |
| 5 | **A separate project** with its own agents and skills, installed next to `naf` | developers | yes, `naf` stays untouched |
| 6 | **Changing NAF code** | developers, as a last resort | **no**: see [04-naf-change-policy.md](04-naf-change-policy.md) |

Most requests stop at step 1 or 2.

## First session with a new agent

Follow the playbook
[Finish the configuration](../playbooks/finish-configuration.md):
1. Read all attributes once and save them to a local file.
2. With the owner, verify the essentials **first**:
   - products and services, and what is not offered;
   - opening hours for every day, with breaks and holidays, and the time zone;
   - prices, and whether the agent may say them on the phone.
3. Then go through the greeting, transfers to a person, FAQ, policies, reports (email/SMS after
   each conversation) and languages.
4. Read the [industry page](../industries/README.md) for what matters in that industry.

## Changing an attribute

- **Send the whole attribute**, not only `{"value": ...}`. For a customer attribute a partial
  body resets the other fields to defaults; for a project attribute the update is partial
  (fields you leave out keep their stored values). Recipe:
  [API reference, Attributes](../reference/api.md#attributes).
- **Values are strings.** Booleans are `"True"` / `"False"`. JSON attributes hold JSON serialized
  as a string: validate it before sending.
- `enum` attributes accept only `possible_values`.
- Read the value back after the change.

## When a change takes effect

- **Read at the start of each new conversation:** most text settings (greeting, business story,
  FAQ, products, transfer criteria). Test with a **new** conversation.
- **Need a project publish of `naf`:** settings compiled at start, such as working hours, time
  zone, languages, voice settings and scenarios. The agent re-initializes; wait 2 to 5 minutes.
- **Flow Designer V2:** a publish activates the whole version and replaces the project's own
  attributes with the values stored in it. Save them first
  (`GET /api/v1/designer/projects/{id}/export_attributes`), compare after, and restore with
  `import_attributes` if needed. See
  [API reference, Publish](../reference/api.md#publish).
- The first call within about two minutes after a publish may still run the previous version.

## Multi-location businesses and partners with many accounts

- One account per location is the usual setup. Keep a table of accounts (`idn`, location, phone
  number, special settings) in the partner's own repository, without secrets.
- Make a change on one test account, test it, then repeat it account by account. Read each
  account's live value first: accounts drift.
