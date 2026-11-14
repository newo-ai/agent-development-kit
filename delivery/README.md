# Delivering an agent: from requirements to production

Use this when a partner delivers an agent **for a customer** and wants a repeatable process: what
to agree first, how to build, how to prove it works, how to go live, and how to keep it healthy.

A business owner who only wants to adjust their own agent does not need the whole process. Go
straight to [docs/03-configure-and-customize.md](../docs/03-configure-and-customize.md) or to the
[playbooks](../playbooks/README.md).

## The stages

| Stage | Done when | It produces |
|---|---|---|
| Setup | the Newo CLI is installed and the assistant can read the account | nothing to keep. See [docs/02-access-and-tools.md](../docs/02-access-and-tools.md): `npm i -g newo`, then `newo init` |
| [01-discover](01-discover/README.md) | the customer agreed on what the agent must do, in statements that can be tested | `requirements.md`, `acceptance-criteria.yaml` |
| [02-build](02-build/README.md) | the agent is configured, passes the health check, and answers the critical cases in a sandbox chat | `build-notes.md` |
| [03-test](03-test/README.md) | every acceptance criterion has a check, and every critical one passes | test scenarios, `test-report.md` |
| [04-launch](04-launch/README.md) | the customer accepted the agent, and it answers real callers | `go-live-checklist.md`, `uat-report.yaml`, `customer-signoff.md` |
| [05-operate](05-operate/README.md) | calls are reviewed, issues are fixed and do not come back | `weekly-review.md` |

Each stage page says what to do, links to the pages and the [playbooks](../playbooks/README.md)
of this repository that explain how, and has templates for what it produces. A playbook is one
task on one agent, step by step; a stage says when to run it and what must be true after it.

## How to use the stages

1. **Find the stage you are in.** Ask the person, or look at what already exists: is there a list
   of acceptance criteria? Is the agent taking real calls? Start from the first stage that is not
   done.
2. **Do not skip the criteria.** Stages 02 to 05 all work from `acceptance-criteria.yaml`. If an
   agent was built without one, write it before you test (01-discover, step 3).
3. **Finish a stage before the next one.** Each page has a "Done when" list. If something on it is
   not true, say so to the person and let them decide.

## Where the files go

The files a stage produces belong to the partner, not to this repository.

- Keep them in the partner's own private folder or repository, next to the agent's files, for
  example `work/<agent-name>/`. Copy the templates from the stage folders there.
- They hold business details. **Never** commit them to this repository, and never put callers'
  personal data, API keys or passwords into them. The rules in [AGENTS.md](../AGENTS.md) apply to
  every stage.

## Status (November 2026)

This is the first version of the delivery process. The steps link to what the platform and the
Newo CLI can do today. It will grow from real deliveries: if a step was wrong, missing or
unclear, propose a fix or a learning ([CONTRIBUTING.md](../CONTRIBUTING.md)).
