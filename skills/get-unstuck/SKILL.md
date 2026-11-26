---
name: get-unstuck
description: Give a person who is lost or blocked exactly one next step, or a drafted request to Newo when only Newo can help. Finds where the work stands from the files in work/<agent-name>/ and from what the person says. Use when a partner says "I'm stuck", "what now", "what's next", "I don't know what to do", "this doesn't work", or when the same step failed twice the same way.
---

# Get unstuck

Stage: any. Produces one next step, said in plain words, or a drafted request to Newo. Writes no
files.

## Rules

- **One step.** Give one next step, not a list of options. Say what it is and why, then offer to
  start it.
- **No tool choice.** Never ask the person which tool to use.
  [docs/02, "Which path"](../../docs/02-access-and-tools.md#which-path) picks it.
- **Act on the closest match.** If you are not sure, take the step that fits best and say which
  one you chose. Ask only when two steps would change different things.

## 1. Find where the work stands

Read what is there. Ask only what you cannot read.

- **What the person said** in this chat: the goal, the error, the last thing that worked.
- **The agent's folder** `work/<agent-name>/`, if there is one: which delivery files exist
  (`requirements.md`, `acceptance-criteria.yaml`, `sow.md`, `build-notes.md`, `test-report.md`,
  `uat-report.yaml`, `customer-signoff.md`). The first stage whose file is missing or not done is
  the stage the work is in ([delivery/README.md](../../delivery/README.md#how-to-use-the-stages)).
- **The connection:** can you reach the account? On the MCP path, list the customers
  (`get_customers`). On the CLI path, run the [setup check](../../docs/setup-check.md).

## 2. Pick the one next step

Go down the table and take the first line that fits. The rows are in order, most specific
first, so a step that failed twice never comes back to "retry once".

| The situation | The next step |
|---|---|
| The same step failed twice the same way | Stop retrying. First rule out the person's side: no permission in Builder, the wrong account, a wrong or old sign-in. If one of these is the cause, give that fix as the step. Otherwise go to [draft-support-request](../draft-support-request/SKILL.md) |
| You cannot reach the account at all | Connect the Newo MCP: [SOP](../../docs/sop/connect-newo-mcp.md) |
| A task needs the CLI and the person is not signed in (`newo auth status` exits 1) | `newo login`, then `newo customer switch <idn>` in the agent's folder: [SOP: sign in to the CLI](../../docs/sop/sign-in-cli.md) |
| A command or tool fails for the first time | Read the error, then the [setup check](../../docs/setup-check.md) or the [debugging pages](../../docs/debugging/README.md). Retry once with the fix |
| Only Newo can do it (a phone number, porting, SIP allowlisting, a platform bug) | [draft-support-request](../draft-support-request/SKILL.md) |
| A scenario card must change | [SOP: edit a scenario](../../docs/sop/edit-a-scenario.md) |
| A delivery is under way | The skill for the stage the work is in ([skills/README.md](../README.md)) |
| The person wants a change to their own agent, no delivery | [AGENTS.md, section 2](../../AGENTS.md#2-find-your-path) |
| Nothing above fits | Ask one question: "What should the agent do that it does not do now?" Then route the answer through [AGENTS.md, section 2](../../AGENTS.md#2-find-your-path) |

## 3. Say it and start

Say it in two or three short sentences: where things stand, the one next step and why. Then ask
"Shall I start?" and go on with that skill or page.

## Done when

- The person has one next step and has said yes or no to it, or
- A request to Newo is drafted and the person knows where to send it.
