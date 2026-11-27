# SOP: sign in to the Newo CLI

Do this **only when your assistant asks**. Most work needs only the Newo MCP
([connect it](connect-newo-mcp.md)). The Newo CLI is for saved test files, CI, an export or a
backup of the agent ([which path](../02-access-and-tools.md#which-path)).

You sign in with your Newo account in the browser, the same account you use at app.newo.ai. You
need no API key.

## 1. Sign in

1. Your assistant runs `newo login`. A browser page opens; the link is also shown in the chat.
2. Sign in with your Newo account.
3. Tell your assistant "signed in".

The sign-in is kept on this computer. Your assistant checks it with `newo auth status`.

## 2. Choose the agent's account

Your assistant runs `newo customer switch <idn>` in the agent's folder and tells you the account's
name. Check that it is the right business. Each agent has its own folder in `work/`, and each
folder remembers its own account.

## If the browser login is refused

The CLI refuses the browser login when:
- your Newo user has no link to the account;
- your role on the account is not owner, co-owner, technical owner or technical support (viewers
  and contractors);
- the account has a signed BAA.

For the first case, ask the account owner for access, or have your assistant draft a request to
Newo. For the other two, use an API key, below.

## Only when the login is refused: an API key

Signing in with a key is deprecated and will be removed. A key in the agent's folder also turns
the browser login off there. Never paste the key into a chat: anyone who reads the chat can use
it.

1. Sign in at https://app.newo.ai, choose the account and open **Builder**.
2. Go to **Integrations** and open **API Integration**.
3. Create a connector. Its IDN must be all lowercase, with no spaces: use `_` instead of a space,
   for example `newo_cli`. Save it.
4. Open the connector again and copy the key. It appears only after saving.
5. Give it to the assistant without the chat:
   - **Claude desktop app:** the assistant opens a field for the key above the prompt. The first
     time, Claude asks whether to turn on the mods written in this session: choose
     **Turn them on** **(to confirm)**. Paste the key into the field and press Enter. The key goes
     straight into a file, the assistant never sees it, and you get a message with the account's
     name.
   - **Any other app, or if the field does not load:** the assistant opens the key file
     (`work/<agent-name>/.env`) in a text editor. Paste the key after `NEWO_API_KEY=` and save.

If the key was exposed (you pasted it into a chat, an email or a file someone else can read), tell
your assistant. Newo support can replace the key.

## If it goes wrong

- **The browser page does not open:** open the link from the chat yourself.
- **The assistant says you are not signed in:** sign in again (step 1).
- **The account named is another business:** tell your assistant the right one. It switches the
  folder to it.

## Next

Your assistant runs the [setup check](../setup-check.md) and tells you the account's name. Check
that it is the right business.

Stuck? Tell your assistant "I'm stuck".
