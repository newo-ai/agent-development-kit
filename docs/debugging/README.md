# Debugging

## The method

1. **Get the facts of one conversation.** Collect:
   - when it happened (date and time with the time zone);
   - the channel (phone, chat, SMS);
   - the caller's number if the person has it;
   - what was expected and what happened.
2. **Find the conversation.** Use the transcripts and the session ID:
   [conversation-debug.md](conversation-debug.md).
3. **Read the logs of that session** to see what the agent did and why.
4. **Classify:**
   - a setting;
   - missing or wrong knowledge ([search-debug.md](search-debug.md));
   - an integration (a request failed or returned something unexpected);
   - the phone line;
   - a platform bug.
5. **Fix at the lowest level of the ladder** ([03-configure-and-customize.md](../03-configure-and-customize.md)).
   Test with the same question, and tell the person what changed.
6. **If it is a platform bug,** file it ([support](../support/README.md#bug-report)).

Pages:
- [conversation-debug.md](conversation-debug.md): transcripts, sessions, logs.
- [search-debug.md](search-debug.md): wrong or missing answers from the knowledge base.
- [common-issues.md](common-issues.md): known problems and what to do.
- [studio-troubleshooting.md](studio-troubleshooting.md): Newo Knowledge Studio problems (building, indexing, testing, connecting).

## Before you tell the person what went wrong

- Separate what you saw in the logs from what you think caused it.
- If you could not confirm the cause, say so, and say what would confirm it.
