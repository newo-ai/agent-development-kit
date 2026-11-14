# Restaurant setup playbook

For an AI assistant setting up a Newo agent for a standard restaurant, café or bar. Read the main
guide first (`read_guide`, the guide itself); its rules always apply: ask the owner before every
change, keep old values, never delete, never ask for an API key. Talk to the owner in their
language, in short messages, about what the agent will know and do.

## The essential work (always, do it first)

A restaurant's callers ask about three things above all. Verify all three with the owner before
anything else, one at a time, and show what the agent will say:

1. **Menu: dishes and drinks (products and services).** Read what the agent has now and compare
   it with the owner's current menu (their website menu page, a PDF or a photo they send, or what
   they tell you). Fix missing dishes, removed dishes, wrong names and categories. Ask about
   dietary information they want the agent to give (vegetarian, vegan, gluten-free, allergens).
2. **Opening hours.** Every day of the week, with breaks, kitchen closing time if it differs, and
   holidays coming up. Check the time zone matches the address.
3. **Prices.** Current prices for the menu items, and whether the agent may say prices on the
   phone at all.

Only when these three are right, move on to reservations, takeaway and delivery, large groups and
events, and reports (see "Next, if the owner wants" below).

## Where the menu goes

- Keep the whole menu, including the wine list or bar card, in the restaurant menu setting
  `project_attributes_restaurant_menu` (and the signature dishes in
  `project_attributes_restaurant_signature_dishes`). The platform builds its own menu overview
  and lookup from it; do not edit `project_attributes_restaurant_menu_overview` by hand.
- Business details, hours and prices follow the main guide's
  "Finish the configuration" playbook ([playbooks/finish-configuration.md](../playbooks/finish-configuration.md)): `project_business_working_hours`,
  `project_business_time_zone`, `project_attributes_products_and_services`,
  `project_representative_agent_providing_prices_explicit_constraint`.
- **No separate knowledge base (AKB) while the whole menu text is at most about 30,000
  characters.** That covers almost every restaurant. Only when the menu with the wine list is
  larger (for example a very long wine list) add the extra part to the knowledge base, as the main
  guide's "Where the agent's knowledge goes" ([assistant guide](../docs/assistant-guide.md#where-the-agents-knowledge-goes), [06-knowledge.md](../docs/06-knowledge.md)) describes.
- Formats and every restaurant setting are in the attribute reference
  [`attributes/industries/restaurant.md`](../reference/attributes/industries/restaurant.md); open it when you need a setting's exact format.

## Keep it simple

A standard restaurant setup needs only the settings above. Do not bring up scenarios, Vibe mode,
the workflow builder, custom skills or code, and do not offer them. Mention them only if the owner
asks for something the standard setup cannot do (for example a custom ordering flow with an
outside system), and then explain in plain words what it would take.

## Next, if the owner wants

- **Reservations:** the booking link the restaurant already uses (for example OpenTable or Google
  Maps reservations) and the email for large-group requests.
- **Takeaway, delivery and catering orders:** the order email and what the agent should collect.
- **Events:** regular events and private dining.
- **Transfers and reports:** who gets calls the agent cannot handle, and the summary after each
  conversation.

Test with a few real questions ("Are you open on Monday?", "Do you have vegan dishes?", "How much
is the ...?") in a new conversation after every change.

## Reservations: systems and policies

- Ask whether the restaurant takes reservations by phone, which system it uses, the maximum party
  size without a manager, and the policies (deposits, cancellations, large groups).
- Many restaurants use a reservation system: OpenTable, SevenRooms, Resy, Tableo and others.
  Check what the system offers:
  - a partner API;
  - an MCP server;
  - only a widget.
- The two-step pattern applies:
  1. check availability;
  2. tell the caller;
  3. book only after the caller confirms.

  See [integrations](../docs/integrations/README.md),
  [Connect external systems](../playbooks/connect-external-systems.md) and the free-tables example in
  [http-rest.md](../docs/integrations/http-rest.md#4-conversation-tools-any-http-api-during-the-call).
- **Availability that the API returns can differ from the widget**, for example for special areas
  or events. Compare both during testing, and report differences to the vendor.
- Large parties, events and special requests usually go to a person: set transfer criteria or a
  callback.

## Orders and catering

Take-out, delivery and catering requests are often handed to staff. Use reports (email or SMS
after each conversation) or the session-ended webhook. Do not promise prices or availability the
agent cannot check. Catering businesses with their own agent use the general playbook
([general.md](general.md)) and the catering settings
([attributes/industries/catering.md](../reference/attributes/industries/catering.md)).
