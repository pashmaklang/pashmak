# Variables and Eval Structure
What is "Eval"? The eval, is a calculation on variables(int, str,...).

For example, `2 + 2` is a eval. `400*(20-10)` is a eval. This is not only math eval. For example, `"hello " + "world"` is a eval. also this can contain variables, `"Hello " + $name` is a eval. Also this can contain function call, `say_hello($name) + '.'` is a eval.

But how this eval is handled by Pashmak Core executor?

You can see `parse_eval` function in prevoius part in lexer.
This function gets a Pashmak eval string and **Converts it to python code**. Then, that python code will be ran by executor.

For example, `"Hello " + $name` will be converted to `"Hello " + self.get_var('name')`. The `$name` was replaced with `self.get_var('name')`.

Also this handles functions and classes. for example `some_func($name)` will be converted to `self.functions["some_func"](self.get_var('name'))`.

The output Python code will be ran using Python's `eval` function **Inside program.Program object**, means that the `self` points to program object(`src/core/program.py`).

There is a method named `eval` in `program.Program` object, this method gets code and converts that to python code using lexer, then, runs that as a python code.

There is a important method named `get_var` in program object. This method gets name of a variable and returns value of that, but if variable does not exists, raises variable error.

You will learn more about `program.Program` object features.

