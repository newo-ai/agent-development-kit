# Restaurants and catering

## Essentials

1. **Menu**, with prices: `project_attributes_restaurant_menu`. Up to about 30,000 characters,
   wine list included, it stays in this setting; no separate knowledge base is needed.
2. **Opening hours**, including kitchen hours, breaks and holidays, and the time zone.
3. **Reservations:** does the restaurant take them by phone, which system it uses, the maximum
   party size without a manager, the policies (deposits, cancellations, large groups).

Playbook: [restaurant setup](https://knowledge.newo.ai/agent-setup/industries/restaurant.md).

## Reservations

- Many restaurants use a reservation system: OpenTable, SevenRooms, Resy, Tableo and others.
  Check what the system offers:
  - a partner API;
  - an MCP server;
  - only a widget.
- The two-step pattern applies:
  1. check availability;
  2. tell the caller;
  3. book only after the caller confirms.

  See [integrations](../docs/integrations/README.md) and the free-tables example in
  [http-rest.md](../docs/integrations/http-rest.md#4-conversation-tools-any-http-api-during-the-call).
- **Availability that the API returns can differ from the widget**, for example for special areas
  or events. Compare both during testing, and report differences to the vendor.
- Large parties, events and special requests usually go to a person: set transfer criteria or a
  callback.

## Orders and catering

Take-out, delivery and catering requests are often handed to staff. Use reports (email or SMS
after each conversation) or the session-ended webhook. Do not promise prices or availability the
agent cannot check.

## Keep it simple

Restaurants rarely need Knowledge Studio, scenarios or code.
