---
name: adjust-scenarios
description: Change how the agent runs a conversation (intent types, scenarios, procedures in the Workflow Builder) for the acceptance criteria that settings, knowledge and tools did not cover, one small tested change at a time. Use from build-agent when a criterion needs a scenario change, or when a partner asks "the agent should ask X before booking", "add a reschedule flow", "triage urgent calls first".
---

# Change scenarios

Stage: [02-build](../../delivery/02-build/README.md), step 7; also for fixes after launch. A
scenario change alters every conversation the agent has, and Newo updates no longer reach a card
you edited. It is the last step of the ladder before a separate project, so it is used only for
what nothing lower could do.

**You cannot change scenarios through the API or the CLI.** Cards are edited in the Workflow
Builder (or Vibe mode) in the Newo portal; the canvas attributes are rebuilt by the platform and
are never written directly ([docs/05](../../docs/05-scenarios.md)). You find what to change and
write the exact text; the partner makes the change in the portal; you check it.

Talk about what the caller will experience: "Before booking, the agent will ask whether it is an
emergency", not "I'll add an intent type". Name a card only when the partner asks or has to find
it in the portal.

## Before you start

1. **Only what is left.** Take the criteria that the plan in `build-notes.md` marks for a scenario
   change. For each, say in one line why a setting, knowledge or a tool cannot do it
   ([level A or B](../../docs/07-health-check.md#0-two-levels-of-customization)). A mixed request
   gets its settings first (where to transfer, what to send), and the card only if the trigger
   also has to change. If nothing is left, stop: no scenario change is needed. After launch, with
   no build notes, the partner's request is the criterion.
2. **The same account everywhere.** Check the account you read (`newo profile` in the agent's
   folder, or `GET /api/v1/customer/profile`) as in
   [setup check, check 3](../../docs/setup-check.md#3-the-right-account), and say its name back. The
   partner edits and publishes in a separate portal session: before each edit and each publish,
   ask them to confirm the portal shows that same account.
3. **Read the canvas** and keep a dated copy: read (never write)
   `project_attributes_private_dynamic_workflow_builder_canvas` and `project_attributes_scenario`.
   If the copy does not show which cards are library and which are custom, ask the partner to look
   in the Workflow Builder. The copy is how a card's old text is typed back; nothing restores it
   through the API.
4. **Real callers and test data.** After the publish the change reaches every conversation. On an
   account that already takes real calls or chats, agree the time with the partner (rules 8 and 10
   in [AGENTS.md](../../AGENTS.md)). For a criterion that books or sends something, follow the
   test-data rule in [build-agent](../build-agent/SKILL.md#3-build-one-change-at-a-time).

## 1. Prove it, then write the smallest change

For one criterion at a time:

1. **Proof first.** Check the criterion where it happens: a new sandbox conversation for chat
   behavior ([text tests](../../docs/testing/text-tests.md)); a test call by the partner for
   phone behavior such as transfers or interruptions, which the sandbox cannot show
   ([voice tests](../../docs/testing/voice-tests.md)); and the other system for a booking or a
   message. If the agent already does it, no change. If not, keep the `session_id` and find in
   its logs where the conversation went wrong (`newo logs --session-id <id>`). Use the same
   check after the change.
2. **Smallest change.** Change the card that already handles this, before you add a new one.
   Never build a second structure next to the existing one, and never put behavior into a field
   meant for facts. One card per change.
3. **Short text.** A few plain sentences: when, and what the agent does. Long instructions make
   the agent unstable. A partner's wording is a symptom, not the text to paste.
4. **Show the partner:** what callers will notice, which card changes, its old and new text, and
   that this card will no longer receive Newo library updates. Wait for "yes".

## 2. The partner makes the change

Tell the partner where to go in the Workflow Builder and give the new text ready to paste. The
change works only after the `naf` project is published, and a publish is its own change with its
own "yes". The partner publishes in the portal. Before it, save the project's attributes
([publish, safe order](../../reference/api.md#publish)); after it, compare. The canvas and its
compiled `…_dynamic_…`, `…_ami_*`, `…_itm_*` attributes are expected to differ: never restore
them. Restore only other values the publish lost, after a "yes". Wait 2 to 5 minutes.

If no card can reach the goal, stop and tell the partner. Framework (NAF) code is only for the
exceptional case in [docs/04](../../docs/04-naf-change-policy.md).

## 3. Check it

1. **Read it back:** the canvas shows the card changed and marked custom.
2. **Test it** with the same check as in the proof, in a new conversation. Judge by what happened.
   Its logs may also show the new text in the instructions the agent ran with
   ([docs/05](../../docs/05-scenarios.md#how-to-change-a-scenario)); logs can arrive a minute late,
   and missing text alone is not a fail.
3. **Check what it can touch:** repeat the smoke test for every critical criterion that goes
   through the same or a neighboring intent, and every transfer if the card routes calls. During
   the build the full rerun of scripted tests comes in [03-test](../../delivery/03-test/README.md);
   after launch, if the agent has scripted tests, rerun them all
   ([run-tests](../run-tests/SKILL.md)) before you call the fix done.
4. **On a fail,** find the cause in the logs and change the text, or ask the partner to put the old
   text back. Putting it back is a change too: it works only after a publish (step 2), then check
   that the old behavior is back. The card may stay custom even then; only Newo support can say
   whether it can follow library updates again. Two failures the same way: stop, show the
   partner and follow [get-unstuck](../get-unstuck/SKILL.md).
5. **Write it down** in `build-notes.md`: the criterion, the card, the new text, the test
   `session_id`s, and "custom card: no library updates".

Then the next criterion, from step 1.

## Next

Back to [build-agent, step 4](../build-agent/SKILL.md#4-health-check): the health check also
catches broken routing (an intent type that points to a scenario that does not exist).
