import hashlib
import json5
import os
import re
import sys
import urllib.request
import zipfile

def fetch_archive(url, destination):
    urllib.request.urlretrieve(url, destination)

def check_archive(archive_name, expected_hash) -> bool:
    if not os.path.exists(archive_name):
        print('\tArchive not found.')
        return False

    h = hashlib.sha256()
    with open(archive_name, 'rb') as fh:
        while True:
            data = fh.read(4096)
            if len(data) == 0:
                break
            else:
                h.update(data)

    ok = expected_hash == h.hexdigest()
    if not ok:
        print(f"\tExpected <{expected_hash}>")
        print(f"\tReceived <{h.hexdigest()}>")
    return ok

def check_mod_name(archive_name, expected_name) -> bool:
    zip = zipfile.ZipFile(archive_name)
    mod_manifest_files = list(filter(lambda f: os.path.basename(f) == 'mod.json', zip.namelist()))

    # We don't handle archives with multiple mods for now
    if len(mod_manifest_files) > 1:
        print('  ⚠️ Multiple mod.json files were found in the archive, skipping verification step.')
        return True

    # Compare JSON name and verified-mods.json name
    data = zip.read(mod_manifest_files[0])
    manifest = json5.loads(data)
    ok = manifest['Name'] == expected_name
    if not ok:
        print(f"\tExpected <{expected_name}>")
        print(f"\tReceived <{manifest['Name']}>")
    return ok


if __name__ == "__main__":
    # tests
    url = "https://gcdn.thunderstore.io/live/repository/packages/cat_or_not-AmpedMobilepoints-0.0.7.zip"
    checksum = "b411368b17df6ab8b4179c121b0a9452cd5a88a50c0fc9fd790fda882b2c5189"
    name = "cat_or_not.AmpedMobilepoint"
    archive_name = "archive.zip"

    # methods
    fetch_archive(url, archive_name)
    check_archive(archive_name, checksum)
    check_mod_name(archive_name, name)
