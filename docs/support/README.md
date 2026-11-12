# Reporting to Newo: bugs, requests, NAF change notices

One standard for every assistant and every partner, so Newo can act fast and learn from every
case.

## Where (November 2026)

- **Now:** Newo support at https://help.newo.ai (chat), or the partner's Newo contact. Copy the
  matching template below into the request.
- **For public, non-confidential findings** about this knowledge base: an issue in this
  repository with the matching template. **Never** put account-specific details, personal data or
  secrets into a public issue.
- **(Planned)** A ticket tool for coding assistants, available through the Newo MCP server.
  Requests will then go straight into Newo's helpdesk.

## Bug report

```text
Type: Bug report
Account idn: C_XX_EXAMPLE
Channel: phone | chat | SMS | email | API | plugin
When (UTC): 2026-11-12 14:05
Session id / external_event_id: ...
Expected: ...
What happened: ...
Steps to reproduce: ...
Frequency: once | sometimes | always
What you checked: settings, logs (quote only the relevant lines, no personal data)
Impact: how many calls or customers
```

## Operations request

For things only Newo can do:
- allowlist SIP/RTP IP addresses;
- a phone number in a country;
- porting a number;
- an Assessor test run;
- checking a SIP registration.

```text
Type: Operations request
Account idn: C_XX_EXAMPLE
Request: allowlist IPs | phone number | porting | Assessor run | SIP registration check | other
Details:
  - IP allowlist: provider name, SIP signaling IPs, RTP IPs
  - Phone number: country, type (local/national/mobile/toll-free), area code, calls or calls+SMS, demo or production
  - Assessor run: scenarios (attach), channel (voice/chat), number of runs
Deadline: ...
```

Documents for phone numbers are **not** attached here. Newo support replies with a secure way to
submit them.

## NAF change notice

Required whenever you modify Newo Agent Framework (NAF) code for an account. See
[04-naf-change-policy.md](../04-naf-change-policy.md).

```text
Type: NAF change notice
Account idn: C_XX_EXAMPLE
Industry: ...
Automatic updates turned off: yes (date)
NAF release the change is based on: x.y.z
The case: what the business needed
Why settings, knowledge, conversation tools, scenarios or a separate project could not do it: ...
What changed: files/skills, and a short diff without customer data
How it was tested: ...
Could this help other businesses? all industries | this industry | probably only this business
```

**What happens next:** a Newo supervisor reviews every notice and answers in the ticket with one of
three decisions:
1. **It goes into NAF.** Move the account back to automatic updates when the release ships.
2. **It goes into the industry templates.** Same as above.
3. **Not planned for now.** Stay without automatic updates and migrate your change to new
   releases yourself.

## Learning (for this repository)

A case worth sharing with other assistants, without anything confidential: see
[learnings](../../learnings/README.md).
