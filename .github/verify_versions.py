import sys
from urllib.request import urlopen
import json

def verify_all_mod_versions():
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
                print('  ✔️ v{}'.format(version['Version']))
            else:
                sys.exit('  ❌ v{} (hash comparison failed)'.format(version['Version']))

def retrieve_tag_info(tag_name, repository_url):
    i = 1
    while True:
        url = '{}?page={}'.format(repository_url, i)
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