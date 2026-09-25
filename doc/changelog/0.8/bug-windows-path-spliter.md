# Windows path splitter bug (0.8)
Before this bug was fixed, paths in both the `PYTHONPATH` and `PASHMAKPATH` environment variables were split on `:`.

Windows uses `:` for determining drives (`C:/...`).

The separator is now `;`, fixing the issue on Windows.

> Patch: GH-133
