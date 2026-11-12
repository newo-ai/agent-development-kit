# How the ecosystem works

Read this first if you want the big picture: why this repository exists, how your work feeds
back into the Newo platform, and why the platform gets better with every agent.

## 1. The problem: deployment, not the demo

A voice agent demo takes minutes. A real deployment touches everything around the agent:

```mermaid
flowchart LR
    A((The AI agent))
    A --- P[Phone system · SIP]
    A --- N[Local numbers, many countries]
    A --- C[CRM]
    A --- S[Scheduling · patient systems]
    A --- SC[Scenarios]
    A --- K[Knowledge base]
    A --- T[Testing]
    A --- W[Weeks of tuning on real calls]
```

Across the industry this work has been done by forward-deployed engineers and solution architects.
There are few of them, they are expensive, and each one takes months to train.

## 2. One framework, every agent

Every Newo agent runs on one shared framework (NAF) on one orchestration platform. When one agent
meets a corner case and Newo fixes it in the framework, the fix reaches every agent.

```mermaid
flowchart TB
    subgraph Agents
      D[Dental] & R[Restaurant] & I[Insurer] & U[University] & H[Home services] & CC[Call center]
    end
    Agents --> F[One shared framework · NAF]
    F --> PL[One orchestration platform · voice · chat · SMS · integrations]
    R -. corner case found .-> F
    F == fix released ==> Agents
```

That is accumulated process intelligence: corner cases from many industries and many calls, folded
into one framework. A small business's agent inherits the stability that larger deployments paid
for.

## 3. The harness: knowledge for AI engineers

AI coding assistants can now do the work of a forward-deployed engineer if they have the
knowledge. This repository gives them that knowledge, and the tools let them act on it.

```mermaid
flowchart LR
    O[Business owner or partner] -- decides --> AI[AI coding assistant<br/>Claude Code · Codex · Cursor · ChatGPT · Claude]
    ADK[This repository<br/>playbooks · policies · learnings] --> AI
    G[Agent setup guide + attribute reference<br/>knowledge.newo.ai] --> AI
    AI -- API · CLI · plugin --> NP[Newo platform]
    AI -- MCP --> KS[Knowledge Studio]
    AI -- vendor API or MCP --> EXT[Phone system · CRM · PMS]
```

## 4. The loop: from your ticket to everyone's release

```mermaid
flowchart LR
    A[AI coding assistants<br/>at partners and owners] -- bug reports · NAF change notices · learnings --> T[Newo helpdesk<br/>one format]
    T --> S[Newo supervisor<br/>finds the patterns]
    S -- general --> REL[Next NAF release<br/>for everyone]
    S -- one industry --> IND[Industry templates]
    S -- too specific --> KEEP[Answer: keep your version<br/>migrate on the next release]
    REL --> A
    IND --> A
```

What this means for you:
- **Report what you find** in the standard format ([support](support/README.md)). Every good
  report can improve every agent.
- **If you had to change NAF,** file the notice
  ([04-naf-change-policy.md](04-naf-change-policy.md)). Then wait for the decision: your change
  may come back to you as part of a release.
- **Share learnings** that other assistants should know ([learnings](../learnings/README.md)).

## 5. Why this knowledge is open

The playbooks and the agent code run only on the Newo platform: its events, commands and
integrations. Publishing the knowledge brings more agents onto the platform, and every agent makes
it more reliable for all the others.

## Status (November 2026)

| Piece | Status |
|---|---|
| This repository, the agent setup guide, the attribute reference | live |
| Newo plugin for ChatGPT and Claude (create and configure agents from a chat) | live |
| Newo CLI with V2 support, sandbox and scripted tests | live |
| Knowledge Studio and its MCP server | live, rolling out |
| A ticket tool for coding assistants | planned |
| A safe test copy of an agent | planned |
| Listing in the ChatGPT and Claude app directories | planned |
| Automated quality assessment built into the platform | planned |
