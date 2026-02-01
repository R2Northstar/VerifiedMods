# Northstar verified mods

This repository lists all mods that have been manually verified by the community, and as such can be downloaded automatically by Northstar clients.

This verified mods enables players to join servers that require custom content such as new maps or new gamemodes.

Verified mods are listed in the present `verified-mods.json` file, using following format:
* Key is mod's name (contained in its `mod.json` manifest's "Name" key);
* Body holds two fields:
  * "Repository" contains the link of the repository hosting the source code of the mod;
  * "Versions" contains a list of version (for the current mod) that have been verified.

Each version contains the following attributes:
* "Version" is the current version identifier (using the `x.y.z` format);
* "CommitHash" is the Git commit associated to the current version;
* "DownloadLink" is the direct download link of the version archive;
* "Checksum" is the SHA256 hash of the version archive;
* "Platform" is the origin of the version, used by the launcher to know how to install downloaded mod.

---

Submitting a mod?

- [How to submit a mod for verification](./docs/mod_submission.md)
- [Check that your submission is valid](./docs/mod_check.md)

Accepting new mods?

- [How to review mod verification requests](./docs/mod_verification.md)
