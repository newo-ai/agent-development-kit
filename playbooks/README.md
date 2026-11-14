# Playbooks

Step-by-step tasks for an AI assistant working on one Newo agent with its owner. Each playbook
follows the rules of the [assistant guide](../docs/assistant-guide.md#rules-always) and of
[AGENTS.md](../AGENTS.md#2-rules-always): ask before every change, keep old values, never delete.

A first session usually goes 1 → 2 → 3.

| # | Playbook | When | Related pages |
|---|---|---|---|
| 0 | [Create the agent](../docs/assistant-guide.md#create-the-agent) | the owner has no agent yet | [docs/02-access-and-tools.md](../docs/02-access-and-tools.md) |
| 1 | [Finish the configuration](finish-configuration.md) | a new agent, or settings look incomplete | [docs/03-configure-and-customize.md](../docs/03-configure-and-customize.md), [industries/](../industries/README.md), [attribute reference](../reference/attributes/index.md) |
| 2 | [Launch at night](night-launch.md) | configuration is done; first real callers | [docs/telephony/go-live.md](../docs/telephony/go-live.md) |
| 3 | [Review conversations](review-conversations.md) | after real calls, or the owner asks how it went | [docs/debugging/conversation-debug.md](../docs/debugging/conversation-debug.md), [docs/07-health-check.md](../docs/07-health-check.md) |
| 4 | [Improve and fix](improve-and-fix.md) | a mistake was found | [docs/debugging/](../docs/debugging/README.md), [docs/04-naf-change-policy.md](../docs/04-naf-change-policy.md) |
| 5 | [Connect external systems](connect-external-systems.md) | calendar, CRM, booking, email/SMS, webhooks, MCP servers | [docs/integrations/](../docs/integrations/README.md) |
| 6 | [Connect the business phone line](connect-phone-line.md) | forwarding or SIP from the business's phone system | [docs/telephony/](../docs/telephony/README.md) |
| 7 | [Get a phone number](get-phone-number.md) | a number in another country or of another type | [docs/telephony/phone-numbers.md](../docs/telephony/phone-numbers.md) |
| – | [Health check](../docs/07-health-check.md) | "check my agent" | [docs/05-scenarios.md](../docs/05-scenarios.md) |
| – | [Knowledge Studio: when something does not work](../docs/debugging/studio-troubleshooting.md) | Studio building, testing, publishing or connecting fails | [docs/06-knowledge.md](../docs/06-knowledge.md) |
| – | [Debugging knowledge answers](../docs/debugging/search-debug.md) | wrong or missing answer from knowledge | [docs/06-knowledge.md](../docs/06-knowledge.md#search-services) |

The requests each playbook uses are in [reference/api.md](../reference/api.md) (Flow Designer V2)
and [reference/api-v1.md](../reference/api-v1.md) (old designer).
