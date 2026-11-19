# Security policy

This repository is public. It holds documentation, not running code, but a page can still be
wrong in a way that harms someone: an instruction that leaks a key, exposes callers' data, or
changes a real phone line without warning.

## Report a vulnerability

Use GitHub private vulnerability reporting: the **Security** tab of this repository, then
**Report a vulnerability**. Only Newo maintainers see the report.

Report there:

- a page or skill that tells an assistant to handle secrets or personal data unsafely;
- a vulnerability in the Newo platform that you found while following these docs;
- a secret, account ID or personal data that was published in this repository, an issue or a pull
  request.

Do not open a public issue or pull request for any of these.

## Not a security report

- Questions about a specific account, phone number or agent: Newo support at
  https://help.newo.ai, or your Newo contact. See [docs/support/](docs/support/README.md).
- A page that is wrong but harmless: the "Documentation correction" issue form.

## If you published a secret by mistake

1. Treat it as compromised right away, even if you delete the comment or commit: it may already
   be cached or copied.
2. Revoke or rotate it now, where it was issued: a key or token from another system (a CRM, a
   booking or payment system) in that system; a Newo API key with help from Newo support at
   https://help.newo.ai. Do not wait for this repository to be cleaned up: until the old value is
   revoked, it still works.
3. Report it privately as above, with a link to where it was published, so a maintainer can remove
   it from there: the file and its history, or the issue, pull request or comment.

## What to include

Where the problem is: the page or file, or a link to the issue, pull request or comment. Then what
is wrong and what could happen. Never repeat the exposed value, and no callers' personal data:
describe the pattern instead.
