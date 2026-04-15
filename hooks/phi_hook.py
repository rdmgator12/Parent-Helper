"""PHI pre-commit hook — v1.4 (2026-04-15, Python).

Importable module. Entry point is `main()`. `pre-commit` is a thin wrapper.

Four-pattern gate:
1. Patient-name slugs in Maieutic/Themis/Nostos reasoning paths
2. Proper-noun name adjacent to PHI field (DOB/MRN/insurance/patient/plaintiff)
3. Credential files (.env, credentials.json, secrets.yml, *private_key*)
4. PHI-risk binary files (pdf/docx/xlsx/png/jpg/tif/dcm) outside allowlisted paths

Path allowlist skips synthetic-fixture directories:
  TestCase_*/ | fixtures/ | test_data/ | tests/fixtures/ |
  test-fixtures/ | scripts/test-* | scripts/demo-*

Install (per repo): ln -sf ../../hooks/pre-commit .git/hooks/pre-commit
Override: git commit --no-verify (discouraged)

Changelog:
  v1.4 — Extracted scan logic into importable module. Added Pattern 4
         (binary-file gate) with path allowlist (assets/docs/images/
         screenshots/references/static/public/.github). icons/favicons/
         logos deliberately NOT allowlisted — tight gate beats clean scan.
         Fixed .env.production regex bug (v1.3 had `$` anchor that broke
         alt-group matching). Allowlisted .env.example / .env.sample /
         .env.template. Replaced content-allowlist short-circuit with
         strip-before-match (self-name and bracket placeholder no longer
         immunize real PHI on the same line). Split CONTENT_ALLOWLIST:
         Ralph self-name is case-sensitive, bracketed placeholder keeps
         IGNORECASE. Pattern 1 (slug) now respects FIXTURE_PATH via
         main()'s pre-filter — lets the hook's own test file (which
         contains synthetic patient-name slugs) commit without
         --no-verify. Added stdlib unittest suite under hooks/tests/
         (42 tests, zero deps). Added hooks/scan-history.py for
         retroactive full-history scans.
  v1.3 — Dropped bare "name:" label trigger (matched CI workflow step
         names like "name: Use Node"). Kept specific labels: patient,
         plaintiff, defendant, patient name. Added path allowlist for
         .github/, CaseTemplate/, plugin/marketplace/package metadata.
         Added content allowlist for "Ralph Martello" (self-identity
         is not PHI per feedback_ralph_name_public_repos.md).
  v1.2 — Python rewrite. Proper word boundaries, testable patterns.
         Fixed alternation-grouping bug.
  v1.1 — Pattern 2 tightened (name+PHI-field) + fixture allowlist.
  v1.0 — Initial 3-pattern gate.
"""

import re
import subprocess
import sys

# ----- Pattern 1: Maieutic/Themis/Nostos path slug with patient-name shape
PATH_SLUG = re.compile(
    r"(?:[Mm]aieutic|[Tt]hemis|[Nn]ostos)"
    r"/[A-Za-z0-9_/-]+/\d{4}-\d{2}-\d{2}-[a-z]+-[a-z]+-[a-z]"
)

DISEASE_ALLOWLIST = re.compile(
    r"\b(kawasaki|dermatomyositis|crohns?|bromfed|adhd|incomplete|"
    r"respiratory|failure|syndrome|disease|treatment|resident|guide|"
    r"update|workup|optimization|pediatric|ddx|myositis|discharge|"
    r"hospital|emergency|dka|sepsis|bronchiolitis|asthma|pneumonia|"
    r"influenza|covid|case-update|pivot-protocol|mri|exam)\b",
    re.IGNORECASE,
)

# ----- Pattern 2: proper-noun name adjacent to PHI field
NAME_SHAPE = r"\b[A-Z][a-z]{1,20}[- ][A-Z][a-z]{1,20}\b"
PHI_FIELD = r"\b(DOB|MRN|dob|mrn|date[_ ]of[_ ]birth|insurance[_ ]?id)\b"

