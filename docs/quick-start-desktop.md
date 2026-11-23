# Quick start: the Claude desktop app, no Git

For a person who is not technical and uses the Claude desktop app. You need no GitHub account, no
Git and no terminal: the assistant runs the commands. Target time: about 10 minutes (an estimate,
not yet measured).

Steps marked **(to confirm)** have not been checked click by click yet. If the screen looks
different, tell your assistant what you see.

## What you need

- The Claude desktop app, signed in, on a Mac or Windows computer.
- A Newo account with the agent, and permission to open its **Builder**.

## Steps

1. **Download the kit.** Open https://github.com/newo-ai/agent-development-kit, click the green
   **Code** button, then **Download ZIP**. Unzip it and move the folder
   (`agent-development-kit-main`) to a place you will find again, for example **Documents**.
2. **Open it in Claude.** In the Claude desktop app, open the **Code** tab and choose the
   `agent-development-kit-main` folder **(to confirm)**.
3. **Paste the starter message.** Change the business name:

   ```text
   Read AGENTS.md. I want to work on the Newo agent for Northfield HVAC. Make a folder for it
   in work/, help me put the API key in its .env file, and run the setup check. I am not
   technical: explain each step in plain words and ask before you change anything.
   ```

4. **Let the assistant install the tools.** It checks Node.js and the Newo CLI and installs what
   is missing. Allow the commands it asks for. If it asks you to install Node.js yourself, take
   the LTS version from https://nodejs.org, then quit and reopen the Claude app.
5. **Create the API key in Newo.** Sign in at https://app.newo.ai, choose the account, open
   **Builder** → **Integrations** → **API Integration**, create a connector (any name, for
   example `newo-cli`) and save it. Open it again and copy the key.
6. **Put the key in the file, not in the chat.** The assistant creates the `.env` file in the
   agent's folder and opens it for you **(to confirm)**. Paste the key after `NEWO_API_KEY=`, save,
   close the file, and type "done". Never paste the key into the chat.
7. **Read the setup check.** The assistant runs the [setup check](setup-check.md) and gives you
   four lines. It says the account name: check that it is the right business. All four pass: you
   are ready.

## After that

- Every agent gets its own folder in `work/` and its own key. Repeat steps 3, 5 and 6 for the next
  agent.
- **Updating the kit:** download the ZIP again, unzip it, and move your `work/` folder from the
  old copy into the new one before you delete the old copy. `work/` holds your agents' files and
  keys.
- Something stopped working? Ask the assistant to run the setup check again.
