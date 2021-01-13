# Pashmak Changelog

## (0.6.7) next release

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

