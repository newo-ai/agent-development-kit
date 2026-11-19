# Project plan: <agent name>

Go-live target: YYYY-MM-DD (fixed / wish) · Updated: YYYY-MM-DD

Set the go-live date first and work back. Owner: Partner, Customer, Newo or Vendor. Status: not
started, in progress, done, blocked. Produced by [plan-project](../../../skills/plan-project/SKILL.md).
Add rows per location if go-lives differ.

## Partner checklist: requests and lead times

Keep the rows that apply, delete the rest; when rows are deleted, rewrite the milestones'
"Depends on" cells to list only kept rows. Send requests as early as possible: they are the most
common cause of a late go-live. ETA is the date the other side gave. Leave "Sent on" and ETA
empty until the request is sent; then write "asked" until they give one, never a guess.

| # | Request | To | Applies when | Sent on | ETA | Owner | Blocks milestone | Status |
|---|---|---|---|---|---|---|---|---|
| R1 | Phone number in [country] ([operations request](../../../docs/support/README.md#operations-request)) | Newo support | A new number is needed | | | Partner | 7 | |
| R2 | Number porting | Newo support | The business moves its number to Newo | | | Partner | 13 | |
| R3 | SIP / RTP IP allowlisting | Newo support | Connecting a PBX or SIP trunk | | | Partner | 9 | |
| R4 | Outbound calling or SMS enabled on the account | Newo support | The agent calls or texts out | | | Partner | 9 | |
| R5 | Assessor test runs ([when](../../../docs/testing/voice-tests.md#automated-voice-tests)) | Partner | Newo set Assessor up for this account; otherwise leave out | | | Partner | 10 | |
| R6 | Test agent or test account on the Newo platform | Partner / Newo | Always | | | Partner | 7 | |
| R7 | API credentials or MCP access: [system] | Vendor / customer IT | Per system in scope | | | Customer | 8 | |
| R8 | Test or sandbox account: [system] | Vendor | Per system the agent writes to | | | Customer | 8 | |
| R9 | BAA signed | Customer / legal | Health data | | | Customer | 8 | |
| R10 | Google Business Profile access, booking widget live without a payment step | Customer | Restaurant, stage 3 | | | Customer | 8 | |
| R11 | Forwarding or PBX change scheduled | Customer / carrier | Keeping the business number | | | Customer | 13 | |
| R12 | Knowledge content: price list, menu, FAQ, scripts | Customer | Always | | | Customer | 7 | |
| R13 | Transfer numbers and report inboxes confirmed | Customer | Always | | | Customer | 7 | |

## Milestones

| # | Stage | Milestone | Owner | Depends on | Gate | Target | Status |
|---|---|---|---|---|---|---|---|
| 1 | 01-discover | Discovery call held; notes saved | Partner | | | | |
| 2 | 01-discover | Requirements confirmed by the customer | Customer | 1 | | | |
| 3 | 01-discover | Acceptance criteria agreed; every criterion has a check | Both | 2 | | | |
| 4 | 01-discover | Feasibility checked; Newo support requests R1 to R5 sent | Partner | 3 | | | |
| 5 | 01-discover | SOW signed; plan and test approach in place | Both | 4 | G2 | | |
| 6 | 01-discover | Customer inputs R7 to R13 requested | Partner | 5 | | | |
| 7 | 02-build | Agent configured; health check passes | Partner | 6, R1, R6, R12, R13 | | | |
| 8 | 02-build | Integrations connected to test accounts | Partner | 6, R7 to R10 | | | |
| 9 | 02-build | Smoke test passes on every channel | Partner | 7, 8, R3, R4 | G3 | | |
| 10 | 03-test | Scripted tests run (critical ones three times); report says ready | Partner | 9 | | | |
| 11 | 04-launch | UAT round 1 | Customer or Partner | 10 | | | |
| 12 | 04-launch | Fixes; UAT round 2 on failed criteria plus passed criteria affected by the fixes | Both | 11 | | | |
| 13 | 04-launch | Night launch, in the agreed phone-change window | Both | 12, R2, R11 | | | |
| 14 | 04-launch | Review of the first 2 to 3 nights | Partner | 13 | | | |
| 15 | 04-launch | Day mode; customer's approval recorded | Both | 14 | | | |
| 16 | 05-operate | Monitoring period ends; weekly review cadence set | Partner | 15 | | | |

## At risk

Milestones waiting on a request with no ETA, or an ETA later than the milestone's start.

| Milestone | Waiting on | Why at risk | Action |
|---|---|---|---|
| | | | |
