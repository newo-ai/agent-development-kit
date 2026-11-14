# Playbook: get a phone number

Every agent gets a phone number when it is created, in a country close to the business. Use this
playbook when the owner needs a number in another country or of another type (mobile, local,
national, toll-free), or a second number.

## 1. What the owner needs

Ask:
- country, and type of number: local (city code), national, mobile or toll-free;
- for local numbers, which city or area code;
- calls only, or also text messages (not every number type supports SMS);
- is it for a demo or trial, or for real customers.

## 2. What Newo can give

- **Immediately (no documents):** the United States, Canada, the United Kingdom, the Netherlands
  and Australia. In some other countries Newo has numbers that can be used for demos and trials;
  ask Newo support.
- **With the business's documents (regulated countries):** most of Europe and many other
  countries require proof of the business and an address before a number can be activated. The
  phone provider reviews the documents; this takes from a few days to a few weeks.
- **Through a local carrier:** in some countries (for example in Central Asia and the Caucasus)
  numbers come from a local operator and are connected over SIP; delivery can take weeks.
- **The owner's own number:** forwarding or SIP from their existing line usually needs no new
  number at all (see [Connect the business phone line](connect-phone-line.md)).

Typical documents for a business number in a regulated country (the exact list depends on the
country and the number type):
- legal business name, registration number, website;
- business address; for **local** numbers, often an address **inside the number's area code**
  (no PO boxes);
- name and email of an authorised representative;
- registration documents (for example, in Germany, a commercial register extract
  "Handelsregisterauszug" or a trade licence "Gewerbeanmeldung");
- sometimes a signed letter of intent or authorisation and a recent utility bill.

Example, Germany: mobile numbers (+49 15x/16x/17x) and local numbers both need business
documents; a local number also needs an address in its area code
([Twilio's German requirements](https://www.twilio.com/en-us/guidelines/de/regulatory)).

## 3. How to request it

1. Collect the answers from step 1.
2. **Do not collect identity or company documents in the chat.** Tell the owner that Newo
   support will send them a secure way to submit documents.
3. Ask the owner to contact Newo support (or their Newo partner) with: account `idn`, country,
   number type, area code, calls/SMS, demo or production.
4. When the number is assigned, test it: a call to the number reaches the agent
   ([API reference](../reference/api.md#conversations)).

Numbers cost money every month. Before asking for an extra number, make sure the owner agrees,
and ask whether an unused number should be released.
