import sys
from urllib.request import urlopen
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
        print(f'Verifying "{mod}":')

        # Build GitHub API link
        words = manifesto[mod]['Repository'].split('/')
        tags_url = f"https://api.github.com/repos/{words[-2]}/{words[-1]}/tags"

        # Check all mod versions one-by-one
        for version in manifesto[mod]['Versions']:
            print(f'  -> v{version['Version']}:')

            ## Check whether commit exists
            distant_version = retrieve_tag_info(version['Version'], tags_url)
            local_hash = version['CommitHash']

            ### Compare manifesto commit hash with repository hash
            if local_hash == distant_version['commit']['sha']:
                print(f"  Commit hash: ✔️")
            else:
                sys.exit(f"  Commit hash: ❌ (hash comparison failed)")
        print()


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
        url = f'{repository_url}?page={i}'
        response = urlopen(url)
        tags_data = json.loads(response.read())

        # If page is empty, it means the tag couldn't be found
        if len(tags_data) == 0:
            raise LookupError('Tag not found.')

        # If there's one matching result, we found the tag!
        matching_distant_versions = list(filter(lambda v: v['name'] == tag_name, tags_data))
        if len(matching_distant_versions) == 1:
            return matching_distant_versions[0]
        i += 1

if __name__ == "__main__":
    verify_all_mod_versions()
