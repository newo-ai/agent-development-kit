# Getting a phone number

Every agent gets a number when it is created, in a country close to the business. This page is
for a number in another country, of another type, or a second number.

## Ask the person first

- Country and type: local (city code), national, mobile or toll-free. For local numbers, the city
  or area code.
- Calls only, or also text messages. Not every number type supports SMS.
- Demo or trial, or real customers.
- Whether they would rather keep their own number. Forwarding or SIP needs no new number:
  [connect-existing-number.md](connect-existing-number.md).

## What Newo can provide (November 2026)

| Situation | What to expect |
|---|---|
| United States, Canada, United Kingdom, Netherlands, Australia | assigned automatically when the agent is created |
| Germany | mobile numbers (+49 15x/16x/17x) are available for demos and trials; SMS is not always available on them. Local (city) numbers need the business's documents (below) |
| Most of Europe and other regulated countries | the business's documents; the phone provider reviews them, from a few days to a few weeks |
| Some countries in Central Asia and the Caucasus | numbers from a local operator connected over SIP; delivery can take weeks; some local operators accept SIP only from inside the country |
| A country Newo cannot cover | keep the business's local number and connect it by [SIP](connect-existing-number.md#b-sip-registration) |

Known gap: when an agent is created for a European business, it may get a Netherlands number
instead of a local one. Ask Newo support for a local number if the business needs it.

## Documents for regulated countries

The exact list depends on the country and the number type. Typical:
- legal business name, registration number, website;
- business address. For **local** numbers this is often an address **inside the number's area
  code**; PO boxes are not accepted;
- name and email of an authorised representative;
- registration documents. In Germany, for example, a commercial register extract
  (Handelsregisterauszug) or a trade license (Gewerbeanmeldung);
- sometimes a signed letter of intent or authorisation, and a utility bill from the last three
  months.

Public example: [Twilio's requirements for Germany](https://www.twilio.com/en-us/guidelines/de/regulatory).

## How to request it

1. **Never collect identity or company documents in a chat**, an issue or this repository. They
   are personal data.
2. Open an **operations request** ([support](../support/README.md#operations-request)) with:
   - account `idn`, country, number type, area code;
   - calls only, or calls and SMS;
   - demo or production.

   Newo support answers with a secure way to submit the documents **(planned: an upload page you
   can send the person to directly)**.
3. When the number is assigned, test it: a call to the number reaches the agent.
4. Numbers cost money every month. Ask whether an unused number should be released.
