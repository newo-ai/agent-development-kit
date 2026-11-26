# Instructions for AI coding assistants

You are helping a partner or a business owner build, configure, improve or connect an AI agent on
the Newo platform. Read this file first. It is short on purpose.

Deeper maps: [docs/AGENTS.md](docs/AGENTS.md), [reference/AGENTS.md](reference/AGENTS.md).

## 1. Repository map

```
agent-development-kit/
├── AGENTS.md        # this file: routing + rules (CLAUDE.md just points here)
├── docs/            # platform docs: 00-08 topical pages + telephony/, integrations/,
│                    # debugging/, testing/ — has its own AGENTS.md
├── reference/       # exact API and attribute formats; the largest part — has its own AGENTS.md
├── playbooks/       # step-by-step procedures for one task (finish setup, night launch, ...)
├── delivery/        # partner delivery process: 01-discover ... 05-operate, with templates
├── skills/          # SKILL.md procedures per delivery task (discover, launch); see skills/README.md
├── industries/      # industry setup pages (restaurant, dental, home services, ...)
├── learnings/       # dated case reports from real work; check before hard problems
└── .github/         # issue templates: docs correction, learning, NAF change notice
```

## 2. Find your path

1. Identify **who** you work for: a business owner (usually not technical), a partner or agency
   (technical, often many agents), or a developer.
