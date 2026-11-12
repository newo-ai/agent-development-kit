# Policy: changing the Newo Agent Framework (NAF)

`naf` is the framework shared by every Newo agent. Newo improves it continuously, and accounts
with automatic updates receive every release. A local change to NAF code splits the account off
that stream.

## Rule

**All changes happen at the level of the agent's own customization.** Modify NAF only in an
absolutely exceptional case, when no other way reaches the customer's goal. Before you touch NAF
code,
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
5. **File a NAF change notice as an issue in this repository**: New issue → "NAF change notice"
   (https://github.com/newo-ai/agent-development-kit/issues/new/choose). The repository is
   public, so the issue holds:
   - the case, described by industry and pattern;
   - why no agent-level customization could do it;
   - the diff;
   - how you tested it.

   It must not hold customer names, personal data or secrets. If Newo needs the account id or
   other private details, send them through Newo support and mention the issue number there.

## What happens with your notice

A Newo supervisor reviews every NAF change notice and decides:

| Decision | What it means for you |
|---|---|
| **Generalize into NAF** | the improvement helps agents in many industries; Newo builds it into a NAF release. When it ships, move the account back to automatic updates and drop your local change. |
| **Generalize into an industry template** | the improvement helps one industry; Newo adds it to that industry's templates. Same as above when it ships. |
| **Not planned** | Newo thanks you and explains it will not generalize this now. The account stays without automatic updates. When a new NAF release brings improvements you want, migrate yourself: take the new release, re-apply your change, test, publish. |

Newo answers in the issue.

## Migrating a local change to a new release

1. Read the release notes and compare the new release with the version you modified.
2. On a **test** account, take the new release, re-apply your change, run your tests.
3. Then do the same on the customer account, in a quiet hour, and watch the first calls.
