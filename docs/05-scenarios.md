# Scenarios

A **scenario** is what the agent does for a caller intent: book an appointment, take an order, a
price question, a complaint. Each industry ships with a default scenario set.

## Where scenarios live

| What | Where | Rule |
|---|---|---|
| Which scenario set is used | `project_attributes_scenario`: `Default Scenario` or `Custom Scenario` | Keep `Default Scenario` unless the account really has a custom workflow. |
| The scenario cards (intents, scenarios, procedures) | **Workflow Builder** in the Newo portal | Change them there. |
| The compiled state | `project_attributes_private_dynamic_workflow_builder_canvas` and related `..._dynamic_...` attributes | **System-managed. Never edit them through the API.** Direct edits are overwritten when the canvas is rebuilt (on publish or on a Newo update). |

## How to change a scenario

1. First check whether a setting does it: transfer rules, booking settings, information the
   agent may send by SMS or email, explicit constraints. Most "scenario" requests are settings.
2. If not, change the scenario card in the Workflow Builder. Cards you edit yourself are kept
   when Newo updates the library; cards that come from the library are re-synced by updates.
3. Publish the `naf` project, wait 2 to 5 minutes, and test the intent with a new conversation.
4. To check what the agent really received, read the logs of the next conversation
   ([debugging](debugging/README.md)): the instructions it ran with appear in the logs of that
   session.

## When the owner should not hear about scenarios

Owners think in outcomes: "it should take reservations", "it should not give prices". Talk about
that. Do not bring up scenarios, the Workflow Builder, Vibe mode or skills unless the owner asks or
the standard setup cannot do what they want.
