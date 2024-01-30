import unittest
import verify_versions

class TestRetrieveTagInfo(unittest.TestCase):
    def test_tag_on_first_page(self):
        data = verify_versions.retrieve_tag_info("1.0.9", "https://api.github.com/repos/Dinorush/LTSRebalance/tags")
        self.assertEqual(data['name'], "1.0.9")
    
    def test_tag_on_third_page(self):
        data = verify_versions.retrieve_tag_info("0.10.6.3", "https://api.github.com/repos/Dinorush/LTSRebalance/tags")
        self.assertEqual(data['name'], "0.10.6.3")
    
    def test_unknown_tag(self):
        with self.assertRaises(LookupError) as context:
            verify_versions.retrieve_tag_info("unknown_tag", "https://api.github.com/repos/Alystrasz/Alystrasz.Parkour/tags")
        self.assertTrue('Tag not found.' in str(context.exception))

class TestModVerification(unittest.TestCase):
    def test_verification(self):
        self.assertTrue(verify_versions.verify_all_mod_versions())

if __name__ == "__main__":
    unittest.main()
