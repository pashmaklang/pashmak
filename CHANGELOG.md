# Pashmak Changelog

## (0.6.x) next release

#### Bug Fixes
- fixed a bug in importing modules environment conflicting
- fixed a bug in `import_once`, `import_run` and `import_run_once` functions
- fixed calling function in class block bug
- fixed `$__dir__`, `$__file__` and `$__ismain__` variables bug in namespace block

## 0.6.7 (2021-1-15)

#### Bug Fixes
- fixed class property setting syntax bug (GH-88)
- fixed a bug in variable frame handling

## 0.6.6 (2021-1-11)

#### Bug Fixes
- fixed a bug in `$__ismain__` variable for builtin modules

## 0.6.5 (2021-1-11)

#### New Features
- added module `string` (GH-82)

#### Bug Fixes
- fixed a bug in module path system about `$__dir__` and `$__file__`

## 0.6.4 (2021-1-10)

#### Bug Fixes
- fixed import directory bug (GH-79)

#### New Features
- added importing sub directories/files in modules loaded from module path system (GH-80)

#### Removed
- removed cli option `-m|--modules`

## 0.6.3 (2021-1-9)

#### Changes
- some optimizations in module importing system (GH-78)

#### Bug Fixes
- fixed a bug in importing scripts related to file path contains `"` or `'` (GH-78)
- fixed `$__ismain__` alwasy is True bug (GH-78)

## 0.6.2 (2021-1-7)

#### New Features
- added `urllib` to imported python standard modules (GH-75)
- added `platform`, `sqlite3.dump`, `sqlite3.dbapi2` to imported python standard modules
- added `pashmak.zen()` (GH-77)

## 0.6.1 (2021-1-5)

#### Changes
- also show error type and message in end of rendered error frames
- imported `sqlite3` python module (GH-69)

#### Bug Fixes
- $this variable exists while calling static method bug in class is fixed (GH-71)
- fixed try-endtry variable error handling bug (GH-73)

