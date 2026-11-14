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

## 4. The same loop through the Knowledge Studio MCP server

A coding assistant connected to `https://app.knowledge.newo.ai/mcp`
([02-access-and-tools.md, C](../02-access-and-tools.md#c-newo-knowledge-studio)) can do steps 1 to
3 itself. Tool names as of November 2026:

| Step | Tools |
|---|---|
| Check access and the workspace | `whoami`, `get_workspace_status`, `list_versions` |
| Find the agent's search request | `list_search_requests` (by time), then `get_search_request` (question, returned articles and positions) |
| See why the ranking came out this way | `explain_search` (every candidate, score, why it was dropped) |
| Try the question yourself | `search`; look up articles with `find_articles`, `get_article` |
| See what callers ask that the knowledge does not cover | `list_gaps` |
| Fix in a copy | `make_copy`, then `edit_article`, `add_asked_as` (caller wording), `exclude_source` |
| Rebuild and test the copy | `start_rebuild`, `get_job`; `run_autotest`, `get_autotest_report`, `compare_versions` |
| Try the copy without touching production | `publish_test` (a separate test endpoint) |
| Go live or go back | `publish_version`, `rollback`: these only **request** the switch; the owner approves it in Studio |

Rules:
- Ask the person before every change, as everywhere in this kit.
- Some read-only search and explain calls use paid tokens: read-only does not mean free.
- Never show the search token, and never copy callers' personal data from search requests into
  tickets, issues or learnings.

## 5. The agent side: did the question reach the search service?

When Studio has **no** search request for that conversation turn, the problem is on the agent
side:

1. `project_attributes_setting_knowledge_source` is `akb_studio` (or `external`): read it.
2. `project_attributes_setting_akb_studio_search` (or `project_attributes_setting_external_kb`)
   is set. Say "set" or "empty"; never show its value.
3. The account has the `http` integration with the `http_connector` connector
   (`GET /api/v1/integrations`, see [reference/api.md](../../reference/api.md#integrations-and-connectors)).
4. Read that session's logs ([reference/api.md, Logs](../../reference/api.md#logs)). Check:
   - Did the agent look something up at all on that turn?
   - Was the answer empty? An empty answer can mean an HTTP error, such as 401 after the token
     was revoked.
5. If the token was revoked or the index moved, publish again from Studio. Do not edit the setting
   by hand.

Studio itself does not work (building, testing, publishing, connecting): see
[studio-troubleshooting.md](studio-troubleshooting.md).
