# Class and Function Structure

## Functions
The file `src/core/function.py` contains a class named `Function`. Pashmak functions are instances of this class, stored in the `functions` property (`self.functions`) of `program.Program`.

This property is a list of `Function` objects.

The `Function` class, is callable.

When you write:

```bash
func somefunc()
	# ...
endfunc
```

You are opening a function block, the `func` keyword will run `src/core/builtin_functions.py`'s `run_func`. This builtin command opens a function block. The function block opening and closing is handled by `self.current_func` property in program object.

Then, while function block is open, commands inside the function will be added to body of function.

The function is accessible through `self.functions['func_name']`.
Calling `self.functions['func_name']()` runs it. During evaluation, function names are replaced with calls of this form.

Function object properties:
- `body`: Body of the function as a list
- `args`: Arguments of function as a list: `[['$name'], ['string $msg'], ['$age', '30(default)']]`

## Classes
Classes work much like functions. They are stored in `self.classes`, handled by eval, and implemented in `src/core/class_system.py`.

The class system has two main Python classes: `Class` and `ClassObject`. `Class` represents a class definition, and `ClassObject` represents an instance created from a class.

Both `Class` and `ClassObject` have `__props__` and `__methods__` properties. `__props__` stores class properties, and `__methods__` stores methods as a list of `Function` objects.

`Class` also has a `__call__` method, which creates and returns a new object. For example, calling a class named `Person` with `Person()` returns a `ClassObject` instance of `Person`. The `__call__` method handles this object creation.

##### NOTE: this guide is only a introduction to source code, for better understanding, read the source code of above sections.