NAME_THEN_PHI = re.compile(NAME_SHAPE + r"[^A-Za-z\n]{0,60}" + PHI_FIELD)
LABEL_THEN_NAME = re.compile(
    r"\b(patient[\s_-]?name|plaintiff|defendant|patient)\b"
    r"[\s\'\"`:=]{1,10}"
    r"[\'\"`]?" + NAME_SHAPE
)

# ----- Content allowlist — known-safe proper-noun phrases
# Ralph's own name is case-sensitive (proper noun, not a substring match).
# Bracketed placeholders like [Patient Name, DOB] are template literals.
SELF_NAME_ALLOW = re.compile(r"\bRalph Martello\b")
BRACKET_PLACEHOLDER_ALLOW = re.compile(
    r"\[[A-Z][a-z]+ [A-Z][a-z]+(,[^\]]+)?\]",
    re.IGNORECASE,
)

# ----- Pattern 3: credential files
# .env, .env.production, .env.local are blocked.
# .env.example / .env.sample / .env.template are template files and pass.
# (v1.3 regex had a bug: `\.env($|\.)` + trailing `$` failed to match `.env.production`
#  because the outer `$` required end-of-string immediately after the alt group.)
CRED_FILE = re.compile(
    r"(^|/)("
    r"\.env(\.(?!(?:example|sample|template)\b)[^/]*)?|"
    r"credentials\.json|"
    r"secrets\.ya?ml|"
    r"[^/]*private_key[^/]*"
    r")$"
)

# ----- Pattern 4: PHI-risk binary extensions
# Any file of these types anywhere NOT under a binary allowlist path is blocked.
BINARY_RISK = re.compile(
    r"\.(pdf|docx?|xlsx?|pptx?|png|jpe?g|tiff?|dcm|dicom|heic|webp)$",
    re.IGNORECASE,
)
# Allowlisted locations for legitimate binaries (docs, research papers, architecture
# diagrams, license graphics, etc.). Paths matched anywhere in the file path.
BINARY_ALLOW_PATH = re.compile(
    r"(^|/)("
    r"assets/|docs/|doc/|images/|img/|screenshots/|references/|"
    r"\.github/|static/|public/"
    r")"
)
# NOTE: `icons/`, `favicons/`, `logos/` are deliberately NOT allowlisted.
# Tight binary gate > clean history scan. Legit icon commits use --no-verify.

# ----- Path allowlist for synthetic-fixture directories AND metadata files
FIXTURE_PATH = re.compile(
    r"(^|/)("
    r"TestCase_|tests?/|test_data/|test-fixtures/|"
    r"fixtures/|scripts/test[-_]|scripts/demo[-_]|scripts/smoke[-_]|"
    r"demo_cases\.ts|test-complex-case\.ts|"
    r"\.github/|"
    r"CaseTemplate/|"
    r"plugin\.json|marketplace\.json|package\.json|package-lock\.json|"
    r"LICENSE"
    r")"
)


def staged_files():
    r = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMRT"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [f for f in r.stdout.splitlines() if f]


def staged_diff(files):
    if not files:
        return ""
    r = subprocess.run(
        ["git", "diff", "--cached", "--"] + files,
        capture_output=True,
        text=True,
        check=True,
    )
    return r.stdout


def added_lines(diff_text):
    return [
        l
        for l in diff_text.splitlines()
        if l.startswith("+") and not l.startswith("+++")
    ]


def strip_allowlisted(line):
    """Remove allowlisted substrings (self-name, bracket placeholders) from a line
    before Pattern 2 matching. Prevents the escape hatch where a placeholder or
    self-name on the same line as real PHI would short-circuit the scan.

    Example: '[Patient Name]: <FIRST> <LAST>, DOB YYYY-MM-DD'
             → ': <FIRST> <LAST>, DOB YYYY-MM-DD'  (unstripped portion still
             feeds NAME_THEN_PHI when real shapes are present)
    """
    line = SELF_NAME_ALLOW.sub("", line)
    line = BRACKET_PLACEHOLDER_ALLOW.sub("", line)
    return line


def scan_slug(diff_lines):
    """Pattern 1. Input: iterable of raw diff lines. Returns [(line, match), ...]."""
    hits = []
    for line in diff_lines:
        for m in PATH_SLUG.finditer(line):
            if not DISEASE_ALLOWLIST.search(m.group(0)):
                hits.append((line.rstrip(), m.group(0)))
                break
    return hits


