# reference/ — exact API and attribute formats

Earned its own file: score 10 (28 files, 77% of the repository's bytes, 100 inbound links).
Guides and procedures live in ../docs/ and ../playbooks/; this tree is the source of exact
formats.

## WHERE TO LOOK

| Need | Go to |
|---|---|
| Current API (Flow Designer V2) | [api.md](api.md) |
| Accounts without the V2 flag (archived V1) | [api-v1.md](api-v1.md) |
| What an attribute means, its tier and type | [attributes/index.md](attributes/index.md) → group page |
| Industry-specific settings | attributes/industries/ (9 pages: beauty, catering, cleaning, dental, general, home_service, hospitality, restaurant, sales) |
| CLI equivalents (`newo pull`, `newo push`) | [api.md](api.md), "Change a skill" (CLI 4.6.0+ for V2) |

## CONVENTIONS

- Decide the designer version first: `GET /api/v1/customer/settings/name/projects_v2_enabled`.
  On a V2 account, never change skills or publish through the old V1 requests ([api.md](api.md)).
- The attribute catalog lists IDN, title, setup tier (A basic, B common, C advanced), level and
  value type, then links to a group page for details; groups 1–6 also have `-advanced` variants.
- Attribute values are always strings; send the whole attribute, not only the value.
- The live account wins: when it differs from this documentation, trust the live value
  ([README.md](README.md)).
- Other pages depend on anchors into api.md (`#which-designer`, `#attributes`, `#publish`,
  `#akb`, `#conversations`, `#integrations-and-connectors`, `#logs`, `#sandbox`) and
  api-v1.md (`#publish`) — do not rename those headings.

## ANTI-PATTERNS

- Never `DELETE`; ask the owner before every change (api.md, api-v1.md).
- Read-only settings: do not change them. Secret values: never display them.
- [attributes/8-system.md](attributes/8-system.md) attributes are platform-managed — "do not
  edit this attribute manually" applies throughout that file.
- The project attribute in [attributes/1-business.md](attributes/1-business.md) must not change
  after the agent is created.
- Deprecated: language requirements must not be encoded in style fields
  ([attributes/2-agent.md](attributes/2-agent.md), "Deprecated Guidance"); the embedded schema
  in [attributes/4-agent-behavior-advanced.md](attributes/4-agent-behavior-advanced.md) is
  deprecated — use `resource`.

## HOTSPOTS (search inside, do not read whole files)

- attributes/4-agent-behavior-advanced.md — 5,200+ lines
- attributes/8-system.md — 1,400+; 2-agent.md — 1,300+; 1-business.md — 1,100+;
  attributes/index.md — 320+
