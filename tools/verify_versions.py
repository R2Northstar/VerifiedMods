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

        # Check all mod versions one-by-one
        for version in manifesto[mod]['Versions']:
            print(f' (v{version["Version"]}):')

            # 1. Run checks against mod host

            ## 1.1. Check whether tag was published
            distant_info = github_checks.retrieve_tag_info(version['Version'], manifesto[mod]['Repository'])
            if distant_info == None:
                print(f"  • VCS tag published: ❌")
                sys.exit(1)
            print(f"  • VCS tag published: ✔️")

            ## 1.2. Check whether commit is properly declared
            local_hash = version['CommitHash']
            distant_hash = github_checks.get_commit_hash(distant_info)
            if local_hash == distant_hash:
                print(f"  • Commit hash: ✔️")
            else:
                print(f"  • Commit hash: ❌ (hash comparison failed)")
                sys.exit(2)

            # 2. Check zip archive

            ## 2.1. Check archive checksum
            dest = '/tmp/archive.zip'
            archive_checks.fetch_archive(version['DownloadLink'], dest)
            if not archive_checks.check_archive(dest, version['Checksum']):
                print(f'  • Checksum comparison: ❌')
                sys.exit(3)
            print(f"  • Checksum comparison: ✔️")

            ## 2.2. Check mod name
            if not archive_checks.check_mod_name(dest, mod):
                print(f'  • Name comparison: ❌')
                sys.exit(4)
            print('  • Name comparison: ✔️')


if __name__ == "__main__":
    verify_all_mod_versions()
