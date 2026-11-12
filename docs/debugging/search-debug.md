# Debugging knowledge answers

The agent answered wrongly, said "I don't know", or used the wrong document.

## 1. Where does the agent's knowledge come from?

Check `project_attributes_setting_knowledge_source` (present on agents that can use Knowledge
Studio; if it is missing, the agent uses its settings and AKB):
- **AKB / settings:** the answer comes from settings and the agent's knowledge base.
- **`akb_studio`:** the answer comes from **Newo Knowledge Studio**. Changes to the AKB do not
  matter; fix it in Studio.

## 2. Was the fact available?

- Find the fact in the settings, in the AKB (`GET /api/v1/akb/topics?...`), or in Studio's
  articles.
- If the fact is nowhere, it is a **knowledge gap**: add it.

## 3. Was it found? (Knowledge Studio)

Every search the agent makes is logged in Studio. To debug:
1. Find the search request of that conversation turn by its time, or by the request ID the agent
   logged.
2. See the question as the agent asked it, the articles returned and their **positions**.
3. Run the same question with an explanation of the ranking: every candidate, its score, why it
   was dropped.

Typical fixes:

| Finding | Fix |
|---|---|
| The right article is not in the top 3–5 | add the caller's wording to the article ("Asked as") |
| A misleading document outranks the right one | exclude that source in a new version |
| Two articles contradict each other | fix one; Studio's review flags contradictions |
| The article is right but the agent misread it | shorten or clarify the article |

4. Make the change in a **copy** of the knowledge version, test the same questions on that copy,
   then publish. A published version can be rolled back.

Through Knowledge Studio's MCP server, a coding assistant can do steps 1 to 4 itself. See
[02-access-and-tools.md](../02-access-and-tools.md#c-newo-knowledge-studio).
