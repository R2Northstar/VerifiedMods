# Mod check

This document describes what can be done to ensure your mod submission is valid.

**tldr:**
1. Get the URI of your raw proposal;
2. Tell your game to use it to retrieve mod info;
3. Check your logs to see whether your mod appears there;
4. Download mod manually.

#### Get the URI of your raw proposal

When you opened a pull request to the repository, you had to previously update the `verified-mods.json` file to add information about your mod.
To make your game use the file you modified as source of truth to download mods, you need to retrieve its URL.
On GitHub, this can be done by clicking the "raw" button on the web file view.

*Example:*

I want to use my version of the manifesto, hosted on https://github.com/Alystrasz/VerifiedMods.

1. I go to the https://github.com/Alystrasz/VerifiedMods webpage;
2. I click the `verified-mods.json` file to display it;
3. I click the "Raw" button, just above the file;
4. I can then copy the raw URL of the file, in my case https://raw.githubusercontent.com/Alystrasz/VerifiedMods/refs/heads/main/verified-mods.json

#### Pass custom manifesto to game

To tell your game client to use a custom manifesto file, you need to pass the previously retrieved URL as a [launch argument](https://docs.northstar.tf/Wiki/using-northstar/launch-arguments).
The name of the argument is `-customverifiedurl`.

*Example:*

If my manifesto URL is https://raw.githubusercontent.com/Alystrasz/VerifiedMods/refs/heads/main/verified-mods.json, I must pass the following launch argument to my game:

```text
-customverifiedurl=https://raw.githubusercontent.com/Alystrasz/VerifiedMods/refs/heads/main/verified-mods.json
```

#### Check whether the manifesto is correctly registered by the game

Start your game with the launch argument set up, and look at the latest log file (located in `<profile>/logs`).
You can check whether the game got the argument by looking for the following entry:

```text
Found custom verified mods URL in command line argument:
```
followed by the URL you specified.

*(if you read "Custom verified mods URL not found in command line arguments, using default URL.", it means you set up the launch argument incorrectly.)*

*Example:*

```text
[2025-12-24] [17:49:40] [NORTHSTAR] [info] Registering ConCommand reload_models
[2025-12-24] [17:49:41] [NORTHSTAR] [info] Registering Convar spewlog_enable
[2025-12-24] [17:49:41] [NORTHSTAR] [info] Mod downloader initialized
[2025-12-24] [17:49:41] [NORTHSTAR] [info] Found custom verified mods URL in command line argument: https://raw.githubusercontent.com/Alystrasz/VerifiedMods/refs/heads/main/verified-mods.json
[2025-12-24] [17:49:41] [NORTHSTAR] [info] Registering ConCommand reload_plugins
[2025-12-24] [17:49:41] [NORTHSTAR] [info] Registering Convar ns_prefer_datatable_from_disk
```

#### Make the game fetch the mods manifesto

**You must connect to multiplayer lobby before doing this!**

To check whether your manifesto is correctly formatted and properly lists your mod, you can tell your game client to retrieve the manifesto from the Internet:
1. Open a console;
2. Enable script execution: `sv_cheats 1`;
3. Trigger the fetching: `script NSFetchVerifiedModsManifesto()`

If everything is fine, your game client should retrieve the mods manifesto, and load it in memory, logging as follows:
```text
[2025-12-24] [17:54:41] [NORTHSTAR] [info] Executing SERVER script code NSFetchVerifiedModsManifesto()
[2025-12-24] [17:54:41] [NORTHSTAR] [info] sq_compilebuffer returned SQRESULT_NULL
[2025-12-24] [17:54:41] [NORTHSTAR] [info] sq_call returned SQRESULT_NULL
[2025-12-24] [17:54:41] [NORTHSTAR] [info] Mods list successfully fetched.
[2025-12-24] [17:54:41] [NORTHSTAR] [info] Loading mods configuration...
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "cat_or_not.AmpedMobilepoint"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "GeckoEidechse.Headhunter"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "Odd.s2space"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "Parkour"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "Dinorush's LTS Rebalance"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "HotPotato"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "nyami.mp_brick"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "Berdox.mp_chroma_null_surf"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "Berdox.surf_game_mode"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "Berdox.gauntlet_framework"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "skrubslayer.mp_sanctuary"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "Neko's Onslaught"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] ==> Loaded configuration for mod "3030 Repeater Apex port"
[2025-12-24] [17:54:41] [NORTHSTAR] [info] Done loading verified mods list.
```

*(if your mod does not appear here, it means you set up something wrong.)*

#### Download mod through the console

**You must connect to multiplayer lobby before doing this!**

If the previous steps went well, you should be able to download any of the listed mods.
This is done running the following command in the console: `script NSDownloadMod( "<modName>", "<modVersion>" )`
Checking your `<profile>/runtime/remote/mods` directory, downloaded mods should appear there.

*Example:*

```text
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Executing SERVER script code NSDownloadMod("cat_or_not.AmpedMobilepoint", "0.0.7")
[2025-12-24] [18:07:53] [NORTHSTAR] [info] sq_compilebuffer returned SQRESULT_NULL
[2025-12-24] [18:07:53] [NORTHSTAR] [info] sq_call returned SQRESULT_NULL
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Fetching mod archive from https://gcdn.thunderstore.io/live/repository/packages/cat_or_not-AmpedMobilepoints-0.0.7.zip
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Downloading archive to C:/users/steamuser/Temp/cat_or_not-AmpedMobilepoints-0.0.7.zip
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Mod archive successfully fetched.
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Expected checksum: b411368b17df6ab8b4179c121b0a9452cd5a88a50c0fc9fd790fda882b2c5189
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Computed checksum: b411368b17df6ab8b4179c121b0a9452cd5a88a50c0fc9fd790fda882b2c5189
[2025-12-24] [18:07:53] [NORTHSTAR] [info] => R2Northstar/runtime/remote/mods/cat_or_not-AmpedMobilepoints-0.0.7/icon.png
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Parent directory does not exist, creating it.
[2025-12-24] [18:07:53] [NORTHSTAR] [info] => R2Northstar/runtime/remote/mods/cat_or_not-AmpedMobilepoints-0.0.7/README.md
[2025-12-24] [18:07:53] [NORTHSTAR] [info] => R2Northstar/runtime/remote/mods/cat_or_not-AmpedMobilepoints-0.0.7/manifest.json
[2025-12-24] [18:07:53] [NORTHSTAR] [info] => R2Northstar/runtime/remote/mods/cat_or_not-AmpedMobilepoints-0.0.7/mods/catornot.AmpedMobilepoints/mod.json
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Parent directory does not exist, creating it.
[2025-12-24] [18:07:53] [NORTHSTAR] [info] => R2Northstar/runtime/remote/mods/cat_or_not-AmpedMobilepoints-0.0.7/mods/catornot.AmpedMobilepoints/keyvalues/playlists_v2.txt
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Parent directory does not exist, creating it.
[2025-12-24] [18:07:53] [NORTHSTAR] [info] => R2Northstar/runtime/remote/mods/cat_or_not-AmpedMobilepoints-0.0.7/mods/catornot.AmpedMobilepoints/mod/resource/mobilepoint_localisation_english.txt
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Parent directory does not exist, creating it.
[2025-12-24] [18:07:53] [NORTHSTAR] [info] => R2Northstar/runtime/remote/mods/cat_or_not-AmpedMobilepoints-0.0.7/mods/catornot.AmpedMobilepoints/mod/scripts/vscripts/gamemodes/cl_gamemode_mcp.gnut
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Parent directory does not exist, creating it.
[2025-12-24] [18:07:53] [NORTHSTAR] [info] => R2Northstar/runtime/remote/mods/cat_or_not-AmpedMobilepoints-0.0.7/mods/catornot.AmpedMobilepoints/mod/scripts/vscripts/gamemodes/cl_gamemode_cp.nut
[2025-12-24] [18:07:53] [NORTHSTAR] [info] => R2Northstar/runtime/remote/mods/cat_or_not-AmpedMobilepoints-0.0.7/mods/catornot.AmpedMobilepoints/mod/scripts/vscripts/gamemodes/_gamemode_mcp.gnut
[2025-12-24] [18:07:53] [NORTHSTAR] [info] => R2Northstar/runtime/remote/mods/cat_or_not-AmpedMobilepoints-0.0.7/mods/catornot.AmpedMobilepoints/mod/scripts/vscripts/gamemodes/sh_gamemode_mcp.gnut
[2025-12-24] [18:07:53] [NORTHSTAR] [info] Done cleaning after downloading cat_or_not.AmpedMobilepoint.
```
