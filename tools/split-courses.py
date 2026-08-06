#!/usr/bin/env python3
"""Split every shared-repo course into its own standalone repo.

Two shapes go in, one comes out:

  13 courses nested in Course_Library are already self-contained -> straight copy.
   7 CHART courses share one assets folder and a -class suffix -> restructured
     to the house layout (/, /web/, /facilitator/) with their own assets.

Every result has the same shape, so one Vercel project per repo serves all
three editions with no build step and no Root Directory setting.
"""
import json
import os
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser

LIB = "/workspace/course_library"
CHART = "/workspace/courses"
OUT = "/workspace"

# Cross-course links that become cross-domain once each course stands alone.
# These point at what is live today; tools/relink.py rewrites them to the
# Vercel domains once those exist.
WS = "https://me5231979.github.io/estesstite/learn/"
WSM = "https://me5231979.github.io/estesstite/learn/managers/"

VERCEL_JSON = json.dumps({
    "cleanUrls": False,
    "headers": [
        {"source": "/(.*).html",
         "headers": [{"key": "Cache-Control",
                      "value": "public, max-age=0, must-revalidate"}]},
        {"source": "/assets/fonts/(.*)",
         "headers": [{"key": "Cache-Control", "value": "public, max-age=2592000"}]},
    ],
}, indent=2) + "\n"

# slug -> source folder under Course_Library
LIFT = {
    "across-your-week": "courses/AI-Across-Your-Week",
    "admin-automated": "courses/Admin-Automated",
    "change-that-sticks": "courses/Change-Leadership-for-AI",
    "delegating-rethought": "courses/Delegating-with-AI",
    "feedback-ready": "ai-coaching-feedback",
    "guardrails-responsible-use": "courses/AI-Guardrails",
    "hiring-human": "courses/Hiring-with-AI",
    "leading-the-shift": "leading-ai-adoption",
    "making-it-normal": "courses/Leading-AI-Adoption",
    "numbers-faster": "courses/Numbers-Faster",
    "people-data-safely": "courses/People-Data-with-AI",
    "talent-calls-sharper": "ai-talent-decisions",
    "trust-then-verify": "courses/Trust-Then-Verify",
}

# slug -> (classroom dir, self-paced dir) inside the courses repo
SPLIT = {
    "first-drafts-faster": ("drafts-class", "drafts"),
    "answers-faster": ("answers-class", "answers"),
    "ideas-faster": ("ideas-class", "ideas"),
    "minutes-faster": ("minutes-class", "minutes"),
    "slides-faster": ("slides-class", "slides"),
    "decisions-sharper": ("decisions-class", "decisions"),
    "working-smarter": ("classroom", ""),   # self-paced sits at the repo root
}

TITLES = {
    "across-your-week": "Across Your Week", "admin-automated": "Admin, Automated",
    "change-that-sticks": "Change That Sticks", "delegating-rethought": "Delegating, Rethought",
    "feedback-ready": "Feedback, Ready", "guardrails-responsible-use": "Guardrails & Responsible Use",
    "hiring-human": "Hiring, Human", "leading-the-shift": "Leading the Shift",
    "making-it-normal": "Making It Normal", "numbers-faster": "Numbers, Faster",
    "people-data-safely": "People Data, Safely", "talent-calls-sharper": "Talent Calls, Sharper",
    "trust-then-verify": "Trust, Then Verify", "first-drafts-faster": "First Drafts, Faster",
    "answers-faster": "Answers, Faster", "ideas-faster": "Ideas, Faster",
    "minutes-faster": "Minutes, Faster", "slides-faster": "Slides, Faster",
    "decisions-sharper": "Decisions, Sharper", "working-smarter": "Working Smarter",
}


def rewrite(path, rules):
    """Apply ordered (old, new) string rules to a file. Order matters: the
    specific links go before the bare ../ that would otherwise swallow them."""
    src = open(path, encoding="utf-8").read()
    for old, new in rules:
        src = src.replace(old, new)
    open(path, "w", encoding="utf-8").write(src)


