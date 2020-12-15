# Pashmak Changelog

## 0.6, 0.6-beta1

- created **Class** system
- change default `RuntimeError` name to the real python exception name in exception system
- created consts system
- some optimizations in mem eval parser
- added a feature to use mem symbol `^` in eval, now you can run `my_function ^ + ' something else'`
- added syntax feature to put `()` in function call syntax, for example `println("hello world")` or `my_func(1, 2)`
- some optimizations in interpreter code
- added `if..elif..else` statement
- deleted `loop` and `while` functions
- deleted `out`, `fread`, `include` and `fwrite` commands because they was very low level and are not needed
- fixed a bug in `eval` function
- fixed a bug in module path system
- added `import_once` function
- added a syntax to handle dictonary item value assigning, now we can run `$my_dict["item"] = "value"`
- fixed some bugs in error raising system
- fixed lot of interpreter internal bugs and some optimizations
- added inline function calling feature, for example `println %{ my_func_or_command %{ another_command_as_arg }% }%`
- removed `$var = ^ command` syntax

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
