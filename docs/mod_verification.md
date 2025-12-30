# How to verify a mod

Wanna help us verify mods? Cool! Here's how to do it:

1. Check the mod's webpage:
  * Ensure there's a link to source code repository.
2. Download zip archive:
  * Ensure mod version is correctly updated compared to previous submitted version;
  * Browse all code for malicious stuff.
3. In JSON document update:
  * Manually checksum archive, and ensure hash is the same with the one included in the PR;
  * Ensure "CommitHash" value is a valid hash on the mod's repository.

If everything seems good to you, you can merge the pull request, officially marking the mod as verified!

However, if you have any doubt during any of the above steps, don't hesitate to start discussion with mod author in the current pull request on GitHub.
