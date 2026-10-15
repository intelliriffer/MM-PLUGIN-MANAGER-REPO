#!/usr/bin/env python3
"""Rebuild assets.json from every .zip in the assets folder.

Drop a zip into assets/, run this, then commit and push.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = "assets"                 # the zips live in their own folder, so the root stays tidy
REPO = "intelliriffer/MM-PLUGIN-MANAGER-REPO"
BRANCH = "main"

where = os.path.join(HERE, FOLDER)
zips = []
if os.path.isdir(where):
    zips = sorted(f for f in os.listdir(where)
                  if f.lower().endswith(".zip") and not f.startswith("."))
if not zips:
    raise SystemExit("No .zip files in the %s folder - assets.json left alone." % FOLDER)

assets = [{"name": f,
           "bytes": os.path.getsize(os.path.join(where, f)),
           "url": "https://raw.githubusercontent.com/%s/%s/%s/%s" % (REPO, BRANCH, FOLDER, f)}
          for f in zips]

with open(os.path.join(HERE, "assets.json"), "w") as fh:
    json.dump({"assets": assets}, fh, indent=2)
    fh.write("\n")

print("assets.json lists %d asset%s:" % (len(assets), "" if len(assets) == 1 else "s"))
for a in assets:
    print("  %-32s %10d bytes" % (a["name"], a["bytes"]))
