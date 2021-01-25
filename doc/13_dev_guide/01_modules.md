# Builtin Modules
The most Customary way for development in Pashmak project, is Developing builtin modules. A bug part of Pashmak is the builtin modules, not interpreter core.

For example, `os`, `sys`... are builtin modules.

Source code of them are in `src/<module-name>/`.

For example, when we import `os`(`import @os`), Source code of that is in `src/os/__init__.pashm`.
Also when you import `sys.path`, source code is `src/sys/path.pashm`.

Totally, when we import `foo.bar.baz`, we are importing `src/foo/bar/baz.pashm` or `src/foo/bar/baz/__init__.pashm`.

If you want to add a module, create a directory with name of module. for example `src/mymodule`. Then, under the above structure, put the files.

After changing/adding a module, you should run `make module` or `make all` to mix them. Mixing the modules means that puting content of this pashmak scripts into file `src/core/modules.py` To be accessible by interpreter core as a python file.

### Set the namespace
If you are adding a new module, surely write your code inside a namespace. for example, if you created `mymodule`, write your code between `namespace mymodule ... endns`. This makes modules splited.

## STDLIB
Stdlib or Standard library, is a very important modules. Some functions/classes/etc in Pashmak are accessible
without importing any module. They are in stdlib. stdlib is a module like all of other modules,
But will be imported by default while program starts.

Content of this is in `src/stdlib/`.
Also content of this module is seprated in several files.
(For example `stdlib.obj`, `stdlib.func`...).
