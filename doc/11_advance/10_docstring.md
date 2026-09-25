# Docstrings
A docstring lets you write descriptions for classes, functions, and methods. Like a comment, it documents code,
but it is stored as a property and is accessible at runtime.

For example, we can use comments to describe how to use a function:

```bash
# This function does something
# other line
# ...
func something()
    # ...
endfunc
```

The interpreter ignores these comments at runtime. A docstring, on the other hand, is available as a property.

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

Now this description is accessible like a variable:

```bash
println(calc_sum->__docstring__)
```

output:

```
This function gets two numbers and returns sum of them

Example:
somefunc(2, 10) -> returns 12

```

This is useful when writing a library: you can use docstrings to explain what a function, class, or method does.

You can also use docstrings for classes and methods:

```bash
@doc "a model for Person"
class Person

    @doc "this is a method"
    func some_method
    endfunc

endclass
```

In general, write `@doc` followed by a string before the declaration. The string can span multiple lines.

The docstring is accessible through the `__docstring__` property.
