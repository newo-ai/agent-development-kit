# SOP: edit a scenario

A scenario is what the agent does for one kind of request: booking, an order, a complaint. You
edit scenarios by hand in the Newo **Workflow Builder**. Your assistant cannot do it for you. It
tells you what to change, and it tests the result. Background: [docs/05](../05-scenarios.md).

Before you start, ask your assistant whether a setting does it. Most "the agent should..."
requests are settings, and the assistant can change those itself.

Steps marked **(to confirm)** have not been checked click by click yet. If the screen looks
different, tell your assistant what you see.

## Steps

1. **Get the change in writing.** Your assistant writes the exact text: which scenario card,
   the old text and the new text. Keep it open next to the Builder.
2. **Open the Workflow Builder.** Sign in at https://app.newo.ai, choose the account, open
   **Builder**, then **Workflow Builder** **(to confirm)**.
3. **Find the card** for the request type the assistant named **(to confirm)**.
4. **Edit and save.** Change only what the assistant wrote. Paste plain text: copy it from a plain
   text file, not from a chat window, so no formatting comes along. Save the card.
5. **Publish** the `naf` project **(to confirm: where the button is)**.
6. **Wait 2 to 5 minutes**, then tell your assistant "I changed the scenario".

Cards you edit yourself are kept when Newo updates the library. Cards you did not touch are
updated by Newo.

## Next

Your assistant tests the change in a new conversation and reads what the agent received. If it
did not take effect, it tells you what to check.
