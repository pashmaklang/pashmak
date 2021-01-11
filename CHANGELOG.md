# Pashmak Changelog

## (0.7) next release

- added `import_run` and `import_run_once` functions (GH-84)
- added cli feature to run modules (GH-84)

## 0.6.5 (2021-1-11)

- added module `string` (GH-82)
- fixed a bug in module path system about `$__dir__` and `$__file__`

## 0.6.4 (2021-1-10)

- fixed import directory bug (GH-79)
- added importing sub directories/files in modules loaded from module path system (GH-80)
- removed cli option `-m|--modules`

## 0.6.3 (2021-1-9)

- some optimizations in module importing system (GH-78)
- fixed a bug in importing scripts related to file path contains `"` or `'` (GH-78)
- fixed `$__ismain__` alwasy is True bug (GH-78)

## 0.6.2 (2021-1-7)

- added `urllib` to imported python standard modules (GH-75)
- added `platform`, `sqlite3.dump`, `sqlite3.dbapi2` to imported python standard modules
- added `pashmak.zen()` (GH-77)

## 0.6.1 (2021-1-5)

- also show error type and message in end of rendered error frames
- imported `sqlite3` python module (GH-69)
- $this variable exists while calling static method bug in class is fixed (GH-71)
- fixed try-endtry variable error handling bug (GH-73)

## 0.6 (2021-1-4)

#### New features
- added **Class** system
- added consts system
- added a feature to use mem symbol `^` in eval, now you can run `my_function ^ + ' something else'`
- added syntax feature to put `()` in function call syntax, for example `println("hello world")` or `my_func(1, 2)`
- added `if..elif..else` statement
- added `return` command for functions
- added `import_once` function
- added a syntax to handle dictonary item value assigning, now we can run `$my_dict["item"] = "value"`
- added inline function calling feature, for example `println(my_func_or_command(another_command_as_arg()))`
- added general variable `$__ismain__`
- added **Jit** compiler
- added `fopen` alias for `open` function
- added `py_load_file` function to load python scripts as object (GH-35)
- added python `json`, `socket`, `socketserver`, `http`, `base64`, `math`, `pprint`, `subprocess` library support
- added `function.{list,delete,exists}`, `class.{list,delete,exists}` super functions
- added `out_*` magic functions to handle program stdout output in advance level
- added multiline using `\` character in end of lines
- added complicated declaring class and function
- added `__namespace__()` function to return current namespace as string
- added `os` module (GH-45)
- added `while` loop system
- added new functions to `random` module (GH-49)
- added function `var_dump()`
- added `ns` alias for `namespace` keyword (GH-51)
- added `format_args()` function
- added `webserver` module
- added `math` module
- added `perror()` function
- added `printf()` function

#### Bug Fixes
- fixed a bug in `eval` function
- fixed a bug in module path system
- fixed some bugs in error raising system
- fixed lot of interpreter internal bugs and some optimizations
- fixed a bug in function declaration syntax
- fixed a bug in `$__dir__` and `$__file__` variables in function
- fixed a bug in multi importing syntax
- fixed some bugs in `end*` commands
- fixed import command bug while using `()`
- blocked using literal chars in names(function/class/namespace
- fixed namespace function bug while calling another function in that namespace
- fixed a bug in function variable isolation

#### Removed
- deleted `loop` and `while` functions
- deleted `out`, `fread`, `include` and `fwrite` commands because they was very low level and are not needed
- deleted `$var = ^ command` syntax(use `$var = command()` instead of that)
- deleted `@file` module(use python file api instead of that)
- removed `chdir` function (GH-45)
 -removed `cwd` function (use `os.cwd()` instead of that)

#### Other changes
- change default `RuntimeError` name to the real python exception name in exception system
- some optimizations in mem eval parser
- some optimizations in interpreter code
- changed raised error data from dictonary to `Error` object
- allow using `;` and `#` inside string without `\`
