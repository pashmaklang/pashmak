# Module path system
The module path system lets you load Pashmak scripts as modules. For example, suppose you have a directory named `/var/lib/pashmak_modules` containing a Pashmak script named `/var/lib/pashmak_modules/mymodule.pashm`. How can you make this script available as a module?

For example, to import that module:

```bash
import '@mymodule'
```

To do this, add the `/var/lib/pashmak_modules` directory to the Pashmak path:

```bash
PASHMAKPATH=/var/lib/pashmak_modules pashmak my_program.pashm
```

To add a directory to the Pashmak path, set the `PASHMAKPATH` environment variable:

```
PASHMAKPATH=/path/to/first/dir;/path/to/another/dir;/another/dir2...
```

You can separate paths with `;`.

The Pashmak interpreter then loads modules from those directories. It treats files with the `.pashm` extension as modules. For example, if a file is named `my_module.pashm`, you can import it with `import "@my_module"`.

You can also import a directory as a module. For example, suppose `/usr/lib/pashmak_modules` is in the module path and contains a directory named `mymodule`. When you import `"@mymodule"`, Pashmak uses `/usr/lib/pashmak_modules/mymodule/__init__.pashm` as the module's main file. You can import other scripts from that file.

For example:

#### __init__.pashm:

```bash
import $__dir__ + '/core.pashm'
import $__dir__ + '/another-file.pashm'
# ...
# or whatever you want to do
```

### Default paths
The default module paths in Pashmak are:

- `<home-directory>/.local/lib/pashmak_modules`
- `/usr/lib/pashmak_modules` (only in UNIX systems)

### Adding module paths at runtime (sys.path module)
The `sys.path` namespace in the `sys` module lets you add module paths at runtime.
You can use it to add directories to the path and load modules from them in your program.

For example:

```bash
import @sys
# or
import @sys.path # only loads sys.path contents

sys.path.add('/home/parsa/my-directory');
```

In the code above, `/home/parsa/my-directory` is added to the module path. You can then import modules from that directory.

For example, suppose `/home/parsa/my-directory/mylib.pashm` is a module. We can import it like this:

```bash
import '@sys.path'

sys.path.add('/home/parsa/my-directory');

import '@mylib'

# do whatever you want
```

This system is useful when you want to load local modules from a directory in your project.

For example, if your project contains a `pashmak_modules` directory with local libraries, you can add it to the module path at the start of your code:

```bash
import $__dir__ + '/pashmak_modules/'

# now i can import libraries from pashmak_modules directory
```

You can also get a list of module paths:

```bash
import '@sys.path'

$module_paths = sys.path.list()

println($module_paths)
```

output:

```
['/path1', '/path2', '...']
```

### Importing sub directories/files from module path
You can import a subdirectory or file from a directory in your module path.

For example, we added `/some/path` directory to our path.
There is a directory named `/some/path/dir1`.
There is also a file named `/some/path/dir1/__init__.pashm`,
and `/some/path/dir1/other.pashm`.

Now, we can import them:

```bash
import @dir1 # imports `/some/path/dir1/__init__.pashm`
import @dir1.other # imports `/some/path/dir1/other.pashm`
import @dir1.subdir.somefile # imports `/some/path/dir1/subdir/somefile.pashm`
```
