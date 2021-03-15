# Windows path spliter bug (0.8)
Before the patch for this bug, paths was splited by `:` character.
For both `PYTHONPATH` and `PASHMAKPATH` environment variables.

Windows uses `:` for determining drives (`C:/...`).

Now, the spliter is changed to `;` and bug is fixed for windows.

> Patch: GH-133
