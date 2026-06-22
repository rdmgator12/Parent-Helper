#!/usr/bin/env python3
"""Retroactive full-history PHI scan.

The pre-commit hook only guards NEW commits. This walks EVERY blob in EVERY commit
reachable from all refs and applies the same pattern gate, so you can audit a repo's
existing history (public repos keep deleted content forever). Read-only — it reports,
never rewrites.

    python hooks/scan-history.py

Exit 0 = clean, 1 = potential PHI found (review the listed blobs). Patterns and the
fixture allowlist are imported from phi_hook.py — single source of truth.
"""

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from phi_hook import (  # noqa: E402
    FIXTURE_PATH,
    scan_binaries,
    scan_credentials,
    scan_data_files,
    scan_name_phi,
    scan_slug,
)


def _git(args):
    return subprocess.run(["git", *args], capture_output=True)


def main():
    commits = _git(["rev-list", "--all"]).stdout.decode().split()
    if not commits:
        print("No commits to scan.")
        return 0

    seen = set()
    fails = []
    blobs = 0
    for c in commits:
        listing = _git(["ls-tree", "-r", "--name-only", c]).stdout.decode()
        for f in listing.splitlines():
            if not f or (c, f) in seen:
                continue
            seen.add((c, f))

            # Path/filename gates always apply (credentials are never ok, even in fixtures).
            for hit in scan_credentials([f]):
                fails.append((c, "credential", hit))
            is_fixture = bool(FIXTURE_PATH.search(f))
            if not is_fixture:
                for hit in scan_binaries([f]):
                    fails.append((c, "binary", hit))
                for hit in scan_data_files([f]):
                    fails.append((c, "data", hit))
                if scan_slug([f]):  # patient-name slug in the path itself
                    fails.append((c, "slug-path", f))

            # Content patterns skip fixture files (synthetic by design) and binaries.
            if is_fixture:
                continue
            raw = _git(["show", f"{c}:{f}"]).stdout
            try:
                lines = raw.decode("utf-8").splitlines()
            except UnicodeDecodeError:
                continue  # binary blob — covered by the extension gates above
            blobs += 1
            for line, _ in scan_slug(lines):
                fails.append((c, "slug", f"{f}: {line[:80]}"))
            for line, _ in scan_name_phi(lines):
                fails.append((c, "name_phi", f"{f}: {line[:80]}"))

    if not fails:
        print(
            f"✅ clean — scanned {len(seen)} path-instances "
            f"({blobs} text blobs) across {len(commits)} commits; no PHI patterns."
        )
        return 0

    print(f"⚠️  {len(fails)} potential PHI hit(s) across history:")
    for c, kind, detail in fails[:200]:
        print(f"  {c[:8]} [{kind}] {detail}")
    if len(fails) > 200:
        print(f"  ... and {len(fails) - 200} more")
    return 1


if __name__ == "__main__":
    sys.exit(main())
