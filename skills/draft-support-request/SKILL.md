---
name: draft-support-request
description: Draft a request to Newo for something only Newo can do - a platform bug, a phone number, porting, SIP allowlisting, a NAF change notice - filled from what was found, with no keys or callers' personal data, for the person to send. Drafts only; never sends. Use when a partner says "contact Newo", "open a ticket", "ask Newo support", "report a bug", when get-unstuck finds that only Newo can help, or when a step failed twice the same way.
---

# Draft a request to Newo

Stage: any. Produces a request the person sends: text in the chat, or a draft in their own
mailbox. The templates and where to send are in
[docs/support/README.md](../../docs/support/README.md).

## 1. Pick the template

| The person needs | Template |
|---|---|
| Something on the platform is broken | [Bug report](../../docs/support/README.md#bug-report) |
| A phone number, porting, SIP allowlisting, a SIP registration check | [Operations request](../../docs/support/README.md#operations-request) |
| Access or a role on an account; removing an agent, connector, webhook or number ([rule 2](../../AGENTS.md#3-rules-always)) | [Operations request](../../docs/support/README.md#operations-request), `Request: other` |
| NAF code was changed for this account | [NAF change notice](../../docs/support/README.md#naf-change-notice) |
| A mistake in this repository, or a learning | Not Newo support: [github-workflow](../github-workflow/SKILL.md) |

## 2. Fill it from what you know

- **Account idn:** from `get_customers` (MCP path), `newo profile` (CLI path) or `build-notes.md`.
- **What happened:** what you saw, with the session id and the time in UTC. Quote only the log
  lines that matter.
- **What you checked:** the steps already tried, and that the same step failed twice the same
  way, if that is why you are here.
- **No secrets and no personal data:** no API keys, tokens or passwords; no caller names, phone
  numbers or transcripts. Describe the pattern ("a caller asked to reschedule"), not the person.
- A field you do not know stays `unknown`. Never guess one.

## 3. Show it, then hand it over

1. Show the person the whole request and wait for a "yes" or their changes.
2. Say where it goes ([docs/support/README.md, "Where"](../../docs/support/README.md#where)): the
   chat at https://help.newo.ai, the partner's Newo contact, or `partner-support@newo.ai`.
3. If the assistant is connected to the person's email and they ask for it, write it as a
   **draft** in their mailbox. Never send it: the person reads it and sends it.
4. A NAF change notice is a public issue in this repository: file it with
   [github-workflow](../github-workflow/SKILL.md), without the account id.

## Done when

- The person has the request and knows where to send it.
- Nothing was sent on their behalf.
