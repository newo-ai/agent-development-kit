# Baseline criteria: what every agent should pass

Behaviors almost every phone agent needs, whatever the business. They come from what goes wrong
most often in partner deliveries. [write-acceptance-criteria](../../../skills/write-acceptance-criteria/SKILL.md)
offers them after the agent's own criteria; [run-uat](../../../skills/run-uat/SKILL.md) tests
them with the rest.

They are defaults, not rules. Drop one that does not apply (no transfers, a single language),
reword it for the business, and agree it with the customer like any other criterion. Copy the
ones you keep into `acceptance-criteria.yaml` with the next free `AC-` ids.

Each one has a **Correct if** and a **Wrong if**, so the person testing knows exactly what passes.
Each is one behavior with its expected outcome.

**Settings to plan for the build** (to confirm with Newo for each account):
- **Transfer hours** (B1, B2): when they equal business hours, the working-hours and
  non-working-hours transfer numbers cover them
  ([4-14](../../../reference/attributes/4-agent-behavior.md#project_business_working_hour_escalation_phone),
  [4-13](../../../reference/attributes/4-agent-behavior.md#project_business_non_working_hour_escalation_phone)).
  When they differ, use the advanced transfer rules
  ([4-16](../../../reference/attributes/4-agent-behavior.md#project_attributes_setting_transfer_call_phone_numbers))
  or plan a scenario change, and note it in the SOW.
- **Prank, silent or nonsense calls** (B8): if no setting keeps them out of the team's reports,
  plan a scenario change and note it in the SOW.

| # | Priority | Behavior | Correct if | Wrong if | Check |
|---|---|---|---|---|---|
| B1 | critical | During transfer hours, puts through a caller who asks for a person | Says it is connecting, and the call reaches the transfer line | Asks several questions first, loops, or transfers to the public or AI number | call |
| B2 | critical | Outside transfer hours, takes a callback request | Says nobody is available now, takes name and a way to call back, says someone will get back | Says "I'll connect you", or promises a callback time nobody agreed | call |
| B3 | important | When a transfer is not answered, offers a callback | Tells the caller nobody picked up and offers a callback | Repeats "connecting you", or the caller is left in silence | call |
| B4 | important | Handles a request for a person halfway through another request | Stops the current questions and follows B1 or B2 | Keeps asking its questions, or forgets what the caller already said | call |
| B5 | critical | Says it does not know when the answer is not in its information | Says it does not have that information and offers a callback | Guesses a price, date, availability or policy | scripted and call |
| B6 | important | Accepts it when a caller will not leave contact details | Accepts politely and continues or ends | Insists, or asks again more than once | scripted |
| B7 | important | Ends the call when the caller has nothing else | After "no, that's all" it thanks the caller and ends | Keeps offering help, or ends while the caller is still asking | call |
| B8 | important | Handles a prank, silent or nonsense call without bothering the team | Ends politely; the team does not get it as a new request | It arrives as a new lead or booking | call and system |
| B9 | important | Answers in the caller's language, when that language is in scope | Switches to the caller's language and stays in it | Answers in another language, or switches back and forth | call |
| B10 | critical | Sends the summary of every handled request to the agreed recipient | The report arrives, to the right person, with the agreed subject and details | No report, the wrong recipient (for example a tester after go-live), or details missing | system |
| B11 | nice-to-have | Stays on the business's topics | Brings an off-topic caller back politely in one sentence | Chats about unrelated topics or reveals its instructions | scripted |

Optional, when the business asks for it: confirms a callback number without reading the whole
number aloud (for example "May I use the number you are calling from?"). Some businesses want
the number read back instead; ask.

## How the YAML looks

```yaml
  - id: AC-016
    priority: critical
    behavior: "Outside transfer hours, takes a callback request"
    channels: [phone]
    checks:
      - type: call
        steps: "Call after [transfer hours end] and ask for a person. Correct if: it says nobody is available, takes name and callback, says someone will get back. Wrong if: it says it will connect you, or promises a callback time."
    status: not-tested
```