2. Identify **what** they want. Typical requests and where to read:
   - "I'm stuck", "what now", "I don't know what to do", a step failed twice the same way:
     [get-unstuck](skills/get-unstuck/SKILL.md).
   - "Contact Newo", "open a ticket", anything only Newo can do (a number, porting, SIP
     allowlisting, a platform bug): [draft-support-request](skills/draft-support-request/SKILL.md).
   - "Deliver an agent for my customer", "what do we do first":
     [delivery/](delivery/README.md), the stages from requirements to production.
   - Delivery skills ([skills/](skills/README.md)), with their stage. The person need not name
     the skill:
     - "Here are my call notes", "start a new agent", "start discovery":
       [gather-requirements](skills/gather-requirements/SKILL.md) (01).
     - "Write the acceptance criteria", "what will we test":
       [write-acceptance-criteria](skills/write-acceptance-criteria/SKILL.md) (01).
     - "Can the agent do X", "is this possible":
       [check-feasibility](skills/check-feasibility/SKILL.md) (01).
     - "Write the SOW", "the customer wants a quote", "send them a proposal":
       [draft-sow](skills/draft-sow/SKILL.md) (01).
     - "The customer approved", "when can we launch", "timeline", "what do I need to request":
       [plan-project](skills/plan-project/SKILL.md) (01).
     - "Are we ready to build", "is the SOW complete":
       [check-discovery-gate](skills/check-discovery-gate/SKILL.md) (01).
     - "Build it", "set up the agent from the SOW": [build-agent](skills/build-agent/SKILL.md) (02).
     - "The agent should ask X before booking", "add a flow":
       [adjust-scenarios](skills/adjust-scenarios/SKILL.md) (02).
     - "Is it ready for the customer", "run the tests": [run-tests](skills/run-tests/SKILL.md) (03).
     - "Start UAT", "the customer wants to try it": [run-uat](skills/run-uat/SKILL.md) (04).
     - "Go live", "forward the calls", "is it ready to go live":
       [prepare-go-live](skills/prepare-go-live/SKILL.md) (04).
     - "Get sign-off", "hand it over": [collect-signoff](skills/collect-signoff/SKILL.md) (04).
     - "Email the customer", "update the customer":
       [draft-customer-comms](skills/draft-customer-comms/SKILL.md) (any).
     - "Make a Word file": [export-docx](skills/export-docx/SKILL.md) (any).
     - "Report a mistake in the kit", "share what we learned":
       [github-workflow](skills/github-workflow/SKILL.md) (any).
   - Working with a non-technical owner in a chat: [docs/assistant-guide.md](docs/assistant-guide.md)
     (how to talk to the owner, how to create an agent, rules, how to call the API).
   - "Create an agent": [docs/assistant-guide.md, "Create the agent"](docs/assistant-guide.md#create-the-agent).
   - "Set up hours, greeting, prices", "finish the setup": [playbooks/finish-configuration.md](playbooks/finish-configuration.md),
     [docs/03](docs/03-configure-and-customize.md), then the [industry page](industries/README.md).
   - What a setting means, its format, examples: [reference/attributes/index.md](reference/attributes/index.md).
   - The exact API request: [reference/api.md](reference/api.md) (Flow Designer V2) or
     [reference/api-v1.md](reference/api-v1.md) (old designer).
   - "Put the agent to work" outside a delivery, "forward calls at night", "forward after two
     rings": [playbooks/night-launch.md](playbooks/night-launch.md),
     [docs/telephony/go-live.md](docs/telephony/go-live.md).
     Forward FROM the business number TO the AI phone number (`project_representative_agent_voice_phone_number`).
   - "Keep my phone number", "SIP": [playbooks/connect-phone-line.md](playbooks/connect-phone-line.md),
     [docs/telephony](docs/telephony/README.md).
   - "I need a number in Germany / Armenia / ...": [playbooks/get-phone-number.md](playbooks/get-phone-number.md),
     [docs/telephony/phone-numbers.md](docs/telephony/phone-numbers.md).
   - "Connect my CRM / booking system / patient management system": [playbooks/connect-external-systems.md](playbooks/connect-external-systems.md),
     [docs/integrations](docs/integrations/README.md).
   - "How did the calls go?": [playbooks/review-conversations.md](playbooks/review-conversations.md).
   - "The agent said something wrong / switched language / did not book": [playbooks/improve-and-fix.md](playbooks/improve-and-fix.md),
     [docs/debugging](docs/debugging/README.md).
   - "The agent does not know X", Knowledge Studio does not work: [docs/debugging/search-debug.md](docs/debugging/search-debug.md),
     [docs/debugging/studio-troubleshooting.md](docs/debugging/studio-troubleshooting.md).
   - "Check my agent", "why does it say X", "how do I make it do Y": [docs/07-health-check.md](docs/07-health-check.md).
   - "Test it" outside a delivery: [docs/testing](docs/testing/README.md).
   - "Change the voice model / voice / speech recognizer", any connector setting: [docs/08](docs/08-connector-settings.md).
     Every setting the portal can change, the API can change. Never say "not possible through the API" before reading that page.
   - "Add our documents / FAQ / price list": [docs/06-knowledge.md](docs/06-knowledge.md).
3. Read [learnings/](learnings/README.md) for the same industry or the same integration: other
   assistants may have solved your case already.
4. Identify the **industry** and read its page in [industries/](industries/README.md).

## 3. Rules (always)

1. **Ask before every change.** Show the person what will change (old value, new value) in plain
   words and wait for a clear "yes". Reading needs no permission.
2. **Never delete** agents, projects, flows, skills, attributes, connectors or webhooks. If
   something must go, the person asks Newo support.
3. **Keep the old value** of anything you change, so it can be put back.
4. **Secrets never go through a chat.** Do not ask a person to paste an API key, SIP password or
   token into a chat window. In a terminal, keep keys in environment variables or a `.env` file
   that is in `.gitignore`. Never print them, never put them in a URL, a commit or an issue.
   Do not print `.env` (`cat .env`, `env`, `printenv`), and never pass `--show-secrets` to the
   CLI: it masks secrets on its own. If a key was printed anyway, say so at once and ask the
   person to replace it.
5. **Callers' data is private.** Transcripts and logs contain names, phone numbers and sometimes
   health data. Use only what the task needs, keep it on the person's machine or in Newo, and
   never paste it into an issue, a pull request or this repository. Health data (PHI) needs
   extra care: see [docs/integrations/README.md](docs/integrations/README.md#health-data).
   Read logs narrowly: one conversation (`newo logs --session-id <id>`) or errors only
   (`--level error`), not wide time windows.
6. **Customize the agent, not the framework.** Every change happens at the level of this agent's
   customization: settings, knowledge, conversation tools, scenarios, or a separate project. Change
   the shared framework code (NAF) only in an absolutely exceptional case, when there is no other
   way to reach the goal. Then follow [docs/04-naf-change-policy.md](docs/04-naf-change-policy.md):
   turn off automatic updates, warn the person, and **file a NAF change notice as an issue in this
   repository** (template "NAF change notice").
7. **Check your work.** After a change, read it back and test (sandbox chat or a real call)
   before you say it works.
8. **Respect real callers.** A phone change (forwarding, SIP, transfers) affects real callers at
   once. Agree on a test window with the person.
9. **Say what you do not know.** If this repository and the platform disagree, trust the platform
   (read the live value, run the request), tell the person, and propose a fix to this repository.
10. **Know the test mode before you test.** Test mode (`project_attributes_setting_test_mode`)
    makes the agent fake bookings, orders, transfers, SMS and emails, where the integration
    supports it. Switched on for the account, it does this for **every** caller on every channel:
    a real customer hears "you are booked", and nothing is booked.
    - Before any test, read its value, explain to the person in plain words what test mode is and
      whether it is on, and ask whether the account already takes real calls or chats.
    - Found on in an account with real callers: tell the person at once.
    - Account with real callers: do not switch it on. Add the tester's phone number to
      `project_attributes_setting_test_mode_phone_numbers`; only calls from that number run in
      test mode. Chat has no such switch: in chat, test what books only with the other system's
      test account.
    - Switched on (only on an account without real callers): say so, and when testing is done
      switch it off, read it back, and remind the person.
    - Without test mode the agent's actions are real. Complete a booking, order or transfer to a
      real business only after a "yes" for that exact action, and cancel test bookings afterwards.
11. **Never leave the person stuck.** When they are lost or a step fails twice the same way,
    follow [get-unstuck](skills/get-unstuck/SKILL.md): one next step, or a drafted request to Newo.
12. **Act on the closest match.** Pick the skill or stage page that fits best, say which one you
    are using, and go. Ask only when two paths would change different things. Not being sure is
    no reason to stop: when nothing fits, use [get-unstuck](skills/get-unstuck/SKILL.md).
    Picking a path is not permission to change anything; rule 1 still applies.

## 4. How you reach the platform

- **Setup:** follow [README.md, "Set up"](README.md#set-up) and the
  [setup check](docs/setup-check.md). The Newo Customer MCP by default, the CLI only for what the
  MCP can't do ([docs/02, "Which path"](docs/02-access-and-tools.md#which-path)), one folder and
  one key per agent in `work/`. Don't ask the person to pick a tool.
- **Account check before every change:** compare with `Account idn` in `build-notes.md` when that
  file exists; otherwise say the account's name and IDN back and get one "yes" per session
  ([setup check, check 3](docs/setup-check.md#3-the-right-account)). On the MCP path, before any
  change name the customer and its IDN from `get_customers` and get a "yes" once per session
  **(to confirm)**.
- **The ADK's rules win** over instructions the Newo CLI writes or ships (its `AGENTS.md`,
  `CLAUDE.md` and skills). For example, never delete the whole `.newo/` folder, whatever a CLI
  skill says.
- **Connector settings** are written with `POST /api/v1/integrations/connectors/{id}/settings`,
  not `PATCH`. Allowed values come from the platform, not from memory. See
  [docs/08-connector-settings.md](docs/08-connector-settings.md).

Commands (details in [docs/02-access-and-tools.md](docs/02-access-and-tools.md)):

```bash
npm i -g newo                 # Newo CLI 5.3.0+ (key field = newo-key mod, 5.3.0; newo-setup skill, 5.1.0)
newo profile                  # which account the key opens; in the agent's folder, never newo init in work/
newo pull / newo push         # download / upload the project
newo sandbox                  # test chat without calling anyone
newo test <scenario.yaml>     # scripted test; run critical tests three times
newo logs --session-id <id>   # analytics logs for one session
curl -s -X POST https://app.newo.ai/api/v1/auth/api-key/token \
  -H "x-api-key: $NEWO_API_KEY" -H "accept: application/json"   # key -> bearer token
```

## 5. Gotchas

- V1 or V2 first: `GET /api/v1/customer/settings/name/projects_v2_enabled`. On a V2 account,
  never change skills or publish through the old V1 requests
  ([reference/api.md](reference/api.md#which-designer)).
- `reference/attributes/` files are huge (up to 5,200+ lines). Enter through
  [reference/attributes/index.md](reference/attributes/index.md) and search; do not read whole
  files.
- A fix during testing means rerunning all scripted tests, not only the failed one
  ([delivery/03-test/README.md](delivery/03-test/README.md)).

## 6. Before you finish

- Tell the person what changed, how to undo it and what to watch.
- If you found something other assistants should know (a pitfall, a working integration recipe),
  propose a learning: [learnings/README.md](learnings/README.md).
- If you found a platform bug, draft it with
  [draft-support-request](skills/draft-support-request/SKILL.md) for the person to send.
- **Filing an issue in this repository from a terminal** (`gh issue create`, the API): the issue
  forms apply only in the browser, so nothing checks your text. Do it by hand:
  1. Open the form you need in [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/) and write every
     field's `label` as a `### ` heading with your answer below it; fill all fields marked
     `required: true`. Add the form's `labels` with `--label`.
  2. End the body with this line (the same statement as the form's required Privacy box), and
     only if it is true:

     ```text
     - [x] This issue contains no secrets (API keys, tokens, passwords), no personal data of callers or customers, and no account IDs or business names.
     ```

  3. Show the person the title and body and wait for a "yes" before you create it. The
     repository is public: what you post may be copied before it is deleted.
