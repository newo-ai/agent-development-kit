# Knowledge Studio: when something does not work

For AI coding assistants helping a partner or owner with Newo Knowledge Studio
(https://app.knowledge.newo.ai). Match the **symptom** first, then tell the person the
**fix** in plain words. Never ask anyone to paste an API key into a chat: they type it into
Studio themselves.

Since 12 Nov 2026 Studio itself explains most problems: a card in the bottom-right corner
says what happened in plain words and offers the next step (for example **Open Newo
connection**). The **Problems** button at the top lists all open cards. Start from that card.

If nothing below matches: in Studio, click **Submit bug report** (top right), add one sentence
of what happened, and tell the person a Newo engineer will look at it. Note the time.

## Building, publishing, versions

| Symptom (what the person sees) | Likely cause | What to do |
|---|---|---|
| "Reconnect Newo with a valid API key before changing the Newo search index", or MCP `start_rebuild` / publish fails with `organization_newo_reconnect` (older builds: `internal`) | The organization's saved Newo connection expired (before 12 Nov 2026 Studio kept it only 7 days; now 180 days) | Owner opens **Settings → Newo connection** (`/settings/newo`) and enters the Newo API key again, once. Then retry the build or publish. |
| Reconnect itself fails | Wrong key, or a different Newo account (customer IDN) than the one connected | Check the key belongs to the same Newo account (same customer IDN). If it still fails, send a bug report with the time. |
| "Build this version" on Testing seems to hang | It opens Indexing; a large workspace can take 30–60 s to open, a build several minutes | Wait for Indexing to show all phases done, then go back to Testing. Do not click Build repeatedly. |
| A version action fails with "busy" / "another job is running" | Indexing, testing or a backup is running for this workspace | Wait until it finishes; nothing is lost. |

## Indexing

| Symptom | Likely cause | What to do |
|---|---|---|
| **Caller questions** phase failed, reason mentions personal details | A caller question contains a caller's name/number (privacy check) | Fixed on 12 Nov 2026: such questions are now skipped and marked "Not checked: personal details". Click **Retry this phase**. Review and Publish work even while this phase shows failed. |
| A single phase failed, the others are done | One step stopped; completed work is kept | Click **Retry this phase** on that phase only. Do not restart all of Indexing. |
| Indexing stopped in the middle, or a card says the step "could not finish" right after a Studio update | A Studio update restarted the server and cut off the running job; completed work is kept | Open **Indexing** and press **Run indexing** (or **Resume**) again. |
| **Calendar** phase failed and "See how to fix" does not help | Known issue under investigation (12 Nov 2026); the reason is not yet shown | The other phases are fine: press **Continue to Review**. Send a bug report so Newo can see the case. |
| Topic map empty or "Topics are out of date" | Articles changed after topics were built | Indexing → Topics → **Run this phase again**. |

## Testing (autotest)

| Symptom | Likely cause | What to do |
|---|---|---|
| "Partial set 85 of 100 … not kept" | Some generated questions could not be verified against the articles; the rest are fine | Run the kept questions. 70 % or more kept is a usable set. |
| Run leaves all cases "Not run" on a partial set | Bug fixed on 12 Nov 2026 | Reload Studio and press **Run** again. If it persists, use **Create** for a new test suite (it runs automatically). |
| Generation "failed" several times with a growing count (74 → 84 → 89) | Older builds labelled a short set as failed | Fixed: a set with 70 %+ verified questions is ready. Press **Run**. |
| Test suite runs but accuracy is low on a few questions | Missing article, or callers phrase it differently | Open the case → **Add as Asked-as** (caller wording) or edit the article. |

## Adding knowledge

| Symptom | Likely cause | What to do |
|---|---|---|
| "This question contains known personal details. Generalise it first." when adding Asked-as | Older build refused it | Fixed: matching words are replaced with `[personal detail]` and the question is saved. |
| Call recordings (audio) are not accepted | Studio reads text transcripts, not audio (audio upload with automatic transcription is in development) | Transcribe first (speaker roles: operator / caller), then upload the transcripts. |

## Connecting an agent

| Symptom | Likely cause | What to do |
|---|---|---|
| A newly created agent cannot be connected right after creation | The agent is still being installed in Newo (1–3 min) | Wait a minute, press **Connect** again. Nothing is lost; do not create a second agent. |
| ChatGPT plugin says the organization "is not on its list" | Plugin access for that organization expired (fixed on 12 Nov 2026 for agents created through the plugin) | Try again. If it still fails, ask Newo support to restore plugin access (no new agent needed). |
