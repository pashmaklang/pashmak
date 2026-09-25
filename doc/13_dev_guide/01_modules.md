# Builtin Modules
One of the most common ways to contribute to Pashmak is by developing built-in modules. A large part of Pashmak's functionality is provided by built-in modules rather than the interpreter core.

For example, `os` and `sys` are built-in modules.

Source code of them are in `src/<module-name>/`.

For example, when we import `os` (`import @os`), its source code is in `src/os/__init__.pashm`.
When you import `sys.path`, its source code is in `src/sys/path.pashm`.

In general, when we import `foo.bar.baz`, we import either `src/foo/bar/baz.pashm` or `src/foo/bar/baz/__init__.pashm`.

To add a module, create a directory named after it, such as `src/mymodule`, then add its files using the structure described above.

After changing or adding a module, run `make module` or `make all` to bundle it. Bundling puts the Pashmak scripts' contents into `src/core/modules.py`, where the interpreter core can access them as Python code.

### Set the namespace
When adding a module, put its code inside a namespace. For example, if you create `mymodule`, write your code between `namespace mymodule` and `endns`. This keeps modules separate.

## STDLIB
The standard library (stdlib) contains functions, classes, and other items that are available
without importing a module. Like other modules, it is imported automatically when a program starts.

Content of this is in `src/stdlib/`.
The module's contents are split across several files, such as `stdlib.obj` and `stdlib.func`.
