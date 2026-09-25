# Windows non-relative import bug (0.8)
If you wrote code like this on Windows in version `0.8.1` or earlier:

```bash
import $__dir__ + '/some/file.pashm'
```

you would get an invalid-path error:

```
C:\my-app\C:\my-app\some/file.pashm
```

You expect this path:

```
C:\my-app\some/file.pashm
```

Instead, the path was `C:\my-app\C:\my-app\some/file.pashm`; `C:\my-app` was repeated twice.

The import path was resolved relative to the current working directory instead of the main file's directory.
The bug came from how relative and absolute paths were detected. The check looked at the first
character of the path and treated `/` as indicating an absolute path. On Windows, however,
paths can start with a drive prefix such as `C:...`.
