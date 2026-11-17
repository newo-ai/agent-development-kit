---
name: check-discovery-gate
description: Check the 01-discover files against the discovery gate (G2) and report pass or fail with exactly what is missing. Read-only. Use before building, or when a partner asks "are we ready to build", "check discovery", "is the SOW complete".
---

# Check the discovery gate (G2)

Stage: [01-discover](../../delivery/01-discover/README.md), exit. Read-only: this skill writes no
files and changes nothing. A person decides whether the gate is passed.

## Read

In `work/<agent-name>/`: `requirements.md`, `acceptance-criteria.yaml`, `feasibility.md` (if any),
`sow.md`, `project-plan.md` (if any).

## Checks

| # | Check | Pass when |
|---|---|---|
| 1 | Requirements confirmed | `requirements.md` says "Confirmed by the customer: yes" |
| 2 | Criteria agreed | `agreed_on` has a date |
| 3 | Every criterion testable | Every criterion has at least one check |
| 4 | Limits covered | Every "must never" and handoff in requirements has a criterion |
| 5 | Ids clean | `AC-001` onward, no duplicates or gaps |
| 6 | Scope tied to criteria | Every use case in `sow.md` 3A lists criteria; every critical criterion is in `sow.md` 11 |
| 7 | Out of scope written | `sow.md` section 8 lists the vertical's exclusions (or there is no vertical) and has no `[brackets]` left |
| 8 | Feasibility | No critical criterion rests on an `assumption` without a note in the Note column of `feasibility.md`'s "By criterion" table. If `feasibility.md` does not exist, offer to run [check-feasibility](../check-feasibility/SKILL.md) first, or fail this check unless the person confirms in writing that no critical criterion is an assumption |
| 9 | Systems | Every system has a test account, or the risk is accepted in writing: a line under `requirements.md`'s "Open questions and risks" like "no test account for [system]: accepted by [who] on [date]". For a live system with no test mode (for example the Reserve with Google booking path), the acceptance says a test booking is a real booking, cancelled after each round |
| 10 | Compliance | If health data: BAA before access is in the SOW |
| 11 | Go-live date | A committed date, or a plan with dates |
| 12 | Signed | The SOW is signed, or the person confirms it is |
| 13 | Clean files | No personal data, keys or passwords in any file |

## Report

Show a table with pass or fail per check and, for each fail, the file and what to add. End with
one line: "Ready to build" or "Not ready: N items". A person approves the gate; never mark it
passed on your own.

## Next

When approved: [02-build](../../delivery/02-build/README.md).