def scan_name_phi(diff_lines):
    """Pattern 2. Input: iterable of raw diff lines (already fixture-filtered).
    Returns [(line, match), ...].

    Allowlisted substrings (Ralph's self-name, bracket placeholders) are stripped
    before matching so they can't immunize real PHI that shares the same line.
    """
    hits = []
    for line in diff_lines:
        stripped = strip_allowlisted(line)
        hit = NAME_THEN_PHI.search(stripped) or LABEL_THEN_NAME.search(stripped)
        if hit:
            hits.append((line.rstrip(), hit.group(0)))
    return hits


def scan_credentials(files):
    """Pattern 3. Returns list of offending file paths."""
    return [f for f in files if CRED_FILE.search(f)]


def scan_binaries(files):
    """Pattern 4. Returns list of offending binary file paths outside allowlists."""
    hits = []
    for f in files:
        if not BINARY_RISK.search(f):
            continue
        if BINARY_ALLOW_PATH.search(f):
            continue
        if FIXTURE_PATH.search(f):
            continue
        hits.append(f)
    return hits


def run_scan(files, diff_lines):
    """Pure scan orchestrator. Returns list of (kind, detail, match) tuples.

    `diff_lines` should be the added-line set from non-fixture files only.
    Callers that need to apply Pattern 1 universally (e.g., the history scanner)
    should call scan_slug() directly.
    """
    fails = []
    for line, m in scan_slug(diff_lines):
        fails.append(("slug", line, m))
    for line, m in scan_name_phi(diff_lines):
        fails.append(("name_phi", line, m))
    for f in scan_credentials(files):
        fails.append(("credential", f, f))
    for f in scan_binaries(files):
        fails.append(("binary", f, f))
    return fails


def main():
    files = staged_files()
    if not files:
        return 0

    non_fixture = [f for f in files if not FIXTURE_PATH.search(f)]
    diff_nf = staged_diff(non_fixture) if non_fixture else ""

    fails = run_scan(
        files=files,
        diff_lines=added_lines(diff_nf),
    )

    if not fails:
        return 0

    slug_hits = [f for f in fails if f[0] == "slug"]
    name_hits = [f for f in fails if f[0] == "name_phi"]
    cred_hits = [f for f in fails if f[0] == "credential"]
    bin_hits = [f for f in fails if f[0] == "binary"]

    if slug_hits:
        print(
            "❌ pre-commit: possible patient-name slug in Maieutic/Themis/Nostos path:"
        )
        for _, line, _ in slug_hits[:5]:
            print(f"    {line[:140]}")
        print()
        print("   Reference cases by number + clinical topic only.")
        print("   Example: 'Maieutic Case 36 — MRI + exam DDx pivot dashboard'")
        print()

    if name_hits:
        print(
            "⚠️  pre-commit: proper-noun name adjacent to PHI field (DOB/MRN/insurance/patient):"
        )
        for _, line, _ in name_hits[:5]:
            print(f"    {line[:140]}")
        print()
        print("   If this is synthetic test data, move it under one of:")
        print("     TestCase_*/ | fixtures/ | test_data/ | tests/fixtures/")
        print("     scripts/test-* | scripts/demo-*")
        print("   Or rename identifiers to obvious placeholders (TEST_USER_001, etc.).")
        print("   If this is Ralph's own name or a known public figure, override:")
        print("     git commit --no-verify")
        print()

    if cred_hits:
        print("❌ pre-commit: credential/env file in staged diff:")
        for _, f, _ in cred_hits:
            print(f"    {f}")
        print()

    if bin_hits:
        print("❌ pre-commit: PHI-risk binary file in staged diff:")
        for _, f, _ in bin_hits:
            print(f"    {f}")
        print()
        print("   Move legitimate binaries under one of:")
        print("     assets/ | docs/ | images/ | references/ | screenshots/")
        print("   Or for test fixtures: tests/ | fixtures/ | TestCase_*/")
        print("   Otherwise: confirm no patient info is in the file, then:")
        print("     git commit --no-verify")
        print()

    print("Commit blocked. See feedback_no_phi_in_repos.md for policy.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
