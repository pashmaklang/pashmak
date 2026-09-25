# Pashmak Changelog

## 0.9 (2025-12-7)

#### New Features
- Added the module `regex` (GH-129)
- Added the `$os.pwd` variable in the `os` module (GH-158)
- Added *Traits* for OOP system (GH-164, GH-165)
- Added the keyword `end` to close blocks instead of `endif`, `endwhile`... the previous keywords still work (GH-171)

## 0.8.5 (2021-5-31)

#### New Features
- Added support for the `list` datatype for the `import` syntax (GH-155)

## 0.8.4 (2021-4-21)

#### Improvements
- Only some improvements in the interpreter core

## 0.8.3 (2021-3-15)

#### Bug Fixes
- Fixed the Windows path splitter bug and changed it from `:` to `;` ([read more](doc/changelog/0.8/bug-windows-path-spliter.md), GH-133)

## 0.8.2 (2021-3-14)

#### Bug Fixes
- Fixed a critical bug in Windows while importing scripts in non-relative mode like `$__dir__ + '/something...'` ([read more](doc/changelog/0.8/bug-windows-non-relative-import.md), GH-132)

## 0.8.1 (2021-3-2)

#### New Features
- Added the command `clear` for the shell (GH-123)

#### Bug Fixes
- Fixed the shared frame variables bug (accessibility of parent frame variables in a child frame). (GH-124)

## 0.8 (2021-2-28)

#### NOTE: This release is fully backward compatible with `0.7`

#### New Features
- Added `debug()` and the debug system ([read the doc](doc/11_advance/14_debug_system.md)) (GH-112)
- Added an interactive builtin shell (command `pashmak @shell`) (GH-113)
- Added the function `load_so()` for loading shared objects (DLLs) ([read the doc](doc/11_advance/15_loading_dll.md)) (GH-117)
- Added an error hiding feature ([read the doc](doc/03_try_endtry/02_hiding_errors.md)) (GH-122)

#### Changes
- Renamed the `section` command to `label`; `section` still works and is backward compatible (GH-110)
- Some optimizations in builtin modules and program bootstrap speed (GH-111)
- Improved the base structure of the lexer and parser, and optimizations in speed (GH-118)
- Some changes in error rendering style (GH-120)
- Improved error rendering in the web environment (GH-121)

#### Bug Fixes
- Fixed the invalid line number bug in the parser and while raising errors (GH-119)

## 0.7.4 (2021-02-24)

#### Changes
- Changed `-` to `<stdin>` as the file name while reading code from stdin

## 0.7.3 (2021-2-22)

#### New Features
- Handle `return` in the importing system via `import()` ([read the doc](doc/05_importing/02_return_value.md)) (GH-109)

#### Changes
- Changed the string of classes from the default to `<class 'NameOfClass'>` (GH-108)

#### Bug Fixes
- Fixed the `typeof()` bug when checking the type of an object from a class (GH-108)

## 0.7.2 (2021-2-16)

#### New Features
- Added a docstring for the function `py_load_module`

#### Bug Fixes
- Fixed the bug where shutdown events did not run while using `exit()` (GH-105)
- Fixed the multiline syntax bug while writing empty lines

## 0.7.1 (2021-2-10)

#### Changes
- Some optimizations in builtin modules

#### Removed
- Removed `shuffle`, `sample`, `triangular`, `choices` and `uniform` from module `random`

## 0.7 (2021-02-09)

