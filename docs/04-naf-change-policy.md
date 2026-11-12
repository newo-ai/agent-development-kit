# Policy: changing the Newo Agent Framework (NAF)

`naf` is the framework shared by every Newo agent. Newo improves it continuously, and accounts
with automatic updates receive every release. A local change to NAF code splits the account off
that stream.

## Rule

**Do not modify NAF unless no other way reaches the customer's goal.** Before you touch NAF code,
check every lower step of the ladder in
[03-configure-and-customize.md](03-configure-and-customize.md):
- settings;
- knowledge;
- conversation tools;
- scenarios;
- a separate project.

## If NAF must change

1. **Explain to the person, in plain words, before you change anything:**
   - automatic updates will be turned off for this account;
   - new Newo fixes and features will **not** reach the agent until someone migrates the change
     to a new release;
   - a mistake in framework code can break every call.

   Wait for a clear "yes".
2. **Back up** the current code first. V2: download the running version. V1: save every skill
   you will change.
3. **Turn off automatic updates** for `naf`. Otherwise the next release overwrites your change
   silently.
4. **Make the smallest possible change**, test it (sandbox and a real call), and keep a short
   changelog in the partner's repository: which file, what changed and why.
5. **File a NAF change notice** in the Newo helpdesk
   ([docs/support](support/README.md#naf-change-notice)). Include:
   - the case and the reason no setting could do it;
   - the industry;
   - the diff, without customer data;
   - how you tested it.

## What happens with your notice

A Newo supervisor reviews every NAF change notice and decides:

| Decision | What it means for you |
|---|---|
| **Generalize into NAF** | the improvement helps agents in many industries; Newo builds it into a NAF release. When it ships, move the account back to automatic updates and drop your local change. |
| **Generalize into an industry template** | the improvement helps one industry; Newo adds it to that industry's templates. Same as above when it ships. |
| **Not planned** | Newo thanks you and explains it will not generalize this now. The account stays without automatic updates. When a new NAF release brings improvements you want, migrate yourself: take the new release, re-apply your change, test, publish. |

Newo answers in the helpdesk ticket.

## Migrating a local change to a new release

1. Read the release notes and compare the new release with the version you modified.
2. On a **test** account, take the new release, re-apply your change, run your tests.
3. Then do the same on the customer account, in a quiet hour, and watch the first calls.
