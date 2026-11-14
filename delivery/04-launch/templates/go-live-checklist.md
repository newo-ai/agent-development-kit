# Go-live checklist: <agent name>

Date: YYYY-MM-DD · Checked by:

## Before real callers

- [ ] The test report says "ready", and the customer's acceptance test passed
- [ ] The settings were saved to a local file today (the copy to go back to)
- [ ] Test mode is **off** (`project_attributes_setting_test_mode`)
- [ ] Integrations point to the customer's real systems, not to test accounts
- [ ] Report recipients, manager email and transfer numbers are the customer's, not the testers'
- [ ] Transfer and escalation numbers are lines where a person answers. None is the public
      business number or the AI phone number
- [ ] Hours and time zone are right, and after hours the agent says the business is closed
- [ ] The phone number's country fits the business
- [ ] The health check has no critical findings ([docs/07-health-check.md](../../../docs/07-health-check.md))

## On the live line

- [ ] A call to the business number during the forwarding window reaches the agent
- [ ] One transfer in each configured direction reached a person
- [ ] A follow-up SMS or email arrived, if configured
- [ ] One real booking appeared in the customer's system and was cancelled again, if booking is
      in scope and the customer agreed
- [ ] The conversation appears in the transcripts, and its logs have no errors

## Agreed with the customer

- [ ] The go-live mode and time: nights only / human first, AI second / AI first
      ([docs/telephony/go-live.md](../../../docs/telephony/go-live.md))
- [ ] The customer has the undo step for the forwarding, in writing
- [ ] Who reviews the first nights' calls, and when
- [ ] Whom the customer contacts when something is wrong
