#!/usr/bin/env python3
"""Git clean filter: remove publisher abstracts from chapter JSON before it is committed.

The working copy keeps the abstracts; the repository stores the JSON without them.
Configured in .git/config as filter.noabstract.clean and applied via .gitattributes.
Abstracts can be re-fetched by DOI from Europe PMC.
"""
import json
import sys

raw = sys.stdin.buffer.read()
try:
    data = json.loads(raw.decode('utf-8'))
except Exception:
    sys.stdout.buffer.write(raw)
    sys.exit(0)

if isinstance(data, dict) and isinstance(data.get('papers'), list):
    for p in data['papers']:
        if isinstance(p, dict):
            p.pop('abstract', None)
    sys.stdout.buffer.write(json.dumps(data, ensure_ascii=False, indent=1).encode('utf-8'))
else:
    sys.stdout.buffer.write(raw)
