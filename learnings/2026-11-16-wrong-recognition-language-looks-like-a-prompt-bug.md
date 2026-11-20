---
title: A German voice agent "inventing" names and dates was the recognizer set to auto, not the prompt
date: 2026-11-16
tags: [industry/general, topic/debugging, topic/configuration, topic/telephony]
status: solved
verified: read the account's settings and both voice connectors, read two real call transcripts, searched the analytics logs for the instruction actually sent to the model (requests below, no keys)
---

## Situation

A hearing-care business in Germany. Voice agent on the phone, German as the primary language,
voice-to-voice with Gemini 2.5 native audio and `v2v_mode_user_stt` = `elevenlabs` (the NAF
default for that model). The partner's non-technical team was configuring it from a browser chat
with the older Newo plugin.

They reported, after a test call:

- the agent asked for the caller's name **in English** in the middle of a German call;
- it "invented" things: it addressed a woman as "Herr";
- it got confused when the caller asked a hypothetical question about a different kind of health
  insurance than her own;
- the email report arrived, but without several details the caller had given.

Their assistant diagnosed the call, proposed six extra behaviour rules for the speaking style, and
said correctly that the English question looked like it came from the platform's own procedure
text rather than from any setting. The team applied the rules, called again, and reported that
some things were better and some were not. Then they were stuck.

## What we tried

**First, the wrong turn — worth writing down, because it is easy to repeat.** The speaking style
setting held the six new rules. The connector's `genai_v2v_initial_system_instruction` did not: a
character-by-character comparison showed the connector copy matching the setting exactly up to the
point where the new block began, then stopping. The obvious conclusion — "the change never reached
the agent, they need to publish" — is **wrong**, and we nearly shipped it as advice.

What settled it was the log:

```
GET /api/v1/analytics/logs?page=1&per=100&message=<a distinctive word from the new rules>
```

The new text appeared in `SendCommand(commandIdn=update_session, ... instructions=...)` from a
precise moment onward, and only in the later of the two calls. So:

- the change **was** live, with no publish; for voice-to-voice the prompt is rebuilt from current
  settings during the call;
- the connector setting is a snapshot written when NAF sets the account up, and it was days old;
- the earlier call, the one the team had analysed, ran *before* the rules existed. They were
  comparing a complaint from one call with a fix applied after it.

Publishing would also have been actively harmful here: Flow Designer V2, `naf` with
`is_auto_update_enabled: true` and a registry, so publishing a private copy would have taken the
account off Newo's releases.

**Then the real cause.** Reading the transcripts instead of the settings. Every caller turn of a
German call had been transcribed into Cyrillic — German words spelled out phonetically in
Ukrainian, for example `Монтах` for *Montag* and `Нааин` for *Nein*. Other turns of the same call
came back as Dutch and as English. The connectors had:

```
v2v_mode_user_stt           = elevenlabs
elevenlabs_stt_language_code = auto
```

Everything the team complained about followed from that one value:

| Complaint | Cause |
|---|---|
| wrong salutation, wrong name | the name reached the text side as phonetic noise |
| wrong weekday noted | the weekday reached the text side as phonetic noise |
| report missing details | same, plus the report's field list for that report type names only three fields |
| agent slipping out of German | the agent's secondary-language list included a language the garbled transcript looked like, and the instruction says to switch to a secondary language when the user uses it — so noise was triggering a legitimate rule |

The session metric `asrRecognition` read `100.0` on both calls.

The English question was real and separate: the platform's name-gathering procedure contains a
quoted English sentence as its output, which a tone rule in a speaking style does not reliably
override. That one is a platform fix, and the team's assistant had already identified it.

## Result

Recommended, in this order: set the recognition language explicitly on both voice connectors
instead of `auto`; trim the secondary-language list to languages the business actually serves; add
the missing fields to the report content; localise the remaining English default phrases. The
recognition language has to be first — until the transcript is right, nothing else can be measured.

## Advice for the next assistant

1. **Read the caller's lines in the transcript before you read any setting.** If they are not in
   the language the caller spoke, stop. Every "the agent invents things" symptom on that call is
   the transcript, and no prompt edit will touch it. The agent can still *speak* correctly while
   this happens, because in voice-to-voice the model hears the raw audio.
2. **"Stored" is not "live", and the connector snapshot is not proof of either.** Prove a change
   is live by finding its text in an `update_session` line in the logs, and take the timestamp.
   Conversations that started before it cannot tell you whether your fix worked.
3. **A recognizer has a language, and `auto` is not a safe default outside English.** Picking
   `elevenlabs` or `google` is half the setting; the language code is the other half.
4. When the owner says "we applied it and it is still broken", first check *which call* they
   judged. Here the answer was a call that pre-dated the fix.