def build_lift(slug):
    dst = os.path.join(OUT, slug)
    keep_git = os.path.join(dst, ".git")
    stash = None
    if os.path.isdir(keep_git):
        stash = keep_git + ".keep"
        shutil.move(keep_git, stash)
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(os.path.join(LIB, LIFT[slug]), dst)
    if stash:
        shutil.move(stash, os.path.join(dst, ".git"))
    if not os.path.exists(os.path.join(dst, "vercel.json")):
        open(os.path.join(dst, "vercel.json"), "w").write(VERCEL_JSON)

    # Two things the course carried because it lived inside Course_Library:
    #  - 404.html used host-absolute paths under /Course_Library/<course>/
    #  - the facilitator's "Self-paced version" link pointed at web/ from
    #    inside facilitator/, which never resolved even before the move
    old_root = f"/Course_Library/{LIFT[slug]}/"
    for dirpath, _, files in os.walk(dst):
        if ".git" in dirpath:
            continue
        for fn in files:
            if fn.endswith((".html", ".md")):
                rewrite(os.path.join(dirpath, fn), [(old_root, "/")])
    fac = os.path.join(dst, "facilitator", "index.html")
    if os.path.exists(fac):
        rewrite(fac, [('href="web/"', 'href="../web/"')])
    return dst


def build_split(slug):
    cls, sp = SPLIT[slug]
    dst = os.path.join(OUT, slug)
    keep_git = os.path.join(dst, ".git")
    stash = None
    if os.path.isdir(keep_git):
        stash = keep_git + ".keep"
        shutil.move(keep_git, stash)
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    os.makedirs(os.path.join(dst, "web"))
    os.makedirs(os.path.join(dst, "facilitator"))
    if stash:
        shutil.move(stash, os.path.join(dst, ".git"))

    # its own copy of what was the shared assets folder
    shutil.copytree(os.path.join(CHART, "assets"), os.path.join(dst, "assets"))

    shutil.copy2(os.path.join(CHART, cls, "index.html"), os.path.join(dst, "index.html"))
    sp_src = os.path.join(CHART, sp, "index.html") if sp else os.path.join(CHART, "index.html")
    shutil.copy2(sp_src, os.path.join(dst, "web", "index.html"))
    shutil.copy2(os.path.join(CHART, cls, "facilitator", "index.html"),
                 os.path.join(dst, "facilitator", "index.html"))

    if slug == "working-smarter":
        # the manager job aid travels with the anchor course
        shutil.copytree(os.path.join(CHART, "managers"), os.path.join(dst, "managers"))
        rewrite(os.path.join(dst, "index.html"), [
            ('href="../"', 'href="web/"'),            # was the self-paced edition
            ('"../assets/', '"assets/'),
        ])
        rewrite(os.path.join(dst, "web", "index.html"), [
            ('href="classroom/"', 'href="../"'),      # classroom now sits at the root
            ('"assets/', '"../assets/'),
        ])
        rewrite(os.path.join(dst, "facilitator", "index.html"), [
            ('href="../../"', 'href="../web/"'),      # was the self-paced edition
            ('"../../assets/', '"../assets/'),
        ])                                            # href="../" already means classroom
    else:
        rewrite(os.path.join(dst, "index.html"), [
            (f'href="../{sp}/"', 'href="web/"'),
            ('href="../managers/"', f'href="{WSM}"'),
            ('href="../"', f'href="{WS}"'),           # the Working Smarter course
            ('"../assets/', '"assets/'),
        ])
        rewrite(os.path.join(dst, "web", "index.html"), [
            ('href="../managers/"', f'href="{WSM}"'),
            ('href="../"', f'href="{WS}"'),           # before the classroom rule below
            (f'href="../{cls}/"', 'href="../"'),
        ])                                            # web/ is one level down: ../assets/ still right
        rewrite(os.path.join(dst, "facilitator", "index.html"), [
            (f'href="../../{sp}/"', 'href="../web/"'),
            ('href="../../managers/"', f'href="{WSM}"'),
            ('href="../../"', f'href="{WS}"'),
            ('"../../assets/', '"../assets/'),
        ])                                            # href="../" already means classroom

    open(os.path.join(dst, "vercel.json"), "w").write(VERCEL_JSON)
    return dst


