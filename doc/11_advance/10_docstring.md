# Docstrings
Docstring is a system to write description for classes, functions and methods. This is something like comments,
but docstring is like a property and is accessible at runtime!

for example, we want to write some description for usage of a function. we can use comments:

```bash
# This function does something
# other line
# ...
func something()
    # ...
endfunc
```

But this comment is not touchable in the code and interpreter will ignore this. But docstring, is like a property.

Look at this example:

```bash
@doc "This function gets two numbers and returns sum of them\n\
\n\
Example:\n\
somefunc(2, 10) -> returns 12\n\
"
func calc_sum($a, $b)
    return $a + $b
endfunc
```

now, this description is accessible like a variable:

```bash
println(calc_sum->__docstring__)
```

output:

```
This function gets two numbers and returns sum of them

Example:
somefunc(2, 10) -> returns 12

```

This system is very helpful, specially while you are writing a library. you can write docstring to tell others
what does this function/class/method.

also you can use this for classes and methods:

```bash
@doc "a model for Person"
class Person

    @doc "this is a method"
    func some_method
    endfunc

endclass
```

general syntax, is that write `@doc` and a string on forward. also you can use multi line.

and the docstring is accessible with `__docstring__` property.