#### New Features
- Added the `import_run` and `import_run_once` functions (GH-84)
- Added a cli feature to run modules (GH-84)
- Added new functions to the module `string` (GH-86)
- Added the Python `mimetypes` module (GH-92)
- Added the `gget` function (GH-92)
- Added the `pashmakexe` variable to the module `sys` (GH-92)
- Added a small internal web server for Pashmak in the module `web.server` (GH-92)
- Added the base of the web development features for the backend with Pashmak (module `@web`) (GH-92)
- Added a cli behavior for the `time` module to show the current time (GH-89)
- Added the `null` keyword as an alias for `None` (GH-90)
- Moved the `pit(pashmhtml)` engine from an external library to a builtin module (GH-85)
- Added the shutdown event system and the function `register_shutdown()` (GH-91)
- Added the `re` Python regex library
- Added the function `die`
- Moved `pashmiler` from an external library to a builtin module and renamed it to `compiler` (GH-93)
- Added the **Docstring** system (GH-94)
- Added the `set` and `get` functions
- Added the name define system and the `define`, `is_defined`, `undefine`, `all_defines` and `redefine` functions
- Added `true` and `false` aliases for `True` and `False` keywords
- Added multiple arguments for functions (GH-95)
- Added keyword arguments for functions (GH-95)
- Added typed arguments for functions (GH-95)
- Added the return type system for functions (GH-99)
- Added some aliases for datatypes, `string` for `str`, `integer` for `int`, `array` for `list`
- Added the Core Developer guide to the documentation (GH-96)
- Added the function `clone()` for copying objects (GH-97)
- Added a message argument for the function `read()`
- Added the Python `pickle` module
- Added the function `match()` (GH-100)
- Added the function `py_load_module` (GH-101)
- Added the Python `io` module

#### Changes

- Some optimizations in multiline syntax
- Changed the syntax of the `free` and `isset` functions
- Fixed some bugs and some optimizations in eval (GH-95)
- Changed the RecursionError message

#### Bug Fixes
- Fixed the cached `$__ismain__` bug while directly running a file on the command line
- Fixed the import command bug while writing something like `import(somefunc())`
- Fixed a small problem in error rendering
- Fixed a bug in the class property setting syntax while running `$obj-><some-existing-name> = ...`
- Fixed a syntax bug while using variables alongside `:`

#### Removed

- Removed the unused function `required`
- Removed the `format_args` function

## 0.6.8 (2021-1-17)

#### Bug Fixes
- Fixed a bug in module importing environment conflicts
- Fixed a bug in the `import_once`, `import_run` and `import_run_once` functions
- Fixed the bug when calling a function in a class block
- Fixed the bug with the `$__dir__`, `$__file__` and `$__ismain__` variables in a namespace block

## 0.6.7 (2021-1-15)

#### Bug Fixes
- Fixed the class property setting syntax bug (GH-88)
- Fixed a bug in variable frame handling

## 0.6.6 (2021-1-11)

#### Bug Fixes
- Fixed a bug in the `$__ismain__` variable for builtin modules

## 0.6.5 (2021-1-11)

#### New Features
- Added the module `string` (GH-82)

#### Bug Fixes
- Fixed a bug in the module path system related to `$__dir__` and `$__file__`

## 0.6.4 (2021-1-10)

#### New Features
- Added importing subdirectories/files in modules loaded from the module path system (GH-80)

#### Bug Fixes
- Fixed the import directory bug (GH-79)

#### Removed
- Removed the cli option `-m|--modules`

## 0.6.3 (2021-1-9)

#### Changes
- Some optimizations in the module importing system (GH-78)

#### Bug Fixes
- Fixed a bug in importing scripts related to file paths containing `"` or `'` (GH-78)
- Fixed the bug where `$__ismain__` was always True (GH-78)

## 0.6.2 (2021-1-7)

#### New Features
- Added `urllib` to the imported Python standard modules (GH-75)
- Added `platform`, `sqlite3.dump`, `sqlite3.dbapi2` to the imported Python standard modules
- Added `pashmak.zen()` (GH-77)

## 0.6.1 (2021-1-5)

#### Changes
- Also show the error type and message at the end of rendered error frames
- Imported the `sqlite3` Python module (GH-69)

#### Bug Fixes
- Fixed the bug where the $this variable existed while calling a static method in a class (GH-71)
- Fixed the try-endtry variable error handling bug (GH-73)
