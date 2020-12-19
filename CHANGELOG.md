# Pashmak Changelog

## 0.6, 0.6-beta3

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
- removed `$var = ^ command` syntax(use `$var = %{ command }%` instead of that)
- added general variable `$__ismain__`
- fixed a bug in function declaration syntax
- created `return` command for functions
- fixed a bug in `$__dir__` and `$__file__` variables in function

