# Variables and Eval Structure
What is "eval"? An eval is an expression that operates on values such as integers and strings.

For example, `2 + 2` and `400*(20-10)` are evals. An eval is not limited to arithmetic: `"hello " + "world"` is also an eval. It can contain variables, as in `"Hello " + $name`, and function calls, as in `say_hello($name) + '.'`.

But how this eval is handled by Pashmak Core executor?

You can see the `parse_eval` function in the previous section about the lexer.
It takes a Pashmak eval string and **converts it to Python code**, which the executor then runs.

For example, `"Hello " + $name` will be converted to `"Hello " + self.get_var('name')`. The `$name` was replaced with `self.get_var('name')`.

This also handles functions and classes. For example, `some_func($name)` is converted to `self.functions["some_func"](self.get_var('name'))`.

The generated Python code is run using Python's `eval` function **inside a `program.Program` object**. This means that `self` refers to the program object in `src/core/program.py`.

The `program.Program` object has an `eval` method. It takes code, converts it to Python using the lexer, and runs the result.

The program object also has an important method named `get_var`. It takes a variable name and returns its value, or raises a variable error if the variable does not exist.

You will learn more about `program.Program` object features.
