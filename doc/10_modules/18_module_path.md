# Module path system
module path is a system to add pashmak scripts as modules to pashmak. for example, you have an directory named `/var/lib/pashmak_modules` and there is an file named `/var/lib/pashmak_modules/mymodule.pashm`. this file is a pashmak script. now, how to add that pashmak script to pashmak as module?

for example, we want to import that module:

```bash
import '@mymodule'
```

to do this, you have to add directory `/var/lib/pashmak_modules` to pashmak path:

```bash
PASHMAKPATH=/var/lib/pashmak_modules pashmak my_program.pashm
```

to add an directory to pashmak path, you have to set that directory to environment variable `PASHMAKPATH`:

```
PASHMAKPATH=/path/to/first/dir:/path/to/another/dir:/another/dir2...
```

you can seprate paths with `:`.

next, pashmak interpreter loads modules from that directories. how? pashmak loads pashmak files with `.pashm` extension as module. for example, if name of file is `my_module.pashm`, you can import that with `import "@my_module"`.

also you can import an directory as module. for example, `/usr/lib/pashmak_modules` is in the module path. and there is a directory in `/usr/lib/pashmak_modules/mymodule/`. if you import `import "@mymodule"`, pashmak uses `/usr/lib/pashmak_modules/mymodule/__init__.pashm` file in that directory as module main file. you can load another scripts of your module in this file.

for example:

#### __init__.pashm:

```bash
import $__dir__ + '/core.pashm'
import $__dir__ + '/another-file.pashm'
# ...
# or whatever you want to do
```

### Default paths
the default module paths in pashmak are:

- `<home-directory>/.local/lib/pashmak_modules`
- `/usr/lib/pashmak_modules` (only in UNIX systems)

### Show list of available modules
to see list of available modules, run this command:

```bash
pashmak -m
# or
pashmak --modules
```

### Adding module paths at runtime (sys.path module)
there is an namespace named `sys.path` in the `sys` module, this module is for adding new module paths at the runtime.
with this feature, you can add another directories to your path and load modules from them in your program.

for example:

```bash
import @sys
# or
import @sys.path # only loads sys.path contents

sys.path.add('/home/parsa/my-directory');
```

in above code, directory `/home/parsa/my-directory` will be added to the module path. after this action, you can import modules of that directory.

for example, we have `/home/parsa/my-directory/mylib.pashm` module and we can import that:

```bash
import '@sys.path'

sys.path.add('/home/parsa/my-directory');

import '@mylib'

# do whatever you want
```

this system is very helpful, specialy when you want to add your local modules from an directory in your project.

for example, i have an project and there is an directory named `pashmak_modules` contains local library. i can add this directory to module path in my code start point:

```bash
import $__dir__ + '/pashmak_modules/'

# now i can import libraries from pashmak_modules directory
```

also you can get list of module paths:

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
You can import sub dir/file of a section in your module path.

For example, we added `/some/path` directory to our path.
There is a directory named `/some/path/dir1`.
Also there is a file named `/some/path/dir1/__init__.pashm`,
and `/some/path/dir1/other.pashm`.

Now, we can import them:

```bash
import @dir1 # imports `/some/path/dir1/__init__.pashm`
import @dir1.other # imports `/some/path/dir1/other.pashm`
import @dir1.subdir.somefile # imports `/some/path/dir1/subdir/somefile.pashm`
```
