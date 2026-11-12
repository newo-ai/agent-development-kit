# Voice tests

## Manual

- **Browser call:** agents created through the Newo plugin get a link to talk to the agent in the
  browser (`agent_status` returns it). It is good for quick checks without a phone.
- **Phone call** to the agent's number or to the business number, if forwarding or SIP is set up.
  This is the only test of the real phone path.

A useful checklist for each call:
1. The greeting is correct, and the language matches the caller.
2. The key facts are right: hours, prices, address.
3. Numbers, dates, times and names are spoken clearly.
4. The agent waits well: no talking over the caller; no long silence while it looks something up.
5. A transfer reaches a person; a booking appears in the real system.
6. A follow-up SMS or email arrives, if configured.
7. The conversation appears in the transcripts, and the logs have no errors.

After the call, read its transcript and logs ([debugging](../debugging/README.md)).

## Test mode

`project_attributes_setting_test_mode` and the test phone number settings let the agent treat
calls from listed numbers as tests, where the integration supports it. Read the descriptions in
the [attribute reference](https://knowledge.newo.ai/agent-setup/attributes/index.md) before using
them, and switch test mode off when done.

## Automated voice tests

Newo runs automated end-to-end tests with **Assessor**:
1. Simulated callers talk to the agent by voice or text, following a written scenario.
2. Each call is judged against expected outcomes.
3. You get a report with verdicts, transcripts and recordings.

The `assessor` project you may see on an account belongs to this.

- Partners can ask Newo for an Assessor run, or for access to run it. Open a request
  ([support](../support/README.md#operations-request)) with the scenarios you want tested.
- Write scenarios the same way as chat tests: who the caller is, what they want, what must happen
  (a booking, a transfer, a correct answer) and what must not.

**(Planned)** Starting a test call and reading its result through the Newo Customer MCP server.

## Night launch: the real-caller test

Before full launch, forward the business line to the agent for a few hours outside business
hours, then review every call. Playbook:
[Launch at night](https://knowledge.newo.ai/agent-setup#night-launch).
