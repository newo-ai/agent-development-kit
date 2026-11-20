#!/usr/bin/env python3
"""Repository checks: links and anchors, SKILL.md format, and things a public repository must not hold.

Run from the repository root: python3 scripts/check.py
Exit code 0 when everything passes, 1 when something is reported. Standard library only.
"""
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "work", "exports", "newo_customers"}
# Files that hold credentials and must never be tracked, whatever they contain.
SECRET_PATHS = re.compile(r"(^|/)(\.env(\.(?!example$)[^/]+)?|[^/]+\.(pem|key|p12|pfx))$")

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


def tracked():
    """Files Git tracks or has staged; local ignored files (a real .env) stay out of scope."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "-z", "--cached"], cwd=ROOT, capture_output=True, check=True
        ).stdout.decode("utf-8")
        paths = [ROOT / p for p in out.split("\0") if p]
    except (OSError, subprocess.CalledProcessError):
        paths = [p for p in ROOT.rglob("*") if not (set(p.relative_to(ROOT).parts) & SKIP_DIRS)]
    return sorted(p for p in paths if p.is_file())


def files(suffixes=None):
    for path in tracked():
        if suffixes is None or path.suffix in suffixes:
            yield path


def text_of(path):
    data = path.read_bytes()
    if b"\0" in data[:8192]:
        return None  # binary
    return data.decode("utf-8", errors="replace")


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
                ref = ref.split("?", 1)[0]
                if not ref:
                    dest = md
                elif ref.startswith("/"):
                    dest = (ROOT / ref.lstrip("/")).resolve()  # GitHub: from the repository root
                else:
                    dest = (md.parent / ref).resolve()
                where = f"{md.relative_to(ROOT)}:{n}"
                if ROOT not in dest.parents and dest != ROOT:
                    problems.append(f"{where}: link leaves the repository")
                elif not dest.exists():
                    problems.append(f"{where}: broken link to {ref}")
                elif anchor and dest.suffix == ".md" and anchor.lower() not in anchors(dest):
                    problems.append(f"{where}: no heading for #{anchor} in {dest.relative_to(ROOT)}")


def yaml_scalar(raw):
    """Read a one-line YAML scalar the way a YAML parser would; return (value, error)."""
    if raw[:1] == '"':
        if len(raw) < 2 or not raw.endswith('"') or re.search(r'(?<!\\)"', raw[1:-1]):
            return None, 'the double-quoted value is not closed, or has an unescaped "'
        return raw[1:-1], None
    if raw[:1] == "'":
        if len(raw) < 2 or not raw.endswith("'") or re.search(r"(?<!')'(?!')", raw[1:-1]):
            return None, "the single-quoted value is not closed, or has an unescaped '"
        return raw[1:-1].replace("''", "'"), None
    if raw[:1] in ("|", ">"):
        return None, "use a one-line value"
    if raw[:1] in tuple("!&*[]{}#%@`,?-") and raw[:2] not in ("- ",):
        return None, f"a plain value cannot start with {raw[:1]!r}; put it in quotes"
    if ": " in raw or raw.endswith(":") or " #" in raw:
        return None, 'a plain value cannot contain ": " or " #"; put it in double quotes'
    return raw, None


def check_skills(problems):
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        where = skill.relative_to(ROOT)
        text = skill.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            problems.append(f"{where}: no front matter between --- lines")
            continue
        meta = {}
        for line in m.group(1).splitlines():
            key, sep, raw = line.partition(":")
            if sep and not line.startswith((" ", "\t", "#")) and key.strip() in ("name", "description"):
                value, error = yaml_scalar(raw.strip())
                if error:
                    problems.append(f"{where}: {key.strip()} is not valid YAML: {error}")
                meta[key.strip()] = (raw.strip() if error else value).strip()
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
    for path in files():
        rel = path.relative_to(ROOT).as_posix()
        if SECRET_PATHS.search(rel):
            problems.append(f"{rel}: a file of this kind holds credentials and must not be tracked")
        if path == Path(__file__).resolve():
            continue
        text = text_of(path)
        if text is None:
            continue
        for n, line in enumerate(text.splitlines(), 1):
            for label, pattern in FORBIDDEN:
                for m in pattern.finditer(line):
                    value = m.group(0)
                    if value.endswith("...") or line[m.end():m.end() + 3] == "...":
                        continue  # a shortened example, not a real value
                    if label == "email address" and (
                        value.lower() in ALLOWED_EMAILS or value.lower().endswith(ALLOWED_EMAIL_DOMAINS)
                    ):
                        continue
                    problems.append(f"{rel}:{n}: {label}")  # never print the value


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
