# Windows non-relative import bug (0.8)
If you write something like this in `0.8.1` or older versions in Windows systems:

```bash
import $__dir__ + '/some/file.pashm'
```

you will get a error that says invalid path:

```
C:\my-app\C:\my-app\some/file.pashm
```

you expect for this path:

```
C:\my-app\some/file.pashm
```

but the path is <br>
`C:\my-app\C:\my-app\some/file.pashm`. 
actually, the `C:\my-app` is repeated 2 times.

Now, the import path is relative with current working directory instead of the main file directory.
The bug was related to checking relative/non-relative paths. this check was checking first
character of the path. if that is `/`, means it is a non-relative path. but in windows,
paths will be started with `C:...`, and bug was from this subject.
