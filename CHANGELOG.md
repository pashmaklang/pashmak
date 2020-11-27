# Pashmak Changelog

## next release

- fixed syntax removing more than 1 space bug. now `println "hello    world"` will print `hello    world`, not `hello world`

## 0.3 (2020-11-26)

- added cli `-r` option to run code from cli arguments
- added cli `-m|--modules` option to show list of modules
- added `/usr/lib/pashmak_modules` and `%HOME%/.local/lib/pashmak_modules` directories as default module paths
- added feature import scripts inside namespaces

## 0.2.3 (2020-11-26)

- fixed modules not not be included from module path bug

## 0.2.2 (2020-11-25)

- added an feature to multiple imports with `include`/`import` commands
- added `\#` to use `#` special character in code

## 0.2.1 (2020-11-24)

- fixed try-in-try bug in try-endtry system

## 0.2 (2020-11-24)

- added module path system
- added `$__file__` and `$__dir__` general variables
- raise error when namespace or function name contains `.` character

## 0.1.1 (2020-11-24)

- fixed an bug in section handling about calling functions inside an loop

## 0.1
first release!
