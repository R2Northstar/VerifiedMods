# Northstar verified mods

*[WORKING DOCUMENT]*

* What's this repo?
* How is this used in Northstar?
* Architecture of mods.json

### How to submit a mod for verification

* Ensure your mod is valid candidate to verification (is client-side required)
* Respects defined criteria:
  * does not embed malicious code
  * follows semantic versioning
  * source code is publicly available (link is on Thunderstore page) 
  * is automatically uploaded to Thunderstore
* Only then can you submit a PR
  * add mod entry to JSON file for new mods, or add version entry
  * don't forget checksum in any case
  * we'll review your PR ASAP

To avoid preventing users connecting to your server requiring a mod that's not been verified yet, we recommand you to update your mod following these steps (let's consider that your server requires a mod with version v0.1.0):
1. Publish the new version of your mod (v0.2.0 for instance) on Thunderstore;
2. Leave your server to use the old version (v0.1.0);
3. Submit a mod verification request of your new version (v0.2.0);
4. Switch your server to using v0.2.0 once it has been verified.

### How to verify a mod

* Check if semver is respected
* Check Thunderstore webpage
  * Ensure source link is present
  * Ensure packages are automatically uploaded to Thunderstore
* Manually download Thunderstore archive
* Browse all code for malicious stuff
* In JSON document update:
  * Check Thunderstore prefix is correct
  * Compare checksum with the one included in the PR
* Accept PR