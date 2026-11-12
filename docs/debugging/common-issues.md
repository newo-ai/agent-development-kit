# Common issues

Known problems, collected from real cases. Add yours through [learnings](../../learnings/README.md).

| Issue | Likely cause | What to do |
|---|---|---|
| A change "did not work" | tested in the same conversation; or a publish-time setting without a publish | test in a **new** conversation; publish `naf` for hours, time zone, languages, voice and scenarios; wait 2–5 minutes |
| A setting reverted by itself | a Newo update or a V2 version activation replaced it; or a system-managed attribute was edited directly | save the attributes before a publish and compare after; never edit `..._dynamic_...` attributes |
| Code change disappeared | automatic updates replaced it | see [04-naf-change-policy.md](../04-naf-change-policy.md) |
| The browser plugin says the access or job id expired | access is tied to the chat where the agent was created; it lasts 180 days | continue in the **same** chat; a new chat does not know the job id |
| Every caller looks like the same person | the forwarding passes the business number instead of the caller's | check the caller number in the conversation; report it |
| Forwarded calls do not reach the agent | wrong forwarding code; "no answer" forwarding with too long a timer; the carrier blocks international forwarding | test with a call from another phone; check the carrier's documentation |
| SIP: no calls or no audio | registration failed; IP addresses not allowed; wrong transport | check the credentials and transport; open an operations request with the SIP and RTP IPs |
| Transfer does not happen | transfers off; the criteria do not match; the PBX does not allow REFER; billing not set up | read the transfer settings and the logs of that call |
| The agent switches to another language | the caller used another language; the language settings; a word in another language in the instructions | find the turn where it switched; check the language settings |
| SMS sent but not received | carrier filtering; registration rules (A2P 10DLC in the US) | check delivery at the SMS provider; check the registration |
| A booking was made twice | a retry, or a repeated "yes" | add a duplicate check or idempotency; confirm once |
| A European business got a Netherlands number | number assignment by region | ask for a local number ([phone-numbers.md](../telephony/phone-numbers.md)) |
