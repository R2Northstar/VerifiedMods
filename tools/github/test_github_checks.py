import unittest
import github_checks


class TestRetrieveTagInfo(unittest.TestCase):
    def test_tag_on_first_page(self):
        data = github_checks.retrieve_tag_info("1.0.9", "https://github.com/Dinorush/LTSRebalance")
        self.assertEqual(data['name'], "1.0.9")

    def test_tag_on_third_page(self):
        data = github_checks.retrieve_tag_info("0.10.6.3", "https://github.com/Dinorush/LTSRebalance")
        self.assertEqual(data['name'], "0.10.6.3")

    def test_unknown_tag(self):
        data = github_checks.retrieve_tag_info("unknown_tag", "https://github.com/Alystrasz/Alystrasz.Parkour")
        self.assertTrue(data == None)


if __name__ == "__main__":
    unittest.main()
