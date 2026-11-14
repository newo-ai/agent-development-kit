# Going live: nights first, then the day

The recommended path from a configured agent to an agent that answers real customers. Follow it
for every business that keeps its own phone number.

## Two numbers, one direction

| Name | What it is | Where to find it |
|---|---|---|
| **Business number** | the number customers already call (mobile, landline, PBX) | the owner knows it |
| **AI phone number** | the number Newo gave the agent when it was created. Calls to it are answered by the agent | the setting `project_representative_agent_voice_phone_number` ("Agent Phone Number (AI Phone)"); the plugin's `agent_status` also returns it |

**Forwarding always goes FROM the business number TO the AI phone number.**

- **Read the AI phone number yourself** from the setting (or `agent_status`) before you talk about
  forwarding. Do not ask the owner for it, and do not confuse it with the business number the
  owner gave you.
- If the setting is empty, the agent has no number yet: tell the owner and Newo support.
- Give the owner the AI phone number in international format (`+49...`, `+1...`). Put it straight
  into the forwarding code or rule you give them.

## Stage 1: nights only

Start outside business hours, when the risk is lowest. For example, every evening from 18:00 (or
closing time) until opening.

1. **Before the first night,** check:
   - the agent knows the hours and time zone, so at night it says the business is closed and
     offers what it can do (take a message, answer questions, book);
   - transfers at night either reach someone who answers, or are off so the agent takes a message;
   - reports after each conversation go to the owner, so no caller is lost;
   - whether night bookings are real or test-only.

   Details: [Launch at night](../../playbooks/night-launch.md).
2. **Forward the business number to the AI phone number for the night window.**
   - unconditional forwarding at closing time, switched off at opening; or
   - a time-based rule in the phone system that does it every day.

   Codes and rules: [connect-existing-number.md](connect-existing-number.md#a-call-forwarding).
3. **Test once:** call the business number from another phone during the window. The agent
   answers.

## Stage 2: review two or three nights

After two or three nights, review every call with the owner. The owner can listen to the calls,
and the owner can ask you, the AI assistant, to review them.
1. Read every conversation of the night ([debugging](../debugging/conversation-debug.md)).
2. Write the owner a short summary:
   - how many calls there were and what callers wanted;
   - what went well;
   - what went wrong, with the exact moment in the transcript.
3. Propose fixes, at the agent level ([03-configure-and-customize.md](../03-configure-and-customize.md)).
   Apply them after the owner's "yes", and test.
4. Repeat for the next nights until the owner is satisfied.

## Stage 3: the day

When the owner is happy with the nights, agree on daytime. There are two ways.

| Mode | What callers experience | How to set it up |
|---|---|---|
| **Human first, AI second (overflow)** | Staff answer as usual. If nobody picks up within about two rings (10 seconds), or the line is busy, the call goes to the agent. No caller is lost and no call goes to voicemail. | **Conditional forwarding** from the business number to the AI phone number: "no answer" after 10 seconds (GSM `**61*<AI phone number>**10#`) plus "busy" (`**67*<AI phone number>#`), or the same rule in the phone system. Keep the night forwarding as well. |
| **AI first, human second** | The agent answers every call and handles what it can. It transfers to a person when the caller needs one (urgent cases, complex questions, a request for a human). | **Unconditional forwarding** to the AI phone number all day. Transfers to people are set in the agent: numbers, criteria, working and non-working hours ([transfers.md](transfers.md)). |

Most businesses start with **human first, AI second**. It changes nothing for the staff and catches
the calls they miss. Move to **AI first** when the owner trusts the agent with every call.

Keep reviewing calls weekly after each change of mode.

## Undo

The owner can always cancel forwarding (GSM `##002#` cancels all forwarding; carriers and phone
systems have their own codes or switches). Write the undo step down for the owner every time you
set forwarding.
