---
name: export-docx
description: Make a Word (.docx) copy of a markdown delivery file such as sow.md, project-plan.md or customer-signoff.md, for customers who review and sign in Word. Use when a partner says "make it a Word document", "export the SOW", "I need a docx".
---

# Export to Word

Produces `<file>.docx` next to the markdown file. The markdown file stays the source; edit it, then
export again.

## Steps

1. **Check the file** has no `[brackets]` left, or tell the person which remain.
2. **Use the tool that is available**, in this order, and ask before installing anything:
   - Pandoc: `pandoc work/<agent-name>/sow.md -o work/<agent-name>/sow.docx`. If the partner has a
     branded Word template: add `--reference-doc=<template.docx>`.
   - The coding assistant's own document tool or skill, if it has one.
   - Neither available: tell the person to open the markdown in Google Docs or Word (paste, or
     "Open with") and save as `.docx`.
3. **Check the result.** Open or read the `.docx` back: headings, tables and lists intact.
4. **Never** put the `.docx` in this repository.

## Done when

- The `.docx` sits next to the markdown file and matches it.
