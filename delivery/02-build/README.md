# 02-build: configure the agent

**Goal:** an agent that is ready to test: it does what the acceptance criteria say, with the
smallest amount of customization.

**Needs:** `requirements.md` and `acceptance-criteria.yaml` from [01-discover](../01-discover/README.md).

**Done when:**
- every acceptance criterion is covered by a setting, knowledge, a tool or a scenario, and
  `build-notes.md` says which;
- the health check has no critical findings;
- each `critical` criterion that a chat can show passes once in a sandbox chat;
- `build-notes.md` is up to date.

## Steps

1. **Read first, and keep a copy.** Read all settings once and save them to a local file
   ([health check, step 1](../../docs/07-health-check.md#step-1-read-everything-once)); with the
   CLI, `newo pull` downloads the settings and the code. This copy is how you put a value back.
2. **Read the industry page** ([industries/](../../industries/README.md)) and check that the
   agent's industry matches the business. The industry cannot be changed later without Newo
   support.
3. **Fill in the settings** from `requirements.md`: the business, hours and time zone, products
   and prices, greeting, transfers, FAQ, policies, reports. Follow
   [docs/03-configure-and-customize.md](../../docs/03-configure-and-customize.md) and put each
   kind of content into its own field
   ([one field, one kind of content](../../docs/07-health-check.md#1-one-field-one-kind-of-content)).
4. **Add knowledge** that does not fit the settings: [docs/06-knowledge.md](../../docs/06-knowledge.md).
5. **Connect the systems:** [docs/integrations/](../../docs/integrations/README.md). Use the
   mechanism that needs no code if there is one. Start with tools that only read; add tools that
   book or change something after the reading tools work.
6. **Set up the phone side** if it is in scope: the number, forwarding or SIP, transfers
   ([docs/telephony/](../../docs/telephony/README.md)). Do not forward real callers yet; that is
   [04-launch](../04-launch/README.md).
7. **Change scenarios only for what is left.** Go through the criteria that settings, knowledge
   and tools did not cover, and change the conversation logic for those
   ([docs/05-scenarios.md](../../docs/05-scenarios.md)).
8. **Run the health check** ([docs/07-health-check.md](../../docs/07-health-check.md)) and fix
   every critical finding.
9. **Smoke-test in a sandbox chat.** For each `critical` criterion, have one short conversation
   (`newo sandbox`, [text tests](../../docs/testing/text-tests.md)). Fix and repeat. Full testing
   is the next stage; this step only proves the agent is worth testing.
10. **Write the build notes:** [templates/build-notes.md](templates/build-notes.md).

## Rules

- **The lowest step of the ladder wins.** A setting before knowledge, knowledge before a tool, a
  tool before a scenario. Framework (NAF) code only under
  [docs/04-naf-change-policy.md](../../docs/04-naf-change-policy.md).
- **Keep instructions short.** Add an instruction only when a test showed it is needed. Long
  instruction texts make the agent unstable.
- **Test data only.** A test booking in a real system is a real appointment. Use the other
  system's test account, or the agent's test mode
  ([voice tests, "Test mode"](../../docs/testing/voice-tests.md#test-mode)).
- **A transfer number is a line where a person answers.** It is never the public number that
  forwards to the agent, and never the AI phone number: the call would loop.
- **Test every change in a new conversation,** and publish when the setting needs it
  ([when a change takes effect](../../docs/03-configure-and-customize.md#when-a-change-takes-effect)).
- **One change at a time** when you tune. If two things changed, you do not know which one helped.
- **Ask before every change,** and keep the old value ([AGENTS.md](../../AGENTS.md), rules 1 and 3).
