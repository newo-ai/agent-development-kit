# Vendor integrations: index

Systems with a ready Newo integration, from the Newo help center (read 2026-11-25). Use the
[connect-integration](../../../skills/connect-integration/SKILL.md) skill: it reads the vendor
page, does the Newo side, and walks the partner through the vendor side.

A system that is not here has no ready integration: use the generic mechanisms in
[../README.md](../README.md#pick-the-mechanism) (webhooks, booking settings, conversation tools,
MCP).

How the columns read:
- **How it connects**: almost every row is a native Newo integration, added to the agent as a
  project from a Newo module, then settings and **Publish All**. The column names how the vendor
  is reached (API key, OAuth, a bridge).
- **Partner does**: in the vendor and, for keys and codes, in the Newo Builder.
- **Assistant does**: in Newo, through the MCP, after a "yes".
- **Newo only**: what neither the partner nor the assistant can do. "None stated" means the help
  article names nothing; it does not promise there is nothing.

The live setting names come from `get_integrations` at run time. Where this page and the platform
disagree, the platform wins.

## Calendars

| Vendor | How it connects | Partner does | Assistant does | Newo only | Page |
|---|---|---|---|---|---|
| Google Calendar | Native; Newo's own Google account, no customer sign-in (to confirm with the platform team) | Nothing in Google | Manager email, calendar setting, scenario | None stated | [google-calendar.md](google-calendar.md) |
| Cal.com | Native module, API key | Creates the API key and an event type; pastes the key | Project, event type, booking and calendar settings, intent, scenario | None stated | [cal-com.md](cal-com.md) |
| Calendly | Native module, OAuth app | Registers an OAuth app (Professional plan+), pastes ID, secret and code | Project, event type, booking and calendar settings, intent, scenario | None stated | [calendly.md](calendly.md) |

## CRM and field service

| Vendor | How it connects | Partner does | Assistant does | Newo only | Page |
|---|---|---|---|---|---|
| Housecall Pro | Native module, API key | Gets the API key (MAX plan); pastes it | Project, settings, intent, scenarios, booking schemas | None stated | [housecall-pro.md](housecall-pro.md) |
| ServiceM8 | Native module, API key | Creates the API key; pastes it | Project, default staff and category | None stated | [servicem8.md](servicem8.md) |
| Workiz | Native module, API key and secret | Copies key and secret; pastes them | Project, booking settings, intent, scenarios | None stated | [workiz.md](workiz.md) |
| GoHighLevel | Native module or Marketplace app; OAuth or private token | Installs the app, or creates a private integration; calendar, staff, pipeline | Project, calendar selection, pipeline rules, sync settings | None stated | [gohighlevel.md](gohighlevel.md) |
| Zoho CRM | Native, OAuth | Authorizes the Newo app, pastes the code | Region, booking and pipeline settings | None stated | [zoho-crm.md](zoho-crm.md) |
| Pipedrive | Native module, API key | Creates the API key; pastes it | Project | None stated | [pipedrive.md](pipedrive.md) |
| Yelp | Native module + Yelp connector | Finds the Yelp Business ID | Project, connector settings, run | None stated | [yelp.md](yelp.md) |
| Kommo | Native module, OAuth (private integration) | Creates the Kommo integration; pastes ID, secret, code | Project, subdomain, pipeline rules | None stated | [kommo.md](kommo.md) |
| Bitrix24 | Native, OAuth app | Creates the OAuth app; pastes ID, secret, code | Base URL, owner, deal and task settings | None stated | [bitrix24.md](bitrix24.md) |
| Odoo | Native module, API key | Creates an API user and key; pastes the key | Project, URL and user name | None stated | [odoo.md](odoo.md) |
| Altegio | Native module, partner and user tokens | Gets tokens from Altegio; pastes them | Project, location, feature switches | None stated | [altegio.md](altegio.md) |

## Practice and property management (PMS)

