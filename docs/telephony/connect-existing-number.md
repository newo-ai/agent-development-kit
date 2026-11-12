# Keep the business's number

## Step 0: find out what the number is

1. Ask the person for the number and which phone system they use: a mobile phone, a landline
   carrier, a business phone system (RingCentral, Nextiva, 8x8, Zoom Phone, Dialpad, Vonage,
   Genesys and others), their own PBX, or a SIP trunk provider.
2. If they do not know, look up the carrier. For example, Twilio Lookup
   (`GET https://lookups.twilio.com/v2/PhoneNumbers/{number}?Fields=line_type_intelligence`) returns
   the carrier name and the line type (mobile, landline, VoIP). This needs a Twilio account of the
   person or partner.
3. Choose:
   - **Mobile number** (Verizon, AT&T, T-Mobile and other mobile carriers): consumer mobile lines
     have **no SIP access**. Use [call forwarding](#a-call-forwarding).
   - **Business phone system / PBX / SIP trunk**: forwarding is simplest; SIP is possible when
     the provider gives SIP credentials.
   - **Landline**: forwarding, through the carrier's codes or account portal.

## A. Call forwarding

Decide **when** calls go to the agent:
- **No answer** (conditional forwarding): people answer first; after about 10 to 15 seconds
  (2 to 3 rings) the call goes to the agent. This is the usual start.
- **After hours**: a time rule in the phone system.
- **Always.**
- **Busy**: when the line is busy.

Where to set it:
- **GSM mobile networks** (most countries), dialed from the business phone:
  - no answer after N seconds: `**61*<agent number>**<seconds>#` (seconds: 5 to 30, in steps of 5);
  - cancel: `##61#`;
  - busy: `**67*<agent number>#`;
  - always: `**21*<agent number>#`.

  Carriers differ: check the carrier's help page.
- **US carriers:** Verizon uses `*72` / `*73` for unconditional forwarding; conditional forwarding
  is in the My Verizon app or portal. AT&T and T-Mobile have their own codes and app settings.
- **Business phone systems:** an answering rule or call-forwarding rule on the user, extension,
  ring group or main number in the admin portal.
  - Many systems have an API, and some an MCP server. With the person's admin access, you may set
    the rule yourself after they confirm the exact rule.
  - Otherwise give them click-by-click steps for their admin portal.
  - Newo does not need access to their phone system.
- The target is always the **AI phone number**: read it from
  `project_representative_agent_voice_phone_number` (or the plugin's `agent_status`). Do not ask
  the owner for it, and do not confuse it with the business number.
- Always use the AI phone number in international format (E.164, `+14155550123`).
- The staged rollout (nights, review, then the day) is in [go-live.md](go-live.md).

Test:
1. The person calls the business number from another phone and lets it ring.
2. A new conversation appears, and the agent answers.
3. Check the caller's number in that conversation. Some systems pass the business number instead
   of the caller's; then every caller looks like the same person. Tell the person and report it
   ([support](../support/README.md)).

Costs: forwarding to a number in another country is an international call billed by the
business's carrier. Prefer an agent number in the same country ([phone-numbers.md](phone-numbers.md)).

## B. SIP registration

Newo connects by **SIP registration** with a username and password (digest). **IP-only SIP
trunking (no credentials) is not supported.**

**1. Get from the phone system or SIP provider** (business SIP products give this in their
onboarding documents or admin portal):
- the SIP server host name and port;
- the SIP username and password of an account or extension for the agent;
- the transport: UDP or TCP. Say so if the provider requires TLS;
- the caller ID: the number that is routed to this SIP account;
- the provider's **IP addresses for SIP signaling and for RTP (audio)**.

**2. On the provider side:**
- route calls for the number (or a ring group, a queue, an after-hours rule) to that SIP account;
- allow it to transfer to extensions and, if needed, to dial out in E.164 format;
- allow Newo's IP addresses if the provider accepts only known IPs. Get Newo's addresses from Newo
  support.

**3. On Newo:** the voice connector `newo_voice_connector` gets:
- provider **Custom SIP**;
- in the SIP group: host:port, username, password, caller ID, transport.

**The password is typed by the person** in the Newo portal (Builder → Integrations), never in a
chat. Changing an existing connector through the API is not reliable today: an update can report
success without saving. Do it in the portal and read it back.

**4. Allowlisting.**
- If calls do not arrive or have no audio, Newo may need to allow the provider's SIP and RTP IP
  addresses.
- Open an **operations request** with the IP addresses:
  [support](../support/README.md#operations-request). Large public providers are often already
  allowed. If everything works, nothing needs to be done.

**5. Test:**
- an inbound call through the real route;
- an outbound call if the agent calls out;
- one transfer to a person.

If the agent receives nothing, the registration may have failed. The API does not show
registration status today: ask Newo support to check it.

## C. Moving the number to Newo (porting)

- Rare. Newo ports numbers only case by case, with a signed contract.
- It needs the carrier's documents for that country.

Prefer forwarding or SIP.
