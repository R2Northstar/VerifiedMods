import archive_checks
import os
import unittest
import urllib


class TestFetchArchive(unittest.TestCase):
    destination = '/tmp/archive.zip'

    def tearDown(self):
        if os.path.exists(self.destination):
            os.remove(self.destination)

    def test_fetch_archive(self):
        url = "https://gcdn.thunderstore.io/live/repository/packages/cat_or_not-AmpedMobilepoints-0.0.7.zip"
        archive_checks.fetch_archive(url, self.destination)
        self.assertTrue(os.path.exists(self.destination))

    def test_fetch_unexisting_archive(self):
        url = "http://i.do.not.exi.st"
        with self.assertRaises(urllib.error.URLError) as context:
            archive_checks.fetch_archive(url, self.destination)
        self.assertTrue('Name or service not known' in str(context.exception))


class TestChecksumArchive(unittest.TestCase):
    destination = '/tmp/archive.zip'

    def setUp(self):
        url = "https://gcdn.thunderstore.io/live/repository/packages/cat_or_not-AmpedMobilepoints-0.0.7.zip"
        self.archive = archive_checks.fetch_archive(url, self.destination)

    def tearDown(self):
        if os.path.exists(self.destination):
            os.remove(self.destination)

    def test_checksum_archive(self):
        hash = "b411368b17df6ab8b4179c121b0a9452cd5a88a50c0fc9fd790fda882b2c5189"
        r = archive_checks.check_archive(self.destination, hash)
        self.assertTrue(r)

    def test_wrong_checksum_archive(self):
        hash = "not a hash"
        r = archive_checks.check_archive(self.destination, hash)
        self.assertFalse(r)

    def test_checksum_unexisting_archive(self):
        os.remove(self.destination)
        hash = "b411368b17df6ab8b4179c121b0a9452cd5a88a50c0fc9fd790fda882b2c5189"
        r = archive_checks.check_archive(self.destination, hash)
        self.assertFalse(r)

if __name__ == "__main__":
    unittest.main()