Health data: read [Health data](../README.md#health-data) before any of these.

| Vendor | How it connects | Partner does | Assistant does | Newo only | Page |
|---|---|---|---|---|---|
| Kolla (bridge) | Native module; Kolla connector on the practice's PC | Kolla invite link, connector install, API key; pastes it | Project, connector id, provider and operatory | None stated | [kolla.md](kolla.md) |
| Dentrix | Through Kolla (on-premises only) | As Kolla | As Kolla, `kolla_connector_id` = `dentrix` | None stated | [dentrix.md](dentrix.md) |
| OpenDental | Through Kolla (on-premises only) | As Kolla | As Kolla, `opendental` | None stated | [opendental.md](opendental.md) |
| Eaglesoft | Through Kolla (on-premises only) | As Kolla | As Kolla, `eaglesoft` | None stated | [eaglesoft.md](eaglesoft.md) |
| Dolphin | Through Kolla (on-premises only) | As Kolla | As Kolla, `dolphin` | None stated | [dolphin.md](dolphin.md) |
| Denticon | Native module, OAuth credentials + subscription key | Gets the credentials; pastes them | Project, office, scenarios, intents | None stated | [denticon.md](denticon.md) |
| Tab32 | Native, subscription key | Gets the key; pastes it | Slot and location settings | None stated | [tab32.md](tab32.md) |
| OpenEMR | Native, OAuth2 against the OpenEMR REST API | Registers an API client and API user; pastes them | URL, facility, provider, feature switches | None stated | [openemr.md](openemr.md) |
| Oracle Opera (hotels) | Native, OAuth2 client credentials | Gets Opera API credentials; pastes them | URL, hotel, feature switches | None stated | [opera.md](opera.md) |

## POS, ordering and reservations

| Vendor | How it connects | Partner does | Assistant does | Newo only | Page |
|---|---|---|---|---|---|
| Square | Native, OAuth; Square Appointments | Developer app, Appointments setup, pastes ID, token, code | Location, feature switches | None stated | [square.md](square.md) |
| Clover | Native module, OAuth (private app) | Creates a Clover app; pastes ID, secret, code | Project, intents, scenarios | None stated | [clover.md](clover.md) |
| SevenRooms | Native module, credentials from SevenRooms | Asks the SevenRooms rep for access; pastes credentials | Project, region URL, time zone, switches | None stated | [sevenrooms.md](sevenrooms.md) |
| Tableo | Native module, API token | Gets the token; pastes it | Project, switches, windows | None stated | [tableo.md](tableo.md) |
| Syrve | Native module, API key | Copies the API key; pastes it | Project, region URL | None stated | [syrve.md](syrve.md) |
| PosHUB | Native module, Marketplace app + webhooks | Pastes admin login; creates the app with Newo's webhook URLs | Project, location | None stated | [poshub.md](poshub.md) |
| Mozrest (bridge) | Native module, Mozrest connector | Confirms the restaurant is on Mozrest | Project, time zone, name, restaurant id | Connector credentials at platform level (to confirm) | [mozrest.md](mozrest.md) |
| Reservours | Through Mozrest | As Mozrest | As Mozrest | As Mozrest | [reservours.md](reservours.md) |

## Messaging and logistics

| Vendor | How it connects | Partner does | Assistant does | Newo only | Page |
|---|---|---|---|---|---|
| ManyChat (WhatsApp, Instagram, Facebook, TikTok, Telegram) | Native module, ManyChat template + API key | Installs templates (Pro plan+), sets default replies, pastes the key | Project, WhatsApp information and report settings | None stated | [manychat.md](manychat.md) |
| Telegram | Telegram connector, bot token | Creates a bot with BotFather; pastes the token | Checks the connector runs | None stated | [telegram.md](telegram.md) |
| TrackB (parcel tracking) | Native module; no customer key | Nothing | Project, publish, check the scenario | None stated | [trackb.md](trackb.md) |
