# Discovery call guide

A 60-minute discovery call, with the questions in the order that works best. Each question says
why we ask it and where the answer goes in [requirements.md](../templates/requirements.md). Then
add the questions for the vertical: [dental and ortho](dental-ortho.md),
[restaurant](restaurant.md), [IVR and support](ivr-support.md).

Record the call only with consent. The recording and transcript stay on the partner's machine.

## Agenda

| Minutes | Block | Goal |
|---|---|---|
| 0 to 5 | Context | Why now, what success looks like |
| 5 to 20 | Calls today | Top reasons and what happens to each |
| 20 to 30 | People and limits | Handoffs, urgent cases, things never to say |
| 30 to 40 | Systems | What the agent touches, access, test accounts |
| 40 to 50 | Phones and launch | Number, forwarding, launch window |
| 50 to 60 | Acceptance and next steps | Who tests, go-live date, inputs and owners |

## 1. Context

| Question | Why we ask | Goes to |
|---|---|---|
| What made you look at an AI agent now? | Finds the real objective: missed calls, staff time, after-hours revenue | Acceptance: Objectives |
| Six months from now, how would you know it worked? | Turns hopes into measurable objectives | Acceptance: Objectives |
| How many calls a month, and when are they missed? | Sizing; nights-first launch | Channels; SOW cover (volume) |

## 2. Calls today

| Question | Why we ask | Goes to |
|---|---|---|
| What are the five most common reasons people call? | These become the use cases | What the agent handles |
| For each: what does your team do, step by step? What does "done" look like? | Each "done" becomes an acceptance criterion | What the agent handles |
| Which calls are handled differently after hours? | Working hours and after hours differ in almost every agent | What goes to a person |
| Do you have call scripts, or recordings with personal data removed? | Real phrasing makes better tests | Facts the agent needs |

## 3. People and limits

| Question | Why we ask | Goes to |
|---|---|---|
| When must a caller reach a person? Who, at what number, in and after hours? | The escalation map. A transfer number must not be the public number | What goes to a person |
| What counts as urgent? | Urgent handling is usually critical | What goes to a person |
| What must the agent never say or promise? | "Never" rules are often the most important criteria | What the agent must never do or say |
| May the agent quote prices? Which ones? | An invented price is a critical failure | Facts the agent needs |

## 4. Systems

| Question | Why we ask | Goes to |
|---|---|---|
| Which systems hold bookings, orders, patients or customer records? | Integration scope | Systems |
| Can other tools connect to it — does it have an API? Does each have an MCP server, a REST API, or only a web interface? | Decides whether the agent can act in it, or only send a link or capture | Systems |
| Who can create credentials or authorize access? | The most common cause of delay | Systems |
| Is there a test or sandbox account? | A test booking in a live system is a real booking | Systems; Open questions and risks |
| Who gets a summary after each conversation, and how? | Reports and notifications | After a conversation |

## 5. Phones and launch

| Question | Why we ask | Goes to |
|---|---|---|
| Keep your number or get a new one? Which carrier or phone system? | Forwarding, SIP or a new number; some transfer features depend on the carrier | Channels |
| Can we start with nights and weekends? | The lowest-risk launch, with real calls for tuning | Acceptance |
| When can we change phone settings without affecting callers? | Agreed change windows | Acceptance |

## 6. Acceptance and next steps

| Question | Why we ask | Goes to |
|---|---|---|
| Who will test the agent for you, and how much time can they give? | Tester time sets the timeline | Acceptance |
| What date would you like to go live, and why that date? | Separates a real deadline from a wish | Acceptance |
| Health data? Recording consent? Where must data stay? | Compliance gates | Compliance |

## Red flags: write them down with an owner

- No test account for a system the agent must write to.
- "The agent should handle everything", with no top reasons named.
- The transfer number is the public business number (calls loop back to the agent).
- A go-live date before the customer's tester is available.
- Health data with no BAA in sight.
- Something only Newo can do: a number in a given country, SIP allowlisting
  ([operations request](../../../docs/support/README.md#operations-request)).
