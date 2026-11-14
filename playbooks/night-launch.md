# Playbook: launch at night

Goal: for a few hours outside business hours, real callers reach the agent instead of voicemail.
The owner sees how the agent handles real people with little risk, then reviews the calls the next
morning.

## Before the launch

Check with the owner and fix through settings (ask before each change):

1. **Configuration is finished** ([Finish the configuration](finish-configuration.md)) and the
   owner has made at least one test call.
2. **Hours and time zone are right.** The agent decides "open" or "closed" from
   `project_business_working_hours` and `project_business_time_zone`. At night it should say the
   business is closed and offer what it can do (take a message, book, answer questions). If the
   hours say "open 24 hours", the agent treats the night as working time: ask whether that is
   true (a 24/7 service) or should become the real office hours.
3. **Transfers at night.** Outside working hours the agent transfers to
   `project_business_non_working_hour_escalation_phone`; during working hours (including a
   24/7 schedule) to `project_business_working_hour_escalation_phone`. Make sure the number used
   during the test window is answered, or set it to empty (or turn transfers off for the window)
   so the agent takes a message instead of transferring callers to a phone nobody picks up.
4. **Reports are on.** `project_attributes_setting_session_ended_report_enabled` is `"True"` and
   the criteria send a report for every conversation to the owner, so no caller is lost.
5. **Bookings.** If the agent can book, decide with the owner whether night bookings are real.
   `project_attributes_setting_test_mode` set to `"True"` stops real bookings and calendar events
   (the agent behaves as if they succeeded); leave it `"False"` for real bookings. Read its
   description in [4-agent-behavior-advanced.md](../reference/attributes/4-agent-behavior-advanced.md)
   before changing it.
6. **The agent's number.** Read `project_representative_agent_voice_phone_number`; this is
   where calls must be forwarded.

## Forwarding the business line

Forwarding is done by the owner on their phone service, not through the Newo API. Ask what the
business uses (mobile carrier, landline provider, a cloud phone system such as RingCentral,
Grasshopper or Google Voice, or a desk-phone PBX) and walk them through it:

- **Forward all calls** (unconditional forwarding) for the test window, then turn it off. Many
  US carriers use a star code to turn it on and another to turn it off, but codes differ by
  carrier and plan; look up the owner's carrier, and prefer the carrier's app or website when it
  offers forwarding settings.
- **Forward when there is no answer** is an alternative: staff answer if they are there, the
  agent takes the rest. Good for later, after the night test.
- **Cloud phone systems** usually have a schedule ("after hours" rule) that forwards to a
  number. This is the most convenient option: the owner sets the window once.
- **Toll-free numbers, call centers, phone menus (IVR).** Forwarding is a task for whoever
  manages the phone system. A safe start is to route one menu option or the after-hours queue
  to the agent's number instead of the whole line.

After forwarding is on, ask the owner to call the business number from another phone and
confirm the agent answers. Agree on the end time and remind the owner to turn forwarding off
(unless they use a schedule).

## During the night

Nothing is required. If the owner is awake and curious, you can check progress:
`GET /api/v1/bff/conversations/user-personas?page=1&per=20` shows new callers, and
`GET /api/v1/analytics/logs` with `levels=error` for the last few hours shows errors.

## The next morning

Go to [Review conversations](review-conversations.md): review every call of the night, then
[Improve and fix](improve-and-fix.md).
