#!/usr/bin/env python3
"""Rebuild assets.json from every .zip sitting in this folder.

Drop a zip in, run this, then commit and push.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "intelliriffer/MM-PLUGIN-MANAGER-REPO"
BRANCH = "main"

zips = sorted(f for f in os.listdir(HERE)
              if f.lower().endswith(".zip") and not f.startswith("."))
if not zips:
    raise SystemExit("No .zip files in this folder - assets.json left alone.")

assets = [{"name": f,
           "bytes": os.path.getsize(os.path.join(HERE, f)),
           "url": "https://raw.githubusercontent.com/%s/%s/%s" % (REPO, BRANCH, f)}
          for f in zips]

with open(os.path.join(HERE, "assets.json"), "w") as fh:
    json.dump({"assets": assets}, fh, indent=2)
    fh.write("\n")

print("assets.json lists %d asset%s:" % (len(assets), "" if len(assets) == 1 else "s"))
for a in assets:
    print("  %-32s %10d bytes" % (a["name"], a["bytes"]))
