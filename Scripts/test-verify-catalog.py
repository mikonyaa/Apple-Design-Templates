#!/usr/bin/env python3
"""Exercise the public CLI on disposable, deliberately broken catalogs."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CatalogGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'catalog'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def run_gate(self, *args):
        return subprocess.run([sys.executable, str(ROOT / 'Scripts/verify-catalog.py'), '--root', str(self.root), *args], capture_output=True, text=True)

    def edit_manifest(self, mutation):
        path = self.root / 'catalog.json'
        data = json.loads(path.read_text())
        mutation(data)
        path.write_text(json.dumps(data, ensure_ascii=False))

    def assert_rejected(self, field):
        result = self.run_gate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(field, result.stdout + result.stderr)

    def test_clean_catalog_passes_without_network(self):
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('OFFLINE PASS', result.stdout)

    def test_wrong_release_tag_is_rejected(self):
        self.edit_manifest(lambda d: d['products'][0]['release'].update(tag='latest'))
        self.assert_rejected('release.tag')

    def test_deleted_preview_is_named(self):
        (self.root / 'Assets/liquid-glass-tab-bars-poster.png').unlink()
        self.assert_rejected('Assets/liquid-glass-tab-bars-poster.png')

    def test_russian_version_drift_is_rejected(self):
        path = self.root / 'README.ru.md'
        path.write_text(path.read_text().replace('Released 1.0.3', 'Released 9.9.9', 1))
        self.assert_rejected('README.ru.md')

    def test_missing_cli_issue_route_is_rejected(self):
        path = self.root / '.github/ISSUE_TEMPLATE/config.yml'
        path.write_text(path.read_text().replace('https://github.com/mikonyaa/ResizeLint/issues/new/choose', 'https://example.com/missing'))
        self.assert_rejected('ResizeLint')

    def test_media_over_budget_is_rejected(self):
        with (self.root / 'Assets/banner.png').open('ab') as stream:
            stream.write(b'X' * 5301010)
        self.assert_rejected('media.max_bytes')

    def test_claim_without_provenance_is_rejected(self):
        self.edit_manifest(lambda d: d['products'][0]['claims'][0].update(evidence=[]))
        self.assert_rejected('claims[0].evidence')

    def test_unsafe_relative_path_is_rejected(self):
        self.edit_manifest(lambda d: d['products'][0]['preview'].update(path='../outside.png'))
        self.assert_rejected('preview.path')

    def test_unknown_slug_is_rejected(self):
        self.edit_manifest(lambda d: d['products'][0].update(slug='unknown'))
        self.assert_rejected('products.slug')

    def test_missing_cli_security_policy_is_rejected(self):
        path = self.root / 'SECURITY.md'
        path.write_text(path.read_text().replace('https://github.com/mikonyaa/ResizeLint/blob/main/SECURITY.md', 'https://example.com/missing'))
        self.assert_rejected('security_policy')

    def test_extra_marketing_guarantee_is_rejected(self):
        path = self.root / 'README.md'
        path.write_text(path.read_text() + '\nFully verified on physical devices.\n')
        self.assert_rejected('README.md')

    def test_inaccessible_network_is_unverified_and_read_only(self):
        before = (self.root / 'catalog.json').read_bytes()
        result = self.run_gate('--online', '--api-base', 'http://127.0.0.1:1', '--network-timeout', '0.2')
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn('UNVERIFIED', result.stdout)
        self.assertNotIn('ONLINE PASS', result.stdout)
        self.assertEqual(before, (self.root / 'catalog.json').read_bytes())


if __name__ == '__main__':
    unittest.main(verbosity=2)
