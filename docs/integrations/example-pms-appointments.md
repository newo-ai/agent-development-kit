# Example: appointments in a practice management system

**The request:** "Connect my clinic's patient management system. The agent should find free slots
with our doctors and book the appointment when the patient agrees."

This is a pattern, not a product guide. Replace "the PMS" with the real system, and its tool and
field names with those from its documentation.

## 1. Research the system (you, the coding assistant)

1. Find the PMS vendor's developer documentation. Look for:
   - an MCP server: address, tools, authorization;
   - or a REST API: authentication, a slots/availability endpoint, an appointment-creation
     endpoint;
   - a sandbox or test environment;
   - idempotency or duplicate-check support.
2. Find the vendor's rules for third-party integrations: does the clinic need to enable API
   access, accept terms, or sign a data-processing agreement?
3. Tell the owner what you found and what they need to do in the PMS (enable access, create
   credentials or authorize Newo). Agree on the test account.

## 2. Choose the mechanism

| The PMS has | Use |
|---|---|
| An MCP server | an MCP connector + a small skill ([mcp-client.md](mcp-client.md)) |
| Only a REST API | conversation tools with `send_webhook` ([http-rest.md](http-rest.md#4-conversation-tools-any-http-api-during-the-call)), or the booking settings if they fit |
| Neither | the agent takes the request and sends it to the clinic (session-ended webhook, email or SMS report). The staff books it manually |

## 3. Design the conversation

1. **Identify the patient** as the clinic requires: for example, name plus date of birth plus
   phone number. Never read out records before that.
2. **Collect:** reason for the visit, preferred doctor, preferred days and times.
3. **Look up** free slots (read-only). Offer two or three options, not a list of twenty.
4. **Confirm:** "Dr. Smith, Tuesday the 14th at 3:30 pm, for a check-up. Shall I book it?"
   Wait for a clear yes.
5. **Book** once (write). Confirm what the PMS returned: date, time, doctor, any reference
   number.
6. **Fail safely:** if the PMS does not answer, the agent says so, takes the request and
   promises a callback. The clinic gets the request in its report.

## 4. Configure

- The person creates the credentials or authorizes the connection in the PMS and in the Newo
  portal. You do not handle the secret.
- Add the read tool first, test it, then the write tool with the "patient confirmed" condition.
- Keep the clinic's rules in settings (hours, which doctors take which visits, cancellation
  policy), so the agent can explain them.

## 5. Test

1. In the PMS test environment:
   - a sandbox chat through the whole flow ([testing/text-tests.md](../testing/text-tests.md));
   - then a scripted test that you can repeat.
2. A real test call. Check:
   - the waiting time and the phrase that covers it;
   - how the date and time are read aloud;
   - the confirmation.
3. Logs: one read call, one write call, no duplicates.
4. Switch to the clinic's live PMS only after the owner approves. Watch the first real bookings
   with the clinic's staff.

## 6. Health data

Follow [the health data rules](README.md#health-data). Do not copy patient data into tickets,
learnings, or this repository.