class Refs(HTMLParser):
    """Collect local href/src targets so we can prove each one resolves.

    Images carrying an onerror fallback are skipped: the facilitator guide
    ships optional slide screenshots and hides the frame when one is absent.
    """
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img" and a.get("onerror"):
            return
        for k, v in attrs:
            if k in ("href", "src") and v:
                self.refs.append(v)


def verify(root, slug):
    """Every local reference must resolve to a file on disk, and nothing may
    reach above the repo root."""
    problems = []
    for dirpath, _, files in os.walk(root):
        if ".git" in dirpath:
            continue
        for fn in files:
            if not fn.endswith(".html"):
                continue
            fp = os.path.join(dirpath, fn)
            p = Refs()
            p.feed(open(fp, encoding="utf-8").read())
            rel = os.path.relpath(fp, root)
            for ref in p.refs:
                if re.match(r"^(#|mailto:|tel:|https?:|data:|//|javascript:)", ref):
                    continue
                if "'" in ref or "+" in ref:      # built by script at runtime
                    continue
                target = ref.split("?")[0].split("#")[0]
                if not target:
                    continue
                # a leading / is host-absolute, so it resolves against the repo root
                base = root if target.startswith("/") else dirpath
                resolved = os.path.normpath(os.path.join(base, target.lstrip("/")))
                if not resolved.startswith(os.path.realpath(root)) and \
                   not resolved.startswith(root):
                    problems.append(f"{rel}: {ref} escapes the repo")
                    continue
                if target.endswith("/"):
                    ok = os.path.exists(os.path.join(resolved, "index.html"))
                else:
                    ok = os.path.exists(resolved)
                if not ok:
                    problems.append(f"{rel}: {ref} -> missing")
    return problems


def readme(slug, kind):
    t = TITLES[slug]
    extra = ""
    if kind == "split" and slug != "working-smarter":
        extra = (f"\n## Cross-course link\n\nThis course points at the Working Smarter "
                 f"course, currently at\n`{WS}`. When the Vercel domains are settled, "
                 f"run `tools/relink.py` in\nCourse_Library to repoint it.\n")
    if slug == "working-smarter":
        extra = ("\n## Also here\n\n`/managers/` is the manager job aid and its printable "
                 "`job-aid.html`.\nThe six sibling CHART courses link back to this course.\n")
    return f"""# {t}

Part of the Vanderbilt Learning Series. One repo, one Vercel project, three
editions served from one deployment:

| Path | Edition |
| --- | --- |
| `/` | classroom, projected and facilitated |
| `/web/` | self-paced, the same course minus the room-only moments |
| `/facilitator/` | facilitator edition with the ATD runbook |

No build step: these are pre-generated static files. In Vercel, leave the
Root Directory empty, set Framework Preset to Other, and set Deployment
Protection to preview-only so learners scanning a QR code are not asked to
sign in.

Catalog: https://github.com/me5231979/Course_Library
{extra}"""


def main():
    only = sys.argv[1:] or None
    built, failed = [], []
    for slug in list(LIFT) + list(SPLIT):
        if only and slug not in only:
            continue
        kind = "lift" if slug in LIFT else "split"
        dst = build_lift(slug) if kind == "lift" else build_split(slug)
        open(os.path.join(dst, "README.md"), "w").write(readme(slug, kind))
        problems = verify(dst, slug)
        n = sum(len(f) for _, _, f in os.walk(dst))
        if problems:
            failed.append((slug, problems))
            print(f"FAIL  {slug:28s} {len(problems)} broken ref(s)")
            for p in problems[:6]:
                print(f"        {p}")
        else:
            built.append(slug)
            print(f"ok    {slug:28s} {kind:6s} {n:3d} files")
    print(f"\nbuilt {len(built)}, failed {len(failed)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
