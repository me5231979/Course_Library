#!/usr/bin/env python3
"""Repoint the cross-course links that outlived the split.

When the AI-enabled Education Series courses each moved into their own repo, three links stopped
being relative and became cross-domain:

  * six courses link to the Working Smarter course
  * Decisions, Sharper links to the manager job aid, which travels with
    Working Smarter at /managers/

They currently point at the GitHub Pages URL that was live at the time of the
split. Once Working Smarter has a Vercel domain, run:

    python3 tools/relink.py --working-smarter working-smarter.vercel.app \\
        --repos /workspace

Add --dry-run to see the edits without writing. Re-running is safe.
"""
import argparse
import os
import re
import sys

OLD = "https://me5231979.github.io/estesstite/learn/"
SATELLITES = ["first-drafts-faster", "answers-faster", "ideas-faster",
              "minutes-faster", "slides-faster", "decisions-sharper"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--working-smarter", required=True,
                    help="domain serving Working Smarter, e.g. working-smarter.vercel.app")
    ap.add_argument("--repos", default="/workspace",
                    help="directory holding the course repo checkouts")
    ap.add_argument("--old", default=OLD, help="URL to replace (default: the split-time URL)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    dom = args.working_smarter.strip().rstrip("/")
    dom = re.sub(r"^https?://", "", dom)
    new = f"https://{dom}/"

    if new == args.old:
        print("nothing to do: that is already the target")
        return 0

    total, touched = 0, []
    for slug in SATELLITES:
        root = os.path.join(args.repos, slug)
        if not os.path.isdir(root):
            print(f"skip  {slug:22s} not checked out at {root}")
            continue
        hits = 0
        for dirpath, _, files in os.walk(root):
            if ".git" in dirpath:
                continue
            for fn in files:
                if not fn.endswith((".html", ".md")):
                    continue
                fp = os.path.join(dirpath, fn)
                body = open(fp, encoding="utf-8").read()
                n = body.count(args.old)
                if not n:
                    continue
                hits += n
                if not args.dry_run:
                    # /managers/ hangs off the same base, so one swap covers both
                    open(fp, "w", encoding="utf-8").write(body.replace(args.old, new))
        if hits:
            touched.append(slug)
            total += hits
        print(f"{'would fix' if args.dry_run else 'fixed':10s} {slug:22s} {hits} link(s)")

    print(f"\n{total} link(s) across {len(touched)} repo(s) -> {new}")
    if touched and not args.dry_run:
        print("\nCommit and push each one:")
        for slug in touched:
            print(f"  git -C {os.path.join(args.repos, slug)} commit -am "
                  f"'Point the Working Smarter link at its own domain' && "
                  f"git -C {os.path.join(args.repos, slug)} push")
    return 0


if __name__ == "__main__":
    sys.exit(main())
