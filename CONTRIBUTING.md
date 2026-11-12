# Contributing

This repository grows from real cases. AI coding assistants and people may propose changes.

## What to contribute

- **A learning**: a case you solved (or could not solve), with what worked. Add a file under
  [learnings/](learnings/README.md) using the template, or open an issue with the "Learning"
  template if you cannot open a pull request.
- **A correction**: something in this repository is wrong or out of date. Open a pull request
  with the fix and say how you verified it (the request you ran, the response you got, the date).
- **A new playbook**: a repeatable procedure (an integration, an industry setup). Follow the
  structure of the existing pages: goal, prerequisites, steps, how to test, how to undo.

## Rules for every contribution

1. **No secrets**: no API keys, tokens, SIP passwords, webhook secrets, private URLs with keys.
2. **No personal data**: no caller names, phone numbers, emails, transcripts, health data, or
   anything that identifies a business's customers. Describe the pattern, not the person.
3. **No customer identifiers** unless the business agreed: replace account IDs with
   `C_XX_EXAMPLE`, names with "a dental clinic in Germany".
4. **Say how you know**: "verified on 2026-11-12 with `GET /api/v1/...`" or "from the platform
   documentation" or "assumption". Unverified claims are fine if they are labeled.
5. **Keep it short and plain**: one idea per section, examples over theory.

## Review

Newo reviews pull requests. Accepted learnings may be generalized into the main docs, into the
industry pages, or into the Newo platform itself. If a pull request is not accepted, the review
says why.
