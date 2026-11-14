# Telephony

Every Newo agent gets its own phone number when it is created: the **AI phone number**
(`project_representative_agent_voice_phone_number`). Most businesses also want to keep the
**business number** their customers already know. Forwarding always goes from the business number
to the AI phone number.

**The recommended path to real customers: [go-live.md](go-live.md).** Nights first, review the
calls, then the day as "human first, AI second" (overflow) or "AI first, human second".

Pick the way to connect with the person:

| Way | When | Page |
|---|---|---|
| **Call forwarding** from the business number to the AI phone number: always, after hours, or when nobody answers (for example after two rings) | the simplest; works with any carrier or phone system; the usual way in the US | [connect-existing-number.md](connect-existing-number.md#a-call-forwarding) |
| **SIP registration**: the agent registers as an extension or SIP account of the business's phone system or SIP provider, and calls arrive on the business's own number | keep a local number when forwarding is expensive or impossible; the agent becomes part of the PBX (internal transfers, own caller ID) | [connect-existing-number.md](connect-existing-number.md#b-sip-registration) |
| **WebSocket voice API**: the business's own telephony or contact-center backend streams the call audio to Newo | contact centers with their own backend (for example Genesys AudioConnector) and a developer team | [websocket-voice-api.md](websocket-voice-api.md) |
| **A new number** from Newo in another country or of another type | the business has no suitable number, or wants a separate one | [phone-numbers.md](phone-numbers.md) |

Transfers from the agent back to people: [transfers.md](transfers.md).

**Every phone change affects real callers at once.** Agree on a test window with the person, test
with a call from another phone, and write down how to undo the change.

Playbooks: [Connect the business phone line](../../playbooks/connect-phone-line.md),
[Get a phone number](../../playbooks/get-phone-number.md), [Launch at night](../../playbooks/night-launch.md).
