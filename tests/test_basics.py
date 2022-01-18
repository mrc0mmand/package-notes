# SPDX-License-Identifier: CC0-1.0

import unittest
from importlib import resources

from _generate_package_notes import generate_section

class TestGeneratedOutput(unittest.TestCase):
    def test_fedora_package(self):
        input = dict(type='rpm', name='package', version='1.2.3', architecture='noarch', osCpe='CPE')
        text = '\n'.join(generate_section(input))
        expected = resources.read_text('resources', 'fedora-package.ld')
        self.assertEqual(text, expected[:-1])

    def test_very_short(self):
        input = dict(type='deb', name='A', version='0', architecture='x', osCpe='o')
        text = '\n'.join(generate_section(input))
        expected = resources.read_text('resources', 'very-short.ld')
        self.assertEqual(text, expected[:-1])

    def test_very_short_rw(self):
        input = dict(type='deb', name='A', version='0', architecture='x', osCpe='o')
        text = '\n'.join(generate_section(input, readonly=False))
        expected = resources.read_text('resources', 'very-short-rw.ld')
        self.assertEqual(text, expected[:-1])

    def test_fedora_long_name(self):
        input = dict(type='rpm',
                     name='rust-plist+enable_unstable_features_that_may_break_with_minor_version_bumps-devel',
                     version='200:1.3.1~rc1.post2^final3',
                     architecture='ppc64le',
                     osCpe='cpe:/o:fedoraproject:fedora:35',
                     debugInfoUrl='https://somewhere.on.the.internet.there.is.a.server.which.is.never.wrong/query')
        text = '\n'.join(generate_section(input))
        expected = resources.read_text('resources', 'fedora-long-name.ld')
        self.assertEqual(text, expected[:-1])

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(stream=sys.stdout, verbosity=3))
