"""Stdlib unittest suite for phi_hook v1.4. Zero deps.

Run from repo root:
    python -m unittest discover -s hooks/tests -v
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from phi_hook import (
    BINARY_ALLOW_PATH,
    BINARY_RISK,
    CRED_FILE,
    DISEASE_ALLOWLIST,
    FIXTURE_PATH,
    LABEL_THEN_NAME,
    NAME_THEN_PHI,
    PATH_SLUG,
    RECORD_ROW,
    added_lines,
    run_scan,
    scan_binaries,
    scan_credentials,
    scan_data_files,
    scan_name_phi,
    scan_slug,
    strip_allowlisted,
)


class TestPattern1Slug(unittest.TestCase):
    """Pattern 1 — Maieutic/Themis/Nostos path slug with patient-name shape."""

    def test_slug_matches_maieutic_path(self):
        line = "+ Maieutic/Cases/2026-04-21-john-smith-a/"
        self.assertEqual(len(scan_slug([line])), 1)

    def test_slug_matches_themis_path(self):
        line = "Themis/cases/2026-03-10-jane-doe-x"
        self.assertEqual(len(scan_slug([line])), 1)

    def test_slug_matches_nostos_path(self):
        line = "Nostos/Patients/2026-02-01-baby-jones-q"
        self.assertEqual(len(scan_slug([line])), 1)

    def test_disease_allowlist_saves_kawasaki(self):
        line = "Maieutic/2026-04-21-kawasaki-disease-a"
        self.assertEqual(scan_slug([line]), [])

    def test_disease_allowlist_saves_dka(self):
        line = "Nostos/2026-04-21-dka-resident-guide"
        self.assertEqual(scan_slug([line]), [])

    def test_slug_ignores_unrelated_path(self):
        line = "src/2026-04-21-john-smith-a/file.py"
        self.assertEqual(scan_slug([line]), [])


class TestPattern2NamePhi(unittest.TestCase):
    """Pattern 2 — proper-noun name adjacent to PHI field."""

    def test_name_then_dob_fires(self):
        line = "+John Smith DOB 1990-01-01"
        self.assertEqual(len(scan_name_phi([line])), 1)

    def test_name_then_mrn_fires(self):
        line = "Mary Jones MRN 1234567"
        self.assertEqual(len(scan_name_phi([line])), 1)

    def test_label_patient_name_fires(self):
        line = "patient name: Jane Smith"
        self.assertEqual(len(scan_name_phi([line])), 1)

    def test_label_plaintiff_fires(self):
        line = "plaintiff: Robert Brown"
        self.assertEqual(len(scan_name_phi([line])), 1)

    def test_label_defendant_fires(self):
        line = 'defendant: "Alice Green"'
        self.assertEqual(len(scan_name_phi([line])), 1)

    def test_clean_line_does_not_fire(self):
        line = "This is a clean line with no PHI."
        self.assertEqual(scan_name_phi([line]), [])

    def test_ralph_self_name_alone_passes(self):
        line = "Reviewed by Ralph Martello, MD."
        self.assertEqual(scan_name_phi([line]), [])

    def test_ralph_name_does_not_immunize_same_line_phi(self):
        line = "Ralph Martello reviewed John Smith DOB 1990-01-01."
        self.assertEqual(len(scan_name_phi([line])), 1)

    def test_bracket_placeholder_alone_passes(self):
        line = "Template: [Patient Name, DOB]"
        self.assertEqual(scan_name_phi([line]), [])

    def test_bracket_placeholder_does_not_immunize_same_line_phi(self):
        line = "Template: [Patient Name, DOB] real: Mary Jones DOB 1980-05-05"
        self.assertEqual(len(scan_name_phi([line])), 1)


class TestPattern3Credentials(unittest.TestCase):
    """Pattern 3 — credential / env files."""

    def test_root_env_blocks(self):
        self.assertEqual(scan_credentials([".env"]), [".env"])

    def test_nested_env_blocks(self):
        self.assertEqual(scan_credentials(["app/.env"]), ["app/.env"])

    def test_env_production_blocks(self):
        self.assertEqual(scan_credentials([".env.production"]), [".env.production"])

    def test_env_local_blocks(self):
        self.assertEqual(scan_credentials([".env.local"]), [".env.local"])

    def test_env_example_passes(self):
        self.assertEqual(scan_credentials([".env.example"]), [])

    def test_env_sample_passes(self):
        self.assertEqual(scan_credentials([".env.sample"]), [])

    def test_env_template_passes(self):
        self.assertEqual(scan_credentials([".env.template"]), [])

    def test_credentials_json_blocks(self):
        self.assertEqual(scan_credentials(["credentials.json"]), ["credentials.json"])

    def test_secrets_yaml_blocks(self):
        self.assertEqual(scan_credentials(["secrets.yaml"]), ["secrets.yaml"])

    def test_secrets_yml_blocks(self):
        self.assertEqual(scan_credentials(["secrets.yml"]), ["secrets.yml"])

    def test_private_key_blocks(self):
        self.assertEqual(
            scan_credentials(["server_private_key.pem"]), ["server_private_key.pem"]
        )

    def test_dot_env_extension_does_not_block(self):
        """File named foo.env (dotenv extension, not dotfile) is NOT a credential file."""
        self.assertEqual(scan_credentials(["foo.env"]), [])

    def test_unrelated_file_passes(self):
        self.assertEqual(scan_credentials(["README.md", "src/main.py"]), [])


class TestPattern4Binaries(unittest.TestCase):
    """Pattern 4 — PHI-risk binary files outside allowlist."""

    def test_root_pdf_blocks(self):
        self.assertEqual(scan_binaries(["leak.pdf"]), ["leak.pdf"])

    def test_root_docx_blocks(self):
        self.assertEqual(scan_binaries(["doc.docx"]), ["doc.docx"])

    def test_root_jpg_blocks(self):
        self.assertEqual(scan_binaries(["photo.jpg"]), ["photo.jpg"])

    def test_root_dicom_blocks(self):
        self.assertEqual(scan_binaries(["scan.dcm"]), ["scan.dcm"])

    def test_assets_pdf_passes(self):
        self.assertEqual(scan_binaries(["assets/diagram.pdf"]), [])

    def test_docs_png_passes(self):
        self.assertEqual(scan_binaries(["docs/screenshot.png"]), [])

    def test_references_pdf_passes(self):
        self.assertEqual(scan_binaries(["references/paper.pdf"]), [])

    def test_screenshots_png_passes(self):
        self.assertEqual(scan_binaries(["screenshots/ui.png"]), [])

    def test_tests_fixture_binary_passes(self):
        self.assertEqual(scan_binaries(["tests/fixtures/sample.pdf"]), [])

    def test_icons_dir_NOT_allowlisted(self):
        """Per v1.4 design: icons/favicons/logos are tight gate, not allowlisted."""
        self.assertEqual(scan_binaries(["icons/app.png"]), ["icons/app.png"])

    def test_text_file_not_flagged(self):
        self.assertEqual(scan_binaries(["README.md", "src/main.py"]), [])


class TestStripAllowlisted(unittest.TestCase):
    """v1.4 strip_allowlisted — allowlisted substrings stripped before name+PHI scan."""

    def test_strip_removes_self_name(self):
        out = strip_allowlisted("Ralph Martello attended.")
        self.assertNotIn("Ralph Martello", out)

    def test_strip_preserves_other_content(self):
        out = strip_allowlisted("Ralph Martello and John Smith.")
        self.assertIn("John Smith", out)

    def test_strip_removes_bracket_placeholder(self):
        out = strip_allowlisted("Use [Patient Name] here.")
        self.assertNotIn("[Patient Name]", out)

    def test_strip_self_name_case_sensitive(self):
        """Ralph self-name allowlist is case-sensitive — lowercase ralph martello should NOT match."""
        out = strip_allowlisted("ralph martello in lowercase.")
        self.assertIn("ralph martello", out)


class TestAddedLines(unittest.TestCase):
    """diff parser — only +lines, excluding +++ headers."""

    def test_includes_added_lines(self):
        diff = "+hello\n+world\n"
        self.assertEqual(added_lines(diff), ["+hello", "+world"])

    def test_excludes_removed_lines(self):
        diff = "+keep\n-drop\n"
        self.assertEqual(added_lines(diff), ["+keep"])

    def test_excludes_plus_plus_plus_header(self):
        diff = "+++ b/file.md\n+real content\n"
        self.assertEqual(added_lines(diff), ["+real content"])


class TestRunScanIntegration(unittest.TestCase):
    """End-to-end run_scan against representative file+diff pairs."""

    def test_clean_input_no_fails(self):
        result = run_scan(files=["README.md"], diff_lines=["+all clear here"])
        self.assertEqual(result, [])

    def test_credential_file_caught(self):
        result = run_scan(files=[".env"], diff_lines=[])
        kinds = [r[0] for r in result]
        self.assertIn("credential", kinds)

    def test_binary_file_caught(self):
        result = run_scan(files=["leak.pdf"], diff_lines=[])
        kinds = [r[0] for r in result]
        self.assertIn("binary", kinds)

    def test_name_phi_caught(self):
        result = run_scan(
            files=["notes.md"],
            diff_lines=["+John Smith DOB 1990-01-01"],
        )
        kinds = [r[0] for r in result]
        self.assertIn("name_phi", kinds)

    def test_multiple_violations_all_caught(self):
        result = run_scan(
            files=[".env", "leak.pdf"],
            diff_lines=["+patient name: Jane Smith"],
        )
        kinds = {r[0] for r in result}
        self.assertIn("credential", kinds)
        self.assertIn("binary", kinds)
        self.assertIn("name_phi", kinds)


class TestRegexShapes(unittest.TestCase):
    """Lightweight assertions on the compiled regex objects themselves."""

    def test_path_slug_compiles(self):
        self.assertIsNotNone(PATH_SLUG.search("Maieutic/Cases/2026-01-01-john-smith-a"))

    def test_disease_allowlist_is_case_insensitive(self):
        self.assertIsNotNone(DISEASE_ALLOWLIST.search("KAWASAKI"))

    def test_name_then_phi_compiles(self):
        self.assertIsNotNone(NAME_THEN_PHI.search("John Smith DOB"))

    def test_label_then_name_compiles(self):
        self.assertIsNotNone(LABEL_THEN_NAME.search('patient: "Jane Doe"'))

    def test_cred_file_compiles(self):
        self.assertIsNotNone(CRED_FILE.search(".env"))

    def test_binary_risk_extensions(self):
        for ext in ["pdf", "docx", "xlsx", "png", "jpg", "tiff", "dcm", "heic", "webp"]:
            self.assertIsNotNone(BINARY_RISK.search(f"file.{ext}"), ext)

    def test_binary_allow_path_matches_assets(self):
        self.assertIsNotNone(BINARY_ALLOW_PATH.search("assets/foo.png"))

    def test_fixture_path_matches_tests(self):
        self.assertIsNotNone(FIXTURE_PATH.search("tests/fixtures/case.md"))

    def test_fixture_path_matches_github(self):
        self.assertIsNotNone(FIXTURE_PATH.search(".github/workflows/lint.yml"))


class TestV15Pattern5DataFiles(unittest.TestCase):
    """v1.5 Pattern 5 — structured-data (.csv/.tsv/.psv) gate."""

    def test_csv_at_root_blocks(self):
        self.assertEqual(scan_data_files(["patient_list.csv"]), ["patient_list.csv"])

    def test_tsv_at_root_blocks(self):
        self.assertEqual(scan_data_files(["export.tsv"]), ["export.tsv"])

    def test_csv_under_fixtures_passes(self):
        self.assertEqual(scan_data_files(["tests/fixtures/sample.csv"]), [])

    def test_csv_under_docs_passes(self):
        self.assertEqual(scan_data_files(["docs/data.csv"]), [])

    def test_json_not_treated_as_data_file(self):
        self.assertEqual(scan_data_files(["package.json", "config/app.json"]), [])

    def test_run_scan_flags_data_kind(self):
        result = run_scan(files=["patients.csv"], diff_lines=[])
        self.assertIn("data", [r[0] for r in result])


class TestV15RecordRow(unittest.TestCase):
    """v1.5 — value-shaped record rows (name + DOB-value + id) evading literal labels."""

    def test_csv_record_row_caught(self):
        self.assertEqual(len(scan_name_phi(["John Smith,2015-03-01,00123456"])), 1)

    def test_tab_delimited_record_caught(self):
        self.assertEqual(len(scan_name_phi(["Mary Jones\t01/02/2015\t99887"])), 1)

    def test_slashed_dob_record_caught(self):
        self.assertEqual(len(scan_name_phi(["Robert Brown, 3/4/2016, 100200"])), 1)

    def test_prose_with_date_not_false_positive(self):
        # no trailing delimited id → not a record row
        self.assertEqual(scan_name_phi(["Meeting Notes 2026-01-15 with the team"]), [])

    def test_record_row_regex_present(self):
        self.assertIsNotNone(RECORD_ROW.search("Jane Doe,2014-06-01,55512"))


class TestV15NameShape(unittest.TestCase):
    """v1.5 — middle initials and apostrophes no longer evade Pattern 2."""

    def test_middle_initial_with_period(self):
        self.assertEqual(
            len(scan_name_phi(["patient: John A. Smith DOB 2015-03-01"])), 1
        )

    def test_middle_initial_no_period(self):
        self.assertEqual(len(scan_name_phi(["John A Smith MRN 1234567"])), 1)

    def test_apostrophe_name(self):
        self.assertEqual(
            len(scan_name_phi(["patient: Sean O'Brien DOB 2015-03-01"])), 1
        )

    def test_hyphenated_first_name(self):
        self.assertEqual(len(scan_name_phi(["Mary-Jane Watson DOB 1990-01-01"])), 1)

    def test_all_caps_acronym_not_a_name(self):
        # 'MRI Scan' must not read as a person name adjacent to a field
        self.assertEqual(scan_name_phi(["MRI Scan ordered, see DOB note"]), [])


class TestV15BracketStrip(unittest.TestCase):
    """v1.5 — bracket-placeholder strip no longer immunizes real bracketed PHI."""

    def test_real_phi_in_brackets_is_caught(self):
        self.assertEqual(
            len(scan_name_phi(["- [Jane Doe, DOB 2015-03-01, MRN 9988]"])), 1
        )

    def test_literal_placeholder_still_passes(self):
        self.assertEqual(scan_name_phi(["Template: [Patient Name, DOB]"]), [])

    def test_first_last_placeholder_passes(self):
        self.assertEqual(scan_name_phi(["Use [First Last] here."]), [])


class TestV15SlugTightening(unittest.TestCase):
    """v1.5 — disease allowlist requires BOTH tokens clinical; Pattern 1 scans paths."""

    def test_patient_plus_disease_token_still_flagged(self):
        self.assertEqual(
            len(scan_slug(["Maieutic/Cases/2026-04-21-johnson-asthma-r"])), 1
        )

    def test_two_clinical_tokens_still_allowlisted(self):
        self.assertEqual(scan_slug(["Maieutic/2026-04-21-kawasaki-disease-a"]), [])

    def test_pattern1_scans_file_path_via_run_scan(self):
        path = "Maieutic/Cases/2026-06-19-john-smith-x/dashboard.md"
        result = run_scan(files=[path], diff_lines=[], slug_paths=[path])
        self.assertIn("slug", [r[0] for r in result])


class TestV15CredentialBroadening(unittest.TestCase):
    """v1.5 — prefixed secrets files and secrets.json now caught."""

    def test_prefixed_secrets_yaml_blocks(self):
        self.assertEqual(
            scan_credentials(["config-secrets.yaml"]), ["config-secrets.yaml"]
        )

    def test_secrets_json_blocks(self):
        self.assertEqual(scan_credentials(["app-secrets.json"]), ["app-secrets.json"])

    def test_plain_secrets_yaml_still_blocks(self):
        self.assertEqual(scan_credentials(["secrets.yaml"]), ["secrets.yaml"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
