# Skills

Step-by-step procedures a coding assistant runs for one delivery task. Each skill is a folder
with a `SKILL.md` in the [Agent Skills](https://agentskills.io) format: front matter with a `name`
and a `description` (what it does and when to use it), then the procedure.

Skills work from this repository. Paths inside a skill, such as
`delivery/01-discover/templates/sow-core.md`, are relative to the repository root. Markdown
links are relative to the SKILL.md file. The files a skill produces belong to the partner and
go in the partner's own folder, for example `work/<agent-name>/`, never into this repository
([delivery/README.md](../delivery/README.md#where-the-files-go)). The one exception is
[github-workflow](github-workflow/SKILL.md), which proposes changes to this repository itself.

## The skills

| Stage | Skill | It produces | Use when |
|---|---|---|---|
| [01-discover](../delivery/01-discover/README.md) | [gather-requirements](gather-requirements/SKILL.md) | `requirements.md` | Starting a new agent; after the discovery call |
| 01-discover | [write-acceptance-criteria](write-acceptance-criteria/SKILL.md) | `acceptance-criteria.yaml` | Requirements are confirmed |
| 01-discover | [check-feasibility](check-feasibility/SKILL.md) | `feasibility.md` | Before promising anything in a SOW |
| 01-discover | [draft-sow](draft-sow/SKILL.md) | `sow.md` (and `sow.docx`) | Criteria are done, or the partner goes straight to the SOW (fast path) |
| 01-discover | [plan-project](plan-project/SKILL.md) | `project-plan.md` with the partner checklist | Dates, and the Newo support and vendor requests to send |
| 01-discover | [check-discovery-gate](check-discovery-gate/SKILL.md) | A pass or fail report | Before building |
| [02-build](../delivery/02-build/README.md) | [build-agent](build-agent/SKILL.md) | `build-notes.md`, the configured agent, a "ready for testing" report | The discovery gate passed |
| 02-build | [adjust-scenarios](adjust-scenarios/SKILL.md) | Changed scenario cards, noted in `build-notes.md` | A criterion that settings, knowledge and tools did not cover |
| [03-test](../delivery/03-test/README.md) | [run-tests](run-tests/SKILL.md) | `tests/` scenario files, `test-report.md` | The build is ready for testing |
| [04-launch](../delivery/04-launch/README.md) | [run-uat](run-uat/SKILL.md) | `uat-report.yaml` | The test report says "ready" |
| 04-launch | [prepare-go-live](prepare-go-live/SKILL.md) | `go-live-checklist.md`, a launch schedule | UAT passed |
| Any | [draft-customer-comms](draft-customer-comms/SKILL.md) | An email draft | Any stage, to update the customer |
| 04-launch | [collect-signoff](collect-signoff/SKILL.md) | `customer-signoff.md` (short form: an email reply), handover | Live in the agreed mode |
| Any | [export-docx](export-docx/SKILL.md) | A `.docx` copy of a markdown file | The customer needs a Word document |
| Any | [github-workflow](github-workflow/SKILL.md) | An issue or a pull request in this repository | Reporting a mistake, sharing a learning, a NAF change notice, proposing a change |
| Any | [get-unstuck](get-unstuck/SKILL.md) | The next step, or a drafted request | The person is stuck |
| Any | [draft-support-request](draft-support-request/SKILL.md) | A request for the person to send | Only Newo can do it |

Steps the person does by hand (connect the MCP, get an API key, edit a scenario):
[docs/sop/README.md](../docs/sop/README.md).

The order in 01-discover:

```
gather-requirements → write-acceptance-criteria → check-feasibility → draft-sow → plan-project → check-discovery-gate
```

## Rules every skill follows

The rules in [AGENTS.md](../AGENTS.md) apply. In particular:

1. **Ask before writing.** Show the draft and wait for a clear "yes" before a file is written,
   an email is drafted for sending, or anything changes on the platform.
2. **No personal data, keys or passwords** in the files a skill writes. Transcripts and call notes
   stay on the person's machine.
3. **Say what is unknown.** An answer the person did not give goes to "Open questions", never into
   the file as a guess.
4. **Standard files, your own skills welcome.** Later stages read the files these skills produce.
   A partner may use their own skill for any step as long as it produces the same file.

## Status

First version (November 2026). These skills are early: run them, check the output, and report
what was wrong or missing ([CONTRIBUTING.md](../CONTRIBUTING.md)). Packaging as a Claude Code or
Codex plugin is planned; until then, open this repository in your coding assistant and ask for
the task by name ("run gather-requirements on my call notes").
