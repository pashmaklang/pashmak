# Pashmak Changelog

## next release

#### New Features
- Added command `clear` for shell (GH-123)

## 0.8 (2021-2-28)

#### NOTE: This release is fully backward compatible with `0.7`

#### New Features
- Added `debug()` and debug system ([read the doc](doc/11_advance/14_debug_system.md)) (GH-112)
- Added interactive builtin shell (command `pashmak @shell`) (GH-113)
- Added function `load_so()` for loading shared objects (DLLs), ([read the doc](doc/11_advance/15_loading_dll.md)) (GH-117)
- Added error hiding feature ([read the doc](doc/03_try_endtry/02_hiding_errors.md)) (GH-122)

#### Changes
- Renamed `section` command to `label`, still `section` works and is backward compatible (GH-110)
- Some optimizations in builtin modules and program bootstrap speed (GH-111)
- Improve base structure of lexer and parser and optimizations in speed (GH-118)
- Some changes in error rendering style (GH-120)
- Improve error rendering in web environment (GH-121)

#### Bug Fixes
- Fixed invalid line number bug in parser and while raising errors (GH-119)

## 0.7.4 (2021-02-24)

#### Changes
- Changed `-` to `<stdin>` as file name while reading code from stdin

## 0.7.3 (2021-2-22)

#### New Features
- Handle `return` in importing system by `import()` ([read the doc](doc/05_importing/02_return_value.md)) (GH-109)

#### Changes
- Changed string of classes from default to `<class 'NameOfClass'>` (GH-108)

#### Bug Fixes
- Fixed `typeof()` bug when checking type of a object from a class (GH-108)

## 0.7.2 (2021-2-16)

#### New Features
- Added docstring for function `py_load_module`

#### Bug Fixes
- Fixed shutdown events not running while using `exit()` bug (GH-105)
- Fixed mulltiline syntax bug white writing empty lines

## 0.7.1 (2021-2-10)

#### Changes
- Some optimizations in builtin modules

#### Removed
- Removed `shuffle`, `sample`, `triangular`, `choices` and `uniform` from module `random`

## 0.7 (2021-02-09)

#### New Features
- Added `import_run` and `import_run_once` functions (GH-84)
- Added cli feature to run modules (GH-84)
- Added new functions to module `string` (GH-86)
- Added python `mimetypes` module (GH-92)
- Added `gget` function (GH-92)
- Added `pashmakexe` variable to module `sys` (GH-92)
- Added a small internal web server for pashmak in module `web.server` (GH-92)
- Added base of web development features for backend with pashmak (module `@web`) (GH-92)
- Added a cli behavior for `time` module to show current time (GH-89)
- Added `null` keyword as a alias for `None` (GH-90)
- Moved `pit(pashmhtml)` engine from a external library to a builtin module (GH-85)
- Added shutdown event system and function `register_shutdown()` (GH-91)
- Added `re` python regex library
- Added function `die`
- Moved `pashmiler` from a external library to a builtin module and renamed to `compiler` (GH-93)
- Added **Docstring** system (GH-94)
- Added `set` and `get` functions
- Added name define system and `define`, `is_defined`, `undefine`, `all_defines` and `redefine` functions
- Added `true` and `false` aliases for `True` and `False` keywords
- Added multiple arguments for functions (GH-95)
- Added keyword arguments for functions (GH-95)
- Added typed arguments for functions (GH-95)
- Added return type system for functions (GH-99)
- Added some aliases for datatypes, `string` for `str`, `integer` for `int`, `array` for `list`
- Added Core Developer guide to Documentation (GH-96)
- Added function `clone()` for copying objects (GH-97)
- Added message argument for function `read()`
- Added python `pickle` module
- Added function `match()` (GH-100)
- Added function `py_load_module` (GH-101)
- Added python `io` module

#### Changes

- Some optimizations in multiline syntax
- Changed syntax of `free` and `isset` functions
- Fixed some bugs and some optimizations in eval (GH-95)
- Changed RecursionError message

#### Bug Fixes
- Fixed bug cached `$__ismain__` while directly running a file in command line
- Fixed import command bug while writing something like `import(somefunc())`
- Fixed a small problem in error rendering
- Fixed a bug in class property setting syntax, while running `$obj-><some-exists-name> = ...`
- Fixed syntax bug while using variables alongside `:`

#### Removed

- Removed unused function `required`
- Removed `format_args` function

## 0.6.8 (2021-1-17)

#### Bug Fixes
- Fixed a bug in importing modules environment conflicting
- Fixed a bug in `import_once`, `import_run` and `import_run_once` functions
- Fixed calling function in class block bug
- Fixed `$__dir__`, `$__file__` and `$__ismain__` variables bug in namespace block

## 0.6.7 (2021-1-15)

#### Bug Fixes
- Fixed class property setting syntax bug (GH-88)
- Fixed a bug in variable frame handling

## 0.6.6 (2021-1-11)

#### Bug Fixes
- Fixed a bug in `$__ismain__` variable for builtin modules

## 0.6.5 (2021-1-11)

#### New Features
- Added module `string` (GH-82)

#### Bug Fixes
- Fixed a bug in module path system about `$__dir__` and `$__file__`

## 0.6.4 (2021-1-10)

#### New Features
- Added importing sub directories/files in modules loaded from module path system (GH-80)

#### Bug Fixes
- Fixed import directory bug (GH-79)

#### Removed
- Removed cli option `-m|--modules`

## 0.6.3 (2021-1-9)

#### Changes
- Some optimizations in module importing system (GH-78)

#### Bug Fixes
- Fixed a bug in importing scripts related to file path contains `"` or `'` (GH-78)
- Fixed `$__ismain__` alwasy is True bug (GH-78)

## 0.6.2 (2021-1-7)

#### New Features
- Added `urllib` to imported python standard modules (GH-75)
- Added `platform`, `sqlite3.dump`, `sqlite3.dbapi2` to imported python standard modules
- Added `pashmak.zen()` (GH-77)

## 0.6.1 (2021-1-5)

#### Changes
- Also show error type and message in end of rendered error frames
- Imported `sqlite3` python module (GH-69)

#### Bug Fixes
- $this variable exists while calling static method bug in class is fixed (GH-71)
- Fixed try-endtry variable error handling bug (GH-73)
