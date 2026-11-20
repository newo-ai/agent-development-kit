#!/usr/bin/env python3
"""Repository checks: links and anchors, SKILL.md format, and things a public repository must not hold.

Run from the repository root: python3 scripts/check.py
Exit code 0 when everything passes, 1 when something is reported. Standard library only.
"""
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "work", "exports", "newo_customers"}
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".json", ".txt", ".py", ".sh", ".html"}

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
HTML_ANCHOR = re.compile(r"<a\s+(?:name|id)=\"([^\"]+)\"")

# Things that must never be in a public repository. Each: (label, pattern).
FORBIDDEN = [
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{30,}")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
    ("AWS key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("OpenAI or Anthropic key", re.compile(r"\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{24,}")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("bearer token", re.compile(r"Bearer\s+(?!\$|<|\{|\.\.\.)[A-Za-z0-9._~+/-]{24,}")),
    # Newo customer IDN, for example C_AB_1234ABCD. Placeholders: C_XX_EXAMPLE, C_NE_ABC12345.
    ("customer IDN", re.compile(r"\bC_[A-Z]{2,4}_(?!EXAMPLE\b|ABC|X{4})(?=[A-Z0-9]*\d)[A-Z0-9]{6,12}\b")),
    # Placeholder domains are fine: example.com, *.example, *.test, yourbusiness.com and similar.
    ("email address", re.compile(
        r"\b[A-Za-z0-9._%+-]+@(?!example\.(?:com|org|net)\b|your[a-z-]*\.com\b)"
        r"[A-Za-z0-9.-]+\.(?!example\b|test\b|invalid\b)[A-Za-z]{2,}\b"
    )),
]
# Addresses that are meant to be public.
ALLOWED_EMAILS = {"noreply@anthropic.com"}
ALLOWED_EMAIL_DOMAINS = ("@newo.ai", "@users.noreply.github.com")


def files(suffixes):
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.suffix in suffixes and not (set(path.relative_to(ROOT).parts) & SKIP_DIRS):
            yield path


def slug(text, seen):
    """GitHub heading anchor."""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "").strip().lower()
    text = "".join(
        ch for ch in text
        if ch in " -_" or unicodedata.category(ch)[0] in ("L", "N")
    )
    base = text.replace(" ", "-")
    count = seen.get(base, 0)
    seen[base] = count + 1
    return base if count == 0 else f"{base}-{count}"


_anchor_cache = {}


def anchors(path):
    if path not in _anchor_cache:
        seen, found, in_fence = {}, set(), False
        for line in path.read_text(encoding="utf-8").splitlines():
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            found.update(HTML_ANCHOR.findall(line))
            m = HEADING.match(line)
            if m:
                found.add(slug(m.group(2), seen))
        _anchor_cache[path] = found
    return _anchor_cache[path]


def check_links(problems):
    for md in files({".md"}):
        in_fence = False
        for n, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            line = re.sub(r"`[^`]*`", "", line)
            for target in LINK.findall(line):
                if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                    continue  # https:, mailto: and other schemes
                ref, _, anchor = target.partition("#")
                dest = md if not ref else (md.parent / ref).resolve()
                where = f"{md.relative_to(ROOT)}:{n}"
                if not dest.exists():
                    problems.append(f"{where}: broken link {target}")
                elif anchor and dest.suffix == ".md" and anchor.lower() not in anchors(dest):
                    problems.append(f"{where}: no heading for #{anchor} in {dest.relative_to(ROOT)}")


def check_skills(problems):
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        where = skill.relative_to(ROOT)
        text = skill.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            problems.append(f"{where}: no front matter between --- lines")
            continue
        meta = dict(
            (k.strip(), v.strip()) for k, _, v in
            (line.partition(":") for line in m.group(1).splitlines() if ":" in line)
        )
        name, desc = meta.get("name", ""), meta.get("description", "")
        if name != skill.parent.name:
            problems.append(f"{where}: name '{name}' does not match the folder '{skill.parent.name}'")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            problems.append(f"{where}: name must be lowercase words joined by hyphens, at most 64 characters")
        if not desc:
            problems.append(f"{where}: description is empty")
        elif len(desc) > 1024:
            problems.append(f"{where}: description is {len(desc)} characters, the limit is 1024")


def check_public(problems):
    for path in files(TEXT_SUFFIXES):
        if path == Path(__file__).resolve():
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for label, pattern in FORBIDDEN:
                for m in pattern.finditer(line):
                    value = m.group(0)
                    if value.endswith("...") or line[m.end():m.end() + 3] == "...":
                        continue  # a shortened example, not a real value
                    if label == "email address" and (
                        value.lower() in ALLOWED_EMAILS or value.lower().endswith(ALLOWED_EMAIL_DOMAINS)
                    ):
                        continue
                    problems.append(f"{path.relative_to(ROOT)}:{n}: {label} ({value[:12]}...)")


def main():
    problems = []
    check_links(problems)
    check_skills(problems)
    check_public(problems)
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)" if problems else "All checks passed")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
