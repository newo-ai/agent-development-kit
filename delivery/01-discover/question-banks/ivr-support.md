# Question bank: IVR replacement and support agents

Ask after the [discovery call guide](discovery-call-guide.md). Answers feed
[sow-ivr.md](../templates/sow-ivr.md) or [sow-support.md](../templates/sow-support.md).

## IVR and routing

| Question | Why it matters |
|---|---|
| Can you share the current phone menu and the call volume for each option? | The starting routing map |
| Which phone system and carrier? How are transfers done today (extension, DTMF, SIP)? | Some transfer methods depend on the carrier; check before promising |
| Which departments have different hours? | After-hours routing per department |
| What should happen when a transfer fails or the queue is full? | A critical fallback criterion |
| Is there a directory of people callers ask for by name? | Directory routing |
| Should calls be routed by account (priority customer, open case)? Which CRM? | Stage 4 lookup |

## Support

| Question | Why it matters |
|---|---|
| What are the top contact reasons, and their share of volume? | What the agent resolves and what it routes |
| Which issues may the agent resolve alone? Which must always reach a person? | The escalation boundary |
| How do you define severity, or "critical"? | When self-service is skipped |
| Where are the approved runbooks and articles? Who keeps them current? | The agent answers only from approved content |
| What must the person receive on a handoff? | Handoff package criterion |
| Which ticketing system? May the agent create or update tickets? Is there a test queue? | Integration and fallback |
| Can you share 20 to 50 redacted transcripts with their outcomes? | A labelled test set for acceptance |

## Red flags

- No written escalation matrix.
- The knowledge base is out of date or scattered.
- "Resolve everything", with no definition of resolved.
