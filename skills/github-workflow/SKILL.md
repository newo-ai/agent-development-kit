---
name: github-workflow
description: Open an issue or a pull request in this repository in the one style every reviewer expects. Decide issue or pull request, remove private data, fill the form or the template, and get the person's "yes" before anything is posted. Use when a partner or an assistant wants to report a mistake in these docs, share a learning, file a NAF change notice, or propose a change, for example "open an issue", "open a PR", "fix this page", "share what we learned".
---

# Issues and pull requests in this repository

Stage: any. This repository is **public**. Nothing goes to GitHub without the person's clear "yes"
on the exact text.

## 1. Choose where it goes

| The person has | It goes to |
|---|---|
| A problem with one account, one phone number, or anything that needs customer data to explain | **Newo support**, not GitHub ([docs/support/README.md](../../docs/support/README.md)) |
| A security problem | The private route in [SECURITY.md](../../SECURITY.md), never a public issue |
| A mistake or a gap in these docs, and no fix yet | Issue, form **Documentation correction** |
| A case others can learn from | Pull request with a file in [learnings/](../../learnings/README.md); an issue with the form **Learning** if a pull request is not possible |
| A change to the agent's framework (NAF) code | Issue, form **NAF change notice** ([docs/04-naf-change-policy.md](../../docs/04-naf-change-policy.md)). The account ID goes to Newo support with the issue number, never into the issue |
| A fix or a new page | Pull request |

Before you write, search what is already open (`gh issue list --search "<words>"`,
`gh pr list --search "<words>"`, or the GitHub search). Add to an existing one instead of opening
a second.

## 2. Remove private data

Go through the title, the body, every attachment, and for a pull request every commit the push
will publish, not only the final files: `git log -p --diff-merges=separate upstream/main..HEAD`
shows each commit's message and change, merge commits included. A key removed in a later commit is still public once the earlier commit is
pushed; clean the unpublished history first
([CONTRIBUTING.md](../../CONTRIBUTING.md#rules-for-every-contribution)):

- no keys, tokens, passwords, or links that carry a key;
- no callers' names, phone numbers, emails, conversation text or health data;
- no account IDs or business names: write `C_XX_EXAMPLE` and "a dental clinic in Germany".
  Never in an issue; in a pull request only if the business agreed;
- requests and responses as evidence are welcome with keys, IDs, names and numbers removed; no
  raw logs, transcripts, or screenshots that show any of the above.

Show the person anything you were not sure about and ask. If private data was already posted,
deleting it is not enough: follow
[SECURITY.md](../../SECURITY.md#if-you-published-a-secret-by-mistake).

## 3. An issue

In a browser, use the form: it checks the required fields and the privacy box. From a terminal,
follow [AGENTS.md, "Before you finish"](../../AGENTS.md#6-before-you-finish). Title: what is wrong,
in plain words, for example "Opening hours example uses the wrong day format".

## 4. A pull request

1. **Access.** If the person cannot push to this repository, fork it: `gh repo fork --remote`
   makes `origin` their fork and `upstream` this repository. Otherwise `upstream` below is
   `origin`.
2. **Branch** from the latest `main` (`git fetch upstream main`, then branch from
   `upstream/main`): `<type>/<short-name>`, lowercase, for example `docs/fix-hours-example`. One
   topic per branch and pull request.
3. **Check the change.** Every link you added or moved opens, and every heading it points to
   exists. A new skill has front matter with `name` and `description` and a row in
   [skills/README.md](../README.md). Files a partner produces for a customer (`work/<agent-name>/`)
   never go into this repository. Run `python3 scripts/check.py`: it checks links, headings,
   skill front matter, and keys, emails and account IDs.
4. **Commit.** Add files by name, never `git add -A`, and read `git diff --staged` first. The
   commit's author name and email become public; use the GitHub noreply address if that matters.
5. **Title** like the history in `git log`: `<type>: <what changes>`, starting lowercase, no period
   at the end. Types: `docs` (pages, skills, templates), `fix` (a wrong statement), `chore`
   (repository settings). Example: `docs: correct the working hours format in the restaurant page`.
6. **Body** from [the pull request template](../../.github/PULL_REQUEST_TEMPLATE.md), with no
   section removed:
   - **What this changes**: what and why, in plain words. If it resolves an issue: `Closes #<n>`.
   - **How it was verified**: the request you ran with its date (keys removed), the test
     conversation, or "documentation only".
   - **Checklist**: tick only what you checked. A claim you did not verify is labeled
     "assumption" in the text.
7. **Show the person** the title, the body, the full change (`git diff upstream/main...HEAD`) and
   any attachments; ask again if any of it changes after that. On "yes": push the branch, then `gh pr create --repo newo-ai/agent-development-kit --base main --title "<title>"
   --body-file <file>`. A body passed as a file keeps its formatting.

## 5. After it is open

- Give the person the link. Newo reviews every pull request; answer the review in the same pull
  request.
- If the branch is behind `main` and the reviewer asks for an update, use the **Update branch**
  button. If GitHub shows a conflict, the button is not there: use **Resolve conflicts** on the
  pull request page for a simple one, or ask the reviewer for help. Never force-push a branch
  somebody else works on.
