# Pashmak Changelog

## (0.7-alpha1) next release

#### New Features
- added `import_run` and `import_run_once` functions (GH-84)
- added cli feature to run modules (GH-84)
- added new functions to module `string` (GH-86)
- added python `mimetypes` module (GH-92)
- added `gget` function (GH-92)
- added `pashmakexe` variable to module `sys` (GH-92)
- added a small internal web server for pashmak in module `webserver` (GH-92)
- added base of web development features for backend with pashmak (GH-92)
- added a cli behavior for `time` module to show current time (GH-89)
- added `null` keyword as a alias for `None` (GH-90)
- moved `tengine(pashmhtml)` engine from a external library to a builtin module (GH-85)
- added shutdown event system and function `register_shutdown()` (GH-91)
- added `re` python regex library
- added function `die`
- moved `pashmiler` from a external library to a builtin module and renamed to `compiler` (GH-93)

#### Bug Fixes
- fixed bug cached `$__ismain__` while directly running a file in command line

## (0.6.x) next release

#### Bug Fixes
- fixed a bug in importing modules environment conflicting
- fixed a bug in `import_once`, `import_run` and `import_run_once` functions

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

