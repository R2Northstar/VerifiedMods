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


class TestBuildTagUrl(unittest.TestCase):
    def test_build_url(self):
        input = "https://github.com/Dinorush/LTSRebalance"
        expected = "https://api.github.com/repos/Dinorush/LTSRebalance/tags"
        r = github_checks.build_tags_url(input)
        self.assertEqual(r, expected)

    def test_build_url_2(self):
        input = "https://github.com/catornot/AmpedMobilepoints"
        expected = "https://api.github.com/repos/catornot/AmpedMobilepoints/tags"
        r = github_checks.build_tags_url(input)
        self.assertEqual(r, expected)

    def test_build_gitlab_url(self):
        input = "https://gitlab.com/Dinorush/LTSRebalance"
        expected = None
        r = github_checks.build_tags_url(input)
        self.assertEqual(r, expected)

    def test_build_wrong_url(self):
        input = "https://this.com/is/wrong"
        expected = None
        r = github_checks.build_tags_url(input)
        self.assertEqual(r, expected)

    def test_build_wrong_url_2(self):
        input = "https://github.com/Dinorush"
        expected = None
        r = github_checks.build_tags_url(input)
        self.assertEqual(r, expected)


if __name__ == "__main__":
    unittest.main()
