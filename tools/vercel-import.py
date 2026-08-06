#!/usr/bin/env python3
"""Create one Vercel project per Learning Series site, linked to its GitHub repo.

Run this from any machine that can reach api.vercel.com (the Claude sandbox
cannot; its network policy blocks that host).

    export VERCEL_TOKEN=...          # Vercel > Account Settings > Tokens
    python3 tools/vercel-import.py

Add --dry-run to see what it would do. Re-running is safe: projects that
already exist are skipped, not duplicated.

Each site is ONE project serving all three editions from one deployment:
    /              classroom edition
    /web/          self-paced edition
    /facilitator/  facilitator edition (+ /facilitator/guide.html)

So the Root Directory stays empty and there is no build step: these are
pre-generated static files.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.vercel.com"

# project name -> GitHub repo (owner/name)
SITES = [
    # repo -> Vercel project. One project serves every edition in that repo.
    ("ai-classroom",                 "me5231979/AI_Classroom"),
    ("difficult-conversations",      "me5231979/Difficult_Conversations"),
    ("coaching-for-performance",     "me5231979/Coaching-for-Performance"),
    ("emotional-intelligence",       "me5231979/Emotional-Intelligence"),
    ("presentation-public-speaking", "me5231979/Presentation-Public-Speaking"),
    ("building-brave-teams",         "me5231979/TeamUp"),
    ("workflow-process-redesign",    "me5231979/Workflow"),
    ("hcm-essentials",               "me5231979/HCM_Education"),
    # estesstite hosts 7 CHART courses under /learn/
    ("chart-program",                "me5231979/estesstite"),
    # Course_Library is the catalog AND hosts 13 courses under /courses/ and /ai-*/
    ("course-library",               "me5231979/Course_Library"),
    # AI 201: still live, no longer carded on the library page
    ("ai-advanced",                  "me5231979/AI-Advanced"),
]


def call(method, path, token, body=None):
    """Return (status, parsed_json_or_text)."""
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, method=method)
    req.add_header("Authorization", "Bearer " + token)
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw or b"{}")
        except json.JSONDecodeError:
            return e.code, raw.decode(errors="replace")
    except urllib.error.URLError as e:
        return 0, str(e)


def resolve_team(token, slug):
    status, body = call("GET", "/v2/teams?slug=" + slug, token)
    if status == 200 and isinstance(body, dict):
        team = body.get("id") and body or (body.get("teams") or [{}])[0]
        if team.get("id"):
            return team["id"], team.get("name") or slug
    print(f"Could not resolve team '{slug}' (HTTP {status}): {body}")
    sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--team", default="flh-ac303cfa",
                    help="Vercel team slug (default: flh-ac303cfa, the FLH team)")
    ap.add_argument("--branch", default="main", help="production branch (default: main)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.dry_run:
        print(f"Would create {len(SITES)} projects in team '{args.team}', "
              f"production branch '{args.branch}':\n")
        for name, repo in SITES:
            print(f"  {name:30s} <- {repo}")
        print("\nEach serves /, /web/, and /facilitator/ from one deployment.")
        return

    token = os.environ.get("VERCEL_TOKEN")
    if not token:
        print("Set VERCEL_TOKEN first: export VERCEL_TOKEN=...")
        sys.exit(1)

    team_id, team_name = resolve_team(token, args.team)
    print(f"Team: {team_name} ({team_id})\n")

    made, skipped, failed = [], [], []
    for name, repo in SITES:
        status, body = call("POST", f"/v11/projects?teamId={team_id}", token, {
            "name": name,
            "framework": None,
            "buildCommand": None,
            "installCommand": None,
            "outputDirectory": None,
            "gitRepository": {"type": "github", "repo": repo},
        })

        if status in (200, 201):
            print(f"created  {name:30s} <- {repo}")
            made.append(name)
        elif status == 409 or (isinstance(body, dict) and "already exists" in str(body).lower()):
            print(f"exists   {name:30s} (skipped)")
            skipped.append(name)
            continue
        else:
            err = body.get("error", {}).get("message", body) if isinstance(body, dict) else body
            print(f"FAILED   {name:30s} HTTP {status}: {err}")
            failed.append((name, err))
            continue

        # First production deploy. Project creation alone does not deploy;
        # after this, every push to the production branch deploys on its own.
        owner, repo_name = repo.split("/", 1)
        dstatus, dbody = call("POST", f"/v13/deployments?teamId={team_id}", token, {
            "name": name,
            "project": name,
            "target": "production",
            "gitSource": {"type": "github", "org": owner, "repo": repo_name, "ref": args.branch},
        })
        if dstatus in (200, 201, 202):
            print(f"         deploying -> https://{dbody.get('url', name + '.vercel.app')}")
        else:
            msg = dbody.get("error", {}).get("message", dbody) if isinstance(dbody, dict) else dbody
            print(f"         no first deploy (HTTP {dstatus}: {msg})")
            print(f"         open the project and click Redeploy, or push any commit")

    if not args.dry_run:
        print(f"\ncreated {len(made)}, skipped {len(skipped)}, failed {len(failed)}")
        print("\nNext, in each project's Settings:")
        print(f"  Git > Production Branch = {args.branch}")
        print("  Deployment Protection > Vercel Authentication = Only Preview Deployments")
        print("     (courses must be reachable without a login; QR codes depend on it)")
        if failed:
            print("\nFailed projects need a look:")
            for n, e in failed:
                print(f"  {n}: {e}")


if __name__ == "__main__":
    main()
