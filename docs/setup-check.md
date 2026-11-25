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
| 1 | CLI installed | `newo --version` | it prints 5.3.0 or later |
| 2 | Key found | `grep -c '^NEWO_API_KEY=..*' .env` | it prints `1` |
| 3 | The right account | `newo profile` | the person confirms the account, or `Customer IDN` equals `Account idn` in `build-notes.md` |
| 4 | Sandbox round trip | `newo sandbox "Hello, this is a setup check." --json` | the agent replies |

**No agent yet** (a new agent that the build creates later): skip check 4, and run it after the
agent is created.

### 1. CLI installed

- `newo: command not found`: install it with `npm i -g newo`. The CLI needs Node.js 22.12 or
  later (`node --version`). If `node` is missing, install Node.js from https://nodejs.org, then
  quit and reopen the assistant app.
- `EACCES` on macOS or Linux: do not use `sudo`. Run `npm config set prefix ~/.npm-global`, add
  `~/.npm-global/bin` to `PATH`, reopen the terminal and install again.
- Older than 5.3.0: run `npm i -g newo` again. The key field (the `newo-key` mod) needs 5.3.0, and
  the CLI's `newo-setup` skill needs 5.1.0.

### 2. Key found

The command prints a count, never the key. Do not run `cat .env`, `env` or `printenv`.

- **Several keys in one file, first:** if
  `grep -c -E '^NEWO_(API_KEYS|CUSTOMER_[A-Za-z0-9_]+_API_KEY)=' .env` prints more than `0`, the
  file holds keys for several accounts. Do not open the key field: it would add one more key. Say
  so: several keys in one file is not recommended (one folder, one agent, one key). Until the
  person moves this agent's key into its own folder, pass `--customer <idn>` to every command.
- `No such file`: check that you are in the agent's folder (`pwd`). If you are, the agent has no
  key yet: follow the next item, which creates the file. Do not run `newo init` inside `work/`: it
  writes its own `AGENTS.md`, `CLAUDE.md` and skills into the folder, and they compete with the
  ADK's. The root `.gitignore` already ignores `work/` and `.env`.
- `0`: no key yet. Give the person the ADK's key steps,
  [docs/02, section A](02-access-and-tools.md#a-terminal-assistants) (the connector IDN is
  lowercase, with `_` instead of spaces), not the key steps in the CLI's `newo-setup` skill. Never
  ask for the key in the chat.
  1. **The key field (Claude desktop app), always first.** The Newo CLI ships a field for the
     key, the `newo-key` mod. Read the CLI's setup skill,
     `$(npm root -g)/newo/assistant-kit/skills/newo-setup/SKILL.md`, and follow only its section
     "In the Claude Code desktop app: a field for the key". The field saves `.env` in the folder
     the session was opened in, usually the repository root, not the agent's folder. After the
     message that names the account, move the file without reading it:
     `mv -n .env work/<agent-name>/.env`. `-n` never overwrites: if `work/<agent-name>/.env`
     already exists, the file stays where it is. Then run `[ -e .env ] && echo 'not moved'`; if
     it prints, stop and ask.
  2. **A text editor, only if the field cannot load** (the mod is off, the person chose
     **Not now**, or another app). Say why, then offer to open the file for the person. Create it
     first if it is missing:
     `mkdir -p work/<agent-name> && [ -e work/<agent-name>/.env ] || (umask 077; printf 'NEWO_API_KEY=\n' > work/<agent-name>/.env)`.
     Then `open -e work/<agent-name>/.env` (Mac, TextEdit) or
     `notepad "work/<agent-name>/.env"` (Windows, with forward slashes and the quotes). They paste
     the key after `NEWO_API_KEY=`, save and close. No code editor is needed. The file name starts
     with a dot, so Finder and File Explorer hide it.
- More than `1`: the file has the line twice. Ask the person to keep one.

If the folder is inside a Git repository, also run `git check-ignore -q .env && echo ignored`. It
must print `ignored`. If it does not, stop: the key could end up in a commit.

### 3. The right account

`newo profile` prints the account. Repeat only `Organization` and `Customer IDN` to the person;
the output also holds an email and a phone number, which the check does not need.

- **`build-notes.md` exists** (the delivery process created it): compare `Customer IDN` with its
  `Account idn`. Equal: pass. Different: stop. The key belongs to another account. Ask the person
  which one is right.
- **No `build-notes.md`:** say the organization name and the IDN to the person and ask "Is this
  the account we are working on?". One "yes" per session is enough; ask again when the key or the
  folder changes. Do not create `build-notes.md` for this: only the delivery process does.
- **A key exported in the shell wins over `.env`**, and so does `NEWO_API_KEYS`. If the account
  is not the expected one, check
  `[ -n "${NEWO_API_KEY+x}${NEWO_API_KEYS+x}" ] && echo "set in the shell"` (it never prints a
  key).
- **The account is wrong right after the key was changed:** the CLI keeps the old sign-in for a
  while. Delete only the sign-in file, `.newo/<account idn>/tokens.json` (or
  `.newo/tokens.json`), and run `newo profile` again. Never delete the whole `.newo/` folder.
- **401 or 403:** the key is wrong or was revoked. Ask the person to copy it again from the
  connector in the Builder.
- **`newo profile` fails for another reason:** use the API instead. Exchange the key for a token
  and call `GET /api/v1/customer/profile`
  ([docs/02, section A](02-access-and-tools.md#a-terminal-assistants)). Check its `idn` the same
  way. Say which way you used.

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
1. CLI installed: pass (5.3.0)
2. Key found: pass
3. Account: pass ([Business Name])
4. Sandbox: pass (the agent replied), or: skipped (no agent yet)
```

For a failed check, give the one next step from the list above. Do not move on to changes until
checks 1 to 3 pass.
