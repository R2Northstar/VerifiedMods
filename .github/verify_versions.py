import os
import sys
import unittest
from urllib.request import Request, urlopen
import json

def verify_all_mod_versions():
    """
    Ensure all mod versions are properly declared to GitHub.

    For each mod entry of this repository's manifesto, this method will fetch information
    from GitHub API and compare declared SHA ("CommitHash" member) to GitHub information,
    to ensure tracability of verified mods.
    """

    # Load local manifesto file
    f = open('verified-mods.json')
    manifesto = json.load(f)

    for mod in manifesto:
        print('Verifying "{}":'.format(mod))

        # Build GitHub API link
        words = manifesto[mod]['Repository'].split('/')
        tags_url = "https://api.github.com/repos/{}/{}/tags".format(words[-2], words[-1])

        # Check all mod versions one-by-one
        for version in manifesto[mod]['Versions']:
            distant_version = retrieve_tag_info(version['Version'], tags_url)
            local_hash = version['CommitHash']
            
            # Compare manifesto commit hash with repository hash
            if local_hash == distant_version['commit']['sha']:
                print('\t✔️  v{}'.format(version['Version']))
            else:
                sys.exit('\t❌  v{} (hash comparison failed)'.format(version['Version']))


def retrieve_tag_info(tag_name, repository_url):
    """
    Retrieves tag information from distant API.

    Since the GitHub API is paginated, (*i.e.* it does not list all data in a single page,
    but rather serves pages holding 30 elements maximum), we need to browse all pages
    until either the tag is found or the page is empty, meaning we didn't find the tag.
    Page browsing is done by updating the `page` URL argument (`?page=1`, `?page=2` etc).

    @param tag_name: the name of the mod release
    @param repository_url: API URL used to access mod's tags data
    @return: tag data, including commit SHA signature
    """

    i = 1
    while True:
        url = '{}?page={}'.format(repository_url, i)
        req = Request(url)

        token = os.getenv('GITHUB_TOKEN')
        print("Using token {}", token)
        req.add_header('authorization', 'Bearer {}'.format(token))

        response = urlopen(req).read()
        tags_data = json.loads(response.read())

        # If page is empty, it means the tag couldn't be found
        if len(tags_data) == 0:
            raise LookupError('Tag not found.')

        # If there's one matching result, we found the tag!
        matching_distant_versions = list(filter(lambda v: v['name'] == tag_name, tags_data))
        if len(matching_distant_versions) == 1:
            return matching_distant_versions[0]
        i += 1


class TestRetrieveTagInfo(unittest.TestCase):
    def test_tag_on_first_page(self):
        data = retrieve_tag_info("1.0.9", "https://api.github.com/repos/Dinorush/LTSRebalance/tags")
        self.assertEqual(data['name'], "1.0.9")
    
    def test_tag_on_third_page(self):
        data = retrieve_tag_info("0.10.6.3", "https://api.github.com/repos/Dinorush/LTSRebalance/tags")
        self.assertEqual(data['name'], "0.10.6.3")
    
    def test_unknown_tag(self):
        with self.assertRaises(LookupError) as context:
            retrieve_tag_info("unknown_tag", "https://api.github.com/repos/Alystrasz/Alystrasz.Parkour/tags")
        self.assertTrue('Tag not found.' in str(context.exception))

    def run(self):
        self.test_tag_on_first_page()
        self.test_tag_on_third_page()
        self.test_unknown_tag()
        print("Tests done!")


# By default, running this script will invoke the `verify_all_mod_versions` method.
# You can execute `retrieve_tag_info` tests by running `python .github\verify_versions.py test`.
if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "test":
        TestRetrieveTagInfo().run()
    else:
        verify_all_mod_versions()