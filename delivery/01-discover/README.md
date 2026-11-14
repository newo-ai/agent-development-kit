# 01-discover: agree on what the agent must do

**Goal:** the customer and the partner agree on the agent's job, in statements that can be tested.
Everything later (build, test, acceptance, go-live) is measured against them.

**Done when:**
- `requirements.md` is filled in and the customer confirmed it;
- `acceptance-criteria.yaml` lists every required behavior, each with a priority;
- the customer agreed on scope and on how they will accept the agent (in a statement of work, or
  in writing).

## Steps

1. **Collect what already exists.** The business's website, price list, opening hours, call
   scripts, and the systems they use. If the agent was created from the website, read its current
   settings first: much of this is already filled in.
2. **Fill in the requirements** with the person: [templates/requirements.md](templates/requirements.md).
   - Read the industry page first ([industries/](../../industries/README.md)): it lists what
     matters for that kind of business.
   - For every system the agent must use, ask the four questions in
     [integrations, "Ask first"](../../docs/integrations/README.md#ask-first). A missing test
     account is a risk: write it down.
   - If the business handles health data, read
     [the health data rules](../../docs/integrations/README.md#health-data) before you go on.
3. **Write the acceptance criteria:** [templates/acceptance-criteria.yaml](templates/acceptance-criteria.yaml).
   - One criterion = one behavior a caller can observe: "books an appointment during working
     hours", "after hours, says the business is closed and takes a message", "never gives prices
     for implants; offers a consultation".
   - Include what the agent must **not** do, and what must go to a person.
   - Give each a priority. `critical` means the agent cannot go live without it.
   - Keep the list short. 10 to 25 criteria cover most agents.
4. **Check that every criterion can be tested.** For each one, note how: a scripted chat test, a
   phone call, or a check in the other system. If you cannot say how to test it, rewrite it.
5. **Check that the platform can do it.** For each criterion, find the lowest step of the ladder
   that delivers it ([docs/03-configure-and-customize.md](../../docs/03-configure-and-customize.md)).
   Tell the person early about anything that needs a scenario change, an integration with code,
   or something only Newo can do (a phone number in a certain country, SIP allowlisting:
   [support](../../docs/support/README.md#operations-request)).
6. **Get the customer's agreement** on the requirements, the criteria and the scope.

## Statement of work

If the partner signs a statement of work with the customer, these sections keep it tied to the
files above:

- scope and use cases (from `requirements.md`);
- what is out of scope;
- systems to connect, and who provides access and test accounts;
- acceptance criteria (the list from `acceptance-criteria.yaml`);
- how acceptance testing runs: who tests, how many rounds, what counts as passed;
- timeline, and who is responsible for what.

## Do not

- Do not put callers' personal data, API keys or passwords into these files.
- Do not promise a behavior before step 5.
