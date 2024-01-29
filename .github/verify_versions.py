import sys
from urllib.request import urlopen
import json

def verify_all_mod_versions():
    # Load local manifesto file
    f = open('verified-mods.json')
    manifesto = json.load(f)

    for mod in manifesto:
        print('Verifying "{}":'.format(mod))

        # Build GitHub API link and fetch distant tags list
        words = manifesto[mod]['Repository'].split('/')
        tags_url = "https://api.github.com/repos/{}/{}/tags".format(words[-2], words[-1])
        response = urlopen(tags_url) 
        tags_data = json.loads(response.read())

        # Check all mod versions one-by-one
        for version in manifesto[mod]['Versions']:
            local_hash = version['CommitHash']
            matching_distant_versions = list(filter(lambda v: v['name'] == version['Version'], tags_data))

            # There should be only one matching version
            if len(matching_distant_versions) != 1:
                sys.exit('  ❌ v{} (unknown distant version)'.format(version['Version']))
            
            # Compare manifesto commit hash with repository hash
            distant_version = matching_distant_versions[0]
            if local_hash == distant_version['commit']['sha']:
                print('  ✔️ v{}'.format(version['Version']))
            else:
                sys.exit('  ❌ v{} (hash comparison failed)'.format(version['Version']))

if __name__ == "__main__":
    verify_all_mod_versions()
