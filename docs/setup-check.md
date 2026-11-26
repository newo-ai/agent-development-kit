# Setup check

Four checks that show whether an assistant can work on one agent through the Newo CLI. Run them:

- at the start of a new setup;
- at the start of a session on a new computer;
- whenever a `newo` command fails in a way you do not understand.

The checks change nothing in the agent's setup. Check 4 leaves one sandbox chat in the
conversations. Some fixes change files on this computer; ask before each one. The sandbox chat in
check 4 reaches no real caller.

Run every command from inside the agent's folder, for example `work/<agent-name>/`
([folder layout](../README.md#set-up)).

## The four checks

| # | Check | Command | Passes when |
|---|---|---|---|
| 1 | CLI installed | `newo --version` | it prints 5.4.1 or later |
| 2 | Signed in | `newo auth status` | it exits with 0, and no API key overrides the browser login |
| 3 | The right account | `newo customer switch <idn>` once, then `newo profile` | the person confirms the account, or `Customer IDN` equals `Account idn` in `build-notes.md` |
| 4 | Sandbox round trip | `newo sandbox "Hello, this is a setup check." --json` | the agent replies |

**No agent yet** (a new agent that the build creates later): skip check 4, and run it after the
agent is created.

### 1. CLI installed

- `newo: command not found`: install it with `npm i -g newo`. The CLI needs Node.js 22.12 or
  later (`node --version`). If `node` is missing, install Node.js from https://nodejs.org, then
  quit and reopen the assistant app.
- `EACCES` on macOS or Linux: do not use `sudo`. Run `npm config set prefix ~/.npm-global`, add
  `~/.npm-global/bin` to `PATH`, reopen the terminal and install again.
- Older than 5.4.1: run `npm i -g newo` again. `newo login` came in 5.4.0; `newo auth status` and
  `newo customer switch` in 5.4.1.

### 2. Signed in

`newo auth status` answers offline and never prints a token. It exits with 0 when the person is
signed in and with 1 when `newo login` is needed first. It does not check the account: check 3
does.

- **Exit 1, not signed in:** tell the person a browser page will open. Run `newo login` in the
  background (it waits for the browser), show the person the link it prints, and wait for
  `Logged in`. EU accounts (app.eu.newo.ai): `NEWO_BASE_URL=https://app.eu.newo.ai newo login`.
  The person's steps: [SOP: sign in to the CLI](sop/sign-in-cli.md).
- **A leftover key, always check:** a key turns the browser login off. `newo auth status --json`
  shows `"method": "api_key"`, or `"api_key_overrides_login": true` when both exist. Count key
  lines without printing them:
  `grep -c -E '^NEWO_(API_KEY|API_KEYS|CUSTOMER_[A-Za-z0-9_]+_API_KEY)=' .env`, and
  `[ -n "${NEWO_API_KEY+x}${NEWO_API_KEYS+x}" ] && echo "set in the shell"`. Neither prints a key.
  If a key is found, say so: key sign-in is deprecated, and the key decides the account, not the
  login. Ask before removing the line. Keep it only where the browser login is refused (below).
- **The browser login is refused** for the account: the person's Newo user has no link to it, the
  role is not owner, co-owner, technical owner or technical support (viewers and contractors), or
  the account has a signed BAA. No link: the owner gives access, or
  [draft-support-request](../skills/draft-support-request/SKILL.md). The other two: use an API key,
  next.

#### Only when the browser login is refused: an API key

The person's key steps are in the [SOP](sop/sign-in-cli.md#only-when-the-login-is-refused-an-api-key)
(the connector IDN is lowercase, with `_` instead of spaces). Never ask for the key in the chat.
One key per folder: if the count above is more than `1`, the file holds keys for several accounts;
pass `--customer <idn>` to every command until the person keeps one.

1. **The key field (Claude desktop app), always first.** The Newo CLI ships a field for the key,
   the `newo-key` mod. Read the CLI's setup skill,
   `$(npm root -g)/newo/assistant-kit/skills/newo-setup/SKILL.md`, and follow only its section
   "In the Claude Code desktop app: a field for the key". The field saves `.env` in the folder the
   session was opened in, usually the repository root, not the agent's folder. After the message
   that names the account, move the file without reading it:
   `mv -n .env work/<agent-name>/.env`. `-n` never overwrites: if `work/<agent-name>/.env` already
   exists, the file stays where it is. Then run `[ -e .env ] && echo 'not moved'`; if it prints,
   stop and ask.
2. **A text editor, only if the field cannot load** (the mod is off, the person chose
   **Not now**, or another app). Say why, then offer to open the file for the person. Create it
   first if it is missing:
   `mkdir -p work/<agent-name> && [ -e work/<agent-name>/.env ] || (umask 077; printf 'NEWO_API_KEY=\n' > work/<agent-name>/.env)`.
   Then `open -e work/<agent-name>/.env` (Mac, TextEdit) or
   `notepad "work/<agent-name>/.env"` (Windows, with forward slashes and the quotes). They paste
   the key after `NEWO_API_KEY=`, save and close. The file name starts with a dot, so Finder and
   File Explorer hide it.

With a key, the account is wrong right after the key was changed: the CLI keeps the old sign-in
for a while. Delete only the sign-in file, `.newo/<account idn>/tokens.json` (or
`.newo/tokens.json`), and run `newo profile` again. Never delete the whole `.newo/` folder.

If the folder is inside a Git repository, also run `git check-ignore -q .env && echo ignored`. It
must print `ignored`. If it does not, stop: `.env` could end up in a commit.

### 3. The right account

Once per agent folder, run `newo customer switch <idn>`. Take the IDN from `Account idn` in
`build-notes.md`, from the MCP's customer list, or ask the person. It checks that the sign-in can
open the account and saves it in the folder's `.env` (`NEWO_DEFAULT_CUSTOMER`). A refused account
changes nothing and exits with 1: see "The browser login is refused" in check 2.

Then `newo profile` prints the account. Repeat only `Organization` and `Customer IDN` to the
person; the output also holds an email and a phone number, which the check does not need.

- **`build-notes.md` exists** (the delivery process created it): compare `Customer IDN` with its
  `Account idn`. Equal: pass. Different: stop. Ask the person which one is right, and switch the
  folder to it.
- **No `build-notes.md`:** say the organization name and the IDN to the person and ask "Is this
  the account we are working on?". One "yes" per session is enough; ask again when the account or
  the folder changes. Do not create `build-notes.md` for this: only the delivery process does.
- **Another account than the one switched to:** a key in `.env` or in the shell wins over the
  login. Run the leftover-key check in check 2.
- **`newo profile` fails:** run `newo auth status` and follow its next step. If it still fails,
  check the account through the MCP (`get_customers`) and say which way you used.

### 4. Sandbox round trip

`newo sandbox` sends one chat message to the agent in the sandbox and prints the reply. `--json`
also gives the `session_id`.

- **The agent replies:** pass. Note the `session_id`. The message shows up in the account's
  conversations as a sandbox chat.
- **No agent yet:** skip this check and run it after the agent is created
  ([assistant-guide.md, "Create the agent"](assistant-guide.md#create-the-agent)).
- **The agent exists but does not reply:** it may not be published yet. Wait 2 to 5 minutes after
  a publish and try again.
- **Timeout or an error from the platform:** run the check once more. If it fails again, report
  it with the command and the error text, without the key
  ([docs/support/](support/README.md)).

A greeting does not book, order or transfer anything, so test mode does not matter for this check.
For real tests, read [AGENTS.md, rule 10](../AGENTS.md#3-rules-always) first.

## Report

Tell the person the result in four short lines, for example:

```text
1. CLI installed: pass (5.4.1)
2. Signed in: pass
3. Account: pass ([Business Name])
4. Sandbox: pass (the agent replied), or: skipped (no agent yet)
```

For a failed check, give the one next step from the list above. Do not move on to changes until
checks 1 to 3 pass.
