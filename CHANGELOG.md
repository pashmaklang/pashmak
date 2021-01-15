# Pashmak Changelog

## (0.7-alpha0) next release

- added `import_run` and `import_run_once` functions (GH-84)
- added cli feature to run modules (GH-84)
- moved `tengine(pashmhtml)` engine from a external library to a builtin module (GH-85)
- added new functions to module `string` (GH-86)
- fixed bug cached `$__ismain__` while directly running a file in command line
- added python `mimetypes` module
- added `gget` function
- added `pashmakexe` variable to module `sys`
- added a small internal web server for pashmak in module `webserver`
- added base of web development features for backend with pashmak
- added a cli behavior for `time` module to show current time

## (0.6.7) next release

- fixed class property setting syntax bug (GH-88)
- fixed a bug in variable frame handling

## 0.6.6 (2021-1-11)

- fixed a bug in `$__ismain__` variable for builtin modules

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

