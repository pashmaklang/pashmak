# Windows non-relative import bug (0.8)
If you write something like this in `0.8.1` or older versions in Windows systems:

```bash
import $__dir__ + '/some/file.pashm'
```

you will get an error that says invalid path:

```
C:\my-app\C:\my-app\some/file.pashm
```

You expect this path:

```
C:\my-app\some/file.pashm
```

But the path is `C:\my-app\C:\my-app\some/file.pashm`. Actually, the `C:\my-app` is repeated 2 times.

Now, the import path is relative with current working directory instead of the main file directory.
The bug was related to checking relative/non-relative paths. This check was checking first
character of the path. If that is `/`, means it is a non-relative path. But in windows,
paths start with `C:...`, and bug was from this subject.
