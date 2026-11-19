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
2. Ask Newo support at https://help.newo.ai to replace the key.
3. Report it privately as above, so a maintainer can remove it from the repository history.

## What to include

The page or file, what is wrong, and what could happen. No secrets, and no callers' personal data:
describe the pattern instead.
