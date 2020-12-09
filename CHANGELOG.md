# Pashmak Changelog

## next release

- removed `loop` and `while` functions
- created **Structs** system
- change default `RuntimeError` name to the real python exception name is exception system

## 0.5.4 (2020-12-6)

- fixed section system loop bug

## 0.5.3 (2020-12-6)

- fixed `$__file__` and `$__dir__` variables bug in windows

## 0.5.2 (2020-12-5)

- fixed namespace bug cannot using variables from another namespace inside a namespace

## 0.5.1 (2020-12-5)

- fixed importing variables bug, now imported variables are accessible from outside
- moved `$pashmakinfo` variable to `sys` module, now is `$sys.pashmakinfo`

## 0.5 (2020-12-2)

- added `sys` internal module and `sys.path` to manage module paths
- changed error raiser to show file and line number of code in error rendering
- changed import command to import modules without quotes. for example `import @hash`. stil you can use quotes.
- fixed an bug in module bootstraper, now the `PASHMAKPATH` environment variable has default empty value

## 0.4 (2020-12-1)

- added new internal module `test` contains assertion functions
- added a feature to module path system to import directories as `__init__.pashm` of them
- fixed pashamk cli signal handling

## 0.3.1 (2020-11-27)

- fixed syntax removing more than 1 space bug. now 'println "hello&nbsp;&nbsp;&nbsp;&nbsp;world"' will print "hello&nbsp;&nbsp;&nbsp;&nbsp;world", not `hello world`
- fixed bug in `$var = ^ <command>` syntax while using it in loop

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
