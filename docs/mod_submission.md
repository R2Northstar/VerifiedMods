# How to submit a mod for verification

##### Note before you start

To avoid preventing users connecting to your server requiring a mod that's not been verified yet, we recommand you to update your mod following these steps (let's consider that your server requires a mod with version v0.1.0):
1. Publish the new version of your mod (v0.2.0 for instance) on Thunderstore;
2. Leave your server to use the old version (v0.1.0);
3. Submit a mod verification request of your new version (v0.2.0);
4. Switch your server to using v0.2.0 once it has been verified.

## Criteria

For your mod to be successfully verified, it MUST follow the following set of rules:
* **do not embed malicious code (obviously)**: your mod is going to be downloaded to people's computers, so it shouldn't do something nasty (*e.g.* mining some cryptos without users' knowledge);
* **source code is public**: your mod's Thunderstore webpage should display a link to your source code repository;
* **Thunderstore upload is automatic**: we don't want people to manually upload mods on Thunderstore since they could induce malicious code that's not in source code repository; we recommand you to use the [AnActualEmerald mod template](https://github.com/GreenTF/NSModTemplate), which integrates a continuous integration job that will automatically build your mod and upload it to Thunderstore each time you create a GitHub release;
* **verified dependencies**: if your mod depends on other mods, they're gonna be downloaded to people's computers too, so they have to be verified as well.

Are all of the above criteria OK? Well, time to create a pull request!

After forking this repository, update the `verified-mods.json` file with content related to your mod:
* add a new entry if your mod hasn't been verified yet;
* add a new version entry in your mod's entry otherwise.

In either case, don't forget to add the new archive's checksum and commit hash to the `verified-mods.json` file.

## Checksum

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
