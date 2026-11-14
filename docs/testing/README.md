# Testing

Test after every change, before you tell the person it works.

| Level | What it proves | Page |
|---|---|---|
| **Sandbox chat** | what the agent says: knowledge, rules, scenarios, tool calls | [text-tests.md](text-tests.md) |
| **Scripted chat tests** (`newo test`) | the same, repeatable, for regressions and CI | [text-tests.md](text-tests.md#scripted-tests-newo-test) |
| **Voice tests**: browser call, phone call | voice, speech recognition, latency, how numbers and dates are spoken, transfers, the phone line | [voice-tests.md](voice-tests.md) |
| **Automated voice tests** (Newo Assessor) | many simulated callers with judged outcomes | [voice-tests.md](voice-tests.md#automated-voice-tests) |

**The sandbox does not test** the phone line, the voice, transfers, SMS delivery or behavior
that depends on the call (silence, interruptions, background noise). Those need a call.

A good habit:
1. Write 5 to 20 test conversations from the owner's real questions, plus the hard cases
   (prices, after hours, transfers, booking, a caller who switches language).
2. Keep them as `newo test` scenarios in the partner's repository.
3. Run them after every change.

Playbooks: [Finish the configuration, 4. Test](../../playbooks/finish-configuration.md#4-test),
[Launch at night](../../playbooks/night-launch.md), [Review conversations](../../playbooks/review-conversations.md).
Requests: [reference/api.md, Sandbox](../../reference/api.md#sandbox).
