# How calls are handled: <business name>

A one-page picture of the agent for the customer: what happens when someone calls, in plain
words. The customer confirms it with the requirements (email 2 in
[customer-comms.md](../../04-launch/templates/customer-comms.md)), it goes into the SOW next to
section 3A, and the final version is part of the handover.

Write it for a business owner who has never seen the Newo platform:
- Say "the assistant", not "agent", "intent", "scenario", "procedure" or "attribute".
- One row per reason people call, in the order of how often they call.
- Every row uses one of the three ways below, and names the details the assistant collects.
- Nothing here that is not in `requirements.md` and `acceptance-criteria.yaml`.

## The three ways the assistant handles a call

| Way | What it means for the caller |
|---|---|
| **Puts them through** | Connects the caller to a person right away, without extra questions. |
| **Takes details and passes them on** | Collects what your team needs, sends it to the right person, and tells the caller someone will get back to them. |
| **Answers itself** | Answers from the information you approved. If it does not know, it says so and takes details instead. |

## When someone calls

| When someone calls about… | The assistant… | Then… |
|---|---|---|
| [Reason 1, e.g. "No heat or no cooling"] | [Way, and what it collects, e.g. "Takes details and passes them on: name, address, what is wrong"] | [Who gets it and how, e.g. "The on-call technician gets a text and an email"] |
| [Reason 2, e.g. "Booking a tune-up"] | [ ] | [ ] |
| [Reason 3, e.g. "Prices, hours, service area"] | [Answers itself] | [If the answer is not in its information: takes details, the office calls back] |
| Wants to talk to a person | During [hours someone answers]: puts them through. Other times: takes details and passes them on | [Who calls back, e.g. "The office calls back the next working day"] |

## For every call

- **People answer transfers:** [days and hours]. Outside them, the assistant does not promise to
  connect; it takes details for a callback.
- **If nobody answers a transfer:** the assistant says so and takes details.
- **The assistant never:** [the "must never" list in plain words, e.g. "gives repair prices",
  "promises an arrival time", "gives advice on a gas smell other than the safety message"].
- **Languages:** [languages the assistant speaks].
- **After every call:** [who gets a summary, and how].
