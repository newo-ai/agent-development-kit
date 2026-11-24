# SOP: edit a scenario

A scenario is what the agent does for one kind of request: booking, an order, a complaint. You
edit scenarios by hand in the Newo **Workflow Builder**. Your assistant cannot do it for you. It
tells you what to change, and it tests the result. Background: [docs/05](../05-scenarios.md).

Steps marked **(to confirm)** have not been checked click by click yet. If the screen looks
different, tell your assistant what you see.

## Before you start

- Ask your assistant whether a setting does it. Most "the agent should..." requests are
  settings, and the assistant can change those itself.
- A card you edit no longer receives Newo's library updates. Your assistant tells you this
  before you change it.
- If the agent already takes real calls, agree a time with your assistant: the change reaches
  every caller after the publish.

## Steps

1. **Get the change in writing.** Your assistant writes the exact text: which scenario card,
   the old text and the new text. Keep it open next to the Builder.
2. **Open the Workflow Builder.** Sign in at https://app.newo.ai, choose the account, open
   **Builder**, then **Workflow Builder** **(to confirm)**. Check that the portal shows the same
   business your assistant named.
3. **Find the card** for the request type the assistant named **(to confirm)**.
4. **Edit and save.** Change only what the assistant wrote. Paste plain text: copy it from a plain
   text file, not from a chat window, so no formatting comes along. Save the card.
5. **Publish.** First your assistant saves the agent's settings and asks for your "yes". Then
   publish the `naf` project **(to confirm: where the button is)**.
6. **Wait 2 to 5 minutes**, then tell your assistant "I changed the scenario".

## If it goes wrong

- **You can't find the card:** tell your assistant what you see.
- **No permission:** ask the account owner, or have your assistant draft a request to Newo.
- **The test fails:** your assistant suggests new text. Or put the old text back and publish
  again.
- **The same failure three times:** stop. Your assistant drafts a request to Newo.

## Next

Your assistant tests the change in a new conversation and reads what the agent received. If it
did not take effect, it tells you what to check.

Stuck? Tell your assistant "I'm stuck".
