# Quick start: the Claude desktop app, no Git

For a person who is not technical and uses the Claude desktop app. You need no GitHub account, no
Git and no terminal: the assistant does the work. You sign in with your Newo account; you need no
API key to start. Target time: about 10 minutes (an estimate, not yet measured).

Steps marked **(to confirm)** have not been checked click by click yet. If the screen looks
different, tell your assistant what you see.

## What you need

- The Claude desktop app, signed in, on a Mac or Windows computer.
- A Newo account that can open the agent.

## Steps

1. **Download the kit.** Open https://github.com/newo-ai/agent-development-kit, click the green
   **Code** button, then **Download ZIP**. Unzip it and move the folder
   (`agent-development-kit-main`) to a place you will find again, for example **Documents**.
2. **Open it in Claude.** In the Claude desktop app, open the **Code** tab and choose the
   `agent-development-kit-main` folder **(to confirm)**.
3. **Connect the Newo MCP.** Follow the [SOP: connect the Newo MCP](sop/connect-newo-mcp.md).
   You do this once.
4. **Paste the starter message.** Change the business name:

   ```text
   Read AGENTS.md. I want to work on the Newo agent for [Business Name]. Use the Newo MCP. I am
   not technical: explain each step in plain words and ask before you change anything.
   ```

5. **Check the account.** Ask your assistant "List my Newo businesses". It names your business.
   If not, see
   [SOP: connect the Newo MCP, "Check it worked"](sop/connect-newo-mcp.md#check-it-worked).

**The CLI only when your assistant asks** (a few tasks need the Newo CLI). You sign in with your
Newo account, no key: [SOP: sign in to the CLI](sop/sign-in-cli.md). The assistant installs the
tools that task needs and asks before each command. If it asks you to install Node.js yourself,
take the LTS version from https://nodejs.org, then quit and reopen the Claude app.

## After that

- For the next agent, repeat steps 4 and 5 with its name. If it needs the CLI, it gets its own
  folder in `work/`, switched to its own account.
- **Updating the kit:** download the ZIP again, unzip it, and move your `work/` folder from the
  old copy into the new one before you delete the old copy. `work/` holds your agents' files and
  keys.
- Stuck, or something stopped working? Tell your assistant "I'm stuck".
