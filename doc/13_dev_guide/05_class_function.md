# Class and Function Structure

## Functions
there is a file in `src/core/function.py`. This file contains a class named `Function`. Actually, Pashmak functions are a instance from this class! They are stored at `program.Program`'s `functions` property.(`self.functions`).

Means, that is a list from `Function` objects.

The `Function` class, is callable.

When you write:

```bash
func somefunc()
	# ...
endfunc
```

You are opening a function block, the `func` keyword will run `src/core/builtin_functions.py`'s `run_func`. This builtin command opens a function block. The function block opening and closing is handled by `self.current_func` property in program object.

Then, while function block is open, commands inside the function will be added to body of function.

The function will be accessible in `self.functions['func_name']`.
Means, `self.functions['func_name']()` runs the function. in the Eval process, function names will be replaced with `self.functions['func_name']()`.

Function object properties:
- `body`: Body of the function as a list
- `args`: Arguments of function as a list: `[['$name'], ['str $msg'], ['$age', '30(default)']]`

## Classes
The class is exactly like function. They are stored at `self.classes`, will be handled by eval, and the code is in `src/core/class_system.py`.

Class system has 2 main Python classes: `Class` and `ClassObject`. The `Class` is the defined class, and the `ClassObject` is the Initiated object from a class.

The `Class` and `ClassObject`, have `__props__` and `__methods__` properties. the `__props__` stores properties of class and `__methods__` stores methods of class, this is a list from `Function` object.

Also `Class` has a `__call__` method. This will make a new object and returns this. for example, we have a class named `Person`, when we call it using `Person()`, the output is a `ClassObject` object from type of that class(Person). so, the `__call__` handles object initiation.

##### NOTE: this guide is only a introduction to source code, for better understanding, read the source code of above sections.

