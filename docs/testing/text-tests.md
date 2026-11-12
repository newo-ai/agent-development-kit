# Text tests

## Sandbox chat through the API

The recipe is in the
[API reference, Sandbox](https://knowledge.newo.ai/agent-setup#api-sandbox):
1. Find the `sandbox` integration and a `running` sandbox connector.
2. Create a test persona and an actor.
3. Send a message.
4. Poll the chat history until the agent's reply appears.

To continue the conversation, keep the same actor.

## Sandbox chat with the CLI

```bash
newo sandbox "Hi, are you open on Sunday?" --json      # reply, session_id, every part of the answer
newo sandbox --list-connectors                         # which sandbox connectors exist
```

Keep the `session_id` from the JSON: it finds the logs of that conversation
(`newo logs --session-id <id>`).

## Scripted tests: `newo test`

A YAML file with turns and expectations. The CLI runs them in one conversation, stops at the first
failure, and with `--json` gives a machine-readable report with log correlation IDs.

```yaml
name: opening hours and booking
timeout: 90
turns:
  - message: "Hi, are you open on Sunday?"
    expect:
      contains: "Sunday"
  - message: "Can I book a table for two tomorrow at 7 pm?"
    timeout: 120
    expect:
      not_contains: "error"
      regex: "(7|seven)"
```

```bash
newo test ./tests/opening-hours.yaml
newo test ./tests/opening-hours.yaml --json > result.json
```

Tips:
- Expectations on exact wording break when the model rephrases. Prefer:
  - key facts (`contains: ["Sunday", "10"]`);
  - `not_contains` for what must never be said.
- Each run creates a test persona that is not deleted. Test conversations show up in the
  conversation list. Their names (`newo-cli-...`, `setup-test-...`) tell them apart.
- Integrations that create real records (bookings, CRM leads) need a test account in that system,
  or test mode on the agent.
