# Setup check

Four checks that show whether an assistant can work on one agent. Run them:

- at the start of a new setup;
- at the start of a session on a new computer;
- whenever a `newo` command fails in a way you do not understand.

The check only reads. It changes nothing in the account, so you can run it as often as you like.
The sandbox chat in check 4 reaches no real caller.

Run every command from inside the agent's folder, for example `work/northfield-hvac/`
([folder layout](../README.md#set-up)).

## The four checks

| # | Check | Command | Passes when |
|---|---|---|---|
| 1 | CLI installed | `newo --version` | it prints 4.6.0 or later |
| 2 | Key found | `grep -c '^NEWO_API_KEY=..*' .env` | it prints `1` |
| 3 | The right account | `newo profile` | `Customer IDN` equals `Account idn` in `build-notes.md` |
| 4 | Sandbox round trip | `newo sandbox "Hello, this is a setup check." --json` | the agent replies |

### 1. CLI installed

- `newo: command not found`: install it with `npm i -g newo`. The CLI needs Node.js 22.12 or
  later (`node --version`). If `node` is missing, install Node.js from https://nodejs.org, then
  quit and reopen the assistant app.
- `EACCES` on macOS or Linux: do not use `sudo`. Run `npm config set prefix ~/.npm-global`, add
  `~/.npm-global/bin` to `PATH`, reopen the terminal and install again.
- Older than 4.6.0: run `npm i -g newo` again. Flow Designer V2 needs 4.6.0 or later.

### 2. Key found

The command prints a count, never the key. Do not run `cat .env`, `env` or `printenv`.

- `No such file`: there is no `.env` in this folder. Check that you are in the agent's folder
  (`pwd`). If you are, `newo init` creates an empty `.env` and a `.gitignore`.
- `0`: the file has no key yet. Ask the person to create the key
  ([docs/02, section A](02-access-and-tools.md#a-terminal-assistants)) and paste it after
  `NEWO_API_KEY=` themselves. Give them the full path of the file. The name starts with a dot, so
  Finder and File Explorer hide it: they can open it in a code editor, or turn on hidden files.
  Never ask for the key in the chat.
- More than `1`: the file has the line twice. Ask the person to keep one.
- If `.env` also holds `NEWO_API_KEYS` or `NEWO_CUSTOMER_..._API_KEY` lines, say so. Several keys
  in one file is not recommended: one folder, one agent, one key.

If the folder is inside a Git repository, also run `git check-ignore -q .env && echo ignored`. It
must print `ignored`. If it does not, stop: the key could end up in a commit.

### 3. The right account

`newo profile` prints the account. Repeat only `Organization` and `Customer IDN` to the person;
the output also holds an email and a phone number, which the check does not need.

- **`build-notes.md` exists:** compare `Customer IDN` with its `Account idn`. Equal: pass.
  Different: stop. The key belongs to another account. Ask the person which one is right.
- **No `build-notes.md` yet** (a new agent): say the organization name and the IDN to the person
  and ask "Is this the agent we are working on?". After a "yes", copy
  [the build-notes template](../delivery/02-build/templates/build-notes.md) to the folder (ask
  first) and fill in `Account idn`.
- **The account is wrong right after the key was changed:** the CLI keeps the old sign-in for a
  while. Delete only the sign-in file, `.newo/<account idn>/tokens.json` (or
  `.newo/tokens.json`), and run `newo profile` again. Never delete the whole `.newo/` folder.
- **401 or 403:** the key is wrong or was revoked. Ask the person to copy it again from the
  connector in the Builder.
- **`newo profile` fails for another reason:** use the API instead. Exchange the key for a token
  and call `GET /api/v1/customer/profile`
  ([docs/02, section A](02-access-and-tools.md#a-terminal-assistants)). Compare its `idn` the same
  way. Say which way you used.

### 4. Sandbox round trip

`newo sandbox` sends one chat message to the agent in the sandbox and prints the reply. `--json`
also gives the `session_id`.

- **The agent replies:** pass. Note the `session_id`. The message shows up in the account's
  conversations as a sandbox chat.
- **No agent, or no reply:** the agent may not be created or published yet. Read
  [assistant-guide.md, "Create the agent"](assistant-guide.md#create-the-agent). If it exists, wait
  2 to 5 minutes after a publish and try again.
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
3. Account: pass (Northfield HVAC)
4. Sandbox: pass (the agent replied)
```

For a failed check, give the one next step from the list above. Do not move on to changes until
checks 1 to 3 pass.
