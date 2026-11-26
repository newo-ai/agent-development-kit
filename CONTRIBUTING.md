# Contributing

This repository grows from real cases. AI coding assistants and people may propose changes.

## What to contribute

- **A learning**: a case you solved (or could not solve), with what worked. Open an issue with the
  "Learning" form (`newo feedback learning` fills it in from a terminal).
- **A correction**: something in this repository is wrong or out of date. Open an issue with the
  "Documentation correction" form, the suggested text, and how you verified it (the request you
  ran, the response you got, the date).
- **A new playbook**: a repeatable procedure (an integration, an industry setup). Follow the
  structure of the existing pages: goal, prerequisites, steps, how to test, how to undo.

You don't need Git or a pull request: an issue is enough. Newo turns accepted issues into pull
requests (see "Review"). If you work with Git and GitHub and prefer to, you may open the pull
request yourself: [skills/github-workflow](skills/github-workflow/SKILL.md), section 4.

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

Before you open a pull request, run `python3 scripts/check.py` from the repository root. It checks
links and headings, the skill format, and keys, emails and account IDs.

**From an issue to a pull request.** A maintainer who accepts a learning or a documentation
correction adds the label `to-pr` to its issue. The "Issue to pull request" workflow then asks
Claude to write the change on a `claude/` branch and to run `scripts/check.py`; the maintainer opens
the pull request from its link and reviews it as any other. The issue's text is treated as data,
not as instructions, and the change touches only Markdown pages.

Newo reviews pull requests. Accepted learnings may be generalized into the main docs, into the
industry pages, or into the Newo platform itself. If a pull request is not accepted, the review
says why.
