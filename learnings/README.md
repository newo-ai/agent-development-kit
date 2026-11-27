# Learnings

Cases from real work, shared by coding assistants and people. Read them before you start a similar
task. Add yours when you finish.

## Read

- Look for files whose **tags** match your case: the industry, the integration (the system's
  name), the topic (telephony, knowledge, testing, debugging).
- A learning is one team's experience at one date. Check that it still holds (read the live
  setting, run the request) before you rely on it.

## Add

1. Write it **without**:
   - secrets;
   - personal data;
   - account IDs or business names (unless the business agreed).

   Describe the pattern: "a dental clinic in Germany using a cloud PMS with an MCP server".
2. Open an issue with the "Learning" form. From a terminal with the Newo CLI,
   `newo feedback learning` fills it in and checks it for private data. Newo turns an accepted
   learning into a file here, from [_template.md](_template.md).
3. Only if you work with Git and GitHub and prefer to: copy [_template.md](_template.md) to
   `learnings/YYYY-MM-DD-short-title.md` and open a pull request
   ([skills/github-workflow](../skills/github-workflow/SKILL.md), section 4).

Newo reviews learnings. Good ones are folded into the main docs, the industry pages or the
platform.
