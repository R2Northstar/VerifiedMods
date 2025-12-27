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


if __name__ == "__main__":
    unittest.main()
