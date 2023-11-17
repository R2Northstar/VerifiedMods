# Northstar verified mods

*[WORKING DOCUMENT]*

This repository lists all mods that have been manually verified by the community, and as such can be downloaded automatically by Northstar clients.

This verified mods enables players to join servers that require custom content such as new maps or new gamemodes.

Verified mods are listed in the present `verified-mods.json` file, using following format:
* Key is mod's name (contained in its `mod.json` manifest's "Name" key);
* Body holds two fields:
  * "DependencyPrefix" contains the string that allows Northstar to retrieve mods on Thunderstore;
  * "Versions" contains a list of version (for the current mod) that have been verified.

## How to submit a mod for verification

Before starting to submit your mod for verification, please ensure that it is a valid candidate to mod verification! Only mods required by a server to be client-side can be verified.

*Good examples:*
* Maps;
* Gamemodes.

*Bad examples:*
* Skins (only required client-side);
* Audio overrides;
* UI changes;
* Custom skyboxes.

##### Note before you start

To avoid preventing users connecting to your server requiring a mod that's not been verified yet, we recommand you to update your mod following these steps (let's consider that your server requires a mod with version v0.1.0):
1. Publish the new version of your mod (v0.2.0 for instance) on Thunderstore;
2. Leave your server to use the old version (v0.1.0);
3. Submit a mod verification request of your new version (v0.2.0);
4. Switch your server to using v0.2.0 once it has been verified.

### Criteria

For your mod to be successfully verified, it MUST follow the following set of rules:
* **do not embed malicious code (obviously)**: your mod is going to be downloaded to people's computers, so it shouldn't do something nasty (*e.g.* mining some cryptos without users' knowledge);
* **follow semantic versioning**: when updating your mod, you should update its version accordingly: increase patch version for small fixes, minor version for new compatible features, major version for breaking changes. Please read [semver.org](https://semver.org/) for more details;
* **source code is public**: your mod's Thunderstore webpage should display a link to your source code repository;
* **Thunderstore upload is automatic**: we don't want people to manually upload mods on Thunderstore since they could induce malicious code that's not in source code repository; we recommand you to use the [AnActualEmerald mod template](https://github.com/GreenTF/NSModTemplate>), which integrates a continuous integration job that will automatically build your mod and upload it to Thunderstore each time you create a GitHub release;
* **verified dependencies**: if your mod depends on other mods, they're gonna be downloaded to people's computers too, so they have to be verified as well.

Are all of the above criteria OK? Well, time to create a pull request!

After forking this repository, update the `verified-mods.json` file with content related to your mod:
* add a new entry if your mod hasn't been verified yet;
* add a new version entry in your mod's entry otherwise.

In either case, don't forget to add the new archive's checksum to the `verified-mods.json` file.

### Checksum

To make sure that the mod downloaded by Northstar is the same that has been verified, we use cryptographic hashes of Thunderstore mod archives (think of them as "file signatures"); if the content of the archive is changed, its hash will change too.

There are different hash algorithms; this mod verification mechanism uses the [SHA256](https://www.movable-type.co.uk/scripts/sha256.html) algorithm.

To submit your mod for verification, you need to provide the hash for the corresponding Thunderstore zip archive.

On Windows, it's done using the `certutil` executable (in Powershell or cmd):
```shell
certutil -hashfile my_thunderstore_mod_archive.zip SHA256
```

On Linux, it's even easier:
```shell
sha256sum my_thunderstore_mod_archive.zip
```
---

Once you're done, submit your pull request! We'll review your mod as soon as possible, so be on the lookout for comments!

## How to verify a mod

Wanna help us verify mods? Cool! Here's how to do it:

1. Check the mod's Thunderstore webpage:
  * Ensure there's a link to source code repository;
  * Ensure packages are automatically uploaded to Thunderstore.
2. Download Thunderstore zip archive:
  * Ensure semver is respected (*i.e.* mod version is correctly updated);
  * Browse all code for malicious stuff.
3. In JSON document update:
  * Check Thunderstore prefix is correct (must equal "Dependency string" on Thunderstore webpage without version information);
  * Manually checksum archive, and ensure hash is the same with the one included in the PR.

If everything seems good to you, you can merge the pull request, officially marking the mod as verified!

However, if you have any doubt during any of the above steps, don't hesitate to start discussion with mod author in the current pull request on GitHub.
