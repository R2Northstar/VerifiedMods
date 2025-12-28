import sys
import json
from archive import archive_checks
from github import github_checks


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
        print(f'\nVerifying "{mod}":')

        # Build GitHub API link
        words = manifesto[mod]['Repository'].split('/')
        tags_url = f"https://api.github.com/repos/{words[-2]}/{words[-1]}/tags"

        # Check all mod versions one-by-one
        for version in manifesto[mod]['Versions']:
            print(f' (v{version["Version"]}):')

            ## Check whether commit exists
            distant_version = github_checks.retrieve_tag_info(version['Version'], tags_url)
            local_hash = version['CommitHash']

            ### Compare manifesto commit hash with repository hash
            if local_hash == distant_version['commit']['sha']:
                print(f"  • Commit hash: ✔️")
            else:
                print(f"  • Commit hash: ❌ (hash comparison failed)")
                sys.exit(1)

            ## Check archive checksum
            dest = '/tmp/archive.zip'
            archive_checks.fetch_archive(version['DownloadLink'], dest)
            if not archive_checks.check_archive(dest, version['Checksum']):
                print(f'  • Checksum comparison: ❌')
                sys.exit(2)
            print(f"  • Checksum comparison: ✔️")

            ## Check mod name
            if not archive_checks.check_mod_name(dest, mod):
                print(f'  • Name comparison: ❌')
                sys.exit(3)
            print('  • Name comparison: ✔️')


if __name__ == "__main__":
    verify_all_mod_versions()
