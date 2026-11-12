# Knowledge

## Where knowledge goes

1. **Settings first.** Business details, hours, products and services with prices, FAQ and
   policies are settings. For a standard setup they are enough.
2. **Knowledge base (AKB)** when knowledge does not fit the settings: long price lists, policies,
   manuals. The AKB belongs to the `GeneralManagerAgent` persona of `naf`. API:
   [API reference, AKB](https://knowledge.newo.ai/agent-setup#api-akb). For simple additions,
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
