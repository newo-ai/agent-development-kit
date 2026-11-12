# Appointment businesses: dental, medical, beauty, wellness

## Essentials

1. **Services**, and which provider (doctor, hygienist, stylist) does which.
2. **Hours** per location and per provider if they differ; holidays; the time zone.
3. **Prices** and insurance questions: what the agent may say, and what goes to staff.
4. **New patients vs existing patients:** what each must provide.
5. **Emergencies:** the exact instruction (an emergency number, a transfer, "call emergency
   services").

## Booking

- **Scheduling or practice management system (PMS):**
  - Check whether it has an MCP server or a REST API.
  - Use the pattern in
    [example-pms-appointments.md](../docs/integrations/example-pms-appointments.md):
    1. identify the patient;
    2. look up free slots;
    3. confirm;
    4. book once;
    5. if anything fails, fail safely.
- **Calendar** (Google Calendar, Cal.com): [http-rest.md](../docs/integrations/http-rest.md#2-calendar-appointments).
- **No integration:** the agent collects the request and the staff confirms by phone. Make that
  promise explicit to the caller.

## Health data

Dental and medical conversations contain health data. Follow
[the health data rules](../docs/integrations/README.md#health-data):
- identity check before records;
- only what is needed;
- nothing copied into tickets or learnings.

## Common requests

- **Reminders and confirmations by SMS:** check consent rules in the country.
- **Cancellations and rescheduling:** need the patient's identity and a search of their existing
  appointment before changing anything.
- **Several locations:** usually one account per location.
