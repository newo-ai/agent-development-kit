# Knowledge

## Where knowledge goes

1. **Settings first.** Business details, hours, products and services with prices, FAQ and
   policies are settings. For a standard setup they are enough.
2. **Knowledge base (AKB)** when knowledge does not fit the settings: long price lists, policies,
   manuals. The AKB belongs to the `GeneralManagerAgent` persona of `naf`. API:
   [API reference, AKB](../reference/api.md#akb). For simple additions,
   `project_attributes_rag_knowledge_base_append_text` is easier.
3. **Newo Knowledge Studio** when the knowledge base would grow beyond about 100 to 200 articles,
   or comes from many documents, websites, call-center scripts or call transcripts. Studio builds
   the knowledge base itself, finds duplicates, contradictions and gaps, and serves it as a
   search service.

Restaurants rarely need more than settings. The menu stays in
`project_attributes_restaurant_menu`, up to about 30,000 characters.

## Knowledge Studio with a Newo agent

1. The owner signs in at https://app.knowledge.newo.ai with Google.
2. They connect the agent: https://app.knowledge.newo.ai/connect-newo-agent (`?idn=` prefills it).
3. In Studio:
   1. add sources (website, files, transcripts);
   2. build;
   3. review what Studio flags;
   4. publish.
4. When the agent uses Studio, `project_attributes_setting_knowledge_source` is `akb_studio`. From
   then on, knowledge is managed in Studio: changes to the AKB or to the knowledge-base text
   settings no longer reach the agent.

## Search services

An agent can answer knowledge questions from its own knowledge base (AKB) or from an external
search service. The setting `project_attributes_setting_knowledge_source` chooses which.

| Value | Where the answers come from |
|---|---|
| `akb` or empty (default) | the agent's own settings and AKB |
| `akb_studio` | the Newo Knowledge Studio search index. Studio writes this value when it publishes. Changes to the AKB or to the knowledge-base text settings no longer reach the agent. |
| `external` **(rolling out)** | another search service, configured in `project_attributes_setting_external_kb`; the AKB is not read |
| `akb_external_shadow` **(rolling out)** | the AKB answers; every question is also sent to the external service and only logged, to compare both |

If the setting is missing on an account, its NAF release has no search services yet: it uses the
AKB.

**How a lookup reaches Knowledge Studio**
- `project_attributes_setting_akb_studio_search` holds the index address, the access token and the
  tool name (`akb_studio_search`). Studio writes it when it publishes.
- **It is a secret:** never display its value, say "set" or "empty". Never edit it by hand.
  Publish again from Studio, or use Studio's **Disconnect search** action, which restores the
  previous knowledge source.
- For each lookup, the agent sends one question to that address as a Vapi-style `toolCalls`
  request, with `Authorization: Bearer <token>`, through the account's `http` integration
  (`http_connector`). Studio answers with up to three whole articles. That text is what the agent
  reads before it answers.
- **The account must have the `http` integration with the `http_connector` connector.** Without
  it, or with an empty or broken setting, every lookup is answered as empty. The same happens on
  an HTTP error (for example 401 after a token was revoked) or an empty answer. The agent then
  says it cannot confirm the detail.

**Other search services (rolling out)**
- `project_attributes_setting_external_kb` describes any search service with the same request
  shape, as JSON:
  - `service`: a short name, shown in logs;
  - `url`;
  - `token`, optional; a secret;
  - `tool_name`, default `search_knowledge`;
  - `arguments`: fixed values the service expects;
  - `call_id`: `session` (default), or `persona:<field>` to send a caller field such as a
    telephony call id.
- Logs of these lookups are tagged `[EXTERNAL_KB:<service>]`.
- Fill it only with a working endpoint, then set the knowledge source to `external`. Try
  `akb_external_shadow` first to compare answers without callers hearing them.

**Studio's search endpoint for other platforms.** Studio gives every published index a search
address for other voice and chat platforms too. The **Connect** screen shows the snippet for each
platform. Through the Studio MCP server, use `get_connection_snippet`.

## Debugging a wrong or missing answer

See [debugging/search-debug.md](debugging/search-debug.md):
1. Find the search request of that conversation turn.
2. See which articles were returned and at what position.
3. Decide what to fix:
   - add or fix the article;
   - add the caller's wording to it (Studio "Asked as");
   - exclude a misleading source.

## Personal data

- Do not upload documents with callers' or patients' personal data into a knowledge base. It is
  searched and read aloud to anyone who calls.
- Internal staff instructions (internal codes, escalation routes) do not belong in customer-facing
  answers either. Keep them out, or let Studio separate them.
