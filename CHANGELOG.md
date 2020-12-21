# Pashmak Changelog

## 0.6, 0.6-beta5

#### New features
- added **Class** system
- added consts system
- added a feature to use mem symbol `^` in eval, now you can run `my_function ^ + ' something else'`
- added syntax feature to put `()` in function call syntax, for example `println("hello world")` or `my_func(1, 2)`
- added `if..elif..else` statement
- added `return` command for functions
- added `import_once` function
- added a syntax to handle dictonary item value assigning, now we can run `$my_dict["item"] = "value"`
- added inline function calling feature, for example `println %{ my_func_or_command %{ another_command_as_arg }% }%`
- added general variable `$__ismain__`
- added **Jit** compiler

#### Bug Fixes
- fixed a bug in `eval` function
- fixed a bug in module path system
- fixed some bugs in error raising system
- fixed lot of interpreter internal bugs and some optimizations
- fixed a bug in function declaration syntax
- fixed a bug in `$__dir__` and `$__file__` variables in function

#### Removed
- deleted `loop` and `while` functions
- deleted `out`, `fread`, `include` and `fwrite` commands because they was very low level and are not needed
- deleted `$var = ^ command` syntax(use `$var = %{ command }%` instead of that)

#### Other changes
- change default `RuntimeError` name to the real python exception name in exception system
- some optimizations in mem eval parser
- some optimizations in interpreter code
